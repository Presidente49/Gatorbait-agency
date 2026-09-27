<!-- Source: stablyai/orca (https://github.com/stablyai/orca) — MIT, Copyright (c) 2026 Lovecast Inc. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Parallel Runbook — run N agents at once, safely

Use this when one job for one brand can be split across several agents
working at the same time. Concepts come from Orca's orchestration model
(see `OVERVIEW.md`). It extends — never replaces —
`agency/shared/protocols.md` and the Paperclip control plane.

**Roles.** The **controller** is the brand's CEO/CMO agent (the one the
escalation table calls "CMO"). It alone creates the run, writes the
board, answers questions, and does the fan-in review. **Workers** are
the specialist agents (scout, scribe, blueprint, …). The **publisher**
is the one agent named to touch the live surface after approval.

---

## 1. Decide: parallel or waterfall?

Parallelize only if **all five** are true. Otherwise use the normal
waterfall in `protocols.md`.

| # | Test | Fails when… |
|---|---|---|
| 1 | **Independent inputs** — every task can start from the frozen brief alone | Scribe needs Scout's finding before it can write a word |
| 2 | **Disjoint write sets** — no two tasks write the same file or folder | Two agents both "update the landing page copy" |
| 3 | **No live writes** — no task publishes, sends, spends, deletes, or edits a live site/account | A task says "post it" or "change the menu price on the site" |
| 4 | **Worth it** — ≥ 2 tasks each take real time; parallel saves wall-clock | Three 2-minute chores |
| 5 | **Budget declared** — run cap fits inside each agent's remaining budget | Any worker is near its monthly cap |

Limits: **max 4 workers per run**, **one level only** (workers never
start workers), **best-of-N drafts ≤ 3 and drafts only**.

Soft dependencies are fine: resolve them by **locking the shared fact in
the brief** (headline, price, dates) so nobody waits on anybody. The
fan-in review checks everyone used it.

---

## 2. Create the run (controller)

Run id format: `YYYY-MM-DD-<short-job-name>` (lowercase, hyphens).

```sh
BRAND=agency/brands/<slug>
RUN=$BRAND/outputs/parallel/<run-id>
mkdir -p "$RUN"/{tasks,claims,inbox,workspaces}
```

Layout (who may write what):

```
outputs/parallel/<run-id>/
  RUN.md            controller only — objective, brief pointer, cap, publisher
  brief.md          controller only — FROZEN shared inputs; workers read-only
  board.md          controller only — the status board (one writer)
  tasks/<T>.md      controller only — one task spec per task
  claims/<T>.md     created once by the worker that checks the task out
  inbox/            append-only; anyone adds NEW files, nobody edits one
  workspaces/<T>/   that task's worker only — drafts, status.md, report.md
  REVIEW.md         controller only — fan-in review
  package/          controller only — the assembled, approved-for-staging result
```

**Naming (so files sort and never collide):**
- Timestamp: `ts=$(date -u +%Y%m%dT%H%MZ)` → `20260927T0409Z`.
- Worker → controller: `inbox/<ts>-<T>-ask.md`, `-escalation.md`, `-done.md`.
- Controller → worker: `inbox/<ts>-controller-<T>-reply.md`, `-followup.md`;
  to everyone: `inbox/<ts>-controller-all-<topic>.md`.
- Task ids: `T<n>-<agent>` (e.g. `T2-scribe`). Reports: `report-a<k>.md`
  (k = attempt). Claims: `<T>.md` for attempt 1, `<T>.attempt<k>.md` after.

### RUN.md template

```markdown
# Run <run-id>
- Objective: <one sentence, traceable to goals.md>
- Controller: <agent>   Publisher (after approval): <agent>
- Brief: brief.md (frozen at <time>)   Deadline: <date/time>
- Budget cap for the run: <amount or token/credit cap>; per-worker: <cap>
- Tasks: <T1 agent>, <T2 agent>, <T3 agent>
- Approval needed from: <name/role from about.md> for <which actions>
  (approvals table still blank? → the owner approves everything and
  nothing publishes until it is filled)
- Live surfaces touched by this run: NONE until fan-in + approval
```

### brief.md — the frozen shared input

Everything two workers must agree on goes here **before** dispatch:
offer facts (price, dates, terms), the locked headline or angle, brand
files to read, sizes/formats, deadline. After dispatch it is **frozen**.
If it must change, the controller writes `brief.md` v2, adds a
`inbox/<ts>-controller-all-brief-changed.md` note naming the change, and
every worker re-reads it at its next checkpoint (step 4).

---

## 3. Write task specs (controller)

One file per task, `tasks/T1-<agent>.md`, `T2-…`. Every spec has the
five fields (Orca's task-spec contract). **Missing field → not
dispatched.**

```markdown
# T<n> — <agent> — <short title>
- Target: <exact files/inputs in scope; what to read>
- Change: <the concrete result to produce>
- Constraints: <brand voice/facts rules; do-not-touch list; "no live writes">
- Ownership: may write ONLY workspaces/T<n>-<agent>/ ; reads brief.md + <brand files>
- Observable acceptance: <files that must exist + checks that must pass>
- Depends on: none   (or a task id — then it goes in a later wave)
```

Dependencies: put a task that truly needs another's output in a
**later wave**. Waves no deeper than 3. Start the whole independent
wave before waiting on anything.

Then write `board.md` with every task in `todo`:

```markdown
# Board — <run-id>   (writer: controller only; updated <time>)
| Task | Agent | Status | Attempt | Last checkpoint | Output |
|---|---|---|---|---|---|
| T1-scout | scout | todo | – | – | – |
```

Status values: `todo → in-progress → in-review → done`, plus `blocked`,
`failed`. Only the controller moves a row.

---

## 4. Worker: claim, work, report

### 4a. Claim (atomic checkout)

Claim only a task whose spec names **you** as the agent. A claim is
created **once**, with a command that fails if the file already exists —
so two agents can never both own a task:

```sh
RUN=agency/brands/<slug>/outputs/parallel/<run-id>   # from RUN.md
( set -o noclobber
  printf '%s\n' "# Claim T1-scout" "- agent: scout" "- attempt: 1" \
    "- claimed: $(date -u +%FT%TZ)" \
    "- writes: workspaces/T1-scout/" \
    "- reads: brief.md, <brand files>" \
    "- live surfaces: none" > "$RUN/claims/T1-scout.md" ) \
  || echo "ALREADY CLAIMED — stop, do not work this task"
mkdir -p "$RUN/workspaces/T1-scout"
```

If Paperclip is running, its atomic task checkout **is** the claim and
this file mirrors it. Never edit or delete another agent's claim.
Only the controller may **void** a bad claim (wrong agent, stale run):
it renames it to `claims/<T>.void-<ts>.md`, appends one line saying
why, and the named agent claims again with the same command.

### 4b. Work inside your workspace only

- Write only under `workspaces/<T>/`. Read `brief.md` and brand files;
  never write them.
- Code tasks only (webmaster/wrench changing repo files): isolate in a
  git worktree on its own branch, and record its path in the claim:
  `git worktree add ../<repo>-<run-id>-<T> -b parallel/<run-id>/<T>`.
  Content tasks use the folder workspace — no git needed.
- Stuck on a question only the controller can answer? Write
  `inbox/<ts>-<T>-ask.md` (question + options), then keep working on
  anything not blocked by it, or wait. Never guess on facts, prices,
  names, or anything in the approvals table.
- Blocked entirely? `inbox/<ts>-<T>-escalation.md` with the reason.

### 4c. Checkpoints

At each natural checkpoint (a section finished, a hypothesis
confirmed, before starting the next file) **and once right before
reporting**:

1. Append one line to `workspaces/<T>/status.md`:
   `<ts> | <phase: researching|drafting|checking|blocked> | <what just happened; next step>`
2. Look in `inbox/` for files addressed to your task or `all`
   (`<ts>-controller-<T>-*.md`, `<ts>-controller-all-*.md`). Apply them.
   A status line is proof of life, **not** proof of done.

### 4d. Report exactly once per attempt

Write `workspaces/<T>/report-a<k>.md`, then drop
`inbox/<ts>-<T>-done.md` containing one line:
`report: workspaces/<T>/report-a<k>.md`. Never overwrite an earlier
attempt's report. On a retry, copy every file you are about to change
to `<name>.a<k-1>.md` first, so the review can see what changed.

```markdown
# Report T<n>-<agent> (attempt <k>)
- outcome: succeeded | failed        ← required; never hide failure in prose
- summary: <3 sentences: what was produced; what was found; what remains>
- files: <real paths only>
- acceptance: <each acceptance check from the spec → pass/fail + evidence>
- facts used from brief: <list — lets the controller check consistency>
```

After reporting, **stop**. No polishing, no new work, no touching
other workspaces. New instructions arrive as a new attempt or task.

---

## 5. Controller: supervise

Loop until every task is `done` or `failed`:

1. Read **all** new inbox files, oldest first. Answer each `ask` with
   `inbox/<ts>-controller-<T>-reply.md`. Move board rows accordingly.
   Record in `board.md` the last inbox file processed, so nothing is
   skipped or handled twice.
2. For each `done` note: open the report, check `outcome`, check the
   files exist, move the row to `in-review`.
3. **Silence is not failure.** A worker with no new status line is
   `unverified`: re-check later, or ask it. Do **not** start a second
   worker on the same task without **positive proof** the first
   stopped (it reported `failed`, or its session is confirmed ended with
   no report).
4. **Retry** = new attempt on the same task: controller edits the task
   spec with the fix, deletes nothing, and the worker appends a new claim
   file `claims/<T>.attempt<k>.md` (same noclobber command) naming
   `retry-of: attempt <k-1>`. **Three failed attempts → task `failed`,
   escalate.** Do not route around it with a new run.
5. Steering a running worker: `inbox/<ts>-controller-<T>-followup.md`.
   Workers only see it at their next checkpoint — plan for that lag.

---

## 6. Fan-in review (controller only)

When every row is `in-review` or `failed`, write `REVIEW.md`:

```markdown
# Fan-in review — <run-id>
## Per task
| Task | Outcome | Acceptance met? | Quality gate (voice / playbook / facts / no L3) | Verdict |
## Cross-task consistency
- Brief facts vs each output: <price/dates/headline/names — match? cite line>
- Contradictions between outputs: <none | list>
- Overlap / duplicate work: <none | list>
## Fixes routed (controller does not edit worker files)
- <T> attempt <k+1>: <exact fix>
## Assembly
- package/ contents: <files, copied from workspaces, sources noted>
## Gates
- Needs owner approval: <what, from whom — per about.md>
- Publisher after approval: <agent> — must check live state first
## Disposition
| Task | Final state | Next owner |
```

Rules:
- **Review authorizes synthesis, not edits.** If a worker's output
  needs a change, route it back as a new attempt to that worker. The
  controller only **copies** accepted files into `package/` and writes
  the glue (cover note, checklist).
- **Consistency is the new risk.** Parallel drafts written from the same
  brief can still disagree (one says "4–9 pm", another "4–10 pm").
  A worker's own "acceptance: pass" is a claim, not evidence — check
  every locked brief fact in every output yourself, mechanically:

  ```sh
  W=$RUN/workspaces
  grep -lF "<locked headline>" $W/*/*.md          # must list every output that shows it
  grep -noE "<pattern for hours/price/date>" $W/*/*.md   # every hit must equal brief.md
  grep -niE "<banned words from brief.md>" $W/*/*.md     # must print nothing
  ```
  Exclude `report-a*.md` and `*.a<k>.md` from verdicts (they quote old values).
- Run the normal quality gate from `protocols.md` on the assembled
  package, once.

---

## 7. Close the run

1. **Approval:** send the package to the approver named in the brand's
   `about.md` (one request for the whole package — not one per worker).
2. **One writer publishes:** after approval the publisher (e.g. hype
   for social, webmaster for the site) posts. Before any post/send/
   re-post, **check the live surface first** — if it's already there,
   don't do it again (a lost confirmation is not proof it didn't happen).
3. **Merge code** (code tasks only): controller merges one worktree
   branch at a time after review, then removes the worktree. Never
   merge two parallel branches blind.
4. **Disposition:** every board row ends `done` or `failed` with a next
   owner. The run isn't closed while any row lacks one.
5. **Log + learn:** one line in `outputs/log.md` — create the file if
   the brand has none yet — (date, `controller`,
   `parallel run <run-id>`, `outputs/parallel/<run-id>/package/`, QC
   result). Append what the run taught to the brand's `learnings.md`,
   and to `agency/shared/learnings.md` if it holds for any business.

---

## Quick checklist

- [ ] 5 parallel tests pass; ≤ 4 workers; no live writes in any task
- [ ] RUN.md + frozen brief.md + one five-field spec per task
- [ ] Every worker claimed with noclobber; one claim per attempt
- [ ] Each worker wrote only its workspace; status lines at checkpoints
- [ ] Exactly one report per attempt, explicit outcome
- [ ] Controller processed every inbox file; no duplicate workers
- [ ] REVIEW.md: consistency checked against brief; fixes routed, not made
- [ ] One approval request; one publisher; live state checked before posting
- [ ] Every row has a final state + next owner; log.md + learnings updated
