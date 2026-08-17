"""Build the published dataset from real IRS 990-PF filings.

Replaces build_sample.py. Emits the identical JSON contract (SPEC §2.6), so
nothing downstream changes.

Run: python3 standing/build_real.py [cohort_size] [--incremental]

Two modes:

  full (default)  Rebuild every foundation in the cohort from source. Correct
                  but expensive: ~220KB of XML per filing-year, so a cohort of
                  4,000 re-fetches several GB even when nothing has changed.

  --incremental   Reuse the committed JSON for any foundation whose filing
                  index has not advanced since it was built, and fetch only
                  the ranks that are genuinely new. Peer medians are always
                  recomputed across the whole union, because they are a
                  property of the cohort rather than of one filer — growing
                  the cohort legitimately moves the comparison under
                  already-published pages, and that change has to be visible
                  rather than silent. checks/expansion_diff.py reports it.

`computed_at` is stamped only on foundations actually rebuilt. A reused figure
keeps the date it was really computed on; refreshing it would misdate the work.
"""

from __future__ import annotations

import collections
import csv
import datetime
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
MISSES = os.path.join(HERE, "data", "build_misses.json")

TODAY = datetime.date.today()
CURRENT_YEAR = TODAY.year
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
        "index_max_year": max(years),
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


def load_existing() -> dict[str, dict]:
    """Committed foundation docs, keyed by EIN.

    These ship with the repo, which is what makes incremental builds possible
    at all — the sandbox starts with no XML cache, so anything not already
    committed has to be re-fetched from source.
    """
    out: dict[str, dict] = {}
    if not os.path.isdir(OUT_DIR):
        return out
    for fn in os.listdir(OUT_DIR):
        if not fn.endswith(".json"):
            continue
        with open(os.path.join(OUT_DIR, fn), encoding="utf-8") as fh:
            doc = json.load(fh)
        out[doc["ein"]] = doc
    return out


def is_current(doc: dict, index_max_year: int) -> bool:
    """Whether a committed doc still reflects everything the index offers.

    Compares against the index high-water mark recorded at build time, not
    against the years actually parsed. A filing that was skipped (fetch
    failure, over the grant ceiling) would otherwise leave years_filed
    permanently short of the index and force a rebuild on every single run.
    Docs written before this field existed have no mark and rebuild once.
    """
    seen = doc.get("provenance", {}).get("index_max_year")
    return seen is not None and seen >= index_max_year


def assemble(b: dict, slug: str) -> dict:
    """One built foundation → the SPEC §2.6 document, minus peer medians.

    Peer medians are added later, in one pass over the whole cohort, because
    they depend on every other foundation in the same asset band.
    """
    m = b["m"]
    rate = m.metrics["new_grantee_rate_pooled"] if m.metrics else None
    return {
        "ein": b["ein"], "slug": slug, "name": b["name"], "state": b["state"],
        "asset_band": asset_band(b["assets"]), "assets_fmv": b["assets"],
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
            "index_max_year": b["index_max_year"],
            "computed_at": TODAY.isoformat(),
            "next_recompute_expected": (TODAY + datetime.timedelta(days=90)).isoformat(),
        },
    }


def apply_peer_medians(docs: list[dict]) -> None:
    """Set each publishable foundation's peer median, excluding itself.

    Recomputed across the full cohort on every run, incremental or not. A
    peer median is a fact about the comparison set, so adding foundations
    genuinely changes it for pages already published — expansion_diff.py
    exists to make that movement visible rather than letting it ship quietly.
    """
    bands = collections.defaultdict(list)
    for d in docs:
        if d["quality"]["publishable"] and d["metrics"]:
            bands[d["asset_band"]].append(d["metrics"]["new_grantee_rate_pooled"])

    for d in docs:
        m = d["metrics"]
        if not (d["quality"]["publishable"] and m):
            continue
        for k in ("peer_median_new_grantee_rate", "peer_basis", "peer_cell_size"):
            m.pop(k, None)
        peers = list(bands.get(d["asset_band"], []))
        if len(peers) < 3:
            continue
        peers.remove(m["new_grantee_rate_pooled"])
        if peers:
            m["peer_median_new_grantee_rate"] = round(statistics.median(peers), 4)
            m["peer_basis"] = "assets"
            m["peer_cell_size"] = len(peers)


def index_row(d: dict) -> dict:
    m = d["metrics"] or {}
    return {
        "ein": d["ein"], "slug": d["slug"], "name": d["name"], "state": d["state"] or "",
        "asset_band": d["asset_band"], "publishable": d["quality"]["publishable"],
        "status_band": d["status_band"],
        "match_rate": round(d["quality"]["match_rate"], 4),
        "new_latest": m.get("new_grantee_count_latest"),
        "total_latest": m.get("total_grantee_count_latest"),
        "rate_pooled": m.get("new_grantee_rate_pooled"),
        "peer_median": m.get("peer_median_new_grantee_rate"),
        "median_grant": (m.get("grant_sizes") or {}).get("median"),
        "lookback": m.get("lookback_years_used"),
        "latest_year": d["window"]["latest_eligible_year"],
        "gate_failures": d["quality"]["gate_failures"],
        "accepts_unsolicited": d["self_reported"]["accepts_unsolicited"],
        "drift_review_flag": d["quality"].get("drift_review_flag"),
        "singleton_share": d["quality"].get("singleton_cluster_share"),
    }


def main() -> int:
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    incremental = "--incremental" in sys.argv
    n = int(argv[0]) if argv else 250

    cohort = load_cohort(n)
    print(f"cohort: {len(cohort)} foundations (4+ filing years, "
          f"${MIN_ASSETS/1e6:.0f}M-${MAX_ASSETS/1e6:.0f}M)")

    existing = load_existing()

    # Foundations that were tried and yielded nothing publishable — fewer than
    # four parseable filings, no grant records. Without this, every run
    # re-fetches the whole tail of failures forever. Recorded with the index
    # mark that produced the miss, so a later filing retries it on its own.
    misses: dict[str, int] = {}
    if os.path.exists(MISSES):
        with open(MISSES, encoding="utf-8") as fh:
            misses = json.load(fh).get("misses", {})

    reuse, to_build, skipped = [], [], 0
    for ein, years in cohort:
        imy = max(years)
        doc = existing.get(ein)
        if incremental and doc and is_current(doc, imy):
            reuse.append(doc)
        elif incremental and doc is None and misses.get(ein, -1) >= imy:
            skipped += 1
        else:
            to_build.append((ein, years))

    if incremental:
        print(f"incremental: reusing {len(reuse)}, skipping {skipped} known misses, "
              f"fetching {len(to_build)}")

    built_docs = []
    registry = {}
    if os.path.exists(SLUGS):
        with open(SLUGS) as fh:
            registry = json.load(fh)
    used = {v["slug"] for v in registry.values()}

    results = []
    if to_build:
        with ThreadPoolExecutor(max_workers=12) as ex:
            for i, res in enumerate(ex.map(build_one, to_build), 1):
                if res:
                    results.append(res)
                if i % 25 == 0:
                    print(f"  {i}/{len(to_build)} processed, {len(results)} usable", flush=True)

    # Slug assignment is serial and name-ordered so a collision suffix never
    # depends on which thread finished first — SPEC §2.6.1 immutability.
    for b in sorted(results, key=lambda r: (r["name"], r["ein"])):
        if b["ein"] in registry:
            slug = registry[b["ein"]]["slug"]
        else:
            slug = slugify(b["name"])
            if slug in used:
                slug = f"{slug}-{b['ein'][-4:]}"
            registry[b["ein"]] = {"slug": slug, "superseded": []}
            used.add(slug)
        built_docs.append(assemble(b, slug))

    docs = reuse + built_docs
    print(f"built: {len(built_docs)} new, {len(docs)} total")

    apply_peer_medians(docs)

    os.makedirs(OUT_DIR, exist_ok=True)
    keep = {d["ein"] for d in docs}
    for f in os.listdir(OUT_DIR):
        if f.endswith(".json") and f[:-5] not in keep:
            os.remove(os.path.join(OUT_DIR, f))
    for d in docs:
        with open(os.path.join(OUT_DIR, f"{d['ein']}.json"), "w") as fh:
            json.dump(d, fh, indent=2, sort_keys=True)
            fh.write("\n")

    with open(SLUGS, "w") as fh:
        json.dump(registry, fh, indent=2, sort_keys=True)
        fh.write("\n")

    produced = {b["ein"] for b in results}
    for ein, years in to_build:
        if ein not in produced:
            misses[ein] = max(years)
    for ein in list(misses):
        if ein in keep:            # started filing again — no longer a miss
            del misses[ein]
    with open(MISSES, "w") as fh:
        json.dump({"note": "cohort members that yielded no publishable document, "
                           "with the filing-index mark that produced the miss",
                   "misses": misses}, fh, indent=2, sort_keys=True)
        fh.write("\n")

    index = sorted((index_row(d) for d in docs), key=lambda r: r["name"])
    with open(os.path.join(HERE, "data", "index.json"), "w") as fh:
        json.dump({
            "generated": TODAY.isoformat(),
            "as_of_fiscal_year": max((d["latest_year"] or 0) for d in index) if index else None,
            "synthetic": False,
            "source": "IRS Form 990-PF via GivingTuesday Data Lake",
            "cohort_rank_depth": n,
            "count": len(index),
            "foundations": index,
        }, fh, indent=2, sort_keys=True)
        fh.write("\n")

    pub = sum(1 for d in index if d["publishable"])
    rates = [d["rate_pooled"] for d in index if d["rate_pooled"] is not None]
    mrs = sorted(d["match_rate"] for d in index)
    print(f"\npublished {len(index)} ({pub} with a comparison, {len(index)-pub} gated)")
    if rates:
        print(f"new-grantee rate  median {statistics.median(rates):.3f}  "
              f"min {min(rates):.3f}  max {max(rates):.3f}")
    if mrs:
        print(f"match rate        median {statistics.median(mrs):.3f}  "
              f"p10 {mrs[len(mrs)//10]:.3f}  below 0.85: "
              f"{sum(1 for m in mrs if m < 0.85)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
