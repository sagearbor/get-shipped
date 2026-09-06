# get-shipped — orchestrator repo

This repo does not contain product code. It is the control tower for finishing
the repos that live beside it in `../` and getting them into production
(app store, website, web extension, crypto network, publication).

## What lives here
- `state/projects.json` — **single source of truth for judgment**: rank,
  hands_off, percent, eta_days, remaining, blocked_on_user, and the
  `estimates` ledger. Hand-edit this, then run `scripts/sync.py --write`.
- `PRIORITIES.md`, `STATUS.md`, `docs/data.json`, `state/history.json` —
  **generated** by `scripts/sync.py --write`. Never hand-edit.
- `docs/index.html` — the GitHub Pages dashboard (reads `docs/data.json`).
  Live at https://sagearbor.github.io/get-shipped/
- `INVENTORY.md` — slow-moving profile of every sibling repo (purpose, stack,
  target, infra). Hand-written; update when a repo's nature changes.
- `projects/<repo>.md` — per-project ship plan: goal, definition of shipped,
  ordered work items, open questions, running log.
- `.claude/skills/sync/SKILL.md` — `/sync`, the session-start routine.
- `tmp/` (gitignored) — hlists, wrapups, scratch.

## Hands-off repos
Some repos are being driven personally by the user in their own CC sessions.
Do **not** edit them from here unless the user explicitly says so in the
current conversation. They stay in the inventory/priority list for context only.
Current hands-off list is marked `HANDS-OFF` in `PRIORITIES.md`.

## How to work on a sibling repo
1. `cd ../<repo>` and read ITS `CLAUDE.md` / `AGENTS.md` first. Its
   conventions override anything here.
2. Check `git status` and `git log -5` before touching anything. Pull if behind.
3. Work on a branch (`feat/...`, `fix/...`), open a PR with `gh pr create`,
   never commit straight to `main` unless that repo's own conventions say so.
4. Run that repo's tests/lint before declaring anything done.
5. When done with a work item, append a dated line to the **Log** section of
   `projects/<repo>.md` here (what changed, PR link, what's next), and update
   the % / blockers in `INVENTORY.md`.
6. Ephemeral output (hlists, wrapups) for a sibling repo goes in THAT repo's
   `tmp/`. Orchestrator-level wrapups go in this repo's `tmp/wrapups/`.

## Session routine
- Start: run `/sync` (= `scripts/sync.py --write`). Read the delta. Sibling
  repos are the truth; this repo only caches them. If a sibling's newest
  wrapup or commits contradict `projects/<repo>.md`, fix the plan first.
- Pick the top non-hands-off item with an unblocked next step unless the user
  names one.
- End: update `projects/<repo>.md` log, `state/projects.json` (percent,
  remaining, estimate actuals), run `scripts/sync.py --write`, commit + push
  here so the dashboard updates.

## Estimates and calibration (the user is worried about "3 days" becoming "2 months")
- Before starting any work item, add an entry to that repo's `estimates` in
  `state/projects.json`: `{date, scope, est_days}`. Estimate in focused
  agent working days for the orchestrator's share only; list user-gated
  steps under `blocked_on_user`, never inside the estimate.
- When the item is done (verified, see below), fill `done` (date) and
  `actual_days` (agent working days actually spent, honestly, including
  debugging). Never delete or rewrite a past estimate; add a new entry if
  scope changed and say so in the scope text.
- The dashboard computes a slip factor from finished entries and applies it
  to open ETAs. Quote the calibrated number to the user, not the raw one,
  once the factor exists.
- If an item is at 2× its estimate and not done, stop and report; do not
  quietly keep going.

## Verification before "done"
- A work item is done only when the orchestrator has run a check that would
  fail if the feature were broken: the repo's test suite plus a targeted test
  for the change, and for UI/extension/mobile work an actual run (emulator,
  `claude-in-chrome` on the built extension, `flutter test` + integration
  test, curl against the deployed endpoint). Write the command and its result
  in the project log line.
- "Builds" and "compiles" are not verification. A user-only step (click
  Promote, test on VPN) is recorded as `blocked_on_user`, with what exactly
  to do and what result to report back.
- Prefer adding a regression test in the sibling repo over a manual check
  when the repo has a test suite.

## Conventions
- Percent-complete is toward *shipped*, not toward "code written".
- "Shipped" is defined per project in `PRIORITIES.md`; don't redefine it.
- Prefer small, mergeable PRs in the target repo over long-lived branches.
- Secrets never enter this repo. Note *which* env vars a repo needs in its
  project file, never their values.
