<!-- Source: coreyhaines31/marketingskills (https://github.com/coreyhaines31/marketingskills) — MIT. Adapted for Gator Bait Agency. -->
# Loop Spec — The Always-On Operating System

**Owner:** all agents via wrench. A loop turns a marketing task you'd otherwise do manually (and forget) into an always-on system. This is how the agency compounds learning across brands: loops check, act, log, and feed the playbook.

**Banned framing:** "set it and forget it", "fully autonomous marketing", "10x on autopilot". Loops are disciplined systems with checkpoints, not magic.

## The 9-part anatomy

Every agency loop must define all nine. A loop missing a stop condition, a self-check, or its state handling is a liability, not an asset.

| Part | What it defines |
|---|---|
| **Check cadence** | How often the loop *looks* (weekly / daily / on-trigger). Match to signal speed. |
| **Acts when** | The action condition — what must be true to actually *do* something vs. just check and skip. Most runs of a good loop are "checked, nothing to do." |
| **Purpose** | The one outcome this loop exists to move. |
| **Skills used** | Which agency skills/agents the loop orchestrates each iteration. |
| **Loop body** | The ordered steps run each iteration. |
| **Self-check** | Verification *before* acting — so the loop doesn't act on noise, seasonality, or a tracking bug. |
| **State / idempotency** | What the loop remembers: last-run marker, dedupe key, cooldown window, "already handled" set. Without this, loops double-act, re-nag, or re-alert. Non-negotiable. |
| **Stop / bail-out** | When the loop skips, halts, escalates, or disables itself — plus what it does on error. Every loop needs one. |
| **Output** | Where results go: a file, a staged draft, a notification, a report. |

**Check cadence ≠ acts when.** A loop might *check* daily but only *act* when a threshold is crossed inside a cooldown window. Conflating the two produces loops that miss the window or spam.

## The cadence rule

Match cadence to how fast the signal actually changes, not how often you'd like an update.

| Signal | Realistic cadence |
|---|---|
| Rankings, backlinks, domain authority | Weekly (they move slowly; daily is noise) |
| Ad creative fatigue, CPA drift | Every 2–3 days (Meta/Google feedback loops are days, not hours) |
| Funnel conversion | Weekly (needs enough volume to be significant) |
| Mentions, comments, social listening | Daily (engagement windows close fast) |
| Content decay | Monthly (traffic erosion is gradual) |
| Competitor changes | Weekly |

Over-frequent loops are the most common failure mode: busywork, burned budget, and outputs nobody reads. A loop nobody acts on should be deleted, not kept.

## The two-tier action model

Classify every action a loop can take. This mirrors the agency's standing rule: only interrupt the owner for money, deletions, credentials, CAPTCHAs, and licensing.

**Tier 1 — Autonomous-safe** (a loop may do these unattended): read data, analyze, diff, score, **draft**, **stage** for review.

**Tier 2 — Gated** (needs a checkpoint by default): **spend** money, **shift budget**, **send** messages, **publish** anything public, **delete/suppress** records, **change** live account settings.

A Tier-2 action runs without per-action approval only if explicitly authorized AND bounded by caps + an allowlist. Otherwise: stage a draft, human approves.

### Spend guardrails (paid loops)
- Hard daily/weekly spend ceiling — halt and alert if approached.
- Per-run change limit (e.g., ≤20% budget movement) so one bad read can't reallocate everything.
- Allowlist: only specified accounts/campaigns are eligible for autonomous changes.
- Judge on revenue/ROAS, never on proxy metrics alone — never optimize CTR into a revenue loss.

### Publish & send guardrails
- Default to staging queue + human approval for anything public or outbound. Auto-drafting is fine; auto-publishing is not.
- Volume caps per run and per recipient. Check suppression/unsubscribe/do-not-contact lists every send.
- Platform ToS: respect rate limits and automation rules; don't auto-act where detection bites (owned social replies, community actions staged for humans).

### Always escalate (never fully autonomous)
Negative/crisis brand mentions · responses to complaints or legal/medical/financial-sensitive issues · newsjacking angles (human veto first) · anomalies in revenue or ad spend (flag, don't self-correct) · anything deleting data or contacting a large audience at once.

### Kill switch
Every scheduled loop has a manual off switch, and there is a documented way to stop **all** loops fast. A loop you can't stop quickly is a liability. No raw PII in loop state or run logs — use internal IDs.

## Agency loop catalog (adapt the closest match)

| Loop | Cadence | Acts when | Owner |
|---|---|---|---|
| **Keyword-gap** | Weekly | Striking-distance keyword (positions 5–20) has no adequate page → draft brief for top 3 | rank |
| **Ranking-drop watch** | Weekly | Priority keyword/page drops materially vs. baseline → diagnose cause + propose fix | rank |
| **Content-decay** | Monthly | Page declined materially over trailing 90 days → draft refresh plan | rank + scribe |
| **Internal-linking** | Weekly / on publish | New page lacks relevant internal links → draft specific link insertions | rank |
| **Ad-fatigue** | Every 2–3 days | Creative CTR/CPA decayed past threshold → draft fresh creative variants | hype |
| **Retargeting hygiene** | Weekly | Frequency too high or audience overlap → draft consolidation | hype |
| **Content-repurposing** | Weekly | New long-form asset un-repurposed → draft channel-native versions | scribe + hype |
| **Competitor-watch** | Weekly | Competitor pricing/positioning/creative shift → brief with implications | scout |
| **Review & UGC harvest** | Weekly | New positive reviews/UGC → stage repurposing drafts (permission + FTC disclosure) | hype |
| **Case-study sourcing** | Monthly | Client/brand win has proof numbers → stage a case-study brief | bridge |
| **Analytics-anomaly** | Daily | Metric moved beyond noise → verify (self-check) then alert or investigate | wrench |
| **Weekly review** | Weekly | Always runs → one-page summary: what moved, what was tested, what ships next | wrench |
| **Experiment-backlog** | Bi-weekly | Concluded tests → update playbook, launch next from backlog | wrench |
| **Tracking-QA** | Weekly | Events failing validation checklist → fix or escalate | wrench |

## Authoring a new loop

Fill all nine anatomy parts. If you can't answer the self-check, state/idempotency, and stop/bail-out concretely, the loop isn't ready to run. Start with tracking + a weekly review; add one loop at a time and prove it earns its keep before adding the next.

## Pre-launch guardrail checklist

- [ ] Every action classified Tier 1 (auto) or Tier 2 (gated)
- [ ] Tier-2 actions staged for approval — or explicitly authorized + capped + allowlisted
- [ ] Spend loops have hard cap + per-run change limit
- [ ] Send loops check suppression + have volume caps
- [ ] No raw PII in state or logs
- [ ] Always-escalate cases route to a human
- [ ] Kill switch documented
