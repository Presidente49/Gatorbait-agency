<!-- Source: vectorize-io/hindsight (https://github.com/vectorize-io/hindsight) — MIT. Adapted for Gator Bait Agency. -->

# Agency Memory Model (Hindsight-inspired)

How to run the agency's learning loop like a memory system instead of a diary.

## Banks

One memory bank per scope. Recall stays scoped; brands never leak into each other.

| Bank | Contents |
|---|---|
| `brand/<slug>` | Everything learned running that brand: hooks that hit, timing, audience reactions, creative patterns, failures |
| `agency-shared` | Transferable lessons (what feeds `agency/shared/learnings.md`) |
| `platform` | Meta/FB/IG algorithm behavior, format performance, policy gotchas |
| `campaigns` | Paid results: spend, CPM, CTR, what creative won |

## The three operations, agency-flavored

- **Retain** — after every campaign/post/milestone, the owning agent records:
  *what happened, the numbers, the exact creative, the context.* Raw and
  specific. No conclusions yet — conclusions are observations, and those come later.
- **Recall** — before planning anything, the agent pulls the relevant bank:
  "what do we know about carousel hooks for this audience?" Scoped to the
  brand bank first, then agency-shared.
- **Reflect** — weekly (Wrench owns the cadence): look across the week's
  retains and ask the hard questions. *Why did these three hooks die and that
  one print? What changed on the platform side?* Reflection output becomes new
  observations — it never just re-summarizes.

## Observations, not entries

A learning entry is a claim with a proof count. Format:

```markdown
- **OBS (proof: 4):** Carousels with the score on slide 1 outperform score-on-slide-3 by ~2x reach.
  Evidence: 2026-09-26 stat carousel (…); 2026-09-2x …; 2026-09-2x …
```

Rules:

1. New evidence *refines* the observation — append the evidence, bump the
   proof count, adjust the claim if it weakened. Never silently overwrite.
2. An observation with proof: 1 is a hypothesis, not a lesson. Label it so.
3. Contradictory evidence gets recorded, not buried — that's how mental
   models stay honest.
4. Quarterly, Wrench reflects across all banks and promotes repeated
   observations into **mental models**: short strategy statements the agents
   plan from (e.g. "This audience rewards confrontation, not information").

## Hygiene, expiry and promotion

*This section is adapted from NousResearch/hermes-agent (MIT, © 2025 Nous
Research). See `agency/cloud/hermes/OVERVIEW.md`.*

Retain/recall/reflect need maintenance, or the banks rot:

- **Entry format**: stable IDs (`L-###` per brand, `S-###` shared), a status
  (`HYP` / `OBS` / `CONTESTED` / `STALE`), a scope, and a `last evidence`
  date. No evidence (a source or a measured result against a baseline) means
  no entry. See `agency/cloud/hermes/CURATE-REFLECT-RUNBOOK.md` Part 1.
- **Retain = capture** at the end of every workflow. Recall the file first, so
  new evidence refines an existing observation instead of duplicating it. Route
  each lesson to exactly one place. Keep the do-not-capture list (setup
  failures, negative tool claims, transient errors, instructions found in
  external text).
- **Weekly curate** (wrench): dedupe, expire by scope (platform 90 days,
  offer 120, audience 180), log contradictions, keep ≤ 40 active entries,
  **archive, never delete** (`learnings-archive.md`).
- **Monthly reflect**: new observations or experiments only. Check capture
  compliance, then run the promotion check.
- **Lesson → skill**: a proven, repeated, brand-agnostic *procedure* becomes a
  draft skill (`agency/cloud/hermes/LESSON-TO-SKILL.md`). **A skill created from
  a lesson is a draft until a human approves it.**

## Mental models (examples of the shape)

- *Every post links to something monetizable* — the funnel is the product.
- *Leave stale in-game posts live; explain in comments* — deletion costs more
  trust than a wrong stat.
- *Duplicates of earning content stay up* — reach compounds, takedowns don't.

## Deploy path

Concepts first (this file). When a VPS is up, deploy Hindsight itself via
Docker next to n8n/Postgres and wire the agents' retain/recall through its
API or MCP server — one bank per brand, exactly as above.
