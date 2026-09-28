# Mentor notes — Marlowe to Claude

Running log. Read before every build session. Each entry: date, what was learned, what changes in your builds.

---

## 2026-09-27 — Meta Advantage+ creative: the ad you wrote is not the ad users see

**What I learned (Meta Business Help Center, "About Advantage+ creative"):**
Meta's Advantage+ creative enhancements can be ON by default and silently change what reaches the user — AI summaries injected between footer and comments, text lifted into overlays, CTAs rewritten with phantom "X% off" claims, website text pulled into the ad on dwell. The primary text and headline you wrote are the *starting* point, not the final ad.

**What you do differently in agency builds:**
1. Any agent or tool that touches ad creative must inventory the FULL enhancement state per ad — every toggle, not just primary text/headline. Build the audit before you build the generator.
2. Never trust AI text inputs (selling points, branding presets, extracted claims). They go stale silently and CAN be shown to users. Every sync/build run diffs live ad copy against the live store or catalog. No diff, no ship.
3. Bake Meta's own creative checklist into the creative agent's spec: product front and centre, brand in the first 3 seconds, design for sound off, one clear CTA, urgency in every sales ad, 9:16 vertical for Reels. These aren't suggestions — they're the acceptance criteria.
4. Small-budget truth: at $5/day, creative wins the auction, not budget. Optimize the agency's creative pipeline for volume (3–5 concepts per campaign, fast variants from existing assets), not for budget tricks.
