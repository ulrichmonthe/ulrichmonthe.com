# Data feasibility check — can the new-grantee rate actually be computed?

**Run:** 30 July 2026 · **Question:** is Form 990-PF Part XV grant detail available as structured data for enough filers to compute new-grantee rates at scale, or does too much of it sit in scanned PDFs?

**Verdict: it clears, with one real caveat that is not the one I expected.**

Same retrieval constraint as the main research — `irs.gov` and `apps.irs.gov` are blocked by this environment's egress policy, so the schema and mandate findings come from search summaries, not from reading the IRS schema files. The S3 probe below is direct observation.

---

## 1. Schema — the field exists and is mandatory ✅

`GrantOrContributionPdDurYrGrp` is a real repeating element in the 990-PF e-file schema. Each instance carries **recipient name, address, grant purpose, and amount**.

It is not optional: when a foundation reports contributions paid in Part I line 25 (`ContriPaidRevAndExpnssAmt` or `ContriPaidDsbrsChrtblAmt`), IRS business rules require **at least one** `GrantOrContributionPdDurYrGrp` entry. A foundation that paid grants cannot file without itemizing them.

**This is the field the whole product depends on, and it is structured, repeating, and enforced.**

## 2. Coverage — paper filing is gone ✅

The **Taxpayer First Act** (signed 1 July 2019) made electronic filing mandatory for the entire Form 990 series. For Form 990-PF it binds for **tax years ending on or after 31 July 2020**, for **all private foundations regardless of size** — the prior carve-outs (under 250 returns, under $10M assets) were eliminated.

**Consequence: for the FY2022–FY2025 window, coverage should be effectively complete.** The scanned-PDF scenario that motivated this check is a pre-2020 problem, not a current one.

## 3. Distribution — the path changed, and the old one is dead ⚠️

Direct probe from this session:

| Endpoint | Result |
|---|---|
| `s3.amazonaws.com/irs-form-990` | **200 — but zero keys.** Bucket resolves and is empty |
| `irs-form-990/index_2019.csv` … `index_2021.csv` | 404 |
| Sample `*_public.xml` object keys | 404 |
| `irs.gov`, `apps.irs.gov`, ProPublica API | Blocked by egress policy (000) |

That empty bucket is explained: **the IRS announced on 16 Dec 2021 that it would stop updating the AWS dataset as of 31 Dec 2021.** The bucket is a decommissioned shell. Anything written against it — including a fair amount of surviving tutorial code — is dead.

**Current viable sources:**
1. **IRS Form 990 series downloads page** — official, XML by year and month. Could not be reached from here.
2. **GivingTuesday Data Lake** — an S3 bucket holding as close to the full e-file universe as exists, **with clean index files**. Community-maintained. The index files matter more than they sound: the IRS's own indexes were the historical pain point.

**Existing tooling that materially cuts build cost:**
- `jsfenfen/990-xml-reader` (IRSx) — parses versioned 990 XML into standardized Python objects with original line numbers preserved
- `Nonprofit-Open-Data-Collective/irs990efile` — R package that builds a research database, pulling from the GivingTuesday Data Lake

**None of this needs to be built from scratch.** That is a meaningful change to the effort estimate.

## 4. The real caveat — 990-PF carries no recipient EIN ⚠️

This is the constraint that actually matters, and it is not the one the check was designed to find.

Part XV reports each grantee's **name and address**. It does **not** require the recipient's EIN. So "did this foundation fund this organization before?" cannot be answered by key lookup — it requires **name matching across filing years**.

**Why it is tractable:** the comparison is *within a single filer's own series*. One foundation, one preparer, usually one naming convention carried forward year to year. That is a far easier matching problem than reconciling grantee names across the whole sector.

**Why it is still a real risk:** naming drift is common — `Riverbend Youth Collective` / `Riverbend Youth Collective, Inc.` / `RYC Programs` — and preparers change. Address gives a second key, but organizations move. Match quality will vary by filer, and **the new-grantee rate is only as good as the match rate**, since an unmatched name looks exactly like a new grantee. **The error runs in the direction that makes closed foundations look open** — the specific failure the product exists to prevent.

**Design consequence:** match rate must be computed per foundation, surfaced, and used as the gate on issuing a verdict. This is what the "no verdict" state should key on — not filing format.

---

## What this changes

**The gate is passed.** The data exists, is structured, is mandatory, and coverage is essentially complete for the target window. Build effort is lower than assumed because parsers and a clean index already exist.

**The prototype was wrong about one thing and has been corrected.** Its "no verdict" case was a paper filer with a non-machine-readable grant schedule. Under the e-filing mandate that case barely exists for FY2022–25. It has been replaced with the failure mode that is real: grantee names that cannot be resolved to a stable entity at sufficient rate.

**Remaining unknowns, in order:**
1. Actual per-filer name-match rates on real data — measurable only by running it, and the single most important number for whether the product works
2. Filing lag: how far behind is the current e-file universe? Determines whether a verdict is 12 or 24 months stale
3. Whether GivingTuesday's index covers 990-PF as completely as it covers 990

**Next concrete step:** pull one year of 990-PF XML for a single state, compute match rates across three filing years, and see what share of foundations clear an 85% threshold. That is the number that decides this.
