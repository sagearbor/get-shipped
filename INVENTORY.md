# INVENTORY — sibling repos in `../`

Profiled 2026-09-06 by three parallel read-only agents plus manual checks.
Git-state columns are live in `STATUS.md` (generated); percent/ETA live in
`state/projects.json`. This file is the slow-moving profile: what each repo
*is*. Update it when a repo's purpose, stack, or deploy target changes.

## Ranked

| repo | purpose | stack | target | live? | infra / env names |
|---|---|---|---|---|---|
| mindshift | AI empathy/tone coach; live-call nudges on phone + watch | Expo RN + web, FastAPI | App stores + Cloud Run | preview builds, OTA | Firebase `arborfam-hub`, Cloud Run, Deepgram/Whisper, multi-LLM |
| contextflow | Chrome/Firefox MV3 extension: pre-reads pages/PDFs, scroll-triggered summaries + quizzes | TS + Vite, Firebase Functions | Chrome Web Store + Firebase | built; store listing unconfirmed; Stripe live | `extension/src/config/config.ts` (gitignored) LLM keys, `LLM_PROXY_URL`, `STRIPE_CONFIG`; Firebase `contextflow-ext` |
| contextFlow-upgrade | satellite micro-site for contextflow: Stripe pricing table, privacy, support | static HTML | GitHub Pages | yes | Stripe publishable key only |
| faculty-adequacy | US med-school faculty teaching-evidence tiers A–E; pipeline + dashboard + manuscript | Python 3.11, SQLite, Playwright, Claude Code as LLM router | Publication + GitHub Pages dashboard | dashboard live | Browserbase, PubMed/ORCID keys, budget caps in `.env.example` |
| FitRival | body-comp competition with friends | Flutter, Hive, Apps Script + Sheets backend | Google Play (Android) | internal track v0.0.66; prod stale v0.0.28 | Apps Script URL + group secret, Play service account, Health Connect |
| openline | payments + voting + UBI protocol (Flurry/Suffrage/Commons/Steward); `cmd/openline-node` prototype | Go, Rust, Solidity, Circom; Expo mobile | public testnet + mobile | local prototype only | none wired; `OPENLINE_STATE_PATH`, `OPENLINE_PERSONHOOD_ENABLED` |
| personhood | proof-of-personhood credential issuer (extracted from openline 2026-05) | TS API + web | Fly.io + Vercel | deploy-ready, not deployed | Persona, Plaid, SendGrid, Twilio, Turnstile (`.example.env`) |
| chatnbook | AI-native chat + agent-ready scheduling for SMBs; WordPress plugin | pnpm/Turborepo TS API, Python connectors, PHP plugin | hosted API + WP plugin | no | Postgres, Redis, Google/MS OAuth, SES, Twilio, OpenAI, Stripe (unused) |

## Unranked

| repo | purpose | stack | target | live? | notes |
|---|---|---|---|---|---|
| taskcaster-app | party game app | Flutter + Firebase | web (live) + stores | web | 213 commits; mobile Firebase not configured; ads/IAP mock |
| oralhistory_timeline | oral histories to shareable timelines | Flutter + Firebase, Whisper | Firebase Hosting + Play | partial | README stale about branch; never run parallel flutter builds |
| arborlife-webpage | personal site + AI job-fit matcher | static + Cloudflare Worker | GitHub Pages | yes | `agent.md` stale; trust CLAUDE.md |
| career-compass | CC plugin: job posting to gap analysis/CV | CC plugin + Python | plugin marketplace | installable | pairs with career-compass-starter |
| career-compass-starter | template workspace for the plugin | markdown | GitHub template | yes | done by design |
| neighborhood-poker | poker tournament Google Sheet generator | Python + Sheets API | shared Sheet | yes | hardcoded spreadsheet id |
| megaCity-rotating | Three.js rotating megacity + AI analysis | React + R3F, Gemini | Cloud Run | yes | rotary union diagram bug |
| ai-ubi-wellbeing-transition-simulator | UBI transition simulator | React + D3, Gemini | Cloud Run | yes | conference demo; phase 8-9 open |
| Medschool_ArborTester | med board AI tutor | Next.js + FastAPI + Postgres | Render | no | stale a year; CORS allow-all |
| sagearbor.github.io | user site root; FitRival landing + privacy | static | GitHub Pages | yes | add other apps' privacy pages here |
| movieScript_firstAI | empty | – | – | no | never started |
| get-shipped | this orchestrator | scripts + docs | GitHub Pages dashboard | – | – |

## Relationships worth remembering
- contextflow ⇄ contextFlow-upgrade: product ⇄ billing/compliance micro-site. Neither is legacy.
- openline ⇄ personhood: openline consumes personhood credentials via `src/suffrage/personhood-verifier`.
- career-compass ⇄ career-compass-starter: plugin ⇄ template.
- oralhistory_timeline and taskcaster-app pin Firebase SDK versions to each other.
- sagearbor.github.io hosts FitRival's privacy policy; taskcaster and oralhistory host theirs on Firebase.
