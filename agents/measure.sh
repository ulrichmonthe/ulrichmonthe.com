#!/usr/bin/env bash
# What one session actually cost.
#
# The budget caps in deploy.sh were guessed, not derived. This reads the real
# figure off a completed session so they can be set from evidence instead.
#
#   ./agents/measure.sh sesn_01ABC...
#
# `list_cost` is consumption priced at public list rates — model tokens at each
# served model's price, web searches at $10 per 1,000, and session running time
# at $0.08/hour. It is not your invoice: with negotiated rates the billed
# figure is lower. It is the right number here because it is exactly what the
# budget cap is compared against.
#
# Run this once the session is idle. A session still running reports partial
# usage, which would set the cap too low.

set -euo pipefail
SESSION="${1:-}"
[[ -z "$SESSION" ]] && { sed -n '2,18p' "$0" | sed 's/^#\ \?//'; exit 2; }
command -v ant >/dev/null || { echo "ant CLI not found"; exit 1; }

json=$(ant beta:sessions retrieve --session-id "$SESSION" --format json)

SESSION_JSON="$json" python3 - <<'PY'
import json, os

s = json.loads(os.environ["SESSION_JSON"])
u = s.get("usage") or {}
cost = (u.get("list_cost") or {}).get("amount")

print(f"session   {s.get('id')}")
print(f"status    {s.get('status')}")
title = s.get("title")
if title:
    print(f"title     {title}")

if s.get("status") == "running":
    print("\nStill running — usage below is partial. Re-run when it goes idle.")

print()
for label, key in (("input tokens ", "input_tokens"),
                   ("output tokens", "output_tokens"),
                   ("cache reads  ", "cache_read_input_tokens"),
                   ("cache writes ", "cache_creation_input_tokens")):
    if u.get(key) is not None:
        print(f"  {label}  {u[key]:>12,}")

secs = u.get("active_seconds")
if secs is not None:
    print(f"  active time    {secs/60:>9.1f} min   (${secs/3600*0.08:.3f} at $0.08/hr)")

st = u.get("server_tool_use") or {}
if st.get("web_search_requests"):
    n = st["web_search_requests"]
    print(f"  web searches   {n:>12,}   (${n/1000*10:.2f} at $10/1k)")

if cost is None:
    print("\nNo list_cost reported. If this session predates budget support, or the "
          "model has no list price, there is nothing to measure — set the cap by "
          "hand.")
    raise SystemExit(0)

dollars = int(cost) / 100
print(f"\n  list cost      ${dollars:>11.2f}")

# A figure is only worth deriving a cap from if the session ran to completion
# without being stopped. Both exclusions below produce a floor rather than a
# cost, and tripling a floor would bake the error into the cap.
truncated = s.get("status") == "running"
reason = "the session is still running" if truncated else None

budget = s.get("budget")
if budget:
    cap = int(budget["max_list_cost"]["amount"]) / 100
    pct = 100 * dollars / cap if cap else 0
    print(f"  cap in force   ${cap:>11.2f}   ({pct:.0f}% used)")
    if pct >= 99:
        truncated = True
        reason = "the run hit its cap and paused before finishing"

if truncated:
    print(f"\nNo cap suggested — {reason}, so the figure above is a floor, not a "
          "cost.\nRaise the cap or let it finish, then measure again.")
    raise SystemExit(0)

# 3x headroom, rounded up to the next dollar. Enough for a heavier week —
# more filings, more gate failures to write up — without being so loose that
# a runaway session goes unnoticed.
import math
suggest = max(1, math.ceil(dollars * 3))
print(f"\nsuggested cap  ${suggest}.00  (3x measured, rounded up)")
print(f'  in agents/deploy.sh, set the last argument of the deploy call to "{suggest * 100}"')
PY
