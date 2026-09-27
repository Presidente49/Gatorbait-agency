<!-- Source: coreyhaines31/marketingskills (https://github.com/coreyhaines31/marketingskills) — MIT. Adapted for Gator Bait Agency. -->
<!-- Source: ericosiu/ai-marketing-skills (https://github.com/ericosiu/ai-marketing-skills) — MIT. Adapted for Gator Bait Agency. -->
# Experiment Runbook — The Compounding Growth Engine

**Primary owner:** wrench (runs the loop, keeps the backlog + playbook). rank, scribe, and hype supply variants. This is the agency's learning engine — individual tests are valuable, a continuous program is a compounding asset.

## The loop

```
1. Generate hypotheses (data, research, competitors, comments, past tests)
2. Prioritize with ICE scoring
3. Design and run the test
4. Analyze with statistical rigor
5. Promote winners to the playbook
6. Generate new hypotheses from learnings → repeat
```

**Always check the playbook before creating new content** — apply proven patterns first, test only what's genuinely unknown.

## Hypothesis framework

```
Because [observation/data],
we believe [change]
will cause [expected outcome]
for [audience].
We'll know this is true when [metrics].
```

Weak: "Changing the button color might increase clicks." Strong: "Because analytics show 70% of mobile visitors abandon the merch PDP before scrolling (object-action events), we believe moving the size selector above the fold will increase add-to-cart by 15%+ for mobile visitors. We'll measure PDP→cart rate."

## ICE prioritization

Score 1–10 on three dimensions. **ICE = (Impact + Confidence + Ease) / 3.** Run the highest scores first; re-score monthly.

| Dimension | Question |
|---|---|
| **Impact** | If this works, how much does it move the primary metric? |
| **Confidence** | How sure are we? (Based on data, not gut.) |
| **Ease** | How fast and cheap to ship and measure? |

## Design rules

- **Test one thing.** One variable per test — otherwise you don't know what worked.
- **Bold enough to detect.** Testing a 2px padding change is measuring noise.
- **Pre-determine sample size.** Quick reference (95% confidence, 80% power, per variant):

| Baseline | 10% lift | 20% lift | 50% lift |
|---|---|---|---|
| 1% | 150k | 39k | 6k |
| 3% | 47k | 12k | 2k |
| 5% | 27k | 7k | 1.2k |
| 10% | 12k | 3k | 550 |

- **Don't peek and stop early.** Pre-commit to the sample size. Checking results early and stopping produces false positives and wrong decisions.

## Metrics

- **Primary:** one metric, tied to business value (revenue, signups, purchases — never a proxy alone).
- **Secondary:** support interpretation (why/how it worked).
- **Guardrail:** things that must not get worse (refund rate, unsubscribes, page speed). Stop the test if a guardrail goes significantly negative — even if the primary is winning.

## What to test (by surface)

| Surface | Levers |
|---|---|
| Pages (site/store) | Headline angle, hero visual, CTA copy/placement, social proof placement, price presentation, form length |
| Paid creative | Hook (first 3 seconds), angle, proof number, CTA type, format |
| Social posts | Hook style, post length, image vs. video, CTA type, topic bucket, timing |
| Email/newsletter | Subject angle, preview text, CTA placement, length, send time |
| Video | Title formula, thumbnail rules, first-15-second hook, retention beats, chapter structure, Shorts cutdowns |

## Velocity targets

| Metric | Target |
|---|---|
| Experiments launched/month | 4–8 |
| Win rate | 20–30% (sustained higher = hypotheses too conservative) |
| Average test duration | 2–4 weeks |
| Backlog depth | 20+ hypotheses queued |
| Cumulative lift | Compound gains from all winners |

## The playbook entry

When a test wins, don't just implement it — document the pattern:

```
## [Experiment Name]
**Date** · **Hypothesis** · **Sample** (n per variant)
**Result:** winner/loser/inconclusive — [primary metric] changed [X%] (95% CI, p-value)
**Guardrails:** [outcomes] · **Segment deltas:** [device/audience differences]
**Why it worked/failed:** [analysis]
**Pattern:** [the reusable insight — e.g., "stat-led hooks beat quote-led hooks for reach"]
**Apply to:** [other pages/brands where this pattern might work]
**Status:** implemented / parked / needs follow-up
```

The playbook becomes a library of proven growth patterns — per brand, and agency-wide for patterns that transfer.

## Cadence

- **Weekly (30 min):** check running experiments for technical issues and guardrail metrics only. No early winners.
- **Bi-weekly:** conclude finished tests, update the playbook, launch the next from the backlog.
- **Monthly (1 hour):** velocity, win rate, cumulative lift; replenish the hypothesis backlog; re-prioritize with ICE.
- **Quarterly:** audit the playbook. Which patterns scaled? Which winners were never applied broadly? What funnel areas are under-tested?

## Common mistakes

- Testing too small a change (undetectable) or too many things (can't isolate).
- No clear hypothesis. Stopping early. Changing variants mid-test. Adding new traffic sources mid-test.
- Ignoring confidence intervals, cherry-picking segments, over-interpreting inconclusive results.
- Optimizing a proxy metric into a revenue loss (e.g., CTR up, revenue down).
