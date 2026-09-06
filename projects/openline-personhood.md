# openline + personhood — ship plan

**Repos:** `../openline` (protocol + `cmd/openline-node` + Expo mobile) and
`../personhood` (credential issuer openline consumes). One plan, one ETA.

## Goal (user's words)
Give it to 5 friends, have them start nodes, and prove a payment can be made
in seconds, comparable to a credit card.

## Definition of shipped
1. One always-on public seed node with persistence that survives restarts.
2. Five friends have the mobile app installed (EAS build or Expo Go link)
   and each holds a wallet funded from the Commons pool.
3. At least two nodes besides the seed run by friends, sharing one ledger.
4. A measured, published number: median end-to-end payment latency between
   two phones through the network, with the measurement script in the repo.
5. Personhood issuer deployed; each friend enrolled once.

## Current state (2026-09-06)
- `cmd/openline-node` is a single-process, in-memory, custodial prototype
  with optional JSON persistence. Real UTXO tx + VRF committee logic runs
  inside the one process. Verified on an Android emulator (`EMULATOR_E2E.md`).
- The "sub-2-second" figure is a whitepaper simulation target, not measured.
- No multi-node networking deployed. Testnet Docker tooling exists.
- personhood has Dockerfile, `fly.toml`, `vercel.json`, CI, `RUNBOOK.md`; every
  URL is a placeholder. Unmerged: `feat/email-tier`, `feat/phone-carrier-tier`,
  `feat/paid-billing-card`, `feat/mobile-capacitor-scaffold`.

## Work items (ordered)
1. Seed node on Fly or Cloud Run with a volume; health endpoint; one-page
   `FRIENDS.md` (install app, get funded, send to a friend).
2. Decide round-1 scope with the user: friends as *wallet users only* first
   (fast), nodes second. Recommendation: wallets first, prove latency, then
   nodes.
3. Multi-node: gossip + ledger sync between two Docker nodes on separate
   hosts; committee across hosts. This is the unknown-size item.
4. Latency harness: script sends N payments phone→node→phone, records p50/p95.
5. Deploy personhood issuer with only the email tier for round 1.

## Env needed (names only)
Hosting account; `OPENLINE_STATE_PATH`; personhood `SENDGRID_*`, `TURNSTILE_*`,
`APP_ATTEST_SECRET` (email tier only).

## Log
- 2026-09-06 — plan created from repo profiling; no code touched.
