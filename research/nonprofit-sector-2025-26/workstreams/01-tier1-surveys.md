# Workstream 1 — Tier-1 Sector Survey Extraction
## Needs, funding disruption, capacity crisis, compliance pressure

**Compiled:** 2026-07-30
**Core research window:** mid-2025 → mid-2026
**Searches/fetches executed:** 46 successful WebSearch queries; 9 WebFetch attempts (all failed); 12 curl attempts (all failed)

---

## ⚠️ CRITICAL METHODOLOGICAL CAVEAT — READ BEFORE USING ANY NUMBER BELOW

**No primary document in this workstream was successfully retrieved and read.** The research environment's egress policy denied every outbound HTTPS connection at the gateway (HTTP 403 on CONNECT). This was verified against the proxy's own failure log:

```
connect_rejected cep.org:443            | gateway answered 403 to CONNECT (policy denial)
connect_rejected www.councilofnonprofits.org:443
connect_rejected www.nationalacademies.org:443
connect_rejected nff.org:443
connect_rejected independentsector.org:443
connect_rejected urban.org:443
connect_rejected candid.org:443
connect_rejected givingusa.org:443
connect_rejected afpglobal.org:443
connect_rejected www.philanthropy.com:443
connect_rejected example.com:443        ← even a control host is blocked
```

The block is total, not site-specific: `example.com` fails identically. Per `/root/.ccr/README.md`, organization policy denials must be reported, not routed around. **This is an environment limitation, not a finding about the sources.**

**Consequence for evidence quality:** Every figure below was retrieved from **WebSearch result summaries** — i.e. a search backend's synthesis of page snippets. This is one step removed from the primary PDF. It means:

1. **Page/section citations are impossible.** The brief was explicit that stats should carry page references. None can be supplied.
2. **Attribution drift is a live risk.** Search summaries blend multiple result pages. Where a number's source-of-record is ambiguous, it is flagged `[ATTRIBUTION UNCERTAIN]`.
3. **Sample sizes and field dates below are as reported in snippets** and were not read off a methodology appendix.
4. **Nothing here should be published without re-verification against the primary PDF** once network access permits. A re-verification checklist is at the end.

I have applied the anti-fabrication rule strictly: nothing below is reconstructed from memory or inferred. Where I could not retrieve something, it appears in `## Data gaps` as an explicit no-data entry.

**Retrieval-grade legend** (orthogonal to evidence grade):
- `[R1]` — figure appeared verbatim and unambiguously in a search summary of the primary publisher's own page/PDF
- `[R2]` — figure appeared in a search summary, but sourced to secondary coverage of the primary
- `[R3]` — figure appeared in a search summary with ambiguous or blended attribution

---

## Key findings

- **Existence of both flagship CEP documents is CONFIRMED.** "A Sector in Crisis" (published 2026-01-28) and "State of Nonprofits 2026: What Funders Need to Know" (published ~2026-05-12, 4th annual edition) both exist, with live PDF URLs on cep.org indexed by search. Neither could be opened. `[R1]`

- **Burnout is the single steepest-moving indicator in the sector.** CEO/ED self-reported burnout as "very much" a concern **jumped from 29% (2025) → 46% (2026)**, a 17-point year-over-year rise — the largest single-year delta found anywhere in this workstream. ~89% report *some* level of concern. `[R1]` [Reported]

- **Funding loss is broad but shallow-tailed by source.** In CEP's Aug–Sep 2025 fielding, **69% of nonprofits lost funding from at least one source**; disaggregated: federal 36%, state/local 34%, foundation >40%. Foundation loss exceeding federal loss is the counterintuitive headline. `[R1]` [Reported]

- **Foundation funding — not federal — is the most-cited pain point among foundation-funded nonprofits.** ~60% of CEOs say foundation grants got *harder* to secure since Jan 2025, vs **48%** reporting federal difficulty. Among orgs running a deficit, **~60% cite lower-than-expected foundation giving** as a top contributor. `[R2]` [Reported]

- **Deficits are at a multi-year high across two independent surveys.** CEP: **39% ran a deficit in FY2025, up from 22% in 2022**. NFF: **36% ended 2024 in deficit — highest in 10 years** of its survey. Independent Sector reports 36%. Convergence across different frames strengthens this. `[R1]` [Reported]

- **The demand/capacity scissors is the core structural finding.** Independent Sector: **68% expect demand to rise in 2026, but only 31% are expanding** the number of people served. CEP 2026: 73% report increased demand. NFF: 85% expected demand increase. `[R1]` [Reported]

- **Documented (not self-reported) job loss:** Challenger, Gray & Christmas counted **28,696 nonprofit job cuts in 2025** vs 5,640 in the first 11 months of 2024. `[R2]` [Documented] — but see the apples-to-oranges warning in `## Capacity crisis`.

- **Government funding disruption hit ~1 in 3 nonprofits in H1 2025** (Urban Institute, fielded Apr–Jun 2025): 21% lost funding, 27% delay/pause/freeze, 6% stop-work order. This is the best-designed sampling frame in the set. `[R1]` [Reported]

- **The strongest disconfirming fact: total giving hit an all-time record.** Giving USA 2026 puts 2025 US charitable giving at **$617.20B, +5.7% nominal / +3.0% real — above $600B for the first time ever**. The sector's *revenue* is growing while its *operators* report crisis. Reconciling these is the central analytic task. `[R1]` [Documented]

- **Compliance pressure is real and forward-loaded, but evidence of it as a *felt* need is thin.** Regulatory change is documented (Aug 2025 EO → OMB 2 CFR overhaul, target effective **Oct 1, 2026**). GAO found **36% of 3,680 single-audit findings involved incomplete subaward reporting**. But no survey was found that quantifies compliance burden as a ranked leader concern. This is a genuine gap.

---

## Quantitative table

Sponsor-bias flags: **V** = vendor/commercial sponsor (directionally useful, biased toward optimism about their product category and toward respondents who are their clients); **A** = advocacy/membership organization with a stake in the finding; **N** = neutral/academic; **F** = funder-sector research intermediary.

### Funding disruption

| Metric | Value | Source | n | Field dates | Sponsor flag | Evidence grade | Retrieval |
|---|---|---|---|---|---|---|---|
| Lost funding from ≥1 source in 2025 | 69% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F | [Reported] | R1 |
| Reduced **federal** funding since Jan 2025 | 36% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F | [Reported] | R1 |
| Reduced **state/local** government funding | 34% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F | [Reported] | R1 |
| Reduced **foundation** funding | >40% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F | [Reported] | R1 |
| Any government funding disruption | ~33% (1 in 3) | Urban Institute | not captured | Apr–Jun 2025 | N | [Reported] | R1 |
| — lost a grant/contract | 21% | Urban Institute | not captured | Apr–Jun 2025 | N | [Reported] | R1 |
| — delay, pause or freeze | 27% | Urban Institute | not captured | Apr–Jun 2025 | N | [Reported] | R1 |
| — stop-work order | 6% | Urban Institute | not captured | Apr–Jun 2025 | N | [Reported] | R1 |
| Harder to secure foundation grants since Jan 2025 | ~60% | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F | [Reported] | R2 |
| Harder to secure federal funding | 48% | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F | [Reported] | R2 |
| Expect further cuts to their funding | 84% | NFF 2025 Survey | 2,206 | 2025 (exact dates not captured) | A | [Reported] | R2 |
| Negative impact from govt policy changes | 47% | CCS *Philanthropy Pulse 2026* | 618 | Q4 2025 | **V** | [Reported] | R1 |
| Expect declines in federal/national grants | 45% | CCS *Philanthropy Pulse 2026* | 618 | Q4 2025 | **V** | [Reported] | R1 |
| Expect declines in state/regional grants | 30% | CCS *Philanthropy Pulse 2026* | 618 | Q4 2025 | **V** | [Reported] | R1 |
| Affected by federal policy changes | 96% | BDO *Nonprofit Standards* 2025 | not captured | not captured | **V** | [Reported] | R2 |
| Lost public funding in 2025 (Charlotte NC metro) | 30% | Charlotte Urban Institute (UNC Charlotte) | not captured | pub. Mar 2026 | N | [Reported] | R3 |

### Financial distress / reserves / closure risk

| Metric | Value | Source | n | Field dates | Sponsor flag | Evidence grade | Retrieval |
|---|---|---|---|---|---|---|---|
| Concerned about financial stability | 71% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F | [Reported] | R1 |
| Concerned about financial stability | 66% (≈"two-thirds") | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F | [Reported] | R1 |
| Ran a deficit in FY2025 | 39% (vs 22% in 2022) | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F | [Reported] | R1 |
| Ended 2024 with operating deficit | 36% — highest in 10 yrs of NFF data | NFF 2025 Survey | 2,206 | 2025 | A | [Reported] | R1 |
| Repeat respondents at a deficit in 2024 | 37% (vs 13% in 2021) | NFF 2025 Survey | subset of 2,206 | 2025 | A | [Reported] | R2 |
| Ended most recent FY with operating deficit | 36% | Independent Sector *Health of the Sector* | not captured | pub. Dec 2025 | A | [Reported] | R1 |
| Repeat respondents with ≥6 months cash on hand | fell 36% → 26% | NFF 2025 Survey | subset of 2,206 | 2025 | A | [Reported] | R2 |
| Hold ≤3 months cash on hand | 52% (18% hold ≤1 month) | attributed to CEP 2026 | 380 | Feb 2026 | F | [Reported] | **R3 — see warning** |
| BIPOC-led NY nonprofits with ≤3 months cash | 62% (vs 41% white-led) | NFF (NY cut) | subset | 2025 | A | [Reported] | R2 |
| Struggled to raise funds covering all costs | 81% | Independent Sector / NFF | not captured | 2025 | A | [Reported] | R1 |
| Difficulty raising funds = top financial challenge | 75% | NFF 2025 Survey | 2,206 | 2025 | A | [Reported] | R1 |
| Of deficit orgs: cite low foundation giving as top cause | ~60% | Candid, citing CEP | 380 (subset) | Feb 2026 | F | [Reported] | R2 |
| Reported negative impacts on financial health/ops since Jan 2025 | 86% | attributed to CEP 2026 | 380 | Feb 2026 | F | [Reported] | **R3** |
| Have a line of credit / of those, borrowed against it in 2025 | 27% / **83%** | NJ Center for Nonprofits *Trends & Outlook 2026* | not captured | late Jan–mid Feb 2026 | A | [Reported] | R1 |

### Demand and service reduction

| Metric | Value | Source | n | Field dates | Sponsor flag | Evidence grade | Retrieval |
|---|---|---|---|---|---|---|---|
| Increased demand for services in 2025 | 65% (higher than 2020) | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F | [Reported] | R1 |
| Increased demand for services | 73% ("almost three-quarters") | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F | [Reported] | R1 |
| Expect demand to increase in 2026 | 68% | Independent Sector | not captured | pub. Dec 2025 | A | [Reported] | R1 |
| …but expanding number of people served | only **31%** | Independent Sector | not captured | pub. Dec 2025 | A | [Reported] | R1 |
| Expected service demand to increase in 2025 | 85% | NFF 2025 Survey | 2,206 | 2025 | A | [Reported] | R1 |
| Anticipated demand increase in 2025 | 75% | Urban Institute (2024 NSNTI) | 2,975 open-ended | 2024 | N | [Reported] — BASELINE | R1 |
| Experiencing increased demand | 78% | BDO 2025 | not captured | not captured | **V** | [Reported] | R2 |
| Reduced the services they provide | ~30% ("nearly a third") | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F | [Reported] | R1 |
| Have already reduced services | 26% | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F | [Reported] | R3 |
| Expect expenses AND demand to rise in 2026 | 75% | NJ Center for Nonprofits | not captured | Jan–Feb 2026 | A | [Reported] | R1 |
| …but anticipate funding to increase | only **39%** | NJ Center for Nonprofits | not captured | Jan–Feb 2026 | A | [Reported] | R1 |

### Capacity / workforce

| Metric | Value | Source | n | Field dates | Sponsor flag | Evidence grade | Retrieval |
|---|---|---|---|---|---|---|---|
| **Burnout "very much" a concern (CEO/ED, self)** | **46% (2026) vs 29% (2025)** | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F | [Reported] | R1 |
| Any level of concern about own burnout | ~89% ("nearly 90%") | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F | [Reported] | R1 |
| Burnout significantly affecting staff | 25% (2026) vs 17% (2025) | CEP, *State of Nonprofits 2026* | 380 | Feb 2026 | F | [Reported] | R2 |
| Reduced staff size | 30% | CEP, *A Sector in Crisis* | 408 | Aug–Sep 2025 | F | [Reported] | R1 |
| Of orgs hit by funding cuts: had reduced staff | 29% | Urban Institute | not captured | Apr–Jun 2025 | N | [Reported] | R1 |
| Of orgs hit by funding cuts: serving fewer people | 21% | Urban Institute | not captured | Apr–Jun 2025 | N | [Reported] | R1 |
| **Nonprofit jobs cut, calendar 2025** | **28,696** (vs 5,640 in first 11 mo. of 2024) | Challenger, Gray & Christmas | census, not survey | CY2025 | N (outplacement firm) | [Documented] | R2 |
| Orgs where ≥21% of staff positions are vacant | 11% | Independent Sector | not captured | pub. Dec 2025 | A | [Reported] | R1 |
| **Report staffing shortages (employers)** | **47%** | NJ Center for Nonprofits | not captured | Jan–Feb 2026 | A | [Reported] | R1 |
| **Average vacancy rate (NJ)** | **18%** | NJ Center for Nonprofits | not captured | Jan–Feb 2026 | A | [Reported] | R1 |
| Nonprofit workers in financially hardshipped households | 1 in 5 | Independent Sector | not captured | pub. Dec 2025 | A | [Reported] | R1 |
| Provide health insurance (all orgs / orgs <$250K) | 67% / **12%** | Independent Sector | not captured | pub. Dec 2025 | A | [Reported] | R1 |
| Leaders concerned about workforce (open-ended) | ~20%; of those ~40% staffing | Urban Institute (2024 NSNTI) | 2,975 | 2024 | N | [Reported] — BASELINE | R1 |

### Giving environment (context + disconfirmation)

| Metric | Value | Source | n | Field dates | Sponsor flag | Evidence grade | Retrieval |
|---|---|---|---|---|---|---|---|
| **Total US charitable giving 2025** | **$617.20B, +5.7% nominal / +3.0% real** | Giving USA 2026 (Lilly Family School) | national estimate | CY2025 | N/A | [Documented] | R1 |
| — Individuals | $394.2B, +4.1% / +1.4% real (64% of total) | Giving USA 2026 | — | CY2025 | N/A | [Documented] | R1 |
| — Foundations | $117.15B, +5.7% / +3.0% real (19%) | Giving USA 2026 | — | CY2025 | N/A | [Documented] | R1 |
| — Bequests | $62.19B, **+19.7% / +16.6% real** (10%) | Giving USA 2026 | — | CY2025 | N/A | [Documented] | R1 |
| — Corporations | $43.67B, +3.1% / ~flat real (7%) | Giving USA 2026 | — | CY2025 | N/A | [Documented] | R1 |
| Donor counts, CY2025 | **−3.6% (±0.5%)** — declines since 2021 | FEP (AFP Fdn / GivingTuesday) | large transactional panel | CY2025 | A | [Documented] | R1 |
| Overall donor retention, CY2025 | 43.3% (from 43.1%) | FEP | same | CY2025 | A | [Documented] | R1 |
| Donor counts, Q1 2026 | −0.8% (loss decelerating) | FEP | same | Q1 2026 | A | [Documented] | R1 |
| YTD quarterly retention Q1 2026 | ~18% | FEP | same | Q1 2026 | A | [Documented] | R1 |
| Online revenue growth 2025 | **+15%** | M+R Benchmarks 2026 | not captured | CY2025 | **V** | [Documented] | R1 |
| Email revenue growth 2025 | +16%; $54/1,000 emails (+4%) | M+R Benchmarks 2026 | not captured | CY2025 | **V** | [Documented] | R1 |
| DAF revenue growth (to nonprofits) | +44% | M+R Benchmarks 2026 | not captured | CY2025 | **V** | [Documented] | R1 |
| Monthly / one-time / mobile / direct mail | +12% / +17% / +48% / +9% | M+R Benchmarks 2026 | not captured | CY2025 | **V** | [Documented] | R1 |
| Foundations expecting to increase giving in 2026 | 44.3% up / 46.9% same / 8.8% down; median **+5.8%** (+3.1% real) | Candid foundation giving forecast | not captured | ~late 2025/early 2026 | F | [Reported] | R1 |
| Revenue gains in most recent FY | **86%**; 90% expect continued growth | BDO 2025 | not captured | not captured | **V** | [Reported] | R2 |
| Revenue gains in FY2025 | ~two-thirds | CCS *Philanthropy Pulse 2026* | 618 | Q4 2025 | **V** | [Reported] | R1 |
| DAF assets / contributions / grants | $326.45B (+27.5%) / $89.64B (+37.3%) / $64.89B | DAF Research Collaborative *Annual DAF Report 2025* | — | most recent yr | F | [Documented] | R2 |
| NPT donor-recommended grants FY2025 | $6.61B, **+20%** | National Philanthropic Trust | — | FY2025 | **V** | [Documented] | R1 |

### Trust and public standing

| Metric | Value | Source | n | Field dates | Sponsor flag | Evidence grade | Retrieval |
|---|---|---|---|---|---|---|---|
| Americans with high trust in nonprofits | **56%** (2026), vs 57% (2025) — stable | Independent Sector *Trust in Nonprofits & Philanthropy 2026* (7th yr), fielded by Edelman DxI | **3,000** US adults, MoE ±2% | 2026 (focus groups over 3 days in April) | A | [Documented] | R1 |
| High trust in philanthropic organizations | 29%, **down 4 pts** from 2025 | Independent Sector 2026 | 3,000 | 2026 | A | [Documented] | R1 |
| Trust gap, nonprofits vs philanthropy | 27 points | Independent Sector 2026 | 3,000 | 2026 | A | [Documented] | R1 |
| Agree nonprofits should disclose AI use | 76% | Independent Sector 2026 | 3,000 | 2026 | A | [Documented] | R1 |
| High trust in military / small business (comparators, 2025) | 45% / 42% | Independent Sector 2025 | not captured | 2025 | A | [Documented] — BASELINE | R2 |

---

## Ranked needs

Two rankings are given because the brief asked for both. **Frequency rank** = how many independent Tier-1 surveys surface the pressure. **Intensity rank** = severity of the language/consequence attached, distinguishing existential threat from directional concern.

### By frequency across surveys

**1. Funding shortfall / revenue instability — appears in 8 of 8 surveys reviewed**
Present in CEP (both editions), NFF, Independent Sector, Urban, BDO, CCS, NJ Center. Strongest single numbers: 69% lost funding from ≥1 source (CEP); 81% can't raise funds covering full costs (IS/NFF); 75% call fundraising difficulty their top financial challenge (NFF). Evidence: [Reported], convergent across frames with different sampling.

**2. Rising demand outpacing capacity — 7 of 8**
CEP 2025 (65%), CEP 2026 (73%), NFF (85% expected), IS (68% expect / only 31% expanding), Urban baseline (75%), BDO (78%), NJ (75%). The IS 68%-vs-31% pair is the cleanest quantification of the gap. Evidence: [Reported], highly convergent.

**3. Staffing shortage, burnout and retention — 6 of 8**
CEP 2026 (46% "very much"; ~89% any), IS (11% of orgs ≥21% vacant), NJ (47% shortages, 18% avg vacancy), Urban baseline (~20% name workforce unprompted), NFF, CCS ("staffing strain"). Evidence: [Reported].

**4. Deficits and reserve depletion — 4 of 8**
CEP (39% deficit), NFF (36%, 10-year high; ≥6mo cash 36%→26%), IS (36%). Evidence: [Reported], convergent on ~36–39%.

**5. Government contracting friction (payment delays, contract terms) — 3 of 8**
NFF (NYC delays), Urban (27% delay/pause/freeze; 6% stop-work), NYC Comptroller audits. Evidence: [Reported] + [Documented] on the audit launches.

**6. Compliance / audit / reporting burden — 1 of 8 surfaces it, and only obliquely**
BDO's 96%-affected-by-federal-policy-changes is the closest thing to a quantified felt need, and it is a vendor survey measuring "affected," not "burdened." See `## Compliance pressure` and `## Data gaps`.

### By intensity (severity of stated consequence)

**1. Existential / closure risk — HIGHEST INTENSITY, WEAKEST QUANTIFICATION**
CEP's framing escalated from "significant challenges" (2025 report) to "existential threats" (2026). CEP's research VP states nonprofits are "pausing operations, closing, or merging." A nonprofit leader quoted directly: *"The stakes are that we might not make it as an organization."* **But no survey found puts a percentage on "we may close."** This is the single most important gap in the workstream — the most severe claim is the least measured. Evidence: [Anecdote] + [Announced], NOT [Reported].

**2. Service withdrawal — measured, severe, concrete**
~30% reduced services (CEP Aug–Sep 2025); 26% (CEP Feb 2026); 21% of funding-cut-affected orgs already serving fewer people (Urban, by Jun 2025). Distinct from anxiety: this is a completed action. Evidence: [Reported].

**3. Layoffs — the only pressure with hard external corroboration**
30% reduced staff size (CEP, self-reported) is corroborated by Challenger's 28,696 counted job cuts. Self-report and external count point the same direction. Evidence: [Reported] + [Documented].

**4. Reserve drawdown — measured, and it is a one-time buffer being spent**
NFF's ≥6-months-cash cohort shrinking 36%→26% is a *depletion* signal, materially worse than a static "low reserves" statistic. The NJ finding that **83% of line-of-credit holders drew on it in 2025** is the sharpest liquidity-stress indicator located. Evidence: [Reported].

**5. Burnout — highest velocity, but a leading indicator not a completed loss**
46% vs 29% is the steepest delta in the dataset. Intensity-ranked below layoffs because it predicts rather than records organizational damage. Evidence: [Reported].

**6. Fundraising difficulty — near-universal, therefore low discriminating intensity**
75–81% report it, but it has been high across all prior editions. High frequency, low *change*. Treat as chronic baseline, not acute crisis signal.

### Triangulation of the two conflicting "financial stability concern" numbers

CEP reports **71%** (Aug–Sep 2025) and **66%** (Feb 2026). These are *not* contradictory and should not be averaged:
- Different fieldings, different instruments (*A Sector in Crisis* vs *State of Nonprofits*), different n (408 vs 380).
- The 5-point decline is within plausible range for a genuine slight easing, or for instrument wording differences that could not be checked because the PDFs were unreadable.
- **Do not report a trend from this pair.** Report the range: 66–71% of foundation-funded nonprofit CEOs concerned about financial stability, mid-2025 to early-2026.

---

## Funding disruption

### By source, magnitude, and who is measuring

**Federal.** CEP: 36% saw reduced federal funding since Jan 2025. Urban (better frame): 21% lost a government grant/contract, 27% experienced delay/pause/freeze, 6% received a stop-work order, by Apr–Jun 2025. CCS: 45% *expect* federal grant declines. These are three different constructs — realized loss, disruption-of-any-kind, and expectation — and should never be presented as one series.

**State/local.** CEP: 34% reduced. CCS: 30% expect state/regional declines. Urban's ~1-in-3 government-disruption figure is deliberately federal+state+local combined; it cannot be decomposed from what was retrievable.

**Foundation — the surprise.** More than 40% saw reduced foundation funding, and ~60% say foundation grants got *harder to secure* — a **higher** share than report federal difficulty (48%). Among deficit-running organizations, ~60% name lower-than-expected foundation giving as a top contributor.

This directly contradicts the foundation sector's self-report in the same CEP research: 64% of foundations said they provided or increased emergency/rapid-response grants and 45% provided or increased multiyear grants. **Both cannot be straightforwardly true of the same relationships.** Candid's forecast adds a third data point: 44.3% of foundations expect to *increase* 2026 giving, median +5.8%.

Most likely reconciliations, in rough order of plausibility — **none of these is established, all are hypotheses for Workstream follow-up**:
1. *Concentration.* Foundations increased total dollars while concentrating them on fewer grantees; the median grantee experiences decline even as the aggregate rises.
2. *Composition.* Emergency/rapid-response grants are small and short; they substitute for, rather than add to, general operating support — so recipients feel a net loss.
3. *Denominator drift.* CEP's nonprofit panel is restricted to orgs already receiving $5M+ foundation money, so it over-indexes on organizations most exposed to foundation portfolio reshuffling.
4. *Base rate.* 42% of foundation leaders CEP interviewed were themselves dissatisfied with the sector's overall response — the funders partly agree with the grantees.

**Individual donors.** The most fragmented picture. Giving USA: individual giving *rose* to $394.2B (+1.4% real). FEP: donor *counts* fell 3.6% in 2025, extending declines since 2021. M+R: online revenue +15%. The synthesis — **more money from fewer people** — is the most robust finding in this section and is corroborated three ways. Note the FEP retention figures cited in different places (42.6%, 43.1%, 43.3%, and a separate ~18% YTD-quarterly measure) are **not** conflicting estimates of one quantity; the ~18% series is a year-to-date quarterly retention metric and the ~43% series is annual retention. FEP also changed methodology recently, which further breaks comparability. Do not mix them.

### Consequential actions taken

| Action | Share | Source |
|---|---|---|
| Reduced staff size | 30% | CEP Aug–Sep 2025 |
| Reduced services | ~30% (Aug–Sep 2025) / 26% (Feb 2026) | CEP |
| Serving fewer people (among funding-cut-affected) | 21% | Urban, by Jun 2025 |
| Reduced staff (among funding-cut-affected) | 29% | Urban, by Jun 2025 |
| Drew on line of credit (among LOC holders, NJ) | 83% | NJ Center 2026 |
| Initiated new partnerships / shared services | ~50% | CEP 2026 |
| Fear of closure | **NO NUMBER FOUND** | — |

Dipping into reserves and cutting programs/staff/benefits are described qualitatively in CEP's *A Sector in Crisis* as the main responses to financial-stability concern, but **the retrievable text gave no percentage for reserve drawdown specifically.**

---

## Capacity crisis

### Burnout — the headline

- 46% of nonprofit CEOs/EDs say their **own** burnout is "very much" a concern (2026), up from 29% (2025). `[R1]`
- ~89% report some level of concern about their own burnout.
- 25% say burnout is significantly affecting their staff, up from 17% in 2025.
- A widely-recirculated figure of "95% of nonprofit leaders concerned about staff burnout, nearly 50% finding it difficult to fill staff vacancies" is attributed to CEP by an intermediary blog. **It could not be traced to a CEP page in any search result and is NOT adopted here.** Listed in `## Data gaps`.

### Vacancy rates — best available

- **NJ Center for Nonprofits 2026 is the only source found that reports an actual average vacancy rate: 18%**, with 47% of employer-respondents reporting staffing shortages. Field dates late Jan–mid Feb 2026. Sample size not retrievable.
- Independent Sector reports the distribution's tail rather than the mean: **11% of organizations have ≥21% of staff positions vacant.**
- No national mean vacancy rate was found. See `## Data gaps`.

### Job losses — the one externally-counted number

Challenger, Gray & Christmas: **28,696 nonprofit job cuts in calendar 2025**, characterized as more than quadrupling from **5,640 during the first 11 months of 2024**. NPR rounded this to "29,000 nonprofit jobs cut last year."

**Warning — this comparison is not clean.** The retrievable phrasing compares full-year 2025 against an 11-month 2024 window. A "+409%" figure computed from those two numbers overstates the change by roughly one month of 2024 baseline. The direction (a large multi-fold increase) is well supported; **the precise multiple is not.** Grade the direction [Documented]; grade the "+409%" [UNVERIFIED].

Challenger data is also a *press-release census of announced cuts*, not a probability sample: it systematically undercounts small organizations that shed staff without announcement, and over-weights large employers. One secondary source noted healthcare-nonprofit cuts alone at 51 hospitals/systems could total 15,000–20,000 in H1 2025, implying either double-counting or that Challenger undercounts — that discrepancy is unresolved.

### Development-staff turnover — evidence quality is poor

Several figures circulate: ~19% nonprofit voluntary turnover vs ~12% all-industry; ~7 in 10 nonprofit employees planning a job search in 2025; 59% reporting more difficulty filling positions in 2024; 60% of leaders naming talent as a top-3 2026 challenge; ED tenure of 5–7 years; "development and finance teams experience elevated turnover."

**All of these surfaced only via content-marketing aggregators** (Mission Edge, cnpc.coach, FoundationList, TalentHR). None could be traced to a named primary instrument with an n and field dates. **Per the methodology rule these are DISCARDED, not reported.** They are recorded in `## Data gaps` so a later pass can chase the primaries (likely candidates: Nonprofit HR's Talent Management Practices Survey; the 2026 Nonprofit Salaries & Staffing Trends report from Careers In Nonprofits, which does exist as a PDF but was not retrievable).

### Hours available for fundraising vs. hours required

**NO DATA FOUND.** See `## Data gaps` — this was searched and returned nothing usable.

### Structural context

Nonprofits are ~9–10% of private-sector employment (~12.8M jobs, 2022 BLS research series; 66.3% of those in health care and social assistance). **BLS's nonprofit research series only runs through 2022**, so there is no authoritative federal employment count for the 2025–26 window. This is why the Challenger announcement-census is doing so much work in sector commentary — it is filling a hole in official statistics, and it is not designed for that job.

---

## Compliance pressure

Evidence here splits cleanly into *regulatory change* (well documented) and *felt burden on nonprofit leaders* (essentially unmeasured).

### Documented regulatory change — [Documented] / [Announced]

- **Executive Order, Aug 7, 2025** directing OMB to revise 2 CFR (Uniform Guidance) to expand transparency/accountability/oversight of federal awards and to ensure discretionary grants permit **termination for convenience**. [Documented]
- **Proposed OMB rule** would expand agencies' termination powers, add **political review before awards are issued**, and attach new conditions to funding. Comments due 45 days after Federal Register publication; **OMB targeting an effective date of October 1, 2026**. [Announced] — proposed, not final, as of this compilation.
- **2025 OMB Compliance Supplement** expanded monitoring expectations, requiring more granular documentation at every funding tier. [Documented]
- **GAO, March 2025:** analyzed **3,680 single audit findings from 2022–2024**; **36% involved incomplete subaward reporting**, and in nearly half of cases recipients lacked internal controls for basic subaward oversight. [Documented] — this is the strongest hard number in the section, and note it is *pre*-window baseline data (2022–24) describing capability, not 2025–26 enforcement.

### Clawback exposure — [Reported], weakly sourced

Practitioner and CPA-firm commentary holds that clawback risk is elevated and that as federal funds shift to state pass-through, audit pressure intensifies because states must ensure pass-through dollars aren't mismanaged. This is a coherent mechanism and is repeated across several professional-services sources. **It is not backed by any incidence statistic that could be retrieved** — no count of clawbacks, no dollar total, no share of organizations affected. Treat as [Anecdote]/professional judgment.

### Compliance as a *felt need* — the gap

BDO's **96% say they have been affected by federal policy changes** is the only quantified proximate measure found, and it is (a) vendor-sponsored, (b) measuring "affected," not "burdened by compliance," and (c) lacking a retrievable n or field dates.

Adjacent-but-not-substitutable: one commercial source claims nonprofit finance teams spend 15–20 hours/week on automatable administrative tasks. This comes from expense-management software marketing, has no visible methodology, and is **discarded** — it is a sales figure, not a research finding.

**Bottom line: compliance/audit burden does not appear as a ranked leader concern in any Tier-1 survey located.** Given the volume of regulatory change documented above, its absence from the survey instruments is itself a finding: either the instruments were fielded before the burden landed (most were fielded Aug 2025–Feb 2026, before the Oct 2026 target date), or leaders are subordinating it to funding and staffing pressures. Both readings are consistent with the data; neither is established.

---

## Disconfirming evidence

A full search cycle was spent seeking evidence against the "sector in crisis" narrative. It found more than expected, and the counter-case is genuinely strong on the revenue side.

### 1. Aggregate giving hit an all-time record

Giving USA 2026: **$617.20B in 2025, first time above $600B, +3.0% after inflation.** Every source category grew in nominal terms, and three of four grew in real terms. Bequests grew **+16.6% real**. If the sector were in undifferentiated financial crisis, this is not what the top line would look like. [Documented]

### 2. Most organizations report revenue *growth*, not decline

- **BDO: 86% reported revenue gains** in their most recent fiscal year; 90% expect continued growth; **69% plan to expand program areas** in the next 12 months. BDO's own summary language is that nonprofits are "financially stable and focused on expanding their programs." (Vendor-sponsored — flag — but the direction is corroborated below.)
- **CCS: roughly two-thirds** reported FY2025 revenue gains (n=618, Q4 2025). Also vendor-sponsored.
- Two independent vendor surveys agreeing on majority revenue growth is weak-but-real evidence. Both skew toward larger, better-resourced organizations that buy professional services — which is precisely the segment the bifurcation hypothesis predicts is doing fine.

### 3. Digital and DAF channels are growing fast

M+R Benchmarks 2026: online revenue +15%, email +16%, **mobile +48%, DAF +44%**, monthly +12%, direct mail +9% — "double-digit increases in nearly every sector." DAF Research Collaborative: DAF assets +27.5% to $326.45B, contributions +37.3% to $89.64B, grants $64.89B (more than all private foundations combined). NPT grants +20% to $6.61B in FY2025.

### 4. Foundations are forecasting increases, not cuts

Candid: **44.3% of foundations expect 2026 giving to increase, 46.9% flat, only 8.8% decrease**; median change **+5.8% nominal (+3.1% real)**. In CEP's own foundation survey, ~one-third increased 2025 payout beyond plan, 64% added or increased emergency/rapid-response grants, 45% added or increased multiyear grants.

### 5. Public trust has not collapsed

56% of Americans report high trust in nonprofits (2026) — statistically indistinguishable from 57% in 2025, and far above trust in government and corporations. If the sector were suffering a legitimacy crisis alongside a funding crisis, this number should be moving. It is not. (Trust in *philanthropy* did fall 4 points to 29% — a funder problem, not a nonprofit problem.)

### 6. Donor loss is decelerating

FEP: donor counts −3.6% for CY2025 but only **−0.8% in Q1 2026** — "donor loss may be flooring out." FEP separately reported the **strongest revenue growth in five years**.

### 7. Closure counts, where measurable, are not spiking

The only sub-sector with reliable closure tracking is higher education: **16 nonprofit institutions announced closures in 2025 — identical to 2024**, and up only modestly from 14 in 2023. Long-run context: ~0.3% annual closure rate 1996–2013, ~0.5% for 2014–2025. This is a slow secular trend, not a 2025 shock. If the crisis narrative predicted a closure wave, higher ed — the one place we can count — does not show one.

### 8. The bifurcation reading

Multiple analyses converge on the same structural claim: the sector is splitting rather than sinking. Larger, revenue-diversified organizations with infrastructure are absorbing the shock; small, single-source-dependent organizations face restructuring, consolidation, or closure. Urban's data supports concentration by field as well — losses were greatest in human services, higher education, food assistance, and youth services, not evenly distributed.

### How to weigh the counter-evidence honestly

The disconfirming evidence is strong on **aggregate revenue** and weak on **organizational condition**. Both sets of facts can hold simultaneously, and the most defensible synthesis is:

> Sector-wide dollars are at a record high and still growing in real terms, while the *distribution* of those dollars has concentrated — into larger organizations, into bequests and DAFs, and into fewer individual donors giving more. The organizations reporting crisis are disproportionately small-to-mid-sized, government-funded, and human-services-focused. "Sector in crisis" is accurate about a large and important *segment* and inaccurate as a statement about the sector's aggregate finances.

Two caveats against over-reading the counter-evidence:
- Giving USA's bequest surge (+16.6% real) is demographic and non-repeatable; stripping it out leaves a much flatter picture.
- BDO, CCS and M+R all sample organizations that buy professional fundraising/advisory/agency services — a selection effect pointing the same direction as their optimism.

---

## Verbatim quotes

**Attribution warning:** these were captured from search-result summaries, not from reading the source page. Quotes 5–7 in particular surfaced in a blended summary drawing on several publications at once; their source-of-record could not be pinned down and they must be re-verified before any use. Quotes are reproduced exactly as retrieved.

**1.** — *"One of the biggest finding is that nonprofits are seeing an increase in demand for their services at the same time that they're seeing really large increases in the burnout of their staff."*
— **Dr. Elisha Smith Arrillaga**, Vice President of Research, Center for Effective Philanthropy. Interview with the National Council of Nonprofits on *State of Nonprofits 2026*, ~May 2026. `[R2]` *(sic on "finding")*

**2.** — *"This isn't happening at the margins — it's happening in cities and towns across the country, to the organizations people rely on most when they have nowhere else to turn."*
— **Dr. Elisha Smith Arrillaga**, VP Research, CEP. On *State of Nonprofits 2026*, May 2026. `[R2]`

**3.** — *"Burnout has intensified dramatically in the last year for nonprofit staff and leadership alike, as their organizations are faced with a combination of increased demand for their work and a tougher funding environment."*
— **Dr. Elisha Smith Arrillaga**, VP Research, CEP. On *State of Nonprofits 2026*, May 2026. `[R2]`

**4.** — Nonprofits are *"pausing operations, closing, or merging."*
— **Dr. Elisha Smith Arrillaga**, VP Research, CEP. On *State of Nonprofits 2026*, May 2026. `[R2]` — partial quote; fuller sentence not retrievable.

**5.** — *"The stakes are that we might not make it as an organization."*
— **Anonymous nonprofit leader**, respondent to CEP's *A Sector in Crisis* (fielded Aug–Sep 2025), as reported by Inside Philanthropy. `[R2]` **The single most severe felt-pain statement located in this workstream.**

**6.** — Funders were eliminating support to *"community-based organizations that provide vital services to LGBTQ+ people."*
— **Anonymous nonprofit respondent**, CEP *A Sector in Crisis*, via Inside Philanthropy. `[R2]`

**7.** — *"We are increasingly concerned about staff burnout and organizational capacity. Our small team is working tirelessly to bridge funding gaps, reapply for grants, and sustain essential services. Without stable, predictable support, we risk losing key personnel and being forced to scale back core operations, an outcome that would profoundly impact the communities we are dedicated to serving."*
— **Anonymous nonprofit leader**, identified only as a "2025 respondent." `[R3 — ATTRIBUTION UNCERTAIN]` Most likely an Urban Institute *Nonprofit Trends and Impacts* open-ended response or a CEP survey verbatim; could not be confirmed. **Re-verify before use.**

**8.** — *"They are the ones who must look into the eyes of someone seeking help and tell them that we cannot provide services for them. It is demoralizing ... As the leader, I am carrying the weight home every day."*
— **Anonymous nonprofit leader**. `[R3 — ATTRIBUTION UNCERTAIN]` Source publication not determinable from the retrieved summary. The most vivid frontline-pain quote located. **Re-verify before use.**

**9.** — *"We have had to be agile, flexible, and optimistic in ways that I haven't experienced before."*
— **Elizabeth Lindsey**, Genesys Works (role title not captured in the retrieved text; she is widely identified as CEO but that was **not** confirmed in retrieval and is therefore not asserted here). `[R3 — ATTRIBUTION UNCERTAIN]` **Re-verify before use.**

**10.** — On foundation hesitancy: *"Fear of political retaliation, litigation, or threats to 501(c)(3) status is causing some funders to delay or reconsider investments."*
— **English Hudson Consulting**, blog post "Nonprofits Are Facing a Perfect Storm." `[R2]` **[Anecdote]** — consultancy commentary, not survey evidence. Included because it names a mechanism (chilling effect on funders) that no Tier-1 survey quantified.

### Quote shortfall — stated plainly

The brief asked for **8–12 fully attributed** quotes. **I have 10 quotes but only 4 fully attributed** (three to Smith Arrillaga, one to a consultancy). Four are anonymous-by-design survey verbatims. Three carry uncertain attribution.

Named leaders who *were* identified as having given on-record accounts but whose actual words could not be retrieved:
- **Ricshawn Roane**, Executive Director, Weissberg Foundation — Chronicle of Philanthropy, "How 6 Leaders Are Navigating Federal Funding Cuts"
- **Crystal Rountree**, CEO, Jumpstart for Young Children — same article
- **Mitch Stripling**, Pandemic Response Institute, Columbia — Chronicle of Philanthropy op-ed
- Four further leaders in the Chronicle piece whose names were not surfaced

That article is the highest-value unretrieved quote source in this workstream. **Priority target on network restoration.**

---

## Data gaps

Explicit no-data entries. Each records what was sought and how hard.

**1. NO PRIMARY DOCUMENT RETRIEVED — 21 fetch attempts across 12 hosts.** Every WebFetch and curl attempt returned HTTP 403 at the egress gateway, including a control request to `example.com`. Confirmed against the proxy's own `recentRelayFailures` log. Affects **every** finding in this workstream. Not a source problem; an environment problem.

**2. NO DATA FOUND after 3 searches for: share of nonprofits fearing closure.** Searched "at risk of closing," "may have to close," "closure," "survival" against CEP 2026 and the NPR/Axios coverage. NPR's headline is literally "Survey warns that some nonprofits are in danger of closing" — yet **no percentage was ever surfaced**. Given that this is the highest-intensity need in the ranking, its absence is the most consequential gap here. It may exist inside the unreadable CEP PDF.

**3. NO DATA FOUND after 2 searches for: share of nonprofits drawing down reserves.** CEP's *A Sector in Crisis* describes "dipping into reserves" qualitatively as a response, with no share attached in retrievable text. NFF's 36%→26% (≥6 months cash) is the closest proxy but measures a different thing — reserve *level*, not the *act* of drawdown.

**4. NO DATA FOUND after 2 searches for: hours available for fundraising vs. hours required.** No survey instrument located measures fundraising-capacity in hours. The only hours figure found (15–20 hrs/week on automatable admin) is expense-software marketing with no methodology and is discarded.

**5. NO DATA FOUND after 2 searches for: national mean nonprofit vacancy rate.** Only NJ Center for Nonprofits reports an actual average (18%, NJ only). Independent Sector reports a tail statistic (11% of orgs ≥21% vacant). No national mean exists in the retrieved material.

**6. NO DATA FOUND after 3 searches for: development-staff-specific turnover with traceable methodology.** ~19%-vs-12% turnover, "7 in 10 job-seeking," 59% hiring difficulty, 60% talent-challenge, 5–7-year ED tenure — all surfaced **only** via content-marketing aggregators with no named instrument, n, or field dates. **Discarded per methodology rule.** Likely primaries to chase: Nonprofit HR Talent Management Practices Survey; *2026 Nonprofit Salaries and Staffing Trends* (Careers In Nonprofits / Professionals for NonProfits) — a PDF for the latter was indexed but not retrievable.

**7. NO DATA FOUND after 2 searches for: compliance/audit/reporting burden as a ranked leader concern.** No Tier-1 survey instrument located includes it. See `## Compliance pressure`.

**8. Michigan Community Resources 2026 Needs Assessment — CONFIRMED TO EXIST, CONTENTS UNRETRIEVABLE.** Documents engagement with **158 nonprofits across Michigan** on 2025 strengths/challenges, framed around the first year of the second Trump administration. **The report is gated behind a download form**, so no statistics are available even absent the network block. The 2025 predecessor (104 organizations, fielded from fall 2024) yielded only governance percentages on denominators of 25–64 — too small to be useful. Requested state sample **not satisfied for Michigan**.

**9. NY Council of Nonprofits (NYCON) 2026 State of the Sector — CONFIRMED TO EXIST, NO NUMBERS RETRIEVED.** Search explicitly returned that the specific percentages "are not included in these search results." NFF's NYC cut was substituted as the New York data point. Requested state sample **only partially satisfied for New York**.

**10. CalNonprofits — only a Jan 2025 instrument located** (n=394, fielded Jan 9–31 2025, distributed to CalNonprofits' email list — a self-selected convenience sample, treat accordingly). This predates the core window and should be labelled baseline. A separate California survey of 164 nonprofits on federal-policy impacts was referenced but its sponsor could not be pinned down (possibly Little Hoover Commission Report #289, June 2025). No 2026 CalNonprofits instrument found.

**11. North Carolina, Minnesota, Ohio, Washington state associations — no 2026 survey results found.** Minnesota's 2026 Current Conditions Survey and Salary & Benefits Survey were confirmed to be **still in the field or unpublished** as of the search (participation deadline May 31, 2026). NC Center for Nonprofits has 2025 federal-grant-freeze policy commentary but no retrievable survey percentages.

**→ State-association sampling scorecard vs. the "at least 4 states" requirement: NJ (good — full data), NY (partial — NFF substitute only), MI (confirmed but gated, zero data), CA (baseline-only, out of window). Effectively 1 solid + 1 partial + 1 baseline. REQUIREMENT NOT MET.**

**12. BDO Nonprofit Standards 2025 — no sample size or field dates retrievable.** All BDO percentages in this document therefore carry incomplete metadata and must be treated as directional only. Same for M+R Benchmarks 2026 (n not captured) and NJ Center for Nonprofits 2026 (n not captured).

**13. Uncorroborated CEP-attributed figures — flagged, not adopted.** Three figures were attributed to CEP by intermediaries but could not be traced to any CEP-published page in search results:
- "52% hold ≤3 months cash on hand; 18% hold ≤1 month" — surfaced via a CPA blog and a **corporate-card vendor's Facebook post**. Retrieval grade R3. **Do not publish without verification.**
- "86% reported negative impacts on financial health and operational stability since January 2025" — R3.
- "95% of nonprofit leaders concerned about staff burnout; nearly 50% difficulty filling vacancies" — surfaced only via an HR-services blog. **NOT adopted anywhere in this document.**

**14. No federal nonprofit employment data exists for the research window.** The BLS nonprofit research series runs only through **2022**. There is no authoritative government count of nonprofit employment for 2025–26. This structural absence is why an outplacement firm's announcement-census (Challenger) is carrying the entire quantitative weight of the sector job-loss narrative — a fragile foundation worth flagging to the wider research operation.

---

## Source log

Legend — **P** primary publisher / **S** secondary coverage. **Fetched?** — `NO (403)` = fetch attempted and blocked; `snippet` = seen only via search result summary; `URL only` = URL surfaced but not summarized.

### Priority primary sources — all blocked

| URL | P/S | Credibility note | Fetched? |
|---|---|---|---|
| `cep.org/wp-content/uploads/2026/05/CEP_State_of_Nonprofits_2026_FNL.pdf` | P | **THE key document.** Flagship annual, 4th ed. Panel restricted to foundation-funded orgs — not generalizable to all US nonprofits. | **NO (403 — host policy-blocked)** |
| `cep.org/wp-content/uploads/2026/01/CEP_A_Sector_in_Crisis_FNL.pdf` | P | Second key document. Dual nonprofit+foundation survey design is a genuine methodological strength. | **NO (403)** |
| `cep.org/wp-content/uploads/2026/01/A_Sector_in_Crisis-2-pager_FNL.pdf` | P | Board-book 2-pager; likely the fastest route to headline numbers. | **NO (403)** |
| `cep.org/wp-content/uploads/2025/05/NVP_State-of-Nonprofits_2025.pdf` | P | Prior-year edition — required for trend deltas. | **NO (403)** |
| `cep.org/report-backpacks/state-of-nonprofits-2026/` | P | Landing page w/ methodology. | **NO (403)** |
| `cep.org/report-backpacks/a-sector-in-crisis-.../` | P | Landing page. | **NO (403)** |
| `cep.org/news/press-releases/new-cep-study-reveals-a-nonprofit-sector-in-crisis/` | P | Press release. | **NO (403)** |
| `cep.org/blog/a-perfect-storm-one-nonprofit-leader-on-fear-funding-and-finding-a-way-through/` | P | First-person leader account — high quote value. | **NO (403)** |
| `nff.org/wp-content/uploads/NFF-2025-Survey-Report.pdf` | P | **Largest n in the set (2,206).** 10th edition. NFF is a CDFI lender — mild interest in a distress narrative. | **NO (403)** |
| `nff.org/insights/2025-state-of-the-nonprofit-sector-survey-findings/` | P | Findings page. | **NO (403)** |
| `nff.org/insights/survey-nyc-nonprofits-.../` | P | NYC regional cut. | **NO (403)** |
| `nff.org/insights/2026trends/` | P | 2026 trends commentary — requested by brief, not retrieved. | **NO (403)** |
| `healthysector.org/.../Independent-Sector-Health-of-the-Nonprofit-Sector-Report-2025.pdf` | P | Dec 2025. Compiles others' data as much as originating it — check provenance of each stat inside. | **NO (403)** |
| `independentsector.org/resource/health-of-the-u-s-nonprofit-sector/` | P | Landing page. | **NO (403)** |
| `independentsector.org/resource/trust-in-civil-society/` | P | Trust series, 7th yr, Edelman-fielded, n=3,000, MoE ±2% — **best-specified methodology in this workstream.** | **NO (403)** |
| `independentsector.org/blog/new-polling-56-of-americans-highly-trust-nonprofits.../` | P | 2026 trust release. | **NO (403)** |
| `urban.org/sites/default/files/2025-10/How_Government_Funding_Disruptions_Affected_Nonprofits_in_Early_2025.pdf` | P | **Best sampling frame located** (501(c)(3)s ≥$50K rev/exp). Neutral. Highest-confidence source here. | **NO (403)** |
| `urban.org/research/publication/nonprofit-leaders-top-concerns-entering-2025` | P | 2024 NSNTI, n=2,975 open-ended. Baseline. | **NO (403)** |
| `urban.org/urban-wire/nonprofit-leaders-concerns-about-finances...` | P | 2024→2025 concern trend. | **NO (403)** |
| `urban.org/data-tools/nonprofit-trends-tracker` | P | Interactive tracker. | **NO (403)** |
| `candid.org/blogs/nonprofit-financial-instability/` | P | Candid aggregates; check provenance per stat. | **NO (403)** |
| `candid.org/blogs/foundation-payout-rate-giving-forecast/` | P | 2026 foundation forecast. | **NO (403)** |
| `candid.org/blogs/nonprofit-closures-layoffs-early-warning/` | P | **Closure/layoff tracker — directly targets the #1 data gap.** Explicitly experimental; author concedes closure data is hard to obtain. | **NO (403)** |
| `philanthropy.indianapolis.iu.edu/.../giving-usa-report-2026.html` | P | Giving USA 2026 / Lilly Family School. Gold standard for aggregate giving; estimates, revised in later editions. | **NO (403)** |
| `publications.fepreports.org/` | P | FEP quarterly. Large transactional panel, not a survey. **Recent methodology change breaks back-comparability.** | **NO (403)** |
| `afpglobal.org/news/fundraising-effectiveness-project-data-q1-2025...` | P | FEP Q1 2025 release. | **NO (403)** |
| `mrbenchmarks.com/fundraising/` , `/email-messaging/` | P | **VENDOR (M+R agency).** Sample = participating orgs, skews large/digitally mature. | **NO (403)** |
| `bdo.com/insights/industries/nonprofit-standards-a-benchmarking-survey` | P | **VENDOR (audit/advisory firm).** 9th annual. Notably the most optimistic source in the set — consistent with a client base of larger orgs. | **NO (403)** |
| `ccsfundraising.com/insights/ccs-philanthropy-pulse/` | P | **VENDOR (fundraising consultancy).** n=618, Q4 2025 — methodology better disclosed than most vendor surveys. | **NO (403)** |
| `njnonprofits.org/wp-content/uploads/2026/03/2026AnnualSurveyRpt.pdf` | P | **Best state-level source found.** Full report + exec summary both indexed. Only source with a stated average vacancy rate. | **NO (403)** |
| `njnonprofits.org/.../2025AnnualSurveyRpt.pdf` | P | Prior-year NJ, for state-level deltas. | **NO (403)** |
| `mi-community.org/2026-nonprofit-needs-report` | P | 158 MI nonprofits. **Gated behind a download form** — inaccessible even without the block. | **NO (403)** |
| `nycon.org/` | P | NYCON 2026 State of the Sector — exists, numbers not surfaced. | **NO (403)** |
| `calnonprofits.org/` | P | No 2026 instrument found. | **NO (403)** |
| `nptrust.org/philanthropic-resources/charitable-giving-statistics/` | P | **VENDOR (largest DAF sponsor)** — direct interest in DAF growth narrative. | **NO (403)** |
| `dafresearchcollaborative.org/annual-daf-report/2025` | P | DAF Research Collaborative — more neutral than sponsor-published DAF data. | **NO (403)** |
| `bls.gov/bdm/nonprofits/nonprofits.htm` | P | Authoritative but **only through 2022** — unusable for the window. | **NO (403)** |
| `nonprofitcenter.schar.gmu.edu/nonprofit-employment-data-project/` | P | GMU Nonprofit Works (ex-Johns Hopkins), relaunched Feb 2025. | **NO (403)** |

### Secondary coverage — snippets only

| URL | P/S | Credibility note | Fetched? |
|---|---|---|---|
| `councilofnonprofits.org/articles/interview-dr-elisha-smith-arrillaga...` | S | **Source of quotes 1–3.** NCN is an advocacy membership body — interested party, but quotes are direct. | NO (403) — snippet |
| `councilofnonprofits.org/pressreleases/new-study-highlights-impact-of-trump-administration-actions...` | S | NCN release on CEP 2026. Advocacy framing. | NO (403) — snippet |
| `npr.org/2026/05/12/nx-s1-5806032/...` | S | NPR on CEP 2026. Source of the "29,000 jobs" rounding. Syndicated to ~10 member stations (all indexed separately — same text). | NO (403) — snippet |
| `axios.com/2026/05/12/nonprofits-federal-funding-survey` | S | Axios on CEP 2026; clean restatement of 66% / 39%-vs-22%. | NO (403) — snippet |
| `insidephilanthropy.com/home/report-nonprofit-sector-is-facing-existential-threats` | S | **Source of quotes 5–6.** Sector trade press; reliable on CEP specifics. | NO (403) — snippet |
| `philanthropy.com/news/nonprofit-layoff-tracker/` | S | "What We Know — and Don't Know About the Nonprofit Layoff Crisis." **Title itself concedes the data gap.** | NO (403) — snippet |
| `philanthropy.com/news/how-a-year-of-funding-whiplash-reshaped-the-nonprofit-work-force/` | S | Source of the Challenger 28,696 figure. | NO (403) — snippet |
| `philanthropy.com/solutions/how-6-leaders-are-navigating-federal-funding-cuts/` | S | **Highest-value unretrieved quote source.** Names Ricshawn Roane (Weissberg Fdn), Crystal Rountree (Jumpstart). | NO (403) — snippet |
| `philanthropy.com/news/nearly-90-percent-of-nonprofit-leaders-worry-about-burnout/` | S | Chronicle on the ~89% burnout figure. | NO (403) — URL only |
| `fortune.com/2026/05/14/nonprofit-surging-demand-trump-administration-cuts-ceo-burnout/` | S | Fortune on CEP 2026 — mainstream pickup. | NO (403) — URL only |
| `forbes.com/sites/aparnarae/2025/12/04/the-invisible-job-crisis...` | S | Forbes contributor — **contributor network, editorial standards vary.** Treat as commentary. | NO (403) — URL only |
| `forbes.com/sites/aparnarae/2026/03/19/nonprofit-workers-are-in-crisis...` | S | Same author, same caveat. | NO (403) — URL only |
| `theconversation.com/1-in-3-us-nonprofits-that-serve-communities-lost-government-funding-in-early-2025-267795` | S | **Written by the Urban researchers themselves** — closest thing to primary that isn't behind the block. High value. | NO (403) — snippet |
| `nonprofitpro.com/article/state-of-nonprofits-2026-3-dire-realities...` | S | Trade press on CEP 2026. | NO (403) — snippet |
| `nonprofitpro.com/article/repeat-and-recaptured-donors-power-growth...` | S | Trade press on FEP. | NO (403) — snippet |
| `nonprofitpro.com/article/giving-usa-2026-bequests-do-the-heavy-lifting...` | S | Trade press on Giving USA 2026. | NO (403) — snippet |
| `nonprofitpro.com/article/nonprofit-revenue-growth-remains-strong...` | S | **Key disconfirming-evidence source** (CCS revenue growth). | NO (403) — snippet |
| `thenonprofittimes.com/npt_articles/fewer-donors-more-dollars-and-methodology-changes-at-fep/` | S | **Flags the FEP methodology change** — important comparability caveat. | NO (403) — snippet |
| `thenonprofittimes.com/npt_articles/study-stress-drained-coffers-threaten-npo-programs/` | S | NPT on CEP. | NO (403) — snippet |
| `thenonprofittimes.com/npt_articles/national-philanthropic-trust-grants-grew-20-to-6-6b/` | S | NPT on NPT DAF data. | NO (403) — snippet |
| `nonprofitquarterly.org/report-uplifts-new-and-old-challenges-facing-nonprofits/` | S | NPQ — sector press with an explicit editorial POV. | NO (403) — URL only |
| `nonprofitquarterly.org/the-quiet-collapse-why-the-erasure-of-the-nonprofit-sector...` | S | Opinion/advocacy framing — **not evidence.** | NO (403) — URL only |
| `foundationsource.com/blog/reflections-on-ceps-state-of-nonprofits-2026-webinar/` | S | **VENDOR blog** summarizing the CEP webinar; useful for numbers stated aloud but not in the PDF. | NO (403) — snippet |
| `foundationsource.com/blog/key-takeaways-from-giving-usas-2026-report...` | S | Vendor summary of Giving USA. | NO (403) — URL only |
| `fplglaw.com/insights/ceps-state-of-nonprofits-2026/` | S | Law-firm summary. | NO (403) — snippet |
| `ui.charlotte.edu/2026/03/18/public-funding-cuts-challenge-charlotte-nonprofits/` | S | UNC Charlotte Urban Institute — **distinct from the DC Urban Institute; do not conflate.** Source of the 30%-lost-public-funding Charlotte figure. | NO (403) — snippet |
| `insidehighered.com/news/business/mergers-collaboration/2025/12/18/colleges-couldnt-survive-2025` | S | **Key disconfirming source** — 16 closures in 2025, flat vs 2024. | NO (403) — snippet |
| `bestcolleges.com/research/closed-colleges-list-statistics-major-closures/` | S | Long-run closure base rates (0.3%→0.5%). | NO (403) — snippet |
| `subjecttoinquiry.com/2026/06/how-federally-funded-organizations-should-prepare-for-omb-proposed-overhaul...` | S | **Law-firm analysis — best compliance source found.** Aug 2025 EO, OMB 2 CFR overhaul, Oct 1 2026 target. | NO (403) — snippet |
| `peasebell.com/insights/omb-2026-uniform-guidance-overhaul/` | S | CPA-firm analysis of the Single Audit / Uniform Guidance overhaul. | NO (403) — snippet |
| `potomaclaw.com/news-Major-Overhaul-Affecting-Federal-Grant-Recipients` | S | Law-firm analysis. | NO (403) — URL only |
| `ncnonprofits.org/public-policy-blog/federal-grant-freezes-terminations-and-cuts-2025` | S | NC Center policy blog (no survey %). | NO (403) — URL only |
| `grantstation.com/gs-insights/tracking-federal-actions-impacting-nonprofit-sector` | S | Federal action tracker. **VENDOR.** | NO (403) — URL only |
| `unitedway.org/news/us-non-profits-slash-jobs-as-government-and-donor-funding-dries-up` | S | Challenger data restated; UWW is an interested party. | NO (403) — URL only |
| `darryllkjones.substack.com/p/independent-sectors-2026-trust-in` | S | Academic (nonprofit-law professor) commentary — **source of the IS 2026 trust methodology details.** | NO (403) — snippet |
| `michiganfoundations.org/resources/sector-crisis-how-us-nonprofits...` | S | CMF hosting CEP material. | NO (403) — URL only |
| `mainephilanthropy.org/programs/sector-crisis-...` | S | Maine Philanthropy Center hosting CEP material. | NO (403) — URL only |
| `nationalacademies.org/cdn/materials/a197fda7-...` | S→P | **National Academies-hosted copy of the CEP "Sector in Crisis" deck** — would have been the best available proxy for the blocked primary. | **NO (403)** |
| `hiltonfoundation.org/learning/listening-to-nonprofit-leaders-insights-from-the-state-of-nonprofits-2026/` | S | Funder reflection on CEP 2026. | NO (403) — URL only |
| `geofunders.org/news/how-foundations-can-support-nonprofit-partners-now/` | S | GEO — funder-practice framing. | NO (403) — URL only |
| `comptroller.nyc.gov/newsroom/comptroller-lander-spotlights-nonprofit-payment-delays...` | S→P | **NYC Comptroller — government primary** on nonprofit payment delays; audits launched of the 3 worst agencies. Underused; good WS-2 lead. | NO (403) — URL only |
| `lhc.ca.gov/wp-content/uploads/Report-289.pdf` | P | Little Hoover Commission, "Survey on California State Funding for Nonprofits," June 2025. Possible source of the CA n=164 figure. **Unconfirmed.** | NO (403) — URL only |

### Sources encountered and DISCARDED (recorded so they are not re-litigated)

| URL | Why discarded |
|---|---|
| `missionedge.org/news-and-resources/talent-burnout-and-retention...` | Consultancy content marketing; turnover stats untraceable to any named instrument. |
| `cnpc.coach/nonprofit-executive-director-statistics/`, `/nonprofit-leadership-development-statistics/` | Coaching-service SEO listicles. Claims "sourced & cited" but chains do not resolve. |
| `foundationlist.org/nonprofit-hiring-trends-2026/`, `/2025-hr-trends/` | Job-board content marketing. |
| `getkleercard.com/blogs/nonprofit-expense-reporting-best-practices` | **Expense-card vendor.** The "15–20 hrs/week admin" figure is a sales claim, not research. |
| `facebook.com/PEXCard/posts/...` | **Corporate-card vendor's Facebook post** — one of only two places the "52% ≤3 months cash" figure appeared. Disqualifying provenance. |
| `fundrobin.com/articles/...` (2 URLs) | AI-generated-appearing "thought leadership"; no methodology. |
| `intuwork.com/post/nonprofit-funding-crisis-what-survivors-do` | Vendor content marketing. |
| `sureimpact.com/post/a-sector-in-crisis` | Vendor blog on CEP; adds nothing beyond the primary. |
| `goodera.com/blog/coping-with-nonprofit-burnout` | Vendor SEO. |
| `timerewards.com/2026-nonprofit-compliance-changes...`, `gatekeeperhq.com/blog/what-is-nonprofit-compliance...`, `instrumentl.com/blog/grant-management-guide`, `vee.com/post/best-practices-for-grant-reporting...`, `blog.blackbaud.com/nonprofit-grant-compliance-warriors/` | Compliance-software marketing. No primary data. |
| `brymar.cpa/post/insights-nonprofit-financial-resilience-2026`, `bpm.com/insights/2026-nonprofit-sector-outlook/`, `pivotcpas.com/...`, `claconnect.com/...` | Professional-services marketing; restate others' numbers without adding provenance. |
| `liveimpact.org/blog/nonprofit-2025-year-in-review-trends`, `nptechforgood.com/...`, `truesense.com/blog/...` (2), `virtuous.org/blog/giving-usa-2026/`, `dbd.group/blog/...`, `amplifinp.com/blog/...`, `stelter.com/2026/06/23/...` | Vendor restatements of Giving USA / M+R. Used only to confirm a figure's existence, never as source of record. |
| `nonprofitlearninglab.org/post/the-complete-guide-to-nonprofit-careers-2026`, `talenthr.io/blog/talent-retention-in-2026/`, `thehrsource.com/...`, `ihire.com/...`, `bamboohr.com/blog/nonprofit-hr-trends`, `hr.com/...`, `spelmanandjohnson.com/...`, `blog.execsearches.com/...` | Generic HR content marketing. |
| `english-hudson.com/blog/the-perfect-storm` | Consultancy blog. **Retained for quote 10 only**, explicitly graded [Anecdote]. |
| `caseworthy.com/articles/...`, `insurancefornonprofits.org/preparing-for-layoffs/`, `hycaz.org/...`, `galaxydigital.com/blog/...`, `oneabacusadvisory.com/...`, `nfcb.org/...`, `techsoup.org/...`, `regenerativeschool.substack.com/...`, `abetternonprofitsector.substack.com/...`, `daniellevanzorn.com/...`, `grantsights.com/...`, `zoominfo.com/...`, `causeiq.com/...`, `linkedin.com/posts/grace-nicolette...`, `facebook.com/minnesotanonprofits/` | No primary data, or single-practitioner commentary. |
| `cryptocoin.news/...` | False-positive search result ("perfect storm"). Irrelevant. |

---

## Re-verification checklist (execute first when network access is restored)

Ordered by value-at-risk:

1. **`CEP_State_of_Nonprofits_2026_FNL.pdf`** — confirm: n=380 of 887 invited (43% RR); 301 repeat respondents; Feb 2026 field dates; 46%/29% burnout; 39%/22% deficit; 66% financial stability; 73% demand; ~60% foundation difficulty vs 48% federal; 26% reduced services. **Specifically hunt for a closure-risk percentage** (Data gap #2). **Verify or kill the 52%/18% cash-on-hand figure** (Data gap #13) — currently sourced to a card vendor's Facebook post.
2. **`CEP_A_Sector_in_Crisis_FNL.pdf`** — confirm: nonprofit n=408 (46% RR), foundation n=227 (30% RR), Aug–Sep 2025; 27 + 31 interviews Sept 2025; 69% / 36% / 34% / >40%; 65% demand; 71% stability; ~30% service reduction; 30% staff reduction. **Look for a reserve-drawdown percentage** (Data gap #3).
3. **`NVP_State-of-Nonprofits_2025.pdf`** — the 2025 baseline. Without it, no CEP delta is independently verifiable.
4. **`philanthropy.com/solutions/how-6-leaders-are-navigating-federal-funding-cuts/`** — harvest named, attributable quotes. Closes the quote shortfall.
5. **`NFF-2025-Survey-Report.pdf`** — confirm exact field dates (currently unknown) and reconcile 36% vs 37% deficit (all-respondents vs repeat-respondents).
6. **`njnonprofits.org/.../2026AnnualSurveyRpt.pdf`** — capture the missing n behind the 18% vacancy rate and 47% shortage figures.
7. **`candid.org/blogs/nonprofit-closures-layoffs-early-warning/`** — the closure tracker; directly targets the largest data gap.
8. **BDO / M+R** — capture the missing sample sizes and field dates so their figures can be graded properly.
9. **NYCON 2026 State of the Sector; Michigan Community Resources 2026 (form-gated); a 2026 CalNonprofits instrument** — to bring the state-association sample up to the required 4 states.
10. **`urban.org/.../How_Government_Funding_Disruptions...pdf`** — capture the n behind the 1-in-3 / 21% / 27% / 6% figures. This is the most methodologically sound source in the set and is currently carrying no sample size.
