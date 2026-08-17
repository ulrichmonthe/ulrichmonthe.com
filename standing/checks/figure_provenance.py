"""V8 — every number in a draft note has to be derivable.

A language model writing about a dataset produces figures that are plausible,
well-formed, and occasionally invented. Reading the draft will not catch it:
a made-up median looks exactly like a real one. So the draft alone is not
accepted. It has to arrive with a claims file that says, for every number in
the prose, the expression that produces it — and this check recomputes each
one from the committed data and compares.

That inverts the usual failure. Instead of a reviewer trying to spot the
fabricated statistic, a fabricated statistic has no expression that yields it,
and the check fails on a number no human noticed.

    python3 standing/checks/figure_provenance.py DRAFT.md CLAIMS.json

CLAIMS.json:

    {"claims": [
       {"figure": "87",
        "expr": "count(x for x in F if x['publishable'])",
        "context": "foundations clearing the publication gate"}
    ]}

`figure` is the exact token as it appears in the prose — "87", "33%",
"$25,000", "0.3298". `expr` is evaluated against the data (names below) with
no builtins available. `context` is for the reader, not the checker.

Names in scope:

    F       index rows, one per published foundation (data/index.json)
    pub     the publishable subset of F
    DOCS    full documents, one per foundation (data/foundations/*.json)
    META    index.json's own header — generated, count, as_of_fiscal_year
    count median mean pct share minimum maximum distinct
    len sum sorted round abs min max set list any all

Exit 1 means the draft may not be published.
"""

from __future__ import annotations

import json
import math
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

# Names, not measurements. Stripped before numbers are extracted so the form
# number in "990-PF" is never mistaken for a claim about the data.
VOCABULARY = [
    "990-PF", "990PF", "Form 990", "Part XV", "line 3a", "501(c)(3)",
    "501c3", "Schedule B", "IRS-1", "SPEC §2", "§2.4", "§2.5", "§2.6",
]


def load_data() -> dict:
    with open(os.path.join(DATA, "index.json"), encoding="utf-8") as fh:
        index = json.load(fh)
    rows = index["foundations"]
    docs = []
    fdir = os.path.join(DATA, "foundations")
    if os.path.isdir(fdir):
        for fn in sorted(os.listdir(fdir)):
            if fn.endswith(".json"):
                with open(os.path.join(fdir, fn), encoding="utf-8") as fh:
                    docs.append(json.load(fh))
    meta = {k: v for k, v in index.items() if k != "foundations"}
    return {"F": rows, "pub": [r for r in rows if r["publishable"]],
            "DOCS": docs, "META": meta}


def _seq(x):
    return list(x)


NAMESPACE_FUNCS = {
    "count": lambda x: len(_seq(x)),
    "median": lambda x: statistics.median(_seq(x)),
    "mean": lambda x: statistics.mean(_seq(x)),
    "pct": lambda a, b: 100.0 * a / b if b else float("nan"),
    "share": lambda a, b: a / b if b else float("nan"),
    "minimum": lambda x: min(_seq(x)),
    "maximum": lambda x: max(_seq(x)),
    "distinct": lambda x: len(set(_seq(x))),
    "len": len, "sum": sum, "sorted": sorted, "round": round, "abs": abs,
    "min": min, "max": max, "set": set, "list": list, "any": any, "all": all,
}

DATA_NAMES = ("F", "pub", "DOCS", "META")

# A number in prose: optional $, digits with thousands separators, optional
# decimal part, optional trailing %. Requires a digit boundary so "2.4" inside
# "§2.4" (already stripped) or a version string is not half-matched.
NUMBER = re.compile(r"(?<![\w.])(\$?\d[\d,]*(?:\.\d+)?%?)(?![\w.]*\d)")

# Spelled-out figures are claims too — "thirty of the pages carry a caveat"
# asserts exactly as much as "30" does, and a digits-only scan would wave it
# through. `one` is deliberately absent: in English it is almost always
# structural ("one of the", "no one", "one another") rather than a count, and
# demanding a derivation for it would push the writing into worse prose.
_UNITS = ["", "", "two", "three", "four", "five", "six", "seven", "eight", "nine",
          "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
          "sixteen", "seventeen", "eighteen", "nineteen"]
_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
         "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
WORD_VALUE: dict[str, float] = {w: i for i, w in enumerate(_UNITS) if w}
WORD_VALUE.update(_TENS)
for _t, _tv in _TENS.items():
    for _i, _u in enumerate(_UNITS):
        if _u and _i < 10:
            WORD_VALUE[f"{_t}-{_u}"] = _tv + _i
WORD_VALUE.update({"hundred": 100, "thousand": 1000, "million": 1_000_000})
WORD_RE = re.compile(r"\b(" + "|".join(sorted(WORD_VALUE, key=len, reverse=True))
                     + r")\b", re.I)


def parse_figure(tok: str) -> tuple[float, float]:
    """A prose token -> (value, tolerance).

    Tolerance is half of the last stated place, so "33%" accepts anything
    that rounds to 33% and "0.3298" demands four places. Stating a figure
    more precisely is what tightens the check.
    """
    t = tok.strip()
    if t.lower() in WORD_VALUE:
        return float(WORD_VALUE[t.lower()]), 0.5
    is_pct = t.endswith("%")
    t = t.rstrip("%").lstrip("$").replace(",", "")
    value = float(t)
    places = len(t.split(".")[1]) if "." in t else 0
    tol = 0.5 * (10 ** -places)
    if is_pct:
        value /= 100.0
        tol /= 100.0
    return value, tol


def numbers_in(prose: str) -> list[str]:
    for term in VOCABULARY:
        prose = prose.replace(term, " ")
    # Markdown links, inline code, and HTML comments carry identifiers rather
    # than claims — drop them before scanning.
    prose = re.sub(r"<!--.*?-->", " ", prose, flags=re.S)
    prose = re.sub(r"`[^`]*`", " ", prose)
    prose = re.sub(r"\]\([^)]*\)", "] ", prose)
    return ([m.group(1) for m in NUMBER.finditer(prose)]
            + [m.group(1).lower() for m in WORD_RE.finditer(prose)])


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__.strip())
        return 2
    draft_path, claims_path = sys.argv[1], sys.argv[2]

    with open(draft_path, encoding="utf-8") as fh:
        prose = fh.read()
    with open(claims_path, encoding="utf-8") as fh:
        claims = json.load(fh)["claims"]

    ns = load_data()
    env = {**ns, **NAMESPACE_FUNCS}

    by_figure: dict[str, dict] = {}
    dupes = []
    for c in claims:
        if c["figure"] in by_figure:
            dupes.append(c["figure"])
        by_figure[c["figure"]] = c

    found = numbers_in(prose)
    unique = sorted(set(found), key=lambda t: (-len(t), t))
    print(f"draft   {os.path.basename(draft_path)}: "
          f"{len(found)} numeric token(s), {len(unique)} distinct")
    print(f"claims  {len(claims)} supplied over {len(by_figure)} distinct figure(s)")
    if dupes:
        print(f"        note: repeated figure(s) in claims, last wins: {sorted(set(dupes))}")

    failures: list[str] = []

    # 1. Nothing in the prose may go unclaimed.
    unclaimed = [t for t in unique if t not in by_figure]
    if unclaimed:
        failures.append(f"{len(unclaimed)} figure(s) in the draft have no claim")
        print(f"\nUNCLAIMED ({len(unclaimed)}) — every number must be derivable:")
        for t in unclaimed:
            ctx = re.search(r".{0,60}" + re.escape(t) + r".{0,60}", prose, re.S | re.I)
            snippet = " ".join(ctx.group(0).split()) if ctx else ""
            print(f"          {t:>12}   …{snippet}…")

    # 2. Every claim must recompute to what the prose says.
    print()
    ok = 0
    for tok in sorted(by_figure):
        c = by_figure[tok]
        expr = c["expr"]
        if not any(re.search(rf"\b{n}\b", expr) for n in DATA_NAMES):
            failures.append(f"claim for {tok} does not reference the data")
            print(f"  CONST {tok:>12}   expr touches no data: {expr}")
            continue
        try:
            got = eval(expr, {"__builtins__": {}}, env)  # noqa: S307 — own repo, no builtins
        except Exception as exc:  # noqa: BLE001
            failures.append(f"claim for {tok} failed to evaluate")
            print(f"  ERROR {tok:>12}   {type(exc).__name__}: {exc}")
            continue
        try:
            want, tol = parse_figure(tok)
        except ValueError:
            failures.append(f"claim figure {tok!r} is not a number")
            print(f"  BAD   {tok:>12}   not parseable as a figure")
            continue
        if not isinstance(got, (int, float)) or isinstance(got, bool):
            failures.append(f"claim for {tok} produced {type(got).__name__}, not a number")
            print(f"  TYPE  {tok:>12}   expr returned {type(got).__name__}")
            continue
        if math.isnan(got) or abs(got - want) > tol:
            failures.append(f"claim for {tok} recomputes to {got}")
            print(f"  WRONG {tok:>12}   draft says {want:g}, data gives {got:g}  "
                  f"(tolerance ±{tol:g})")
            print(f"                     {expr}")
            continue
        used = " (unused in draft)" if tok not in unique else ""
        print(f"  ok    {tok:>12} = {got:g}{used}")
        ok += 1

    print(f"\n{ok}/{len(by_figure)} claim(s) verified against "
          f"{len(ns['F'])} foundations")
    if failures:
        print()
        for f in failures[:12]:
            print(f"FAIL  {f}")
        return 1
    print("V8 OK — every figure in the draft recomputes from committed data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
