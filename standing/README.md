# Standing — funder standing analysis

Implements `research/nonprofit-sector-2025-26/SPEC.md`.

```
pipeline/resolve.py   entity clustering (SPEC §2.4)
pipeline/metrics.py   derived metrics (SPEC §2.5)
pipeline/tests/       V4 and window-edge checks — mandatory
checks/               V6 neutrality lint
build_sample.py       demonstration dataset, generated THROUGH the pipeline
data/                 output in SPEC §2.6 format
```

## Run

```
python3 standing/pipeline/tests/test_unresolved_bias.py   # 17 checks
python3 standing/pipeline/tests/test_window_edges.py      # 19 checks
python3 standing/checks/neutrality_lint.py                # V6
python3 standing/build_sample.py                          # regenerate data
```

## Status

The IRS extraction (`extract.py`, SPEC §2.2–2.3) is **not built** — irs.gov is
unreachable from the environment this was developed in. Everything downstream
of extraction is complete and tested. `build_sample.py` stands in, emitting the
identical JSON contract, so replacing it changes nothing else.

## Two things not to undo

**`tests/test_unresolved_bias.py` needs both halves.** Half one asserts an
ambiguous record cannot inflate the rate. Half two asserts a genuine
first-time grantee *is* counted. Without half two the test is vacuous — an
implementation that marks every unmatched record ambiguous collapses all rates
to zero, makes every foundation read closed, and passes half one cleanly.

**The similarity guards in `resolve.py` are load-bearing.** Bare token-set
matching returns 100 when one name's tokens are a subset of another's, merging
`UNIVERSITY OF MICHIGAN` with `UNIVERSITY OF MICHIGAN SCHOOL OF NURSING`. The
numeric guard exists because `PS 128` and `PS 129` are one character apart and
any character-similarity measure scores them as near-identical. Both errors
make open foundations read closed, and no automated check can see them —
over-merging *raises* the match rate.

## A limitation the gate does not cover

Match rate is blind to naming drift. When a preparer renames a repeat grantee,
the record does not become ambiguous — it forms a second cluster. That is a
false split, which inflates the new-grantee rate while match rate stays at
1.00. `singleton_cluster_share` and `drift_review_flag` surface it as a caveat
on the row; they deliberately do not gate, because genuine turnover and a
renamed grantee are indistinguishable without reading the filings.
