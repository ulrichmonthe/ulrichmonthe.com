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
#   ./agents/deploy.sh --paused   create everything dormant; nothing fires
#
# --paused exists because the budget caps in this file are guesses. Creating
# resources costs nothing — only sessions cost — so the honest order is to
# create everything paused, run one session by hand, read what it actually
# cost with agents/measure.sh, and set the caps from that number instead of
# from an estimate. See agents/README.md § "Setting the caps from a real run".
#
# Requires: ant (https://platform.claude.com/docs/en/api/sdks/cli), and either
# ANTHROPIC_API_KEY exported or `ant auth login` already run. --dry-run needs
# neither.

set -euo pipefail
cd "$(dirname "$0")/.."

DRY=0; PAUSED=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY=1 ;;
    --paused)  PAUSED=1 ;;
    -h|--help) sed -n '2,16p' "$0" | sed 's/^#\ \?//'; exit 0 ;;
    *) echo "unknown flag: $arg (try --help)"; exit 2 ;;
  esac
done
IDS="agents/.ids.env"
TZ_NAME="America/New_York"
[[ -f "$IDS" ]] && source "$IDS"

# --dry-run only renders payloads, so it does not need the CLI or credentials.
# That makes it useful as a first check on a machine where nothing is set up.
if [[ $DRY == 0 ]]; then
  command -v ant >/dev/null || { echo "ant CLI not found — see the URL above"; exit 1; }
fi

# On a fresh checkout nothing has been created yet and .ids.env does not exist.
# Under `set -u` an unset id would abort the run, so give them all a value.
: "${ENV_ENVIRONMENT:=}" "${ENV_ENVIRONMENT_ANALYTICS:=}"
: "${AGENT_COVERAGE_EXPANDER:=}" "${AGENT_NOTE_WRITER:=}" "${AGENT_INDEX_WATCH:=}"
: "${DEPLOY_COVERAGE_EXPANDER:=}" "${DEPLOY_NOTE_WRITER:=}" "${DEPLOY_INDEX_WATCH:=}"

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
# them. Check before assuming — but not in dry-run, which renders the payloads
# without needing the CLI at all.
if [[ $DRY == 0 ]] && ! ant beta:deployments --help >/dev/null 2>&1; then
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

# Pausing suppresses the schedule only — a manual run still works, which is
# both how you test credentials and how you measure a real run's cost.
pause_deployment() {  # name-of-id-variable  reason
  local id="${!1:-}" reason="$2" state
  [[ $DRY == 1 || -z "$id" ]] && return 0
  state=$(ant beta:deployments retrieve --deployment-id "$id" \
          --transform status -r 2>/dev/null || echo unknown)
  if [[ "$state" == "active" ]]; then
    ant beta:deployments pause --deployment-id "$id" >/dev/null
    echo "  paused $id — $reason"
  fi
}

[[ $DRY == 0 ]] && source "$IDS"     # deploy() only wrote the ids to the file

# Always paused: Search Console is not verified for the property and the vault
# credentials do not exist, so every firing would spend a session reporting
# that it cannot read anything.
pause_deployment DEPLOY_INDEX_WATCH "blocked on Search Console (agents/README.md)"

if [[ $PAUSED == 1 ]]; then
  pause_deployment DEPLOY_COVERAGE_EXPANDER "--paused: measure before scheduling"
  pause_deployment DEPLOY_NOTE_WRITER      "--paused: measure before scheduling"
fi

if [[ $PAUSED == 1 && $DRY == 0 ]]; then
  cat <<GUIDE

Everything is created and dormant. Nothing will fire on a schedule.

The caps in this file ($12 / $6 / $3 per session) are guesses, not
measurements. Replace them with one real number:

  1. Run one session by hand — a manual run works while paused:
       ant beta:deployments run --deployment-id "\$DEPLOY_COVERAGE_EXPANDER"

  2. Read what it actually cost, once it goes idle:
       ./agents/measure.sh <session-id>

  3. Put a cap based on that figure into the deploy calls in this file,
     re-run ./agents/deploy.sh, then unpause:
       ant beta:deployments unpause --deployment-id "\$DEPLOY_COVERAGE_EXPANDER"

Ids are in $IDS — source it to get those variables.
GUIDE
fi

# 1st of the month, 07:00.
deploy "note-writer" "$AGENT_NOTE_WRITER" "$ENV_ENVIRONMENT" \
  "0 7 1 * *" \
  "Find one publishable finding in the funder-standing dataset, draft a note in the site's voice with a claims file covering every figure, verify it with standing/checks/figure_provenance.py, render the page, update the sitemap and open a pull request. If no finding clears the bar this month, publish nothing and report what you examined and why each candidate was rejected." \
  "agents/note-writer.rubric.md" "600"

say "done. IDs in $IDS (gitignored)."
