<!-- Source: ericosiu/ai-marketing-skills (https://github.com/ericosiu/ai-marketing-skills) — MIT. Adapted for Gator Bait Agency. -->
# Quality Gate — Expert-Panel Scoring Before Anything Publishes

**Primary owner:** scribe (runs the gate on its own output; any agent can invoke it on anything publishable). Concepts only — no code vendored.

Run this on every publishable artifact: post captions, articles, landing-page copy, ad creative, scripts, newsletter editions, thumbnail/title packages. Nothing public-facing ships without passing.

## Step 1 — Intake

Collect: the artifact, its type, the brand and offer context, and whether there are multiple variants to compare. If the context is obvious, don't ask — just proceed.

## Step 2 — Assemble the panel

Auto-assemble **7–10 experts** tailored to the artifact type and domain:

- **Content-type experts first** (e.g., a Short-Form Copy Expert for a reel script, a Conversion Copy Expert for a landing page).
- **Add 1–3 domain experts** who understand the specific industry/audience (e.g., Sports Media Expert for a Gators brand).
- **Always include these two:**
  - **AI-writing detector** — flags the 24 tell-tale patterns of AI slop (em-dash spam, "delve", "in today's fast-paced", list-of-three clichés, vague intensifiers). Weighted **1.5x** in the aggregate. Non-negotiable.
  - **Brand-voice match** — checks alignment with the brand's `brand-voice.md` and its known rejection patterns. Non-negotiable.
- Cap at 10; merge overlapping roles.

List each expert with name, lens, and what they check.

## Step 3 — Pick the rubric

| Artifact type | Rubric |
|---|---|
| Posts, articles, emails, scripts, newsletters | Content quality (clarity, hook, specificity, voice, CTA) |
| Strategy, recommendations, analysis | Strategic quality (insight, evidence, actionability) |
| Landing pages, ads, CTAs, merch PDPs | Conversion quality (value prop, friction, trust, CTA) |
| Graphics, charts, infographics | Visual quality (hierarchy, readability, on-brand) |

## Step 4 — Score recursively to 90+

Target: **90/100 weighted aggregate across all experts. Max 3 rounds.**

Each round produces the round score table, aggregate, top-3 weaknesses, and the specific edits addressing them — then the revised artifact.

Rules: scores are brutally honest (no padding to 90). Below 90: identify top-3 weaknesses → revise → next round. At/above 90: finalize. After 3 rounds still under 90: return the best version with its honest score and what's holding it back. **Show all rounds** — the iteration trail is part of the value.

**Variant comparison:** score each variant independently through the full panel, rank by aggregate, and only iterate on the best one.

## Step 5 — Output

Winner + score at the top, then the artifact, then the full scoring history. If it's a rewrite of another skill's output, include a **source-improvement brief**: what scored low, the specific example, and the concrete rule the source skill should adopt — this is how the gate feeds the agency playbook.

## Step 6 — Learn from approvals and rejections

- **Approved:** note what worked; no action needed unless a new positive pattern emerges.
- **Rejected or overridden:** record the pattern in the brand's `learnings.md` as a rejection rule (what to never do again for this brand). The gate checks known rejection patterns before scoring, so documented patterns are penalized even if individual experts miss them.

This is the mechanism that makes the agency's quality compound: every rejection becomes a permanent rule.
