<!-- Source: coreyhaines31/marketingskills (https://github.com/coreyhaines31/marketingskills) — MIT. Adapted for Gator Bait Agency. -->
<!-- Source: ericosiu/ai-marketing-skills (https://github.com/ericosiu/ai-marketing-skills) — MIT. Adapted for Gator Bait Agency. -->
# CRO Playbook — Conversion Rate Optimization

**Primary owner:** rank (analysis + recommendations) → webmaster (implements on the site). scribe supplies copy variants. Concepts only — no code vendored.

Run this whenever a page exists to convert and isn't converting enough: homepage, landing pages, pricing/membership pages, merch product pages, email/newsletter signup forms, article pages with monetized CTAs.

## The 8-dimension audit

Score every page 0–100 across these dimensions, in order of impact. The overall score is a weighted average; the priority fixes are the lowest-scoring dimensions with the highest revenue impact.

1. **Value proposition clarity** (highest impact) — Can a cold visitor understand what this is and why they should care within 5 seconds? Benefit-focused beats feature-focused. Vague or clever loses to specific and plain.
2. **Headline effectiveness** — Communicates the core value prop, specific (numbers/timeframes), matches the traffic source's messaging. Strong patterns: "Get [outcome] without [pain point]", "The [category] for [audience]", "Never [unpleasant event] again", "[Question naming the pain point]".
3. **CTA placement, copy, hierarchy** — One clear primary action, visible without scrolling, repeated at key decision points. Button copy states value, not just action: "Get My Report" beats "Submit". Primary vs. secondary CTA hierarchy is obvious.
4. **Visual hierarchy & scannability** — A scanner gets the main message; important elements are prominent; white space exists; images support the message (not decoration).
5. **Trust signals & social proof** — Attributed testimonials with specifics, real numbers, recognizable logos, review scores — placed near CTAs and after benefit claims.
6. **Objection handling** — Price/value, "will this work for me?", difficulty, "what if it doesn't work?" — answered via FAQ, guarantees, process transparency.
7. **Friction points** — Form field count, unclear next steps, confusing nav, slow load, broken mobile layout. Every extra required field costs conversions.
8. **Page speed indicators** — Unoptimized images, heavy scripts, render-blocking resources. Slow pages fail before the copy even gets read.

**Industry note:** adapt benchmarks to the page type — merch PDPs are judged against ecommerce norms, articles against media norms.

## Output format for every audit

### Quick Wins (implement now)
Easy changes with likely immediate impact. Ranked by impact.

### High-Impact Changes (prioritize)
Bigger changes worth the effort. Each with a one-line hypothesis.

### Test Ideas
Hypotheses worth A/B testing rather than assuming. Feed these into the experiment backlog (`EXPERIMENT-RUNBOOK.md`).

### Copy Alternatives
For headlines and CTAs, provide 2–3 alternatives with rationale.

## Page-type frameworks

- **Homepage:** clear positioning for cold visitors; fastest path to the most common conversion; serve both "ready to buy" and "still researching".
- **Landing page:** single message, single CTA; headline matches the ad/post that sent the traffic (message match); complete argument on one page.
- **Pricing/membership page:** help the visitor choose — flag the recommended plan, answer "which is right for me?" anxiety.
- **Merch product page:** outcome-first headline (what wearing/owning it signals), proof (photos, reviews), price anchoring, one primary CTA, scarcity only if real.
- **Article page:** contextual CTAs matching the article topic; inline CTAs at natural stopping points — never just a banner in the sidebar.

## Form optimization (signup/newsletter/checkout)

- Fewer fields win. Ask only for what the next step needs.
- Multi-step beats long single-page when many fields are unavoidable.
- Error handling should be inline, specific, and blame-free ("That email looks incomplete" not "Invalid input").
- Primary CTA communicates what they get: "Get the Free Guide" > "Sign Up".

## Rules

- **Recommendations come with evidence:** name the dimension, the observation, the expected lift, and whether it's a quick win or a test.
- **Never assume:** page-type frameworks suggest; tests decide (`EXPERIMENT-RUNBOOK.md`).
- **One variable per test:** don't bundle the headline rewrite with the CTA change and claim you know what worked.
