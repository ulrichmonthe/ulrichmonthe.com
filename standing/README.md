# Standing — funder standing analysis

Implements `research/nonprofit-sector-2025-26/SPEC.md`.

```
pipeline/fetch_index.py    filer index from the yearly 990 indices (SPEC §2.1)
pipeline/extract.py        one record per grant PAID (SPEC §2.2–2.3)
pipeline/resolve.py        entity clustering (SPEC §2.4)
pipeline/metrics.py        derived metrics and the publication gate (SPEC §2.5)
pipeline/tests/            V4 and window-edge checks — mandatory
checks/neutrality_lint.py  V6 — published pages carry no imperative language
checks/expansion_diff.py   V7 — what growing the cohort did to live pages
checks/figure_provenance.py V8 — every figure in a draft note recomputes
checks/independent_check.py second implementation, for disagreement hunting
checks/tests/              V7 and V8 self-tests
build_real.py              the published dataset (SPEC §2.6)
build_sample.py            synthetic dataset, kept for pipeline demonstration
build_pages.py             one static page per foundation
data/                      output in SPEC §2.6 format
```

## Run

```
python3 standing/pipeline/tests/test_unresolved_bias.py   # 20 checks
python3 standing/pipeline/tests/test_window_edges.py      # 19 checks
python3 standing/checks/tests/test_checks.py              # 24 checks, V7 + V8
python3 standing/checks/neutrality_lint.py                # V6
python3 scripts/build_sitemap.py --check                  # sitemap matches disk
```

Rebuilding the dataset:

```
python3 standing/pipeline/fetch_index.py 2020 2021 2022 2023 2024
python3 standing/build_real.py 400 --incremental
python3 standing/build_pages.py
python3 scripts/build_sitemap.py
python3 standing/checks/expansion_diff.py <(git show HEAD:standing/data/index.json)
```

`data/pf_index.csv` and `.cache/` are gitignored build artifacts — several
hundred megabytes together, both reproducible from the two commands above.

## Expanding the cohort

`build_real.py N` publishes the top N filers by assets, deterministically
ordered. 118 are published today; 10,700 meet the structural bar, so N is the
growth dial. Always pass `--incremental` above a few hundred: the full path
rewrites and re-fetches every foundation, which costs gigabytes to reproduce
figures that did not change and re-dates `computed_at` on work that was done
months ago.

Peer medians are recomputed across the whole cohort every run, incremental or
not. They are a property of the comparison set, so adding foundations
genuinely moves the number printed under pages already live — `expansion_diff.py`
reports that movement, and fails outright if a page disappeared or a slug
moved. `agents/` runs this weekly.

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
