# Learnings — Gator Bait Media

Brand-specific learnings. Shared cross-brand principles live in
`agency/shared/learnings.md`; this file is what's true about GATOR BAIT
in particular.

## Audience
- Die-hard Florida Gators fans; react strongest to player-first content
  (Baugh, Clark, Philo) and coach-mic moments (Sumrall pressers).
- "Work the cut" / "it ain't fully awake yet" language is identity-level
  — the audience repeats it back.
- Rival-fan smack talk (Tennessee, Georgia, FSU) is top engagement fuel;
  clap back playfully, never meanly.

## Content
- Postgame presser clips are the highest-ROI content type.
- Stat carousels after wins travel far; verify every number against the
  final box score before posting (Sep 26: caught a 2-TD vs 3-TD error
  pattern on in-game graphics).
- One game photo = one post. Never batch photos into a single post;
  each photo is its own revenue surface.
- Columns get native posts with an original hook + article link, never
  bare link drops.

## Cadence
- Facebook: 4–6 posts/week normally; game day is unlimited.
- Group shares: ~1/hour, Gator groups only, varied share text, always
  share the original Page post (never re-upload).
- Instagram: only via the owner's approval taps — stage in small waves.

## Money
- Meta Content Monetization: reels earn the most, then photos. Dollar
  figures and payout status are private; they are kept in the owner's Drive,
  not in this public repo.
- A payout security hold after account changes pauses withdrawals, not
  earnings. It is not a suspension.
- Subject lines starting with "Buddy Martin" earn 60–67% open rates vs
  36–41% for generic subjects (Wix email, Sep 2026).

## People & access
- Chris Spears: game photographer, shoots free for the credential,
  admins the FB page. Photo drops land postgame.
- Scott Burns (UF football communications): media credentials route.
- Wix login is Google SSO — no password exists. Browser work rides the
  existing Google session.

## 2026-09-27: The front page leads with the newest story, so every story is a potential cover
- Loren's postgame piece went live with an AI cartoon cover and four misspelled names and became the front-page lead within minutes. Proven fix: desk review before publish (`editorial-desk.md` submission rules) plus the copy-desk audit after every publishing burst.
- A headline over a photo reads as a publication; the headline under the photo reads as a blog. Real photos only under an overlay.
- Headless fetch tools don't run the custom renderer; they show the hidden native Wix layer. Don't report what they "see" as what readers see.
- Email: 8 sends Sept. 25–27 each reached 1,807–1,816 delivered. The postgame reaction email (presser + column) drew the most clicks (150).

## 2026-09-27 — Design Desk created
Brenden: "A copy desk — go get yourself a graphics design team." The Design Desk (lead: blueprint) now does a visual pass on every post between the copy and the publish, then verifies the live page on a phone. Trigger case: Chris Spears' column went out with every mobile headline clipped by the template's full-bleed header. See brands/gator-bait-media/design-desk.md and skills-library/design/article-visual-qc.md.

## 2026-09-27 night into 2026-09-28: first live run of the dispersed department tools
- Ran copy-desk-audit, photo-sourcing, embed-patch and a light seo-audit against real live content for the first time since they were dispersed. Findings: 3 zero-tag posts (fixed), one cover photo reused across two live posts (fixed — the photo-sourcing rule catches this even when nobody flags it), and a real repo/live drift on 3 Wix embeds caught by embed-patch's own "sync the repo copy" step, which had been skipped after 3 live patches earlier that night.
- **Take the audits seriously as a standing loop, not a one-off.** Every one of tonight's findings (cover dup, missing tags, embed drift) had already happened silently before the audit ran; nothing was caught until the department tool was actually pointed at live content.

## 2026-09-28: font and typography drift recurs even after a documented ban
- Georgia serif reappeared in the site's live header and Magazine embeds (headlines, account/plan titles, recent-post widget) months after the site's own docs banned it. Caught only because Brenden complained about "the site font."
- Blueprint/webmaster should grep the live header/homepage/magazine embeds for banned font names (Georgia, Times New Roman, Montserrat) as a standing item in the visual QC pass, not just when a page is newly built.

## 2026-09-28: AdSense root cause — Homepage and Magazine hide the container Auto Ads needs
- The Homepage and Magazine custom pages hide Wix's native `#SITE_PAGES` container to kill an old page-flash bug. Google's Auto Ads places in-content units by scanning that same container, so those two highest-traffic pages likely can't serve in-content ads at all — only article pages, which don't hide it. This had been an open, unexplained "why no ad revenue" question; it's a structural design conflict, not a broken integration. A fix needs a deliberately built, visible ad slot inside the custom page markup, decided with the owner — not resurrecting old disabled ad-repositioning code, which can't create a placement surface that never existed.

## 2026-09-28: a live page's own refresh logic can silently undo a manual content edit
- Added a Chris Spears photo gallery to the Magazine's "Inside the issue" grid by editing the embed's static fallback data — which would have been wiped out the instant the page's own live feed refresh ran, because that refresh only keeps posts from 5 named columnists and Chris Spears isn't one of them. Caught before shipping by reading the actual runtime code, not just the edited data.
- Before trusting any edit to a live-rendered page "will show," check whether the page has its own refresh/poll/re-render logic downstream that could overwrite or filter it out.

## 2026-09-28: gallery pattern and photo inventory
- Built the brand's first photo gallery post (10 credited Chris Spears photos, Ole Miss game) using only already-identified/captioned photos from `CREDIT.md` — never the 27 uncaptioned SmugMug photos sitting in Wix, which still need viewing and identification before use (photo-sourcing rule: "not yet viewed/captioned: identify subjects before placing in a post").
- Standing backlog: those 27 SmugMug photos are a ready source for a second gallery or to round out the first, once identified.

## 2026-09-28: email list hygiene needs a Gmail sweep, not just campaign stats
- A subscriber's mail host silently forwards to a dead, abandoned mailbox under GatorBait's own Return-Path. Wix's campaign stats saw it as DELIVERED every time; the real bounce arrived as a `postmaster@outlook.com` notice in the owner's personal Gmail, invisible to any audit that only checks the email platform. Fixed by also searching `from:postmaster OR from:mailer-daemon OR subject:undeliverable` in the owner's inbox during any list-hygiene pass. See `agency/skills-library/marketing/email-delivery-check.md` for the standing checklist to extend.
