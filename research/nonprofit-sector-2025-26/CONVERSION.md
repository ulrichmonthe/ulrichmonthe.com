# Tool → consulting: conversion paths and instrumentation

**Date:** August 2026 · **Scope:** the three tools at `/live-projects/`

---

## The premise

Free tools convert badly to high-ticket consulting through generic calls to action, because the visitor did not arrive with a budget question. Conversion happens at one specific moment: **when the tool surfaces a problem it cannot itself solve, in front of someone who holds a budget.**

Each tool therefore needs its own path, because each reveals a different problem to a different buyer. Running them as one funnel wastes the two that work.

---

## Per-tool paths

### EIN Due-Diligence Checker — converts on scale

| | |
|---|---|
| Reveals | This grantee is amber. And there are four hundred more. |
| Next question it cannot answer | "How does this become part of our grants process rather than a person doing it by hand?" |
| Buyer | Foundation grants manager or operations director — the best-funded audience across all three tools |
| Engagement | Due-diligence workflow design: an automation project wearing a compliance hat |
| CTA shipped | *"Checking one is a search box. Checking four hundred is a process."* |

**The batch upload is the qualification mechanism.** One EIN is curiosity. A CSV of three hundred is institutional work, a standing process problem, and a budget line — established without asking the visitor anything.

### Nonprofit AI Policy Generator — converts on the implementation gap

| | |
|---|---|
| Reveals | You have a policy. The policy names things you do not have: an inventory, a review cadence, an approver. |
| Next question it cannot answer | "We adopted it. What actually changes on Monday?" |
| Buyer | ED or ops lead — or, far more valuably, a funder who wants this for its grantees |
| Engagement | Responsible-AI pilot. The most direct line to the existing service of any tool here. |
| CTA shipped | *"The policy is the easy part."* plus an offer to review a generated policy for implementation gaps, and an explicit invitation to funders. |

The funder-as-distributor path is the single highest-value flow on the site. A foundation offering this to two hundred grantees is a cohort engagement, not one contract.

### Funder Standing — converts by being seen, not by being used

The obvious read is wrong here.

Its users are grant writers and development directors, and the sector research found that segment is **cutting, not buying** — the poorest audience in the sector. Optimising this tool for user conversion optimises the wrong thing.

But the foundations *in* the data also read it. A program officer who finds their own new-grantee rate published, computed from their own filings, reacts — and the second thing they ask is how it was built.

| | |
|---|---|
| Reveals | To grant writers: your pipeline is worse than you thought. To foundations: someone is measuring us. |
| Next question it cannot answer | Grant writers ask "where do we go instead" — that is fundraising strategy, **not the service on offer**. Foundations ask "how did you build this, and what else is in our data?" |
| Buyer | The foundation, not the user |
| Engagement | Data capability demonstration → analytics or product work |
| CTA shipped | *"If your foundation is in here."* — invites correction first, positions the capability second |

This tool earns through **authority and citation** rather than user conversion. The Openness Index is the engine: a citation in the Chronicle or NPQ puts the name in front of foundation staff in a context where it belongs to the person who measured something nobody else had.

---

## Instrumentation

Four signals separate institutional visitors from curious ones without gating anything.

| # | Signal | Where | What it means | Priority |
|---|---|---|---|---|
| 1 | **Batch upload used** — and row count | EIN checker | Institutional process work. The strongest single qualifier on the site. | **Highest** |
| 2 | **Subsector selected** | Policy generator | Organization type and rough size band, captured before any conversation | High |
| 3 | **Export / print** | Funder Standing | Building an artifact for someone else — a board packet or a client deliverable | Medium |
| 4 | **Repeat sessions across tools** | All | One person using two tools is evaluating the author, not the tool | High |

### How to capture them without breaking the privacy promise

The policy generator states that answers never leave the browser. That promise is load-bearing and must not be broken. Everything below is compatible with it:

- **Count events, never content.** Record that a batch of ~300 rows was processed; never the rows. Record that the subsector was "health"; never the free-text answers.
- **No identity.** No cookies tying a person to an organization. Cross-tool repeat visits can be measured with a first-party random ID in `localStorage`, which is a session counter, not an identity.
- **Say what is measured.** A line in the existing privacy note listing exactly these four counters costs nothing and reinforces the reason people trust the tools.

A minimal first-party endpoint is enough — event name, tool, coarse bucket, timestamp. No third-party analytics is required and adding one would undercut the positioning.

### The threshold that matters

The point is not a dashboard. It is a weekly list of **sessions that crossed a qualification line** — a batch above roughly fifty rows, or a third session across two tools. That list is short enough to act on by hand, which at consulting volumes is the correct response.

---

## The tension, and how the CTAs resolve it

The policy generator deliberately never asks for an email. Excellent for trust, and part of why it works. It also means the **highest-intent tool produces no pipeline.**

Breaking that promise would be a bad trade. The resolution shipped is an *asymmetric* offer: not "give me your email", but something worth trading for — send the policy you already have and get back the clauses organizations most often fail to implement. That converts intent into a conversation without gating the artifact, and the value moves first.

---

## What actually closes

For an AI product consultant, the tools are not lead magnets. **They are the portfolio** — the site's own lede says working software, not case studies.

Most contracts will not come from a CTA click. They will come from someone who used a tool, remembered it six weeks later when a project landed on their desk, and searched the name.

That argues for optimising the tools for **memorability and citation** over conversion mechanics — roughly the opposite of standard funnel advice, and the right call for this position. The CTAs above are there to catch the minority who are ready now. The Openness Index, the guides, and the tools themselves do the heavier work of being remembered.
