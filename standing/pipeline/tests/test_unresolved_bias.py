"""V4 — ambiguity-bias assertion. MANDATORY. Do not delete.

This test protects the product's core claim, and it only does so with BOTH
halves present.

Half one: an ambiguous record must not inflate the new-grantee rate.
Half two: a genuine first-time grantee must be COUNTED as new.

Half one alone is vacuous. An implementation that marks every unmatched record
ambiguous collapses all rates to zero and makes every foundation read closed —
and it passes half one cleanly, because corrupting a repeat grantee cannot
raise a rate that is already zero. That was a real defect in v1.0 of the spec,
found by a cold-read audit. Half two is what makes the check mean anything.

Run: python3 standing/pipeline/tests/test_unresolved_bias.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from metrics import compute  # noqa: E402
from resolve import GrantRecord, normalize, similarity  # noqa: E402

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


def rec(year, name, state="MI", amount=10000.0):
    return GrantRecord(
        filer_ein="000000000", tax_year=year, recipient_name_raw=name,
        recipient_state=state, amount=amount,
    )


def baseline_records():
    """Four years. Five stable repeat grantees each year."""
    out = []
    for y in (2021, 2022, 2023, 2024):
        for n in ("Alpha Center", "Bravo Trust", "Charlie Society",
                  "Delta Institute", "Echo Association"):
            out.append(rec(y, n))
    return out


# ---------------------------------------------------------------- half one
print("\nV4a — an ambiguous record must not inflate the new-grantee rate")

base = baseline_records()
m0 = compute(base, CURRENT_YEAR)
rate0 = m0.metrics["new_grantee_rate_pooled"]
match0 = m0.quality["match_rate"]

# Corrupt one repeat grantee in the latest year so it cannot be assigned.
corrupt = baseline_records()
for r in corrupt:
    if r.tax_year == 2024 and r.recipient_name_raw == "Alpha Center":
        r.recipient_name_raw = "VARIOUS"

m1 = compute(corrupt, CURRENT_YEAR)
rate1 = m1.metrics["new_grantee_rate_pooled"]
match1 = m1.quality["match_rate"]

check("rate does not increase when a record becomes ambiguous",
      rate1 <= rate0, f"{rate0} -> {rate1}")
check("ambiguous record excluded from numerator and denominator",
      m1.metrics["total_grantee_count_pooled"] < m0.metrics["total_grantee_count_pooled"],
      f"{m0.metrics['total_grantee_count_pooled']} -> {m1.metrics['total_grantee_count_pooled']}")
check("match rate drops", match1 < match0, f"{match0} -> {match1}")

# ---------------------------------------------------------------- half two
print("\nV4b — a genuine first-time grantee MUST be counted as new")

with_new = baseline_records()
with_new.append(rec(2024, "Foxtrot Community Partners"))

m2 = compute(with_new, CURRENT_YEAR)

check("new grantee is not marked ambiguous",
      m2.quality["ambiguous_records"] == 0,
      f"ambiguous={m2.quality['ambiguous_records']}")
check("new_grantee_count_latest increases by exactly 1",
      m2.metrics["new_grantee_count_latest"] == m0.metrics["new_grantee_count_latest"] + 1,
      f"{m0.metrics['new_grantee_count_latest']} -> {m2.metrics['new_grantee_count_latest']}")
check("match rate stays at 1.0 — forming a cluster is not a failure",
      m2.quality["match_rate"] == 1.0, f"match_rate={m2.quality['match_rate']}")
check("pooled rate increases",
      m2.metrics["new_grantee_rate_pooled"] > rate0,
      f"{rate0} -> {m2.metrics['new_grantee_rate_pooled']}")

# ------------------------------------------------------- the inverted build
print("\nV4c — the collapse an implementation must not produce")

# A foundation that funds someone new every single year must NOT read as 0.
churn = []
for y in (2021, 2022, 2023, 2024):
    churn.append(rec(y, "Anchor Trust"))
    for i in range(4):
        churn.append(rec(y, f"Rotating Partner {y}-{i}"))

m3 = compute(churn, CURRENT_YEAR)
check("a high-churn funder reads as high, not zero",
      m3.metrics["new_grantee_rate_pooled"] > 0.5,
      f"rate={m3.metrics['new_grantee_rate_pooled']}")
check("high-churn funder is not penalised on match rate",
      m3.quality["match_rate"] == 1.0, f"match_rate={m3.quality['match_rate']}")

# ------------------------------------------------------------- over-merging
print("\nV12 unit floor — parent/affiliate must not merge")

pairs = [
    ("UNIVERSITY OF MICHIGAN", "UNIVERSITY OF MICHIGAN SCHOOL OF NURSING"),
    ("BOYS & GIRLS CLUB", "BOYS & GIRLS CLUB OF DETROIT"),
    ("UNITED WAY", "UNITED WAY OF SOUTHEAST MICHIGAN"),
    ("YMCA", "YMCA OF METROPOLITAN DETROIT"),
]
for a, b in pairs:
    check(f"no merge: {a} / {b}",
          similarity(normalize(a), normalize(b)) < 92.0,
          f"score={similarity(normalize(a), normalize(b))}")

# ------------------------------------------------- address change regression
print("\nV4d — a grantee that MOVES must not read as new")

# Found in real data: AFRICAN PARKS FOUNDATION OF AMERICA is recorded under DC
# in some years and NY in others across a five-year grantee relationship.
# Blocking every match on state split it in two and counted a long-standing
# repeat grantee as new — a false split, which inflates the rate.
moved = []
for y, st in ((2021, "DC"), (2022, "DC"), (2023, "NY"), (2024, "NY")):
    moved.append(rec(y, "African Parks Foundation of America", state=st))
    for n in ("Alpha Center", "Bravo Trust", "Charlie Society",
              "Delta Institute", "Echo Association"):
        moved.append(rec(y, n))

m5 = compute(moved, CURRENT_YEAR)
check("relocated grantee is not counted as new",
      m5.metrics["new_grantee_count_latest"] == 0,
      f"new={m5.metrics['new_grantee_count_latest']}")
check("rate stays at zero for an all-repeat funder",
      m5.metrics["new_grantee_rate_pooled"] == 0.0,
      f"rate={m5.metrics['new_grantee_rate_pooled']}")

# But two genuinely different orgs sharing a fuzzy-similar name in different
# states must still stay separate.
distinct = []
for y in (2021, 2022, 2023, 2024):
    for n in ("Alpha Center", "Bravo Trust", "Charlie Society",
              "Delta Institute", "Echo Association"):
        distinct.append(rec(y, n))
distinct.append(rec(2023, "Community Health Partners of Dayton", state="OH"))
distinct.append(rec(2024, "Community Health Partners of Denver", state="CO"))
m6 = compute(distinct, CURRENT_YEAR)
check("similarly-named orgs in different states stay separate",
      m6.metrics["new_grantee_count_latest"] == 1,
      f"new={m6.metrics['new_grantee_count_latest']}")


print("\nnormalization sanity")
check("legal suffix stripped", normalize("Riverbend Youth Collective, Inc.") == "RIVERBEND YOUTH COLLECTIVE")
check("leading THE stripped", normalize("The Lindmark Trust") == "LINDMARK TRUST")
check("distinguishing token kept", "FOUNDATION" in normalize("Harrowgate Foundation"))
check("naming drift still matches",
      similarity(normalize("Riverbend Youth Collective, Inc."),
                 normalize("Riverbend Youth Collective")) >= 92.0)

print(f"\n{PASSES} passed, {len(FAILURES)} failed")
if FAILURES:
    for f in FAILURES:
        print(f"  - {f}")
    sys.exit(1)
print("V4 + V12 unit floor: OK")
