<!-- Source: vectorize-io/hindsight (https://github.com/vectorize-io/hindsight) — MIT. Adapted for Gator Bait Agency. -->

# Hindsight — Overview

**What it is:** Hindsight is an agent memory system built to create agents that
*learn over time*, not just remember conversation history. It claims
state-of-the-art accuracy on long-term memory benchmarks (LongMemEval) and is
used in production at Fortune 500 enterprises. Self-hostable via Docker
(Postgres-backed), pip, Helm, or a managed cloud.

**The model that matters for us** (concepts, not the app):

- **Memory types** — *world facts* (facts about the world), *experiences* (the
  agent's own experiences), *observations* (consolidated, evidence-backed
  beliefs formed from many memories), *mental models* (learned understanding
  synthesized from observations and facts).
- **Banks** — memories live in named banks; one bank per concern keeps recall
  scoped and clean.
- **Three operations** — `retain` (push new memory in; an LLM extracts facts,
  entities, relationships, time series), `recall` (retrieve via semantic +
  keyword + graph + temporal strategies fused together), `reflect` (deep
  analysis across memories to form new connections — e.g. *why did these
  outreach messages get replies and those didn't?*).
- **Observations with proof** — retained facts don't stay a flat pile. Related
  facts consolidate into observations that keep their supporting evidence with
  exact quotes and a proof count. New evidence *refines* an observation instead
  of overwriting it — beliefs strengthen, weaken, or extend.

**Why it matters:** Our `agency/shared/learnings.md` is currently a flat
append-only list. Hindsight is the blueprint for graduating it into a real
memory system: per-brand banks, evidence-backed observations, and periodic
reflection that turns raw campaign results into durable strategy.

See `AGENCY-MEMORY-MODEL.md` for the concrete design.
