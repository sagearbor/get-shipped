# contextflow — ship plan

**Repo:** `../contextflow` (product: Chrome/Firefox MV3 extension + Firebase backend).
**Satellite:** `../contextFlow-upgrade` is NOT legacy. It is the static GitHub Pages
micro-site the extension points to: Stripe pricing table (live keys), privacy
policy, and support page required by the Chrome Web Store. Nothing to migrate;
keep both.

## Goal (user's words)
Present ContextFlow to companies as an option for annual training on long,
boring PDFs. Two things stand between here and that demo.

## Definition of shipped
1. The extension works on an intranet-hosted, embedded PDF (an intranet LMS).
2. Quick results are stored to the cloud for commercial (org) customers.
3. Org customers can pay through a distinct Stripe path (per-seat / annual),
   separate from the individual Basic/Pro pricing table.
4. Published to the Chrome Web Store at a version containing 1–3.

## Work items (ordered)
### 1. Embedded-PDF failure on VPN-only URL
Repro URL: an intranet-hosted training PDF reachable only on the customer's VPN (exact URL in the local, gitignored `tmp/contextflow-private-notes.md`).

What the code does today (`extension/src/utils/pdfReader.ts:155-166`): detects a
PDF if the URL ends in `.pdf`, `document.contentType` is `application/pdf`, or an
`embed[type="application/pdf"]` exists; then fetches the bytes and extracts text
with `unpdf`. Content script is `<all_urls>`, `document_idle`, and does **not**
set `all_frames: true` (`extension/manifest.json`).

Hypotheses to test, in order (needs the user on VPN; the orchestrator cannot
reach the URL):
- **Iframe.** The LMS wraps the PDF in an `<iframe>`; without `all_frames`
  the content script only sees the outer page and finds no embed. Fix:
  `all_frames: true` + frame-aware messaging, or detect `iframe[src$=".pdf"]`
  and fetch that src.
- **Server-side fetch.** If any path (Firebase cache warm, `llmProxy`, sub-page
  fetcher) fetches the URL from the cloud, an intranet URL is unreachable there.
  Fix: always extract text client-side and send text, never the URL, for
  non-public hosts.
- **Plain HTTP.** Mixed-content / HTTPS-upgrade rules may block the `fetch`
  of an `http://` PDF from an extension context. Check the console.
- **Auth/cookies.** The library may require session cookies; confirm the
  `fetch` sends credentials (`credentials: 'include'`).
- **No text layer.** If the PDF is scanned, `unpdf` returns nothing. Confirm
  by selecting text in Chrome's viewer.

Diagnostic first step for the user (after PR #90 merges): on VPN, open the
URL, open DevTools, run `window.__cfDiagnosePDF()` in the console, and paste
the output into `../contextflow/tmp/`. One run answers all five hypotheses.

### 2. Cloud storage of quick results for org users
Exists: shared Firebase cache of page analyses (`extension/src/utils/firebaseCache.ts`,
`contextflow-backend/firestore.rules`). Unknown: whether *per-user* quick
results (quiz scores, completion) are persisted for org reporting.
Per `docs/NEXT_SESSION_HANDOFF.md`, org enrollment works but access is a
hand-made Firestore doc. Work: define the org "training record" (user, doc URL
hash, score, completed-at), write it from the extension, read it in a minimal
org admin view or CSV export. That is the thing an org customer would actually buy.

### 3. Distinct Stripe path for orgs
Exists: individual Stripe webhook billing (`contextflow-backend/functions/index.js`,
`extension/src/utils/license.ts`). Missing (handoff doc): per-seat subscription,
seat counting/enforcement, "leave org" freeing a seat, and enrollment logic is
duplicated between `popup.js` and `license.ts`. Work: one Stripe Product
"Org annual per seat", checkout session with `quantity`, webhook sets
`orgs/{id}.seats`, `validateLicense` enforces seat count.

### 4. Chrome Web Store release
Branch triage done 2026-09-08 (PR #90, `docs/BRANCH_TRIAGE.md`): all twelve
stale branches were already merged via GitHub PRs; they only need deleting.
Remaining: bump `manifest.json` version (0.1.44 now) and submit.

## Open questions for the user
- Is ContextFlow currently listed on the Chrome Web Store? (Support/privacy
  pages were built for review in Feb 2026; no listing URL found in either repo.)
- For org customers: does the pitch need SSO, or is email-domain enrollment enough?

## Env needed (names only)
`extension/src/config/config.ts` (gitignored): LLM API keys, `LLM_PROXY_URL`,
`ORG_CONFIG.enrollUrl`, `STRIPE_CONFIG.*`. Firebase project `contextflow-ext`.

## Log
- 2026-09-08 — Round 2 agent: org training records + per-seat billing, PR #89 (open, owner review). Round 3 agent: branch triage + PDF debug aid, PR #90 (open).
- 2026-09-06 — plan created from repo profiling; no code touched.
