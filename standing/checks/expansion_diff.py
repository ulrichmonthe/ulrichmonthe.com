"""V7 — what an expansion actually did.

Growing the cohort is not additive. Peer medians are a property of the
comparison set, so pulling in 300 more foundations moves the number sitting
under pages that were published months ago. Slugs are supposed to be
immutable and a collision suffix could quietly break an indexed URL. A
foundation that cleared the gate at one cohort size can fail at another.

None of that is visible in a git diff of 400 JSON files. This produces the
summary the pull request is written from, and fails on the two changes that
are never acceptable — a slug that moved and a page that vanished — while
merely reporting the ones that are legitimate but need eyes.

Run: python3 standing/checks/expansion_diff.py BEFORE.json [AFTER.json]

BEFORE is an index.json captured before the run (`git show HEAD:...`).
AFTER defaults to the working copy. Exit 1 means do not merge.
"""

from __future__ import annotations

import json
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_AFTER = os.path.join(HERE, "..", "data", "index.json")

# A peer median that moves more than this on an already-published page is
# reported prominently. It is not a failure — a better comparison set is the
# point of expanding — but a large move means the old figure was thin.
PEER_SHIFT_NOTABLE = 0.05


def load(path: str) -> dict[str, dict]:
    with open(path, encoding="utf-8") as fh:
        return {r["ein"]: r for r in json.load(fh)["foundations"]}


def pct(n: int, d: int) -> str:
    return f"{100.0 * n / d:.1f}%" if d else "—"


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__.strip())
        return 2
    before = load(sys.argv[1])
    after = load(sys.argv[2] if len(sys.argv) > 2 else DEFAULT_AFTER)

    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    kept = sorted(set(before) & set(after))

    failures: list[str] = []

    print(f"cohort  {len(before)} -> {len(after)}   "
          f"(+{len(added)} new, -{len(removed)} dropped, {len(kept)} carried over)")

    # ---- new pages: what cleared, what was withheld -----------------------
    new_pub = [e for e in added if after[e]["publishable"]]
    new_gated = [e for e in added if not after[e]["publishable"]]
    print(f"\nnew:    {len(new_pub)} publishable, {len(new_gated)} gated "
          f"({pct(len(new_gated), len(added))} withheld)")
    reasons: dict[str, int] = {}
    for e in new_gated:
        for r in after[e]["gate_failures"] or ["unspecified"]:
            reasons[r] = reasons.get(r, 0) + 1
    for r, c in sorted(reasons.items(), key=lambda kv: -kv[1]):
        print(f"          {c:>4}  {r}")

    bands: dict[str, int] = {}
    for e in added:
        bands[after[e]["asset_band"]] = bands.get(after[e]["asset_band"], 0) + 1
    if bands:
        print("        asset bands entered: "
              + ", ".join(f"{b} ({c})" for b, c in sorted(bands.items())))

    # ---- disappearing pages: never acceptable silently --------------------
    if removed:
        failures.append(f"{len(removed)} foundation(s) present before are gone after")
        print(f"\nDROPPED ({len(removed)}) — these have live URLs:")
        for e in removed[:20]:
            print(f"          {before[e]['slug']}  ({before[e]['name']})")

    # ---- slug immutability ------------------------------------------------
    moved = [(e, before[e]["slug"], after[e]["slug"])
             for e in kept if before[e]["slug"] != after[e]["slug"]]
    if moved:
        failures.append(f"{len(moved)} slug(s) changed on an existing foundation")
        print(f"\nSLUG MOVED ({len(moved)}):")
        for e, a, b in moved[:20]:
            print(f"          {a}  ->  {b}")

    # ---- gate flips on carried-over pages ---------------------------------
    lost = [e for e in kept if before[e]["publishable"] and not after[e]["publishable"]]
    gained = [e for e in kept if not before[e]["publishable"] and after[e]["publishable"]]
    if lost or gained:
        print(f"\ngate:   {len(gained)} newly publishable, {len(lost)} newly gated")
        for e in lost[:10]:
            print(f"          now gated: {after[e]['slug']}  "
                  f"{after[e]['gate_failures']}")

    # ---- the quiet one: peer medians under existing pages -----------------
    shifts = []
    for e in kept:
        pa, pb = before[e]["peer_median"], after[e]["peer_median"]
        if pa is None or pb is None:
            if pa != pb:
                shifts.append((e, pa, pb, None))
            continue
        if pa != pb:
            shifts.append((e, pa, pb, abs(pb - pa)))

    sized = [s for s in shifts if s[3] is not None]
    print(f"\npeer:   {len(shifts)} existing page(s) changed peer median "
          f"({pct(len(shifts), len(kept))} of carried-over)")
    if sized:
        deltas = [s[3] for s in sized]
        print(f"        median move {statistics.median(deltas):.4f}, "
              f"largest {max(deltas):.4f}")
        big = sorted((s for s in sized if s[3] >= PEER_SHIFT_NOTABLE),
                     key=lambda s: -s[3])
        if big:
            print(f"        {len(big)} moved by more than {PEER_SHIFT_NOTABLE}:")
            for e, pa, pb, d in big[:10]:
                print(f"          {after[e]['slug']}: {pa} -> {pb}  (Δ{d:.4f})")

    appeared = [s for s in shifts if s[1] is None]
    vanished = [s for s in shifts if s[2] is None]
    if appeared:
        print(f"        {len(appeared)} gained a peer comparison they did not have")
    if vanished:
        print(f"        {len(vanished)} lost their peer comparison")

    # ---- figures that changed without a rebuild ---------------------------
    # rate_pooled is derived only from a foundation's own filings, so it must
    # not move unless that foundation was actually rebuilt from new source.
    rate_moved = [e for e in kept
                  if before[e]["rate_pooled"] != after[e]["rate_pooled"]]
    if rate_moved:
        print(f"\nrate:   {len(rate_moved)} existing page(s) changed new-grantee rate")
        for e in rate_moved[:10]:
            print(f"          {after[e]['slug']}: "
                  f"{before[e]['rate_pooled']} -> {after[e]['rate_pooled']}")
        print("        (expected only where a genuinely new filing was picked up)")

    # ---- drift ------------------------------------------------------------
    drift_new = [e for e in added if after[e].get("drift_review_flag")]
    print(f"\ndrift:  {len(drift_new)} of {len(added)} new page(s) flagged for "
          f"naming drift ({pct(len(drift_new), len(added))})")

    print()
    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        return 1
    print("V7 OK — no page dropped, no slug moved. "
          "Peer movement above is expected; read it before merging.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
