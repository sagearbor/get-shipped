# PRIORITIES — generated from `state/projects.json` at 2026-09-17T07:16
_Edit `state/projects.json` (rank, hands_off, percent, eta_days, remaining, estimates), then `scripts/sync.py --write`. Prose plans live in `projects/<repo>.md`._

## Ranked
1. **mindshift** — 80%
   - goal: AI empathy/tone coach with live-call nudges; user is driving this personally; owner asked 2026-09-17 to complete agentically, too busy to drive personally
   - shipped means: see `projects/mindshift.md`
   - [ ] Owner runs manual nudge checks, then server deploy + OTA
   - [ ] Shouting voice-identity miss
   - [ ] Activation classifier retrain
   - needs user: everything: hands-off

2. **contextflow** — 82%, ETA ~9 agent-days
   - goal: Demo-ready for companies: annual training on long PDFs, with org results in the cloud and org billing
   - shipped means: see `projects/contextflow.md`
   - [ ] Owner uploads v0.1.48 zip to Chrome Web Store
   - [ ] Set STRIPE_ORG_SECRET (test) + price id; deploy stripeWebhook while watching
   - [ ] Owner runs __cfDiagnosePDF() on VPN
   - needs user: CHROME WEB STORE UPLOAD (owner-only, I never touch a store account). The zip is already built at /Users/sagearbor/projects/githubs/contextflow/extensi; ENABLE ORG BILLING IN TEST MODE (3 steps, in order). (1) Create the product/price with a Stripe TEST key: `cd contextflow-backend && STRIPE_SECRET=sk_; DEPLOY stripeWebhook YOURSELF WHEN YOU CAN WATCH IT. I deliberately did not deploy it: it processes LIVE individual payments, and my change adds event

3. **faculty-adequacy** — **HANDS-OFF** (user drives it personally; do not edit from here unless told in-session) — 88%
   - goal: Full draft covering all US med schools + paper stubbed for handoff to a co-author; refresh for a new year of data
   - shipped means: see `projects/faculty-adequacy.md`
   - [ ] Co-author reviews docs/manuscript_CHANGES_2026-09-15.md (one conclusion changed: rho -0.44)
   - [ ] 12 external-seeded schools never tier-classified (4,173 records): queue Phase 3
   - [ ] Policy: role-only evidence toward Tier A
   - [ ] UCLA/Hopkins full harvests
   - [ ] Journal submission; annual-run next data year
   - needs user: Co-author review: section 6 now reports a NON-NULL negative correlation between teaching-evidenced share and evidence coverage (rho -0.44 [-0.63,-0.19; Co-author decision: old Table 4's six-class roster-failure taxonomy was dropped (its premise, '34 schools without a roster', is now false -- only 5 ar; 12 schools (4,173 records) still owe a Phase 3 identity pass and are labelled 'pending'; the manuscript rests on 187 of 204 schools until that runs. E

4. **FitRival** — 76%, ETA ~8 agent-days
   - goal: Good enough for two family members to lose weight together: shared weight and %fat curves, gamification, seeing each other
   - shipped means: see `projects/FitRival.md`
   - [ ] Promote to Play production (target-API branch, full test run, release)
   - [ ] Walk second-user onboarding as a new user; fix every developer-only step
   - [ ] Verify two-user rolling-average weight and %fat curves; add goal lines
   - [ ] Firebase Auth instead of group secret, if onboarding needs it
   - [ ] Streak + head-to-head challenge card on home
   - needs user: PLAY UPLOAD + PRODUCTION PROMOTION (blocked here, your click): restore ~/fitrival-upload-keystore.jks + app/android/key.properties and ~/.config/play/; CLEANUP: delete test rows from the production Sheet — group OVERNIGHT-TEST-0907 (id 675c3043-ee42-4781-b43d-1cb0d77accaf), users Sophie/Sis/Bro with *; PR #53 (Firebase backend, your PR) left untouched — not needed for promotion; decide separately.

5. **openline** — 80%, ETA ~12 agent-days
   - goal: Give to 5 friends, have them run nodes, and prove a payment settles in seconds, comparable to a credit card
   - shipped means: see `projects/openline.md`
   - [ ] Deploy one always-on public seed node (Fly/Cloud Run) with persistence
   - [ ] Multi-node networking: nodes discover each other and share the ledger (today: single process)
   - [ ] Friend install path: one-page guide + prebuilt mobile app (Expo EAS) pointing at the seed node
   - [ ] Measure real end-to-end payment latency across nodes; publish the number
   - [ ] Personhood: deploy the credential issuer so friends can enroll
   - needs user: Send a friend the link. They need the Personhood invite code, which is deliberately NOT in the repo: gcloud run services describe personhood-issuer --; Cosmetic, worth fixing before sharing widely: the wallet's Receive button is clipped at 390px width (Send/Receive row overflows). Seen in the headless; Cost note: the seed node runs min-instances=0 / max-instances=1, so it idles free and cold-starts in about a second. max-instances MUST stay 1 - two i

5. **personhood** — 88%
   - goal: Proof-of-personhood credential issuer that OpenLine consumes; shipped together with openline
   - shipped means: see `projects/personhood.md`
   - [ ] Deploy issuer (fly.toml, vercel.json exist)
   - [ ] Merge or drop feat/email-tier, feat/phone-carrier-tier, feat/paid-billing-card
   - needs user: BACK UP THE ISSUER KEY (root of trust; rotating it invalidates every credential): gcloud secrets versions access latest --secret=personhood-issuer-key; Give friends the invite code friends-OrXX8NXwFvAK (not committed anywhere; lives only in this status file and the Cloud Run env). Rotate: gcloud run s; Test mode caveat: with DEV_EXPOSE_CHALLENGE_SECRETS=1 anyone holding the invite code can 'verify' ANY email address. Fine for 5 trusted friends, not f

6. **chatnbook** — 74%, ETA ~15 agent-days
   - goal: Live and useful enough to sell to small companies with chatbots that can't handle AI
   - shipped means: see `projects/chatnbook.md`
   - [ ] Reality check: docker-compose up, one booking end to end
   - [ ] P7-2..P7-4: adapter generator compile, plugin volume mount, e2e WP test
   - [ ] Host the API
   - [ ] Stripe Checkout for one plan
   - [ ] One pilot customer
   - needs user: CI's `test` job ('Full test suite (pytest + TS + adapter-gen)' step in .github/workflows/ci.yml) hangs reproducibly (3/3 attempts) right after package; tmp/cloudrun-secrets.env (repo-root tmp/, gitignored, chmod 600) now holds the live service's AGENT_HMAC_SECRET/TOKEN_ENCRYPTION_KEY/ADMIN_API_KEY, pu

## Unranked (live or parked; touch only when asked)
| repo | % | live | goal |
|---|---|---|---|
| Medschool_ArborTester | 60 | no (hosted_url null) | Med board exam AI tutor |
| ai-ubi-wellbeing-transition-simulator | 92 | yes | UBI transition simulator (conference demo); user is driving this personally in their own sessions (2026-09-10) |
| arborlife-webpage | 90 | yes | Personal site + AI job-fit matcher |
| career-compass | 85 | installable | Claude Code plugin: job posting to gap analysis + CV |
| career-compass-starter | 100 | yes | Template workspace for career-compass |
| contextFlow-upgrade | 95 | yes | ContextFlow pricing/privacy/support micro-site (satellite of contextflow, not legacy) |
| megaCity-rotating | 70 | yes | Three.js rotating megacity visualization |
| movieScript_firstAI | 0 | no | Empty repo, never started |
| neighborhood-poker | 90 | yes | Google Sheets poker tournament manager |
| oralhistory_timeline | 84 | partial (Play internal) | Oral history to interactive shareable timeline |
| sagearbor.github.io | 100 | yes | User site root: FitRival landing + privacy policy |
| taskcaster-app | 94 | https://taskmaster-app-3d480.web.app | Addictively fun, near-zero-friction Taskmaster-style play that works apart: async loop, auto-edit, reveal gating, crowd grading with ads as the model (owner direction 2026-09-12) |

