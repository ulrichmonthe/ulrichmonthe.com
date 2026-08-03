"""Derived metrics — SPEC.md §2.5.

Unit of analysis is the distinct grantee-year, never the grant record. Three
grants to one organization in one year is one relationship.

Two rates are produced and they are different quantities:
  * pooled  — across eligible years, used ONLY for the status band
  * latest  — most recent eligible year, used for the headline sentence
Swapping them reintroduces, one layer up, the unit error this corrects.
"""

from __future__ import annotations

from dataclasses import dataclass

from resolve import GrantRecord, resolve_filer

WINDOW_YEARS = 5
LOOKBACK_YEARS = 3
MIN_PRIOR_YEARS = 2
MAX_GAP_YEARS = 2

MATCH_RATE_GATE = 0.85
MIN_ELIGIBLE_YEARS = 2
MIN_POOLED_GRANTEES = 10
MAX_STALENESS_YEARS = 3


@dataclass
class FilerMetrics:
    window: dict
    quality: dict
    metrics: dict | None
    publishable: bool
    gate_failures: list[str]


def _grantees_by_year(records: list[GrantRecord]) -> dict[int, set[int]]:
    """Distinct cluster ids per year. Ambiguous records excluded entirely."""
    out: dict[int, set[int]] = {}
    for r in records:
        if r.ambiguous or r.cluster_id is None:
            continue
        out.setdefault(r.tax_year, set()).add(r.cluster_id)
    return out


def _prior(year: int, present: list[int], grantees: dict[int, set[int]]) -> tuple[set[int], int]:
    """Union of the up-to-3 immediately preceding PRESENT years.

    Walks present years rather than doing calendar arithmetic. On a gappy
    series (2018, 2022, 2023, 2024) calendar arithmetic would give prior(2023)
    = {2022} alone, counting a grantee last funded in 2018 as new — a bias in
    the open-looking direction, which is the failure this module exists to
    prevent. Returns the union and how many years it actually drew on.
    """
    preceding = [y for y in present if y < year][-LOOKBACK_YEARS:]
    union: set[int] = set()
    for y in preceding:
        union |= grantees.get(y, set())
    return union, len(preceding)


def compute(
    records: list[GrantRecord],
    current_year: int,
    peer_median: float | None = None,
    peer_basis: str | None = None,
    peer_cell_size: int | None = None,
) -> FilerMetrics:
    clusters, quality = resolve_filer(records)

    all_years = sorted({r.tax_year for r in records})
    present = all_years[-WINDOW_YEARS:]
    windowed = [r for r in records if r.tax_year in present]

    # Recompute quality over the window only.
    _, quality = resolve_filer(windowed)

    grantees = _grantees_by_year(windowed)

    eligible: list[int] = []
    skipped: list[dict] = []
    lookback_used: dict[int, int] = {}

    for i, y in enumerate(present):
        preceding = [p for p in present if p < y]
        if len(preceding) < MIN_PRIOR_YEARS:
            skipped.append({"year": y, "reason": "insufficient_baseline"})
            continue
        if y - preceding[-1] > MAX_GAP_YEARS:
            skipped.append({"year": y, "reason": "stale_baseline"})
            continue
        if not grantees.get(y):
            skipped.append({"year": y, "reason": "no_grantees"})
            continue
        eligible.append(y)
        _, n = _prior(y, present, grantees)
        lookback_used[y] = n

    window = {
        "start_year": present[0] if present else None,
        "end_year": present[-1] if present else None,
        "years_present": present,
        "eligible_years": eligible,
        "eligible_year_count": len(eligible),
        "latest_eligible_year": max(eligible) if eligible else None,
        "skipped_years": skipped,
    }

    pooled_new = 0
    pooled_total = 0
    latest_new = latest_total = 0

    for y in eligible:
        prior, _ = _prior(y, present, grantees)
        gy = grantees.get(y, set())
        new = gy - prior
        pooled_new += len(new)
        pooled_total += len(gy)
        if y == window["latest_eligible_year"]:
            latest_new, latest_total = len(new), len(gy)

    # Drift signal. Match rate is BLIND to naming drift: when a preparer
    # renames a repeat grantee, the record does not become ambiguous — it
    # forms a second cluster. That is a false split, which INFLATES the
    # new-grantee rate (the open-looking bias) while match_rate stays at 1.0.
    # Share of clusters appearing in exactly one present year is the cheapest
    # available proxy. It is genuinely ambiguous — a high-churn funder looks
    # the same as a drifting one — so it is surfaced as a caveat, never used
    # to gate. Confirming which it is requires V12 sampling.
    seen_years: dict[int, set[int]] = {}
    for r in windowed:
        if r.ambiguous or r.cluster_id is None:
            continue
        seen_years.setdefault(r.cluster_id, set()).add(r.tax_year)
    n_clusters = len(seen_years)
    singletons = sum(1 for ys in seen_years.values() if len(ys) == 1)
    quality["singleton_cluster_share"] = round(singletons / n_clusters, 4) if n_clusters else 0.0
    quality["drift_review_flag"] = bool(
        n_clusters and (singletons / n_clusters) > 0.6 and len(present) >= 4
    )

    gate_failures: list[str] = []
    if quality["match_rate"] < MATCH_RATE_GATE:
        gate_failures.append("match_rate")
    if len(eligible) < MIN_ELIGIBLE_YEARS:
        gate_failures.append("eligible_year_count")
    if pooled_total < MIN_POOLED_GRANTEES:
        gate_failures.append("total_grantee_count_pooled")
    if window["latest_eligible_year"] is None or window["latest_eligible_year"] < current_year - MAX_STALENESS_YEARS:
        gate_failures.append("recency")

    # Never divide by zero — emit no metrics instead.
    if pooled_total == 0:
        return FilerMetrics(window, quality, None, False, gate_failures or ["no_grantees"])

    metrics = {
        "new_grantee_count_latest": latest_new,
        "total_grantee_count_latest": latest_total,
        "lookback_years_used": lookback_used.get(window["latest_eligible_year"], 0),
        "new_grantee_rate_pooled": round(pooled_new / pooled_total, 4),
        "new_grantee_count_pooled": pooled_new,
        "total_grantee_count_pooled": pooled_total,
        "peer_median_new_grantee_rate": peer_median,
        "peer_basis": peer_basis,
        "peer_cell_size": peer_cell_size,
        "repeat_dollar_concentration": _repeat_dollar_concentration(windowed, eligible, present, grantees),
        "grant_sizes": _grant_sizes(windowed, window["latest_eligible_year"]),
    }

    return FilerMetrics(window, quality, metrics, not gate_failures, gate_failures)


def _repeat_dollar_concentration(records, eligible, present, grantees) -> float | None:
    repeat = total = 0.0
    for y in eligible:
        prior, _ = _prior(y, present, grantees)
        for r in records:
            if r.tax_year != y or r.ambiguous or r.cluster_id is None:
                continue
            if r.amount is None or r.amount < 0:
                continue
            total += r.amount
            if r.cluster_id in prior:
                repeat += r.amount
    return round(repeat / total, 4) if total else None


def _percentile_nearest_rank(values: list[float], pct: float) -> float:
    """Nearest-rank method, stated on the methodology page (SPEC §7.1 item 3)."""
    if not values:
        return 0.0
    s = sorted(values)
    import math
    k = max(1, math.ceil(pct / 100.0 * len(s)))
    return s[k - 1]


def _grant_sizes(records, year: int | None) -> dict | None:
    if year is None:
        return None
    amounts = [
        r.amount for r in records
        if r.tax_year == year and not r.ambiguous and r.amount is not None and r.amount >= 0
    ]
    if not amounts:
        return None
    return {
        "min": min(amounts),
        "p25": _percentile_nearest_rank(amounts, 25),
        "median": _percentile_nearest_rank(amounts, 50),
        "p75": _percentile_nearest_rank(amounts, 75),
        "max": max(amounts),
    }


def status_band(rate: float | None) -> str:
    """Descriptive only. Never an imperative — SPEC §0.2."""
    if rate is None:
        return "Not enough data to compare"
    if rate >= 0.25:
        return "Adds new grantees regularly"
    if rate >= 0.10:
        return "Adds new grantees occasionally"
    return "Rarely funds new grantees"
