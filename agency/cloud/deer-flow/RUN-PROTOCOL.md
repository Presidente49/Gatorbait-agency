<!-- Source: bytedance/deer-flow (https://github.com/bytedance/deer-flow) — MIT, Copyright (c) 2025 Bytedance Ltd. and/or its affiliates; (c) 2025-2026 DeerFlow Authors. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Run Protocol: how the controller works one task from request to report

A **run** is one request worked from start to finish, for example "launch a
weekend special campaign". This runbook covers the path from the request
to a verified report. It sits under the Paperclip layer: Paperclip decides
*which* task gets worked and by whom (`agency/cloud/paperclip/`). This
runbook decides *how* that task is worked. For fill-in forms, see
`TEMPLATES.md` in this folder.

## Roles: one controller, workers, one approver

| Role | Who | Can | Cannot |
|---|---|---|---|
| **Controller** | The brand's single lead (Marlowe/CEO in the Paperclip mapping, the "CMO" in `protocols.md`). **Exactly one per brand.** | Clarify, plan, delegate, verify, write the report | Approve its own gated actions or act as a second controller |
| **Worker** | One of the 8 agents, named in a delegation record | Do the scoped work inside the run folder and return a report | **Delegate further**, touch anything outside its allowlist, or take a gated action |
| **Approver** | The human named in the brand's `about.md` approvals table | Approve or reject a checkpoint | (human) |
| **Wrench** | The ops agent | Keep run folders tidy, append `outputs/log.md`, archive old runs, flag stale BLOCKED runs | Plan, delegate or approve. Wrench does housekeeping and has no authority over the work. |

Only the controller delegates. A worker that needs help returns
`status: blocked` with the reason, and the controller decides what happens
next. This keeps the org chart a strict tree.

## Run folder (the workspace boundary)

Each run gets its own folder. **Workers write only inside it.** Anything
that leaves the folder (a post, a send, a site edit, a spend) happens only
at step 6, after an approved checkpoint.

```
agency/brands/<slug>/outputs/runs/<YYYY-MM-DD>-<run-slug>/
  plan.md            # step 2: goal, assumptions, steps, gates
  delegations.md     # step 3: one record per worker, with its return block
  workspace/         # drafts, copy, images, schedules (never live)
  checkpoints.md     # step 4: every gate, with the approver's decision
  report.md          # step 7: outcome, evidence, what is still open
```

Also add one line per run to `agency/brands/<slug>/outputs/log.md`
(`date | agent | task | output path | QC result`, the format in
`protocols.md`). Create the file if it does not exist.

## Run limits (set in plan.md before the first delegation)

| Limit | Default | When it is hit |
|---|---|---|
| Delegations per run | **5** | Stop delegating. Finish directly or report what remains open. |
| Workers at the same time | **3**, and only for independent scopes | Queue the rest. |
| Attempts per worker scope | **2 identical attempts**, then stop (loop breaker) | Mark the scope `loop_capped` and report it. |
| Spend | **$0** unless the plan names a budget line that the approver has approved | Any spend is an L3 gate. |

Paperclip budgets cap cost per agent per month. These limits cap scope per run.

## Two interaction modes

- **Interactive:** the approver is reachable during the run. Ask clarifying
  questions *before* any work starts (step 1).
- **Unattended:** a heartbeat or scheduled run with no human available.
  **Never wait for an answer.** For low-risk, reversible work, make the
  smallest assumption, write it under *Assumptions* in plan.md, and
  continue. For anything gated or irreversible, stop with a `BLOCKED`
  report that names the missing decision. Stage the drafts, and leave the
  checkpoint `pending`.

## Step 1: Clarify before acting

Read the brand pack: `about.md`, `offers.md`, `goals.md`, `brand-voice.md`
and `learnings.md`. Then check the request against these five triggers. Any
trigger that fires is either asked (interactive) or recorded as an assumption
or BLOCKED (unattended). This happens **before** any work, never partway
through.

| Trigger | Pizza-shop example |
|---|---|
| Missing information | Which item is the special? What is the price? Which dates? |
| Ambiguous requirement | Does "weekend" mean Friday to Sunday or Saturday to Sunday? |
| Approach choice | Organic only, or boosted? Email, or social only? |
| Risk confirmation | Will a public post go up, money be spent, or a list be emailed? |
| Suggestion | "I recommend adding a pinned comment with the order link. OK?" |

**A fact the business owns** (a price, a date, a menu item, an allergen) is
never assumed. Mark it `[VERIFY]` and route it to a checkpoint.

## Step 2: Plan

Write `plan.md` using the TEMPLATES.md form: the goal, the money metric it
moves, assumptions, numbered steps, and run limits. Mark each step as
**direct** (the controller does it) or **delegated** (with the named agent).
Mark each gated step with its level (L3 = escalate, per `protocols.md`). Use
a plan only when the work has 3 or more steps. For 1 or 2 steps, just do the
work and write the report.

**Plan checkpoint:** before any delegation, record the plan as CP-0 in
checkpoints.md. The approver must approve CP-0 when either of these holds:
- the plan contains any L3 step, or
- this is the brand's first run of this kind.

Otherwise CP-0 is recorded as auto-approved under standing rules
(`protocols.md`, "Default is GO").

What happens while CP-0 is waiting depends on the mode:
- **Interactive:** wait for the CP-0 decision before delegating.
- **Unattended:** set CP-0 to `pending` and continue with the drafting
  steps only. They stay inside the run folder and can be reversed. The
  approver then reviews the plan and the drafts together. No gated step
  runs until CP-0 and that step's own checkpoint are both `approved`.

## Step 3: Delegate only when it clearly pays

Direct work is the default. Before each delegation, compare benefit and cost:

- **Benefit:** a specialist skill (the worker's identity or skills) or
  isolation (the task would bury the controller in detail) or real time
  saved by independent parallel scopes.
- **Cost:** handoff overhead, the worker re-reading context the controller
  already has, reconciling results, and the risk of state conflicts or side
  effects.

Delegate only when the benefit clearly wins. **Hard no to parallel work**
when one scope needs another scope's output, or when two scopes touch the
same file, list, account or post. Put dependent work in sequence.

Every delegation gets a record in `delegations.md` (TEMPLATES.md form)
before the worker starts:

1. **Scope:** one bounded job. Say what is out of scope.
2. **Context given:** the file paths and facts from this run that the
   worker needs. Workers still do their normal startup (identity plus
   brand pack, per `protocols.md`), but they do not see the controller's
   conversation, other workers' drafts or earlier runs unless this list
   names them. If something is not listed, assume the worker does not
   know it.
3. **Expected output:** the file path or paths inside `workspace/`.
4. **Side-effect ownership:** which live actions this worker may take.
   The default is **none**, meaning drafts only.
5. **Allowed skills and tools:** an allowlist. Nothing outside it.
6. **Acceptance criteria:** 1 to 5 checks that can be tested objectively.
7. **Limits:** attempt cap, and the deadline if one applies.

The worker returns a **return block** (TEMPLATES.md form) in the same
record:
- a status of `completed`, `failed` or `blocked`, plus a stop reason if a cap ended it
- a path for every deliverable
- each criterion answered, with evidence
- what failed, what was skipped, and what is uncertain

A claim with no handle does not count.

## Step 4: Gate check (fail closed)

Before **any** action leaves the run folder, check it against the gate list.
**If in doubt, it is gated.** If the approver or the rule is unclear, treat
it as denied until that is resolved (fail closed).

Always L3, with a human checkpoint and no exceptions:
- publishing or scheduling anything public: posts, emails, site or CMS changes, ads
- spending money, including boosts, ads, paid tools and print orders
- accounts and credentials: creating, connecting or changing them
- deleting anything that cannot be recovered
- the first public post of a new brand or format
- anything on the brand's own `about.md` approvals table that names a person

**If there is no approver:** when the brand's `about.md` names no person
for a gated action (a fresh brand has an empty table), the checkpoint is
`pending` with blocker `needs_user_input`. The fix is to fill in
`about.md`. The controller **never** fills that gap by approving the
action itself.

A deterministic check does **not** replace the human. It only catches
problems earlier. Each gated action gets its own checkpoint entry
(CP-1, CP-2 and so on) listing the exact artifacts to approve. An approval
covers **only** those artifacts on **only** that channel, once. It is not a
standing approval for future sends.

## Step 5: Verify

For each delegation, grade every acceptance criterion:

- **holds:** checked against the artifact itself. Reuse the output.
- **does not hold:** repair *only* that criterion, by a direct fix or one
  re-scoped delegation. Never restart the whole task. If the repair needs a
  fact the business owns (a price, a link, a date), do **not**
  re-delegate, because that only repeats the same attempt. Carry the
  criterion as a blocker on the checkpoint it affects.
- **UNVERIFIED:** there is no evidence either way. Check the artifact
  yourself. If you still cannot confirm it, carry it into the report as
  uncertain. Never count it as a pass.

`completed` from a worker means the work finished. It does **not** mean the
work was accepted. Spot-check load-bearing facts (prices, dates, names,
links) against the brand pack even when every criterion holds. Then run the
quality gate in `protocols.md`.

## Step 6: Act (only what was approved)

Take only the actions whose checkpoint reads `approved`. There is one writer
per live surface, and it is the agent named in that action's side-effect
ownership. Record evidence for each action: a live URL, a scheduled-post
ID or a screenshot path. "Done" without evidence is not done.

## Step 7: Report and close the loop

Write `report.md` (TEMPLATES.md form):
- **Outcome:** `done`, `partial`, `blocked` or `failed`
- **Blocker type** if not done: `needs_user_input`, `external_wait`,
  `missing_evidence` or `run_failed`
- evidence for each approved action, and what is still open
- limits used, for example delegations 3/5

Then:
1. Add the line to `outputs/log.md`.
2. Add lessons to the brand's `learnings.md`. Lessons that hold for any
   business also go into `agency/shared/learnings.md`. These entries are
   the *retain* step in `agency/cloud/hindsight/AGENCY-MEMORY-MODEL.md`.
3. Update the Paperclip task status: `in_review` if a checkpoint is
   pending, `done` only if the outcome is `done` with evidence.

A `blocked` run is a valid, complete report. It is never a silent stall.
Wrench flags any BLOCKED run that has had no approver decision for 48 hours.
