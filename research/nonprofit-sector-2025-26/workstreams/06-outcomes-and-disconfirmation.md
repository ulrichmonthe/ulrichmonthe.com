# Workstream 6 — Outcomes Evidence and Systematic Disconfirmation

**Research window:** mid-2025 through mid-2026. **Compiled:** 2026-07-30.

---

## ⚠️ METHODOLOGY LIMITATION — READ FIRST

This workstream was executed under two hard tooling constraints that materially degrade
its evidence quality relative to the brief. Both must be understood before any finding
below is used.

**1. Zero primary documents were retrieved.** Every `WebFetch` call in this session
returned HTTP 403. The agent egress proxy denied `CONNECT` to every host attempted —
including `example.com` — confirming a blanket policy denial rather than site-specific
blocking. Blocked hosts recorded by the proxy include `cep.org`, `nff.org`,
`philanthropy.com`, `instrumentl.com`, `grantstation.com`, `councilofnonprofits.org`,
`nationalacademies.org`, and the HubSpot CDN hosting the Virtuous AI report. Per
`/root/.ccr/README.md` ("do not retry or route around it — report the blocked host"),
no workaround was attempted.

**Consequence: I could not open a single PDF, report, or study.** The brief's core
methodology rule — "primary over secondary, trace to original with page/section" — could
not be satisfied for **any** claim in this document. Everything below is derived from
search-engine result summaries.

**2. The search budget was exhausted mid-research.** This session shares a 200-call
`WebSearch` budget across all six parallel workstreams. It was consumed after **18
searches** by this workstream — well short of the 30+ the brief required. Searches that
were queued and never executed are listed under Data gaps.

**How to read the grades below.** Because nothing was fetched, no claim here can earn a
clean [Documented] grade on its own evidence. Where I write [Documented], it means *the
underlying study appears to use a method capable of documenting a result* (comparison
group, administrative data, meta-analysis) — **not** that I verified the numbers against
the source. Every such claim is additionally tagged `[snippet-only]`. Treat this
document as a **prioritized verification queue**, not as settled findings. Any number
here that matters to a decision must be re-checked against the primary source before use.

---

## Key findings

1. **The single most important finding is an absence.** For the large majority of
   interventions the sector currently promotes — capacity-building grants, trust-based
   philanthropy, revenue diversification pushes, emergency/bridge funds, shared services,
   and nonprofit AI adoption — I found **no rigorous outcome evaluation published in the
   2025–26 window**. Not weak evidence: *no evidence located*. The sector's advocacy for
   these practices runs far ahead of its evidence base, and this gap is itself the
   headline result.

2. **Exactly one intervention in scope appears to have a real, methodologically serious
   outcome study**: CEP's three-year study of MacKenzie Scott's large unrestricted gifts
   ("Breaking the Mold", Feb 2025), which reportedly pairs survey data with tax-filing
   financial data and a **comparison group of non-recipients**. That design feature —
   a counterfactual — is essentially unique in this literature. [snippet-only]

3. **Capacity building is the starkest evidence vacuum.** The literature explicitly
   concedes rigorous evaluation "has seldom been undertaken," and that experimental
   comparison-group designs are considered infeasible. The flagship cited evaluation
   (PropelNext) is a 12-organization, mixed-methods, no-control-group study published in
   2018 — outside the window and not causal.

4. **AI: adoption is near-universal, measured impact is near-zero, and the sector does
   not measure.** The Virtuous/Fundraising.AI 2026 report (n=346) reportedly finds 92%
   AI use but only **7%** reporting major capability improvement, and describes outcome
   tracking as "very rare." Cross-sector, MIT's Project NANDA reported **95% of GenAI
   pilots delivered no measurable P&L impact**. Essentially all nonprofit AI benefit
   claims in circulation are [Reported], not [Documented].

5. **Claim 5 — the client's core product thesis — is the weakest of the five tested.**
   The decisive structural fact: **71% of ~112,000 private foundations state on their
   Form 990-PF that they do not accept unsolicited requests** (Candid, 2025), a figure
   that has risen from ~60% in 2011. Better funder-fit analysis cannot open a door that
   is closed by policy. Combined with a crowded, cheap, well-reviewed incumbent tool
   market (Candid dropped a core product from $299 to $100/month in Jan 2026; free tier
   for orgs under $1M revenue), the "unsolved acute pain point" framing does not survive
   contact with the evidence I found.

6. **"Unprecedented crisis" is half-true and needs disaggregating.** Giving USA 2026
   reports 2025 US charitable giving at a record **$617.20B, +3.0% inflation-adjusted**,
   and roughly **62% of organizations reported revenue increases**. Simultaneously, 39%
   of nonprofits ran a deficit in FY2025 (up from 22% in 2022). The crisis is real but
   **distributional** — concentrated in federally-dependent and small organizations —
   not sector-wide.

7. **Foundations moved less than the rhetoric suggests.** Independent-foundation payout
   reportedly stayed at ~5% in FY2025 and among 466 foundations reporting both years,
   total giving was **flat at $19.4B**. Movement is real but confined to specific
   subsets (midsize foundations, a ~35-signatory pledge, MacArthur at 7.1%).

8. **Measured closure data barely exists.** Candid launched an experimental closure
   tracker in **March 2026** that surfaced **~65 events in three months** — a number
   explicitly described as experimental and non-representative. There is no denominator,
   no baseline churn rate, and no reliable national closure count. Nearly all "closure"
   discourse in the window is *fear-of-closure survey response*, not measured closure.

---

## Documented outcomes

Interventions where a study design capable of measuring a result appears to exist.
**Note the shortness of this list — that is the finding.**

### MacKenzie Scott's large unrestricted gifts — the one strong case
**[Documented — design-credible] [snippet-only]**

- **Study:** Center for Effective Philanthropy, *Breaking the Mold: The Transformative
  Effect of MacKenzie Scott's Big Gifts*, published Feb 2025. Third year of a
  multi-year series (Year 2 report: *Emerging Impacts*, Nov 2023).
- **n / method:** Reported as 1,000+ grantee survey responses — **813 nonprofit leaders
  and 243 foundation leaders** — plus financial data from tax filings for 1,000+
  organizations **including comparable nonprofits that did not receive a grant**.
- **Median grant:** $5 million.
- **Reported findings:** Recipients "strengthened their long-term sustainability after
  funds were spent"; gifts helped strengthen financial stability and increased community
  impact; **the feared negative consequences (e.g. donor crowd-out, organizational
  overwhelm) "have not come to pass, at least not yet."**
- **Sponsor / bias flag:** CEP is a philanthropy-sector research organization and is a
  vocal advocate for unrestricted giving; the study subject is a single donor. Advocacy
  alignment is a real bias risk. **Offsetting:** the reported use of administrative tax
  data plus a non-recipient comparison group is the strongest design encountered
  anywhere in this workstream.
- **Critical caveat:** This documents outcomes of *very large gifts from one donor*
  (median $5M). **It does not generalize to ordinary general operating support**, and
  should not be cited as evidence that unrestricted funding in general improves grantee
  outcomes. Nobody should treat this as settled for the broader GOS question.
- **VERIFY:** `cep.org/wp-content/uploads/2025/02/CEP_Breaking_the_Mold_FNL.pdf` — blocked.

### Revenue diversification — genuinely evaluated, and the answer is "barely"
**[Documented — meta-analytic] [snippet-only]**

- **Study:** ChiaKo Hung & Mark A. Hager, "The Impact of Revenue Diversification on
  Nonprofit Financial Health: A Meta-analysis," *Nonprofit and Voluntary Sector
  Quarterly*, 48(1), Feb 2019, pp. 5–27.
- **Scope:** **40 original studies, 296 statistical effects.**
- **Finding:** a **small, positive, statistically significant** association between
  revenue diversification and nonprofit financial health. Crucially, the study reports
  that **US nonprofits demonstrate weaker (or more negative) effects**, that measurement
  granularity drives effect size, and that the effect **has shifted over time**.
- **Interpretation:** This is the best available evidence on diversification and it does
  **not** support the strong claim that diversification stabilizes budgets. A small
  effect that is weaker in the US and unstable over time is a weak basis for the
  confident "diversify your revenue" advice that dominated 2025–26 sector guidance.
- **Window caveat:** 2019 publication — pre-window. **I found no 2025–26 study measuring
  whether diversification pushes actually replaced lost federal revenue.** See Failures.

### Revenue diversification under crisis conditions — the effect does not survive shocks
**[Documented — quasi-experimental/longitudinal] [snippet-only]**

- **Study:** Su Young Choi, "How Does Nonprofit Revenue Diversification Affect Revenue
  Volatility Before, During, and After External Economic Crisis?", *NVSQ*, 2025
  (doi: 10.1177/08997640251316487).
- **Finding as retrieved:** diversification effectively lowers revenue volatility **under
  normal conditions**, but **this effect did not persist during and after the Recession**;
  certain individual revenue sources were more efficient at reducing volatility during
  downturns.
- **Why this matters enormously for this window:** the entire 2025–26 diversification
  push is a *response to a shock*. This study indicates diversification is precisely
  least protective in exactly the conditions the sector is invoking it for. This is the
  most directly thesis-relevant academic finding I located.
- **Not verified:** abstract-level only; effect sizes, n, and dataset unconfirmed.

### Fundraising / donor retention — real measured panel data, and it is not good
**[Documented — panel data] [snippet-only]**

Association of Fundraising Professionals **Fundraising Effectiveness Project (FEP)**,
quarterly donor-level panel:

| Period | Retention rate | Prior year |
|---|---|---|
| Q1 2025 | 18.1% | 18.3% |
| Q2 2025 (mid-year) | 26.3% | −0.1 pt YoY |
| Q3 2025 | 31.9% | 31.7% |
| Q4 2025 / full year | 43.3% | 43.1% |
| Q1 2026 | ~18% (25.8% on one measure, +0.2 pt) | — |

- **Donor counts fell an estimated −3.6% in 2025 — the fifth consecutive annual decline.**
- **Total dollars raised grew ~+5.0% in 2025**, described as the strongest growth in five years.
- **Bias flag:** FEP is derived from participating CRM vendors' data, not a random
  sample of the sector; it skews toward orgs using major donor software.
  **Critical caveat:** reporting indicates **FEP changed its methodology** during this
  period ("Fewer Donors, More Dollars, and Methodology Changes At FEP", NonProfit Times).
  **Year-over-year comparisons across the methodology change may not be valid.** I could
  not retrieve the methodology note. Do not cite these trend deltas without checking it.
- **What this documents:** the sector is raising more money from fewer, wealthier people.
  It does **not** document that any *intervention* (retention program, monthly giving
  push) worked. **I found zero evaluated donor-retention or monthly-giving interventions
  with measured results.**

### Aggregate sector revenue — measured, and it contradicts the crisis narrative
**[Documented — national estimate] [snippet-only]**

- **Giving USA 2026** (Indiana University Lilly Family School of Philanthropy, published
  June 2026): total US charitable giving reached **$617.20 billion in 2025**, the first
  time above $600B. **+5.7% current dollars, +3.0% inflation-adjusted.** Second-highest
  total on record in real terms.
- All four giving sources rose in current dollars; three of four rose in real terms.
  **Bequests +~20% current (+16.6% real)** — the largest increase of the four sources.
  **Giving to foundations declined.**
- **Bias flag:** Giving USA is a modeled national estimate, not a census, and is produced
  in partnership with the fundraising profession (Giving USA Foundation / The Giving
  Institute). It systematically captures large-donor and bequest activity better than
  small-org revenue. Its strength is direction; its weakness is distribution.

---

## Documented failures

### AI pilots — the largest measured failure in scope
**[Documented — cross-sector, mixed method] [snippet-only]**

- **Study:** MIT Project NANDA, *The GenAI Divide: State of AI in Business 2025*,
  published July 2025.
- **Method as reported:** 52 executive interviews, surveys of 153 leaders, analysis of
  300 public AI deployments.
- **Headline:** **95% of pilots delivered no measurable P&L impact.** Only 5% of
  integrated systems created significant value. **42% of companies reported abandoning
  most AI initiatives.** Over 80% of organizations had piloted tools like ChatGPT or
  Copilot; ~40% reported deployment; benefits accrued to *individual* productivity rather
  than measurable enterprise outcomes.
- **Two mandatory caveats:** (a) **This is cross-sector enterprise research, not
  nonprofit research.** Do not present it as a nonprofit finding. (b) **The 95% figure
  has been publicly contested** — e.g. Marketing AI Institute, "That Viral MIT Study
  Claiming 95% of AI Pilots Fail? Don't Believe the Hype." I could not retrieve either
  the study or the critique, so I cannot adjudicate. Treat 95% as **contested**
  [UNVERIFIED] and cite it with the dispute attached.

### Nonprofit AI — adoption without capability gain
**[Reported — vendor-sponsored survey] [snippet-only]**

- **Source:** Virtuous + Fundraising.AI, *2026 Nonprofit AI Adoption Report*, released
  ~Feb 2026. **n = 346 nonprofits.**
- **Findings as reported:** **92% use AI**; **79% report small-to-moderate efficiency
  gains**; **only 7% report major improvements in organizational capability**; **65%
  describe their use as reactive and individual**; only **7%** have embedded AI into
  goals, budgets and strategy; **nearly half have no formal AI governance policy**;
  **outcome tracking is "very rare,"** with most orgs relying on informal observation
  rather than systematic metrics.
- **Bias flag — significant.** Virtuous is a nonprofit CRM vendor and Fundraising.AI is
  an AI advocacy initiative. Both have a commercial interest in AI adoption. That the
  report nonetheless publishes a **7% major-impact** figure makes the *negative* finding
  more credible, not less — a vendor reporting against interest.
- **The 79% efficiency-gain figure is [Reported], not [Documented]** — self-assessment,
  no baseline, no measurement. Per the brief's own rule, "AI saved us time" is not
  evidence of time saved.

### Claims circulating as evidence that are actually paid PR — flagged for exclusion
**[REJECTED — promotional content, do not cite]**

A cluster of striking statistics circulating in the window traces to a **single GetNews
syndicated press release**, "Small Nonprofits Bleed Funding as Faulty AI Grant Tools
Mislead Research" (July 2025), republished verbatim across barchart.com,
theglobeandmail.com (Markets/GetNews section), and financialcontent.com. Wire syndication
to financial-media pages is a **paid distribution channel**, not editorial coverage.

Claims it makes, **none of which should be used**: that 33% of AI-generated grant
recommendations contain critical errors; that a "Sharke.ai Crisis Report" documented
350+ grant failures across 22 states; that small nonprofits invest up to 200 hours per
federal application at 10–15% success rates; that 36% of small nonprofits operate in
deficit; that 23% of foundations reject AI outright. It also carries a quotation
attributed to Dr. Kate Crawford (USC Annenberg). **[UNVERIFIED]** — I could not verify
the quote, the report's existence, or any methodology. "Sharke.ai" appears to be the
commercial sponsor. **Treat this entire cluster as vendor marketing.** Its wide
circulation is itself a finding about the low evidentiary standards of sector discourse.

### Capacity building — failure to evaluate, rather than evaluated failure
**[Documented absence] [snippet-only]**

The capacity-building literature openly concedes it has not tested itself:

- "Evaluation research to determine the effectiveness of capacity-building interventions
  has **seldom been undertaken**."
- "Consultants and trainers who work with nonprofit organizations have performed **little
  rigorous evaluation** of their capacity-building efforts."
- "It is **not feasible to employ experimental methods** such as comparison group studies
  since there are too many variables that influence organizations over time."
- "Most evaluations have focused on shorter-term outcomes rather than meaningful but hard
  to measure impacts such as improved program quality, enhanced organizational
  performance, and better outcomes for the people nonprofits serve."

**Sources:** a CSUN-hosted PDF, *Strengthening Nonprofits: Capacity Building and
Philanthropy*, and *Evaluating Capacity-Building Efforts for Nonprofit Organizations*
(fundingcapacity.issuelab.org). **Publication dates unconfirmed — both are likely
substantially older than the window.** [UNVERIFIED dates] The absence they describe
nonetheless persisted through this window: **I found no 2025–26 capacity-building outcome
evaluation of any kind.**

### Mergers — a decade on, still no resilience evidence
**[Documented absence] [snippet-only]**

- The reference study is Mission + Strategy's *Mergers as a Strategy for Success* — 25
  Chicago-area mergers, 100+ interviews. Finding retrieved: in **80% of cases a prior
  relationship or collaboration existed** between the merging organizations.
- A **10-year longitudinal revisit is underway in 2026 but has not published results.**
  The original study "could not answer how these mergers played out over time."
- Retrieved characterization: **"the field still has little evidence about whether
  mergers make organizations more resilient over time."**
- **I found no post-merger outcome study, and no documented count of failed or abandoned
  nonprofit mergers, in the 2025–26 window.** Given that mergers were actively promoted
  as a crisis response throughout this period, this is a significant gap.

### Diversification pushes as crisis response — promoted, unmeasured
**[Documented absence]**

Vendor survey data (Instrumentl, 2025) reports **82% of nonprofits pursuing more private
and corporate grants** as their primary adaptation to federal cuts, and **two-thirds
submitting more applications**. Separately, private foundation giving was **projected to
grow 5–7%**, which reporting notes **cannot offset federal losses**.

**No study measures whether these pivots replaced the lost revenue, or over what time
horizon.** Given Choi (2025) — that diversification's volatility-damping effect did not
persist through the last major shock — the prior should be *skeptical*, not optimistic.
This is a live, unanswered, high-stakes question.

### Emergency / bridge funds — no survival-rate evidence whatsoever
**[Documented absence]**

Per CEP data, **64% of foundations provided emergency grants** and numerous rapid-response
and bridge funds launched (including a Charity Bridge Fund platform connecting affected
nonprofits to funders). Reported design limitations: federal awards "may not cover full
program costs," reimbursement cycles lengthen, and restrictions on allowable costs make
it hard to maintain staffing and compliance. Some rapid-response funds explicitly funded
**wind-down costs** — layoffs, transitioning clients to new providers, merger support —
i.e. financing orderly failure rather than survival.

**I found no study comparing survival rates of bridge-fund recipients versus
non-recipients.** The brief's question — "did recipients survive at higher rates?" — has
**no available answer**. This is arguably the single most important unmeasured question
of the window, since emergency capital was the sector's flagship crisis response.

### Advocacy and litigation outcomes
**[NOT RESEARCHED — search budget exhausted]**

I did not reach this topic. No findings. Do not infer absence of evidence from absence of
research here.

---

## Announced-but-unevaluated

The register of interventions treated as working during 2025–26 for which I located **no
outcome evaluation at all**. This list is the workstream's primary deliverable.

| Intervention | Promotion level in window | Outcome evidence located |
|---|---|---|
| **Emergency / bridge funds** | Very high — 64% of foundations | **None.** No survival-rate comparison exists. |
| **Capacity-building grants** | High, continuous | **None in window.** Literature concedes rigorous evaluation "seldom undertaken." |
| **Trust-based philanthropy** | Very high | **None.** No measured burden reduction, no measured grantee outcome change. See below. |
| **Mergers & shared services** | High as crisis response | **None.** Longitudinal revisit in progress, unpublished. |
| **Revenue diversification as crisis response** | Very high — 82% pursuing | **None in window.** Best prior evidence (Hung & Hager; Choi) is weak-to-negative. |
| **Nonprofit AI adoption** | Extreme — 92% adoption | **Self-report only.** Outcome tracking "very rare." 7% report major capability gain. |
| **Donor retention programs / monthly giving pushes** | High | **None.** Panel data on outcomes exists; no evaluated intervention found. |
| **General operating support (beyond Scott)** | Very high | **None generalizable.** Only the Scott study, median gift $5M — not transferable. |
| **Shared services / back office consolidation** | Moderate | **Not researched** (budget exhausted). |

### Trust-based philanthropy: the clearest case of advocacy outrunning evidence

Searched specifically for measured reduction in application/reporting burden and for
measured grantee outcome change. **Found neither.** What exists instead:

- A **CEP finding that 60% of grantees say reporting diverts them from their core work**
  — this measures the *problem*, not any intervention's effect on it. [Reported]
- **Existence proofs, not evaluations:** e.g. Headwaters Foundation's "GO! Grants"
  designed to take under an hour to apply for, with under-a-week turnaround. That an
  application is short is [Announced] design, not [Documented] outcome. No before/after
  aggregate burden measurement was located.
- **NFF 2025:** 40% of respondents said foundation grants had become **less restrictive**
  since late 2022. [Reported] — grantee perception, not measured burden, and not
  attributable to trust-based practice specifically.
- Bridgespan's *The Trust-Based Philanthropy Conundrum* (April 2024) is the most
  substantive critical treatment located, noting that "truly value-adding,
  high-intervention donor strategies are rare" and that there is "no singular solution to
  the trust conundrum." It has itself been critiqued as catering to donors who want to
  retain control. [UNVERIFIED — retrieved via summary only.]

**Verdict: trust-based philanthropy is, as of mid-2026, an unevaluated practice.** I
found grantee *satisfaction* signals and *design* descriptions, and zero measured
outcomes. The brief asked whether there is evidence of improved grantee outcomes "or only
grantee satisfaction." Based on what I retrieved: **only satisfaction, and even that is
thin.**

---

## Systematic disconfirmation

### Claim 1 — "Grant competition has spiked since the federal pullback"

**Searched:** application-volume data at funders; foundation-reported demand increases;
invite-only trends; nonprofit application behavior.

**Evidence for:** 87% of foundation leaders report increased demand for funding (CEP
survey, ~230 foundation leaders) [Reported]. Two-thirds of organizations submitting more
applications; 27% of those who lost federal funding increased application load beyond
plans (Instrumentl 2025 survey — **vendor-sponsored, bias flag**) [Reported]. 85% of
nonprofits report being impacted by federal funding changes; 82% pursuing more private
and corporate grants [Reported]. Reporting that funders "already report record
application volumes and tighter cycles."

**Evidence against / complications found:**
1. **Every data point is self-report.** I found **no funder-side administrative data**
   — no foundation publishing actual application counts before and after. "Increased
   demand" as perceived by program officers is not a measured application-volume series.
2. **Confounding by AI, not by the federal pullback.** Multiple sources attribute rising
   application volume to generative AI lowering the cost of applying, not to federal cuts
   increasing need. Retrieved: funding bodies "from Australia to the United Kingdom have
   seen a sharp rise in applications since 2022, which coincides with the advent of
   ChatGPT, with good evidence suggesting many of these increases are AI-driven." **A
   volume spike beginning in 2022 cannot be caused by a 2025 federal pullback.** This
   materially undercuts the causal story even while supporting the volume claim.
3. **Counter-pressure on the denominator.** Foundations responding by going invite-only,
   shortening cycles, or capping reviewed applications *reduces* the number of
   competitive open opportunities — changing the nature of competition rather than
   simply intensifying it in open competitions.

**Verdict: HOLDS DIRECTIONALLY, FAILS ON CAUSATION AND ON MEASUREMENT.** Competition
almost certainly rose. But (a) it is measured only by perception, never by funder
administrative data, and (b) the increase demonstrably predates the federal pullback and
is substantially AI-driven. Anyone attributing the spike primarily to the federal
pullback is over-claiming. **Do not use this claim causally.**

### Claim 2 — "Governance is the primary gap in nonprofit AI adoption"

**Searched:** nonprofit AI governance policy prevalence; barriers to AI value capture;
measured AI outcomes.

**Evidence for:** "Nearly half of nonprofits report having no formal AI governance
policy" (Virtuous 2026, n=346) [Reported]. Only 15% of foundations had established
written AI guidelines for applicants (2024 survey) [Reported].

**Evidence against — this is the claim that held up worst:**
1. **The same report names a different primary gap.** Virtuous reportedly frames the
   binding constraints as **strategic integration and measurement**, not governance:
   65% describe AI use as "reactive and individual," only 7% have embedded AI into goals,
   budgets and strategy, and **outcome tracking is "very rare."** Governance is listed
   among structural gaps; it is not identified as *the* primary one.
2. **MIT's cross-sector finding points elsewhere entirely** — to workflow integration and
   organizational friction, with benefits stuck at individual rather than enterprise
   level. Governance is not the diagnosis.
3. **A measurement gap logically precedes a governance gap.** An organization that does
   not track outcomes cannot know whether its AI use is working, and therefore cannot
   govern it meaningfully. **Governance is plausibly downstream of measurement.**
4. Governance-gap framing is disproportionately produced by parties selling governance
   frameworks, consulting, and compliance tooling. **Bias flag on the claim itself.**

**Verdict: WEAK — LIKELY MISDIAGNOSED.** The evidence I retrieved points to **absence of
measurement and absence of strategic integration** as the primary gaps, with governance
a secondary and partly derivative issue. I found **no evidence at all** that governance
maturity predicts AI outcome achievement. This claim should be substantially rewritten
before use.

### Claim 3 — "The nonprofit sector is in an unprecedented crisis"

**Searched:** aggregate giving; revenue growth distribution; deficits; sector resilience
counter-narratives.

**Evidence for:** 39% of nonprofits ran a deficit in FY2025, up from 22% in 2022 (CEP)
[Reported]. 37% of NFF respondents operated at a deficit in 2024 vs 13% of repeat
respondents in 2021 (NFF, n=2,206, fielded Jan 30–Mar 14 2025) [Reported]. 73% report
increased demand. Two-thirds of CEOs concerned about financial stability. Roughly $425B
in federal funds reportedly canceled or frozen since 2025 [UNVERIFIED — figure retrieved
via summary; I could not trace it to a primary source and it should be independently
confirmed before use].

**Evidence against — substantial:**
1. **Aggregate giving hit an all-time record.** $617.20B in 2025, **+3.0% real**, first
   time over $600B. Giving grew faster than the cost of living "for the first time in a
   few years."
2. **Most organizations grew.** In FY2025, **62% of organizations reported revenue
   increases**; 25% reported losses; 14% no change. Typical org revenue growth ~4.3% YoY.
   A majority-growing sector is not a sector-wide crisis.
3. **Bequests rose ~20% current / 16.6% real** — the strongest of the four sources.
4. **Deficits are not unprecedented in kind.** A deficit rate rising from ~22% to ~39% is
   serious deterioration but well within historical range for a sector that routinely
   runs planned deficits against reserves.
5. **Baseline problem.** There is **no measured baseline closure rate** against which to
   judge whether current closures are elevated. Without a denominator, "unprecedented" is
   not a testable statement.

**Verdict: HALF TRUE — TRUE IN DISTRIBUTION, FALSE IN AGGREGATE.** The honest formulation
is: *aggregate sector revenue reached a record while distress concentrated sharply among
federally-dependent organizations, small organizations, and those reliant on small-dollar
donors.* Growth accrued to large organizations and mid-to-major gifts; small
organizations and sub-$1,000 giving lagged or declined. **"Unprecedented sector-wide
crisis" is not supported by the aggregate data and should not be used unqualified.**

### Claim 4 — "Foundations have meaningfully increased payout and unrestricted giving"

**Searched:** payout rates FY2024–25; grant dollar changes; unrestricted/multiyear
commitments; pledges.

**Evidence for:** 42% of foundations provided more unrestricted grants than in previous
years; 28% distributed more multiyear grants; 64% provided emergency grants; 86% plan to
maintain or increase giving (CEP) [Reported]. Payout among small foundations (<$10M) rose
9.9%→10.3% and midsize ($10–100M) 6.9%→7.1% in 2024. 1,136 private foundations awarded
4.2% more grant dollars overall in 2024, with a 13.6% jump among midsize foundations.
At least 35 philanthropies signed CHANGE Philanthropy's Level Up pledge (20%+ budget
increase or 8%+ payout for at least two fiscal years). MacArthur committed to a 6% floor
and reported **7.1% actual 2025 charitable spending — ~$647M, ~$190M above budget**
[Documented — self-reported actual].

**Evidence against — the strongest disconfirmation of any of the five claims:**
1. **Headline payout did not move.** "Foundation payout rates in FY2025 overall did not
   meaningfully change from previous years for independent foundations and **remained at
   5%**" — the statutory minimum.
2. **Giving was flat where measured on a consistent panel.** Among **466 foundations
   reporting grant payments for both FYE2024 and FYE2025, total cumulative giving was
   flat: $19.4 billion in each year.** A matched-panel flat result is far stronger
   evidence than cross-sectional intention surveys.
3. **"Maintain or increase" conflates.** 86% planning to "maintain **or** increase" is
   consistent with most foundations doing nothing. The construction hides the null.
4. **Movement is confined to small subsets** — small and midsize foundations, ~35
   pledge signatories, individual leaders like MacArthur. Large foundations, which hold
   most assets, show no aggregate movement.
5. **Giving *to* foundations declined in 2025** (Giving USA), pressuring future payout.
6. **Nonprofits report the opposite experience: more than 40% of CEOs reported *reduced*
   foundation funding** — directly contradicting a general increase.

**Verdict: LARGELY FALSE AS STATED.** Payout stayed at the 5% floor; matched-panel giving
was flat; more than 40% of nonprofits experienced *decreases*. Real increases exist but
are concentrated in a visible minority of small/midsize foundations and a handful of
publicly committed leaders. **The gap between the sector's self-description and the panel
data is the finding.** State it as: *a visible minority moved meaningfully; the aggregate
did not.*

### Claim 5 — "Nonprofits urgently need help deciding which funders to apply to"
**(the client's core product thesis — researched adversarially, as instructed)**

**Searched:** stated grantseeker pain points; funder-fit vs. relationship-based access;
unsolicited-proposal acceptance rates; incumbent tool pricing/adoption/complaints; grant
success rates.

**Evidence for the claim:** Reporting that grantseekers face "lack of time, competition,
and finding opportunities," and that grant writing "includes searching for and
prioritizing potential funders." A structural framing that "more than 1.9 million
organizations vie for support from just 100,000 private and corporate funders."

**Evidence against — five independent lines, all pointing the same way:**

**(a) The addressable market is structurally closed — the decisive fact.**
Per Candid research analyzing **over 112,000 private foundations, 71% report on their
IRS Form 990-PF that they do not accept unsolicited requests for funds.** Only ~29% will
consider a proposal absent an invitation. The trend is one-directional: **~60% in 2011**,
~70% of 87,000+ foundations per Bradford K. Smith (then Foundation Center) in *SSIR*
Winter 2019, a ~72% estimate by 2015, **71% in 2025**. The Sunderland Foundation closed
its open application portal in January 2026.
*Caveat, stated fairly:* this is a **checkbox on a tax form**, and sources note
foundations "may be choosing the easiest path rather than accurately describing their
practices." The true closed share may be lower. But the direction is consistent across
15 years and multiple independent estimates.
**Implication: better funder-fit analysis cannot open a door closed by policy.** For the
majority of foundation capital, the binding constraint is *access*, not *identification*.

**(b) The stated pain point is time and writing, not identification.**
Retrieved characterization of nonprofit leaders' grant challenges: "the three main
challenges... are time, time and time," with foundation grants taking 15–20 hours and
federal grants over 100 hours, and most grantseekers relying on 1–2 people. The
identified difficulty is **producing customized applications** — "virtually every funder
wants something different" — not **choosing whom to apply to**. Funder identification
appears in these accounts as a sub-task, never as the primary bottleneck.
**I found no survey in which "deciding which funders to apply to" ranks as a top
grantseeker pain point.** That is a notable absence for a product thesis.

**(c) Access runs through relationships, and the sector says so explicitly.**
The retrieved guidance literature is near-unanimous that funding follows warm
introductions and prior relationships: personal introductions are "one of the most
effective ways to get a grantmaker's attention"; "that introduction transfers trust";
advice centers on leveraging board members, advisors and existing supporters to reach
foundations. This is corroborated structurally by the merger literature finding that
**80% of merging nonprofits had a prior relationship**, and by the invite-only trend
itself, which converts access into a purely relational asset. **Fit analysis is not the
operative selection mechanism for a large share of foundation dollars.**

**(d) The incumbent market is crowded, mature, well-reviewed, and rapidly getting
cheaper — the opposite of an unsolved problem.**
See the dedicated section below. Decisively: **Candid launched Candid Search on 15 Jan
2026, combining GuideStar and Foundation Directory data, and cut price from $299 to
$100/month**, while offering a **free year of Premium to nonprofits under $1M in revenue**
via its Gold Seal program. Aggressive price cuts and free tiers from the category's
data monopolist are the signature of a **commoditizing** category, not an underserved one.
Incumbent satisfaction is high (Instrumentl 4.9/5 on 128 G2 reviews; DonorSearch 4.6/5
on 226).

**(e) AI is making *more* applications, and funders are responding by closing doors.**
Retrieved: "Program officers are seeing more applications than ever, and many are clearly
mass-produced"; "Every generic, poorly-matched proposal that lands in a program officer's
inbox makes them more likely to close the door to unsolicited applications entirely."
Only ~10% of foundations said they would accept AI-generated proposals; **23% said they
would not; 67% are undecided.** A tool that increases application volume operates
**against** the grain of where funders are moving, and risks accelerating the closure
that shrinks its own market.

**What would have to be true if this problem were acute and unsolved — and isn't:**
- Funder-fit would surface as a top-ranked pain point in grantseeker surveys. **It does
  not appear as such in anything I retrieved.**
- Incumbent tools would be poorly rated. **They are rated 4.6–4.9/5.**
- Incumbent pricing would be rising on strong demand. **Candid cut a core product ~67%
  and gave away a free tier.**
- The universe of applicable funders would be open and growing. **It is 71% closed and
  closing further.**
- Funders would want more applications. **They are capping, shortening cycles, and going
  invite-only.**

**Verdict: THE CLAIM DOES NOT HOLD IN THE FORM STATED.** I set out to disconfirm it and
found more disconfirming evidence than for any other claim tested. The problem as framed
— *nonprofits struggle to decide which funders to apply to, and this is an acute unsolved
need* — is contradicted by (i) a 71%-closed foundation universe, (ii) pain-point data
pointing to time and customization rather than selection, (iii) relationship-mediated
access, (iv) a mature, cheap, well-liked incumbent market that is actively commoditizing,
and (v) funder-side movement against application volume.

**Stated fairly, the residual opportunity is narrower and different:** it lives in the
~29% open universe, and it is more plausibly about **reducing the cost of producing
customized, well-matched applications** and **navigating relationship pathways into
invite-only funders** than about *identification* or *fit scoring*. **Caveat on my own
confidence:** this verdict rests entirely on snippet-level evidence, and the pain-point
finding is an *absence* in a small number of searches, not a systematic survey review. It
is strong enough to demand the thesis be revised before investment, but it should be
re-tested with primary sources and, ideally, direct customer discovery.

---

## Existing funder-fit / prospect-research tool landscape

All pricing **[snippet-only]**, retrieved via search summaries, not vendor pages
(instrumentl.com blocked). **Pricing figures conflict across sources and must be
re-verified directly before any competitive analysis is relied upon.**

### Candid (Foundation Directory / GuideStar / Candid Search) — the incumbent data monopoly
- Public pricing page (as reported, checked 18 Jun 2026): **Free**; **Premium $219/month**;
  **Premium annual $1,199**; **Ultimate annual $1,699**; **Enterprise custom**.
- **Candid Search launched 15 January 2026**, combining GuideStar and Foundation Directory
  data, **cutting price from $299 to $100/month**.
- **"Go for Gold": a free year of Candid Premium** for nonprofits with annual revenue or
  expenses under **$1M** that earn a 2026 Gold Seal of Transparency.
- Underlying dataset: **112,000+ private foundations** (the source of the 71% statistic).
- **Strategic read:** the category's authoritative data holder is cutting price ~67% and
  giving the product away free to the small-org segment. Any new entrant is competing
  against **$0** for the segment most likely to feel funder-identification pain.

### Instrumentl
- **Conflicting reported tiers.** Source A: Discover **$299/mo annual** ($349 monthly),
  Pre-Award **$499/mo**, Full Lifecycle **$999/mo**. Source B: Starter **~$179/mo**
  (annual), Pro **$499/mo** (20 projects; proposal drafting, CRM integrations, peer
  prospecting, finance tracking), Advanced **$899/mo** (40 projects; SSO, API, branded
  reports, dedicated CSM). Enterprise/University custom.
- Annual cost commonly cited in the **$2,150–$3,600** range; **14-day free trial**.
- **G2: 4.9/5 across 128 reviews.**
- Publishes its own market research (grant statistics, 2025 nonprofit survey) — **note
  that several statistics circulating in this workstream originate from a direct
  competitor's marketing content and carry a bias flag.**

### DonorSearch
- **G2: 4.6/5 across 226 reviews** — the largest review base encountered.
- Positioned as the affordable option for organizations "that do not have $20K to drop on
  prospect research." [secondary, vendor-adjacent source]

### iWave / WealthEngine
- Historically top-rated (iWave 95 overall satisfaction vs DonorSearch 79, WealthEngine 69
  in a **2020–21** G2 Grid — **dated, do not present as current**).
- Reported to "price out 80 percent of US nonprofits." [secondary, vendor-adjacent —
  **[UNVERIFIED]**, and note it appears in a competitor's positioning content.]

### GrantStation, Grant Assistant, Grantsights, FundRobin, OpenGrants
- Present in the category. **GrantStation's site was egress-blocked**; I could not
  retrieve pricing or adoption for it. Grantsights and FundRobin appear primarily as
  **comparison/affiliate content publishers** ranking the incumbents — an ecosystem
  pattern that itself indicates a mature, heavily-marketed category.

### User complaints — an honest null
**I searched specifically for negative reviews, cancellations and "not worth it"
complaints and found essentially none.** Search returned overwhelmingly positive ratings
and vendor comparison content. **This is a weak null, not a strong one:** G2 and Capterra
pages were egress-blocked, so I could not read actual review text, and review platforms
are themselves vendor-influenced. **The honest statement is: I found no evidence of
widespread dissatisfaction with incumbent prospect-research tools, and I was unable to
look where such evidence would most likely be.** Direct review-site reading is the single
highest-value follow-up for the product decision.

### Grant success rates — context, heavily caveated
Reported by **Instrumentl** (a vendor, from its own platform data — **strong selection
bias**, since users are self-selected active grantseekers): overall **34%**;
state/local government **52%**; private foundations **30%**; federal **25%**; corporate
**22%**. Smaller foundations 35–45% vs major foundations 15–25%.
**Counter-figure:** the Grant Professionals Association is cited as putting typical
proposal success at **10–30%**. The gap between 34% and 10–30% is large and unexplained;
**the vendor figure should not be used.**

---

## Organizational closures

### Measured
**[Documented — but explicitly experimental and non-representative] [snippet-only]**

- **Candid launched an experimental closure/layoff tracker in March 2026.** In its **first
  three months** it surfaced **close to 65 distinct potential closure or layoff events**
  at US nonprofits.
- **Closures outnumbered layoffs roughly 7 to 1.**
- **Most-cited reason over the three months: non-federal funding cuts** — a genuinely
  counterintuitive finding worth flagging, since sector narrative attributes distress
  primarily to federal cuts.
- Candid's own framing, as retrieved: **"there aren't good statistics available about
  nonprofit closures."**
- **Severe limitations, all acknowledged:** "potential" events, not confirmed
  dissolutions; media-monitoring methodology (surfacing bias toward larger and
  better-covered organizations); three months of data; **no denominator and no baseline
  churn rate**; launched near the end of the research window.

### Named closures / near-closures (all [Anecdote] — individually documented, not a sample)
- **Corporation for Public Broadcasting** — began winding down operations after Congress
  clawed back **$1.1 billion** through FY2027; reported wind-down by **30 September**.
  The largest and best-documented closure of the window.
- **Humanities North Dakota** — federal grant terminated; a **$900,000** FY2025 grant cut
  effective immediately; reported "in limbo"/facing closure.
- **The Breathing Association** (~120 years old) — CEO stated that absent **$2 million**
  in federal funding, the agency would close.
- Also surfaced via Candid's tracker or reporting: **Global Washington**, **Tacoma Arts
  Live**, **Senior Resource Connection** (Ohio, Meals on Wheels), **North Napa Shelter**
  (California). **[UNVERIFIED individually]** — names retrieved from a Substack summary,
  not confirmed against primary reporting.
- At least one reversal was recorded (**a Lamar nonprofit reopened after the federal
  funding freeze lifted**), and one reprieve (**14th and Chestnut Center**) —
  **important**, because it shows announced closures are not all realized and that
  point-in-time counts overstate permanent loss.

### Feared
- **Two-thirds of nonprofit CEOs have concerns about their organization's financial
  stability** (CEP, State of Nonprofits 2026) [Reported].
- **39% ran a deficit in FY2025**, up from 22% in 2022 [Reported].
- **37% of NFF respondents operated at a deficit in 2024**, vs 13% of repeat respondents
  in 2021 (n=2,206) [Reported].

### The critical distinction
**Fear-of-closure data is abundant, well-sampled, and comes from credible surveys.
Measured-closure data is scarce, experimental, three months old, and has no denominator.
These must never be conflated.** A sector where two-thirds of CEOs worry about financial
stability and where an experimental tracker finds ~65 events in three months is **not**
demonstrably a sector experiencing mass closure. **No one can currently state how many US
nonprofits closed in 2025 or 2026, or whether that number is above the historical
baseline.** I attempted to research the historical baseline closure rate; the search
budget was exhausted before that query ran.

---

## Verbatim quotes

**⚠️ Attribution caveat:** because every primary document was egress-blocked, these were
retrieved from **search-engine result summaries**, which sometimes paraphrase. They are
reproduced as retrieved and attributed to the source the summary named. **Each should be
confirmed against the primary document before publication.** I have not silently
"cleaned up" any of them, and where I am unsure of exact wording I say so.

1. **On the absence of capacity-building evidence** — *Strengthening Nonprofits: Capacity
   Building and Philanthropy* (CSUN-hosted PDF; date unconfirmed):
   > "Evaluation research to determine the effectiveness of capacity-building
   > interventions has seldom been undertaken."

2. **On why it is not evaluated** — same literature cluster
   (fundingcapacity.issuelab.org, *Evaluating Capacity-Building Efforts for Nonprofit
   Organizations*):
   > "It is not feasible to employ experimental methods such as comparison group studies
   > since there are too many variables that influence organizations over time."

3. **On consultants not evaluating their own work** — same cluster:
   > "Consultants and trainers who work with nonprofit organizations have performed little
   > rigorous evaluation of their capacity-building efforts."

4. **On the merger evidence gap** — Mission + Strategy, on its 10-year longitudinal
   revisit (as characterized in retrieved summary):
   > "The field still has little evidence about whether mergers make organizations more
   > resilient over time."

5. **On the absence of closure statistics** — Candid, "An experiment in tracking nonprofit
   closures and layoffs":
   > "There aren't good statistics available about nonprofit closures."

6. **On AI adoption without measurement** — Virtuous / Fundraising.AI, *2026 Nonprofit AI
   Adoption Report* (n=346). Outcome tracking described as **"very rare,"** with the
   report noting that without defined benchmarks, nonprofits cannot determine whether AI
   is expanding fundraising capacity or merely accelerating existing tasks. *(Wording
   partly paraphrased in the retrieved summary — verify.)*

7. **On AI pilots failing to produce results** — MIT Project NANDA, *The GenAI Divide:
   State of AI in Business 2025* (July 2025), as reported:
   > "95% of pilots delivered no measurable P&L impact."
   *(Contested — see Marketing AI Institute, "That Viral MIT Study Claiming 95% of AI
   Pilots Fail? Don't Believe the Hype.")*

8. **On AI-driven application volume predating the federal pullback** — retrieved from
   coverage of the AI grant flood (Nature news piece, "Responses to the AI grant flood
   must prioritize fairness as part of excellence," and related reporting):
   > "Funding bodies from Australia to the United Kingdom have seen a sharp rise in
   > applications since 2022, which coincides with the advent of ChatGPT, with good
   > evidence suggesting many of these increases are AI-driven."

9. **On mass applications closing doors — directly relevant to the product thesis** —
   Spark the Fire Grant Writing, "Why 2026 is the Year to Stop Writing Grant Proposals to
   Every Foundation":
   > "Every generic, poorly-matched proposal that lands in a program officer's inbox makes
   > them more likely to close the door to unsolicited applications entirely."

10. **On the limits of donor-side intervention** — Bridgespan, *The Trust-Based
    Philanthropy Conundrum* (April 2024):
    > "Truly value-adding, high-intervention donor strategies are rare."

11. **On the honesty of the tax-form closure statistic** — retrieved commentary on the
    Candid 71% figure:
    > "Foundations may be choosing the easiest path rather than accurately describing
    > their practices."
    *(Included deliberately: it cuts against a statistic that supports my own
    disconfirmation of Claim 5.)*

---

## Data gaps

### Gaps caused by tooling failure (not by absence of evidence)
These are questions I was **prevented** from answering, and must not be reported as
"no evidence exists."

- **Every primary document.** CEP *State of Nonprofits 2026*, CEP *Breaking the Mold*,
  NFF 2025 full report, the Virtuous AI report PDF, Hung & Hager and Choi full texts.
  **All blocked.** Every percentage in this document is unverified against source.
- **G2 / Capterra review text** for all prospect-research tools — blocked. This is the
  most important unfilled gap for the product decision.
- **Vendor pricing pages** — blocked; pricing reported here is second-hand and internally
  inconsistent for Instrumentl.

### Searches queued but never run (budget exhausted after 18 of 30+)
- Urban Institute / NCCS registered nonprofit counts and **historical baseline closure
  rate** — the missing denominator for all closure analysis.
- **Nonprofit litigation outcomes** against federal funding cuts — Part 2 of the brief,
  entirely unresearched.
- **Advocacy campaign outcomes** — entirely unresearched.
- **Shared services / back-office consolidation** outcome evaluations.
- Foundation-side **administrative application-volume data** (the missing proof for Claim 1).
- Systematic review of **grantseeker pain-point surveys** — needed to firm up the Claim 5
  finding, which currently rests on an absence observed across few searches.
- Bridgespan and NFF analytic work beyond the survey.
- Randomized/quasi-experimental nonprofit intervention studies as a category.

### Genuine evidence gaps (searched, nothing found)
- **No survival-rate study for emergency/bridge fund recipients vs non-recipients.**
- **No measured burden reduction from trust-based philanthropy.**
- **No 2025–26 capacity-building outcome evaluation.**
- **No post-merger outcome study; no count of failed/abandoned mergers.**
- **No study measuring whether diversification pivots replaced lost federal revenue.**
- **No evaluated donor-retention or monthly-giving intervention with measured results.**
- **No nonprofit AI study with an objective (non-self-reported) outcome measure.**
- **No survey ranking funder-identification as a top grantseeker pain point.**

---

## Source log

**Universal caveat: every entry below is `snippet-only`.** No URL in this table was
successfully fetched; all content derives from search-engine result summaries. Zero
primary verification.

| # | Source / URL | Type | Credibility note |
|---|---|---|---|
| 1 | CEP, *State of Nonprofits 2026* — `cep.org/wp-content/uploads/2026/05/CEP_State_of_Nonprofits_2026_FNL.pdf` | Primary survey (secondary access) | High credibility; sector-advocacy alignment. **Host blocked.** |
| 2 | CEP, *Breaking the Mold* (Feb 2025) — `cep.org/wp-content/uploads/2025/02/CEP_Breaking_the_Mold_FNL.pdf` | Primary study | Strongest design found (comparison group + tax data). **Blocked.** |
| 3 | CEP, *Emerging Impacts* (Nov 2023) — Year 2 of Scott series | Primary study | Pre-window; context. **Blocked.** |
| 4 | NFF, *2025 State of the Nonprofit Sector Survey* — `nff.org` (n=2,206; fielded 30 Jan–14 Mar 2025) | Primary survey | High credibility; self-report. **Host blocked.** |
| 5 | Virtuous + Fundraising.AI, *2026 Nonprofit AI Adoption Report* (n=346, ~Feb 2026) | Vendor-sponsored survey | **Commercial interest in AI adoption**; negative findings credible against interest. **Blocked.** |
| 6 | MIT Project NANDA, *The GenAI Divide: State of AI in Business 2025* (Jul 2025) | Academic/industry | Cross-sector, **not nonprofit**. 95% figure **publicly contested**. |
| 7 | Marketing AI Institute — critique of the MIT 95% figure | Secondary critique | Necessary counterweight to #6. Not retrieved. |
| 8 | Hung & Hager, *NVSQ* 48(1), Feb 2019, pp. 5–27 | Peer-reviewed meta-analysis | Highest-quality evidence in this document. Pre-window. |
| 9 | Choi, *NVSQ* 2025, doi 10.1177/08997640251316487 | Peer-reviewed | In-window, directly thesis-relevant. Abstract-level only. |
| 10 | Giving USA 2026 — IU Lilly Family School of Philanthropy | Primary national estimate | Authoritative for aggregates; modeled, not census; sector-partnered. |
| 11 | AFP Fundraising Effectiveness Project, quarterly reports | Panel data | Real measurement; **vendor-CRM-derived, non-random; methodology changed mid-series.** |
| 12 | NonProfit Times, "Fewer Donors, More Dollars, and Methodology Changes At FEP" | Trade press | Flags the FEP methodology break — **important caveat source.** |
| 13 | Candid, "An experiment in tracking nonprofit closures and layoffs" | Primary tracker | Only measured closure data; **explicitly experimental**, ~65 events / 3 months. |
| 14 | Candid, foundation payout / Foundation Source data blogs | Primary-ish analysis | Source of the flat-$19.4B matched-panel finding — key disconfirmation for Claim 4. |
| 15 | Candid, "Where do foundations stand on AI-generated grant proposals?" | Primary survey | Source of 10% accept / 23% reject / 67% undecided. |
| 16 | Candid 2025 research on 112,000+ private foundations — **71% do not accept unsolicited requests** | Primary (990-PF derived) | **Single most decisive fact for Claim 5.** Checkbox-derived; self-caveated. Accessed via secondary summaries only. |
| 17 | Bradford K. Smith, *SSIR*, Winter 2019 — ~70% of 87,000+ foundations | Primary commentary | Corroborates the trend line. Not retrieved. |
| 18 | unfundedlist.com, "Inundated: Why Many Foundations Are Invite Only" | Secondary/practitioner | Carrier of the 71% and 2011/2015 trend figures. Practitioner blog — **corroborate.** |
| 19 | Spark the Fire, "Why 2026 is the Year to Stop Writing Grant Proposals to Every Foundation" | Secondary/practitioner | Source of quote #9. Commercially interested (sells grant training). |
| 20 | Bridgespan, *The Trust-Based Philanthropy Conundrum* (Apr 2024) | Secondary analysis | Most substantive critical treatment of TBP found. Pre-window. |
| 21 | Mission + Strategy — *Mergers as a Strategy for Success* + 2026 10-year revisit | Primary study | Original: 25 mergers, 100+ interviews, Chicago. **Revisit unpublished.** |
| 22 | Engage R+D / Harder+Company, *PropelNext Alumni Study: The Road to High Performance* (Jun 2018) | Primary evaluation | 12 orgs, mixed methods, **no control group**. Pre-window. Funder-commissioned. |
| 23 | *Strengthening Nonprofits: Capacity Building and Philanthropy* (CSUN-hosted PDF) | Secondary/academic | Source of quotes #1, #3. **Date unconfirmed — likely well pre-window.** |
| 24 | *Evaluating Capacity-Building Efforts for Nonprofit Organizations* (fundingcapacity.issuelab.org) | Secondary/academic | Source of quote #2. Date unconfirmed. |
| 25 | Instrumentl — grant statistics, success rates, 2025 nonprofit survey | **Vendor marketing** | **Direct competitor to the client's proposed product.** Selection-biased. Success-rate figures should not be used. |
| 26 | Candid pricing page + Candid Search launch coverage (15 Jan 2026) | Vendor primary (secondary access) | **$299→$100/mo cut; free tier under $1M revenue.** Key competitive fact. |
| 27 | Grantsights / FundRobin / TrustRadius / G2 pricing comparisons | Affiliate/comparison content | **Internally inconsistent on Instrumentl pricing.** Low reliability; monetized by referral. |
| 28 | G2 — Instrumentl 4.9/128 reviews; DonorSearch 4.6/226; iWave 2020–21 Grid | Review platform | Ratings retrieved; **review text blocked.** iWave figures **dated**. |
| 29 | GetNews syndicated PR, "Small Nonprofits Bleed Funding as Faulty AI Grant Tools Mislead Research" (Jul 2025) — barchart / Globe and Mail / financialcontent | **Paid press release** | **REJECTED — do not cite.** Vendor marketing ("Sharke.ai"). All statistics **[UNVERIFIED]**. Listed to prevent re-ingestion. |
| 30 | Nature, "Responses to the AI grant flood must prioritize fairness as part of excellence" (d41586-026-01422-x) | Peer journal news | Credible; source of quote #8 context. Not retrieved. |
| 31 | NPR (1 Aug 2025) — CPB shutdown after $1.1B clawback | Primary journalism | High credibility. Largest documented closure of the window. |
| 32 | Yahoo/AOL syndicated local reporting — Humanities North Dakota, The Breathing Association, Lamar reopening, 14th & Chestnut reprieve | Local journalism (syndicated) | [Anecdote]-grade individually. **Reversal cases matter** — announced ≠ realized closure. |
| 33 | abetternonprofitsector.substack.com (Laura Pierce), "Nonprofit closures — a few recent examples" | Newsletter | Source of several org names. **[UNVERIFIED]** — confirm each individually. |
| 34 | NonProfit PRO — 2025 revenue growth reporting (62% increases, ~4.3% growth) | Trade press | **Underlying study not identified in the summary.** Key disconfirmation stat for Claim 3 — **must be traced before use.** |
| 35 | Philanthropy.com (Chronicle) — emergency funding, foundation-giving outlook pieces | Trade press | Credible sector press. **Host blocked.** |

**Blocked-host register (egress policy denials recorded by the proxy):** `cep.org`,
`nff.org`, `philanthropy.com`, `instrumentl.com`, `grantstation.com`,
`councilofnonprofits.org`, `nationalacademies.org`,
`539405.fs1.hubspotusercontent-na1.net`, `example.com`.
