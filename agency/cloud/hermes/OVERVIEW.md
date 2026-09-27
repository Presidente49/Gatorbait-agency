<!-- Source: NousResearch/hermes-agent (https://github.com/NousResearch/hermes-agent) — MIT, Copyright (c) 2025 Nous Research. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Hermes Agent — the learning loop, as a reference

**What it is:** Hermes Agent (Nous Research, MIT) is a self-hosted agent
that bills itself as "self-improving." It has a closed learning loop:
agent-curated memory with periodic nudges, skills created from completed
work, a background curator that keeps the skill library tidy, full-text
search over past sessions, and optional user modelling. We borrow the
**loop design and its guardrails**. We do not vendor or run the app.

Hindsight (`agency/cloud/hindsight/`) already gives the agency its memory
*model*: banks, retain/recall/reflect, and observations with proof counts.
Hermes adds the *maintenance* the model was missing: how lessons get
captured, deduplicated, expired, and promoted into skills, plus what must
never be captured.

## The Hermes loop, and where each piece lands here

| Hermes mechanism (source path, commit `28e6496`) | What it does upstream | Agency equivalent |
|---|---|---|
| Background review fork (`agent/background_review.py`, `_MEMORY_REVIEW_PROMPT`, `_SKILL_REVIEW_PROMPT`) | After a turn, a forked agent rereads the conversation and asks "should any memory or skill be saved or updated?" | **Close-the-loop capture** at the end of every workflow (protocols step 7), using the entry format and do-not-capture list in `CURATE-REFLECT-RUNBOOK.md` |
| Nudge intervals (`agent/agent_init.py`: memory `nudge_interval` 10 user turns, skills `creation_nudge_interval` 10 tool iterations) | Review fires on a counter, so the agent can't just forget to reflect | Capture is a **required step of every workflow**, and a missing entry is itself flagged in the weekly curate |
| One fact → one store (`_MEMORY_ROUTING_BLOCK`) | Profile facts go to USER.md, environment facts go to MEMORY.md, procedures go to skills. A fact is never stored twice. | **Routing table**: brand `learnings.md`, `agency/shared/learnings.md`, brand context files (`audience.md`, `about.md`), or a skill. Each lesson lives in one place and the others link to it. |
| Memory char caps + "IF FULL: consolidate" (`tools/memory_tool.py`, 2,200 / 1,375 chars) | A size limit forces merging and pruning instead of endless growth | **Active-lesson cap** per learnings file (agents read these at every startup) |
| Duplicate refusal + injection scan (`tools/memory_tool_store.py`, `_scan_memory_content`) | Exact duplicates are refused. Text that looks like instructions or exfiltration is rejected, because memory re-enters every prompt. | **Dedupe rule** plus **source hygiene**: text from comments, competitors and web pages is data, never instructions |
| Lesson-layer rules (`_LESSON_LAYER_BLOCK`) | A pitfall is a general rule plus one clause of *why*. No incident narration or ticket numbers. The same lesson learned twice becomes one rule. A wrong rule gets fixed in place. | **Entry-writing rules** in the runbook |
| Do-not-capture list (`_DO_NOT_CAPTURE_BLOCK`) | Never persist environment failures, negative tool claims, transient errors, one-off narratives, or unresolved failures dressed up as "the workflow" | Adopted almost verbatim, in agency terms |
| `/learn` (`agent/learn_prompt.py`) | Turns "what we just did" into a skill. Extends an existing skill before creating one, and never invents flags or paths. | **Lesson → skill promotion** (`LESSON-TO-SKILL.md`), **draft-only until a human approves** |
| Skill preference order (`_SKILL_REVIEW_PROMPT`) | Patch a loaded skill, then an existing umbrella, then add a support file, and only then create a new *class-level* skill. Never name a skill after an incident. | Same order in the promotion rule |
| Curator (`agent/curator.py`, `skills/AGENTS.md` §Curator) | Idle-triggered, 7-day interval. Skills move active → stale (14 d) → archived (30 d). Never delete, only archive. Pinned skills are skipped. Every run writes a report. There is a dry-run mode. | **Weekly curate / monthly reflect runbook** (Wrench): stale → archive with a written reason, `learnings-archive.md`, a run report in `outputs/` |
| "use=0 is absence of evidence" (curator rule 4) | A never-used skill isn't pruned just for being unused while it is young | A lesson is **never expired for lack of re-tests** before its review window closes |
| Session search (`tools/session_search_tool.py`, FTS5, no LLM) | Recall past work by searching real transcripts. Task progress stays out of memory. | **Recall from `outputs/log.md` + `outputs/`** before re-deriving. Task logs never go into learnings. |
| Honcho user modelling (external `plastic-labs/honcho` plugin, `plugins/memory/honcho/`) | Builds a model of the user across sessions | **Not adopted as software.** The agency's "user model" is the brand's `audience.md` + `about.md`, and audience and owner-preference lessons are routed there |

## What we deliberately did NOT take

- **Autonomous skill writes.** Hermes lets a background fork create and patch
  skills with no human present. Here, a skill made from a lesson is a
  **draft until a human approves it**, because skills drive public-facing work.
- **"Be ACTIVE — most sessions produce at least one skill update."**
  (`_SKILL_REVIEW_PROMPT`). That bias to write makes sense for a
  personal coding agent. In marketing it produces confident rules from single
  posts. Our bar is evidence: a source or a measured result.
- **Consolidation quotas.** (`CURATOR_REVIEW_PROMPT`: "fewer than 10
  archives, you stopped too early"). Quotas reward churn. We merge when content
  overlaps, not to hit a number.
- **Hermes' short windows (14 / 30 days).** Those are tuned to skill *usage*.
  Marketing lessons age by domain (platform behavior fast, audience slowly),
  so our expiry windows are per-scope.
- **The app itself**: SQLite state, the gateway, cron, and the provider plugins.
  They are out of scope. Paperclip (`agency/cloud/paperclip/`) is our runtime.

## Files

- `CURATE-REFLECT-RUNBOOK.md`: the entry format, capture rules, and the weekly
  curate / monthly reflect procedure (dedupe, evidence, expiry, contradictions,
  routing, cap)
- `LESSON-TO-SKILL.md`: when a repeated lesson becomes a reusable skill, and
  the draft → approval path
- `agency/cloud/hindsight/AGENCY-MEMORY-MODEL.md`: the memory model these
  maintain (retain / recall / reflect)
