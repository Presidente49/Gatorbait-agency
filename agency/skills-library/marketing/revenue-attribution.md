<!-- Source: ericosiu/ai-marketing-skills (https://github.com/ericosiu/ai-marketing-skills) — MIT. Adapted for Gator Bait Agency. -->
# Revenue Attribution — Prove What Made the Money

**Primary owner:** wrench (runs the reports). scout supplies competitor context; bridge uses the output in client conversations. Concepts only — no code vendored. Vendor-agnostic: works with any analytics platform + any CRM/order system.

## What it does

Maps content and campaigns to revenue so the agency knows what to double down on — and can prove it. Every brand gets a monthly answer to: *which content made money, and which was just busywork?*

## Attribution models (run all three, compare)

| Model | What it credits | Best for |
|---|---|---|
| **First-touch** | The content that started the journey | Proving top-of-funnel content value (social posts, viral reels) |
| **Linear** | Every touchpoint equally | Fair credit across long journeys |
| **Time-decay** | Recent touchpoints more | Short-window promos, merch drops |

When models disagree, that's signal: it tells you where in the journey each content type actually works.

## What every report includes

1. **Content-to-revenue mapping** — which posts, videos, articles, emails drove sessions → conversions → revenue.
2. **Cost-per-acquisition by content type** — blog, short video, long video, email, paid creative. The cheapest CPA wins future budget.
3. **Revenue per piece** — ranked list; top 10% of content gets the repurposing loop (`LOOP-SPEC.md`).
4. **Content gap analysis** — funnel stages with traffic but no attributed revenue. That's the brief queue for scribe.
5. **Anomaly flags** — unusual spikes/drops with severity and context. Not explanations — flags.

## Data sources (per brand)

Analytics platform (traffic, sessions, conversions, UTMs) + CRM/order system (deals, orders, close dates). Minimum viable: UTM discipline on every outbound link (`ANALYTICS-LOOP.md`) — without it, attribution is guesswork.

## Readback discipline

Attribution numbers change decisions, so they get the same rigor as experiments:

- **Define the primary metric before looking at the result.** Otherwise it's KPI karaoke.
- Baseline window vs. candidate window, stated up front.
- Separate seasonality, concurrent campaigns, list quality, and dirty attribution before claiming a win.
- Every recommendation that changes spend, content investment, or sales language gets a readback with a rollback rule.

Common primary metrics: positive reply rate · booked rate · pipeline created · content-assisted revenue · conversion rate · CPA by content type.

## Client-facing use

The monthly report is also the client-retention asset: executive summary with period-over-period changes, what content drove what revenue, where the next investment goes. Revenue proof is the moat against churn — a client who can see their money trail doesn't shop for a cheaper agency.

## Rules

- Never credit a single touchpoint in client reporting — show the model, name the caveats.
- A "winning" channel with dirty attribution is unproven. Say so.
- Feed every confirmed win back into the playbook (`EXPERIMENT-RUNBOOK.md` playbook entry) and every gap into the content queue.
