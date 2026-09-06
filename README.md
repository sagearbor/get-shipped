# get-shipped

Control tower for finishing the side projects that live beside this repo in
`../` and getting them into production: app stores, websites, a Chrome
extension, a payments network, a publication.

No product code lives here. Claude Code runs from this directory as an
orchestrator and works *in* the sibling repos, following each repo's own
conventions.

| file | who edits it | what |
|---|---|---|
| `PRIORITIES.md` | human judgment | ordered list, definition of *shipped* per project, HANDS-OFF flags |
| `INVENTORY.md` | human judgment (rarely) | profile of every sibling repo: purpose, stack, target, infra |
| `projects/<repo>.md` | orchestrator + human | ship plan, work items, running log |
| `STATUS.md` | **generated** by `scripts/sync.py` | git state + newest wrapup per repo, delta since last sync |
| `state/last-sync` | generated | timestamp of last sync |
| `CLAUDE.md` | human | rules for Claude Code sessions here |
| `tmp/` | gitignored | hlists, wrapups, scratch |

## Resume a session

```
cd get-shipped && claude
> /sync
```

`/sync` regenerates `STATUS.md` from every sibling repo (git log, dirty and
unpushed state, newest `tmp/wrapups/*.yaml`) and reports what changed since
this repo last looked. Sessions run in other repos need no extra step: their
git history and wrapups are picked up on the next `/sync`.

## Scripts

- `scripts/sync.py [--write] [--prs] [--repo X]` — the delta + status report
- `scripts/snapshot.sh` — quick one-table git snapshot (no wrapups)
