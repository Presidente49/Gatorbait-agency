<!-- Source: anthropics/knowledge-work-plugins (https://github.com/anthropics/knowledge-work-plugins) — Apache-2.0, Copyright (c) 2026 Anthropic, PBC. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
<!-- Modified from marketing/skills/email-sequence/SKILL.md: brand-first, draft-only with send approval gate, unsourced benchmark table removed in favour of brand baselines, compliance checklist added, templates tuned for small/local + media brands. -->
# Email Sequence — Multi-Email Flows, Drafted and Ready for Approval

**Primary owner:** scribe (writing). Wrench sets up the flow in the email tool *after* approval; scout reads back results. Concepts only — no code vendored.

Designs and drafts a complete automated sequence — welcome, nurture, launch, re-engagement, win-back, post-purchase — with copy, timing, branching, exits, and a test plan. **Output is drafts. Nothing is sent, scheduled, or loaded into a live list by this skill.**

## Step 1 — Read the brand (brand-first)

Read `about.md` (email tool, **who approves email sends**, never-claim list), `brand-voice.md`, `newsletter-voice.md` if present, `audience.md`, `offers.md`, `learnings.md`. Then ask only for what's missing:

| Input | Required? | Notes |
|---|---|---|
| Sequence type (template below) | Yes | |
| Trigger — what event enrolls someone | Yes | e.g., signs up via site form, first order, 60 days no order |
| Goal = the exit event | Yes | The action that means "done" (first order, booking, reply) |
| Offer/CTA links | Yes | Must be in `offers.md`. Discount codes only if the owner supplied them. |
| Number of emails / cadence | No | Default from the template |
| Current email baselines (open, click, conversion) | No | From the email tool's reports via scout. If none: `NO BASELINE`. |

## Step 2 — Architecture before copy

Write, in 5 lines max: the narrative arc (first email → last), what each email moves the reader toward, how intensity escalates, the exit event, and suppression rules (unsubscribed, already converted, in another active sequence, recent complaint).

### Templates (adapt; don't pad)

| Type | Emails / span | Arc |
|---|---|---|
| Welcome | 3–5 / 10–14 days | Welcome + what to expect → best-of / story → social proof → first offer → soft check-in |
| Lead nurture | 4–6 / 3–4 weeks | Useful tip → pain point → offer with proof → social proof → soft CTA → direct CTA |
| Launch / event | 3–5 / 1–3 weeks | Teaser → announcement with details → spotlight/use case → proof or early buzz → last chance (real deadline only) |
| Post-purchase | 3–4 / 2–3 weeks | Thanks + what's next → how to get the most out of it → review request → related offer |
| Re-engagement | 3–4 / 10–14 days | "Still want these?" with a reason → what's new → incentive (if approved) → last email + easy unsubscribe |
| Win-back | 3–5 / 30 days | Check-in, ask what went wrong → what's new → incentive (if approved) → feedback ask → door-open goodbye |

## Step 3 — Draft each email

For every email:

- **Send timing** — days after trigger / previous email; any engagement condition.
- **Who gets it** — segment/condition; who skips.
- **Subject lines** — 3 options (curiosity, benefit, specific/number), ≤50 characters where possible.
- **Preview text** — 40–90 characters, adds to the subject, never repeats it.
- **Purpose** — one sentence.
- **Body** — hook → 2–3 short paragraphs → one CTA. In the brand voice. Personalisation tokens written as `{{first_name}}` with a fallback ("there").
- **CTA** — button text + link from `offers.md`, with UTM `utm_source=email&utm_medium=email&utm_campaign=<sequence-slug>&utm_content=e<N>`.

## Step 4 — Flow logic

Text diagram of the flow with branches and exits, e.g.:

```
[Trigger] → E1 (day 0) → E2 (day 2) ──clicked CTA──→ [EXIT: goal]
                            │ no click
                            ▼
                         E3 (day 5) → E4 (day 9) → [EXIT: sequence complete]
```

Then list: branching conditions, exit conditions, re-entry rule, suppression rules.

## Step 5 — Compliance check (every email)

- Physical mailing address and one-click unsubscribe present in the footer (CAN-SPAM / GDPR / CASL norms — the email tool usually inserts these; confirm, don't assume).
- Only sent to people who opted in. No purchased or scraped lists.
- No claims on the brand's never-claim list; no unsubstantiated superlatives ("best in town") unless the brand files cite proof; testimonials only if real and attributed.
- Deadlines and scarcity are real ("ends Sunday" only if it ends Sunday).
- Subject line doesn't misrepresent the content.

Fail any item → fix before output.

## Step 6 — Test plan and targets

- **Sample-size gate first.** Look up the per-variant sample in the table in `agency/growth/EXPERIMENT-RUNBOOK.md` (e.g., ~550 per variant just to detect a 50% lift on a 10% baseline). If the list will not reach that within the test window, **do not A/B test** — ship one version and use the first 30 days as a baseline. Small local lists almost always fail this gate.
- If the gate passes: 2 A/B tests max (e.g., subject line on E1, CTA text on the offer email): what's varied, split, the metric that decides, and the pre-committed sample size.
- Targets: baseline from this brand's own email reports × a stated improvement assumption. If `NO BASELINE`, set the first 30 days as the baseline window and say so. **Do not insert industry benchmark numbers as targets.**
- Readback date for scout (30 days after first send).

## Step 7 — Output and approval

Save to `agency/brands/<slug>/outputs/email-sequence/<YYYY-MM-DD>-<sequence-slug>.md`: Overview table (`# | Timing | Subject (A) | Purpose | CTA | Condition`) · Flow diagram · Full drafts · Compliance checklist results · Test plan · **Setup checklist for wrench** (create flow, set trigger, add emails + delays, branches/exits, suppression, UTMs, send one test to the owner's own inbox) · Approval block:

```
APPROVAL REQUIRED — email sends
Approver (from about.md): <name/role>
Approved: [ ] yes  [ ] changes requested   Date: ____
```

Run the drafts through `marketing/quality-gate.md` (content rubric) before presenting. Append one line to `outputs/log.md`. Wrench builds the flow **only after** the approval block is ticked; the flow is set live by the approver or with their explicit go.
