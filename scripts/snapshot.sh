#!/usr/bin/env bash
# Regenerate a git-state snapshot of every sibling repo in ../
# Usage: scripts/snapshot.sh            -> prints markdown table
#        scripts/snapshot.sh > tmp/snapshot-$(date +%Y%m%d).md
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
echo "# Sibling repo snapshot — $(date '+%Y-%m-%d %H:%M %Z')"
echo
echo "| repo | last commit | commits | branch | dirty | unpushed | remote |"
echo "|---|---|---|---|---|---|---|"
for d in "$ROOT"/*/; do
  d=${d%/}; name=$(basename "$d")
  [ "$name" = "get-shipped" ] && continue
  [ -d "$d/.git" ] || { echo "| $name | (no git) | | | | | |"; continue; }
  last=$(git -C "$d" log -1 --format=%ad --date=short 2>/dev/null || echo "-")
  n=$(git -C "$d" rev-list --count HEAD 2>/dev/null || echo 0)
  br=$(git -C "$d" symbolic-ref --short -q HEAD 2>/dev/null || echo "(empty)")
  dirty=$(git -C "$d" status --porcelain 2>/dev/null | wc -l | tr -d ' ')
  up=$(git -C "$d" rev-list --count @{u}..HEAD 2>/dev/null || echo "?")
  remote=$(git -C "$d" remote get-url origin 2>/dev/null | sed -E 's#.*github.com[:/]##; s#\.git$##' || echo "-")
  echo "| $name | $last | $n | $br | $dirty | $up | $remote |"
done
