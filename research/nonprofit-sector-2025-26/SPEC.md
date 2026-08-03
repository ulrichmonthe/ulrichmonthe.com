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
| S4 | Openness Index | `/openness/2026/` | 1 |
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

**This is a CLUSTERING problem, not a lookup.** Read this paragraph twice; getting it wrong is the single most likely way to build a product that is confidently wrong.

The task is to partition one filer's grant records into **grantee identities**. A grantee appearing in exactly one year forms a valid singleton identity — a genuine first-time grantee. "Unresolved" does **not** mean "matched nothing." It means "cannot be assigned to an identity with confidence."

Conflating those two produces catastrophe: if a record matching no prior year is marked unresolved and then excluded, every true new grantee vanishes, every rate collapses toward zero, and every foundation reads as closed. **V4 would still pass.** Do not do this.

**Clustering procedure** (deterministic, within one filer)

Process records in ascending `(tax_year, recipient_name_raw)` order — never input order, which would break V9.

For each record:
1. Compute `normalized_name` and `recipient_state`.
2. If the name is unusable → mark `ambiguous`, do not cluster. Unusable means: empty; or matching a generic placeholder list (`VARIOUS`, `VARIOUS ORGANIZATIONS`, `SEE ATTACHED`, `MULTIPLE RECIPIENTS`, `ANONYMOUS`, `CONFIDENTIAL`); or an individual grant per §2.3.
3. Compare against the **canonical name of each existing cluster only** — never against every member. Canonical = the normalized name of the cluster's earliest record. This makes assignment order-independent within a year and avoids transitive drift.
4. Candidate clusters are those where `same_state` **and** `similarity ≥ 92` (see below).
   - Exactly one candidate → assign, `method: exact` or `fuzzy`, score recorded
   - Zero candidates → **create a new cluster** (this is the normal path for a first-time grantee; it is not an error)
   - Two or more candidates → mark `ambiguous`, do not cluster

**Similarity function — do NOT use bare `token_set_ratio`.**

`token_set_ratio` returns **100** whenever one name's token set is a subset of the other's. `UNIVERSITY OF MICHIGAN` and `UNIVERSITY OF MICHIGAN SCHOOL OF NURSING` score 100. So do `BOYS & GIRLS CLUB` and `BOYS & GIRLS CLUB OF DETROIT`. Both are same-state, both clear 92, and distinct affiliates collapse into one identity — suppressing new-grantee counts and making an open foundation read as closed. That is the mirror image of the bias in §2.4's opening, and V3 and V4 both miss it because over-merging *raises* match rate.

Use instead:

```python
def similarity(a: str, b: str) -> float:
    ta, tb = set(a.split()), set(b.split())
    # Strict-subset guard: extra distinguishing tokens mean different entities
    if ta < tb or tb < ta:
        extra = ta ^ tb
        if len(extra) >= 2 or (extra - STOPWORDS):
            return 0.0
    if min(len(a), len(b)) / max(len(a), len(b)) < 0.6:
        return 0.0
    return rapidfuzz.fuzz.token_sort_ratio(a, b)
```

`STOPWORDS = {OF, THE, AND, FOR, IN, AT, A}`. The guard is the load-bearing part: any distinguishing token beyond a stopword blocks the merge. Prefer a false split (two identities for one org — inflates new-grantee count slightly, visible in V12 sampling) over a false merge (invisible, and biases toward "closed").

**Ambiguity rate**, per foundation, over the window:

```
ambiguous_records = records marked ambiguous in steps 2 or 4
match_rate = 1 − (ambiguous_records / total_grant_records)
```

**The critical rule.** An `ambiguous` record is excluded from **both** the numerator and denominator of every rate, and never counted as a new grantee. A record that legitimately forms a new cluster is **not** ambiguous and **is** counted.

§6/V4 asserts the exclusion; §6/V12 samples clusters by hand to catch over-merging.

### 2.5 T4 — Derived metrics

**Year basis:** use `TaxYr` throughout, never `TaxPeriodEndDt`. A June-FY filer's `TaxYr` is the prior calendar year; mixing the two shifts every window by one. The as-of stamp displays `TaxYr`.

**Deduplication (do before anything else):** if two filings share `(ein, tax_year)`, keep the one with the later `period_end`; on a tie keep the later-received file and log it. Amended returns otherwise double every count *and raise* match rate, so V3 looks healthier while output is wrong.

Window: the most recent **5** tax years present for that filer.

Unit of analysis is the **distinct grantee-year**, not the grant record. Three grants to one organization in one year is one relationship.

```
present(F)   = tax years with a filing, ascending
grantees(y)  = distinct clustered identities in year y (ambiguous excluded)
prior(y)     = grantees of the up-to-3 immediately preceding PRESENT years
new(y)       = grantees(y) − prior(y)
```

**`prior(y)` walks present years, not calendar arithmetic.** For years `[2018, 2022, 2023, 2024]`, `prior(2023) = grantees(2022) ∪ grantees(2018)` — not `{2022}` alone. Calendar arithmetic on a gappy series yields a one-year baseline, counting long-standing grantees as new, which biases open. That is the exact failure this section exists to prevent.

**Eligibility.** Year `y` is eligible when:
- ≥2 present years precede it in the window, **and**
- the gap between `y` and its immediately preceding present year is ≤2 years, **and**
- `|grantees(y)| > 0`

A year failing the gap test is skipped with reason `stale_baseline`. Zero-grant years are skipped but still occupy a window slot and still count as "present" for baselines.

**Two rates, both persisted — they are different quantities and must not be swapped.**

```
# Pooled across eligible years. Grantee-YEARS, so a grantee present in two
# eligible years is counted twice. Used ONLY for the status band.
new_grantee_rate_pooled = Σ|new(y)| / Σ|grantees(y)|

# Most recent eligible year only. Used for the headline sentence.
latest_eligible_year   = max(eligible years)
new_grantee_count_latest = |new(latest_eligible_year)|
total_grantee_count_latest = |grantees(latest_eligible_year)|
```

§4.1's headline renders the **latest-year** pair (`2 of 34 grantees in FY2024`). The status band uses the **pooled** rate. Rendering the pooled numerator against a single-year label would reintroduce, one layer up, exactly the unit error the prototype made.

If `Σ|grantees(y)| = 0` across all eligible years, emit no metrics and set `publishable: false`. Never divide.

Display raw counts first: `2 of 34 grantees`. Percentage secondary.

**Lookback copy must match actual depth.** Never write "prior three years" when `prior(y)` drew on fewer. Persist `lookback_years_used` and render it: "had not funded in the prior [n] years."

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
  "window": {
    "start_year": 2020, "end_year": 2024,
    "years_present": [2020,2021,2022,2023,2024],
    "eligible_years": [2022,2023,2024],
    "eligible_year_count": 3,
    "latest_eligible_year": 2024,
    "skipped_years": [{ "year": 2021, "reason": "stale_baseline" }]
  },
  "quality": {
    "match_rate": 0.94,
    "total_grant_records": 187,
    "ambiguous_records": 11,
    "clusters_formed": 62,
    "publishable": true,
    "individual_grants_excluded": 3,
    "duplicate_filings_dropped": 0
  },
  "metrics": {
    "new_grantee_count_latest": 14,
    "total_grantee_count_latest": 45,
    "lookback_years_used": 3,
    "new_grantee_rate_pooled": 0.311,
    "total_grantee_count_pooled": 128,
    "peer_median_new_grantee_rate": 0.19,
    "peer_basis": "assets+ntee",
    "peer_cell_size": 87,
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
publishable = (match_rate >= 0.85)
          AND (eligible_year_count >= 2)
          AND (total_grantee_count_pooled >= 10)
          AND (latest_eligible_year >= current_year - 3)
```

With a 5-year window and eligibility requiring 2 preceding present years, a filer needs **4 present years** to reach 2 eligible years. Filers with 3 present years produce exactly 1 eligible year and are **not publishable** — this is intentional, and it is why §2.5 uses a 5-year window rather than 4.

Foundations failing the gate render the **insufficient-data template**, which states which condition failed and shows no comparison. Build it for every failing foundation — "only if they have search demand" was unimplementable, since no search-volume source exists in §2.1. Cost is a static page.

**Peer cells.** Band on BMF assets (`<$1M`, `$1–10M`, `$10–100M`, `$100M+`; boundaries inclusive at the lower bound, so exactly $10M lands in `$10–100M`). Serialize as `"<1M"`, `"1-10M"`, `"10-100M"`, `"100M+"`. Peer median is computed over **publishable foundations only, excluding the subject foundation**. Minimum cell size 30; below that, fall back to assets-only and record `peer_basis: "assets"`; below 30 again, emit `null` and render no comparison.

**Peer medians are computed over a gate-selected sample.** Stable naming clears the gate more often, and stable naming correlates with repeat-heavy rosters — so the published corpus skews toward closed foundations and the peer median is biased low. Quantify it (V13) and disclose it on the methodology page. Do not present the median as a population parameter.

This gate is simultaneously the engineering correctness gate and the content-quality gate that keeps a large page count out of scaled-content territory.

---

## 3. Site architecture

```
/foundations/[slug]/                    S1  entity page
/foundations/state/[state]/             S5  state cut
/foundations/state/[state]/small-grants/    S5  Persona A
/foundations/subject/[ntee-slug]/       S5  Persona B
/foundations/invitation-only/           S5  Persona C  (link magnet)
/screen/                                S2  worklist
/openness/2026/                         S4  the study
/openness/2026/methodology/             S4
/openness/new-grantee-rates/            S4  practitioner benchmark cut
/guides/[slug]/                         S6
```

Three route corrections from earlier drafts: `/foundations/[state]/` and `/foundations/[slug]/` were mutually ambiguous, so cuts are namespaced under `state/` and `subject/`; `/index/…` collided with the root `index.html` on GitHub Pages; and the benchmark page moved off `/benchmarks/`, which already exists on the site.

**Subject taxonomy.** `subject` is the **NTEE major group letter** from the BMF, rendered via a fixed 26-entry `ntee_major → {slug, label}` map committed at `standing/data/ntee_map.json` (e.g. `P → {"slug": "human-services", "label": "Human Services"}`). A foundation with no BMF NTEE gets **no subject-cut link**, and V7 must not require one. Do not invent a taxonomy.

**Base URL** is declared once in `standing/config.json` and used for every canonical and sitemap entry.

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

**Title:** `[Name] — Grant History` · fallback when that exceeds 60 chars: `[Name]` truncated to 57 + `…`
The previous suffix (`— Grant History and Application Status`, 38 chars) left 22 characters for the name against a 60-char cap. Most real foundation names do not fit.

**Meta** (target 120–160 chars; the builder must assemble and measure, not concatenate blindly):
`[Name] funded [G] organizations in FY[YYYY]; [M] were new. Grant sizes, recipients and application status from IRS filings.`

With a 21-char name this is ~124. **Truncation ladder** when it exceeds 160: drop `and application status` → drop `Grant sizes, recipients` → truncate the name to fit. Assemble programmatically and assert length; V5 fails the build otherwise.

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
Select 10 foundations spanning asset bands and match rates, **including at least one with a gap year and one with a zero-grant year**. Record the EINs in `checks/v2_sample.json` before running. For each, a human opens the actual filings and computes counts by hand.
- **Grant record count must match exactly**
- **Distinct grantee count per year must match exactly**
- **`new_grantee_count_latest` must match exactly**
- **Pooled rate within 1 percentage point**

Any mismatch: fix, then re-run **the same 10 EINs** — never a fresh sample. Re-drawing after a failure is how a systematic bug survives verification.

This is the only check that can catch a wrong parser. Do not skip it.

### V3 — Match-rate distribution (automated)
Report median, p10, p90 across all foundations.
- Median <0.70 → **fail**, indicates a normalization bug, not bad data
- >30% of foundations below the 0.85 gate → **warn**, review normalization before publishing

**V3 only detects under-matching.** Over-merging *raises* match rate and makes this check look healthier while the output is wrong. V12 covers that direction. Never treat a high match rate as evidence of correctness.

### V4 — Ambiguity-bias assertion (unit test, mandatory)
Fixture: a known repeat grantee's name corrupted so it becomes ambiguous.
- **Assert the new-grantee rate does not increase**
- Assert the record is excluded from numerator and denominator
- Assert match rate drops

**Companion assertion, equally mandatory** — this is what makes V4 meaningful rather than vacuous:
- Fixture with a genuine first-time grantee in the latest eligible year
- **Assert it forms a new cluster, is NOT ambiguous, and IS counted as new**
- Assert `new_grantee_count_latest` increases by exactly 1

Without the second half, an implementation that marks every unmatched record ambiguous — collapsing all rates to zero and making every foundation read closed — passes V4 cleanly. That was a real defect in v1.0 of this spec.

### V12 — Over-merge sampling (manual, mandatory before publication)
Automated checks cannot detect a false merge; it is invisible in every aggregate.

Sample 30 clusters containing ≥2 distinct `recipient_name_raw` values, weighted toward the longest names. A human confirms each cluster is one organization.
- **Any confirmed false merge → fail.** Tighten the §2.4 guard and re-sample.
- Log the sample and outcomes; re-run whenever the similarity function changes.

Priority targets: university systems, hospital networks, `BOYS & GIRLS CLUB OF …`, `UNITED WAY OF …`, `YMCA OF …` — parent/affiliate names are where subset matching does its damage.

### V13 — Selection-bias quantification (automated, gates the Index)
The 0.85 gate selects for stable naming, which correlates with repeat-heavy rosters, so the published corpus skews closed.

- Compute the new-grantee rate for gate-failing foundations using their resolved subset only
- Report both distributions side by side and the delta
- **The Index and methodology pages must publish this delta.** Failing to render it fails the build.

Disclosing the match-rate distribution does **not** disclose this. They are different limitations.

### V5 — Page integrity (automated, every page)
- Exactly one `<h1>`
- Visible as-of fiscal year and recompute date present
- Match rate present wherever a rate is rendered
- `<title>` ≤ 60 chars; meta description 120–160
- Canonical URL present and self-referential
- Valid JSON-LD, correct `@type`
- No page rendered for a foundation with `publishable: false` unless using the explicit insufficient-data template

### V6 — Neutrality lint (automated backstop, NOT a proof)
Templates wrap every block naming a specific foundation in `<div data-foundation-context>`. The lint scans only inside those elements, case-insensitive:

```
do not apply, don't apply, avoid, skip this, not worth,
waste of time, bad funder, won't fund you, no chance,
you should, we recommend, futile, pointless, don't bother,
best funders, worst funders
```

Any hit is a **build failure**. Scoping to the marked elements prevents false positives on methodology copy that legitimately discusses avoidance.

**This is a substring blocklist and it is defeatable** — "applying here is likely futile" would pass a naive list, which is why `futile` is on it. It catches careless phrasing, not intent. §0.2 is enforced by human review of every template string; the lint is a net beneath that, and §6's earlier claim that it "mechanically enforces §0.2" was overstated. Extend the list whenever review catches a new phrasing.

### V7 — Link graph (automated)
- Every entity page links to its state cut, and to its subject cut **when `ntee_major` is present**
- Every cut links to the Index
- Zero orphans; zero internal 404s
- **Sitemap completeness:** every rendered route appears in `sitemap.xml`, and every pre-existing site URL enumerated from the tree is preserved. Assert `sitemap_count == rendered_routes + preexisting_routes − redirect_stubs`. Redirect stubs are excluded from the sitemap and carry `noindex`.

The earlier form (`sitemap count == rendered page count`) failed unconditionally, since the sitemap must also carry the 65 pre-existing URLs.

### V8 — Gate enforcement (automated)
`build.py` emits `data/render_manifest.json` mapping `route → {ein, template}`. V8 reads it and asserts that for every route using `foundation.jinja`, the source record satisfies **all four** conditions of §2.7 — `match_rate`, `eligible_year_count`, `total_grantee_count_pooled`, and recency.

v1.0 of this check omitted the grantee-count condition, so a 9-grantee foundation would have rendered on the standard template and passed.

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
- [ ] V12 passes (over-merge sampling) and V13 delta computed
- [ ] 300–500 entity pages, with V5, V6, V7, V8, V9 and V11 all passing
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

## 7.1 Audit trail and remaining known issues

v1.0 of this spec was audited by an engineer reading it cold. It found one defect that would have produced a confidently wrong product, and several that would have blocked or silently diverged. Fixed above:

| Was | Now |
|---|---|
| §2.4 never said what a record was matched *against*. Under the natural reading, every true new grantee became "unresolved" and was excluded — collapsing all rates toward zero, making every foundation read closed, **with V4 still passing** | §2.4 rewritten as explicit clustering; singletons are valid; V4 gains a mandatory companion assertion |
| Bare `token_set_ratio ≥ 92` merges parent and affiliate (`UNIVERSITY OF MICHIGAN` / `… SCHOOL OF NURSING` score 100) | Subset guard + length-ratio floor + `token_sort_ratio`; new manual check V12 |
| `prior(y)` used calendar arithmetic, so a gappy series got a one-year baseline and read open | `prior(y)` walks present years; gap and eligibility rules added |
| Pooled rate computed, single-year figure rendered | Both persisted and separately assigned to band and headline |
| Title and meta templates arithmetically exceeded their own V5 limits | Shortened, with a measured truncation ladder |
| Subject cuts routed and required by V7 with no taxonomy in the data | NTEE major group + committed map; link conditional |
| `eligible_years` used by the gate but absent from the schema | Added, with skip reasons |
| V7 asserted a sitemap count that could never hold | Reformulated to include pre-existing URLs |
| V8 omitted the grantee-count condition | Reads a render manifest, asserts all four |
| Index selection bias undisclosed | V13 quantifies and must render it |
| `/index/` and `/benchmarks/` collided with existing routes | Namespaced under `/openness/` and `/foundations/{state,subject}/` |

**Known issues accepted for v1.0 — decide before Phase 1:**

1. **Phase-0 vertical undecided.** Pick the state and record it here. Blocks nothing technically; blocks starting.
2. **`recipient_state` missing or foreign.** Same-state is required for clustering, so records without a usable US state can never cluster. Interim rule: treat missing state as a wildcard that matches any single candidate but forces `ambiguous` on two or more. Measure how often this fires before trusting it.
3. **Percentile method** for p25/p75 unspecified — use nearest-rank and state it on the methodology page.
4. **Guide copy carries hardcoded statistics** (e.g. the 71% preselected-only figure) that the Index also computes. Nothing checks agreement. Either compute both from the pipeline or add a check before publishing guides.
5. **Currency and negative amounts** — grant amounts are assumed USD and non-negative. Log and exclude negatives rather than summing them.
6. **V9 determinism** needs a canonical form: pin `SOURCE_DATE_EPOCH`, sort all collections, and confine `computed_at` to a single field excluded from the diff.
7. **V11 bootstrap** — "previously published" means the committed `slug_registry.json` at `HEAD`, not prior build output.

## 8. Known risks

| Risk | Mitigation |
|---|---|
| Name matching wrong in the open-looking direction | V4 unit test (both halves); ambiguous excluded from both sides; match rate always shown |
| **Over-merging — wrong in the closed-looking direction, and invisible to every automated check** | §2.4 subset guard; V12 manual sampling. Prefer a false split to a false merge |
| **Index selection bias from the publication gate** | V13 quantifies it; methodology must render the delta |
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
