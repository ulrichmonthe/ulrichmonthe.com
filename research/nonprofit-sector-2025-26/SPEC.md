# Standing — full build specification

**Version:** 1.0 · **Date:** 30 July 2026
**Audience:** an engineer or agent building this from scratch with no prior context.

Read §0 before writing any code. It tells you which facts in this document are verified and which are assumptions you must check first. Building on the unverified ones without checking will produce silently wrong output.

---

## 0. Before you start

### 0.1 What this product is

A free, static website that answers one question about US private foundations that no existing site answers: **does this foundation actually fund organizations it has not funded before?**

It answers by parsing IRS Form 990-PF — the annual return every private foundation must file — comparing each year's grantee list against prior years, and publishing the result as a neutral fact with the context needed to read it.

### 0.2 The one rule that governs all output

**Present decision-relevant facts. Never issue an imperative about a named real foundation.**

Write `2 of 98 grantees were new; the peer median is 19%`.
Never write `Do not apply` or `This foundation is closed` or `Avoid`.

Reason: these are real organizations, the data has known error bars, and a reader who reaches their own conclusion will defend it in a board meeting where a tool's verdict would not survive. §6 defines an automated check that enforces this.

### 0.3 Verified vs. assumed — read this carefully

| Fact | Status |
|---|---|
| `GrantOrContributionPdDurYrGrp` is a repeating element in the 990-PF schema carrying recipient name, address, purpose and amount | **Verified** via IRS MeF schema documentation |
| IRS business rules require ≥1 `GrantOrContributionPdDurYrGrp` entry when contributions paid are reported in Part I line 25 | **Verified** |
| E-filing is mandatory for all private foundations, tax years ending on/after 31 Jul 2020 (Taxpayer First Act) | **Verified** |
| The AWS `irs-form-990` S3 bucket is decommissioned — resolves but returns zero keys | **Verified by direct probe** |
| Current bulk sources: IRS Form 990 series downloads page; GivingTuesday Data Lake | **Reported, not tested** |
| 990-PF grant records contain **no recipient EIN** | **High confidence, verify in T1** |
| All other XML element names in this document | **ASSUMED — verify in T1 before use** |

**T1 (§2.2) exists to resolve the last two rows. Do not skip it.** Every element path below other than `GrantOrContributionPdDurYrGrp` is a plausible guess that must be confirmed against a real filing.

### 0.4 Repository context

Static site, GitHub Pages, custom domain via `CNAME`. Existing conventions to follow, not reinvent:

```
/index.html                     consulting homepage
/guides/[slug]/index.html       9 existing guides, JSON-LD present
/verify/[state]/index.html      51 state pages, unique per-state IRS counts
/live-projects/[tool]/          EIN checker, AI policy generator
/benchmarks/index.html
/sitemap.xml  /robots.txt  /styles/  /assets/
```

Every page is a hand-written or generated `index.html` in a directory. There is no framework. Keep it that way — the build should emit static HTML.

### 0.5 Stack

- **Python 3.11+** for the data pipeline (`lxml`, `rapidfuzz`, `pydantic`)
- **Static generation**: a Python script emitting HTML from Jinja2 templates. No JS framework.
- **Client-side only** for the screening tool: vanilla JS, `localStorage`, fetching prebuilt JSON.
- **No backend, no database, no auth.** Everything is free; nothing needs a server.

---

## 1. Scope

### 1.1 Surfaces

| ID | Surface | Path | Phase |
|---|---|---|---|
| S1 | Foundation profile | `/foundations/[slug]/` | 1 |
| S2 | Screening worklist | `/screen/` | 2 |
| S3 | Shared board history (opt-in, inside S2) | — | 2 |
| S4 | Openness Index | `/index/openness-2026/` | 1 |
| S5 | Cut pages (state, subject, invitation-only) | `/foundations/[cut]/` | 1–2 |
| S6 | Guides | `/guides/[slug]/` | 1–2 |
| S7 | "How do we look to funders" | extends `/live-projects/ein-checker/` | 3 |

### 1.2 Out of scope for v1

- Any paid tier, account, or login
- Grant *deadline* inference — 990-PF carries no grant dates, only the tax period. Deadlines may appear as free text in the application-info group; if present, surface **verbatim** and never infer a cycle from them.
- Peer-grantee **enrichment** (recipient budget/subject). Requires a name→EIN join against the BMF with its own error rate. v1 shows recipient names and amounts verbatim from the filing, which is already more than incumbents present readably.

---

## 2. Data pipeline

### 2.1 Sources

1. **IRS Form 990 series downloads** — `irs.gov/charities-non-profits/form-990-series-downloads`. Official. XML by year/month.
2. **GivingTuesday Data Lake** — S3, full e-file universe plus clean index files.
3. **IRS Business Master File (BMF)** — for foundation metadata (name, state, NTEE, assets). Needed for cut pages and peer bands.

Do **not** target `s3.amazonaws.com/irs-form-990`. It is decommissioned; it returns HTTP 200 with an empty listing, which will read as "no data" rather than as an error.

### 2.2 T1 — Schema discovery (blocking task, do first)

**Goal:** replace every assumed element path in this document with a verified one.

**Procedure**
1. Download 20 990-PF filings spanning ≥3 distinct tax years and a range of foundation sizes.
2. Parse each; emit every distinct element path under the 990-PF return.
3. Locate and record the true paths for:

| Needs | Assumed path (verify) |
|---|---|
| Filer EIN | `ReturnHeader/Filer/EIN` |
| Filer name | `ReturnHeader/Filer/BusinessName/BusinessNameLine1Txt` |
| Tax year | `ReturnHeader/TaxYr` |
| Period end | `ReturnHeader/TaxPeriodEndDt` |
| Grant records (**verified**) | `IRS990PF/GrantOrContributionPdDurYrGrp` |
| Recipient org name | `…/RecipientBusinessName/BusinessNameLine1Txt` |
| Recipient person name | `…/RecipientPersonNm` |
| Recipient state | `…/RecipientUSAddress/StateAbbreviationCd` |
| Grant amount | `…/Amt` |
| Grant purpose | `…/GrantOrContributionPurposeTxt` |
| "Preselected only" indicator | `IRS990PF/OnlyContriToPreselectedInd` |
| Application info / deadlines | `IRS990PF/ApplicationSubmissionInfoGrp` |
| FMV of assets | `IRS990PF/FMVAssetsEOYAmt` |
| **Recipient EIN — confirm ABSENT** | — |

4. **Write findings to `pipeline/schema_map.json`.** All later code reads paths from this file. No element path may be hardcoded elsewhere.

**Verification V1 — must pass before T2**
- `schema_map.json` exists with a resolved path for every row above
- Each path was observed in ≥15 of the 20 sample filings (record the count)
- The recipient-EIN finding is recorded explicitly as present or absent
- Schema version differences across tax years are recorded; if paths differ by year, `schema_map.json` is keyed by year

> If recipient EIN turns out to be **present**, stop and re-read §2.4. Entity resolution becomes a key lookup, match rate ceases to be a limiting factor, and the 85% publication gate can be removed. This would be a materially better product.

### 2.3 T2 — Extraction

For each filing, emit one row per grant record:

```json
{
  "filer_ein": "046000000",
  "filer_name": "HARROWGATE FOUNDATION",
  "tax_year": 2024,
  "period_end": "2024-12-31",
  "recipient_name_raw": "Riverbend Youth Collective, Inc.",
  "recipient_state": "MI",
  "amount": 60000,
  "purpose": "General operating support",
  "is_individual": false
}
```

Rules:
- Skip records where `RecipientPersonNm` is populated and the org name is empty — grants to individuals are not grantee relationships. Count them separately for disclosure; exclude from all rates.
- Preserve `recipient_name_raw` **exactly**. Normalization happens downstream and must never overwrite the source string.
- A filing with contributions reported in Part I line 25 but zero grant records is a **data error** — log it, exclude the foundation, do not treat it as "made no grants."

### 2.4 T3 — Entity resolution

**This is the highest-risk component in the system. The error it produces runs in the direction that makes closed foundations look open.**

Matching is only ever performed **within a single filer's own series** — one foundation's grantee lists across its own years. Never across foundations. Same preparer, usually consistent naming, which makes this tractable where sector-wide matching would not be.

**Normalization**
1. Uppercase; strip accents
2. Remove punctuation except internal `&`
3. Strip leading `THE `
4. Strip trailing legal suffixes: `INC`, `INCORPORATED`, `LLC`, `LTD`, `CORP`, `CORPORATION`, `CO`, `PC`, `PA`
5. Collapse whitespace
6. **Do not** strip `FOUNDATION`, `TRUST`, `FUND`, `SOCIETY`, `ASSOCIATION`, `CENTER`, `INSTITUTE` — these are distinguishing tokens, not noise

**Blocking key:** `normalized_name` + `recipient_state`

**Resolution ladder** (within one filer)
1. Exact normalized-name + state match → `resolved`, `method: exact`
2. `rapidfuzz.token_set_ratio ≥ 92` **and** same state → `resolved`, `method: fuzzy`, score recorded
3. Otherwise → `unresolved`

**The critical rule.** An `unresolved` record is excluded from **both** the numerator and denominator of every rate. It is never counted as a new grantee.

An unresolved name is indistinguishable from a first-time grantee. Counting it as new inflates the new-grantee rate and makes a closed foundation read as open — the precise failure this product exists to prevent. §6/V4 asserts this with a unit test.

**Match rate**, per foundation, over the window:

```
match_rate = resolved_grant_records / total_grant_records
```

### 2.5 T4 — Derived metrics

Window: the most recent **4** tax years available for that filer. Minimum **3** consecutive years, or no metrics are computed.

Unit of analysis is the **distinct grantee-year**, not the grant record. A foundation making three grants to one organization in one year has one grantee relationship, not three.

```
grantees(y)      = distinct resolved recipient identities in year y
prior(y)         = union of grantees(y-1), grantees(y-2), grantees(y-3), limited to years present
new(y)           = grantees(y) − prior(y)
```

Only years having ≥2 prior years in the window are *eligible*.

**New-grantee rate**
```
new_grantee_rate = Σ|new(y)| / Σ|grantees(y)|   over eligible y
```
Display as raw counts first: `2 of 98 grantees`. Percentage secondary.

> **Correction to the existing prototype.** `standing-mvp.html` says "2 of 112 grants." The unit is grantees, not grants. Update prototype copy when implementing.

**Repeat-dollar concentration**
```
repeat_dollar_concentration = Σ amount to grantees ∈ prior(y) / Σ amount to all resolved grantees, over eligible y
```

**Grant size distribution** — `min`, `p25`, `median`, `p75`, `max` of resolved grant amounts in the most recent year.

**Peer median new-grantee rate** — median across foundations in the same asset band and same NTEE major group. Asset bands: `<$1M`, `$1–10M`, `$10–100M`, `$100M+`. NTEE comes from the BMF join; if unavailable, band on assets alone and record which basis was used.

**Accepts unsolicited** — from the preselected-only indicator. Always label as **self-reported**; it is an unaudited checkbox.

**Recipient list** — most recent year's resolved recipients with names and amounts, verbatim.

### 2.6 Output

One file per foundation: `data/foundations/[ein].json`

```json
{
  "ein": "046000000",
  "slug": "harrowgate-foundation",
  "name": "Harrowgate Foundation",
  "state": "MI",
  "ntee_major": "P",
  "asset_band": "10-100M",
  "window": { "start_year": 2021, "end_year": 2024, "years_present": [2021,2022,2023,2024] },
  "quality": {
    "match_rate": 0.94,
    "total_grant_records": 187,
    "resolved_grant_records": 176,
    "publishable": true,
    "individual_grants_excluded": 3
  },
  "metrics": {
    "new_grantee_count": 14,
    "total_grantee_count": 45,
    "new_grantee_rate": 0.311,
    "peer_median_new_grantee_rate": 0.19,
    "peer_basis": "assets+ntee",
    "repeat_dollar_concentration": 0.62,
    "grant_sizes": { "min": 5000, "p25": 25000, "median": 75000, "p75": 150000, "max": 400000 }
  },
  "self_reported": { "accepts_unsolicited": true, "application_info_text": null },
  "recipients_latest_year": [ { "name": "…", "amount": 60000, "purpose": "…", "is_new": false } ],
  "provenance": {
    "source": "IRS Form 990-PF",
    "as_of_fiscal_year": 2024,
    "computed_at": "2026-07-30",
    "next_recompute_expected": "2026-11-01"
  }
}
```

### 2.6.1 Identity and slugs (URL stability — get this right once)

**EIN is the primary key**, never the name. Foundations rename themselves; EINs persist.

Slug generation:
1. Lowercase the filer name as it appears in the **most recent** filing
2. Strip punctuation; replace whitespace with `-`
3. Strip leading `the-`
4. Truncate at 60 chars on a word boundary
5. **On collision, append the last 4 digits of the EIN** — `smith-family-foundation-4821`

**Slugs are immutable once published.** Maintain `data/slug_registry.json` mapping `ein → slug` plus any superseded slugs:

```json
{ "046000000": { "slug": "harrowgate-foundation", "superseded": ["harrowgate-fdn"] } }
```

On rebuild, an EIN already in the registry keeps its slug even if the filer name changed. A changed name emits a `301` entry into `redirects.json` from every superseded slug. Regenerating slugs from names on each build would silently break every inbound link and every citation — the single most damaging reversible mistake available here.

**V11 (automated):** assert every published `ein` appears in the registry; assert no slug maps to two EINs; assert no previously published slug has disappeared without a redirect entry.

### 2.7 Publication gate

```
publishable = (match_rate >= 0.85) AND (eligible_years >= 2) AND (total_grantee_count >= 10)
```

Foundations failing the gate get a page **only** if they have search demand, and that page states what is missing and why no comparison is shown. It never guesses.

This gate is simultaneously the engineering correctness gate and the content-quality gate that keeps a large page count out of scaled-content territory.

---

## 3. Site architecture

```
/foundations/[slug]/                    S1  entity page
/foundations/[state]/                   S5  state cut
/foundations/[state]/small-grants/      S5  Persona A
/foundations/[state]/[subject]/         S5  Persona B
/foundations/invitation-only/           S5  Persona C  (link magnet)
/screen/                                S2  worklist
/index/openness-2026/                   S4  the study
/index/openness-2026/methodology/       S4
/guides/[slug]/                         S6
```

**Internal link graph** — every entity page links to its state cut and subject cut; every cut links to the Index; the Index links to methodology; the methodology links back to a sample of entity pages. This is what distributes the authority the Index earns. Orphans are a build failure (V7).

**Build:** `build.py` reads `data/foundations/*.json` + `templates/*.jinja` → emits `index.html` per route, regenerates `sitemap.xml`. Idempotent: running twice produces byte-identical output.

### 3.1 Repository layout

Everything new lives under `standing/`, leaving the existing site untouched. Rendered pages are written into the site root so GitHub Pages serves them.

```
standing/
  pipeline/
    schema_map.json          T1 output — the only place element paths live
    fetch.py                 source download + local cache
    extract.py               T2  XML → grant records
    resolve.py               T3  entity resolution
    metrics.py               T4  derived metrics
    tests/
      test_unresolved_bias.py    V4 — mandatory, do not delete
      fixtures/
  data/
    foundations/[ein].json   one per foundation
    slug_registry.json       EIN → slug, immutable
    redirects.json           superseded slug → current
    index_openness_2026.json
  templates/
    foundation.jinja  cut.jinja  screen.jinja  index_study.jinja  guide.jinja
  checks/
    neutrality_lint.py       V6
    page_integrity.py        V5
    link_graph.py            V7
  build.py
```

**Sitemap:** `build.py` regenerates `/sitemap.xml` wholesale from rendered routes — never appends. Include `lastmod` from each foundation's `computed_at`. Preserve the 65 existing URLs by enumerating the current site tree, not by hardcoding.

**Redirects:** GitHub Pages has no server-side redirect support. Emit a meta-refresh + canonical stub page at each superseded slug.

---

## 4. Page specifications

### 4.1 S1 — Foundation profile

**Route:** `/foundations/[slug]/`

**Title:** `[Name] — Grant History and Application Status`
**Meta:** `[Name] made [N] grants to [G] organizations in FY[YYYY]. [M] were organizations it had not funded in the prior three years. Grant sizes, recipients, and application status from public filings.`

**Sections in order**
1. **H1** — foundation name. Directly beneath: state, asset band, EIN, `Data as of FY[YYYY]`
2. **Descriptive status line** — one of: `Adds new grantees regularly` · `Adds new grantees occasionally` · `Rarely funds new grantees` · `Not enough data to compare`. Bands: ≥25% / 10–25% / <10% / gate failed. **No imperatives.**
3. **The headline fact** — `[M] of [G] grantees in FY[YYYY] were organizations it had not funded in the prior three years.` Peer median on the next line.
4. **Grant sizes** — distribution with median emphasized
5. **Recipients** — table of the most recent year, new ones marked with a neutral label (`first grant in this window`), never a value-laden one
6. **Application status** — the checkbox value, explicitly labeled self-reported; verbatim application text if present
7. **How this was computed** — match rate, records resolved, window, link to methodology
8. **Corrections** — visible path for a foundation to dispute. Required before launch.
9. Links to state cut, subject cut, Index

**Schema.org:** `Dataset` with `creator`, `dateModified`, `isBasedOn` pointing at the IRS source. Extend the existing `ld+json` pattern.

### 4.2 S2 — Screening worklist `/screen/`

Vanilla JS, `localStorage`, no account. Fetches `data/foundations/*.json` on demand.

- Add foundations by name search or pasted list
- Comparable table: name, new-grantee count/total, peer median, median grant, match rate, as-of year
- Sort by any column
- **Export CSV and a clean print stylesheet for one-page PDF.** For Persona B the export *is* the deliverable; if they retype numbers into an email the feature failed.
- Local named screens ("client A", "client B") for Persona C
- Empty state explains the tool in one sentence and offers a sample screen

### 4.3 S3 — Shared board history (opt-in)

Off by default. Renders nothing until the user pastes their own roster.

- Reports **co-listing only**: `Both listed as directors on Form 990 filings, 2019–2023.` Never asserts that two people know each other.
- Centers the user's person: `Dana may have context on this funder — worth asking her.` Never frames a person as a route to a target.
- Provenance line naming the filing on every connection
- Visible boundary statement: *"Only board and officer listings from public filings are used. No other sources."*
- Per-person remove control
- Roster never leaves the browser. State this in the UI.

### 4.4 S4 — Openness Index

The authority engine, not a marketing byproduct: the entity pages cannot rank without the links it earns. Built from the same extraction as T1–T4.

Publishes: share of private foundations that added ≥1 new grantee in the latest year, cut by asset band, state, and NTEE major group; distribution of new-grantee rates; share reporting preselected-only; and the match-rate distribution as an honest limitation.

Methodology page states sample, window, exclusions, match-rate distribution, and known biases — including that unresolved names are excluded and what that does to the estimate.

### 4.5 S6 — Guides

Full per-persona specs (URLs, titles, metas, target queries) are in `BUILD-PLAN.md` §3. Build order: `/guides/why-most-foundations-wont-read-it/`, `/guides/qualify-a-funder-fast/`, `/guides/telling-a-client-no/`, `/guides/defend-your-pipeline/`.

---

## 5. Copy rules

1. Raw counts before percentages. `2 of 98` outranks `1.8%` for trust.
2. Every data page carries a visible as-of fiscal year and next-recompute date.
3. Self-reported fields always labeled self-reported.
4. Uncertainty stated in the same visual weight as the finding, never in a footnote.
5. No imperative, recommendation, or evaluative adjective attached to a named real foundation.
6. Match rate shown wherever a rate is shown.

---

## 6. Verification

Each check is automated unless marked manual. **The build fails if any check fails.**

### V1 — Schema map (gates T2)
- `schema_map.json` has a resolved path for every required field
- Each path observed in ≥15/20 sample filings, counts recorded
- Recipient-EIN presence recorded explicitly
- Per-year path differences recorded if any

### V2 — Hand verification (manual, gates publication)
Select 10 foundations spanning asset bands and match rates. For each, a human opens the actual filings and computes grantee counts by hand.
- **Grant record count must match exactly**
- **Distinct grantee count must match exactly**
- **New-grantee rate within 1 percentage point**
- Any mismatch: fix and re-run all 10

This is the only check that can catch a systematically wrong parser. Do not skip it.

### V3 — Match-rate distribution (automated)
Report median, p10, p90 across all foundations.
- Median <0.70 → **fail**, indicates a normalization bug, not bad data
- >30% of foundations below the 0.85 gate → **warn**, review normalization before publishing

### V4 — Unresolved-bias assertion (unit test, mandatory)
Construct a fixture where a known repeat grantee's name is corrupted so it fails to resolve.
- **Assert the new-grantee rate does not increase.**
- Assert the record is excluded from numerator and denominator.
- Assert match rate drops.

This test protects the product's core claim. If it is deleted, the product is unsound.

### V5 — Page integrity (automated, every page)
- Exactly one `<h1>`
- Visible as-of fiscal year and recompute date present
- Match rate present wherever a rate is rendered
- `<title>` ≤ 60 chars; meta description 120–160
- Canonical URL present and self-referential
- Valid JSON-LD, correct `@type`
- No page rendered for a foundation with `publishable: false` unless using the explicit insufficient-data template

### V6 — Neutrality lint (automated, mandatory)
Scan all rendered HTML within any foundation-context block for banned patterns, case-insensitive:

```
do not apply, don't apply, avoid, skip this, not worth,
waste of time, bad funder, won't fund you, no chance,
you should, we recommend, best funders, worst
```

Any hit is a **build failure**. This mechanically enforces §0.2. Add to the list as new phrasings appear in review.

### V7 — Link graph (automated)
- Every entity page links to its state cut and subject cut
- Every cut links to the Index
- Zero orphans; zero internal 404s
- `sitemap.xml` count equals rendered page count

### V8 — Gate enforcement (automated)
Assert no page rendered with the standard template has `match_rate < 0.85` or `eligible_years < 2`.

### V9 — Idempotency (automated)
Run `build.py` twice from clean. Output must be byte-identical apart from the build timestamp.

### V11 — Slug stability (automated, mandatory)
- Every published EIN appears in `slug_registry.json`
- No slug maps to more than one EIN
- No previously published slug has vanished without a `redirects.json` entry and a rendered stub
- Re-running the build after mutating a filer name in the source data does **not** change that EIN's slug

Slug drift silently breaks every inbound link and every citation the Index earns. This is the most damaging reversible mistake available in this build.

### V10 — Staleness (automated, scheduled)
Fail the scheduled job if any published page's `next_recompute_expected` is in the past. Stale pages are worse than absent ones.

---

## 7. Definition of done

**Phase 0 — the gate**
- [ ] V1 passes; `schema_map.json` committed
- [ ] One state extracted, ≥3 filing years
- [ ] V3 reported; V4 passing; V11 passing
- [ ] **Deliverable: the share of foundations clearing 0.85.** This number decides the scale of everything else.

**Phase 1 — prove the atom**
- [ ] V2 passes on 10 hand-checked foundations
- [ ] 300–500 entity pages, all of V5–V9 passing
- [ ] Openness Index + methodology published
- [ ] 4 guides live
- [ ] Corrections process live on every entity page

**Phase 2 — the working surface**
- [ ] `/screen/` with CSV + print export
- [ ] S3 opt-in, roster never leaves the browser (verify in devtools)
- [ ] Entity pages scaled to all foundations clearing the gate
- [ ] Remaining guides

**Phase 3 — the loop**
- [ ] EIN-checker integration
- [ ] Scheduled recompute; V10 wired to the schedule
- [ ] Second Index for year-over-year

---

## 8. Known risks

| Risk | Mitigation |
|---|---|
| Name matching wrong in the open-looking direction | V4 unit test; unresolved excluded from both sides; match rate always shown |
| Data 12–24 months stale | As-of stamps everywhere; V10 fails the build on overdue recompute |
| A foundation disputes its page | Corrections process live before launch; facts only, no verdicts, every figure traceable to a filing |
| Scaled-content penalty | 0.85 gate limits count; every page carries unique computed data; Index earns the links |
| Free means unmaintained | Recompute is a Phase 3 checklist item, not an aspiration; V10 enforces it |
| Peer grantees weaker than hoped | v1 ships verbatim names and amounts only; enrichment deferred until the BMF join has a measured error rate |

---

## 9. Related documents

| File | Contents |
|---|---|
| `REPORT.md` | Sector research; why the original funder-fit thesis was revised |
| `DATA-FEASIBILITY.md` | The 990-PF availability check and what it resolved |
| `BUILD-PLAN.md` | Jobs-to-be-done mapping and full per-persona SEO page specs |
| `../../prototypes/standing-mvp.html` | Interactive UI prototype. Note the grants/grantees unit correction in §2.5 |
