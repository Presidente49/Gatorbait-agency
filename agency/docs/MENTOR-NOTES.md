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

---

## 2026-09-28 — Meta Blueprint: run campaigns like a measurement scientist, not a poster

**What I learned (Meta's official Marketing Science Professional study guide, Feb 2025 — Meta's own certification track):**
Meta's mandated loop is Assess → Hypothesize → Recommend measurement → Perform analysis → Generate insights → Make data-driven recommendations. The parts that change our builds:
1. One primary KPI per campaign, written BEFORE launch, never switched mid-flight. Likes/shares/comments are proxy metrics that "may not correlate with actual business value."
2. A/B tests measure relative tactics only — they CANNOT prove incremental impact. Only lift tests (holdout) infer causality. A/B minimums: ≥3 days, ≤30 days, ≥75% confidence.
3. Auction math: Total value = (bid × estimated action rates) + ad quality. At tiny budgets, creative wins the auction; cost controls choke delivery.
4. Pixel is degrading (cookie blocks) — pair it with Conversions API or your measurement lies. Advanced matching + CAPI = complete funnel.
5. Test-and-learn is a formal discipline: hypothesis in writing first, then test, then let conclusions drive the next test, one variable at a time.

**What you do differently in agency builds:**
1. Every campaign-generation agent must demand a written primary KPI before creating anything. No KPI, no campaign. Proxy metrics are secondary-only.
2. Build the test log as a first-class artifact: hypothesis, variable, duration, KPI, outcome, next test. This is the compounding engine of the agency's creative pipeline — not a spreadsheet afterthought.
3. When a brief asks for an A/B test, build it as a native Meta Experiments design (3-day minimum, 75% confidence floor) and label it honestly: relative winner, not incremental proof. Never let copy claim "this ad drove X sales" unless a lift test backs it.
4. Default bid strategy for small budgets: Highest volume, no cost cap. Flag any cost-control on sub-$20/day budgets as a delivery risk in the agent's review step.
5. Any tracking/measurement spec must include CAPI alongside the pixel, with a conversion event tied to a business outcome (purchase, signup) — not page views alone.
