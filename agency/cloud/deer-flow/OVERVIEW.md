<!-- Source: bytedance/deer-flow (https://github.com/bytedance/deer-flow) — MIT, Copyright (c) 2025 Bytedance Ltd. and/or its affiliates; (c) 2025-2026 DeerFlow Authors. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# DeerFlow: overview (run-level control patterns)

**What it is:** DeerFlow 2.0 is ByteDance's open-source "super agent
harness", built on LangGraph. One **lead agent** plans, can hand work to
**sub-agents**, runs tools inside a **sandbox** with separate workspace,
uploads and outputs folders, asks a human for **clarification** before acting,
and keeps long-term memory. Python backend plus a Next.js UI.

**License:** MIT. The LICENSE file was read on 2026-09-27. Copyright lines:
"Copyright (c) 2025 Bytedance Ltd. and/or its affiliates" and "Copyright
(c) 2025-2026 DeerFlow Authors". There is no commercial carve-out.

**What we took: concepts only.** No code, prompts or config are vendored.
The agency does not run DeerFlow. Adopting it would add a second runtime
and a second controller, and the agency already has one control plane
(Paperclip).

## Where it fits

Paperclip (`agency/cloud/paperclip/`) runs the **company**: the org chart,
the task queue, budgets, heartbeats and board approvals. It does not say
how one task is worked from request to result. DeerFlow's lead agent works
at that level, the **run**. This folder turns its run-level patterns into a
runbook:

| Layer | Owns | Lives in |
|---|---|---|
| Company | Org chart, budgets, heartbeats, governance | `agency/cloud/paperclip/` |
| Run (one task, start to finish) | Clarify, plan, approval checkpoints, delegation contracts, workspace boundary, verification, run report | `agency/cloud/deer-flow/RUN-PROTOCOL.md` + `TEMPLATES.md` |
| Memory across runs | Retain, recall, reflect | `agency/cloud/hindsight/` (the run report feeds it) |
| Escalation levels, quality gate | L0–L3, auto-approve checks | `agency/shared/protocols.md` |

## Patterns adopted, with upstream source paths

| Pattern | DeerFlow source (repo-relative) | Agency version |
|---|---|---|
| Clarify, then plan, then act. Clarification types: missing info, ambiguous, approach choice, risk confirmation, suggestion | `backend/packages/harness/deerflow/agents/interaction_policy.py` (`_INTERACTIVE_CLARIFICATION_SYSTEM`) | RUN-PROTOCOL step 1 |
| Unattended runs never wait for a human. They make the smallest reversible assumption and list it, or they return a structured `BLOCKED` | same file (`_AUTONOMOUS_CLARIFICATION_SYSTEM`), `backend/docs/RUN_INTERACTION_POLICY.md` | Heartbeat or scheduled mode, step 1 |
| Plan mode: a todo list with pending, in_progress and completed items, used only for work with 3 or more steps | `backend/docs/plan_mode_usage.md` | Plan file, step 2 |
| Delegation check: direct work is the default. Delegate only when the benefit clearly beats the cost. Parallel work is ruled out when tasks depend on each other or share state. Use the fewest workers | `backend/packages/harness/deerflow/agents/lead_agent/prompt.py` (`_build_subagent_section`) | Step 3 |
| Delegation contract: a bounded scope, known context, expected output, **explicit side-effect ownership**, acceptance criteria | same function, plus `backend/packages/harness/deerflow/subagents/report_contract.py` | Delegation record template |
| Sub-agents cannot delegate (`disallowed_tools` defaults to `["task"]`). Each sub-agent has an allowlist of tools and skills, a turn cap and a timeout | `backend/packages/harness/deerflow/subagents/config.py` | "Only the controller delegates", step 3 |
| Hard caps on delegations per step and per run. Past the cap, finish the work directly | `prompt.py` (`MAXIMUM … task CALLS PER RUN`) | Run limits |
| Self-report contract: every deliverable carries a verifiable handle, and the report states what failed or was skipped | `subagents/report_contract.py` | Worker return block |
| Acceptance verdicts per criterion: `holds`, `does not hold` or `UNVERIFIED`. "Completed" means the work finished, not that it was accepted. Repair only the unmet criterion; do not restart | `prompt.py` (acceptance results), `subagents/acceptance_checks.py`, `subagents/status_contract.py` | Step 5 |
| Stop reasons: `turn_capped`, `token_capped`, `loop_capped` | `subagents/status_contract.py` | Report status field |
| A workspace per thread, with separate workspace, uploads and outputs directories | `backend/docs/ARCHITECTURE.md` (Sandbox System, virtual path mapping) | Run folder layout |
| A guardrail checks every tool call before it runs and **fails closed** | `backend/docs/GUARDRAILS.md` | Gate check, step 4 |
| Goal evaluation with typed blockers (`missing_evidence`, `needs_user_input`, `run_failed`, `external_wait`, `goal_not_met_yet`), a cap on continuations and a no-progress breaker | `backend/packages/harness/deerflow/agents/goal_state.py`, README "Session Goals" | Run report outcome and blocker fields |
| Loop detection per run | `backend/docs/LOOP_DETECTION.md` | "Two identical attempts, then stop" |

## Rejected or deliberately not adopted

- **Running DeerFlow as a second runtime or controller.** Paperclip plus
  this runbook covers the need. The agency has one controller per brand.
- **The DeerFlow version of "human approval is too slow for autonomous
  workflows, so guardrails replace it"** (GUARDRAILS.md intro). Guardrails
  are adopted *in addition to* human gates, never *instead of* them.
  Publishing, money, accounts, credentials, deletions and first public
  posts always stop for the approver named in the brand's `about.md`.
- **Durable batch mode (`batch_task`)** and the per-response parallelism
  settings are runtime engineering and are not needed at agency scale.
- **Memory (DeerMem).** `agency/cloud/hindsight/` already owns memory.
  Run reports feed it.
- **Model-provider and deployment details** (Docker/E2B sandboxes,
  provider adapters, sponsored model recommendations). These are
  deploy-time choices, out of scope here.
