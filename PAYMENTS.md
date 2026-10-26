# In-app payments (subscriptions) across all repos

Shared setup for selling in-app plans in any of the sibling apps. The
step-by-step procedure (keys, per-app checklist, Play API gotchas) lives in the
ship-mobile-app skill: `~/.claude/skills/ship-mobile-app/reference/payments.md`.

## Account-level, done once (2026-10-25, during oralhistory_timeline)
- Apple: Paid Apps agreement, bank, W-9 — Active.
- Apple In-App Purchase key "RevenueCat – all apps": `~/.config/revenuecat/SubscriptionKey_5L99K4ZUXP.p8`
- Google Payments merchant account: existing "SAGE CHILD ARBOR" payments
  profile (Individual), public name "Sage Arbor Apps", statement "SAGE ARBOR APP".
- RevenueCat account (sagearbor@gmail.com), card on file; free under $2.5k/mo
  tracked revenue, then 1%.
- TODO (owner): 15% fee programs — Play "service fees" enrollment, Apple Small
  Business Program. Both are account-wide.

## RevenueCat SDK per repo (what to pick in RevenueCat's platform list)
Selected at signup: Flutter, React Native, Native Apple, Native Android.

| Repo | Stack | RevenueCat SDK |
|---|---|---|
| oralhistory_timeline | Flutter | purchases_flutter (already in pubspec) |
| FitRival (`app/`) | Flutter | purchases_flutter |
| mosaicHighRes (`app/`) | Flutter | purchases_flutter |
| taskcaster-app | Flutter | purchases_flutter |
| mindshift phone (`apps/mobile`) | Expo 57 / React Native 0.86 | react-native-purchases |
| mindshift Apple Watch (`apps/mobile/targets/watch`) | Swift (watchOS) | Native Apple — usually not needed: buy on the phone, watch reads the entitlement |
| mindshift Wear OS (`apps/watch/wearApp`) | Kotlin | Native Android — same as above |

## Per app
One RevenueCat **project** per app (own entitlements, offerings, webhook,
secret key). Upload the same Apple .p8 and the same Google service-account JSON.

## Status
- oralhistory_timeline: 6 plans created on ASC + Play (Play active 2026-10-25,
  174 regions). RevenueCat project, webhook and build 94 pending.
