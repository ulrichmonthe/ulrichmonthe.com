#!/usr/bin/env bash
# Apply the agent definitions in this directory to the Claude platform.
#
# The split this follows: the CLI owns the control plane (agents, environments,
# schedules — static things that belong in version control), and sessions are
# whatever runs against them. Everything here is idempotent-ish: it creates on
# first run and records the IDs in .ids.env, then updates on subsequent runs.
#
#   ./agents/deploy.sh            create or update everything
#   ./agents/deploy.sh --dry-run  print what would be sent, change nothing
#
# Requires: ant (https://platform.claude.com/docs/en/api/sdks/cli), and either
# ANTHROPIC_API_KEY exported or `ant auth login` already run.

set -euo pipefail
cd "$(dirname "$0")/.."

DRY=0; [[ "${1:-}" == "--dry-run" ]] && DRY=1
IDS="agents/.ids.env"
TZ_NAME="America/New_York"
[[ -f "$IDS" ]] && source "$IDS"

command -v ant >/dev/null || { echo "ant CLI not found — see the URL above"; exit 1; }

say() { printf '\n\033[1m%s\033[0m\n' "$*"; }
record() { grep -v "^$1=" "$IDS" 2>/dev/null > "$IDS.tmp" || true
           echo "$1=$2" >> "$IDS.tmp"; mv "$IDS.tmp" "$IDS"; }

# ---------------------------------------------------------------- environments
for env_file in agents/environment.yaml agents/environment-analytics.yaml; do
  key="ENV_$(basename "$env_file" .yaml | tr 'a-z-' 'A-Z_')"
  existing="${!key:-}"
  say "environment: $env_file"
  if [[ $DRY == 1 ]]; then cat "$env_file"; continue; fi
  if [[ -n "$existing" ]]; then
    ant beta:environments update --environment-id "$existing" < "$env_file" >/dev/null
    echo "  updated $existing"
  else
    id=$(ant beta:environments create < "$env_file" --transform id -r)
    record "$key" "$id"; echo "  created $id"
  fi
done
[[ $DRY == 0 ]] && source "$IDS"

# ---------------------------------------------------------------------- agents
for agent_file in agents/coverage-expander.agent.yaml \
                  agents/note-writer.agent.yaml \
                  agents/index-watch.agent.yaml; do
  key="AGENT_$(basename "$agent_file" .agent.yaml | tr 'a-z-' 'A-Z_')"
  existing="${!key:-}"
  say "agent: $agent_file"
  if [[ $DRY == 1 ]]; then cat "$agent_file"; continue; fi
  if [[ -n "$existing" ]]; then
    # Version is an optimistic lock; read the current one and pass it through.
    ver=$(ant beta:agents retrieve --agent-id "$existing" --transform version -r)
    ant beta:agents update --agent-id "$existing" --version "$ver" < "$agent_file" >/dev/null
    echo "  updated $existing (now version $((ver + 1)))"
  else
    id=$(ant beta:agents create < "$agent_file" --transform id -r)
    record "$key" "$id"; echo "  created $id"
  fi
done
[[ $DRY == 0 ]] && source "$IDS"

# ----------------------------------------------------------------- deployments
# Deployments are a newer surface than the rest; older CLI builds do not expose
# them. Check before assuming.
if ! ant beta:deployments --help >/dev/null 2>&1; then
  say "NOTE: this ant build has no beta:deployments — see agents/README.md for
the raw-HTTP form. Agents and environments above are applied and usable now;
only the cron schedules are missing."
  exit 0
fi

deploy() {  # name  agent_id  env_id  cron  outcome_description  rubric_file  budget_cents
  local name="$1" agent="$2" env="$3" cron="$4" desc="$5" rubric="$6" budget="$7"
  local key="DEPLOY_$(echo "$name" | tr 'a-z -' 'A-Z__')"
  local existing="${!key:-}"
  say "deployment: $name  ($cron $TZ_NAME)"

  local body
  body=$(RUBRIC_FILE="$rubric" NAME="$name" AGENT="$agent" ENVID="$env" \
         CRON="$cron" DESC="$desc" TZNAME="$TZ_NAME" BUDGET="$budget" python3 - <<'PY'
import json, os
rubric = open(os.environ["RUBRIC_FILE"], encoding="utf-8").read() if os.environ["RUBRIC_FILE"] else None
event = ({"type": "user.define_outcome",
          "description": os.environ["DESC"],
          "rubric": {"type": "text", "content": rubric},
          "max_iterations": 5}
         if rubric else
         {"type": "user.message",
          "content": [{"type": "text", "text": os.environ["DESC"]}]})
print(json.dumps({
    "name": os.environ["NAME"],
    "agent": os.environ["AGENT"],
    "environment_id": os.environ["ENVID"],
    "initial_events": [event],
    "budget": {"type": "limit",
               "max_list_cost": {"amount": os.environ["BUDGET"], "currency": "USD"}},
    "schedule": {"type": "cron", "expression": os.environ["CRON"],
                 "timezone": os.environ["TZNAME"]},
}))
PY
)
  if [[ $DRY == 1 ]]; then echo "$body" | python3 -m json.tool; return; fi
  if [[ -n "$existing" ]]; then
    echo "$body" | ant beta:deployments update --deployment-id "$existing" >/dev/null
    echo "  updated $existing"
  else
    id=$(echo "$body" | ant beta:deployments create --transform id -r)
    record "$key" "$id"; echo "  created $id"
  fi
}

# Monday 06:00 — a full week of new filings, and the pull request is waiting
# rather than landing mid-week.
deploy "coverage-expander" "$AGENT_COVERAGE_EXPANDER" "$ENV_ENVIRONMENT" \
  "0 6 * * 1" \
  "Expand the published funder-standing cohort by 250 ranks beyond the current cohort_rank_depth in standing/data/index.json. Rebuild the filing index, run build_real.py incrementally at the new depth, rebuild the foundation pages and the sitemap, run every check, and open a pull request reporting what cleared the gate, what was withheld and why, and what moved under pages already published. If any check fails, do not open a pull request — report the failure and stop." \
  "agents/coverage-expander.rubric.md" "1200"

# Monday 08:00 — after the expansion, so a jump in page count is visible in the
# same week's reading.
deploy "index-watch" "$AGENT_INDEX_WATCH" "$ENV_ENVIRONMENT_ANALYTICS" \
  "0 8 * * 1" \
  "Read the last 28 days of Search Console coverage, impressions and queries against the 28 days before, cross-reference the analytics API, reconcile against sitemap.xml, and write the report to /mnt/session/outputs/. Say plainly where the data does not support a conclusion." \
  "" "300"

# Created paused: Search Console is not verified for the property yet and the
# vault credentials do not exist, so every firing would burn a session to
# report that it cannot read anything. Unpause once agents/README.md §
# "Index Watch prerequisites" is done:
#
#   ant beta:deployments unpause --deployment-id "$DEPLOY_INDEX_WATCH"
#
# Pausing suppresses the schedule only — a manual run still works, which is
# how to test the credentials the moment they exist.
[[ $DRY == 0 ]] && source "$IDS"     # deploy() only wrote the id to the file
if [[ $DRY == 0 && -n "${DEPLOY_INDEX_WATCH:-}" ]]; then
  state=$(ant beta:deployments retrieve --deployment-id "$DEPLOY_INDEX_WATCH" \
          --transform status -r 2>/dev/null || echo unknown)
  if [[ "$state" == "active" ]]; then
    ant beta:deployments pause --deployment-id "$DEPLOY_INDEX_WATCH" >/dev/null
    echo "  paused — blocked on Search Console (see agents/README.md)"
  fi
fi

# 1st of the month, 07:00.
deploy "note-writer" "$AGENT_NOTE_WRITER" "$ENV_ENVIRONMENT" \
  "0 7 1 * *" \
  "Find one publishable finding in the funder-standing dataset, draft a note in the site's voice with a claims file covering every figure, verify it with standing/checks/figure_provenance.py, render the page, update the sitemap and open a pull request. If no finding clears the bar this month, publish nothing and report what you examined and why each candidate was rejected." \
  "agents/note-writer.rubric.md" "600"

say "done. IDs in $IDS (gitignored)."
