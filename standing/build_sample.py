"""Generate the demonstration dataset — SPEC.md §2.6 output format.

The foundations here are INVENTED. Their filings are synthesised, then run
through the real pipeline (resolve.py, metrics.py), so every figure the tool
displays is genuinely computed rather than hand-written. That makes the demo
an end-to-end proof of the pipeline while the IRS sources are unreachable.

Replace this module with extract.py output to go live. Nothing downstream
changes — the JSON contract is identical.

Run: python3 standing/build_sample.py
"""

from __future__ import annotations

import json
import os
import random
import statistics
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "pipeline"))

from metrics import compute, status_band  # noqa: E402
from resolve import GrantRecord  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "data", "foundations")
CURRENT_YEAR = 2026
AS_OF = 2024
YEARS = [2020, 2021, 2022, 2023, 2024]

RECIPIENT_POOL = [
    "Riverbend Youth Collective", "Northgate Community Kitchen", "Halloway Arts Trust",
    "Селтик Learning Center".replace("Селтик", "Seltic"), "Marrow Street Clinic",
    "Fairhaven Housing Alliance", "Quarry Hill Conservancy", "Bellwether Legal Aid",
    "Copperline Literacy Project", "Ashford Youth Orchestra", "Tanner Creek Watershed Fund",
    "Willowmere Elder Services", "Draper Valley Food Bank", "Stonebridge Family Center",
    "Kestrel Ridge Land Trust", "Morningside Health Partners", "Lantern Hill Shelter",
    "Beacon Row Employment Services", "Cranmere Public Media", "Fenwick Museum of Craft",
]

# name, state, ntee, asset band, profile
PROFILES = [
    ("The Lindmark Trust", "MI", "P", "100M+", "entrenched"),
    ("Harrowgate Foundation", "MI", "P", "10-100M", "open"),
    ("Pemberton Family Foundation", "MI", "A", "10-100M", "moderate"),
    ("Ashby and Vale Foundation", "OH", "P", "1-10M", "small_grants"),
    ("The Quillon Fund", "MI", "S", "1-10M", "young"),
    ("Marchetti Family Trust", "IL", "A", "10-100M", "moderate"),
    ("Westover Foundation", "OH", "P", "100M+", "contracting"),
    ("The Bellhaven Fund", "MI", "P", "10-100M", "messy_names"),
    ("Calder Ridge Foundation", "IN", "C", "1-10M", "open"),
    ("Sandhurst Charitable Trust", "IL", "P", "100M+", "entrenched"),
    ("Kestrel Foundation", "MI", "S", "10-100M", "open"),
    ("Thornbury Family Fund", "OH", "A", "1-10M", "moderate"),
]

DRIFT = [
    lambda n: n + ", Inc.",
    lambda n: "The " + n,
    lambda n: n.upper(),
    lambda n: n,
]


def slugify(name: str) -> str:
    s = "".join(c.lower() if c.isalnum() else "-" for c in name)
    while "--" in s:
        s = s.replace("--", "-")
    s = s.strip("-")
    if s.startswith("the-"):
        s = s[4:]
    return s[:60].rstrip("-")


def synth(profile: str, state: str, rng: random.Random) -> list[GrantRecord]:
    """Build a plausible filing series for one profile."""
    recs: list[GrantRecord] = []
    core = RECIPIENT_POOL[: {"entrenched": 12, "contracting": 10}.get(profile, 8)]

    for year in YEARS:
        if profile == "young" and year < 2022:
            continue

        if profile == "entrenched":
            grantees = list(core)
            if year == 2024:
                grantees.append("Sable Point Institute")
            sizes = (150_000, 400_000)
        elif profile == "open":
            grantees = core[:6] + [f"{RECIPIENT_POOL[(year + i) % len(RECIPIENT_POOL)]} {chr(65 + i)}"
                                   for i in range(4)]
            sizes = (25_000, 150_000)
        elif profile == "moderate":
            grantees = core[:7] + [f"Newcomer {year} {i}" for i in range(2)]
            sizes = (20_000, 90_000)
        elif profile == "small_grants":
            grantees = core[:9] + [f"Micro Grantee {year}"]
            sizes = (4_000, 18_000)
        elif profile == "young":
            grantees = [f"Founding Partner {i}" for i in range(3)] + \
                       [f"Cohort {year} Member {i}" for i in range(4)]
            sizes = (30_000, 60_000)
        elif profile == "contracting":
            grantees = core[: max(4, 10 - (year - 2020))]
            sizes = (60_000, 200_000)
        elif profile == "messy_names":
            grantees = core[:8]
            sizes = (30_000, 120_000)
        else:
            grantees = core
            sizes = (20_000, 80_000)

        for g in grantees:
            name = g
            # Naming drift after a preparer change — the real-world condition
            # the match rate exists to measure.
            if profile == "messy_names" and year >= 2023:
                name = DRIFT[rng.randrange(len(DRIFT))](g)
                roll = rng.random()
                if roll < 0.34:
                    # Acronym rename — a false SPLIT. Match rate cannot see it.
                    name = "".join(w[0] for w in g.split()) + " Programs"
                elif roll < 0.52:
                    # Grant schedule collapsed to a placeholder — genuinely
                    # ambiguous, and the only drift match rate does catch.
                    name = "Various Organizations"
            recs.append(GrantRecord(
                filer_ein="", tax_year=year, recipient_name_raw=name,
                recipient_state=state,
                amount=float(rng.randrange(sizes[0], sizes[1], 1000)),
                purpose="General operating support" if rng.random() < 0.5 else "Program support",
            ))
    return recs


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    for f in os.listdir(OUT_DIR):
        if f.endswith(".json"):
            os.remove(os.path.join(OUT_DIR, f))

    rng = random.Random(20260803)  # fixed seed — V9 idempotency
    built = []

    for idx, (name, state, ntee, band, profile) in enumerate(PROFILES):
        ein = f"38{idx:07d}"
        recs = synth(profile, state, rng)
        for r in recs:
            r.filer_ein = ein
        m = compute(recs, CURRENT_YEAR)
        built.append((ein, name, state, ntee, band, profile, m))

    # Peer medians over publishable foundations only, excluding self.
    # Cell size here is far below the spec's minimum of 30, so peer_basis is
    # recorded as "demo" and the tool labels it as illustrative.
    for ein, name, state, ntee, band, profile, m in built:
        if not m.metrics:
            continue
        peers = [o.metrics["new_grantee_rate_pooled"]
                 for e2, _, _, _, b2, _, o in built
                 if o.metrics and o.publishable and e2 != ein and b2 == band]
        if len(peers) >= 2:
            m.metrics["peer_median_new_grantee_rate"] = round(statistics.median(peers), 4)
            m.metrics["peer_basis"] = "demo:assets"
            m.metrics["peer_cell_size"] = len(peers)

    index = []
    for ein, name, state, ntee, band, profile, m in built:
        slug = slugify(name)
        rate = m.metrics["new_grantee_rate_pooled"] if m.metrics else None
        doc = {
            "ein": ein,
            "slug": slug,
            "name": name,
            "state": state,
            "ntee_major": ntee,
            "asset_band": band,
            "window": m.window,
            "quality": {**m.quality, "publishable": m.publishable,
                        "gate_failures": m.gate_failures,
                        "singleton_cluster_share": m.quality.get("singleton_cluster_share"),
                        "drift_review_flag": m.quality.get("drift_review_flag"),
                        "individual_grants_excluded": 0,
                        "duplicate_filings_dropped": 0},
            "metrics": m.metrics,
            "status_band": status_band(rate if m.publishable else None),
            "self_reported": {
                "accepts_unsolicited": profile in ("entrenched", "open", "small_grants",
                                                   "young", "messy_names"),
                "application_info_text": None,
            },
            "provenance": {
                "source": "SYNTHETIC — demonstration data, not IRS filings",
                "as_of_fiscal_year": AS_OF,
                "computed_at": "2026-08-03",
                "next_recompute_expected": "2026-11-01",
            },
        }
        with open(os.path.join(OUT_DIR, f"{ein}.json"), "w") as fh:
            json.dump(doc, fh, indent=2, sort_keys=True)
            fh.write("\n")

        index.append({
            "ein": ein, "slug": slug, "name": name, "state": state,
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
                        "singleton_cluster_share": m.quality.get("singleton_cluster_share"),
                        "drift_review_flag": m.quality.get("drift_review_flag"),
            "accepts_unsolicited": doc["self_reported"]["accepts_unsolicited"],
            "drift_review_flag": m.quality.get("drift_review_flag"),
            "singleton_share": m.quality.get("singleton_cluster_share"),
        })

    index.sort(key=lambda d: d["name"])
    with open(os.path.join(HERE, "data", "index.json"), "w") as fh:
        json.dump({
            "generated": "2026-08-03",
            "as_of_fiscal_year": AS_OF,
            "synthetic": True,
            "count": len(index),
            "foundations": index,
        }, fh, indent=2, sort_keys=True)
        fh.write("\n")

    pub = sum(1 for d in index if d["publishable"])
    print(f"{len(index)} foundations, {pub} publishable, {len(index) - pub} gated")
    for d in index:
        flag = "" if d["publishable"] else f"  GATED ({', '.join(d['gate_failures'])})"
        rate = f"{d['rate_pooled']:.3f}" if d["rate_pooled"] is not None else "  —  "
        print(f"  {d['name'][:34]:34} rate={rate}  match={d['match_rate']:.2f}{flag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
