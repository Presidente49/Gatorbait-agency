<!-- Source: anthropics/knowledge-work-plugins (https://github.com/anthropics/knowledge-work-plugins) — Apache-2.0, Copyright (c) 2026 Anthropic, PBC. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
<!-- Modified from marketing/skills/campaign-plan/SKILL.md: rewritten brand-first, agent-mapped, output feeds campaign-board.md, invented benchmarks removed, approval gates added. -->
# Campaign Plan — Goal to Dated, Agent-Assigned Task Board

**Primary owner:** blueprint (Creative Strategist). Scout supplies baselines, scribe/hype/rank/bridge/webmaster receive tasks. Concepts only — no code vendored.

Turns one business goal ("sell 60 tickets to the wine night", "200 new newsletter signups before the season") into a campaign brief plus ready-to-paste rows for `agency/shared/campaign-board.md`. Nothing launches from this skill: it plans, the owner approves, agents execute through their own skills.

## Step 1 — Read the brand (brand-first)

Read `agency/brands/<slug>/about.md` (approvals, platforms, never-claim list), `goals.md`, `audience.md`, `offers.md`, `distribution.md`, `learnings.md`. Only then ask the owner for what is still missing:

| Input | Required? | If missing |
|---|---|---|
| Goal with a number and a deadline | Yes | Ask. Do not plan against "more awareness". |
| The offer being pushed (must exist in `offers.md`) | Yes | Ask; a campaign with no offer has nothing to link to. |
| Hard dates (launch, event, holiday) | Yes | Ask. |
| Budget | No | Plan owned + earned channels only; mark every paid line `BUDGET NEEDED — owner approval`. |
| Baseline numbers (current weekly signups, sales, CTR…) | No | Ask scout to pull them. If none exist, write `NO BASELINE` — never guess one. |

## Step 2 — Frame the campaign (one screen, no padding)

1. **Name** + one-sentence summary.
2. **Objective type** — pick one: awareness · consideration · conversion · retention · advocacy.
3. **Primary metric** — one number, defined *before* launch (per `agency/growth/ANALYTICS-LOOP.md` readback rules). Format: `<metric> from <baseline or NO BASELINE> to <target> by <date>`.
4. **Audience line** — "<who> who <pain/desire>, reached on <channels from audience.md>, cares most about <priority>."
5. **Message hierarchy** — (a) why care, (b) what the offer is, (c) why this business vs. alternatives including doing nothing, (d) the CTA. Each supporting point needs a proof point that exists in the brand files or can be verified; otherwise mark `[VERIFY]`. Nothing on the brand's never-claim list.

## Step 3 — Pick channels from what the brand actually runs

Only channels listed in `about.md` / `distribution.md`. Adding a new channel is a recommendation, not a plan line. For each chosen channel write: why it fits this audience, format, effort (low/med/high), owning agent.

| Channel type | Examples | Owning agent |
|---|---|---|
| Owned social | Page posts, reels, stories | hype (publishes), scribe (copy), blueprint (visuals) |
| Owned site | Landing page, article, menu/offer page | webmaster (build), rank (SEO), scribe (copy) |
| Email / SMS | Announcement, sequence | scribe via `marketing/email-sequence.md`; send needs approval |
| Earned | Partners, cross-promos, local press, groups | bridge |
| Paid | Boosts, search/social ads | Owner approval before any spend (always escalated) |

## Step 4 — Build the calendar backward from the hard dates

1. Put the fixed milestones on the calendar first.
2. Work backward with production lead times (use the brand's `learnings.md` if it records real ones; otherwise use these planning defaults and label them as defaults): social post 1–2 days · email 2–3 days · landing page 5–7 days · short video 3–5 days.
3. Check that the offer's link actually resolves (open it). If it doesn't, the first calendar row is fixing it and every post depends on that row.
4. Write dependencies explicitly ("landing page live before any post links to it"; "tracking UTMs set before first send").
5. Leave ~20% of slots open for reactive content.
6. Every post in the calendar links to the offer (agency rule: no linkless posts).

Calendar table:

| Date / week | Asset | Channel | Agent | Depends on | Approval needed |
|---|---|---|---|---|---|

## Step 5 — Measurement and kill criteria

- Primary metric (Step 2) + 2–4 secondary metrics, each with **where it is read** (platform insights, store/POS export, email tool report).
- UTM plan: `utm_source=<platform>&utm_medium=<social|email|partner>&utm_campaign=<campaign-slug>` on every outbound link.
- Mid-point check date and a kill/adjust rule ("if <metric> < 30% of target at the mid-point, move effort from <channel> to <channel>").
- Targets only from baseline × a stated assumption. No industry "benchmarks" invented to fill the table.

## Step 6 — Risks

2–3 real risks (date slip, offer not ready, channel under-delivers, weather/event cancellation) with one mitigation each.

## Step 7 — Output

Save to `agency/brands/<slug>/outputs/campaign-plan/<YYYY-MM-DD>-<campaign-slug>.md` with sections: Summary · Objective & primary metric · Audience & messages · Channels · Calendar · Budget (or "owned/earned only") · Measurement & kill rule · Risks · **Campaign-board rows**.

The campaign-board rows are paste-ready for `agency/shared/campaign-board.md` using the board's columns `| ID | Task | Agent | Status |`. IDs are `<BRAND>-<AGENT>-<NNN>` so they never collide with other brands on the shared board: `<BRAND>` = a 2–4 letter brand code, agent codes `S` scout, `SC` scribe, `H` hype, `B` blueprint, `R` rank, `BR` bridge, `WM` webmaster, `WR` wrench; status `PROPOSED`. Do not write them into the board until the owner approves the plan.

Append one line to `agency/brands/<slug>/outputs/log.md`: date, `campaign-plan`, blueprint, output path, QC result.

## Rules

- Plans only. No post, send, spend, or site change happens from this skill.
- Every paid line and every email send carries `Approval: owner` (or whoever `about.md` names).
- Never invent a baseline, benchmark, or proof point. Unknown = `NO BASELINE` / `[VERIFY]`.
- Run the brief through `marketing/quality-gate.md` (strategy rubric) before presenting.
- After the campaign ends, scout runs the readback; confirmed wins go to the brand's `learnings.md`.
