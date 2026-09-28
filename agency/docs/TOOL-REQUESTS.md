# Tool requests for Muse — from Jarvis (GatorBait Media ops), Sept. 28, 2026

Brenden: "Tell Muse to look for that so you can get tools … whatever else you need."
Muse owns the registry (`SOURCES.md`, handpicked). These are open gaps no current
row covers, found while running GatorBait Media today. Please scout, add rows with
design directives the usual way, and mark which request each one answers.

**Hard constraints (same as the registry):** MIT/Apache only. No new servers, databases,
or Docker for anything we need this month — runs in GitHub Actions, the browser, or a
Wix custom embed (15,000-char cap). Nothing that emails or messages subscribers on its own.

## Priority 1 — reach readers we're losing
- **R1. Wix member-app (Spaces by Wix) push.** Wix exposes no API to push to members in the
  Spaces app; the owner sends by hand from the dashboard. Need any documented, ToS-safe way to
  notify app members when a story posts — or the best alternative channel (web push that runs
  inside a Wix custom embed, e.g. a service-worker-free approach, or an RSS→push bridge that
  needs no server).
- **R2. Win-back / re-permission for lapsed subscribers** that works with Wix Email Marketing
  segments and labels (we have #126 chappie and #325 lifecycle-skills — need anything for
  deliverability recovery after a "sender rank BAD" suspension, and engagement-based
  send throttling / warm-up schedules).

## Priority 2 — measure what's real
- **R3. Accurate article view counting on Wix.** Wix Blog view counts (~300/post) look far
  below site traffic (12.6k unique visitors / 60 days). Need a lightweight, consent-aware,
  privacy-safe page-view counter that can live in a custom embed and write to a free
  store (or GitHub via Actions), plus a report that joins GSC clicks (#269) and Wix analytics.
- **R4. GA4 / Search Console pulls from GitHub Actions** without a server (service-account
  based), producing a weekly per-article report.

## Priority 3 — quality gates (stop repeat mistakes)
- **R5. Quote verification for the copy desk.** Tooling that aligns quoted text in an article
  against a transcript (fuzzy match, flags any quote with no source span). Transcripts arrive
  as ASAP Sports text / PDFs.
- **R6. Rendered-font / visual regression on a live Wix site** in Actions (Playwright-based is
  fine; #79 covers screenshots) that reads computed `font-family` for native Wix widgets
  (Blog, Pricing Plans, Members) and fails on anything not Barlow.
- **R7. Wix Blog paywall / metering** patterns (post↔plan gating at scale, soft metered paywall
  in a custom embed) that don't require Velo backend changes.

## Priority 4 — nice to have
- **R8. Broken-link / broken-image / stale-copy sweeper** for a Wix site from Actions.
- **R9. Structured-data (NewsArticle) and meta-description linter** for Wix Blog output.

Reply by adding rows to `SOURCES.md` (tag them `answers R#`) and a one-line note here.
Jarvis will sequence and deploy them in gatorbait-media-redesign under the one-controller rule.
