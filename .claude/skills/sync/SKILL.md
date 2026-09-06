---
name: sync
description: Resume the orchestrator — regenerate STATUS.md from every sibling repo in ../ (git state, newest wrapups, optional open PRs) and report what moved since the last visit here. Run at the start of every get-shipped session or when the user says "sync", "what changed", "resume", "where are we".
---

# /sync — resume the orchestrator

1. Run `scripts/sync.py --write` (add `--prs` if the user wants GitHub PR state
   and network is fine). This rewrites `STATUS.md` and stamps `state/last-sync`.
2. Read the **Delta since last sync** section. For each repo that moved, decide
   whether the hand-written judgment in `PRIORITIES.md` / `projects/<repo>.md`
   is now wrong (a wrapup's `next_steps` supersede the project file's plan if
   newer). Update those files; keep edits minimal and dated.
3. Reply to the user with, in this order:
   - what moved since last visit (repo, one line each, from the delta)
   - anything alarming: dirty trees, unpushed commits, hands-off repos with
     unmerged PRs the user may have forgotten
   - the top 3 non-HANDS-OFF items from `PRIORITIES.md` with their next
     unblocked step
4. Commit `STATUS.md` + `state/last-sync` + any judgment edits here
   (`chore(sync): YYYY-MM-DD`). Push.

Never edit sibling repos during /sync; it is read-only toward `../`.
