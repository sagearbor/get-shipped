# PRIORITIES — generated from `state/projects.json` at 2026-10-05T01:01
_Edit `state/projects.json` (rank, hands_off, percent, eta_days, remaining, estimates), then `scripts/sync.py --write`. Prose plans live in `projects/<repo>.md`._

## Ranked
1. **mindshift** — 83%
   - goal: AI empathy/tone coach with live-call nudges; user is driving this personally
   - shipped means: see `projects/mindshift.md`
   - [ ] Install watch APK (needs owner's device IP:port)
   - [ ] Decide whether to enable the valence veto: shadow-log first with MINDSHIFT_TONE_AUDIO=on, gate off
   - [ ] PR #185 blocked on a real test-collection bug (two dirs both import as module 'tests'); owner decision on layout
   - [ ] Merge order still #183 (3wk stale CI) then #185, independent: #184; #173 has conflicts
   - [ ] gpt-audio labeller needs credits; real-voice validation needs owner's own recordings
   - needs user: Install watch APK: apps/watch/wearApp/build/outputs/apk/debug/wearApp-debug.apk; Re-run PR #183 CI then merge (android changes into a live health app, not done unattended); Decide test-layout fix for PR #185's collection failure

2. **contextflow** — 85%, ETA ~9 agent-days
   - goal: Demo-ready for companies: annual training on long PDFs, with org results in the cloud and org billing
   - shipped means: see `projects/contextflow.md`
   - [ ] URGENT: purge confirmed-leaked docs via contextflow-backend/functions/scripts/purge-cached-page.js
   - [ ] Submit v0.1.49 to Chrome Web Store (fixes don't protect installed clients until then)
   - [ ] Wire the existing background/index.js privacy blacklist into the cache-write gate too (gap found: keep.google.com/messages.google.com were cached despite being on that list)
   - [ ] Org-level content control (Phase 2, scoped): org registers domain+optional-path rules; only that org's own enrolled employees skip shared cache there
   - [ ] Set STRIPE_ORG_SECRET (test) + price id; deploy stripeWebhook while watching
   - needs user: Confirm go-ahead to run the purge script now (irreversible delete of leaked docs); CHROME WEB STORE UPLOAD of v0.1.49; Stripe test key + price id

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
| mosaicHighRes | 88 | Signed v1.2.5 APK delivered (sideload); privacy policy live; one Play Console session from submission | Print-quality (up to 1200 DPI, lossless) photo mosaic app for iOS/Android, fully on-device so it ships free, no backend |
| movieScript_firstAI | 0 | no | Empty repo, never started |
| neighborhood-poker | 90 | yes | Google Sheets poker tournament manager |
| oralhistory_timeline | 84 | partial (Play internal) | Oral history to interactive shareable timeline |
| sagearbor.github.io | 100 | yes | User site root: FitRival landing + privacy policy |
| taskcaster-app | 94 | https://taskmaster-app-3d480.web.app | Addictively fun, near-zero-friction Taskmaster-style play that works apart: async loop, auto-edit, reveal gating, crowd grading with ads as the model (owner direction 2026-09-12) |

