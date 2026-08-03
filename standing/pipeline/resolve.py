"""Entity resolution — SPEC.md §2.4.

Partitions ONE filer's grant records into grantee identities.

The single most important thing to understand here: this is a clustering
problem, not a lookup. A grantee appearing in exactly one year forms a valid
singleton cluster — a genuine first-time grantee. "Ambiguous" means "cannot be
assigned to an identity with confidence", NOT "matched nothing".

Conflating those two collapses every rate toward zero and makes every
foundation read as closed. See tests/test_unresolved_bias.py, which asserts
both directions.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from difflib import SequenceMatcher

SIMILARITY_THRESHOLD = 92.0
LENGTH_RATIO_FLOOR = 0.6

STOPWORDS = {"OF", "THE", "AND", "FOR", "IN", "AT", "A"}

LEGAL_SUFFIXES = {
    "INC", "INCORPORATED", "LLC", "LTD", "CORP", "CORPORATION", "CO", "PC", "PA",
}

# Deliberately NOT stripped — these are distinguishing tokens, not noise.
KEEP_TOKENS = {
    "FOUNDATION", "TRUST", "FUND", "SOCIETY", "ASSOCIATION",
    "CENTER", "CENTRE", "INSTITUTE",
}

PLACEHOLDER_NAMES = {
    "", "VARIOUS", "VARIOUS ORGANIZATIONS", "VARIOUS ORGANIZATION",
    "SEE ATTACHED", "SEE ATTACHED SCHEDULE", "MULTIPLE RECIPIENTS",
    "ANONYMOUS", "CONFIDENTIAL", "NA", "N A", "NONE", "UNKNOWN",
}

_PUNCT = re.compile(r"[^\w&\s]")
_WS = re.compile(r"\s+")


def normalize(name: str) -> str:
    """SPEC §2.4 normalization. Never overwrites recipient_name_raw."""
    if name is None:
        return ""
    s = unicodedata.normalize("NFKD", name)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.upper()
    s = _PUNCT.sub(" ", s)
    s = _WS.sub(" ", s).strip()
    if s.startswith("THE "):
        s = s[4:]
    tokens = s.split()
    while tokens and tokens[-1] in LEGAL_SUFFIXES:
        tokens.pop()
    return " ".join(tokens)


def _token_sort_ratio(a: str, b: str) -> float:
    """Stdlib stand-in for rapidfuzz.fuzz.token_sort_ratio.

    Sorting tokens before comparison makes the measure order-insensitive.
    Swap in rapidfuzz where it is available; keep this as the fallback so the
    mandatory tests run without a dependency.
    """
    sa = " ".join(sorted(a.split()))
    sb = " ".join(sorted(b.split()))
    return SequenceMatcher(None, sa, sb).ratio() * 100.0


def similarity(a: str, b: str) -> float:
    """SPEC §2.4 similarity, with the subset guard.

    Bare token_set_ratio returns 100 whenever one name's token set is a subset
    of the other's, so UNIVERSITY OF MICHIGAN and UNIVERSITY OF MICHIGAN SCHOOL
    OF NURSING score identically. That merges distinct affiliates into one
    identity, suppresses new-grantee counts, and makes an open foundation read
    as closed — a bias no automated check can see, because over-merging RAISES
    the match rate.

    Prefer a false split (visible in V12 sampling) to a false merge (invisible).
    """
    if not a or not b:
        return 0.0
    if a == b:
        return 100.0

    ta, tb = set(a.split()), set(b.split())

    # Numeric guard. Digits are among the most distinguishing tokens in
    # organization names — PS 128 vs PS 129, Local 43 vs Local 44, District 5
    # vs District 6 — yet they are a single character apart, so any
    # character-similarity measure scores them as near-identical and merges
    # them. Differing numeric tokens always mean different entities.
    if {t for t in ta if t.isdigit()} != {t for t in tb if t.isdigit()}:
        return 0.0

    # Strict-subset guard: any distinguishing token beyond a stopword blocks it.
    if ta < tb or tb < ta:
        extra = ta ^ tb
        if len(extra) >= 2 or (extra - STOPWORDS):
            return 0.0

    if min(len(a), len(b)) / max(len(a), len(b)) < LENGTH_RATIO_FLOOR:
        return 0.0

    return _token_sort_ratio(a, b)


@dataclass
class GrantRecord:
    filer_ein: str
    tax_year: int
    recipient_name_raw: str
    recipient_state: str | None
    amount: float
    purpose: str = ""
    is_individual: bool = False
    # assigned during resolution
    cluster_id: int | None = None
    ambiguous: bool = False
    ambiguous_reason: str = ""
    match_method: str = ""
    match_score: float = 0.0


@dataclass
class Cluster:
    cluster_id: int
    canonical: str
    state: str | None
    members: list[GrantRecord] = field(default_factory=list)


def _unusable(normalized: str, rec: GrantRecord) -> str:
    if rec.is_individual:
        return "individual_grant"
    if not normalized:
        return "empty_name"
    if normalized in PLACEHOLDER_NAMES:
        return "placeholder_name"
    return ""


def _state_compatible(a: str | None, b: str | None) -> bool:
    """Missing state acts as a wildcard (SPEC §7.1 known issue 2).

    A wildcard match is permitted against a single candidate; two or more
    candidates still force `ambiguous` via the normal count check.
    """
    if a is None or b is None:
        return True
    return a == b


def resolve_filer(records: list[GrantRecord]) -> tuple[list[Cluster], dict]:
    """Cluster one filer's records. Deterministic and order-independent.

    Records are processed in ascending (tax_year, recipient_name_raw) order —
    never input order, which would break V9 idempotency.
    """
    ordered = sorted(records, key=lambda r: (r.tax_year, r.recipient_name_raw or ""))
    clusters: list[Cluster] = []
    next_id = 0
    ambiguous_count = 0

    for rec in ordered:
        norm = normalize(rec.recipient_name_raw)

        reason = _unusable(norm, rec)
        if reason:
            rec.ambiguous = True
            rec.ambiguous_reason = reason
            ambiguous_count += 1
            continue

        # Compare against each cluster's CANONICAL name only — never against
        # every member. Prevents transitive drift through chained fuzzy links.
        candidates = []
        for cl in clusters:
            if not _state_compatible(rec.recipient_state, cl.state):
                continue
            score = similarity(norm, cl.canonical)
            if score >= SIMILARITY_THRESHOLD:
                candidates.append((score, cl))

        if len(candidates) == 1:
            score, cl = candidates[0]
            rec.cluster_id = cl.cluster_id
            rec.match_method = "exact" if score == 100.0 else "fuzzy"
            rec.match_score = score
            cl.members.append(rec)
        elif len(candidates) == 0:
            # The normal path for a first-time grantee. NOT an error,
            # NOT ambiguous, and it MUST be counted as new downstream.
            cl = Cluster(cluster_id=next_id, canonical=norm, state=rec.recipient_state)
            next_id += 1
            rec.cluster_id = cl.cluster_id
            rec.match_method = "new_cluster"
            rec.match_score = 100.0
            cl.members.append(rec)
            clusters.append(cl)
        else:
            rec.ambiguous = True
            rec.ambiguous_reason = "multiple_candidates"
            ambiguous_count += 1

    total = len(ordered)
    quality = {
        "total_grant_records": total,
        "ambiguous_records": ambiguous_count,
        "clusters_formed": len(clusters),
        "match_rate": (1.0 - ambiguous_count / total) if total else 0.0,
    }
    return clusters, quality
