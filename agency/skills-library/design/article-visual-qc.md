# Article Visual QC

**Owner:** blueprint (Design Desk), with webmaster for template fixes. The brand checklist lives in `brands/<brand>/design-desk.md`.

Run it on every post after the Copy Desk is done, and again on the live page after publishing.

1. **Cover:** a real, credited, landscape (≥1.3:1) photo unless the piece is a graphic-led column. Never AI art on news.
2. **Inline photos:** place them at the matching beat (the Baugh photo under the Baugh item). Caption the action and credit the photographer. Name a player only when confirmed (the jersey number against the roster). Vertical photos are SMALL.
3. **Render at 390px and desktop:**
   - The headline's box sits inside its clipping ancestor.
   - The cover block is visible when expected.
   - `scrollWidth` is at most the viewport width.
   Live: run `automation/vision/live-qc.mjs` (add the post as a target with `postFormat.hero:true`).
4. **Fix order if something breaks:** fix the post content first. Change the template only if the problem affects every post, and then note the rollback and the fingerprint (web/embed-patch.md).
5. Report to the owner in one line: what's live, what was fixed, and what is still unverified.
