"""Build the published dataset from real IRS 990-PF filings.

Replaces build_sample.py. Emits the identical JSON contract (SPEC §2.6), so
nothing downstream changes.

Run: python3 standing/build_real.py [cohort_size]
"""

from __future__ import annotations

import collections
import csv
import json
import os
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "pipeline"))

from extract import fetch, parse  # noqa: E402
from metrics import compute, status_band  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "data", "pf_index.csv")
OUT_DIR = os.path.join(HERE, "data", "foundations")
CACHE = os.path.join(HERE, ".cache")
SLUGS = os.path.join(HERE, "data", "slug_registry.json")

CURRENT_YEAR = 2026
MIN_ASSETS, MAX_ASSETS = 1e7, 5e8
MAX_GRANTS_PER_FILING = 4000  # skip the handful of enormous filers


def slugify(name: str) -> str:
    s = "".join(c.lower() if c.isalnum() else "-" for c in name)
    while "--" in s:
        s = s.replace("--", "-")
    s = s.strip("-")
    if s.startswith("the-"):
        s = s[4:]
    return s[:60].rstrip("-") or "foundation"


def load_cohort(n: int) -> list[tuple[str, dict]]:
    by = collections.defaultdict(dict)
    with open(INDEX, encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            ty = r["TaxYear"]
            if ty.isdigit():
                by[r["EIN"].zfill(9)][int(ty)] = r

    def assets(v):
        try:
            return float(v[max(v)]["TotalAssetsBkEOY"] or 0)
        except (ValueError, KeyError):
            return 0.0

    elig = [(e, v) for e, v in by.items()
            if len(v) >= 4 and MIN_ASSETS <= assets(v) <= MAX_ASSETS]
    # Deterministic: largest first, then EIN.
    elig.sort(key=lambda kv: (-assets(kv[1]), kv[0]))
    return elig[:n]


def build_one(args):
    ein, years = args
    filings = []
    for yr in sorted(years):
        oid = years[yr]["ObjectId"]
        data = fetch(oid, cache_dir=CACHE)
        if not data:
            continue
        try:
            f = parse(data)
        except Exception:  # noqa: BLE001
            continue
        if f and len(f.records) <= MAX_GRANTS_PER_FILING:
            filings.append(f)
    if len(filings) < 4:
        return None

    # Dedup on (ein, tax_year), keeping the later period_end — SPEC §2.5.
    best: dict[int, object] = {}
    dupes = 0
    for f in filings:
        prev = best.get(f.tax_year)
        if prev is None:
            best[f.tax_year] = f
        else:
            dupes += 1
            if (f.period_end or "") > (prev.period_end or ""):
                best[f.tax_year] = f
    filings = [best[k] for k in sorted(best)]
    if len(filings) < 4:
        return None

    records = [r for f in filings for r in f.records]
    if not records:
        return None

    latest = filings[-1]
    m = compute(records, CURRENT_YEAR)

    # Recipient list for the latest compared year. "Who did they actually
    # fund" is the most persuasive thing on a foundation page — people
    # calibrate fit against organizations like themselves, not against a rate.
    recips = []
    ly = m.window.get("latest_eligible_year")
    if ly is not None and m.metrics:
        from resolve import resolve_filer
        clusters, _ = resolve_filer([r for r in records if r.tax_year in m.window["years_present"]])
        prior = set()
        for y in [y for y in m.window["years_present"] if y < ly][-3:]:
            for c in clusters:
                if any(x.tax_year == y for x in c.members):
                    prior.add(c.cluster_id)
        agg = {}
        for c in clusters:
            mine = [x for x in c.members if x.tax_year == ly and not x.ambiguous]
            if not mine:
                continue
            agg[c.cluster_id] = {
                "name": mine[0].recipient_name_raw,
                "amount": sum(x.amount or 0 for x in mine),
                "purpose": mine[0].purpose or "",
                "is_new": c.cluster_id not in prior,
            }
        recips = sorted(agg.values(), key=lambda r: -r["amount"])

    return {
        "ein": ein,
        "name": latest.name.title() if latest.name.isupper() else latest.name,
        "state": latest.state,
        "assets": latest.fmv_assets,
        "accepts_unsolicited": latest.accepts_unsolicited,
        "application_info_text": latest.application_info_text,
        "future_excluded": sum(f.future_grants_excluded for f in filings),
        "duplicate_filings_dropped": dupes,
        "years_filed": [f.tax_year for f in filings],
        "recipients": recips,
        "m": m,
    }


def asset_band(a: float | None) -> str:
    if not a:
        return "unknown"
    if a < 1e6:
        return "<1M"
    if a < 1e7:
        return "1-10M"
    if a < 1e8:
        return "10-100M"
    return "100M+"


def main() -> int:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 250
    cohort = load_cohort(n)
    print(f"cohort: {len(cohort)} foundations (4+ filing years, ${MIN_ASSETS/1e6:.0f}M-${MAX_ASSETS/1e6:.0f}M)")

    built = []
    with ThreadPoolExecutor(max_workers=12) as ex:
        for i, res in enumerate(ex.map(build_one, cohort), 1):
            if res:
                built.append(res)
            if i % 25 == 0:
                print(f"  {i}/{len(cohort)} processed, {len(built)} usable", flush=True)

    print(f"built: {len(built)}")

    # Peer medians over publishable foundations only, excluding self.
    bands = collections.defaultdict(list)
    for b in built:
        if b["m"].publishable and b["m"].metrics:
            bands[asset_band(b["assets"])].append(b["m"].metrics["new_grantee_rate_pooled"])

    os.makedirs(OUT_DIR, exist_ok=True)
    for f in os.listdir(OUT_DIR):
        if f.endswith(".json"):
            os.remove(os.path.join(OUT_DIR, f))

    registry = {}
    if os.path.exists(SLUGS):
        with open(SLUGS) as fh:
            registry = json.load(fh)

    used = {v["slug"] for v in registry.values()}
    index = []

    for b in built:
        m = b["m"]
        band = asset_band(b["assets"])
        peers = [r for r in bands.get(band, [])]
        if m.publishable and m.metrics and len(peers) >= 3:
            others = list(peers)
            others.remove(m.metrics["new_grantee_rate_pooled"])
            if others:
                m.metrics["peer_median_new_grantee_rate"] = round(statistics.median(others), 4)
                m.metrics["peer_basis"] = "assets"
                m.metrics["peer_cell_size"] = len(others)

        # Slug immutability — SPEC §2.6.1
        if b["ein"] in registry:
            slug = registry[b["ein"]]["slug"]
        else:
            slug = slugify(b["name"])
            if slug in used:
                slug = f"{slug}-{b['ein'][-4:]}"
            registry[b["ein"]] = {"slug": slug, "superseded": []}
            used.add(slug)

        rate = m.metrics["new_grantee_rate_pooled"] if m.metrics else None
        doc = {
            "ein": b["ein"], "slug": slug, "name": b["name"], "state": b["state"],
            "asset_band": band, "assets_fmv": b["assets"],
            "window": m.window,
            "quality": {**m.quality, "publishable": m.publishable,
                        "gate_failures": m.gate_failures,
                        "future_grants_excluded": b["future_excluded"],
                        "duplicate_filings_dropped": b["duplicate_filings_dropped"]},
            "metrics": m.metrics,
            "recipients_latest_year": b["recipients"],
            "status_band": status_band(rate if m.publishable else None),
            "self_reported": {
                "accepts_unsolicited": b["accepts_unsolicited"],
                "basis": "ApplicationSubmissionInfoGrp present in latest filing",
                "application_info_text": b["application_info_text"],
            },
            "provenance": {
                "source": "IRS Form 990-PF, Part XV (grants paid during the year)",
                "distribution": "GivingTuesday Data Lake mirror of the IRS e-file corpus",
                "as_of_fiscal_year": max(b["years_filed"]),
                "years_filed": b["years_filed"],
                "computed_at": "2026-08-03",
                "next_recompute_expected": "2026-11-01",
            },
        }
        with open(os.path.join(OUT_DIR, f"{b['ein']}.json"), "w") as fh:
            json.dump(doc, fh, indent=2, sort_keys=True)
            fh.write("\n")

        index.append({
            "ein": b["ein"], "slug": slug, "name": b["name"], "state": b["state"] or "",
            "asset_band": band, "publishable": m.publishable,
            "status_band": doc["status_band"],
            "match_rate": round(m.quality["match_rate"], 4),
            "new_latest": m.metrics["new_grantee_count_latest"] if m.metrics else None,
            "total_latest": m.metrics["total_grantee_count_latest"] if m.metrics else None,
            "rate_pooled": rate,
            "peer_median": m.metrics.get("peer_median_new_grantee_rate") if m.metrics else None,
            "median_grant": (m.metrics.get("grant_sizes") or {}).get("median") if m.metrics else None,
            "lookback": m.metrics.get("lookback_years_used") if m.metrics else None,
            "latest_year": m.window["latest_eligible_year"],
            "gate_failures": m.gate_failures,
            "accepts_unsolicited": b["accepts_unsolicited"],
            "drift_review_flag": m.quality.get("drift_review_flag"),
            "singleton_share": m.quality.get("singleton_cluster_share"),
        })

    with open(SLUGS, "w") as fh:
        json.dump(registry, fh, indent=2, sort_keys=True)
        fh.write("\n")

    index.sort(key=lambda d: d["name"])
    with open(os.path.join(HERE, "data", "index.json"), "w") as fh:
        json.dump({
            "generated": "2026-08-03",
            "as_of_fiscal_year": max((d["latest_year"] or 0) for d in index) if index else None,
            "synthetic": False,
            "source": "IRS Form 990-PF via GivingTuesday Data Lake",
            "count": len(index),
            "foundations": index,
        }, fh, indent=2, sort_keys=True)
        fh.write("\n")

    pub = sum(1 for d in index if d["publishable"])
    rates = [d["rate_pooled"] for d in index if d["rate_pooled"] is not None]
    mrs = [d["match_rate"] for d in index]
    print(f"\npublished {len(index)} ({pub} with a comparison, {len(index)-pub} gated)")
    if rates:
        print(f"new-grantee rate  median {statistics.median(rates):.3f}  "
              f"min {min(rates):.3f}  max {max(rates):.3f}")
    if mrs:
        mrs.sort()
        print(f"match rate        median {statistics.median(mrs):.3f}  "
              f"p10 {mrs[len(mrs)//10]:.3f}  below 0.85: "
              f"{sum(1 for m in mrs if m < 0.85)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
