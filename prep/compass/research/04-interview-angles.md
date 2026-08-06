# Interview Prep Research: Executive in Residence — AI, Compass Working Capital

## 0. Compass context (what could be verified)

- Compass Working Capital: Boston-HQ national nonprofit, ~38–50 staff, CEO Markita Morris-Louis (former Clarifi GC/exec; legal + financial-capability background). Three lines of work: direct-service FSS financial coaching, capacity building for other orgs (Compass FSS Link, compassfsslink.org), and policy advocacy. (Leadership: https://compassworkingcapital.org/leadership/ , FSS Link: https://www.compassfsslink.org/about-us/ , ZoomInfo staff count)
- Abt Global has run multiple rigorous evaluations of Compass's FSS model showing earnings and credit gains — Compass is unusually evidence-driven for its size; expect the CEO to care about measurement. (https://www.abtglobal.com/CompassFSS)
- June 2026: bipartisan housing bill passed a pilot expanding FSS asset-building — Compass is in a policy-momentum moment; AI capacity is likely framed as scaling infrastructure. (Morningstar/PR Newswire 2026-06-24)
- Could not find the EIR job posting itself (site 403'd). Budget size not confirmed (990s suggest ~$8–12M range; verify on GuideStar https://www.guidestar.org/profile/20-3975100).

## 1. State of the art: nonprofit AI adoption 2024–2026

**Adoption is near-universal; impact and governance are not.**
- TechSoup/Tapp Network, "State of AI in Nonprofits 2025" (n≈1,300): 85.6% exploring AI tools, only 24% have a formal strategy; only 24% have any AI policy (76% none); adoption ~2x higher in orgs >$1M budget (66% vs 34%). (https://page.techsoup.org/ai-benchmark-report-2025)
- 2026 benchmark coverage: adoption hits 92%, but only 7% report major impact — sector's core problem is conversion of usage into outcomes, not access. (NonProfit PRO)
- Fast Forward, "2025 AI for Humanity Report": 84% say funding is the top need to scale AI work; ~half report higher expenses from AI adoption. (https://www.ffwd.org/2025-ai-for-humanity-report)
- Google.org "Nonprofits and Generative AI" (2024, n=4,600): 4 in 5 see applicability, ~half not using due to tools/training/funding gaps; 2 in 5 orgs had zero staff trained; none had a majority trained. Accelerator grantees report goals achieved in ~1/3 the time at ~half the cost.
- Project Evident + Stanford HAI, "Inspiring Action" (2024): ~80% of both funders and nonprofits believe AI could enhance mission outcomes but lack tools/knowledge/funding.
- Salesforce Nonprofit Trends (7th ed., 2025): most orgs "early innings." Consumer trust: ~75% want to know when they're talking to AI; 45% likelier to use AI with a clear human escalation path.

**Common failure modes:**
1. Shadow AI: staff ChatGPT use with no policy → client data leakage (92% adoption / 24% policy gap).
2. Pilot purgatory: tools adopted, workflows unchanged, no impact (92%→7% gap).
3. Unfunded mandate: AI as add-on labor; expenses rise.
4. Vendor drift: outsourced systems change without org oversight (NEDA).
5. Generative AI where deterministic accuracy is required (NYC MyCity).
6. Training inequity: tools bought, literacy never built.

**Responsible-AI frameworks:**
- NIST AI RMF 1.0 — Govern/Map/Measure/Manage; credible backbone for right-sized policy.
- NTEN AI Framework for an Equitable World — equity-first question framework.
- NetHope AI Ethics for Nonprofits Toolkit + Humanitarian AI Code of Conduct.
- Fundraising.AI Framework — 10 tenets for responsible AI in fundraising (initiative 3).
- Project Evident OutcomesAI / Equitable AI Adoption (Gates-funded).
- Policy templates: Community IT acceptable-use template; Candid guide.

## 2. Case studies

**Successes**
- Crisis Text Line (triage, not conversation): ML prioritizes imminent-risk texters — ~86% of severe-risk identified in first conversations, ~94% of high-risk served in <5 min. AI does queue triage; humans do 100% of counseling. Counter-lesson: 2022 Loris.ai data-sharing scandal — consent-on-paper is not consent-in-spirit.
- CareerVillage "Coach": nonprofit-built AI career coach; co-designed with a 20-org coalition; 8-principle Responsible AI Framework. Model for "AI extends coaching reach where no human coach exists."
- Beam "Magic Notes" (UK adult social care): genAI turns recorded client meetings into case notes; ~85 UK councils. ~46–63% admin-time reduction (Swindon 63%, Somerset 11 hrs/week/practitioner, Kingston 50–60%), assessments submitted 65% faster. Closest analog to "AI strengthens the coach relationship" — buys back coach time. Caveat: accuracy/assumption errors requiring edits.
- SaverLife "Navigator": AI-powered personalized financial guidance for low-income members (650k+); published "early lessons" (empathy, transparency, adaptability). Most direct financial-coaching analog.
- Change Machine: Salesforce-based coach platform with AI fintech-product recommendation — coach-facing, not client-facing.
- NextLadder Ventures (Ballmer Group et al., ~$100M) funding AI for economic mobility — funding vehicle Compass could tap.
- JFF Center for AI & the Future of Work: workshops for career coaches on integrating AI.

**Failures**
- NEDA "Tessa" (2023): replaced human helpline (post-unionization) with chatbot that gave weight-loss advice to eating-disorder sufferers; pulled within days. Root causes: (a) replacement not augmentation framing; (b) vendor enabled generative responses without NEDA's knowledge; (c) no live output monitoring. Canonical anti-pattern for Compass's governing principle.
- NYC MyCity chatbot (2024): genAI bot told users landlords could reject Section 8 voucher holders (source-of-income discrimination), employers could take tips. Lesson: generative AI answering benefits/rights questions for low-income populations fails in ways that harm exactly Compass's clients; eligibility/rules need retrieval from vetted sources + human review, or shouldn't be automated.

**Cross-cutting lessons:** disclosure that AI is in use (75% want it); voluntary, revocable, trauma-informed consent; human escalation path always visible; bias/equity review before AI touches eligibility/prioritization/resource allocation; vendor change-control clauses; monitor live outputs, not just pilot outputs.

## 3. Governance specifics for Compass

**Client PII with LLM vendors:** no client PII in consumer-grade tools. Enterprise paths: enterprise tiers with no-training commitments, DPAs, zero-data-retention; or PII redaction before processing. (Vendor DPA terms not re-verified — check before citing specifics.)

**HUD/FSS data rules (differentiating detail):**
- FSS governed by 24 CFR Part 984; participants sign HUD-52650 Contract of Participation; PHAs report via HUD-50058. Compass operates as program partner with PHAs/owners — PHA retains ultimate program responsibility.
- EIV (Enterprise Income Verification) data is the hard line: access limited to HUD, PHA employees, PHA-hired agents; use restricted to recertification. Income data near EIV-derived data going into an LLM without PHA data-sharing-agreement review = serious compliance risk.
- Data map: (a) EIV-derived income data — likely never in LLMs; (b) client financial/coaching data — enterprise-only, consented, possibly de-identified; (c) internal knowledge/grant/finance content — low risk, fastest wins. Initiatives 2–4 are largely category (c) — strategic reason to start there.

**Consent architecture:** disclosure at intake; voluntary opt-out with no service penalty; recording consent for note-taking AI (MA is two-party consent — confirm with counsel); revocation mechanism; consent language at reading level and in Spanish.

**Lightweight governance policy shape:** 2–4 pages — approved-tool list; data classification with red lines; human-review-before-external-use rule; disclosure norms; one named owner + small cross-functional review group; quarterly review. NIST AI RMF as scaffolding, not bureaucracy.

**Funder-facing AI (initiative 3):** Candid surveys: only ~10% of foundations accept/plan to accept genAI-created applications, 67% undecided; 61% of nonprofits already use AI in fundraising vs 15% of foundations with applicant guidelines. Position: AI drafts, humans own voice and facts; check each funder's policy; never fabricate outcomes data.

## 4. Likely CEO interview questions (~15) and what strong answers emphasize

**Strategy**
1. "What would your first 90 days look like?" — Listen-first: ride along with coaches, map data flows, inventory shadow AI, ship one visible low-risk win (dev/comms or KM), draft governance baseline. Not: arrive with a tool list.
2. "How do you decide where AI goes first across our four initiatives?" — risk×readiness×value triage: start where data risk low and time savings provable (grants/reporting, onboarding KM, finance ops), sequence client-adjacent AI behind governance and consent. Cite 92%/7% gap: value comes from workflow redesign, not tool purchase.
3. "Our principle is AI strengthens, not replaces, the coach relationship. What does that mean operationally?" — Tests: more client-facing minutes for coaches (Beam: 46–63% admin reduction)? Human accountable for every client-affecting output? Visible path to a person? Contrast NEDA vs Crisis Text Line.
4. "How do you measure whether AI is working?" — Baseline first; coach time reallocation, quality spot-audits, client trust signals, cycle times; tie to Compass's evaluation culture (Abt). Kill criteria upfront.
5. "A consultant already owns program-delivery AI strategy. How do you work with that?" — Clarify decision rights week one; EIR owns enterprise governance, data architecture, initiatives 2–4; feeds guardrails into consultant's workstream; one shared governance framework so clients don't experience two AI regimes.
6. "What's realistic for an org of ~40 staff with a nonprofit budget?" — 2–3 durable wins and an operating system for AI (policy, literacy, vendor stack), not a transformation program. Fund via capacity grants (Google.org accelerator, NextLadder-type funders).

**Adoption**
7. "Coaches fear AI is a step toward replacing them." — Name it directly; coaches as co-designers (CareerVillage coalition model); early tools remove their most-hated tasks; NEDA's union-timing subtext shows why replacement framing is fatal.
8. "Staff are already pasting things into ChatGPT." — Don't punish, channel: approved enterprise tools beat prohibition; 76%-no-policy stat means this is normal; policy + training within a quarter.
9. "How do you build AI literacy without a training budget?" — Champions model, office hours, prompt libraries in real workflows; free curricula (NTEN, TechSoup, JFF).
10. "Tell me about an AI adoption effort that failed and why." — Pattern fluency: pilot purgatory, tool-first thinking, no workflow change, no owner after champion leaves.

**Judgment**
11. "A vendor pitches a client-facing financial-guidance chatbot. Evaluate it." — MyCity/Tessa lens: generative answers about benefits/eligibility for low-income families = highest-harm category; demand grounding in vetted content, output monitoring, contractual change control, human escalation; default may be "not yet."
12. "What client data can go into an LLM?" — FSS-specific map: EIV-derived data never; client PII only under enterprise DPA + consent, prefer de-identified; PHA data-sharing agreements reviewed first. Knowing EIV cold is a differentiator.
13. "A funder asks whether our grant proposals are AI-written." — Transparency: AI assists drafting, humans own substance and voice; Candid data (10% accept, 67% undecided); propose disclosure norm before being asked.
14. "AI flags a client as high-risk for dropping out. Act on it?" — Human-in-the-loop, bias-audited, used to offer support never to ration service; who bears the cost of a false positive?
15. "What would make you tell me to stop an AI project?" — Tripwires: client harm signal, consent gaps, vendor drift, accuracy below human baseline, coach trust collapsing. Willingness to kill projects is the judgment signal.

Also plausible: "How do you think about our data readiness?", "What does the board need to understand?", "What's the exit plan when your residency ends?"

## 5. Questions the candidate should ask the CEO (pick 4–6)

1. Consultant boundary: "Where exactly does the program-delivery AI consultant's mandate end and this role's begin — who arbitrates when an initiative touches both, since clients will experience one Compass?"
2. Funding: "Is this role and its tooling funded from unrestricted dollars, or a capacity-building grant? 84% of nonprofits say funding is the top constraint — what happens in year two?"
3. Data readiness: "How clean and centralized is coaching and escrow data today — one CRM, or spread across PHA systems and spreadsheets? What data-sharing agreements exist with PHA partners, and do they contemplate AI processing?"
4. Success definition & exit: "What does 'done' look like — a strategy the permanent team runs, a hire I help make, capabilities embedded in each department? What must be true at handoff?"
5. Board and risk posture: "What has the board been told about AI? Appetite for a formal policy this year? Where does the board sit between 'move fast' and 'first, do no harm'?"
6. Coach voice: "What have coaches themselves said about AI? Would you support coaches co-designing and holding veto power over coach-facing tools?"
7. Client trust: "Given clients are mostly Black and Latina women in a federal housing program — with real reasons to distrust both tech and government systems — how do you want consent and disclosure to feel, beyond compliance?"
8. Kill authority: "If I conclude a planned AI initiative shouldn't happen — including something the consultant proposes — do I have standing to say so, and to whom?"

**Uncertainty flags:** Compass budget/staff figures are third-party estimates; vendor DPA terms not re-verified; MA recording-consent application should be confirmed with counsel; "92%/7%" from NonProfit PRO 2026 coverage (methodology not inspected); Crisis Text Line figures self-reported.
