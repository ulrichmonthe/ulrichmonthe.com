# Deep UX pass — the three tools

**Date:** August 2026 · **Method:** each tool driven end to end in a browser, not reviewed from source.

---

## What I found, in one line

All three tools are **one-shot**. You use one, you get a good answer, you leave, and nothing brings you back or travels with you. That is the single largest gap, it is shared across all three, and it is the direct cause of both problems in the brief: nothing is memorable because nothing persists, and nothing converts because nothing is shareable.

Fixing it adds no friction. Every fix below is additive — nothing gates a path that is currently open.

---

## What each tool does well (do not break these)

**EIN Checker** — the audience toggle (*"I'm vetting an org" / "This is my org"*) reframes the whole result for two different jobs, which most tools never bother to do. Pre-seeded examples kill the blank-state problem. The batch box already exists.

**Policy Generator** — genuinely the strongest flow on the site. Twelve steps, honest "≈ 3 min" estimate, a live counter, and — the best moment in any of the three — an **analysis stage before generation**: *"Your AI risk profile · Moderate · 2 rule sets in play · 1 gap flagged"*, followed by named readiness gaps. That is a real diagnostic, delivered before anything is asked in return.

**Funder Standing** — refusal is a first-class state. Gated rows say which condition failed. Match rate sits on every row. It is the most intellectually honest of the three.

---

## The gaps, ranked

### Tier 1 — highest leverage, no friction added

**1. Nothing is shareable. (Funder Standing, then the others.)**

The jobs work established that a development director's real job is *defensibility* — the artifact is ammunition for a conversation with an ED or a board. Right now the only ways to move a screen out of the browser are a CSV or a screenshot.

A screen of 12 funders is entirely client-side over public data. It could be a URL: `?s=ein,ein,ein`. That one change does three jobs at once — it is how someone returns, how they send it upward, and how the tool spreads without any marketing.

**This is the highest-value change available and it is roughly an afternoon.**

**2. The screen has rows but no headline. (Funder Standing.)**

Twelve rows of data is a table. The memorable version is the aggregate sentence sitting above it:

> *These 12 foundations funded 41 organizations last year. Six of them were new. Applying to all twelve is roughly 190 hours.*

A number that surprises someone is what gets repeated in a meeting. Right now the tool makes the reader do that arithmetic themselves, which means nobody does it.

**3. No per-foundation URLs. (Funder Standing.)**

There is no way to link to one foundation. That blocks the obvious sharing move (*"look at this one"*) and it also means **the entire SEO plan is currently unbuilt** — `/foundations/[slug]/` is where the search traffic was always going to land. The slug registry already exists; the pages do not.

**4. Single-check users never discover batch. (EIN Checker.)**

Batch is the qualification signal the conversion work depends on, and nothing surfaces it to someone checking organizations one at a time. After a second or third single check, the tool should say so in passing: *"Checking several? Paste a list."* No modal, no interruption — one line where it is already looking.

### Tier 2 — deepens the flows that exist

**5. The readiness gaps are the best output and they get buried. (Policy Generator.)**

*"Staff use personal AI accounts. Move work use to organization-managed accounts"* is specific, about them, and actionable — the most memorable thing the tool produces. It appears once mid-flow and does not survive into the final documents.

It should be a section of the delivered packet, and the closing CTA should reference **their** flagged gaps rather than gaps in general. That costs nothing and converts far better than a generic offer.

**6. No return path anywhere.**

If a board meets in three weeks, there is no way back to a generated policy. Funder Standing saves a screen to `localStorage` but never says so and offers no way to reach it. The EIN checker keeps no record of what was checked.

Minimum viable: a line saying *"this is saved on this device"* plus a way back to it. Costs one line of copy and a link.

**7. Nothing tells anyone when the data changes. (Funder Standing.)**

Filings update annually and the tool knows its own recompute date. *"Tell me when this foundation's next filing lands"* is an email capture that is genuinely useful to the person giving it — the opposite of extractive, and the only natural return trigger any of the tools has.

**8. Continue is disabled with no explanation. (Policy Generator, step 4.)**

Step 4 asks two questions — paid staff and active volunteers — and gates Continue on both. Answer one and the button stays dead with nothing saying why. A short hint (*"answer both to continue"*) removes the only confusing moment in an otherwise excellent flow.

### Tier 3 — worth doing, lower urgency

**9. The error state is a dead end. (EIN Checker.)** *"Something went wrong reaching the checker."* True, but it ends there. Offer a retry and a next step.

**10. Wrong arrival mode. (Funder Standing.)** A grant writer does not browse 118 foundations; they arrive holding a list of twelve. "Paste your list" should be a first-class entry point beside search.

**11. No session history. (EIN Checker.)** Five checks leave no trace. A running list would make it feel like a workspace rather than a lookup, which is what a portfolio user actually needs.

---

## On the existing gate

The policy generator locks the **board memo** and **adoption resolution** behind email while leaving the policy and staff one-pager free. That is a well-judged split: the free artifacts are what an individual needs, the gated ones are what someone taking this to a board needs — which is exactly the higher-intent buyer.

I would leave it alone. It is the only gate on the site and it sits in the right place.

---

## The through-line

Every fix above is the same fix wearing different clothes: **give the work somewhere to live.**

A URL for a screen. A saved policy you can return to. A record of what you checked. A notification when the data moves. None of them ask anything of the user, and all of them convert a one-shot lookup into something with a second visit — which is where memorability comes from, and where consulting conversations actually start.

## Suggested order

1. Shareable screen URL + aggregate headline (Funder Standing)
2. Per-foundation pages (also unblocks the SEO plan)
3. Contextual batch prompt (EIN Checker)
4. Readiness gaps into the packet + gap-specific CTA (Policy Generator)
5. Return paths and the filing-update notification
