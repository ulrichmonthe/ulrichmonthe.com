"""V2 — independent verification against the raw filings.

Re-derives every published figure for a sample of foundations using a
deliberately SEPARATE code path: it does not import resolve.py or metrics.py,
and it re-reads the XML from scratch with its own parsing and its own matching.
If the two agree the pipeline is probably not systematically wrong; if they
disagree, one of them is.

What this is NOT: a human reading filings. An independent recomputation catches
parser and logic bugs. It cannot catch a shared misunderstanding of what Part XV
means, because both implementations were written by the same author from the
same reading. The printed per-year tables exist so that a person can check a
handful of numbers against the actual returns in a few minutes — that check is
still outstanding and is the one that matters most.

Run: python3 standing/checks/independent_check.py [n_samples]
"""

from __future__ import annotations

import csv
import collections
import json
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
STANDING = os.path.dirname(HERE)
CACHE = os.path.join(STANDING, ".cache")
DATA = os.path.join(STANDING, "data")
NS = "{http://www.irs.gov/efile}"

# ---------------------------------------------------------------- independent
# Written without reference to resolve.py. Simpler on purpose: exact match on a
# conservatively normalised name, ignoring state entirely. It should UNDER-count
# new grantees relative to the pipeline where names drift, and OVER-count where
# the pipeline merges two records the pipeline thinks are one organisation.


def naive_norm(name: str) -> str:
    s = unicodedata.normalize("NFKD", name or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^A-Za-z0-9& ]", " ", s.upper())
    s = re.sub(r"\s+", " ", s).strip()
    for suffix in (" INC", " INCORPORATED", " LLC", " LTD", " CORP", " CO"):
        if s.endswith(suffix):
            s = s[: -len(suffix)]
    if s.startswith("THE "):
        s = s[4:]
    return s.strip()


PLACEHOLDERS = {"", "VARIOUS", "VARIOUS ORGANIZATIONS", "SEE ATTACHED",
                "MULTIPLE RECIPIENTS", "ANONYMOUS", "CONFIDENTIAL", "NONE", "NA"}


def read_filing(path: str):
    """Return (tax_year, [normalised grantee names]) straight from the XML."""
    root = ET.parse(path).getroot()
    yr = root.findtext(f"{NS}ReturnHeader/{NS}TaxYr")
    if not yr or not yr.isdigit():
        return None, []
    sup = root.find(f".//{NS}SupplementaryInformationGrp")
    if sup is None:
        return int(yr), []
    names = []
    # Deliberately ONLY the paid-grants element. If this and the pipeline both
    # excluded future-approved grants, that agreement is meaningful.
    for g in sup.findall(f"{NS}GrantOrContributionPdDurYrGrp"):
        n = g.find(f"{NS}RecipientBusinessName/{NS}BusinessNameLine1Txt")
        if n is None or not n.text:
            continue
        nn = naive_norm(n.text)
        if nn in PLACEHOLDERS:
            continue
        names.append(nn)
    return int(yr), names


def main() -> int:
    n_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    idx = collections.defaultdict(dict)
    with open(os.path.join(DATA, "pf_index.csv"), encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["TaxYear"].isdigit():
                idx[r["EIN"].zfill(9)][int(r["TaxYear"])] = r["ObjectId"]

    published = json.load(open(os.path.join(DATA, "index.json")))["foundations"]
    pub = [f for f in published if f["publishable"]]

    # Deterministic spread across the rate range, not the easiest cases.
    pub.sort(key=lambda f: f["rate_pooled"])
    picks = []
    if pub:
        step = max(1, len(pub) // n_samples)
        picks = [pub[min(i * step, len(pub) - 1)] for i in range(n_samples)]

    print(f"INDEPENDENT VERIFICATION — {len(picks)} foundations")
    print("Re-derived from raw XML with a separate parser and simpler matching.\n")

    agree = disagree = skipped = 0
    report = []

    for f in picks:
        ein = f["ein"]
        doc = json.load(open(os.path.join(DATA, "foundations", f"{ein}.json")))
        window = doc["window"]
        per_year = {}
        for yr, oid in sorted(idx[ein].items()):
            p = os.path.join(CACHE, f"{oid}.xml")
            if not os.path.exists(p):
                continue
            y, names = read_filing(p)
            if y is not None:
                per_year[y] = names

        present = window["years_present"]
        latest = window["latest_eligible_year"]
        if latest is None or latest not in per_year:
            skipped += 1
            continue

        prior_years = [y for y in present if y < latest][-3:]
        prior = set()
        for y in prior_years:
            prior |= set(per_year.get(y, []))
        this = set(per_year.get(latest, []))
        naive_new = len(this - prior)
        naive_total = len(this)

        m = doc["metrics"]
        pipe_new = m["new_grantee_count_latest"]
        pipe_total = m["total_grantee_count_latest"]

        d_new = pipe_new - naive_new
        d_total = pipe_total - naive_total
        ok = abs(d_new) <= max(2, round(0.05 * naive_total)) and abs(d_total) <= max(2, round(0.05 * naive_total))
        agree += ok
        disagree += (not ok)

        print(f"{'OK  ' if ok else 'FLAG'} {doc['name'][:44]:44} EIN {ein}")
        print(f"       pipeline  {pipe_new:>4} new of {pipe_total:>4}   rate {m['new_grantee_rate_pooled']:.3f}")
        print(f"       independent {naive_new:>4} new of {naive_total:>4}   delta new {d_new:+d}, total {d_total:+d}")
        print(f"       grant lines per year: " +
              ", ".join(f"FY{y}={len(per_year.get(y, []))}" for y in present))
        print(f"       match rate {doc['quality']['match_rate']:.3f} · "
              f"future-approved excluded {doc['quality'].get('future_grants_excluded', 0)}")
        print()

        report.append({
            "ein": ein, "name": doc["name"], "slug": doc["slug"],
            "latest_year": latest,
            "pipeline": {"new": pipe_new, "total": pipe_total},
            "independent": {"new": naive_new, "total": naive_total},
            "delta": {"new": d_new, "total": d_total},
            "grant_lines_per_year": {str(y): len(per_year.get(y, [])) for y in present},
            "match_rate": doc["quality"]["match_rate"],
            "within_tolerance": ok,
        })

    print(f"agree {agree} · flagged {disagree} · skipped {skipped}")
    print("\nTolerance: the two differ by design. The independent pass ignores state")
    print("and does exact matching only, so it splits organisations whose names drift")
    print("and merges same-named organisations in different states. Deltas within")
    print("5% (or 2 grantees) are expected; larger ones need a look.")
    print("\nSTILL OUTSTANDING: a person opening these returns and counting by eye.")
    print("Both implementations share one author and one reading of Part XV, so")
    print("agreement here cannot rule out a shared misunderstanding.")

    out = os.path.join(DATA, "verification.json")
    with open(out, "w") as fh:
        json.dump({"checked": len(report), "agree": agree, "flagged": disagree,
                   "method": "independent recomputation, separate parser",
                   "human_verified": False, "results": report}, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"\nwrote {out}")
    return 1 if disagree else 0


if __name__ == "__main__":
    raise SystemExit(main())
