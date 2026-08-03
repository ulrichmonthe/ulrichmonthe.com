"""V6 — neutrality lint. SPEC.md §6.

Scans rendered HTML for imperatives attached to a named foundation. Any hit
fails the build.

This is a BACKSTOP, not a proof. It is a substring blocklist and it is
defeatable by paraphrase. SPEC §0.2 is enforced by human review of template
strings; this catches careless phrasing beneath that review.

Run: python3 standing/checks/neutrality_lint.py
"""

from __future__ import annotations

import os
import re
import sys

BANNED = [
    "do not apply", "don't apply", "avoid this", "skip this", "not worth",
    "waste of time", "bad funder", "won't fund you", "no chance",
    "you should", "we recommend", "futile", "pointless", "don't bother",
    "best funders", "worst funders", "worth applying",
]

# Files whose foundation-facing copy is in scope.
TARGETS = [
    "live-projects/funder-standing/index.html",
    "standing/pipeline/metrics.py",
]

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def scan(path: str) -> list[str]:
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return [f"{path}: MISSING"]
    with open(full, encoding="utf-8") as fh:
        text = fh.read()

    # Strip the explanatory prose blocks, which legitimately discuss what the
    # tool does NOT do. Only foundation-facing copy is in scope.
    body = re.sub(r"<section>.*?</section>", "", text, flags=re.S)

    hits = []
    low = body.lower()
    for phrase in BANNED:
        idx = low.find(phrase)
        if idx >= 0:
            ctx = body[max(0, idx - 50): idx + 60].replace("\n", " ")
            hits.append(f"{path}: {phrase!r} -> …{ctx}…")
    return hits


def main() -> int:
    all_hits = []
    for t in TARGETS:
        all_hits += scan(t)

    # The status bands must never contain an imperative.
    sys.path.insert(0, os.path.join(ROOT, "standing", "pipeline"))
    from metrics import status_band  # noqa: E402

    for rate in (0.4, 0.31, 0.15, 0.018, 0.0, None):
        band = status_band(rate).lower()
        for phrase in BANNED:
            if phrase in band:
                all_hits.append(f"status_band({rate}): contains {phrase!r}")
        for word in ("should", "avoid", "recommend", "must", "don't"):
            if word in band:
                all_hits.append(f"status_band({rate}): imperative {word!r} in {band!r}")

    if all_hits:
        print("V6 FAIL — neutrality violations:")
        for h in all_hits:
            print("  -", h)
        return 1

    print(f"V6 OK — {len(TARGETS)} files, {len(BANNED)} patterns, status bands clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
