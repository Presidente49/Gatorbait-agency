# design-desk.md — Gator Bait Media

The Design Desk is the visual partner to the Copy Desk. Brenden set it up on Sept. 27, 2026: "A copy desk — go get yourself a graphics design team."

Lead: **blueprint** (creative/design). **webmaster** handles site-template deploys. The Copy Desk (scribe) owns words and facts; the Design Desk owns how the story looks. It is not another layer of agents; it's a checklist and a toolkit the desk runs on every piece.

## Order of work

1. The Copy Desk finishes the copy.
2. The Design Desk does the visual pass.
3. Publish.
4. The Design Desk verifies the live page on a phone.

Nothing goes out without steps 2 and 4.

## What the desk owns

- **Covers:** the lead photo for every post and the Magazine cover. Real, credited photography only (Chris Spears, UAA handouts with credit). No AI art on news. Landscape covers need a ratio of 1.3:1 or wider, or the template drops the cover block.
- **Inline layout ("magazine style"):** photos placed at the right beat of the story, not stacked at the top. Captions follow "what's happening. Photo by NAME, GatorBait Media". Players are named only when their identity is confirmed (the jersey number checked against the roster), and verticals get size SMALL.
- **Graphics:** poll ladders, stat cards, scoreboards and covers built from the HTML templates, not freehand. Use the brand fonts (Barlow Condensed 800 for headlines, Barlow for body) and brand colors (brand-style.md). Data comes only from a verified source.
- **Headline-over-photo leads** on the front page and Magazine (skills-library/design/hero-overlay.md).
- **Newsletter visuals:** at most 2 photos per issue, real photos only, and a check at 390px and 1000px.
- **Post template health:** headline, cover block, kicker and byline row on phones.

## Visual QC checklist (every post, before and after publish)

At 390px (iPhone), and again at desktop width:
- [ ] The headline is fully visible. No letters are clipped on either side, and no line is wider than its box.
- [ ] The cover photo shows under the headline (landscape), or is intentionally absent (square or vertical graphic).
- [ ] The first inline photo appears within the first two screens on a photo-led piece.
- [ ] Every photo has a credit, and no photo repeats the cover.
- [ ] Nothing scrolls sideways.
- [ ] The kicker and byline row read correctly (the named writer, or "By NAME" in the first line when there's no member account).

Anything that fails blocks the publish, or gets fixed within 10 minutes if it's already live.

## Toolkit (site repo `Presidente49/gatorbait-media-redesign`)

- `automation/vision/live-qc.mjs`: iPhone and desktop renders of live pages. It hard-fails on a clipped headline, a missing landscape cover and sideways scroll. It runs on every push to `deploy/wix-served/**`, and you can also start it manually (workflow_dispatch).
- `gameday/<date>/polls/build.py` and `cover.html`: poll-ladder and cover templates.
- `design/blog-post-template-v1/post-template-embed.html`: the post template (Wix embed 14a887e3). Its 15,000-character cap is tight, so trim before you add.
- The scratchpad render scripts (Playwright, `/opt/pw-browsers/chromium`) for local proofs. Google Fonts are blocked locally, so check the metrics with DejaVu/Liberation.

## Known lessons

- **Sept. 27, full-bleed trap:** a `width:100vw; margin:0 calc(50% - 50vw)` header gets clipped by a narrower ancestor on some phones, and every post headline lost its first letters. Keep blocks inside the column on mobile. The QC now catches it.
- Phones can show a stale page right after an edit, so tell the owner to pull to refresh before judging a fix.
