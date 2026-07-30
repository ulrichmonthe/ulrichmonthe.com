# Workstream 2 — Grant-Seeking Economics

**Research window:** mid-2025 through mid-2026. **Compiled:** 2026-07-30.

---

## ⚠️ READ THIS FIRST — RESEARCH CAPABILITY WAS SEVERELY CONSTRAINED

This section is not a caveat. It changes how every number below should be treated.

**1. WebFetch was 100% blocked.** Every attempt to retrieve a primary document returned HTTP 403 from the session's egress proxy (organization policy denial, confirmed via `$HTTPS_PROXY/__agentproxy/status` → `connect_rejected: "gateway answered 403 to CONNECT"`). Hosts denied, 8 for 8:

| Host attempted | Document I was trying to read |
|---|---|
| `grantstation.com` | 2025 State of Grantseeking Report + Key Findings PDF + Government Report PDF + methodology page |
| `cep.org` | *A Sector in Crisis*, *Mounting Pressure*, *State of Nonprofits 2026* PDFs |
| `urban.org` | Federal grants-to-nonprofits data tables |
| `candid.org` | Government-reliance blog and grants data fact sheet |
| `arxiv.org` | von Hippel & von Hippel (2015) grant-writing cost study |
| `instrumentl.com` | Grant statistics compilation |
| `nonprofitoregon.org`, `writeepicgrants.com` | Secondary summaries of GrantStation |
| `en.wikipedia.org`, `irs.gov` | Control tests — also blocked |

`curl` through the proxy fails identically (`CONNECT tunnel failed, response 403`). Per `/root/.ccr/README.md`, policy denials must be reported, not routed around.

**2. The session-wide WebSearch budget was exhausted at 200/200** partway through my work. Because the budget is shared across all six workstreams, I completed **16 searches**, not the 30+ the brief specified. The last two queries I issued were refused.

**Consequence for evidence grading:** I read **zero primary documents**. Every figure below comes from a search-engine-generated summary of snippets. Under the brief's own grading scheme, **nothing here can honestly be graded [Documented]** — the highest grade available is **[Reported, snippet-only]**. Search-engine summaries are themselves a synthesis layer that can conflate two reports, misattribute a sample size, or fabricate an inference (I caught it doing all three — see Data gaps). Treat every number as a **lead to verify**, not as a citable statistic.

**Recommendation to the client: this workstream should be re-run with fetch access before any number is published.**

---

## Key findings

1. **The clearest, best-sourced number in this workstream is the substitution-gap math, and it is decisive.** Candid puts government grants to nonprofits at **~$303B/yr** against **~$107B/yr** in private foundation grantmaking; foundations would have to raise grantmaking by **~282%** to backfill. My own arithmetic check confirms internal consistency ($303B ÷ $107B = 2.83 → +283%). Foundation money cannot substitute for federal money at the sector level. [Reported, snippet-only]

2. **Demand-side pressure on foundations is measured, not anecdotal — and it is very large.** The Center for Effective Philanthropy found **87% of foundation leaders reported increased demand for grant funding**, from a survey of foundations giving ≥$5M annually (Aug–Sep 2025, 227 foundations responding, 30% response rate). This is the single strongest quantitative support for the "application surge" thesis. [Reported, snippet-only]

3. **But foundation supply barely moved.** Only **~30% of foundations increased payout beyond plan, at a median increase of 2 percentage points**. The gap between 87% seeing more demand and 30% adding money *is* the competition story. [Reported, snippet-only]

4. **Grantseekers confirm it got harder.** CEP's *State of Nonprofits 2026* (Feb 2026, 380 responding of 887 surveyed, 43% RR): **~60% of nonprofit CEOs say it has become harder to secure foundation grants since January 2025**, and **>40% reported actual reductions in foundation funding received**. [Reported, snippet-only]

5. **Individual foundations report concrete surges with award rates near 20% or far below.** Community Foundation Tampa Bay: **426 applications, +17% over 2025, 88 programs funded** (≈20.7% award rate, my arithmetic). Ackerman Foundation: **applications up ~50%**, funding pool flat, **met <40% of dollars requested**. George Family Foundation: **~4% of LOIs invited to full proposal, ~1% ultimately funded**. [Reported, snippet-only]

6. **GrantStation does not publish a per-application win rate — and this is the most important methodological finding in the workstream.** What GrantStation reports is the share of *organizations* receiving *at least one* award, segmented by how many applications they submitted. That metric rises mechanically with submission volume and cannot be read as a proposal-level success rate. Anyone citing "82.9% success rate for 3–5 applications" as a win rate is misreading it. **NO per-application foundation win rate was found from any source.**

7. **Grantseekers themselves do not rank competition as their top problem.** In GrantStation's 2025 data the barriers to successful grantseeking were staff/time limitations **24%**, finding matching opportunities **15%**, increased funder requirements **14%**, and *competition for finite monies* **10%** — fourth. This is real disconfirming evidence and is discussed below. [Reported, snippet-only]

8. **Hours-per-application figures are consultant estimates, not measured data.** The only *measured* time-use study I located is academic (astronomers/psychologists, 2015): **116 PI hours + 55 co-I hours per federal research proposal**. Every nonprofit-sector figure (15–20h foundation, 80–200h federal) traces to grant-writing vendors and consultancies with no published methodology. **There is no credible measured time-use study of nonprofit foundation-proposal preparation.**

9. **Rejection economics is essentially undocumented.** No source produced declined-applications-per-award, poor-fit submission rates, or sunk-cost estimates for the nonprofit sector. This is a genuine hole in the sector's evidence base, not a search failure.

10. **Countervailing signal:** GrantStation's mid-2025 data shows organizations' *reliance* on grants **decreasing** (share drawing ≤10% of funding from grants rose 26.0% → 28.5%) and federal grant-seeking activity **dropping ~12 points to 43.2%**. Total application volume may be shifting between funder types rather than rising uniformly.

---

## Application volume data

### Metadata table

| # | Finding | Source (originator) | n | Field dates | Sponsor / bias flag | Grade | Retrieval |
|---|---|---|---|---|---|---|---|
| A1 | **87% of foundation leaders reported increased demand for grant funding** | Center for Effective Philanthropy, *Mounting Pressure* / *A Sector in Crisis* | 227 foundations responding (30% RR); population = all US independent/community foundations giving ≥$5M/yr | Aug–Sep 2025 | CEP is a nonprofit research org serving foundations; funder-facing but no product to sell. Low vendor bias. Self-selection at 30% RR is a real limitation. | [Reported] | Snippet only — cep.org blocked |
| A2 | **~30% of foundations increased payout beyond plan; median increase 2 percentage points** | CEP, same survey | as above | Aug–Sep 2025 | as above | [Reported] | Snippet only |
| A3 | **64% of foundations provided emergency/rapid-response funding; 42% made more unrestricted grants; ~40% streamlined application/reporting processes** | CEP, same survey | as above | Aug–Sep 2025 | as above | [Reported] | Snippet only |
| A4 | **~60% of nonprofit CEOs say it is harder to secure foundation grants since Jan 2025; >40% saw actual reductions in foundation funding** | CEP, *State of Nonprofits 2026* | 380 responding of 887 surveyed (43% RR) | **February 2026** | as above | [Reported] | Snippet only |
| A5 | **73% of nonprofits report increased demand for services** | CEP, *State of Nonprofits 2026* | as A4 | Feb 2026 | as above | [Reported] | Snippet only |
| A6 | **Community Foundation Tampa Bay: 426 applications, +17% vs 2025; 88 programs funded; >$2.5M awarded; described as a record year** | 83 Degrees Media reporting on CFTB | single foundation | 2026 grant cycle | Local trade press reporting a foundation's own announcement. Single-case. | [Reported] | Snippet only |
| A7 | **Ackerman Foundation: applications up ~50%; $100K to 43 nonprofits; pool flat vs prior year; met <40% of dollars requested** | Hudson Valley 360 / Daily Gazette | single foundation | 2026 cycle | Local press; very small funder ($100K total). Not generalizable. | [Reported] | Snippet only |
| A8 | **George Family Foundation: ~4% of LOIs invited to full proposal; ~1% ultimately approved. Foundation states it expects 2025 and 2026 to be more competitive than a typical year.** | georgefamilyfoundation.org "How to Apply" | single foundation | stated as typical-year | Foundation's own published guidance — primary-ish, but a standing page, not a dated measurement | [Reported] | Snippet only; **verification search was refused (budget exhausted)** |
| A9 | **Federal government grants dropped ~12 points to 43.2%** as a cited funding source among respondents | GrantStation, *2025 State of Grantseeking Government Update Report* | 1,056 organizations | activity Jan–Jul 2025 | **VENDOR BIAS: GrantStation sells grant-database subscriptions.** Self-selected nonrandom sample of GrantStation-affiliated orgs, SurveyMonkey, explicitly "not scientifically conducted" per their own methodology page. | [Reported] | Snippet only |
| A10 | **76.5% increased private or corporate submissions; 57.7% expanded individual donor outreach; 63.1% reduced or eliminated programs** | GrantStation Government Update Report | 1,056 | Jan–Jul 2025 | as A9 | [Reported] | Snippet only |
| A11 | **~1/3 of nonprofits experienced federal reductions or cancellations, median loss $150,000** | GrantStation Government Update Report | 1,056 | Jan–Jul 2025 | as A9 | [Reported] | Snippet only |
| A12 | **~1/3 of nonprofit service providers had a government funding disruption in H1 2025: 21% lost a grant/contract, 27% delay or freeze, 6% stop-work order** | Urban Institute, *How Government Funding Disruptions Affected Nonprofits in Early 2025* | **2,737**, described as nationally representative | fielded **Apr–Jun 2025** | Urban Institute — highest methodological credibility in this set. Nationally representative panel. | [Reported] | Snippet only — urban.org blocked |

### The single most important application-volume number

**A10 is the load-bearing statistic for the surge thesis: 76.5% of grantseekers say they increased private or corporate submissions in Jan–Jul 2025.** That is the mechanism — federal pullback pushing applications into the foundation channel — measured on the grantseeker side, and it pairs with A1 (87% of foundations seeing more demand) measured on the funder side. Two independent surveys, opposite sides of the transaction, same direction. **That is the strongest triangulation in this workstream.**

Its weakness: A10 comes from the vendor-biased, self-selected GrantStation panel. It should not be published without reading the actual report.

### What I could NOT establish

- **NO DATA FOUND** for aggregate foundation application volume 2024 vs 2025 vs 2026. No sector-wide counter exists. Candid tracks grants *made*, not applications *received*. Grants-management platforms (Foundant, Fluxx, Submittable, Blackbaud) sit on exactly this data and I found no evidence any of them has published an application-volume index. **To answer this question, one of those vendors would have to publish aggregate submission counts across their customer base year over year. Ask them directly.**
- **NO DATA FOUND** on 2026 application volumes at the sector level. The CEP Feb 2026 survey measures perceived difficulty, not counts.

---

## Win rates

### The measurement problem, stated plainly

**GrantStation's widely-cited "success rates" are organization-level "received at least one award" rates, segmented by number of applications submitted.** They are not proposal win rates. A 95% figure for organizations submitting 11–20 applications is close to arithmetically inevitable and says nothing about the probability any given proposal succeeds. The commonly repeated advice that "submitting more applications increases your success rate" is, on this data, partly a statistical artifact.

### The two conflicting ladders I retrieved

**Ladder 1** (attributed in search results to GrantStation 2025 data):

| Applications submitted | Share of orgs receiving ≥1 award |
|---|---|
| 1 | 70.1% |
| 2 | 75.6% |
| 3–5 | 82.9% |
| 6–10 | 91.8% |
| 11–20 | 95.0% |

**Ladder 2** (attributed in search results to the 2026 State of Grantseeking Report):

| Applications submitted | Share of orgs receiving ≥1 award |
|---|---|
| 1 | 62% |
| 3–5 | 88% |
| 6–10 | 96% |

**Triangulation:** These are not reconcilable as stated. Three possible explanations, none confirmed:
1. Ladder 1 is from the **Government** Update Report (government awards only) and Ladder 2 from the **main** report (all funder types) — different denominators.
2. They are different survey years (2024 activity vs 2025 activity) and the 1-application rate genuinely fell 70.1% → 62%.
3. The search summarizer conflated reports.

**If explanation 2 is correct it is a headline finding — the single-application success rate falling 8 points would be direct evidence of tightening.** I could not test it. **This is the highest-value single verification task for a re-run: open both GrantStation PDFs and determine whether the 1-application rate moved.**

### Other win-rate findings

| Finding | Source | Grade | Note |
|---|---|---|---|
| **22.2% of respondents received no government awards; 22.2% received 3–5; 18.0% one; 14.1% two; 10.9% six-to-ten; ~8% more than ten** | GrantStation 2025 Government Report (n=1,056) | [Reported] | Award-count distribution, not win rate |
| **31.3% of respondents submitted 3–5 applications** — the most common activity level | GrantStation 2025 Government Report | [Reported] | |
| **Organizations are 60% more likely to receive a grant if they cultivated a relationship ahead of the ask** | Grants Plus blog, citing State of Grantseeking | [Reported, weak] | **Prior-relationship effect — directly responsive to the brief.** But this is a consultancy's blog summarizing GrantStation; "60% more likely" is ambiguous (relative risk? percentage points?). **Do not publish without the underlying table.** |
| **Local/community-focused grants deliver success rates between 30% and 50%; large national/federal grants lower due to competition** | grants.com, loosely attributed to "the 2026 State of Grantseeking Report" | [Anecdote — DISCARD] | Content-farm domain, attribution unverifiable, no methodology. I could not confirm GrantStation publishes any such figure. **Flagged for exclusion.** |
| **61% of grantseekers rely on only one or two people for grant writing and submission** | Submittable blog, "34 Grant Statistics" — a **2020** compilation | [Reported, stale] | Outside research window; included only as capacity context |

### Win rates by org size and funder type

**NO DATA FOUND after 4 searches touching this question.** GrantStation segments by budget size and mission focus, and by funder type (private foundations cited by 89% of respondents as an award source; state government 51%, local 43%, federal 40%) — but the segmented *win-rate* tables sit inside the paywalled/blocked PDFs. The data very likely exists in the GrantStation reports. **It is retrievable; I simply could not retrieve it.**

---

## Hours and cost per application

**This is the weakest-evidenced part of the workstream, and the weakness is in the underlying literature, not only in my access.**

### Measured data (one study, wrong sector)

**von Hippel, T. & von Hippel, C. (2015), "To Apply or Not to Apply: A Survey Analysis of Grant Writing Costs and Benefits," PLOS ONE 10(3):e0118494.**
- **n = 113 astronomers + 82 psychologists**, active federal grant applicants
- **Field window: grant-writing history January 2009 – November 2012**
- **The average proposal takes 116 PI hours and 55 co-investigator hours to write.**
- Time spent writing was **not** related to whether the grant was funded.
- Investigators who wrote more grants received more funding.
- Authors conclude that **funding rates below ~20% are likely to drive at least half of active researchers away from federally funded research.**
- Grade: **[Documented in the literature, but retrieved snippet-only]** — peer-reviewed, but this is *academic research grants*, not nonprofit foundation proposals. **Use as an analogue, never as a nonprofit statistic.**

That last finding — a ~20% funding rate as the threshold at which applicants exit — is worth flagging to the client. Community Foundation Tampa Bay's implied 20.7% award rate sits exactly on it.

### Consultant/vendor estimates (no methodology found for any)

| Estimate | Attributed to | Assessment |
|---|---|---|
| Foundation grant: **15–20 hours** (some sources 5–20h; <$5,000 grants "10 hours or less") | Grant-writing consultancies (Allied Grant Writers, DH Leonard, Lakeview Consulting, Grant Writing & Funding) | [Anecdote] — practitioner rules of thumb. No survey behind any of them. |
| Typical nonprofit grant: **30–50 hours** of staff time | Same cluster | [Anecdote] |
| Federal grant: **80–200 hours** (range extends 70–300h) | Same cluster | [Anecdote] |
| Grant writing generally: **20–40 hours per application** | grantcycle.com | [Anecdote] |
| **Cost of writing a single grant application: $600 – $18,000** | grantcycle.com | [Anecdote] — 30x range makes it near-useless. Almost certainly derived by multiplying the hour ranges above by assumed rates. Circular. |
| **Cost of preparing reports for a single grant: $720 – $2,880** | grantcycle.com | [Anecdote] |
| **Grant management via spreadsheets costs an average of 20% of grant funding** | grantcycle.com | [Anecdote — DISCARD]. grantcycle.com sells grant-management software; this is a vendor selling against the status quo. **Textbook vendor bias.** |
| **"Average grant proposal creation and application/selection process takes 27.45 hours per grant"** attributed to Project Streamline | grantcycle.com, attributing to Project Streamline | **DISCARD.** The two-decimal precision on a 2008-era study is a red flag; I could not locate this figure in any Project Streamline material; peakgrantmaking.org was blocked. **Do not use.** |

### The "net grant" concept — conceptually valuable, numerically thin

Exponent Philanthropy argues nonprofits receive a **"net grant"** — award value minus the true cost of obtaining and managing it — and illustrates with **a $10K grant worth ~$9K to the grantee, and a $20K grant worth ~$17K**. That implies a **10–15% cost-of-acquisition drag**, rising as a share for smaller grants. [Reported, illustrative]. Exponent explicitly presents these as illustrations, not measurements. **The framing is the useful output here, not the numbers.**

The 2008 Project Streamline report *Drowning in Paperwork, Distracted from Purpose* (Grants Managers Network, now PEAK Grantmaking) remains the canonical treatment of application burden and describes an "effectiveness paradox." Referenced burden scale: **a single organization may juggle 40–60 applications and as many distinct reporting requirements from 20–30 funders**. [Reported, and ~18 years old — outside the research window by a wide margin.]

### Grant professional salary data

**NO DATA FOUND after 3 searches.** I did not retrieve any GPA (Grant Professionals Association) compensation survey, nor any GPA member survey on hours. GPA's site appeared in results only as a State-of-Grantseeking partner page. **Without a salary figure I deliberately did NOT compute a cost-per-application — doing so would have required inventing a wage rate. Per the anti-fabrication rule, that gap is left open.**

---

## Competition trend and the federal-to-foundation substitution gap

### The substitution gap — the best-supported quantitative finding in this workstream

| Quantity | Figure | Source | Note |
|---|---|---|---|
| Government grants to nonprofits, annual | **~$303 billion** to **100,000+ nonprofits**; ~30% of Form-990-filing nonprofits report government grant funding | Candid | All levels of government |
| Private foundation grants to US nonprofits, annual | **~$107 billion** | Candid | |
| Required foundation increase to backfill | **282%** | Candid | **Arithmetic check passes:** $303B ÷ $107B = 2.83 → +283%. Internally consistent. |

**Triangulating the government-grants total (three figures, three definitions — do not average them):**

- Urban Institute: **$267B in 2021**, all levels of government including foreign — cited as published February [year not captured].
- Urban Institute time series: **$304B (2021), $294B (2022), $240B (2023)** — "at least $240B each year."
- Candid: **~$303B annually**.

The 2021 figures ($267B vs $304B) differ by ~14% within the same institution, almost certainly reflecting different inclusion rules (grants only vs grants + contracts; which government levels; which filer universe). **Report the range $240B–$304B and name the year, never a single point estimate.** Candid's $303B appears to sit at the top of the range and near the 2021 peak; if the correct current-year figure is the 2023 $240B, the required foundation increase falls to roughly +124%… **which is still impossible.** The conclusion is robust to the definitional dispute.

**Scale conclusion: private foundation giving is roughly one-third of government grantmaking to nonprofits. There is no version of the arithmetic in which foundations substitute for federal money.**

### Supporting evidence on the qualitative mismatch (restricted vs. unrestricted, program vs. operations)

- CEP: **42% of foundations made more unrestricted grants** in response to the crisis — meaning a **majority did not**, and the baseline for foundation money remains restricted/program-tied. [Reported]
- CEP: **>40% of nonprofits reported actual reductions in foundation funding received** even as demand rose — foundation money did not merely fail to expand, it contracted for a large minority. [Reported]
- Urban Institute: among nonprofits that experienced disruption, **government funding made up 42% of their revenue**, versus **under a third of overall revenue** across all nonprofits. The organizations most exposed are exposed *deeply*, which is precisely the profile foundation grants are worst suited to replace. [Reported]

### Competition-trend evidence

**Funder side:**
- **87% of foundation leaders report increased demand for grant funding** (CEP, Aug–Sep 2025, 227 foundations). [Reported]
- Against which: **~30% increased payout beyond plan, median +2 percentage points.** [Reported]

**Grantseeker side:**
- **76.5% increased private or corporate submissions** (GrantStation, Jan–Jul 2025, n=1,056). [Reported]
- **~60% of nonprofit CEOs say foundation grants are harder to secure since Jan 2025** (CEP, Feb 2026, n=380). [Reported]

**Individual-foundation oversubscription:**

| Foundation | Applications | Awards | Implied award rate | Change | Grade |
|---|---|---|---|---|---|
| Community Foundation Tampa Bay (2026 cycle) | **426** | **88 programs**, >$2.5M | **20.7%** (my arithmetic) | **+17%** vs 2025 (implying ~364 in 2025, my arithmetic) | [Reported] |
| Ackerman Foundation (2026) | not stated | **43 nonprofits**, $100K total | not computable | **applications up ~50%**; pool flat; **met <40% of dollars requested** (implying >$250K requested, my arithmetic) | [Reported] |
| George Family Foundation (typical year) | "high volume" of LOIs | — | **~4% of LOIs invited to full proposal; ~1% funded** | Foundation states it expects 2025 and 2026 to be more competitive than typical | [Reported] |
| New York Foundation | "hundreds of requests each cycle" | **~5 new grants per cycle** | ~1–2% (my inference from "hundreds") | no trend stated | [Anecdote] |

**Caution:** four self-selected foundations that chose to publicize a surge. This is a convenience sample with obvious publication bias — foundations announcing "applications flat this year" is not a press release anyone writes. **These cases illustrate; they do not measure.**

**One claim I am flagging for exclusion:** OpenGrants asserts "one major regional funder saw a 3.5x spike in a single cycle, and only about a quarter of recent inquiries advanced." **The funder is unnamed, no date is given, and OpenGrants sells grant-seeking services. DISCARD.**

---

## Rejection / wasted-effort economics

**NO DATA FOUND after 5 searches across: declined applications per successful one; applications submitted to poor-fit funders; sunk cost of unsuccessful grant-seeking; total sector-wide hours spent on rejected proposals.**

What I have instead, and it is thin:

1. **Award-count distribution as a weak proxy:** 22.2% of GrantStation respondents received **no** government awards in the period. That is a floor on total-loss grantseekers but says nothing about applications wasted by those who did win. [Reported]

2. **Foundation-side funnel ratios imply the rejection volume:** if George Family Foundation invites ~4% of LOIs and funds ~1%, then **99 of every 100 LOIs written to that funder are sunk effort.** At Tampa Bay's 20.7% award rate, **~338 of 426 applications were unsuccessful in a single cycle at a single foundation.** Multiplying either by an hours figure is exactly the temptation I am declining, because the hours figures are unmeasured (see above). **The client should not let anyone do that multiplication and call it a finding.**

3. **The AI-volume hypothesis — untested but important.** The Charity CFO argues that AI has made it easier to submit more applications but not better ones, and that when organizations use AI to apply broadly without funder-fit analysis, **volume rises and win rates fall**. This is the mechanism by which wasted effort would be *increasing* right now. **It is asserted, not measured — no data was offered.** [Anecdote] **This is the most interesting untested hypothesis I encountered and would be my top recommendation for original research.**

4. **The von Hippel 20% threshold** (above) is the only quantitative treatment I found of the point at which grant-seeking stops being worth it — and it is from astronomy/psychology, not the nonprofit sector.

**What would need to exist to answer this properly:** a grants-management platform (Foundant, Fluxx, Submittable, Blackbaud) publishing, across its funder customer base, (a) applications received per cycle year over year, (b) awards made, and (c) declines by reason code including "outside guidelines." All three fields already exist in those systems. Nobody publishes them. **That is the single highest-leverage data ask in this entire workstream.**

---

## Disconfirming evidence

Per the brief I spent a dedicated cycle looking for evidence the thesis is wrong. I found real disconfirmation. It does not overturn the thesis, but it constrains it.

**1. Grantseekers rank competition FOURTH among barriers, at only 10%.** GrantStation 2025: staff and time limitations **24%**, difficulty finding opportunities matching mission/location/program **15%**, increased funder requirements **14%**, **competition for finite monies 10%**. If competition had truly spiked to crisis level, one would expect grantseekers to name it first. They name their own capacity first. **This meaningfully weakens the "competition is the binding constraint" framing — the binding constraint grantseekers report is internal capacity.** [Reported]

**2. Reliance on grant funding DECREASED in H1 2025.** GrantStation: the share of organizations drawing ≤10% of total funding from grants rose **26.0% → 28.5%**, and the 11–25% band rose **17.6% → 19.4%**. Organizations are moving *away* from grant dependence, not piling further into it. [Reported]

**3. Federal grant-seeking activity FELL sharply** — federal grants cited as a source dropped **~12 points to 43.2%**. Some of the "surge" narrative may be substitution *between* channels rather than growth in total application volume. Nobody has published a total-volume figure that would settle this. [Reported]

**4. GrantStation's organization-level success rates do not show collapse.** 70–95% of organizations received at least one award depending on volume submitted. Whatever is happening to per-proposal odds, most active grantseekers were still winning something. [Reported]

**5. The measurement artifact.** As set out under Win rates, the "more applications → higher success" finding is substantially a denominator effect. It is repeated uncritically across the sector's trade press. **A thesis built on it would be built on sand.**

**6. The individual-foundation surge cases are a biased sample.** Tampa Bay, Ackerman, George Family — every one is a funder that chose to publicize demand pressure. **NO DATA FOUND on any foundation reporting flat or declining application volume**, and that absence is itself evidence of publication bias rather than evidence of universal surge.

**7. Foundation assets and giving are rising, not falling.** Headlines retrieved (MinistryWatch, Chronicle of Philanthropy, Candid) indicate foundation assets at all-time highs and private foundation giving projected to grow **5–7% in 2026**. The pool is growing. It is simply growing far slower than demand — which is a *different* claim from "the pool is shrinking," and the brief's framing should reflect that. [Reported]

**Net assessment:** the application-surge thesis survives, principally on CEP's 87% (funder side) triangulated against GrantStation's 76.5% (grantseeker side). But two of the thesis's usual supporting props — collapsing win rates and grantseekers naming competition as their top problem — **are not supported by the data I retrieved, and the second is actively contradicted.**

---

## Verbatim quotes

**This section is largely a failure and I am reporting it as such rather than filling it.**

The brief asked for 6–10 verbatim quotes with full attribution, prioritizing grant professionals and program officers. **Capturing verbatim quotes requires reading source documents. Every document fetch was blocked.** Search-engine output is paraphrase; reproducing it as quotation would be fabrication. I therefore have **one** fragment that appeared inside quotation marks in retrieved output:

> **1.** Community Foundation Tampa Bay, on its 2026 applications — the applications *"reflected a growing need across our region, particularly for programs focused on basic needs such as housing, food security, clothing, healthcare, and other essential services."*
> — Reported by 83 Degrees Media. **Speaker not identified in retrieved text.** [Reported, snippet-level — verify wording and attribution before use.]

**Quotes 2–10: NOT CAPTURED.** Do not let this gap be filled from memory by any downstream process.

**Where the quotes are, for a re-run with fetch access:**
- CEP *A Sector in Crisis* (Jan 2026) — includes **27 nonprofit-leader interviews and 31 foundation-leader interviews, both conducted September 2025.** This is the single richest quote source identified and it is exactly on-brief: foundation leaders describing demand in their own words. `cep.org/wp-content/uploads/2026/01/CEP_A_Sector_in_Crisis_FNL.pdf`
- CEP *State of Nonprofits 2026* — `cep.org/wp-content/uploads/2026/05/CEP_State_of_Nonprofits_2026_FNL.pdf`
- CEP *Mounting Pressure* — `cep.org/wp-content/uploads/2025/10/Mounting_Pressure_FINAL.pdf`
- Let's Hear It podcast, episode with CEP's Elisha Smith Arrillaga on *A Sector in Crisis* — `letshearitcast.com/elisha/` (interview format, quote-dense)
- The Charity CFO, "The State of Grant Seeking in 2026" article + YouTube episode 155 — practitioner voice on AI-driven volume
- Write Epic Grants episode #291 on the 2025 SoG report — grant-professional voice

---

## Data gaps

Ordered by how much they matter to the client.

**1. No sector-wide foundation application-volume series exists. [STRUCTURAL — not a search failure]**
Candid counts grants *made*. Nobody counts applications *received*. The only entities that could are the grants-management SaaS vendors. **Until one publishes, "applications are up X% sector-wide" is unanswerable and any figure claiming it should be treated as fabricated.**

**2. No per-application win rate for foundation grants, from any source. [STRUCTURAL]**
GrantStation's metric is organization-level "≥1 award." The proposal-level denominator is not published by anyone. **This is the number the client most wants and it does not exist in public data.**

**3. Contradictory GrantStation win-rate ladders, unresolved. [MY ACCESS FAILURE — recoverable]**
70.1/75.6/82.9/91.8/95.0 vs 62/88/96. Resolvable in ten minutes with the two PDFs open. **Top verification priority.**

**4. GrantStation methodology is weak and must be disclosed wherever cited. [KNOWN]**
Per GrantStation's own methodology page: SurveyMonkey, **self-selected nonrandom sample of organizations affiliated with GrantStation and its partners, explicitly "not scientifically conducted."** GrantStation sells grant-database subscriptions — a direct commercial interest in the finding that more applications produce more awards. **Every GrantStation figure in this document carries that flag.**

**5. Sample-size attribution for GrantStation is unresolved. [MY ACCESS FAILURE]**
"Nearly 1,258 organizations" was returned as the basis for **both** the 2025 and the 2026 report — and "nearly 1,258" is itself incoherent phrasing for a precise integer. This is very likely boilerplate reuse on GrantStation's site or summarizer error. The Government Update Report's n=1,056 (Jan–Jul 2025) appears more reliably attributed. **Do not cite 1,258 for either year without verification.**

**6. No GPA member survey, no grant-professional salary data. [MY ACCESS FAILURE + budget exhaustion]**
Consequently **no cost-per-application figure was computed.** Deliberate omission, not oversight.

**7. No measured time-use study of nonprofit proposal preparation exists. [STRUCTURAL]**
Every nonprofit hours figure in circulation is a consultancy rule of thumb. The one rigorous study (von Hippel 2015, 116 PI hours) is academic-sector. **A defensible nonprofit hours-per-application number would require original time-diary research. It has not been done.**

**8. Rejection economics: essentially nothing exists.** See that section.

**9. Restricted vs. unrestricted foundation share not quantified.** I have CEP's 42%-increased-unrestricted but **no baseline** for what share of foundation dollars are restricted vs. unrestricted, and no comparison to the restriction profile of federal grants. **The qualitative mismatch argument is therefore asserted with only partial numbers.**

**10. Average foundation grant size vs. average federal grant size: NO DATA FOUND.** This would sharpen the scale argument considerably (Candid's grants data fact sheet likely holds the foundation side).

**11. PEAK Grantmaking practices surveys, GEO research, Council on Foundations statements: NOT RETRIEVED.** All appeared in results; none were reachable. The GEO piece "How Foundations Can Support Nonprofit Partners Now" and PEAK's Project Streamline archive are the specific targets.

**12. Chronicle of Philanthropy and Inside Philanthropy: NOT RETRIEVED.** `philanthropy.com` blocked. Two relevant headlines identified but unread: "In a Time of Nonprofit Defunding, Will Foundations Put More Money on the Line?" and "Foundation Coffers Are Full as Pressure Mounts to Increase Giving."

**13. Search-summarizer error was observed directly and should temper trust in everything here.** In one result the summarizer reasoned that because "eight out of ten grantmakers surveyed" had streamlined their practices, the study "surveyed 10 grantmakers." That is a fabricated inference from an idiom. **The layer between me and the primary sources demonstrably invents facts. This is the strongest argument for re-running with fetch access.**

---

## Source log

**Legend — Retrieval:** all entries are **snippet-only**; no document in this workstream was successfully fetched. **Every WebFetch attempt returned HTTP 403 (egress policy).**

### Tier 1 — high credibility, primary originator, worth the re-fetch

| Source | URL | Type | Credibility | Status |
|---|---|---|---|---|
| CEP, *A Sector in Crisis* (Jan 2026) | `cep.org/wp-content/uploads/2026/01/CEP_A_Sector_in_Crisis_FNL.pdf` | Primary | High. Aug–Sep 2025; 408 nonprofits surveyed/46% RR; 227 foundations/30% RR; 27+31 interviews Sep 2025. Representative sample of orgs funded by ≥$5M/yr foundations. | **Blocked** |
| CEP, *State of Nonprofits 2026* (May 2026) | `cep.org/wp-content/uploads/2026/05/CEP_State_of_Nonprofits_2026_FNL.pdf` | Primary | High. Feb 2026; 887 surveyed, 380 responses, 43% RR. | **Blocked** |
| CEP, *Mounting Pressure* (Oct 2025) | `cep.org/wp-content/uploads/2025/10/Mounting_Pressure_FINAL.pdf` | Primary | High. >400 nonprofit + >200 foundation leaders, Aug–Sep 2025. | **Blocked** |
| CEP Current Context Survey instrument (foundations) | `cep.org/wp-content/uploads/2026/01/CEP_Current-Context-Survey-2025_Foundations_final.pdf` | Primary | **The actual questionnaire — lets you check exact question wording behind the 87%.** | **Blocked** |
| Urban Institute, *How Government Funding Disruptions Affected Nonprofits in Early 2025* | `urban.org/research/publication/how-government-funding-disruptions-affected-nonprofits-early-2025` | Primary | **Highest in set.** n=2,737, nationally representative, fielded Apr–Jun 2025. | **Blocked** |
| Urban Institute, *What Is the Financial Risk of Nonprofits Losing Government Grants?* | `urban.org/research/publication/what-financial-risk-nonprofits-losing-government-grants` | Primary | High | **Blocked** |
| Urban Institute, Government Grants and Contracts data tables (2023 data) | `urban.org/sites/default/files/2025-02/Government%20Grants%20and%20Contracts%20for%20Nonprofits%20in%202023_Data%20Tables%20from%20Nonprofit%20Trends%20and%20Study_0.pdf` | Primary | High — **source for the $240B/$294B/$304B series** | **Blocked** |
| Candid, "How reliant are nonprofits on government grants?" | `candid.org/blogs/how-many-nonprofits-rely-on-government-grants-data/` | Primary (data owner) | High — **source of $303B / $107B / 282%** | **Blocked** |
| Candid, "How long can nonprofits survive without government grants?" | `candid.org/blogs/how-long-nonprofits-cash-runway-can-survive-without-government-grants/` | Primary | High | **Blocked** |
| Candid grants data fact sheet | `candid.org/about/our-data/grants-data-fact-sheet/` | Primary | High — likely holds average foundation grant size | **Blocked** |
| von Hippel & von Hippel (2015), PLOS ONE 10(3):e0118494 | `journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0118494` / `arxiv.org/abs/1503.04201` / PMC4349454 | Primary, peer-reviewed | High for its own field; **wrong sector for direct use** | **Blocked** |

### Tier 2 — primary but methodologically weak / vendor-conflicted

| Source | URL | Credibility |
|---|---|---|
| GrantStation, *2025 State of Grantseeking Report* + Key Findings | `grantstation.com/sites/default/files/imageLibrary/SoG/2025/...` | **VENDOR — sells grant databases.** Self-selected, nonrandom, SurveyMonkey, self-described as not scientifically conducted. Blocked. |
| GrantStation, *2025 State of Grantseeking Government Update Report* (n=1,056, Jan–Jul 2025) | same path | As above. **Most on-window GrantStation product.** Blocked. |
| GrantStation, *2026 State of Grantseeking Report* | `grantstation.com/public-resources/pathfinder/state-of-grantseeking-report-2026` | As above; free download claimed. Blocked. |
| GrantStation methodology page | `grantstation.com/public-resources/sog-methodology` | **The disclosure of nonrandom self-selection comes from here.** Blocked. |
| George Family Foundation, How to Apply | `georgefamilyfoundation.org/how-to-apply` | Foundation's own guidance — 4%/1% LOI funnel. Undated. Blocked; verification search refused. |
| New York Foundation, Apply | `nyf.org/apply` | Foundation's own guidance — "hundreds of requests," ~5 new grants/cycle. |
| PEAK Grantmaking, *Drowning in Paperwork* (2008) | `peakgrantmaking.org/wp-content/uploads/Drowning-In-Paperwork-Report.pdf` | Canonical but **~18 years old.** Blocked. |

### Tier 3 — secondary reporting, used for individual-foundation cases

| Source | URL | Note |
|---|---|---|
| 83 Degrees Media — Community Foundation Tampa Bay | `83degreesmedia.com/community-foundation-tampa-bay-grants-support-record-number-of-nonprofits/` | Local trade press; **source of 426 apps / +17% / 88 programs / $2.5M** |
| Hudson Valley 360 / Daily Gazette — Ackerman Foundation | `dailygazette.com/hv360/hv360/ackerman-foundation-awards-100k-to-43-community-nonprofits/...` | Local press; **source of +50% applications / <40% of requests met** |
| NonProfit PRO, "Foundations Stepped Up — But Nonprofit Gaps Remain" | `nonprofitpro.com/article/nonprofits-say-foundation-funding-didnt-meet-expectations-in-2025-new-data-shows/` | Secondary on CEP |
| NonProfit PRO, "State of Nonprofits 2026: 3 Dire Realities" | `nonprofitpro.com/article/state-of-nonprofits-2026-3-dire-realities-facing-the-sector-right-now/` | Secondary on CEP |
| Chronicle of Philanthropy (2 articles, identified not read) | `philanthropy.com/news/in-a-time-of-nonprofit-defunding-will-foundations-put-more-money-on-the-line/`; `philanthropy.com/news/foundation-coffers-are-full-as-pressure-mounts-to-increase-giving/` | **Blocked** |
| Grants Plus, "Grantseeking Trends in Real Time" | `grantsplus.com/insights/blog/uncategorized/grantseeking-trends-in-real-time/` | Consultancy; **source of the 60%-relationship claim and the 89%/51%/43%/40% funder-source split** |
| The Charity CFO, "State of Grant Seeking in 2026" | `thecharitycfo.com/grant-seeking-2026-nonprofit-strategy/` | Practitioner commentary; **AI-volume hypothesis** |
| Let's Hear It podcast — Elisha Smith Arrillaga (CEP) | `letshearitcast.com/elisha/` | **Best identified quote source; not retrieved** |
| GEO, "How Foundations Can Support Nonprofit Partners Now" | `geofunders.org/news/how-foundations-can-support-nonprofit-partners-now/` | Not retrieved |
| National Council of Nonprofits press release | `councilofnonprofits.org/pressreleases/new-study-highlights-impact-trump-administration-actions-nonprofits` | **Blocked** |
| Exponent Philanthropy, "Why Your Net Grant Matters" | `exponentphilanthropy.org/blog/why-your-net-grant-matters/` | Source of the net-grant framing and $10K→$9K illustration |

### Tier 4 — retrieved but FLAGGED FOR EXCLUSION

| Source | Reason |
|---|---|
| `grantcycle.com/article/calculating-the-true-cost-of-grants` | Sells grant-management software; "20% of grant funding" claim is a direct sales argument; **the "27.45 hours" Project Streamline attribution could not be verified anywhere and should be treated as unsound** |
| `opengrants.io` (multiple pages) | Sells grant-seeking services; the "3.5x spike at one major regional funder" claim names no funder and no date |
| `grants.com` "Top Community Grants With the Highest Success Rates in 2026" | Content farm; the "30–50% success rate" attribution to the 2026 SoG report is unverifiable |
| `instrumentl.com/blog/grant-statistics-and-trends` | Vendor aggregator; **secondary compilation — never cite it in place of the originating report** |
| Submittable, "34 Grant Statistics" | **2020 vintage**, outside window |
| `professionalgrantwriter.org`, `fundingforgood.org`, `grantsights.com`, `fundrobin.com`, `grantedai.com`, `recoverymovementconsult.com` | Vendor/SEO content; useful only as pointers to originators |

---

## Recommended next actions

1. **Restore fetch access and re-run.** Everything above is a verified-lead list, not a finished evidence base. The two highest-value fetches are the **GrantStation 2025 and 2026 report PDFs** (resolves the win-rate contradiction and the n=1,258 problem) and **CEP's *A Sector in Crisis*** (resolves the 87% question and supplies the missing 6–10 quotes from 58 leader interviews).
2. **Ask a grants-management vendor directly** for year-over-year applications-received counts. This is the only path to a real application-volume series.
3. **Do not publish any cost-per-application figure** until a grant-professional wage source is obtained AND the hours estimate has a methodology behind it. Currently neither exists.
4. **Lead with the substitution-gap math.** It is the most defensible finding, it is robust to the $240B–$304B definitional dispute, and it survives the disconfirming evidence intact.
