<!-- Source: bytedance/deer-flow (https://github.com/bytedance/deer-flow) — MIT, Copyright (c) 2025 Bytedance Ltd. and/or its affiliates; (c) 2025-2026 DeerFlow Authors. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Run templates

These are the fill-in forms for `RUN-PROTOCOL.md`. Copy each form into the
run folder `agency/brands/<slug>/outputs/runs/<YYYY-MM-DD>-<run-slug>/`
and replace every `<…>` placeholder. A form that still contains a `<…>`
placeholder is not done.

## plan.md

```markdown
# Run plan: <request, in the requester's words>
- Run ID: <YYYY-MM-DD>-<run-slug> · Brand: <slug> · Controller: <name>
- Mode: interactive | unattended · Requested by: <who> · Date: <date>
- Goal: <one sentence> · Money metric it moves: <e.g. weekend orders, AOV>
- Limits: delegations <n>/5 · parallel <n>/3 · attempts per scope 2 · spend $<0 or approved line>

## Clarifications (step 1)
| # | Trigger | Question | Answer, or assumption, or [VERIFY] |
|---|---|---|---|

## Assumptions (reversible only; each one is listed in the report)
- <assumption>

## Steps
| # | Step | Direct/Delegated (agent) | Depends on | Gate |
|---|---|---|---|---|
| 1 | <step> | Delegated (scout) | — | none |
| 4 | <step> | Direct | 2,3 | L3 → CP-1 |
```

## delegations.md (one record per worker)

```markdown
## D-<n>: <agent> — <scope title>
- Scope: <one bounded job> · Out of scope: <…>
- Context given: <paths + facts; the worker sees nothing else>
- Expected output: workspace/<file>
- Side-effect ownership: none (drafts only) | <exact live action + channel, gated by CP-n>
- Allowed skills/tools: <skills-library files, tools>
- Acceptance criteria:
  1. <objectively checkable>
- Limits: 2 attempts · deadline <…>

### Return (filled by worker)
- Status: completed | failed | blocked · Stop reason: none | loop_capped | turn_capped | token_capped
- Deliverables: <path per deliverable>
- Criteria: 1 <met/not met + evidence> …
- Failed / skipped / uncertain: <…, or "none">

### Verification (filled by controller)
- Criteria: 1 holds | does not hold | UNVERIFIED — <what was checked>
- Action: accept | repair criterion <n> | carry as uncertain
```

## checkpoints.md

```markdown
| CP | What exactly | Level | Artifacts | Channel | Approver | Decision | Date | Evidence after action |
|---|---|---|---|---|---|---|---|---|
| CP-0 | Run plan | auto / L3 | plan.md | — | <name> | approved / auto-approved / rejected / pending | | — |
| CP-1 | <exact action> | L3 | workspace/<file> | <one channel> | <name from about.md> | pending | | <URL / post ID / screenshot> |
```

Each approval covers one action on one channel, once. A CP that says
`pending` blocks that action.

## report.md

```markdown
# Run report: <run-id>
- Outcome: done | partial | blocked | failed · Blocker: none | needs_user_input | external_wait | missing_evidence | run_failed
- Goal met? <yes/no + the evidence>
- Limits used: delegations <n>/5 · repairs <n> · spend $<n>

## Delivered (evidence per item)
| Item | Path / URL / ID | Verified how |
|---|---|---|

## Open items (who must do what)
- <CP-n pending: approver decision on …>

## Assumptions made
- <from plan.md>

## Uncertain (UNVERIFIED carried forward)
- <…, or "none">

## Learnings
- Brand: <line appended to brand learnings.md>
- Shared: <line appended to agency/shared/learnings.md, or "none">
```

## outputs/log.md line

```
<date> | <controller> | run <run-id>: <request> | outputs/runs/<run-id>/report.md | <outcome>; QC <pass/fail>
```
