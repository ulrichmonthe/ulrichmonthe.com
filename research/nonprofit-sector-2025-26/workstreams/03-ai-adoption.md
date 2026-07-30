# Workstream 3 — The AI Adoption Paradox

**Research window:** mid-2025 – mid-2026. **Compiled:** 2026-07-30.

---

## ⚠️ RETRIEVAL LIMITATIONS — READ BEFORE USING ANY NUMBER IN THIS FILE

Two hard constraints shaped this workstream. Both affect how much weight each figure can carry.

**1. No primary document was ever opened.** Every attempt to fetch a page or PDF directly returned
HTTP 403 from the session's egress proxy — this is an organization egress policy, not a site
paywall. Confirmed blocked hosts include `539405.fs1.hubspotusercontent-na1.net` (the Virtuous
report PDF), `cep.org`, `virtuous.org`, `prnewswire.com`, `nonprofitpro.com`, `nten.org`,
`ssir.org`, `aijourn.com`, and even `example.com`. The proxy status endpoint recorded these as
`connect_rejected — gateway answered 403 to CONNECT (policy denial or upstream failure)`.

Consequence: **the brief's core methodology rule ("primary over secondary, cite page/section")
could not be satisfied.** Everything below is derived from search-engine-synthesized summaries of
those pages. No page numbers, no section references, no verification of question wording against
source instruments. Every row in the tables below should be treated as **snippet-only**.

**2. Search budget exhausted.** The session-wide WebSearch budget (200 calls, shared across all six
workstreams) ran out after **22 distinct searches** in this workstream, against a target of 28+.
Six planned search cycles were not executed — they are itemized under *Data gaps → Searches not run*.

**What this means practically:** the 92% / 7% figures ARE corroborated across multiple independent
outlets (see below) and can be used. The *methodology metadata* (field dates, recruitment,
question wording, sponsor disclosures) is thin-to-absent for nearly every source, and the brief's
central analytical task — explaining the 80–92% spread via question wording — can only be answered
**inferentially, not evidentially.** I say so explicitly rather than manufacturing the explanation.

---

## Key findings

1. **The headline "92% adoption" figure is real and independently corroborated, but it measures
   almost nothing.** The single most useful datapoint retrieved is from Google.org: only **one in
   five** nonprofits say *at least half* their organization uses generative AI. Set against
   adoption headlines of 80–97%, this implies the sector-standard adoption question is capturing
   "at least one person here has opened a chatbot." Adoption percentage is not a meaningful
   sector metric. [Reported]

2. **The spread across sources is 61%–97%, wider than the brief's 80–92%.** CEP's nationally
   representative survey (~two-thirds) sits ~30 points below BDO's (97%). The two sources with the
   most defensible sampling (CEP) and the most vendor-proximate sampling (Virtuous, BDO) sit at
   opposite ends of the range — which is itself the finding.

3. **I could NOT verify the question wording behind any adoption figure.** The brief hypothesized
   that wording ("any staff member has used AI" vs. "organization has deployed AI") explains most
   of the spread. That hypothesis is *consistent* with the retrieved evidence and with the
   TechSoup wording that did surface ("85.6% are **exploring** AI tools"), but it is **not
   demonstrated**. Do not present it as established.

4. **The 7% figure is confirmed but is being used for two different things,** and the sources blur
   them: 7% report *major improvement in organizational capability*, and 7% say AI is *embedded
   into goals, budgets and performance indicators*. These may be the same respondents, overlapping
   groups, or coincidentally equal percentages. **Nothing retrieved establishes which.** Anyone
   claiming "the 7% who embedded AI are the 7% who got results" is asserting a correlation the
   published summaries do not support.

5. **Governance statistics are wildly inconsistent — by a factor of seven.** Virtuous says 53% have
   a policy (47% do not). The AI Equity Project says 6.9%. Whole Whale says 10%. TAG says 30% of
   *foundations*. TechSoup says 24% have a formal *strategy*. This is the single largest
   unreconciled conflict in the workstream.

6. **The strongest evidence against the "governance is the AI gap" thesis comes from the one survey
   that only sampled organizations already running AI in production** (Coastal Cloud, n=75
   nonprofits). Their stall points are **data (72%), problem definition (60%), integration (59%),
   and staff distrust of outputs (53%)** — not missing policy documents. Governance is what
   vendors and consultancies sell; data quality and problem definition are what practitioners
   report.

7. **Failure evidence in this sector is dominated by vendor-manufactured content.** The most
   search-visible "nonprofit AI failure" story is a paid press release from an AI grant-writing
   vendor. See *Named failure modes → Discarded*. Genuine, independently documented nonprofit AI
   failures were **not found**.

8. **The most important upcoming source has not published.** NTEN + Bridgespan's *2026 State of
   Nonprofit AI Adoption and Governance* survey was in the field (open SurveyMonkey link, promoted
   by NTEN CEO Amy Sample Ward) with results unpublished as of these searches. This is the source
   most likely to be non-vendor and governance-focused. Flag for follow-up.

---

## Reconciled adoption statistics

| Source | Reported adoption % | n | Field dates | Question wording (as retrieved) | Sponsor | Bias flag |
|---|---|---|---|---|---|---|
| **Virtuous / Fundraising.AI**, *2026 Nonprofit AI Adoption Report* | **92%** use AI | 346 nonprofits | **CONFLICT:** summaries variously say "late 2025", "December 2025", and "February 2026". Released 16 Feb 2026. Field dates **unverified** | Not retrieved. Reported as "use AI" / "use AI in some capacity" | Virtuous (nonprofit CRM vendor) + Fundraising.AI | 🚩🚩🚩 **SEVERE.** CRM vendor publishing an adoption report that concludes customers need integrated workflows and governance — i.e. the vendor's product category. Sample near-certainly drawn from Virtuous/Fundraising.AI audience lists. Not population-representative. |
| **BDO**, *2025 Nonprofit Standards Benchmarking* (9th annual) | **97%** of nonprofits / **92%** of public charities "report using AI across operations" | ~250 nonprofit leaders | 2025, exact dates not retrieved | "using AI across operations" | BDO (accounting/advisory firm serving nonprofits) | 🚩🚩 Professional-services firm; sample = BDO's client-adjacent leader panel. The 97%/92% split framing is odd and **[UNVERIFIED]**. Highest figure found. |
| **TechSoup + Tapp Network**, *The State of AI in Nonprofits: 2025* | **85.6%** "are **exploring** AI tools" | 1,300+ nonprofit professionals | Released ~Jan 2025 (partially pre-window) | **"exploring AI tools"** — the only softened verb retrieved in any source | TechSoup (nonprofit tech intermediary) + Tapp Network (agency) | 🚩 Mixed. TechSoup is a sector intermediary, not a for-profit vendor, but Tapp Network is a marketing agency and the report drives TechSoup's AI services. **"Exploring" ≠ "using"** — do not place this in the same column as the others. |
| **AI Equity Project 2025** (via ALIGN Assoc. of Community Services; cited by AFP) | **~80%** "using AI in some way" | 850+ nonprofits, US + Canada | 2025 | "using AI in some way" | Not established | 🚩 Sponsor unidentified in retrieved material. Cross-border sample (US+Canada) — **not clean for a US-sector brief.** |
| **Center for Effective Philanthropy**, *AI With Purpose* | **~two-thirds** ("almost two-thirds") | **451 nonprofits + 215 foundations**, plus 16 interviews | Published Sept 2025 | "report their organization uses AI in its work" | CEP (independent sector research nonprofit) | ✅ **LOWEST BIAS.** Described as nationally representative; two separate instruments; no product to sell. **This is the anchor source.** ~30 points below BDO. |
| **Fast Forward**, *2025 AI for Humanity Report* | **82%** "using AI to assist internal operations" | 34 AI-powered + 83 AI-assisted + 73 both (~190) | 2025 | "using AI to assist internal operations" | Fast Forward (tech-nonprofit accelerator) | 🚩🚩🚩 **SEVERE selection bias.** Respondents are applicants to a *tech-nonprofit accelerator*. Structurally the most AI-forward population in the sector. Useless as a sector adoption estimate; useful only as a within-cohort profile. |
| **Whole Whale** (agency analysis) | **82%** use AI, **10%** have policies | Not retrieved | 2025 | Not retrieved | Whole Whale (nonprofit digital agency) | 🚩🚩 Underlying survey **not identified** — may be a restatement of another source. Treat the 82% as unsourced. |
| **Coastal Cloud / Oxford Economics**, *AI Operations Report 2026* (nonprofit cut) | **N/A — cannot be used for adoption** | 75 nonprofits, within 800 US business/tech leaders | 2026 | **Screening criterion: "all respondents have at least one AI initiative in production today"** | Coastal Cloud (Salesforce implementation consultancy) + Oxford Economics | 🚩🚩 Vendor-sponsored, BUT the screening criterion makes this the **most useful failure-mode source** in the file. Adoption rate is 100% by construction — never cite it as an adoption figure. |
| **Google.org** (survey referenced in Google blog) | **Only 1 in 5** say *at least half* their organization uses generative AI | Not retrieved | Not retrieved | "at least half their organization uses generative AI" | Google.org | 🚩 Funder/platform sponsor. **But this is the single most analytically valuable adoption datapoint found**, because it is the only one measuring *depth* rather than *any use*. |
| **Deloitte** (health nonprofits) | **61%** of health nonprofits use gen AI | Not retrieved | Not retrieved | Not retrieved | Deloitte | 🚩 **Headline only — never opened.** Subsector-specific (health). Listed for completeness; do not cite without verification. |
| **Technology Association of Grantmakers (TAG)** | **81%** of *foundations* experimenting with AI | Not retrieved | Reported via Chronicle of Philanthropy, Oct 2025 | "experimenting with AI" | TAG (grantmaker tech membership assoc.) | 🚩 Membership self-selection (tech-engaged grantmakers). **Foundations, not nonprofits** — different population, do not merge rows. |
| **Bonterra** (funder survey) | **91%** of funders see AI transforming philanthropy; **92%** worry about data use/ethics | Not retrieved | Released 10 Nov 2025 | Not retrieved | Bonterra (nonprofit software vendor) | 🚩🚩 Vendor. **Headline only — never opened.** Attitudinal, not adoption. |

### Why the numbers range — assessed honestly

The brief proposed that question wording explains most of the spread. Here is what the evidence
actually supports:

- **[SUPPORTED]** *Depth vs. any-use is definitely a factor.* Google.org's "1 in 5 have half the org
  using gen AI" versus 80–97% headline adoption is a ~60-point gap within roughly the same
  universe. Something in the question is doing enormous work.
- **[SUPPORTED]** *At least one source demonstrably uses a softer verb.* TechSoup's "**exploring**
  AI tools" (85.6%) is not the same construct as "uses AI in its work" (CEP, ~66%) — and yet
  TechSoup's softer question produced a *higher* number, which is the direction the wording
  hypothesis predicts.
- **[SUPPORTED]** *Sampling frame explains a large share independently of wording.* Fast Forward
  (accelerator applicants) and Coastal Cloud (screened for AI-in-production) are structurally
  incapable of producing sector-representative figures. Virtuous and BDO draw from vendor/client
  panels. CEP — the only source described as nationally representative — returns the lowest
  general-population figure. **The correlation between sampling independence and lower adoption
  estimates is the most robust pattern in this table.**
- **[NOT ESTABLISHED]** *That wording explains "most" of the spread.* I never retrieved a single
  verbatim survey item from any instrument. This cannot be asserted.
- **[NOT ESTABLISHED]** *Whether any two sources are even measuring the same population.* Foundations
  (TAG, Bonterra, part of CEP) and operating nonprofits are mixed together in most secondary
  coverage. Several figures in circulation are foundation figures being reported as nonprofit
  figures.

**Recommended framing for the final report:** do not publish a reconciled point estimate. Publish
the range with sampling-frame annotations, and lead with the depth statistic (1 in 5) rather than
the breadth statistic (92%).

---

## Profile of the high-impact minority

**Source base:** almost entirely Virtuous/Fundraising.AI — i.e. **a single vendor-sponsored survey
and its own marketing blog.** Corroboration from independent sources: **none found.** Grade
everything in this section **[Reported]** at best, and note that the characteristics named
correspond closely to the sponsor's product and services offering.

### Confirmed figures
- **7%** report major improvements in organizational capability. Examples named: doubling prospect
  research capacity; personalizing donor communication at scale; reallocating staff time from
  execution to relationship strategy. [Reported]
- **7%** say AI is embedded into goals, budgets and performance indicators. [Reported]
- **18%** report operational use across team workflows (the middle tier). [Reported]
- **65%** describe use as reactive and individual — one-off prompts, personal experimentation. [Reported]
- **79%** report only small-to-moderate efficiency gains — the report's "**efficiency plateau**". [Reported]
- **4%** have documented, repeatable workflows. [Reported]
- **~one-fifth** have foundational elements in place (some governance, documentation, measurement);
  **~another fifth** at early experimentation stage. **[UNVERIFIED — single search summary, not
  corroborated]**

### Distinguishing characteristics named

From the report as summarized by press coverage — the report "identifies … the foundations that
separate organizations seeing major impact from those stuck at the efficiency plateau":

1. **Clear governance**
2. **Documented workflows** (vs. the 81% ad-hoc / 4% documented split)
3. **Cross-functional ownership**
4. **Consistent measurement**

From Virtuous's own follow-on blog, *"How to Transform Your Nonprofit With AI: 7 Patterns From the
Top 7%"* — note this is **marketing content, not the report** [Reported/promotional]:

5. **Started where risk was low and return was clear**, measuring small early gains and refining
   before moving to higher-stakes applications
6. **Stopped treating AI as a personal shortcut** — explicit contrast with the 81% ad-hoc majority
7. **Strengthened strategy before tools** — "AI doesn't rescue broken systems—it accelerates them"
8. **Predictive intelligence for donor understanding** — moving beyond wealth as the primary signal
   *(note: this is a direct description of Virtuous's own product category — heaviest bias flag in
   the section)*

### Brief-requested characteristics with NO DATA FOUND

The brief asked for *every* characteristic named. These were specifically sought and **not found**
for the high-impact group:

- **Leadership involvement** — NO DATA FOUND. (Adjacent only: Coastal Cloud's 67% citing lack of
  strategic direction/leadership as a constraint, and Board.Dev's 24% board tech/data
  representation — neither is a high-impact-cohort characteristic.)
- **Training approach** — NO DATA FOUND. Nothing retrieved describes how the 7% train staff.
- **Dedicated budget** — NO DATA FOUND as a *distinguishing* characteristic. "Budgets" appear only
  inside the composite phrase "embedded into goals, budgets, and performance indicators."
  Separately, AI Equity Project reports **<4% of all nonprofits** have budgets for AI-specific
  training — a sector figure, not a cohort figure.
- **Data readiness** — NO DATA FOUND in the Virtuous material. Conspicuous by absence given that
  data quality is the top failure driver in the one production-screened survey (Coastal Cloud, 72%).
- **Organization size / budget of the 7%** — NO DATA FOUND. Not knowing whether the high-impact
  cohort is simply the largest, best-resourced organizations is a serious gap: TechSoup's 66%-vs-34%
  large/small adoption split suggests size may be the confound.

**Analytical caution:** the four named "foundations" (governance, documentation, cross-functional
ownership, measurement) are the standard consulting prescription for *any* technology adoption.
Nothing retrieved indicates these were derived from a statistical comparison of the 7% against the
rest, as opposed to being the authors' interpretation. Absent the methodology section, **treat the
causal claim as unproven.**

---

## Named failure modes

### Tier 1 — Quantified, from a survey screened for organizations actually running AI

**Coastal Cloud / Oxford Economics, *AI Operations Report 2026*, nonprofit cut (n=75; all
respondents have ≥1 AI initiative in production).** This is the highest-value failure source found,
precisely because it excludes the merely curious. Vendor-sponsored (Salesforce implementation
consultancy) — flag — but the findings run *against* tech optimism, which raises confidence.
All [Reported]:

| Failure mode | % |
|---|---|
| Face data accuracy or availability issues | **72%** |
| Cite lack of strategic direction or leadership as a constraint | **67%** |
| Name problem definition / requirements gathering as where initiatives stall | **60%** |
| Face ongoing integration difficulty | **59%** |
| Face more maintenance than planned | **56%** |
| **Staff did not trust the outputs enough to act on them** (when systems fell short) | **53%** |
| Can point to measurable results | **only 19%** |

**How initiatives were scoped** — the most concrete failure-origin data retrieved anywhere:
- **12%** began their most recent AI initiative with a **clearly defined problem**
- **37%** adopted a **vendor's recommended use case**
- **37%** **chose a platform first**
- **13%** **never settled on a scope at all**

That is **74% of nonprofit AI initiatives originating from a vendor or a platform rather than from
a problem** — the sharpest single indictment in this workstream, and it comes from a vendor's own
research.

### Tier 2 — Structural failure modes named in the Virtuous report

- **Knowledge evaporation.** 81% use AI without documenting workflows, so gains are "linked to an
  individual's legacy knowledge and are lost if that individual leaves the organization."
  [Reported] (via The NonProfit Times, 18 Feb 2026)
- **Policy vacuum → data exposure.** 47% have no governance policy, "meaning donor data and other
  confidential information can be misused or exposed." Note the modal verb: this is a **stated
  risk, not a documented incident.** [Reported — hypothetical harm]
- **Boundary ambiguity.** "Most organizations are operating without clear boundaries about
  appropriate AI use, and staff are uncertain what is allowed, especially regarding donor data or
  confidential information that might feed into the system." [Reported]

### Tier 3 — Barriers to deeper use

From a search summary attributing these to the Virtuous report; **attribution [UNVERIFIED]** as the
summary blended sources:
- Privacy and security concerns — **32%** of active users
- Time and capacity constraints — **31%**
- **Staff skepticism based on experience — 19%**

### DISCARDED — vendor-manufactured failure content

**"Small Nonprofits Bleed Funding as Faulty AI Grant Tools Mislead Research"** is the most
search-visible nonprofit-AI-failure story in existence (syndicated to Globe and Mail, Barchart,
FinancialContent). It is a **GetNews paid press release, apparently from the AI grant vendor
Sharke.ai.** Claims made: 33% error rate in AI grant recommendations; a "Sharke.ai Crisis Report"
documenting "350+ grant failures across 22 states in 2025"; a Texas mental health nonprofit told by
a foundation it doesn't fund mental health (mandate changed years earlier); 23% of foundations
reject AI outright; a "Stanford Medicine March 2026 evaluation" of generative tools in grant writing.

**Do not use any of it.** The structure is textbook problem-manufacturing: a vendor documents a
crisis its own product solves. The "Crisis Report" has no independent existence I could establish;
the Stanford Medicine citation could not be verified (fetch blocked). Recorded here so the research
team recognizes and rejects it if it resurfaces — and as evidence for a genuine meta-finding:
**the nonprofit AI failure literature has been colonized by vendor marketing.**

### NO DATA FOUND — specifically sought, not located

- **Named nonprofits that abandoned an AI tool.** NO DATA FOUND after 3 targeted searches. Every
  result returned enterprise-sector failure statistics (MIT/NANDA-lineage "95% of pilots", "80% of
  AI projects fail", "50% abandoned after PoC") with **zero nonprofit case studies.**
- **A documented incident of fabricated AI content in an actual submitted grant application.** NO
  DATA FOUND after 2 targeted searches. Abundant *advisory* content on hallucination risk; zero
  documented incidents. Notably, **Candid found fewer than 1% of surveyed funders (4 respondents)
  said they had received AI-generated applications** — evidence the feared flood has not
  materialized, or is undetected.
- **A documented donor-data misuse incident traced to AI.** NO DATA FOUND.
- **A documented biased-screening incident at a nonprofit or foundation.** NO DATA FOUND.

---

## Governance landscape

### What share have an AI policy — UNRECONCILED, factor-of-seven conflict

| Source | Figure | Population | Construct |
|---|---|---|---|
| Virtuous/Fundraising.AI 2026 | **47% have NO policy** → implies **53% have one** | 346 nonprofits (vendor panel) | "AI governance policy" |
| AI Equity Project 2025 | **6.9% have internal AI policies** | 850+ US+Canada nonprofits | "internal AI policies" |
| AI Equity Project 2025 (same source, different citation) | **15% have successfully implemented an AI policy** | same | "successfully implemented" |
| Whole Whale 2025 | **10% have policies** | unspecified | "policies" |
| TechSoup/Tapp 2025 | **24% have a formal AI strategy** | 1,300+ | "formal strategy" (≠ policy) |
| TAG (via Chronicle, Oct 2025) | **30% have an AI policy**; **9%** have an advisory group on tech + policy | foundations | "AI policy in place" |

**Triangulation:** these cannot all be right. Three observations:

1. **The AI Equity Project contradicts itself** across two citations of the same study (6.9% vs
   15%) — likely "has a policy" vs. "has implemented a policy," but **unverifiable** (fetch blocked).
2. **Virtuous is a 4–8× outlier above the non-vendor sources.** Two candidate explanations, both
   plausible, neither testable here: (a) its sample is drawn from a CRM vendor's engaged customer
   base, which is more mature than the sector; (b) its question accepted informal guidance as a
   "policy" where others required a formal document.
3. **The clustering of independent sources at 7–15% is more credible than the vendor figure of 53%.**
   **Recommendation: do not cite "47% have no AI policy" as a sector fact.** The defensible
   statement is "estimates of nonprofits with a formal AI policy range from ~7% to ~53%, with
   non-vendor sources clustering at the low end."

Supporting: **<4% of nonprofits have budgets for AI-specific training** (AI Equity Project) and
**9% feel ready to use AI responsibly** (same) — both consistent with the low end.

### Who is producing policy templates and governance support

- **NTEN** — AI For Nonprofits Resource Hub (`nten.org/learn/resource-hubs/artificial-intelligence`).
  Videos, templates, resources spanning governance principles to board-level discussions. Stated
  free. [Announced — availability confirmed by search result; contents not inspected]
- **ANB Advisory (Afua Bruce & Rose Afriyie), *AI Policy Template*, Sept 2024**, hosted on NTEN's
  domain and developed in partnership with NTEN. **Adapted from NIST's AI Risk Management
  Framework** for nonprofit use cases; equity-focused, emphasizing harm reduction. The only
  template found with an identifiable standards lineage. (Pre-dates the research window.)
- **NTEN + Bridgespan** — *2026 State of Nonprofit AI Adoption and Governance* survey, fielded via
  SurveyMonkey, promoted by NTEN CEO Amy Sample Ward on LinkedIn. Anonymous responses; **results to
  be published as a free report. NOT YET PUBLISHED as of these searches.** [Announced]
- **Candid** — "Getting started on a responsible AI use policy for nonprofits" guidance; also
  publishing funder-side research on AI-generated proposals and AI screening.
- **Whole Whale** — comparative analysis of published nonprofit AI policies, specifically **United
  Way, American Red Cross, Oxfam International, Save the Children.** Oxfam's is described as a
  rights-based approach grounded in the **UN Guiding Principles**; Save the Children's is focused on
  **child protection and privacy.** These four are the closest thing to sector reference
  implementations found.
- **Board.Dev + Dell Technologies + TechSoup** — *Building the Leadership Nonprofits Need to Make AI
  Work* (n=180 nonprofits, 44 states). Board/leadership governance framing; offers "practical tools."
  🚩 Dell is a hardware vendor sponsor.
- **Forvis Mazars** — *AI Governance for Nonprofit Boards* (Feb 2026) and *2026 State of the
  Nonprofit Sector: AI Adoption & Governance* (June 2026). **Titles only — not retrieved.**
- **The Nonprofit Alliance (TNPA)** — standing AI resource page.
- **State associations** — confirmed active: **Maine Association of Nonprofits** ("Nonprofits and
  AI"); **NJ Center for Nonprofits** (event: "AI Ethics and Policy for Nonprofits: Navigating
  Innovation with Integrity"). Indicates state-association-level diffusion but only two instances
  surfaced.
- **BoardSource** — **NO DATA FOUND.** Despite being named as a priority source, no BoardSource AI
  governance material appeared in any search. Not evidence of absence (search budget ended before a
  dedicated BoardSource query), but flagged.

### What nonprofits say they WANT from governance support

Thin. Retrieved:
- **~90% of nonprofits are interested in expanding their use of AI** while **~90% of foundations
  provide no AI implementation support**; only **10%** of foundations support grantees on AI
  implementation, and **only half of that** focuses on ethical AI (CEP). The single clearest
  statement of unmet demand found. [Reported]
- **Three-quarters of nonprofit leaders believe none or just a few of their foundation funders
  understand their organization's AI-related needs or concerns** (CEP). [Reported]
- **84% of AI-building nonprofits say additional funding is what's most needed** to develop and
  scale their AI work (Fast Forward) — note: **money, not governance templates.** [Reported]
- **NO DATA FOUND** on what nonprofits specifically want in a *governance* support offering
  (template vs. training vs. peer review vs. funder-supplied policy). No source surfaced asked this.

---

## Trust and incidents

### Staff trust
- **53%** of nonprofits with AI in production say that when systems fell short, **staff did not
  trust the outputs enough to act on them** (Coastal Cloud, n=75). Strongest staff-trust datapoint
  found. [Reported]
- **79%** of nonprofit leaders say their employees are eager to work with AI — but the source
  characterizes actual buy-in as "tenuous" (same). Note this is **leaders reporting on staff
  attitudes**, not staff self-report. [Reported]
- **19%** cite **staff skepticism based on experience** as a barrier to deeper use.
  **[UNVERIFIED attribution]**
- **Almost two-thirds** of nonprofits and foundations report **none or just a few staff have a solid
  understanding of AI and its applications** (CEP). Capacity, not trust, but bears on it. [Reported]
- **63%** of fundraisers are unsure about using generative AI for donor communications **because it
  seems less personal.** [Reported — attribution uncertain, likely Nonprofit Tech for Good compilation]

### Donor trust
All figures below are **snippet-only with uncertain primary attribution** — they surfaced in a
compilation page (Nonprofit Tech for Good) and/or Give.org's Donor Trust Report 2026, neither of
which could be opened. **Do not publish without verification.**
- **31%** of donors say they would be **less likely to donate** if nonprofits use AI; **43%** say AI
  use would have a positive or neutral effect; **9%** would be more likely. [Reported, [UNVERIFIED]]
- **54.5%** say they would be **discouraged from giving** if they knew an appeal (with AI-generated
  images) **was not verified for accuracy by a staff member.** Note the conditional — this measures
  reaction to *unverified* AI content, not AI content per se. [Reported, [UNVERIFIED]]
- **7%** of donors say AI summaries influence their giving choices (as of end-2025). [Reported, [UNVERIFIED]]
- Give.org identifies the top three donor accountability priorities as: how the charity spends its
  money, **appeal accuracy**, and **protection of donor information** — the latter two both directly
  implicated by AI use. [Reported]
- Relevant framing: **Bonterra** reports **92% of funders worry about data use and ethics** while
  **91%** see AI transforming philanthropy. 🚩 Vendor, headline-only.

### Funder / grantmaker trust
- **Only 10%** (1 in 10) of funders would **accept grant applications containing generative-AI-created
  content**; **67% are undecided** (Candid). [Reported]
- **Fewer than 1%** of funder respondents (4 people) said they had **received** an AI-generated
  application — and **most foundations admit they cannot reliably detect AI-assisted submissions**
  (Candid). [Reported] **This pair is important: near-total funder inability to detect, combined
  with near-zero detected incidence, means the sector has no observational basis for claims about
  AI-generated proposal volume in either direction.**
- **CEP:** top shared concerns of nonprofit and foundation leaders are **data security and privacy,
  misinformation and inaccuracy from AI, staff expertise, and bias.** [Reported]

### Deployed AI screening — the one concrete deployment found
- **GitLab Foundation** received **800 applications** and used AI systems to review them in **30
  minutes**, work its **three program officers** would have taken hundreds of hours to do. Reported
  via Chronicle of Philanthropy. [Reported — no independent evaluation of decision quality, no
  bias audit, no comparison against human review outcomes retrieved. **This is a throughput claim,
  not an accuracy claim.**]

### Documented incidents
**NO DOCUMENTED INCIDENTS FOUND after 4 targeted searches.** Not one verifiable case of: fabricated
content in a submitted grant application; donor-data misuse via an AI tool; biased AI screening
harming applicants or beneficiaries at a nonprofit or foundation. The sector's AI risk discourse is
**entirely prospective.** The only "incident" content located was vendor-manufactured (see *Named
failure modes → Discarded*).

### Beneficiary trust
**NO DATA FOUND.** Zero sources retrieved measure how the people nonprofits serve feel about AI in
service delivery. Given that the sector's stated equity commitments run through beneficiaries, this
is arguably the largest single evidence gap in the entire workstream.

---

## Segmented AI needs (non-adopters / ad-hoc / mature)

**Caveat: no retrieved source segments stated needs this way.** The framework below is *assembled*
from figures collected across sources; segment assignment is my inference, not any author's. Treat
the segment labels as analysis, the figures as data.

### Non-adopters / early-stage (~one-fifth per Virtuous [UNVERIFIED]; small orgs disproportionately)
- **Money and access first.** TechSoup's large-vs-small adoption split (**66% vs 34%** for >$1M vs
  <$1M budgets, a ~2x gap) is the clearest structural signal: the barrier at this tier is
  resources, not policy.
- **Baseline literacy.** Almost two-thirds of nonprofits report none/few staff with a solid
  understanding of AI (CEP).
- **Training budget.** <4% of nonprofits have any budget for AI-specific training (AI Equity Project).
- **NO DATA FOUND** on what non-adopters *say* they need. No source retrieved asked non-adopters
  directly. This segment is essentially unstudied.

### Ad-hoc / individual users (the dominant segment — 65–81%)
- This is where the sector actually lives: **81%** use AI individually without shared workflows;
  **65%** describe use as reactive and individual; **only 4%** have documented repeatable workflows.
- **Stated barriers to going deeper:** privacy/security **32%**, time and capacity **31%**, staff
  skepticism **19%** [UNVERIFIED attribution].
- **Boundary clarity** — staff "uncertain what is allowed, especially regarding donor data."
  This is the one place where the governance-gap thesis has direct practitioner support: the
  expressed need is for *permission clarity*, which is cheaper and more specific than "an AI policy."
- **Workflow documentation** is the named mechanism for converting individual gains into
  organizational ones (Virtuous) — but note this is the *authors'* prescription, not a respondent
  request.

### Organizationally mature users (7–19%)
- **Data before anything else.** Among organizations with AI actually in production, **72%** hit data
  accuracy/availability problems and **59%** hit integration difficulty. These are engineering and
  data-infrastructure needs, not governance needs.
- **Problem definition capability.** **60%** stall at problem definition/requirements gathering, and
  only **12%** started from a defined problem. The need is analytical discipline upstream of tooling.
- **Sustained maintenance capacity.** **56%** face more maintenance than planned — an ongoing
  operating-cost need that project-based grant funding structurally does not meet.
- **Measurement.** Only **19%** can point to measurable results.
- **Funding to scale.** **84%** of AI-building nonprofits say additional funding is the top need
  (Fast Forward).
- **Leadership/strategy.** **67%** cite lack of strategic direction or leadership as a constraint;
  only **24%** of nonprofit boards have tech or data backgrounds represented (Board.Dev/Dell/TechSoup).

**Cross-cutting, all segments:** ~90% of nonprofits want to expand AI use; ~90% of foundations offer
no implementation support; three-quarters of nonprofit leaders think their funders don't understand
their AI needs (all CEP). **The most consistently expressed need across every segment is funder
support — not governance templates.**

---

## Disconfirming evidence

*Per the brief, a dedicated cycle was spent looking for evidence against "governance is the AI gap."
It was productive.*

### 1. The strongest data says the gap is DATA and PROBLEM DEFINITION, not governance
The only survey that screened for organizations **actually running AI in production** (Coastal
Cloud, n=75 nonprofits) found stall points dominated by **data accuracy/availability (72%)**,
**problem definition (60%)**, **integration (59%)**, **maintenance load (56%)**, and **staff
distrust of outputs (53%)**. Governance/policy does not appear as a top failure mode. The closest is
"lack of strategic direction or leadership" (67%) — which is a *leadership capacity* problem, not a
*policy document* problem, and the two are routinely conflated in vendor framing.

Note the sponsorship asymmetry: the "governance is the gap" thesis comes from a **CRM vendor**
(Virtuous), a **hardware vendor + board consultancy** (Dell/Board.Dev), and **accounting firms**
(BDO, Forvis Mazars) — all of whom sell governance-adjacent services. The "data is the gap" finding
comes from a **Salesforce implementation consultancy** that also sells data services. **Every
available account of the gap is sold by someone.** The correct posture is skepticism toward all of
them, with weight given to Coastal Cloud only because its sample was screened for real deployments.

### 2. Vendor-origination, not governance-absence, is the strongest predictor of a bad start
**74%** of nonprofit AI initiatives began from a vendor's recommended use case (37%) or a platform
choice (37%), versus **12%** from a defined problem. A governance policy would not have fixed a
single one of these — they are failures of procurement discipline and problem framing. This is the
most direct rebuttal in the file, and it comes from a vendor's own research.

### 3. Resources, not governance, track adoption
TechSoup's **66% vs 34%** adoption split by budget size means the strongest observed correlate of
adoption is **money**. Governance maturity is plausibly a *proxy* for organizational size and
slack rather than an independent driver. **No source retrieved controls for organization size when
comparing high-impact to low-impact adopters** — so the entire "7% did governance right" narrative
is confounded with "the 7% are bigger and better resourced." This is a serious, unaddressed threat
to the report's central claim.

### 4. The adoption numbers are close to meaningless
- Google.org: only **1 in 5** nonprofits have even half their organization using generative AI —
  against headline adoption of 80–97%.
- Virtuous itself: **65%** reactive/individual, **only 4%** with documented workflows.
- TechSoup's actual verb is "**exploring**."
- CEP's nationally representative estimate (~66%) is **~30 points below** BDO's (97%).

A metric that moves 30 points on sampling frame and collapses from 92% to 20% when you ask about
depth is not measuring an organizational property. **"Nonprofit AI adoption" as currently surveyed
is a measure of individual curiosity, not institutional capability.**

### 5. AI adoption's correlation with outcomes is unestablished
No retrieved source demonstrates a link between AI adoption and mission outcomes. The nearest
claims are: Google.org grantees reporting goals achieved "in one third of the time at nearly half
the cost" (**grantees self-reporting to their own funder — among the most biased possible
configurations**), and Fast Forward's reach-by-budget medians (2,000 lives at small budgets →
7 million at $5M+), which measure **budget, not AI**, and are self-reported reach figures.
**[Reported] at best; arguably [Announced].**

### 6. Sector-wide, AI pilots mostly fail — nonprofits may simply be normal
Widely circulated enterprise figures: ~95% of gen AI pilots show no P&L return; ~80% of AI projects
fail to deliver business value; ≥50% abandoned after proof of concept; only ~14% reach production.
**[UNVERIFIED — secondary, non-nonprofit, not traced to primary sources; the "95%" is a
much-contested statistic.]** Directionally, though, this reframes the paradox: if 7% of nonprofits
see major impact where ~5–20% of enterprises do, **the nonprofit sector is not anomalously bad at
AI. It is normal.** Framing 7% as a nonprofit-specific failure — as vendor reports do — may be a
category error, and one that conveniently supports selling nonprofits a remedy.

### 7. Peer-proven skepticism is rational, not a deficit
"Much skepticism about AI in the nonprofit sector stems from decades of watching 'transformative'
tools cycle through with limited results. After years of overpromised solutions, nonprofit leaders
now prioritize peer-proven tools with demonstrable dollar impact." Reframes the 19% "staff
skepticism based on experience" barrier as **accumulated institutional learning** rather than a
change-management problem to be overcome.

---

## Verbatim quotes

*Target was 8–12. Ten below. All are quoted as they appeared in search-result summaries of the
source pages — **the source pages themselves could not be opened**, so these are one remove from the
originals. Verify before publication.*

**On the shallowness of adoption**

1. > "Our data shows most organizations are still in the early innings with AI: one person using
   > ChatGPT to help draft an appeal, while the rest of the team is still buried in manual processes
   > and disconnected systems."
   — **Gabe Cooper**, CEO and Founder, Virtuous. *2026 Nonprofit AI Adoption Report* press release,
   Feb 2026. 🚩 Vendor CEO.

2. > "I think that debate is largely settled. The real question is how quickly are nonprofit teams
   > adopting AI and fundamentally re-thinking their workflows."
   — **Gabe Cooper**, CEO and Founder, Virtuous. Same release. 🚩 Note the rhetorical move: declaring
   the *whether* question closed and permitting only the *how fast* question — characteristic vendor
   framing.

3. > "What we're seeing is that AI only drives meaningful impact when nonprofit organizations rethink
   > how work gets done — not when it's treated as a side experiment individuals run in isolation."
   — **Nathan Chappell**, Chief AI Officer, Virtuous. Same release. 🚩 Vendor executive.

4. > "Frequency of use has outpaced organizational readiness."
   — *2026 Nonprofit AI Adoption Report* authors, quoted in **The NonProfit Times**, 18 Feb 2026.

**On what actually goes wrong**

5. > "AI doesn't rescue broken systems—it accelerates them."
   — **Virtuous**, *"How to Transform Your Nonprofit With AI: 7 Patterns From the Top 7%"*
   (marketing blog). 🚩 Promotional, but the sharpest formulation of the point found anywhere.

6. > "…any gains made through the use of AI are linked to an individual's legacy knowledge and are
   > lost if that individual leaves the organization."
   — **The NonProfit Times**, 18 Feb 2026, summarizing the report's finding on the 81% who do not
   document workflows.

7. > "Most organizations are operating without clear boundaries about appropriate AI use, and staff
   > are uncertain what is allowed, especially regarding donor data or confidential information that
   > might feed into the system."
   — **The NonProfit Times**, 18 Feb 2026.

**Skeptical and critical voices**

8. > "Much skepticism about AI in the nonprofit sector stems from decades of watching 'transformative'
   > tools cycle through with limited results. After years of overpromised solutions, nonprofit
   > leaders now prioritize peer-proven tools with demonstrable dollar impact."
   — **OpenGrants**, *"Nonprofit Technology Trends 2026: What Leaders Need to Know Beyond the Hype."*
   🚩 Vendor-adjacent (grants platform), but the most explicitly skeptical framing retrieved.

9. > "…nonprofits now face the urgent question of whether they will shape how AI is governed, funded,
   > and constrained, or whether those decisions will be made primarily by vendors, markets, and
   > states."
   — **Nonprofit Quarterly**, *"AI in the Nonprofit Sector Is a Question of Governance, Not Just
   Technology,"* 1 Apr 2026. ✅ Independent sector journalism.

10. > "With clear governance and accountability, AI could help address long-standing capacity
    > constraints, but without them, it risks becoming another extraction mechanism that concentrates
    > power while dispersing risk."
    — **Nonprofit Quarterly**, same article, 1 Apr 2026. ✅ The strongest critical framing found —
    and notably the only source treating AI as a *power* question rather than a *productivity* question.

**Additional characterizations (attribution weaker — verify)**

11. > "Nonprofits aren't resisting AI — they're navigating it without the leadership infrastructure and
    > support systems needed to adopt it sustainably and responsibly."
    — **Board.Dev / Dell Technologies / TechSoup**, *Building the Leadership Nonprofits Need to Make
    AI Work* (n=180 nonprofits, 44 states). 🚩 Hardware-vendor-sponsored.

---

## Data gaps

### Retrieval failures (environmental, not sectoral)
- **NO PRIMARY DOCUMENT OPENED.** Egress policy returned 403 on every host attempted. The Virtuous
  PDF, the CEP PDF, the TechSoup PDF and the Board.Dev/Dell PDF all have known public URLs (listed
  in the source log) and should be retrieved in an environment without the block. **This is the
  single highest-value follow-up action for this workstream.**
- **Searches not run** (budget exhausted at 200 session-wide calls, after 22 in this workstream):
  1. Give.org *Donor Trust Report 2026* — n, field dates, AI question wording
  2. Nonprofit Tech for Good 2026 AI statistics — to establish primary attribution for the donor
     trust figures currently marked [UNVERIFIED]
  3. BoardSource AI governance — named as a priority source, never queried directly
  4. Stanford Social Innovation Review AI coverage — priority source, never queried directly
  5. Salesforce Nonprofit Cloud AI research — attempted once, returned only Virtuous material;
     no discrete Salesforce nonprofit AI adoption figure was located
  6. Funder-sponsored AI capacity-building program *evaluations* (as opposed to announcements)

### Substantive gaps in the sector's own evidence base
- **Beneficiary trust in AI: NO DATA FOUND.** Not one source measures how served populations feel
  about AI in service delivery. Largest gap in the workstream.
- **Documented incidents: NO DATA FOUND** after 4 targeted searches — no verified case of fabricated
  grant content, donor-data misuse, or biased screening at a US nonprofit or foundation. The risk
  discourse is entirely prospective.
- **Named nonprofits that abandoned AI tools: NO DATA FOUND** after 3 targeted searches.
- **Question wording for any adoption statistic: NOT RETRIEVED** for any source. The brief's central
  reconciliation task is therefore answered inferentially only.
- **Size controls on the high-impact 7%: NO DATA FOUND.** Whether the high-impact minority is
  distinguished by governance or merely by budget is unresolved and is a live confound.
- **Training approach, leadership involvement, dedicated budget and data readiness among the 7%: NO
  DATA FOUND** — four of the six characteristics the brief asked for.
- **What nonprofits want from governance support: NO DATA FOUND.** No retrieved instrument asked.
- **Non-adopters' stated needs: NO DATA FOUND.** No retrieved instrument surveyed non-adopters.
- **NTEN + Bridgespan 2026 survey: IN FIELD, UNPUBLISHED.** Likely the most important forthcoming
  non-vendor source. Monitor.
- **Field dates for the Virtuous report: UNRESOLVED CONFLICT** — "late 2025", "December 2025" and
  "February 2026" all appear in coverage. Only the 16 Feb 2026 release date is firm.

---

## Source log

| Source | URL | Primary/Secondary | Retrieved how | Credibility note |
|---|---|---|---|---|
| Virtuous/Fundraising.AI, *2026 Nonprofit AI Adoption Report* (PDF) | `539405.fs1.hubspotusercontent-na1.net/hubfs/539405/AI Report/Virtuous 2026 Nonprofit AI Adoption Report.pdf` | **Primary** | ❌ **FETCH BLOCKED (403)** — snippet only | 🚩🚩🚩 CRM vendor. n=346. Core source for 92%/7%/47%/81%/4%. Conclusions map onto sponsor's product category. |
| Virtuous report landing page | `virtuous.org/resource/the-2026-nonprofit-ai-adoption-report-download/` · `ai-adoption.report.virtuous.org` | Primary | ❌ Blocked (403) | Gated download. |
| Virtuous blog, *"...7 Patterns From the Top 7%"* | `virtuous.org/blog/how-to-transform-your-nonprofit-with-ai/` | Secondary (promotional) | ❌ Blocked — snippet only | 🚩🚩 Marketing content, not the report. Sole source for 4 of the 8 high-impact characteristics. |
| PR Newswire release, 16 Feb 2026 | `prnewswire.com/news-releases/...-302688325.html` | Primary (press release) | ❌ Blocked — snippet only | Source of the Cooper and Chappell quotes. Vendor-issued. |
| **The NonProfit Times**, "Nonprofits Embrace AI, But Little To Show For It So Far", 18 Feb 2026 | `thenonprofittimes.com/npt_articles/nonprofits-embrace-ai-but-little-to-show-for-it-so-far/` | Secondary | ❌ Blocked — snippet only | ✅ Independent trade press. Best secondary account of the Virtuous findings; source of quotes 4, 6, 7. |
| NonProfit PRO, "Nonprofit AI Adoption Hits 92%, But Only 7% See Major Impact" | `nonprofitpro.com/article/nonprofit-ai-adoption-hits-92-but-only-7-see-major-impact/` | Secondary | ❌ Blocked — snippet only | ✅ Independent trade press. Corroborates 92%/7%/65%/18%. |
| **CEP, *AI With Purpose*** (PDF) | `cep.org/wp-content/uploads/2025/09/CEP_AI_Layout_FINAL.pdf` | **Primary** | ❌ **FETCH BLOCKED (403)** — snippet only | ✅ **Highest-credibility source in the file.** n=451 nonprofits + 215 foundations + 16 interviews, Sept 2025, described as nationally representative. Independent research nonprofit, nothing to sell. **Retrieve this first.** |
| CEP report landing page | `cep.org/report-backpacks/ai-with-purpose-...` | Primary | ❌ Blocked | — |
| CEP, *State of Nonprofits 2026* (PDF) | `cep.org/wp-content/uploads/2026/05/CEP_State_of_Nonprofits_2026_FNL.pdf` | Primary | ❌ Blocked — title only | May 2026. Not examined; may contain AI content. Flag for WS1/WS2. |
| TechSoup/Tapp, *State of AI in Nonprofits 2025* | `page.techsoup.org/ai-benchmark-report-2025` · `blog.tappnetwork.com/tapp-and-techsoup-release-2025-ai-benchmark-report` | Primary | ❌ Blocked — snippet only | 🚩 n=1,300+. Source of 85.6% "exploring", 24% strategy, 66%/34% size split. Jan 2025 (partly pre-window). |
| TechSoup transcript, *AI-Powered Nonprofits: 2025 Report* | `techsoup.org/sitecollectiondocuments/webinar-...-2025-01-21-transcript.pdf` | Primary | ❌ Blocked — not examined | Webinar transcript, 21 Jan 2025. Potentially contains methodology detail. |
| **Coastal Cloud / Oxford Economics**, *AI Trends in Nonprofits 2026* | `coastalcloud.us/resources/ai-trends-in-nonprofits-2026-report/` · `.../the-ai-operations-report-2026-nonprofit/` | Primary | ❌ Blocked — snippet only | 🚩🚩 Salesforce implementation consultancy. **n=75 nonprofits screened for AI in production.** Best failure-mode data in the file; findings run against sponsor interest, which raises confidence. |
| **AI Equity Project 2025** | `alignab.ca/resource/ai-equity-project-2025-report/` | Primary | ❌ Blocked — snippet only | 🚩 n=850+, US+Canada. Sponsor unclear. Source of 6.9% policy / 9% ready / <4% training budget. **Internally inconsistent** (6.9% vs 15%) across citations. Cross-border sample. |
| AFP, "The New Currency of Fundraising: Trust in the Age of AI" | `afpglobal.org/new-currency-fundraising-trust-age-ai` | Secondary | ❌ Blocked — snippet only | ✅ Professional association. Vehicle for the AI Equity Project figures. |
| **Nonprofit Quarterly**, "AI in the Nonprofit Sector Is a Question of Governance, Not Just Technology", 1 Apr 2026 | `nonprofitquarterly.org/ai-in-the-nonprofit-sector-is-a-question-of-governance-not-just-technology/` | Secondary (analysis) | ❌ Blocked — snippet only | ✅ **Best independent critical voice found.** Source of quotes 9 and 10. |
| Whole Whale, "Top Nonprofit AI Policies 2025" | `wholewhale.com/tips/top-nonprofit-ai-policies-2025-analysis-and-trends/` | Secondary | ❌ Blocked — snippet only | 🚩 Agency. 82%/10% figures **unsourced**. Useful for naming the four reference policies (United Way, Red Cross, Oxfam, Save the Children). |
| Board.Dev + Dell + TechSoup, *Building the Leadership Nonprofits Need to Make AI Work* (PDF) | `45089564.fs1.hubspotusercontent-na1.net/hubfs/45089564/Building the Leadership Nonprofits Need to Make AI Work \| Board.Dev x Dell.pdf` | **Primary** | ❌ **FETCH BLOCKED** — snippet only | 🚩🚩 Dell-sponsored. n=180 across 44 states. Source of 24% board tech/data representation. Worth retrieving. |
| BDO, *2025 Nonprofit Standards Benchmarking* | `insights.bdo.com/2025-Nonprofit-Benchmarking-Report-Overview.html` | Primary | ❌ Blocked — snippet only | 🚩🚩 ~250 leaders. Highest adoption figure (97%/92%); the split framing is **[UNVERIFIED]**. |
| Google.org blog, "Google.org shares new report on AI use among nonprofits" | `blog.google/company-news/outreach-and-initiatives/google-org/google-for-nonprofits-generative-ai-report/` | Primary-ish | ❌ Blocked — snippet only | 🚩 Platform sponsor. **Source of the single best datapoint in the file (1 in 5 with ≥half the org using gen AI).** n and field dates NOT retrieved — high priority to verify. |
| Google.org Accelerator: Generative AI | `blog.google/.../generative-ai-accelerator-cohort-2025/` · `impactchallenge.withgoogle.com/genaiaccelerator` | Primary | ❌ Blocked — snippet only | [Announced] 21 orgs (2024), 20 orgs + $30M (2025). "30M beneficiaries over 3 years" is a **projection**. Grantee "1/3 time, 1/2 cost" claim is self-report to funder. |
| Fast Forward, *2025 AI for Humanity Report* | `ffwd.org/2025-ai-for-humanity-report` | Primary | ❌ Blocked — snippet only | 🚩🚩🚩 Accelerator applicants — extreme selection bias. Useful only as within-cohort profile. |
| Chronicle of Philanthropy, "Grant Makers Don't Understand Nonprofits' A.I. Needs" | `philanthropy.com/opinion/grant-makers-dont-understand-nonprofits-a-i-needs-heres-how-to-change-that/` | Secondary | ❌ Blocked — snippet only | ✅ Independent trade press, Oct 2025. Vehicle for the **TAG** figures (81%/30%/9%) and the GitLab Foundation example. |
| Technology Association of Grantmakers (TAG) survey | Not located directly | Primary | ❌ Not located — cited via Chronicle | 🚩 Membership self-selection. **Foundations, not nonprofits.** Underlying report should be located. |
| Candid, "Where do foundations stand on AI-generated grant proposals?" | `candid.org/blogs/funders-insights-on-ai-generated-grant-application-proposals/` | Primary-ish | ❌ Blocked — snippet only | ✅ Independent infrastructure nonprofit. Source of 10% accept / 67% undecided / <1% detected. |
| Candid, "Will AI soon be reviewing your grant applications?" | `candid.org/blogs/will-foundations-soon-use-ai-to-screen-grant-applications/` | Secondary | ❌ Blocked — snippet only | ✅ |
| Candid, "Getting started on a responsible AI use policy for nonprofits" | `candid.org/blogs/how-to-create-responsible-ai-use-policy-for-nonprofits/` | Secondary (guidance) | ❌ Blocked — snippet only | ✅ Governance-support provider. |
| NTEN AI For Nonprofits Resource Hub | `nten.org/learn/resource-hubs/artificial-intelligence` | Primary | ❌ **Blocked (403)** — snippet only | ✅ Sector intermediary. Free templates and governance resources. Contents not inspected. |
| ANB Advisory (Bruce & Afriyie), *AI Policy Template*, Sept 2024 | `word.nten.org/wp-content/uploads/2024/08/AI-Policy-Template-by-ANB-Advisory.pdf` | **Primary** | ❌ Blocked — snippet only | ✅ Only template found with **NIST AI RMF** lineage. Pre-window (Sept 2024) but still the reference artifact. |
| **NTEN + Bridgespan**, *2026 State of Nonprofit AI Adoption and Governance* survey | `surveymonkey.com/r/5277QR7` | Primary (instrument) | Search result only | ⏳ **IN FIELD, RESULTS UNPUBLISHED.** Promoted by NTEN CEO Amy Sample Ward. Highest-value forthcoming non-vendor source. **MONITOR.** |
| Bridgespan, "AI Can't Be Ignored: Exploring the Opportunities for Nonprofits and the Social Sector" | `bridgespan.org/insights/exploring-ai-opportunities-for-nonprofits-and-the-social-sector` | Secondary | ❌ Blocked — title only | ✅ Not examined. Follow up. |
| Give.org, *Donor Trust Report 2026* | `give.org/donor-trust-report/2026-trends-in-donor-trust-and-perspectives` | Primary | ❌ Blocked — **not searched (budget)** | ✅ BBB Wise Giving Alliance. Likely primary source for donor-trust AI figures. **Unverified — high priority.** |
| Nonprofit Tech for Good, 2026 AI Marketing & Fundraising Statistics | `nptechforgood.com/101-best-practices/ai-marketing-fundraising-statistics-for-nonprofits/` | **Tertiary (compilation)** | ❌ Blocked — snippet only | 🚩 Statistics compilation, not original research. Probable route by which the 31%/43%/9% and 54.5% donor figures entered circulation. **Do not cite; trace to originals.** |
| NPT, "AI Generated Info Not Swaying Some Donors" | `thenonprofittimes.com/npt_articles/ai-generated-info-not-swaying-some-donors/` | Secondary | ❌ Blocked — title only | ✅ Not examined. |
| Bonterra funder report | `businesswire.com/news/home/20251110626529/en/...` | Primary (press release) | ❌ Blocked — headline only | 🚩🚩 Vendor. 91%/92%. Headline only. |
| Deloitte, "Sixty-one percent of health nonprofits use gen AI..." | `deloitte.com/us/en/Industries/life-sciences-health-care/blogs/health-care/...` | Secondary | ❌ Blocked — headline only | 🚩 Subsector (health). Headline only — **do not cite unverified.** |
| Social Current, "The Growing AI Gap Between Social Sector Organizations", Jan 2026 | `social-current.org/2026/01/the-growing-ai-gap-between-social-sector-organizations/` | Secondary | ❌ Blocked — title only | ✅ Sector membership org. Not examined. |
| Forvis Mazars, *2026 State of the Nonprofit Sector: AI Adoption & Governance* (Jun 2026); *AI Governance for Nonprofit Boards* (Feb 2026) | `forvismazars.us/forsights/2026/06/...` · `.../2026/02/ai-governance-for-nonprofit-boards` | Secondary | ❌ Blocked — titles only | 🚩 Accounting/advisory firm. Not examined. |
| OpenGrants, "Nonprofit Technology Trends 2026: ...Beyond the Hype" | `opengrants.io/nonprofit-technology-trends-2026-...` | Secondary | ❌ Blocked — snippet only | 🚩 Vendor-adjacent. Source of quote 8 (skepticism framing). |
| philanthropy.org, "AI and Nonprofits: Poll Results" | `philanthropy.org/ai-and-nonprofits-quick-poll/` | Primary (quick poll) | ❌ Blocked — not examined | Quick poll — low rigor. |
| **DISCARDED:** "Small Nonprofits Bleed Funding as Faulty AI Grant Tools Mislead Research" | `theglobeandmail.com/investing/markets/markets-news/GetNews/33414334/...` and syndications | **Paid press release** | Snippet only | ❌❌ **DO NOT USE.** GetNews wire distribution, apparently from AI grant vendor Sharke.ai. Unverifiable "Crisis Report", unverifiable Stanford citation. Recorded as an example of vendor-manufactured failure content. |
| One Hundred Nights, "The 47% Without AI Policies" et al. | `onehundrednights.com/article/nonprofit-ai-policy-governance-gap/` | **Tertiary (SEO)** | Snippet only | ❌ SEO content built on the Virtuous statistic. No independent value. |
| Maine Association of Nonprofits, "Nonprofits and AI" | `nonprofitmaine.org/blog/nonprofits-and-ai` | Secondary | ❌ Blocked — title only | ✅ State-association evidence of policy-support diffusion. |
| NJ Center for Nonprofits, "AI Ethics and Policy for Nonprofits" (event) | `njnonprofits.org/event/ai-ethics-and-policy-for-nonprofits-...` | Secondary | ❌ Blocked — title only | ✅ State-association evidence. |
| The Nonprofit Alliance, AI resource page | `tnpa.org/get-involved/artificial-intelligence/` | Secondary | ❌ Blocked — title only | ✅ Not examined. |

**Search count this workstream:** 22 distinct WebSearch queries (target 28+; session budget
exhausted). **Successful direct fetches: 0 of 8 attempted** (all 403, organization egress policy).
