"""V7 and V8 self-tests.

Both checkers are the only thing standing between an agent and published
output, so they get the same treatment as the pipeline: fixtures that assert
they fail on the cases they exist to catch. A checker that passes everything
is worse than no checker, because it is mistaken for coverage.

Run: python3 standing/checks/tests/test_checks.py
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

import expansion_diff  # noqa: E402
import figure_provenance  # noqa: E402

passed = failed = 0


def check(name: str, got, want) -> None:
    global passed, failed
    if got == want:
        passed += 1
    else:
        failed += 1
        print(f"  FAIL {name}: got {got!r}, want {want!r}")


def run(fn, argv: list[str]) -> tuple[int, str]:
    """Call a checker's main() with argv, capturing exit code and output."""
    buf = io.StringIO()
    old = sys.argv
    sys.argv = argv
    try:
        with contextlib.redirect_stdout(buf):
            code = fn()
    finally:
        sys.argv = old
    return code, buf.getvalue()


def row(ein: str, **kw) -> dict:
    d = {"ein": ein, "slug": f"f-{ein}", "name": f"Foundation {ein}", "state": "NY",
         "asset_band": "100M+", "publishable": True, "status_band": "band",
         "match_rate": 1.0, "new_latest": 5, "total_latest": 20,
         "rate_pooled": 0.25, "peer_median": 0.30, "median_grant": 25000.0,
         "lookback": 3, "latest_year": 2024, "gate_failures": [],
         "accepts_unsolicited": False, "drift_review_flag": False,
         "singleton_share": 0.1}
    d.update(kw)
    return d


def write_index(path: str, rows: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"generated": "2026-01-01", "count": len(rows),
                   "as_of_fiscal_year": 2024, "foundations": rows}, fh)


# ------------------------------------------------------------------ V7 diff
print("expansion_diff (V7)")
with tempfile.TemporaryDirectory() as td:
    before = os.path.join(td, "before.json")
    after = os.path.join(td, "after.json")

    base = [row("1"), row("2"), row("3")]
    write_index(before, base)

    # A clean expansion: everything carried over, three added.
    write_index(after, base + [row("4"), row("5"), row("6", publishable=False,
                                                       gate_failures=["match_rate"])])
    code, out = run(expansion_diff.main, ["x", before, after])
    check("clean expansion passes", code, 0)
    check("counts new pages", "+3 new" in out, True)
    check("reports what was withheld", "1  match_rate" in out, True)

    # A page that disappeared — a live URL would start 404ing.
    write_index(after, [row("1"), row("2")])
    code, out = run(expansion_diff.main, ["x", before, after])
    check("dropped page fails", code, 1)
    check("names the dropped slug", "f-3" in out, True)

    # A slug that moved — the old URL is indexed and would break.
    moved = [row("1"), row("2", slug="renamed"), row("3")]
    write_index(after, moved)
    code, out = run(expansion_diff.main, ["x", before, after])
    check("moved slug fails", code, 1)
    check("shows the rename", "f-2" in out and "renamed" in out, True)

    # Peer medians moving is legitimate, and must be reported, not failed.
    shifted = [row("1", peer_median=0.42), row("2"), row("3")]
    write_index(after, shifted)
    code, out = run(expansion_diff.main, ["x", before, after])
    check("peer shift passes", code, 0)
    check("peer shift is reported", "1 existing page(s) changed peer median" in out, True)

    # A rate moving without a rebuild is suspicious and must surface.
    write_index(after, [row("1", rate_pooled=0.9), row("2"), row("3")])
    code, out = run(expansion_diff.main, ["x", before, after])
    check("rate change surfaced", "changed new-grantee rate" in out, True)


# ------------------------------------------------------- V8 figure provenance
print("figure_provenance (V8)")
with tempfile.TemporaryDirectory() as td:
    data = os.path.join(td, "data")
    os.makedirs(os.path.join(data, "foundations"))
    write_index(os.path.join(data, "index.json"),
                [row(str(i), publishable=(i < 8)) for i in range(10)])
    figure_provenance.DATA = data

    draft = os.path.join(td, "d.md")
    claims = os.path.join(td, "c.json")

    def note(text: str, cl: list[dict]) -> tuple[int, str]:
        with open(draft, "w", encoding="utf-8") as fh:
            fh.write(text)
        with open(claims, "w", encoding="utf-8") as fh:
            json.dump({"claims": cl}, fh)
        return run(figure_provenance.main, ["x", draft, claims])

    code, out = note(
        "The dataset holds 10 foundations, of which 8 publish.",
        [{"figure": "10", "expr": "count(F)", "context": "total"},
         {"figure": "8", "expr": "count(pub)", "context": "publishable"}])
    check("correct draft passes", code, 0)

    code, out = note(
        "The dataset holds 10 foundations, of which 9 publish.",
        [{"figure": "10", "expr": "count(F)", "context": "total"},
         {"figure": "9", "expr": "count(pub)", "context": "fabricated"}])
    check("fabricated figure fails", code, 1)
    check("prints both values", "draft says 9, data gives 8" in out, True)

    code, out = note(
        "The dataset holds 10 foundations across 4 states.",
        [{"figure": "10", "expr": "count(F)", "context": "total"}])
    check("unclaimed figure fails", code, 1)
    check("names the unclaimed token", "UNCLAIMED" in out, True)

    code, out = note(
        "The dataset holds 10 foundations.",
        [{"figure": "10", "expr": "10", "context": "constant"}])
    check("constant expression fails", code, 1)
    check("flags the constant", "CONST" in out, True)

    # Spelled-out figures are claims too.
    code, out = note(
        "Eight of the foundations publish.",
        [])
    check("spelled-out figure caught", code, 1)
    check("names the word", "eight" in out.lower(), True)

    code, out = note(
        "Eight of the foundations publish.",
        [{"figure": "eight", "expr": "count(pub)", "context": "publishable"}])
    check("spelled-out figure can be claimed", code, 0)

    # `one` stays usable as ordinary English.
    code, out = note(
        "This is one of several findings; 10 foundations are covered.",
        [{"figure": "10", "expr": "count(F)", "context": "total"}])
    check("structural 'one' is exempt", code, 0)

    # Tolerance follows the precision written.
    code, out = note(
        "80% of the dataset publishes.",
        [{"figure": "80%", "expr": "share(count(pub), count(F))", "context": "share"}])
    check("percentage within tolerance passes", code, 0)

    # Form numbers are names, not measurements.
    code, out = note(
        "Built from Form 990-PF Part XV. It covers 10 foundations.",
        [{"figure": "10", "expr": "count(F)", "context": "total"}])
    check("vocabulary not treated as a claim", code, 0)

    # An expression that blows up is a failure, not a pass.
    code, out = note(
        "There are 10 foundations.",
        [{"figure": "10", "expr": "count(F['nope'])", "context": "broken"}])
    check("broken expression fails", code, 1)

print()
print(f"{passed} passed, {failed} failed")
print("V7 + V8 checks: " + ("OK" if not failed else "FAILING"))
raise SystemExit(1 if failed else 0)
