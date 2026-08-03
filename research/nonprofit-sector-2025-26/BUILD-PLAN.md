# Standing — build plan, jobs mapping, and SEO architecture

**Status:** planning · **Date:** 30 July 2026
**Prerequisite not yet met:** the per-filer name-match test (see `DATA-FEASIBILITY.md`). Page counts below are ranges until that runs.

---

## 0. Operating constraints

**Everything is free.** No paywall, no login, no gated export. Three consequences that shape every decision below:

1. **No auth, no backend, no database.** Every surface can be a prerendered static page plus precomputed JSON, screened client-side. That fits the existing GitHub Pages setup, costs nothing to host, and is the fastest thing Google can crawl.
2. **No cannibalization problem.** The usual pSEO tension — how much do we give away before people subscribe — disappears. Give away all of it. Optimize for reach and credibility.
3. **Monetization is the consulting practice and the authority position**, not the tool. The tool's job is to make the author the obvious person to call, and to be the citable source for a statistic nobody else publishes.

**The real cost is maintenance, not hosting.** Twenty thousand pages that go stale are worse than two hundred that don't. Recompute cadence is a launch requirement, not a later concern.

**Voice rule, applied everywhere:** present decision-relevant facts with the context needed to read them. Never issue an imperative about a named real foundation. The reader draws the conclusion and therefore owns it.

---

## 1. What to build

Six surfaces. Each line item traces to a named job from the persona work.

### Surface 1 — Foundation profile `/foundations/[slug]/`

The SEO atom and the highest-traffic page. Most people will only ever see this one.

| Element | Job it serves | Persona |
|---|---|---|
| New-grantee rate, as raw counts first (`2 of 112 grants`) with percentage secondary | "Do they actually fund organizations like us, or is the portal decorative?" | All |
| Peer median alongside it | Makes the number readable without telling anyone what to think | All |
| Grant size distribution + median | "What's a realistic ask?" | A, B |
| **Peer grantees** — who of similar budget/subject/geography they funded | "Are we the kind of org they fund?" — likely the most persuasive element on the page | All |
| Cycle timing from filing and grant dates | "When do they decide?" / "Will they ghost us?" | B, C |
| Unsolicited-proposal status, labeled as self-reported | Sets the baseline expectation | All |
| Match rate + recompute date, always visible | Trust; prevents stale data reading as wrong data | All |
| "As of FY20XX" stamp | Same | All |

**No verdict language.** Descriptive framing only: `Rarely funds new grantees`, `Adds new grantees regularly`, `Insufficient data to compare`.

### Surface 2 — Screening worklist `/screen/`

Client-side, localStorage, no account. Add foundations, get a comparable table, export.

| Element | Job | Persona |
|---|---|---|
| Multi-foundation comparison table | "Build and defend a portfolio for the year" | B, C |
| Hours-at-stake total across the set | Makes the cost of the current plan legible | B, C |
| **Export to CSV and to a clean one-page PDF** | *The boss test.* This is the artifact that goes into a board packet | **B** |
| Client switcher (local, unnamed) | "Qualify prospects across a client book" | **C** |
| Saved screens, local only | Return visits without an account | B, C |

The export is not a nice-to-have. For Persona B the deliverable *is* the internal argument, and if they retype numbers into an email the feature has failed.

### Surface 3 — Shared board history (opt-in, inside `/screen/`)

Off by default. Never runs unless the user pastes their own roster.

- Reports **co-listing only**: "Both listed as directors on Form 990 filings, 2019–2023." Never asserts a relationship.
- Centers the user's own person: *"Dana may have context on this funder — worth asking her."*
- Provenance line on every connection naming the filing it came from.
- Public filings only, stated visibly in the UI as a boundary.
- Per-person suppress control.

### Surface 4 — "How do we look to funders?" — reuse `/live-projects/ein-checker/`

The existing EIN checker and 990 guides already serve the funder's due-diligence view of a nonprofit. Point that lens at the user's own org and Standing becomes the other half of something already built.

Serves Persona A's *"are we even fundable?"* and Persona C's *"should I take this client at all?"*

### Surface 5 — The Foundation Openness Index `/index/openness-2026/`

The authority engine. What share of private foundations added any new grantee last year, cut by asset size, state, and subject.

The research established that no such figure exists from any non-vendor source. This is the piece journalists cite, the piece that earns the links that make Surface 1 rank, and the piece most likely to be absorbed into AI answers. **It is not a marketing byproduct — it is the reason the entity pages can rank at all.**

Falls out of the same extraction as the match test. Build it from the test data.

### Surface 6 — Grantseeker-side guides `/guides/`

The existing nine guides all serve people *checking out* nonprofits — grantmakers doing due diligence. There is currently nothing for people *seeking* money. Specced in §3.

---

## 2. Build sequence

**Phase 0 — the gate (do this first, nothing else matters until it resolves)**
Pull 990-PF XML for one state, three filing years. Compute per-filer name-match rates. Establish what share of foundations clear 85%. That number decides how many entity pages exist and whether the product works at all.

**Phase 1 — prove the atom**
- 300–500 foundation profiles in one vertical (one state, or one subject nationally)
- The Openness Index, built from Phase 0 data
- 4 guides (specced below)
- Watch what indexes, what ranks, what people expand

**Phase 2 — the working surface**
- `/screen/` with export
- Shared board history, opt-in
- Scale entity pages to whatever cleared the match threshold
- Remaining guides

**Phase 3 — the loop**
- "How do we look to funders" integration with the EIN checker
- Recompute pipeline on the annual filing cycle
- Second Openness Index for year-over-year, which is when it becomes a series rather than a one-off

---

## 3. SEO architecture, by persona

Titles are written to length. Every page carries a unique computed figure — no template filler.

### Persona A — Solo ED, sub-$1M, fundraising is one of nine hats

Search behavior: anxious, general, low jargon. They don't know the vocabulary yet.

| URL | Target query | Title tag | Meta description | Unique data |
|---|---|---|---|---|
| `/foundations/[state]/small-grants/` | "grants for small nonprofits in [state]" | Foundations That Fund Small Nonprofits in [State] | [N] [State] foundations made grants under $25,000 last year, and [M] of them funded an organization they had not funded before. Free, no login. | Count of sub-$25k funders + new-grantee count |
| `/guides/find-your-first-foundation/` | "how to find grants for my nonprofit" | How to Find Your First Foundation Funder | A first-principles walkthrough using public filings: how to tell who funds organizations your size, and how to read the signals before you spend 15 hours. | Worked example on a real filing |
| `/guides/realistic-first-ask/` | "how much should I ask for in a grant" | What a Realistic First Ask Looks Like | Foundation grant sizes cluster far more tightly than most first-time applicants expect. What the filing data shows about asking within range. | Grant-size distribution stats |
| `/guides/why-most-foundations-wont-read-it/` | "why do foundations reject applications" | Why Most Foundations Will Never Read Your Proposal | Roughly 7 in 10 private foundations report that they do not accept unsolicited requests. What that means before you write anything. | The 71% figure, sourced |

**Emotional job in the copy:** these pages should relieve the feeling of missing an obvious secret. Plain language, no jargon, and an explicit "this is normal, here's the structure" tone. Persona A's deepest need is *permission to stop chasing everything* — the guides give that through evidence, never through advice.

### Persona B — Development Director, $3–10M

Search behavior: benchmarking, defensibility, named entities. They know the vocabulary and want numbers to put in a deck.

| URL | Target query | Title tag | Meta description | Unique data |
|---|---|---|---|---|
| `/foundations/[state]/[subject]/` | "foundations that fund [subject] in [state]" | [Subject] Funders in [State] — Who Actually Added New Grantees | [N] foundations funded [subject] work in [State]. [M] added at least one new grantee last year. Grant sizes, cycles, and filing-based detail. | Per-cut new-grantee counts |
| `/benchmarks/new-grantee-rates/` | "foundation grant win rate benchmark" | How Often Foundations Fund Someone New — Benchmarks | Median new-grantee rate by foundation size and subject, computed from Form 990-PF filings. The benchmark the sector has never had. | The Index, cut for practitioners |
| `/guides/defend-your-pipeline/` | "grant pipeline board presentation" | How to Defend a Grant Pipeline to Your Board | The question is always "why aren't we applying there." Filing-based evidence you can put in a board packet, with a template. | Downloadable one-pager |
| `/guides/renew-or-pursue/` | "should we reapply to a foundation" | Renew or Pursue: Reading a Funder's Repeat Behavior | Repeat-dollar concentration tells you whether a funder's portfolio has room. How to read it from public filings. | Concentration distribution |

**Social job in the copy:** every page here should produce something quotable in a board meeting. Lead with the number, make it copyable, and offer the export. This persona is not reading for insight — they're shopping for evidence.

### Persona C — Freelance grant writer with a client book

Search behavior: efficiency and qualification. Highest commercial intent, most likely to become a consulting contact.

| URL | Target query | Title tag | Meta description | Unique data |
|---|---|---|---|---|
| `/screen/` | "grant prospect research tool free" | Screen a List of Funders — Free, No Login | Paste a list of foundations. Get new-grantee rates, grant ranges, and peer grantees from public filings. Export to CSV. No account. | The tool |
| `/guides/qualify-a-funder-fast/` | "how to qualify a grant prospect" | Qualify a Funder in Ten Minutes | A repeatable filing-based check that tells you whether a foundation's portfolio has room before you commit billable hours. | Step-by-step on live data |
| `/foundations/invitation-only/` | "foundations that don't accept unsolicited proposals" | Foundations That Do Not Accept Unsolicited Requests | [N] private foundations report on Form 990-PF that they do not take unsolicited applications. Searchable, by state and subject. | The full list — high link magnet |
| `/guides/telling-a-client-no/` | "how to tell a client not to apply for a grant" | How to Tell a Client a Grant Isn't Worth It | The evidence that makes a "no" land as expertise rather than defeatism, and how to put it in front of a board that has already decided. | Script + evidence template |

**Emotional job in the copy:** this persona sells the appearance of landscape expertise. Give them material that makes them look sharper to their own clients — the last guide in particular is a job nobody is serving and it will be disproportionately shared.

### Shared entity layer (all personas)

| URL | Target query | Title pattern |
|---|---|---|
| `/foundations/[slug]/` | "[foundation name] grant application" · "does [foundation] accept unsolicited proposals" | [Foundation Name] — Grant History and Application Status |

Meta pattern: `[Foundation] made [N] grants in FY20XX. [M] went to organizations it had not funded in the prior three years. Grant sizes, past recipients, and application status from public filings.`

This is where the volume is. Nobody currently answers this query well — Candid, ProPublica, and Cause IQ all show financials, none answers whether applying is worth the hours, and the incumbents are commercially prevented from doing so.

### Technical notes

- `Dataset` and `FAQPage` schema on entity pages; `Article` on guides; extend the existing `ld+json` pattern
- **Publish only above the match threshold.** The engineering gate doubles as the content-quality gate that keeps 20,000 pages out of scaled-content territory
- Visible `as of FY20XX` and recompute date on every data page
- Every entity page links to its state and subject cut; every cut links to the Index; the Index links to the methodology. That internal graph is what distributes the authority the Index earns
- Correction path published on every entity page before launch — foundations will write in, and having a visible process is both the ethical and the practical answer

---

## 4. What to measure

Not time on page. Three things:

- **Expand rate on the evidence** for foundations with low new-grantee rates. If people don't open it, they're browsing, not being persuaded.
- **Export rate on `/screen/`.** Proxy for the boss test — did the artifact leave the building?
- **Behavior on "insufficient data" rows.** Bounce means refusal reads as broken; engagement means it reads as honest, which is what the whole design bets on.

---

## 5. Open decisions

1. **Domain.** Entity pages on their own domain, or a subfolder of `ulrichmonthe.com`? The audiences diverge — existing content serves grantmakers doing due diligence, Standing serves grantseekers — but a new domain starts with no authority. Leaning separate, with the Index and guides staying on the consulting site.
2. **Vertical for Phase 1.** One state, or one subject nationally? A subject cut makes a better Index story; a state cut is easier to check by hand.
3. **How much of the Index to give journalists directly.** A pitched embargo to Chronicle or NPQ is worth more than organic discovery for a first release.
