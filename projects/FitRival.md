# FitRival — ship plan

**Repo:** `../FitRival` (Flutter, Android; backend = Google Apps Script + Sheets).

## Goal (user's words)
Good enough for the user and their sister to use together to lose weight,
socially: interesting average-weight and %-fat curves, gamification, seeing
each other.

## Definition of shipped
1. Two real users (user + sister) on the Play **production** track, not the
   internal track, logging daily without workarounds.
2. Shared trend view: both users' weight and body-fat curves on one chart,
   with rolling average and goal-normalized ("% of goal") comparison.
3. At least one running challenge between them with visible scoring/streaks.
4. Sign-in that doesn't rely on a shared group secret (Firebase Auth), so
   inviting the sister is a link, not a config step.

## Current state (from repo profiling, 2026-09-06)
- v0.0.66 on the Play internal track; production track stale at v0.0.28 (June).
  A target-API deadline (Aug 31) was pending; check Play Console for warnings.
- Social features exist: groups (`app/lib/screens/groups_screen.dart`),
  challenges + scoring (`app/lib/services/challenge_scoring.dart`), multi-friend
  chart with Raw / % of goal toggle (`app/lib/widgets/multi_friend_chart.dart`),
  body trend chart, location-sharing modes, avatars.
- Not done: Firebase Auth (branch `feat/firebase-production`), full test run on
  merged tree before v0.0.66, Health Connect declaration review, iOS.
- Many unmerged branches: `feat/firebase-production`, `feat/target-api-36`,
  `feat/wearable-metrics`, `feat/goal-percent-toggle`, `feat/chart-interactivity`,
  `fix/body-comp-and-honesty-polish`, several `claude/*`.
- Privacy policy live at `https://sagearbor.github.io/fitrival/privacy.html`.

## Work items (ordered)
1. **Unblock production.** Merge `feat/target-api-36`, run the full suite,
   cut a release, promote to production. Check Play Console policy status.
2. **Sister onboarding path.** Walk the invite flow as a brand-new user on a
   second device; write down every step that needs the developer. Those are
   the bugs.
3. **Curves.** Verify the multi-friend chart shows rolling-average weight and
   %-fat for two users; add whatever is missing (smoothing window, goal lines).
4. **Firebase Auth** (`feat/firebase-production`) if item 2 shows the group
   secret is the onboarding blocker; otherwise defer.
5. **Gamification pass.** Weekly streak + head-to-head challenge card on the
   home screen. Keep it to what two people notice.

## Env needed (names only)
Apps Script deployment URL + group secret; Play Console service-account JSON
for `app/scripts/play_publish.py`; Firebase config if item 4 lands.

## Log
- 2026-09-06 — plan created from repo profiling; no code touched.
