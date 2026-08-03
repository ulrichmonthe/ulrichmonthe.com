"""Window edge cases — SPEC.md §2.5.

Covers the failure the audit flagged as SERIOUS and uncovered: a gappy filing
series given a one-year baseline, which counts long-standing grantees as new
and biases in the open-looking direction.

Run: python3 standing/pipeline/tests/test_window_edges.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from metrics import compute, status_band  # noqa: E402
from resolve import GrantRecord  # noqa: E402

CURRENT_YEAR = 2026
FAILURES = []
PASSES = 0


def check(label, condition, detail=""):
    global PASSES
    if condition:
        PASSES += 1
        print(f"  PASS  {label}")
    else:
        FAILURES.append(f"{label} — {detail}")
        print(f"  FAIL  {label} — {detail}")


def rec(year, name, amount=10000.0, state="MI"):
    return GrantRecord(filer_ein="1", tax_year=year, recipient_name_raw=name,
                       recipient_state=state, amount=amount)


print("\ngap years — a stale baseline must not manufacture new grantees")

# Funded Alpha in 2018 and again in 2023. Calendar arithmetic would give
# prior(2023) = {2022} only, making Alpha look new. Walking present years
# includes 2018, so it is correctly a repeat.
gappy = [rec(2018, "Alpha Center"), rec(2018, "Bravo Trust"),
         rec(2022, "Bravo Trust"), rec(2022, "Charlie Society"),
         rec(2023, "Alpha Center"), rec(2023, "Bravo Trust")]
m = compute(gappy, CURRENT_YEAR)

# 2023's preceding present year is 2022 — a one-year gap, within MAX_GAP_YEARS.
check("2023 is eligible", 2023 in m.window["eligible_years"], str(m.window))
check("Alpha not counted as new despite the 2019-21 gap",
      m.metrics["new_grantee_count_latest"] == 0,
      f"new={m.metrics['new_grantee_count_latest']}")
check("lookback depth is reported honestly",
      m.metrics["lookback_years_used"] == 2,
      f"lookback={m.metrics['lookback_years_used']}")

print("\nstale baseline — a gap wider than the limit skips the year")

stale = [rec(2015, "Alpha Center"), rec(2016, "Alpha Center"),
         rec(2024, "Alpha Center"), rec(2024, "Zulu Fund")]
m2 = compute(stale, CURRENT_YEAR)
check("2024 skipped rather than compared to a decade-old baseline",
      2024 not in m2.window["eligible_years"], str(m2.window["eligible_years"]))
check("skip reason recorded",
      any(s["reason"] == "stale_baseline" for s in m2.window["skipped_years"]),
      str(m2.window["skipped_years"]))
check("not publishable", not m2.publishable, str(m2.gate_failures))

print("\nzero-grant year")

zero = []
for y in (2021, 2022, 2024):
    for n in ("Alpha Center", "Bravo Trust", "Charlie Society",
              "Delta Institute", "Echo Association", "Golf Fund"):
        zero.append(rec(y, n))
zero.append(rec(2023, "VARIOUS"))  # a year with no usable grantees
m3 = compute(zero, CURRENT_YEAR)
check("zero-grantee year skipped",
      2023 not in m3.window["eligible_years"], str(m3.window["eligible_years"]))
check("2023 still occupies a window slot as a present year",
      2023 in m3.window["years_present"], str(m3.window["years_present"]))
check("no divide-by-zero", m3.metrics is not None)

print("\nempty filer — must not divide by zero")
m4 = compute([rec(2024, "VARIOUS"), rec(2023, "SEE ATTACHED"), rec(2022, "")], CURRENT_YEAR)
check("no metrics emitted", m4.metrics is None)
check("not publishable", not m4.publishable, str(m4.gate_failures))

print("\npublication gate — all four conditions")

three_years = []
for y in (2022, 2023, 2024):
    for i in range(6):
        three_years.append(rec(y, f"Org {chr(65+i)} Center"))
m5 = compute(three_years, CURRENT_YEAR)
check("3 present years yields exactly 1 eligible year",
      m5.window["eligible_year_count"] == 1, str(m5.window["eligible_years"]))
check("and is therefore not publishable — this is why the window is 5 years",
      not m5.publishable and "eligible_year_count" in m5.gate_failures,
      str(m5.gate_failures))

stale_filer = []
for y in (2016, 2017, 2018, 2019):
    for i in range(6):
        stale_filer.append(rec(y, f"Org {chr(65+i)} Center"))
m6 = compute(stale_filer, CURRENT_YEAR)
check("a filer whose latest data is years old fails recency",
      "recency" in m6.gate_failures, str(m6.gate_failures))

print("\nstatus bands are descriptive, never imperative")
for rate, expected in [(0.31, "Adds new grantees regularly"),
                       (0.15, "Adds new grantees occasionally"),
                       (0.018, "Rarely funds new grantees"),
                       (None, "Not enough data to compare")]:
    band = status_band(rate)
    check(f"band for {rate}", band == expected, f"got {band!r}")

banned = ["do not", "avoid", "should", "recommend", "worth"]
all_bands = [status_band(r) for r in (0.31, 0.15, 0.018, None)]
check("no band contains an imperative",
      not any(b in band.lower() for band in all_bands for b in banned),
      str(all_bands))

print(f"\n{PASSES} passed, {len(FAILURES)} failed")
if FAILURES:
    for f in FAILURES:
        print(f"  - {f}")
    sys.exit(1)
print("window edges: OK")
