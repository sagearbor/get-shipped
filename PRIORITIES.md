# PRIORITIES — generated from `state/projects.json` at 2026-09-08T02:39
_Edit `state/projects.json` (rank, hands_off, percent, eta_days, remaining, estimates), then `scripts/sync.py --write`. Prose plans live in `projects/<repo>.md`._

## Ranked
1. **mindshift** — **HANDS-OFF** (user drives it personally; do not edit from here unless told in-session) — 80%
   - goal: AI empathy/tone coach with live-call nudges; user is driving this personally
   - shipped means: see `projects/mindshift.md`
   - [ ] Owner runs manual nudge checks, then server deploy + OTA
   - [ ] Shouting voice-identity miss
   - [ ] Activation classifier retrain
   - needs user: everything: hands-off

2. **contextflow** — 74%, ETA ~9 agent-days
   - goal: Demo-ready for companies: annual training on long PDFs, with org results in the cloud and org billing
   - shipped means: see `projects/contextflow.md`
   - [ ] Fix embedded/intranet PDF failure (intranet LMS, VPN only)
   - [ ] Persist per-user quick results for org customers + minimal org report/CSV
   - [ ] Distinct Stripe path for orgs: per-seat annual, seat enforcement
   - [ ] Triage 10+ unmerged feat/* branches
   - [ ] Bump version and submit to Chrome Web Store
   - needs user: Run `STRIPE_SECRET=sk_test_xxx PRICE_PER_SEAT_USD=96 npm --prefix contextflow-backend run setup-stripe-org-product` to actually create the test-mode S; Set STRIPE_ORG_ANNUAL_PRICE_ID as a runtime env var / secret for createOrgCheckoutSession once the price id above exists.; Set orgs/{domain}.adminKey by hand for any org that wants the getOrgTrainingReport CSV (same manual step as joinCode today).

3. **faculty-adequacy** — **HANDS-OFF** (user drives it personally; do not edit from here unless told in-session) — 30%
   - goal: Full draft covering all US med schools + paper stubbed for handoff to a co-author; refresh for a new year of data
   - shipped means: see `projects/faculty-adequacy.md`
   - [ ] Extraction is the bottleneck: 46 curated schools yield zero Tier A
   - [ ] 12 schools with roster but no curriculum URL
   - [ ] Fill manuscript placeholders in docs/manuscript.md
   - [ ] make annual-run for the new data year
   - needs user: everything: hands-off

4. **FitRival** — 76%, ETA ~8 agent-days
   - goal: Good enough for two family members to lose weight together: shared weight and %fat curves, gamification, seeing each other
   - shipped means: see `projects/FitRival.md`
   - [ ] Promote to Play production (target-API branch, full test run, release)
   - [ ] Walk second-user onboarding as a new user; fix every developer-only step
   - [ ] Verify two-user rolling-average weight and %fat curves; add goal lines
   - [ ] Firebase Auth instead of group secret, if onboarding needs it
   - [ ] Streak + head-to-head challenge card on home
   - needs user: PLAY UPLOAD + PRODUCTION PROMOTION (blocked here, your click): restore ~/fitrival-upload-keystore.jks + app/android/key.properties and ~/.config/play/; CLEANUP: delete test rows from the production Sheet — group OVERNIGHT-TEST-0907 (id 675c3043-ee42-4781-b43d-1cb0d77accaf), users Sophie/Sis/Bro with *; PR #53 (Firebase backend, your PR) left untouched — not needed for promotion; decide separately.

5. **openline** — 60%, ETA ~12 agent-days
   - goal: Give to 5 friends, have them run nodes, and prove a payment settles in seconds, comparable to a credit card
   - shipped means: see `projects/openline.md`
   - [ ] Deploy one always-on public seed node (Fly/Cloud Run) with persistence
   - [ ] Multi-node networking: nodes discover each other and share the ledger (today: single process)
   - [ ] Friend install path: one-page guide + prebuilt mobile app (Expo EAS) pointing at the seed node
   - [ ] Measure real end-to-end payment latency across nodes; publish the number
   - [ ] Personhood: deploy the credential issuer so friends can enroll
   - needs user: Deploy the always-on seed node so friends can reach it. Cheapest: on this Mac, `cd cmd/openline-node && OPENLINE_GENESIS_SEED=<pick-a-secret> OPENLINE; Docker is not installed on this Mac, so the rebuilt Dockerfile is verified statically only. To verify: `brew install colima docker && colima start`, t; Remote friends on Expo Go need either the same Wi-Fi as whoever runs `npx expo start`, or `npx expo start --tunnel` (requires a free Expo account logi

5. **personhood** — 65%
   - goal: Proof-of-personhood credential issuer that OpenLine consumes; shipped together with openline
   - shipped means: see `projects/personhood.md`
   - [ ] Deploy issuer (fly.toml, vercel.json exist)
   - [ ] Merge or drop feat/email-tier, feat/phone-carrier-tier, feat/paid-billing-card
   - needs user: Deploy is still an owner-only step (unchanged from last night): install flyctl+vercel CLI, fly auth login, vercel login, SendGrid key OR Gmail app pas

6. **chatnbook** — 40%, ETA ~15 agent-days
   - goal: Live and useful enough to sell to small companies with chatbots that can't handle AI
   - shipped means: see `projects/chatnbook.md`
   - [ ] Reality check: docker-compose up, one booking end to end
   - [ ] P7-2..P7-4: adapter generator compile, plugin volume mount, e2e WP test
   - [ ] Host the API
   - [ ] Stripe Checkout for one plan
   - [ ] One pilot customer
   - needs user: Pilot customer; Hosting + Stripe accounts

## Unranked (live or parked; touch only when asked)
| repo | % | live | goal |
|---|---|---|---|
| Medschool_ArborTester | 60 | no (hosted_url null) | Med board exam AI tutor |
| ai-ubi-wellbeing-transition-simulator | 88 | yes | UBI transition simulator (conference demo) |
| arborlife-webpage | 90 | yes | Personal site + AI job-fit matcher |
| career-compass | 85 | installable | Claude Code plugin: job posting to gap analysis + CV |
| career-compass-starter | 100 | yes | Template workspace for career-compass |
| contextFlow-upgrade | 95 | yes | ContextFlow pricing/privacy/support micro-site (satellite of contextflow, not legacy) |
| megaCity-rotating | 70 | yes | Three.js rotating megacity visualization |
| movieScript_firstAI | 0 | no | Empty repo, never started |
| neighborhood-poker | 90 | yes | Google Sheets poker tournament manager |
| oralhistory_timeline | 82 | partial (Play internal) | Oral history to interactive shareable timeline |
| sagearbor.github.io | 100 | yes | User site root: FitRival landing + privacy policy |
| taskcaster-app | 82 | web | Party game app; web MVP live, mobile stores not wired |

