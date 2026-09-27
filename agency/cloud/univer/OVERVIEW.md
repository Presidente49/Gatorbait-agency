<!-- Source: dream-num/univer (https://github.com/dream-num/univer) — Apache-2.0. Adapted for Gator Bait Agency. -->

# Univer — Overview

**What it is:** Univer calls itself "The Office Harness for AI Agents" —
spreadsheets, docs, slides, canvas, relational tables, and PDF in one runtime
that both people and AI agents can work in. Apache-2.0. Includes an SDK, a
self-hostable workspace (univer-workspace), and a CLI for agents to create,
edit, inspect, and deliver Office content.

**The concept that matters for us:** agents that *write into real office
documents* instead of dumping markdown nobody opens.

- Agents generate spreadsheet-based mini-apps: decision dashboards,
  interactive reports, business dashboards.
- People and agents collaborate in the same files — a human can review what
  the agent built without learning the agent's tooling.
- Content composes across tools with linked data and references.

**Agency mapping:**

| Agent / pipeline | Univer-shaped output |
|---|---|
| Rank (SEO) | Keyword tracking as a living spreadsheet, not a chat message |
| Wrench (ops) | Weekly analytics digest as a dashboard workbook: spend, reach, revenue per brand |
| n8n `weekly-analytics-digest` workflow | Writes rows into a shared workbook instead of (or as well as) chat |
| Blueprint (creative) | Campaign briefs as real docs the client can comment on |
| White-label clients | Each brand gets workbooks it already knows how to read — no new UI to learn |

**Rule:** chat is for decisions, documents are for records. Anything a human
needs to re-read, compare week over week, or share with a client goes into a
real document — and agents should be the ones writing it.

**Deploy path:** concepts now; when the stack matures, self-host
univer-workspace on the VPS next to n8n, or use the Univer CLI in agent
pipelines to generate workbooks as build artifacts.
