<!-- Source: paperclipai/paperclip (https://github.com/paperclipai/paperclip) — MIT. Adapted for Gator Bait Agency. -->

# Agency → Paperclip Mapping

How the 8 agency agents map onto Paperclip's company/agent model. One
Paperclip instance; **one company per white-label brand** (Gator Bait
Media is company #1; each new `new-brand.sh` client becomes another
company with its own goal, agents, and budget).

## Org chart

```
CEO (Marlowe — strategy, delegation, approvals)
├── Scout      — research agent
├── Scribe     — writing agent
├── Hype       — social publishing agent
├── Blueprint  — creative/design agent
├── Rank       — SEO agent
├── Bridge     — outreach agent
├── Webmaster  — web agent
└── Wrench     — ops agent
```

- Each agent = a Paperclip employee: role + reporting line (all report
  to CEO/Marlowe), capabilities description, adapter config, per-agent
  monthly budget, status.
- New brand onboarding = new company: same 8 roles re-instantiated
  under the brand's goal, reading `agency/brands/<slug>/`.
- Keep the tree strict: every agent reports to exactly one manager.
  Escalation and delegation flow through the chain — no side channels.

## Heartbeat patterns for always-on ops

Paperclip heartbeats are short wake-windows, not 24/7 loops. Map our
existing schedules onto heartbeat triggers:

| Agency rhythm | Heartbeat trigger | Cadence |
|---|---|---|
| Article money pipeline (3–5 packages/day) | Schedule | Daily ~08:24 |
| Gators news digest | Schedule | Daily ~07:24 |
| Drive upload watch | Schedule | Every 10 min |
| Carousel comment watch | Schedule | Every 10 min |
| FB engagement sweep | Schedule | Every 12 h |
| Bot watch sweep | Schedule | Every 12 h |
| Weekly SEO digest | Schedule | Weekly Mon |
| Merch ads stop | Schedule | Run-once |
| New comment / new task assigned | Assignment / @-mention | Event-driven |
| Brenden taps "go" in chat | Manual invoke | On demand |
| Approval resolved | Approval resolution | Event-driven |

**Heartbeat protocol for each agent** (adapted): check identity (read
brand pack + role) → review assignments → pick highest-priority task →
atomic checkout → do the work → update status + append learnings.

## Task model

- Every unit of work is a task with one assignee, one parent, and a
  status (`backlog → todo → in_progress → in_review → done`).
- Tasks trace back to the brand's goal — if a task doesn't serve the
  goal, it doesn't get done.
- Atomic checkout: only one agent owns a task at a time. (Our
  no-double-post / no-duplicate-reel rules are the content-side version
  of this.)

## Budget & governance per brand

- **Per-agent monthly budgets** (in cents, Paperclip's unit): set a
  spend cap per agent per brand. When an agent hits its limit, it stops.
  No runaway API costs on a client's dime.
- **Per-company budget**: each brand company gets a monthly ceiling;
  the CEO sees burn across all companies in one dashboard.
- **Governance gates** (human = Brenden): hiring new agents, CEO
  strategy changes, and anything irreversible (deletions, money
  movement, credentials) require board approval. Everything else runs
  on standing rules.
- **Audit trail**: every mutation logged — who did what, when, to
  which task. This is our ops-log discipline, enforced by the system
  instead of by habit.

## Skill Studio ↔ skills-library

Paperclip's Skill Studio (org-wide shared skills, evals, saved test
runs) is the productized version of our `skills-library/` + brand
`learnings.md` loop. Direction of travel: keep authoring skills as
markdown in the repo (portable, reviewable), and let Paperclip be the
runtime that serves, versions, and evaluates them.
