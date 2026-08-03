# Nonprofit Sector Needs, Coping Strategies, and Evidence of What Works
### Mid-2025 → Mid-2026 | Compiled 30 July 2026

---

## ⚠️ Reliability ceiling — read before citing any number

**No primary document was read in this research.** The session's egress policy returned HTTP 403 for every external host attempted across all six workstreams — including `cep.org`, `urban.org`, `candid.org`, `nff.org`, `grantstation.com`, `philanthropy.com`, `reddit.com`, and control fetches to `example.com` and `wikipedia.org`. Only GitHub and package registries are reachable. This was verified independently at the proxy status endpoint and by direct probe, not merely reported by the agents.

Every figure in this report therefore comes from **web-search result summaries** — a synthesis layer sitting between the source and the researcher. Under the brief's own grading scheme, **the highest grade honestly available is [Reported, snippet-only].** Nothing here is [Documented] in the sense the brief intended, even where the underlying study is rigorous.

**What this means practically:** this report is a **verification queue**, not a citable evidence base. Its findings are strong enough to redirect strategy and to tell you which questions matter. They are not strong enough to publish, quote in a pitch, or put in front of a client. Each workstream file carries a re-verification checklist ordered by value.

Two further constraints: the shared web-search budget hit its session cap, cutting every workstream short of its planned search count (agents completed 16–46 searches against targets of 25–30+); and the practitioner-voice workstream reached **zero** of its three target platforms, because Reddit blocks Anthropic's crawler at the user-agent level and LinkedIn is gated.

**One consequence deserves separate emphasis, because it biases everything below.** The sources that survive this filter — trade press, consultancy blogs, vendor marketing, press releases — are precisely the ones with a commercial or institutional interest in a particular framing. The sources that were blocked — primary research PDFs, practitioner forums, review sites — are the ones with the least. **This research is structurally tilted toward the official narrative and toward vendor optimism, and the tilt cannot be corrected from inside this environment.**

---

## 1. Executive summary

Five findings that should change decisions, each with its strongest number.

### 1. The funder-fit verdict thesis does not hold in the form stated — this is the most consequential finding in the research

Workstream 6 was instructed to attack this claim and found **more disconfirming evidence than for any other claim tested.** Five independent lines converge:

- **The market is structurally closed.** Per Candid research across **112,000+ private foundations, 71% state on Form 990-PF that they do not accept unsolicited requests** — up from ~60% in 2011 and trending one-directionally. Better fit analysis cannot open a door closed by policy.
- **The stated pain is time and customization, not selection.** No survey was found in which "deciding which funders to apply to" ranks as a top grantseeker pain point. Practitioner accounts describe "time, time and time" and the burden that "virtually every funder wants something different."
- **Access is relationship-mediated.** The guidance literature is near-unanimous that warm introductions drive access; 80% of merging nonprofits had a prior relationship.
- **The incumbent market is commoditizing, not underserved.** Candid launched Candid Search in January 2026 **cutting price from $299 to $100/month**, plus a **free year of Premium for nonprofits under $1M revenue**. Incumbents rate 4.6–4.9/5. Aggressive price cuts and free tiers from the category's data monopolist are the signature of commoditization.
- **Funders are moving against application volume.** Only ~10% would accept AI-generated proposals; 23% would not; 67% undecided. A tool that increases application volume accelerates the door-closing that shrinks its own market.

**The residual opportunity is narrower and different:** the ~29% open universe, and *reducing the cost of producing customized, well-matched applications* or *navigating relationship pathways* — not identification or fit scoring.

**Important caveat on this verdict.** It rests on snippet-level evidence, and the pain-point finding is an *absence across a small number of searches*, not a systematic review. It is strong enough to demand the thesis be revised before investment. It is not strong enough to abandon the thesis on. **The correct next step is direct customer discovery, not more desk research.**

### 2. The crisis is real in distribution and false in aggregate

Total US charitable giving reached **$617.20B in 2025 — up 5.7% nominal, 3.0% real, above $600B for the first time ever** (Giving USA 2026). **62% of organizations reported revenue increases** in FY2025. Simultaneously, **39% ran a deficit** (up from 22% in 2022) and **69% lost funding from at least one source**.

Both are true. The honest formulation: *aggregate sector revenue hit a record while distress concentrated sharply among federally-dependent, small, and human-services organizations.* **"Unprecedented sector-wide crisis" is not supported by the aggregate data.** Any positioning built on generalized sector collapse is factually vulnerable — and the segment that *is* in crisis is disproportionately the segment that cannot pay for consulting.

### 3. Foundation funding is a bigger felt pain point than federal funding

**~60% of nonprofit CEOs say foundation grants became harder to secure since January 2025, versus 48% reporting federal difficulty.** Among organizations running a deficit, **~60% cite lower-than-expected foundation giving** as a top contributor. More than **40% experienced reduced foundation funding.**

This inverts the standard "federal pullback" narrative and is the most counterintuitive finding in the dataset. Workstream 1 offers four candidate reconciliations and establishes none — the mechanism is unresolved and is a high-value research target.

### 4. The funder-generosity narrative is largely false as stated

Against a sector self-description of surging payout: **independent-foundation payout remained at 5%, the statutory floor.** Among **466 foundations reporting grant payments for both FYE2024 and FYE2025, total giving was flat at $19.4B in each year** — a matched-panel result, far stronger evidence than cross-sectional intention surveys. The widely-cited "86% will maintain or increase giving" conflates action with inaction.

Real increases exist but are confined to a visible minority of small and midsize foundations and a handful of public leaders (MacArthur reported 7.1% actual payout, ~$647M). **State it as: a visible minority moved meaningfully; the aggregate did not.**

### 5. The AI governance gap is probably a misdiagnosis

The governance framing held up worst of the claims tested. The evidence points instead to **absence of measurement and absence of strategic integration** as the binding constraints:

- The vendor report most cited for the governance gap **names different primary constraints**: 65% describe AI use as "reactive and individual," only 7% have embedded AI into goals, budgets and strategy, and outcome tracking is "very rare."
- A survey **screened for organizations running AI in production** ranks failure causes as **data quality (72%), problem definition (60%), integration (59%), staff distrust (53%)** — policy absent from the top four.
- **74% of AI initiatives began from a vendor use case or platform choice; 12% from a defined problem.**
- **No evidence was found that governance maturity predicts AI outcome achievement.**
- Governance-gap framing is disproportionately produced by parties selling governance frameworks. **Bias flag on the claim itself.**

Governance is plausibly *downstream* of measurement: an organization that does not track outcomes cannot know whether its AI use works, and therefore cannot govern it meaningfully.

---

## 2. Quantitative dashboard

Sponsor flags: **V** vendor/commercial · **A** advocacy/membership · **N** neutral/academic · **F** funder-sector intermediary. All rows are [Reported, snippet-only] unless marked otherwise; the grade shown is the grade the *underlying study* would carry if read directly.

### Funding disruption

| Metric | Value | Source | n | Field dates | Flag |
|---|---|---|---|---|---|
| Lost funding from ≥1 source | 69% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F |
| Reduced federal funding | 36% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F |
| Reduced state/local funding | 34% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F |
| Reduced foundation funding | >40% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F |
| Any government funding disruption | ~33% | Urban Institute | not captured | Apr–Jun 2025 | N |
| — lost grant/contract | 21% | Urban Institute | — | Apr–Jun 2025 | N |
| — delay/pause/freeze | 27% | Urban Institute | — | Apr–Jun 2025 | N |
| — stop-work order | 6% | Urban Institute | — | Apr–Jun 2025 | N |
| **Harder to secure foundation grants** | **~60%** | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F |
| Harder to secure federal funding | 48% | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F |
| Expect further cuts | 84% | NFF 2025 Survey | 2,206 | 2025 | A |

### Financial distress

| Metric | Value | Source | n | Field dates | Flag |
|---|---|---|---|---|---|
| Concerned about financial stability | 71% → 66% | CEP (Aug–Sep 2025 → Feb 2026) | 408 / 380 | — | F |
| **Ran a deficit FY2025** | **39%** (22% in 2022) | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F |
| Operating deficit 2024 | 36% — 10-year high | NFF 2025 Survey | 2,206 | 2025 | A |
| Operating deficit, most recent FY | 36% | Independent Sector | not captured | Dec 2025 | A |
| Repeat respondents with ≥6 months cash | fell 36% → 26% | NFF | subset | 2025 | A |
| Of deficit orgs: cite low foundation giving | ~60% | Candid citing CEP | subset | Feb 2026 | F |
| Have line of credit / borrowed against it | 27% / **83%** | NJ Center for Nonprofits | not captured | Jan–Feb 2026 | A |

> **Discarded:** the widely circulated "52% hold ≤3 months cash" traces only to a corporate-card vendor's social post. **Do not publish.** Roughly 40 further vendor/SEO sources were discarded outright by Workstream 1.

### Demand and capacity

| Metric | Value | Source | n | Field dates | Flag |
|---|---|---|---|---|---|
| Increased demand for services | 73% | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F |
| Expect demand to rise 2026 | 68% | Independent Sector | not captured | Dec 2025 | A |
| …but expanding people served | **only 31%** | Independent Sector | not captured | Dec 2025 | A |
| **Burnout "very much" a concern (CEO self)** | **46% (2026) vs 29% (2025)** | CEP | 380 | Feb 2026 | F |
| Any concern about own burnout | ~89% | CEP | 380 | Feb 2026 | F |
| Burnout significantly affecting staff | 25% vs 17% (2025) | CEP | 380 | Feb 2026 | F |
| Reduced staff size | 30% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F |
| **Nonprofit job cuts, CY2025** | **28,696** | Challenger, Gray & Christmas | census | CY2025 | N |
| Staffing shortages / avg vacancy rate (NJ) | 47% / **18%** | NJ Center for Nonprofits | not captured | Jan–Feb 2026 | A |
| Orgs with ≥21% positions vacant | 11% | Independent Sector | not captured | Dec 2025 | A |

> The Challenger figure is the only externally *counted* workforce number, but its "+409%" framing compares full-year 2025 against an 11-month 2024 window. **Do not repeat the percentage.**

### Giving environment — the disconfirming evidence

| Metric | Value | Source | Field dates | Flag |
|---|---|---|---|---|
| **Total US giving 2025** | **$617.20B, +5.7% nominal / +3.0% real** | Giving USA 2026 | CY2025 | N/A |
| — Individuals | $394.2B (64%) | Giving USA 2026 | CY2025 | N/A |
| — Foundations | $117.15B (19%) | Giving USA 2026 | CY2025 | N/A |
| — Bequests | $62.19B, **+16.6% real** | Giving USA 2026 | CY2025 | N/A |
| Organizations reporting revenue increases | **62%** | via WS6 | FY2025 | — |
| Donor counts CY2025 | **−3.6%** | Fundraising Effectiveness Project | CY2025 | A |
| Donor retention | 43.3% | FEP | CY2025 | A |
| Online / DAF revenue growth | +15% / +44% | M+R Benchmarks 2026 | CY2025 | **V** |
| Foundations expecting to increase giving 2026 | 44.3%, median +5.8% | Candid forecast | late 2025 | F |
| Trust in nonprofits / in philanthropy | 56% (stable) / 29% (−4 pts) | Independent Sector, n=3,000 | 2026 | A |
| Agree nonprofits should disclose AI use | **76%** | Independent Sector, n=3,000 | 2026 | A |

**The central tension of this entire report sits in these two tables:** record aggregate dollars, falling donor counts, rising deficits, collapsing leader morale.

---

## 3. Needs analysis — painkiller vs. vitamin

Classification rule: **painkiller** = behavioral evidence of paying or acting (budget reallocation, hiring, borrowing, cutting). **Vitamin** = stated agreement only.

| Rank | Need | Classification | Behavioral evidence |
|---|---|---|---|
| 1 | **Cash / operating liquidity** | **Painkiller** | 83% of NJ orgs with a line of credit borrowed against it; reserves cohort with ≥6 months cash fell 36%→26%; 30% cut staff |
| 2 | **Replacing lost revenue** | **Painkiller** | 88% pursuing new funders; 76.5% increased private/corporate submissions; 63.1% reduced or eliminated programs |
| 3 | **Staff capacity / burnout relief** | **Painkiller, unmonetized** | 28,696 documented job cuts; 18% vacancy rates. Acute pain, but the response is *cutting*, not *buying* — orgs in this state have no budget |
| 4 | **Reducing grant-application cost** | **Painkiller (weak-moderate)** | Pain is time and customization. Behavioral evidence is orgs applying *more*, not buying tooling |
| 5 | **AI training / strategy** | **Vitamin trending painkiller** | 74% of initiatives started from a vendor use case, not a defined problem — the signature of a vitamin. Only 7% embedded AI into goals and budgets |
| 6 | **AI governance / policy** | **Vitamin** | Policy-prevalence stats conflict 7×; no evidence governance maturity predicts outcomes; demand is mostly template-shaped, and templates are free |
| 7 | **Funder identification / fit** | **Vitamin** | Does not surface as a top-ranked pain point in any survey retrieved; incumbents rated 4.6–4.9/5 and giving product away free |
| 8 | **Compliance / audit readiness** | **Unclassified — latent** | Regulatory change documented (OMB 2 CFR overhaul, target 1 Oct 2026), but appears in **no** Tier-1 survey as a ranked concern. Genuine gap |

**The uncomfortable pattern:** the needs that rank as painkillers are the ones organizations respond to by *spending less*, and the needs that would support a software or consulting purchase rank as vitamins.

---

## 4. Grant-seeking economics deep dive

### The substitution gap — the best-sourced finding in the workstream

Government grants to nonprofits run **~$303B/yr** against **~$107B/yr** in private foundation grantmaking. Foundations would need to raise grantmaking **~282%** to backfill federal money. The conclusion survives even at Urban's lower $240B (2023) figure. **Foundation money cannot substitute for federal money at the sector level.** Any strategy premised on the foundation channel absorbing federal losses is arithmetically unsound.

### The surge thesis — triangulated, but causally misattributed

Two independent surveys measuring **opposite sides of the same transaction** point the same direction:

- **87% of foundation leaders report increased demand** (CEP, n=227 foundations giving ≥$5M, Aug–Sep 2025, 30% response rate)
- **76.5% of grantseekers increased private or corporate submissions** (GrantStation, n=1,056, Jan–Jul 2025) — **vendor-sponsored, self-selected, explicitly "not scientifically conducted" per its own methodology**

Meanwhile supply barely moved: **only ~30% of foundations raised payout beyond plan, median +2 percentage points.** The gap between 87% seeing more demand and 30% adding money *is* the competition story.

**But the causal story fails.** Application volume began rising in **2022, coinciding with ChatGPT**, with good evidence the increase is AI-driven. **A spike beginning in 2022 cannot be caused by a 2025 federal pullback.** Competition almost certainly rose; it is measured only by perception, never by funder administrative data; and it substantially predates the pullback. **Do not use this claim causally.**

### Win rates — the most important methodological finding

**GrantStation publishes no per-application win rate.** What it reports is the share of *organizations* winning *at least one* award, segmented by submission volume — a metric that **rises mechanically with volume**. Anyone citing "82.9% success rate for 3–5 applications" as a win rate is misreading it, and the sector's "apply more, win more" advice is substantially a **denominator artifact**.

**No per-application foundation win rate was found from any source.** Vendor platform data reports 34% overall (30% private foundations); the Grant Professionals Association is cited at 10–30%. The gap is large and unexplained; **the vendor figure should not be used.**

Two incompatible GrantStation win-rate ladders were found (70.1/75.6/82.9/91.8/95.0 versus 62/88/96). If the single-application rate genuinely fell from 70.1% to 62%, that is a headline — it could not be tested without document access. **High-value verification target.**

### Hours and cost per application — a genuine void

Every nonprofit-sector figure (15–20h foundation, 80–200h federal) traces to grant-writing vendors and consultancies **with no published methodology**. The only *measured* time-use study located is academic and cross-sector (von Hippel 2015: 116 PI hours + 55 co-I hours per federal research proposal).

**Workstream 2 deliberately declined to compute a cost-per-application** rather than invent a wage rate — the correct call, and the resulting gap is a finding.

**Rejection economics — declined applications per award, poor-fit submission rates, sunk cost — is essentially undocumented.** This is a hole in the sector's evidence base, not a search failure.

### Disconfirming evidence on competition

- Grantseekers rank **competition only fourth** among barriers (10%), behind staff/time limitations (24%), finding matching opportunities (15%), and increased funder requirements (14%).
- Grant *reliance* **decreased** in H1 2025 (share drawing ≤10% of funding from grants rose 26.0%→28.5%); federal grant-seeking activity **dropped ~12 points to 43.2%**.
- Foundation assets are at all-time highs with giving projected +5–7% in 2026.

**The pool is growing, just slower than demand — a different and weaker claim than the brief assumes.**

### Explicit data gaps

- **NO DATA** on aggregate foundation application volume 2024 vs 2025 vs 2026. No sector-wide counter exists; Candid tracks grants *made*, not applications *received*. Grants-management platforms (Foundant, Fluxx, Submittable, Blackbaud) hold exactly this data and none appears to publish an index. **Ask them directly — this is original-research territory.**
- **NO DATA** on per-application win rates from any non-vendor source.
- **NO DATA** on rejection economics of any kind.

---

## 5. Response catalog and scorecard

| Strategy | Prevalence | Outcome evidence | Grade |
|---|---|---|---|
| Pursue new funders | 88% | None found | [Reported] |
| Increase private/corporate submissions | 76.5% | None found | [Reported] |
| Reduce or eliminate programs | 63.1% | n/a — the outcome *is* the harm | [Reported] |
| Partnerships / shared services / co-location | ~50% | **No post-merger outcome study found** | [Reported] |
| Draw down reserves | ≥6mo cash cohort 36%→26% | n/a | [Reported] |
| Borrow against line of credit | 83% of those holding one (NJ) | None found | [Reported] |
| Reduce staff | 30% | 28,696 counted cuts | [Documented] |
| Delay compensation increases | 46% considering | None found | [Reported] |
| Revenue diversification | Widely urged | **Weak-to-negative** (below) | [Documented] |
| Mergers | ~1%/yr, **unchanged** | Intent grew, completions did not | [Reported] |
| AI adoption | 61–97% (see §6) | Outcome tracking "very rare" | [Reported] |

### Funder-side

| Response | Claim | Reality | Grade |
|---|---|---|---|
| Payout increases | Sector narrative of surging payout | **Independent-foundation payout stayed at 5%; matched panel of 466 foundations flat at $19.4B** | [Documented] against |
| Emergency/rapid-response funding | 64% of foundations | No evidence it reached operating costs | [Announced] |
| More unrestricted grants | 42% of foundations | **>40% of nonprofits report *reduced* foundation funding** | Contradicted |
| More multiyear grants | 28% of foundations | None found | [Announced] |
| Streamlined applications | ~40% of foundations | "There is a weariness in the responses" — grantee survey | [Announced] |
| Trust-based philanthropy | 170+ signatories | **Signature counts only**; funders regressed to pre-pandemic norms once already after 2020 | [Announced] |

### The three claims that came back overstated

**Diversification.** A meta-analysis (Hung & Hager, NVSQ 2019; 40 studies, 296 effects) finds only a **small positive effect, weaker for US nonprofits**. Later work (Choi, NVSQ 2025) finds the volatility benefit **did not persist through the last shock**. This directly undercuts the sector's headline 2025–26 coping strategy.

**Mergers.** Candid's ~1%/year baseline has not moved. Infrastructure and intent grew; completed mergers did not. A circulating "19% recently merged" figure is irreconcilable with the 1% baseline and was discarded.

**Trust-based philanthropy.** Evidenced by signature counts, not behavior change. The sector's paper of record ran an op-ed titled *"Even in an Era of Trust-Based Philanthropy, Grantees Can't Trust Funders"* (19 Oct 2025) and two rebuttals. **The existence of a public argument is itself the finding.**

### Terminology correction

**"The Great Handoff" is not a sector term.** Two targeted searches found exactly one user: a grant-search vendor's marketing page. No research body, association, or trade outlet uses it. The underlying federal→state devolution is real; **the label is not — drop it.**

### Announced-but-unevaluated register

Workstream 5 logs **13 items**; Workstream 6 finds that capacity building, trust-based philanthropy, emergency and bridge funds, mergers, shared services, and nonprofit AI **all lack rigorous outcome evaluation in the window**. The capacity-building literature openly concedes evaluation "has seldom been undertaken."

**Only one design-credible outcome study surfaced** across the entire research program: CEP's *Breaking the Mold* (Feb 2025) on MacKenzie Scott gifts, using survey plus tax-filing data plus a non-recipient comparison group — reporting ~90% improved long-term sustainability and 2× operating cash versus peers. **Median gift $5M; it does not generalize to ordinary general operating support.**

> **Live opportunity:** the Level Up Pledge *builds in* 990-publication verification, its two-year window from 2025 is closing, and nobody appears to have scored it. That is original analysis available to whoever does it first — a credible piece of earned authority rather than another literature review.

---

## 6. AI adoption paradox

### Reconciled adoption statistics

| Source | Adoption | n | Sponsor | Note |
|---|---|---|---|---|
| BDO | 97% | not captured | **V** | Highest; vendor |
| Virtuous / Fundraising.AI | **92%** | 346 | **V** | The widely-cited headline |
| TechSoup | 85.6% "exploring" | 1,300+ | **V** | "Exploring" ≠ adopted |
| AI Equity | ~80% | 850+ | A | — |
| **CEP** | **~66%** | 451 + 215 | **F/N** | **Nationally representative, non-vendor** |
| Google.org | **1 in 5** have half the org using gen AI | — | **V** | Different question, different answer |

**The true range is 61–97%, wider than the brief's 80–92%. Reported adoption correlates inversely with sampling independence:** the most independent survey lands near 66%; vendor surveys land at 92–97%.

**Important honesty note:** question wording **could not be verified for any source**, because no primary document could be opened. The reconciliation hypothesis — that wording explains most of the spread — is supported *inferentially* but is **not demonstrated**. Workstream 3 declined to manufacture the evidence.

**Headline adoption is close to meaningless.** The vendor's own data shows **65% reactive/individual use** against **4% with documented workflows**, and only **7% reporting expanded capability**. "92% adoption" and "one person has a ChatGPT tab open" are the same data point read two ways.

### The high-impact minority

**The profile is thin and single-sourced** — vendor data plus its own marketing blog. Four of the six characteristics the brief asked for — **training approach, leadership involvement, dedicated budget, data readiness — are NO DATA FOUND.** There are **no size controls**, so "governance" is confounded with "larger organization."

**This is the weakest evidence base supporting the most commercially attractive story in the sector.** Treat any "here's what the 7% do differently" content — including your own — as unfounded until primary data exists.

### Named failure modes

From the survey screened for organizations running AI **in production** (n=75): **data quality 72%, problem definition 60%, integration 59%, staff distrust 53%.** And **74% of initiatives began from a vendor use case or platform choice versus 12% from a defined problem.**

**Zero documented incidents were found** after four targeted searches — no fabricated-grant cases, donor-data misuse, or biased-screening incidents. **Beneficiary trust: NO DATA FOUND at all.**

### Governance landscape

Policy-prevalence figures **conflict by 7×**: Virtuous 53% have a policy; AI Equity 6.9%; Whole Whale 10%; TAG 30% (foundations). **Do not cite "47% have no policy" as sector fact.**

Against this: **76% of the public agrees nonprofits should disclose AI use** (Independent Sector, n=3,000, MoE ±2%) — one of the most robust numbers in the entire report, and a genuine reputational exposure independent of the governance-consulting story.

### ⚠️ Source-poisoning warning

A cluster of vivid statistics circulating in the sector — **"33% of AI grant recommendations erroneous," a "Sharke.ai Crisis Report," "350+ grant failures"** — traces to a **single paid press release** syndicated to financial-media pages. Workstream 6 logged it **REJECTED**. It is exactly the kind of citation that would surface first in a casual search and destroy credibility if repeated. **Do not use these figures.**

---

## 7. Quote bank

**All quotes are [SNIPPET-ONLY]. None was read on its source page.** The brief asked for 25–40 fully attributed verbatim quotes; the honest yield is **roughly 30 quoted strings, of which fewer than 10 are fully attributed.** Nothing was invented or paraphrased into quotation. Items marked ⚠ could not be cleanly separated from a summarizer's paraphrase — treat as characterizations.

### Felt pain

> **"The stakes are that we might not make it as an organization."**
> — Anonymous nonprofit leader, CEP *A Sector in Crisis* (fielded Aug–Sep 2025), via Inside Philanthropy. *The single most severe felt-pain statement located.*

> **"We are cutting fat and tightening up operations. But that also means we're all working at 175%, and it is not sustainable."**
> — Nonprofit CEO, CEP *State of Nonprofits 2026* (n=380, Feb 2026)

> **"[O]ur amazing team is overworked and overloaded from demand for services, but we are unable to expand staffing given the current financial [constraints]"**
> — Anonymous nonprofit CEO, CEP *State of Nonprofits 2026*. *(Brackets are the source's truncation.)*

> **"They are the ones who must look into the eyes of someone seeking help and tell them that we cannot provide services for them. It is demoralizing … As the leader, I am carrying the weight home every day."**
> — Anonymous nonprofit leader. ⚠ **Attribution uncertain — source publication not determinable. Re-verify before any use.**

> **"We are increasingly concerned about staff burnout and organizational capacity. Our small team is working tirelessly to bridge funding gaps, reapply for grants, and sustain essential services. Without stable, predictable support, we risk losing key personnel and being forced to scale back core operations…"**
> — Anonymous "2025 respondent." ⚠ **Attribution uncertain.**

> **"devastating because we were a healthy functional organization"**
> — CEO, Center for Neighborhood Technology (Chicago), on ~$1M lost and 5 of 20 staff laid off. Chronicle of Philanthropy layoff tracker, 2026.

> **"we had to change to monthly"**
> — The Campaign Against Hunger (Brooklyn), after losing $3.3M in government funding; food pickups moved from biweekly to monthly. CBS News New York, 2025.

### Sector-level diagnosis

> **"One of the biggest finding is that nonprofits are seeing an increase in demand for their services at the same time that they're seeing really large increases in the burnout of their staff."**
> — Dr. Elisha Smith Arrillaga, VP Research, Center for Effective Philanthropy. National Council of Nonprofits interview, ~May 2026. *(sic)*

> **"This isn't happening at the margins — it's happening in cities and towns across the country, to the organizations people rely on most when they have nowhere else to turn."**
> — Dr. Elisha Smith Arrillaga, CEP, May 2026.

> **"Burnout has intensified dramatically in the last year for nonprofit staff and leadership alike, as their organizations are faced with a combination of increased demand for their work and a tougher funding environment."**
> — Dr. Elisha Smith Arrillaga, CEP, May 2026.

> Nonprofits are **"pausing operations, closing, or merging."**
> — Dr. Elisha Smith Arrillaga, CEP, May 2026. *Partial quote.*

> Staff are operating at **"175 percent,"** which is **"not viable long-term"**; a sector built on overextension **"risks exhausting the very people communities depend on most."** ⚠
> — Starsha Valentine, Partner & Chief Culture Officer, Purpose Possible, 2026.

### Funder behavior and the trust gap

> **"there is a weariness in the responses"**
> — Kari Aanestad, GrantAdvisor, on preliminary grantee-survey results about whether funders will follow through on application-burden reform. Chronicle of Philanthropy. *The most on-point quote located for the trust-based-philanthropy contradiction.*

> **"Even in an Era of Trust-Based Philanthropy, Grantees Can't Trust Funders"**
> — Chronicle of Philanthropy, Opinion, 19 Oct 2025 *(headline, verbatim)*. Drew two published rebuttals.

> **"Funders, stop viewing your tedious and paternalistic requirements as nonprofit 'accountability'"**
> — Vu Le, Nonprofit AF *(post title, verbatim)*.

> **"Let's talk about invitation-only grants. Actually, let's not."**
> — Vu Le, Nonprofit AF *(post title, verbatim)*.

> **"Fear of political retaliation, litigation, or threats to 501(c)(3) status is causing some funders to delay or reconsider investments."**
> — English Hudson Consulting. **[Anecdote]** — consultancy commentary, not survey evidence. Included because it names a chilling-effect mechanism **no Tier-1 survey quantified.**

### Grant-seeking and funder fit

> **"Program officers are seeing more applications than ever, and many are clearly mass-produced."**

> **"Every generic, poorly-matched proposal that lands in a program officer's inbox makes them more likely to close the door to unsolicited applications entirely."**

> **"Why 2026 is the Year to Stop Writing Grant Proposals to Every Foundation"** *(article title, verbatim)* — evidence that **demand for the negative recommendation already exists at the advice layer.** Whether practitioners *act* on it against board pressure is **unvalidated** and requires the forums that could not be reached.

### Named on-record accounts that could NOT be retrieved

The Chronicle of Philanthropy's *"How 6 Leaders Are Navigating Federal Funding Cuts"* is the **highest-value unretrieved quote source** in the project. Identified but unquotable: **Ricshawn Roane** (Executive Director, Weissberg Foundation), **Crystal Rountree** (CEO, Jumpstart for Young Children), **Mitch Stripling** (Pandemic Response Institute, Columbia), and four further leaders. **Priority target on network restoration.**

---

## 8. Data gaps and the practitioner-voice failure

**Workstream 4 did not achieve its brief, and the failure is itself a finding.** Reddit was blocked at three independent layers — WebFetch refused, curl got 403 from the egress proxy, and the search API returned a hard error stating reddit.com is inaccessible to Anthropic's user agent. Ten attempts across four mirrors; **0% reached.** LinkedIn is gated.

**The consequence is structural, not incidental:** the unofficial record of the sector is systematically unavailable to this toolchain, so any research program built on it **over-weights the official survey narrative and consultant marketing content by construction.**

The brief's most valuable category — *"we tried X and Y happened"* — is **nearly empty**. Best artifacts recovered: the Center for Neighborhood Technology CEO's account and The Campaign Against Hunger's shift to monthly pickups.

**Named absences across all six workstreams:**

- No sector-wide foundation application-volume series exists (2024/2025/2026)
- No per-application win rate from any non-vendor source
- No measured time-use study of nonprofit foundation-proposal preparation
- No rejection economics of any kind
- **No survey puts a percentage on "we may close"** — the highest-intensity claim is the least measured, despite national headlines asserting it
- No measured baseline closure rate, so "unprecedented" is not a testable statement. Candid's closure tracker (launched Mar 2026) found ~65 events in three months **with no denominator or baseline**
- No documented AI incidents; **no beneficiary-trust data at all**
- No evidence governance maturity predicts AI outcomes
- Compliance burden appears in **no** Tier-1 survey as a ranked leader concern
- State-association sampling fell short: only NJ is solid (MI form-gated, NY partial, CA out-of-window)

**22 explicit NO-DATA-FOUND entries are logged in Workstream 5 alone.**

---

## 9. Implications appendix

*Kept separate from evidence, and deliberately not used to shape collection.*

### (a) For the funder-fit verdict agent

**The thesis needs revision before investment, and the evidence says so more clearly than expected.** The binding constraint for the majority of foundation capital is **access, not identification** — 71% of the universe is closed by policy, and no amount of fit analysis opens it. The stated pain is producing customized applications, not choosing targets. The incumbent that owns the underlying data cut price 67% and is giving the product away free to the sub-$1M segment that would feel identification pain most acutely.

**What survives, and is arguably strengthened:** the *bounded refusal* design principle. If funders are closing doors specifically because of mass-produced, poorly-matched proposals, then a tool whose output is "**don't** apply — here's the evidence" runs *with* the grain of where funders are moving, while every volume-increasing tool runs against it. That is a genuine and defensible differentiator. The market for it is just smaller and differently shaped than the brief assumes — and it is a **feature of an application-production workflow**, not a standalone product.

**Three things to do before writing more code:**
1. **Customer discovery, not desk research.** The pain-point finding is an absence across few searches. Ten conversations with development directors would settle in a week what no amount of searching resolved.
2. **Read the review sites directly.** The "no complaints about incumbents" null is *weak* — G2 and Capterra were blocked, so the search looked everywhere except where dissatisfaction would live. This is the single highest-value verification for the product decision.
3. **Test the 29%.** If the open universe is the market, size it properly. That is tractable 990-PF analysis.

### (b) For responsible-AI consulting positioning

**The governance-first pitch is the weakest available position, and it is weak for a reason worth internalizing: the framing is disproportionately produced by people selling governance.** Being on the correct side of that observation is itself differentiating.

The evidence points to **measurement and problem definition** as the binding gaps. **74% of AI initiatives start from a vendor use case rather than a defined problem** — that is the sellable diagnosis, it is empirically grounded, and it reframes the engagement from compliance to value. Governance follows naturally once measurement exists, and lands better as a consequence than as a lead.

**One clean, defensible hook:** **76% of the public thinks nonprofits should disclose AI use** (n=3,000, ±2%) — among the most robust numbers in this report. That is a reputational exposure argument that does not depend on any contested adoption statistic.

**Do not build content on the "7% high-impact" profile.** Four of its six characteristics are NO DATA FOUND, it has no size controls, and it is single-sourced to a vendor.

### (c) Content and GTM

The strongest available position is **counter-narrative, and it is unusually well supported**: the sector is repeating claims its own data does not support. Payout did not rise. Mergers did not surge. Diversification has weak-to-negative evidence. "92% AI adoption" means one person has ChatGPT open. The crisis is distributional, not aggregate.

Four pieces the evidence would carry today:
1. **"Foundation payout didn't rise."** The matched panel of 466 foundations flat at $19.4B against the sector's self-description is the strongest single disconfirmation in the research.
2. **"The win rate you've been quoted isn't a win rate."** The GrantStation denominator artifact is a genuine methodological catch and useful to every grant professional who reads it.
3. **Score the Level Up Pledge.** Verification is built in, the window is closing, nobody has done it. Original analysis beats commentary.
4. **"Your AI problem is a measurement problem."** Directly counter-positions the governance-template crowd.

**And the honest constraint on all of it:** every number above needs verification against a primary document before publication. Publishing snippet-sourced statistics while positioning as the person who checks sources would be self-refuting.

### Where the evidence argues against the current thesis — stated plainly

- Funder-fit is a **vitamin** by the brief's own test, not a painkiller.
- The incumbent market is **commoditizing**, with the data monopolist pricing toward zero for the most sympathetic segment.
- The organizations in acute pain are **cutting**, not buying — the pain and the budget are in different organizations.
- AI governance, the natural consulting anchor, is **likely misdiagnosed**.
- The sector-crisis framing that motivates urgency is **half-true**, and the aggregate data contradicts it.

**None of this says stop. It says the current framing is aimed at the wrong bottleneck, and the fix is customer discovery rather than more research.**

---

## 10. Source log and verification queue

Full source logs — every URL, credibility note, primary/secondary classification, and fetched-vs-snippet status — are in each workstream file:

| File | Scope | Lines |
|---|---|---|
| `workstreams/01-tier1-surveys.md` | Needs, funding disruption, capacity, compliance | 603 |
| `workstreams/02-grant-economics.md` | Application volumes, win rates, hours/cost | 398 |
| `workstreams/03-ai-adoption.md` | Adoption reconciliation, failure modes, governance | 706 |
| `workstreams/04-practitioner-voice.md` | Practitioner record + access-failure analysis | 666 |
| `workstreams/05-responses-and-funders.md` | Coping strategies, funder responses, 13-item register | 533 |
| `workstreams/06-outcomes-and-disconfirmation.md` | Outcomes, 5-claim disconfirmation, tool landscape | 902 |

### Verification queue, ordered by decision value

1. **G2 / Capterra review text** for Instrumentl, DonorSearch, iWave — the weak null on incumbent dissatisfaction is the highest-leverage unknown for the product decision.
2. **CEP *A Sector in Crisis* and *State of Nonprofits 2026* PDFs** — the backbone of §2 and §3; needed for page-level citation and the survey verbatims.
3. **Chronicle of Philanthropy, *"How 6 Leaders Are Navigating Federal Funding Cuts"*** — the highest-value unretrieved quote source.
4. **GrantStation State of Grantseeking** — resolve the two incompatible win-rate ladders.
5. **Candid 990-PF analysis** — verify the 71% closed-universe figure and size the open 29%.
6. **Reddit r/nonprofit and r/grantwriting** — from an environment that can reach them; the entire practitioner-voice workstream needs a re-run.
7. **Foundant / Fluxx / Submittable / Blackbaud** — ask directly for aggregate application-volume trends. No such index is published; obtaining one would be genuinely novel.

### Sources explicitly rejected

- **"52% of nonprofits hold ≤3 months cash"** — traces to a corporate-card vendor's social post.
- **"33% of AI grant recommendations erroneous" / "Sharke.ai Crisis Report" / "350+ grant failures"** — single paid press release syndicated to financial-media pages.
- **"19% of nonprofits recently merged"** — irreconcilable with Candid's ~1% baseline.
- **"$425B in federal funds frozen"** — untraceable to a primary source.
- **Instrumentl's 34% grant success rate** — vendor platform data, strong selection bias, contradicted by GPA's 10–30%.
- **~40 further vendor/SEO sources** discarded by Workstream 1.
