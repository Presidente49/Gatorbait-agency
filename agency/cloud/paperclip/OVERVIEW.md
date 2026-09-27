<!-- Source: paperclipai/paperclip (https://github.com/paperclipai/paperclip) — MIT. Adapted for Gator Bait Agency. -->

# Paperclip — Overview

**What it is:** Paperclip is the open-source app for managing teams of AI
agents at work. Its own tagline: *"If OpenClaw is an employee, Paperclip is
the company."* A Node.js server + React UI that orchestrates agents toward
business goals. Bring your own agents (Claude Code, Codex, Cursor, shell,
HTTP webhooks — "if it can receive a heartbeat, it's hired"), assign goals,
and track work and costs from one dashboard.

**License:** MIT (Copyright (c) 2025 Paperclip AI) — clean, no commercial
carve-out. Safe to adapt concepts and, if wanted, to run or fork the app.

**The four pillars** (Paperclip's framing, adapted):

| Pillar | What it covers | Agency equivalent |
|---|---|---|
| Agentic Task Manager | Declare intent; agents work; you verify | Hype/queue workflows, approval gates |
| Org Chart for Agents | Roles, permissions, boundaries | Our 8 agents + per-brand scoping |
| Agent Employee Training | Skills studio, evals, learning loops | skills-library + brand learnings.md |
| Agentic OS | Runtimes, sandboxing, SSO, cost controls | cloud/ (n8n, scheduler), budgets |

**Core concepts that matter for the agency:**

- **Organization** — top-level unit: a goal, employees (agents), org
  structure, monthly budget, task hierarchy. One Paperclip instance runs
  **multiple companies** — this maps 1:1 onto our white-label brands:
  each client brand becomes a Paperclip company with its own goal,
  agents, and budget.
- **Agents** — every employee is an agent: adapter (how it runs), role
  and reporting line, capabilities, per-agent budget, status
  (active/idle/running/error/paused/terminated). Strict tree hierarchy —
  every agent reports to exactly one manager.
- **Tasks (issues)** — the unit of work: title, description, status,
  priority, one assignee, parent task (traceable to the company goal).
  Lifecycle: `backlog → todo → in_progress → in_review → done`
  (plus `blocked`). Claiming a task is an **atomic checkout** — one
  agent at a time, no double-work.
- **Heartbeats** — agents don't run continuously; they wake in short
  execution windows triggered by schedule, new assignment, @-mention,
  manual invoke, or approval resolution. The heartbeat protocol: check
  identity → review assignments → pick work → check out task → do work
  → update status.
- **Governance** — board (human) approvals for hiring agents and CEO
  strategy; board can pause/resume/terminate any agent and reassign any
  task. Full activity audit trail.
- **Agent Companies spec** (`agentcompanies/v1-draft`) — a
  vendor-neutral, markdown+YAML-frontmatter format for describing
  companies, teams, agents, projects, tasks, and skills
  (`COMPANY.md`, `TEAM.md`, `AGENTS.md`, `PROJECT.md`, `TASK.md`,
  `SKILL.md`). GitHub-native, no registry required, attribution must
  survive import/export. Our repo layout already rhymes with this —
  aligning to it keeps us portable.

**Why it matters for the agency:** it is the missing management layer.
We have 8 specialist agents, skills, a studio, and cloud automation —
but no control plane: no org chart, no task queue with ownership, no
budgets, no heartbeat schedule, no audit trail. Paperclip is exactly
that layer, and it's MIT.
