# Agents

Three scheduled agents that extend and check the site. Each is a version-
controlled definition applied with the `ant` CLI — the agent configuration
lives here, in git, rather than being clicked together in a console.

| Agent | Cadence | Environment | Status |
|---|---|---|---|
| Coverage Expander | Mondays 06:00 ET | `standing-agents` | ready |
| Index Watch | Mondays 08:00 ET | `standing-analytics` | **blocked** — needs Search Console |
| Evidence-Led Note Writer | 1st of the month, 07:00 ET | `standing-agents` | ready |

```
./agents/deploy.sh --dry-run     # print what would be sent
./agents/deploy.sh               # create or update everything
```

IDs land in `agents/.ids.env` (gitignored), so re-running updates rather than
duplicating. Agent updates create a new version; sessions already running keep
the version they started on.

---

## What runs where

Each agent gets the smallest reachable network it can do its job with.
`standing-agents` can reach the 990 filing mirror and GitHub, and nothing
else — not Google, not the analytics API. `standing-analytics` is the
reverse, and has `write` and `edit` disabled outright: Index Watch reports,
it does not modify the site.

---

## Coverage Expander

118 foundation pages are published. 10,700 filers in the index meet the
structural bar — four or more filing years, $10M–$500M in assets. This walks
that gap 250 ranks a week.

**One correction to the original plan.** This was scoped as a multiagent
coordinator fanning out one subagent per foundation. Reading the pipeline
first showed that would be strictly worse: `build_real.py` already
parallelises across filers with a twelve-thread pool, and replacing that with
150 subagents would cost far more, run slower, and produce byte-identical
output. Subagents earn their place when each one needs its own context window
for reasoning. Fetching and parsing XML needs no reasoning at all. So this is
a single agent, and the judgment it applies — is this expansion safe to
publish — is one context's worth of work.

### What had to be built first

The agent could not have worked against the pipeline as it stood.

- **`build_real.py --incremental`.** The full build wipes and rebuilds every
  foundation, and `.cache/` is gitignored, so a fresh sandbox re-fetches from
  S3 every run — roughly 220KB per filing-year. At a cohort of 4,000 that is
  several gigabytes weekly to reproduce data that did not change. Incremental
  mode reuses any committed document whose filing index has not advanced,
  records foundations that yielded nothing so they are not retried forever,
  and fetches only the new ranks. Measured on a 250 → 400 expansion: 118
  documents reused, 132 known misses skipped, 150 fetched.
- **`checks/expansion_diff.py`.** Peer medians are a property of the
  comparison set. Growing the cohort from 118 to 264 changed the peer median
  under **87 of the 118 pages already published** — a median move of 0.0097.
  Legitimate, and completely invisible in a diff of 400 JSON files. This
  reports it, and fails outright on the two changes that are never acceptable:
  a page that disappeared, or a slug that moved.
- **`scripts/build_sitemap.py`.** `sitemap.xml` was hand-maintained. Adding
  146 pages would have left every one of them undiscoverable, with nothing to
  report it — and would have quietly undermined Index Watch, whose whole
  subject is discovery. The sitemap is now generated from what is on disk;
  `--check` fails a pull request when the two disagree. It reproduces the
  hand-maintained file exactly, reordered alphabetically.

### The gate is not the agent's to move

`metrics.py` decides publishability: match rate ≥ 0.85, ≥ 2 eligible years,
≥ 10 pooled grantees, latest year within 3. The rubric fails the run if any of
those constants, or the asset band, is touched. Reaching a page count by
loosening the bar is the exact failure this product exists to prevent, so it
is graded rather than trusted.

Roughly 30% of newly built foundations fail the gate and stay unpublished. The
rubric requires that number in the pull request body. Reporting only what
cleared would misrepresent how selective the dataset is.

### First run is slower

No committed document carries the `index_max_year` mark yet, so the first
incremental run rebuilds all 118 once to stamp them. Subsequent runs reuse.

---

## Evidence-Led Note Writer

Monthly. Finds a claim the data supports and drafts a note in the site's
voice.

The interesting part is the gate. A model writing about a dataset produces
statistics that are plausible, well-formed, and occasionally invented, and
reading the draft does not catch it — a fabricated median looks exactly like a
real one. So the draft is not the deliverable. The draft **plus a claims
file** is, where every number in the prose is paired with an expression that
computes it, and `standing/checks/figure_provenance.py` independently
recomputes each one against the committed data.

That inverts the burden. Rather than a reviewer trying to spot the invented
figure, an invented figure has no expression that yields it.

```
python3 standing/checks/figure_provenance.py draft.md claims.json
```

- A number in the prose with no claim → fail.
- A claim whose expression touches no data (`"expr": "7"`) → fail.
- A claim that recomputes to something else → fail, with both values printed.
- Spelled-out figures count. "Thirty of the pages" is as much a claim as "30".
  (`one` is exempt — in English it is almost always structural, and demanding
  a derivation for "one of the" would only produce worse prose.)

Tolerance comes from the precision written: `33%` accepts anything rounding to
33%, `0.3236` demands four places. Stating a figure more precisely is what
tightens the check.

The rubric also treats **publishing nothing as a pass**, provided the run says
what it examined and why each candidate was rejected. A monthly cadence with
no escape hatch is how a thin finding gets shipped to have something to ship.

---

## Index Watch — prerequisites

The agent is written and applies cleanly. It has nothing to read from yet.

1. **Verify the property in Google Search Console.** Nothing in the repo does
   this today — no verification meta tag, no `google*.html` file. Either add
   the meta tag to `index.html` or use DNS TXT verification. Then submit
   `https://ulrichmonthe.com/sitemap.xml`.
2. **Create a vault and add two credentials.** Both are
   `environment_variable` credentials, substituted at egress — the sandbox
   sees an opaque placeholder, never the secret:

   | Secret name | For | Allowed hosts |
   |---|---|---|
   | `GSC_ACCESS_TOKEN` | Search Console API bearer token | `searchconsole.googleapis.com`, `www.googleapis.com`, `oauth2.googleapis.com` |
   | `UMAMI_API_KEY` | `x-umami-api-key` header | `api.umami.is`, `cloud.umami.is` |

3. **Attach the vault** to the deployment (`vault_ids`), then unpause it.

Until step 1 is done there is no coverage data to read, and the report would
be two sentences saying so every week. Leave the deployment paused.

---

## GitHub access

Coverage Expander and Note Writer both open pull requests, which needs two
separate things:

- A **`github_repository` session resource** with a fine-grained PAT
  (`Contents: Read and write`) — this mounts the repo and authenticates
  `git push`. The token is injected by an Anthropic-side git proxy after the
  request leaves the sandbox; code running in the container cannot read it.
- The **GitHub MCP server**, declared on the agent, with its OAuth credential
  in a vault. The repository mount gives filesystem and git access only —
  opening the pull request itself is an MCP tool call.

Both are required. A mount without MCP can push a branch and then has no way
to open the pull request.

---

## Budgets

Every deployment carries a hard cap, in cents, on list-priced spend:

| Agent | Cap | Why |
|---|---|---|
| Coverage Expander | $12.00 | Long sessions — index rebuild plus several hundred filings fetched and parsed. Runtime dominates. |
| Note Writer | $6.00 | Reads the dataset, drafts, iterates against the gate. |
| Index Watch | $3.00 | A handful of API reads and a report. |

A session that reaches its cap **pauses** rather than terminating — it goes
idle with `stop_reason: budget_reached`, keeping its history and sandbox. Raise
or remove the budget to resume, or leave it and read what it got done. Start
here and adjust from the first month's actual figures rather than guessing
upward.

---

## Running one by hand first

Do this before trusting any of them on a schedule. Create a session against
the agent, send the same instruction the deployment would, and watch it in the
console:

```
ant beta:sessions create \
  --agent "$AGENT_COVERAGE_EXPANDER" \
  --environment-id "$ENV_ENVIRONMENT" \
  --title "manual: expand to 400"
# then open https://platform.claude.com/workspaces/<workspace>/sessions/<id>
```

Start the Coverage Expander at a depth of 400 rather than the scheduled 250-
rank step. That is the expansion already validated end to end here, so a
disagreement between its result and the numbers in this file is a signal worth
chasing.
