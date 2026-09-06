# chatnbook — ship plan

**Repo:** `../chatnbook` (pnpm/Turborepo: TS API, Python connectors, widget,
MCP adapter, generated WordPress plugin). Last commit 2025-08-12.

## Goal (user's words)
Useful enough, and live, to try selling to small companies whose chatbots
can't handle AI.

## Definition of shipped
1. Hosted API (one small VPS or Fly/Render) with Postgres + Redis, HTTPS.
2. A WordPress plugin zip a non-developer can install that shows the chat +
   booking widget and completes a real booking against Google Calendar.
3. One paid plan via Stripe Checkout (even if seats are hand-provisioned).
4. One pilot customer (a friend's small business) using it for a week.

## Current state (from repo profiling, 2026-09-06)
- `plan.yaml` marks P0–P6 done, but the API core is ~130 LOC
  (`packages/api/src/index.ts`, `notify.ts`) so "done" means scaffolded.
- P7 open: adapter-generator TypeScript compile (P7-2), docker plugin volume
  mount (P7-3), end-to-end WordPress test (P7-4).
- Stripe env vars exist (`.env.example`) but no billing logic; `docs/mvp.md`
  lists payments as a non-goal.
- No hosting config beyond `infra/docker-compose.dev.yml`; no live URL.
- Estimated 35–40% to sellable. This is the furthest from the line of the
  named priorities.

## Work items (ordered)
1. **Reality check (half day).** Bring up docker-compose, run the WP test
   site, try one booking end to end. Write down what actually works.
2. Fix P7-2..P7-4 so the WordPress plugin is generated, installed, and tested.
3. Deploy API to one host; point plugin at it.
4. Stripe Checkout for a single Starter plan.
5. Recruit one pilot.

## Env needed (names only)
Postgres/Redis URLs, Google + Microsoft OAuth client IDs, AWS SES, Twilio,
OpenAI key, `STRIPE_SECRET`, `PLAN_STARTER_PRICE_ID`, HMAC secret. See `.env.example`.

## Log
- 2026-09-06 — plan created from repo profiling; no code touched.
