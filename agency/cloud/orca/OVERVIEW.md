<!-- Source: stablyai/orca (https://github.com/stablyai/orca) — MIT, Copyright (c) 2026 Lovecast Inc. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Orca — Overview (parallel-agent orchestration model)

**What it is:** Orca is a desktop "AI orchestrator" (Electron app + CLI)
that runs several coding agents side by side, each in its own git
worktree or folder workspace, and supervises them through a structured
coordination layer: Runs, Tasks, Dispatches, a coordinator inbox,
blocking questions, and one explicit completion report per worker.

**License:** MIT, Copyright (c) 2026 Lovecast Inc. (LICENSE read
2026-09-27, standard MIT text, no carve-out). We take **concepts and
runbook discipline only**. The app, CLI, terminals and mobile companion
are not vendored, installed, or run by the agency.

**Where it fits:** Paperclip (`agency/cloud/paperclip/`) is the control
plane — org chart, task queue, budgets, heartbeats, approvals.
`agency/shared/protocols.md` is the one-at-a-time handoff waterfall.
Neither says how to run **several agents at once on one job** without
two of them writing the same file, double-posting, or the controller
losing track of who finished. Orca's model fills exactly that gap. The
operating runbook is `PARALLEL-RUNBOOK.md` in this folder.

## Concepts taken (and their agency meaning)

| Orca concept | Orca source | Agency meaning |
|---|---|---|
| **Run** — durable namespace + coordinator inbox for one objective | `skill-guides/orchestration.md` ("Authority and safety floor") | One parallel job = one run folder under `agency/brands/<slug>/outputs/parallel/<run-id>/` |
| **Task** — the unit of work; **Dispatch** — the one authoritative attempt at it | same | Task spec file + claim record; a retry is a new numbered attempt, never a silent second worker |
| **Task-spec contract**: Target, Change, Constraints, Ownership, Observable acceptance | `skill-guides/orchestration.md` ("Task-spec contract") | Mandatory five fields in every task spec — no field, no dispatch |
| **Isolated workspaces** — every task its own worktree; folder workspaces are first-class; a new worktree only when sharing a checkout is unsafe | `docs/site/content/docs/model/worktrees.mdx`; `references/placement-and-remote.md` | Each agent writes only inside its own `workspaces/<task-id>/` folder; a git worktree only for tasks that change repo code |
| **Worker obligations** — do only the current task; ask, don't guess; check for controller follow-ups at checkpoints; send `worker_done` exactly once with an explicit outcome | `references/worker-contract.md` | Worker rules + `report.md` with `outcome: succeeded|failed` and a three-sentence summary |
| **Durable enqueue ≠ read** — sending proves the message is stored, not that anyone acted | `references/messaging-and-gates.md` | Inbox is append-only files; the controller processes every file before marking the batch done |
| **Absence is not failure** — timeout, silence, or an unchanged tail authorizes nothing; only positive proof authorizes stop/retry/release | `references/recovery-and-cleanup.md` ("Stall needs positive evidence") | A quiet worker is `unverified`, not dead. No duplicate worker on the same task without proof the first one stopped |
| **Retry-of + circuit breaker** — retries name the failed attempt; three failures fail the task; never route around it with a new Run | `references/recovery-and-cleanup.md` | Attempt numbers in the claim; attempt 3 failing kills the task and escalates |
| **"Was the mutation applied?"** — check the receipt before replaying a lost write | `references/recovery-and-cleanup.md` | Before re-posting/re-sending anything, check the live surface — the no-double-post rule, made explicit |
| **Review ownership** — a review result authorizes synthesis, not coordinator edits; fixes go back to the owner | `references/coordinator-loop.md` ("Review ownership") | Controller's fan-in review routes fixes to the owning agent; it does not rewrite their files |
| **Completion accounting** — every settled worker gets a next owner: reuse, retain, or release | `skill-guides/orchestration.md` ("Completion accounting") | Run is not closed until every task row on the board has a final state and a disposition |
| **Waves, not deep chains** — real dependencies only, chains ≤3–4 deep, nested depth limited | `skill-guides/orchestration.md`; `references/coordinator-loop.md` | Max one level: workers never spawn workers |
| **Checkpoint comments + card status** (`todo / in-progress / in-review / completed`) | `docs/site/content/docs/cli/worktree-checkpoints.mdx` | Status board columns and one-line checkpoint format |
| **One status store, many readers** | `AGENTS.md` ("Agent Status") | `board.md` has one writer (the controller); workers write only their own `status.md` |

## Deliberately NOT taken

- **The app itself** (Electron UI, terminals, mobile companion, design
  mode, SSH/WSL remotes). The agency is markdown runbooks; installing
  a desktop orchestrator is a deploy-time decision for the owner.
- **Per-workspace cloud environments** (`skill-guides/orca-per-workspace-env.md`):
  paid VMs/sandboxes per task. Out of scope; would need a budget gate.
- **"Fan one prompt across five agents, merge the winner"** (README) as
  a default. Best-of-N burns budget N times; allowed only for drafts,
  with N ≤ 3, and never for anything that touches a live surface.
- **Nested runs** (a worker coordinating its own child run). Orca
  permits it with a depth limit; we forbid it — one controller only.
- **Group broadcast addresses** (`@all`, `@claude`, …). Noise in a
  markdown inbox; the controller addresses one task at a time.
- **Worker-to-worker messaging.** All messages go through the
  controller, matching the strict one-manager tree in Paperclip.

## Rules that do not change

Parallel execution is a speed tool, not an authority change:

1. **One controller** per run (the brand's CEO/CMO agent). Workers never
   coordinate each other.
2. **One writer per live surface** (website, each social account, email
   list, store). Parallel workers only ever **stage**; exactly one named
   agent publishes after fan-in and approval.
3. **Approval gates stay.** Anything in the brand's `about.md`
   approvals table, and every L3 item in `agency/shared/protocols.md`
   (money, credentials, legal, first public post), is still escalated
   to the owner — once, for the assembled package.
4. **Budgets stay.** Each worker still draws on its own Paperclip
   per-agent budget; a run declares its total cap up front.
