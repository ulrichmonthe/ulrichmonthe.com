"""Build the 990-PF filer index — SPEC.md §2.1.

Source: GivingTuesday Data Lake (gt990datalake-rawdata), the community mirror
of the IRS e-file corpus. The IRS's own AWS bucket was decommissioned at the
end of 2021 and now returns an empty listing; this bucket carries the full
universe plus per-year index files.

Streams each yearly index, keeps only FormType == 990PF, and writes a compact
CSV. Nothing large is held in memory or on disk.

Run: python3 standing/pipeline/fetch_index.py 2020 2021 2022 2023 2024
"""

from __future__ import annotations

import csv
import io
import os
import sys
import urllib.request

BUCKET = "https://gt990datalake-rawdata.s3.amazonaws.com"
SNAPSHOT = "2026-06-04"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "pf_index.csv")

KEEP = [
    "EIN", "TaxYear", "TaxPeriodEndDate", "ObjectId", "OrganizationName",
    "LegalDomicileState", "TotalAssetsBkEOY", "FormType", "ReturnVersion",
    "SubmittedOn",
]


def index_url(year: int) -> str:
    return f"{BUCKET}/Indices/990xmls/yearly/{year}_efiledata_xmls_created_on_{SNAPSHOT}.csv"


def stream_year(year: int, writer: csv.DictWriter) -> tuple[int, int]:
    url = index_url(year)
    kept = total = 0
    req = urllib.request.Request(url, headers={"User-Agent": "standing/1.0"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        text = io.TextIOWrapper(resp, encoding="utf-8", errors="replace", newline="")
        reader = csv.DictReader(text)
        for row in reader:
            total += 1
            if (row.get("FormType") or "").strip().upper() != "990PF":
                continue
            writer.writerow({k: (row.get(k) or "").strip() for k in KEEP})
            kept += 1
    return kept, total


def main(years: list[int]) -> int:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    grand_kept = grand_total = 0
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=KEEP)
        w.writeheader()
        for y in years:
            try:
                kept, total = stream_year(y, w)
            except Exception as exc:  # noqa: BLE001
                print(f"  {y}: FAILED — {exc}", file=sys.stderr)
                continue
            grand_kept += kept
            grand_total += total
            print(f"  {y}: {kept:,} 990-PF of {total:,} filings", flush=True)
    print(f"total: {grand_kept:,} 990-PF rows of {grand_total:,} -> {OUT}")
    return 0


if __name__ == "__main__":
    yrs = [int(a) for a in sys.argv[1:]] or [2020, 2021, 2022, 2023, 2024]
    raise SystemExit(main(yrs))
