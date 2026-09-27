<!-- Source: darkzOGx/youtube-automation-agent "AgentTube" (https://github.com/darkzOGx/youtube-automation-agent) — MIT, Copyright (c) 2025 YouTube Automation Agent Contributors. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
<!-- Concepts from utils/growth-experiment-service.js, utils/production-readiness-service.js and agents/publishing-scheduling-agent.js (commit 0d7eaf9). No code vendored. The sample-size table was computed for this agency, not copied. -->
# Packaging Tests and the Publish Gate

**Owners:** hype (runs the test), scout (reads the numbers), with the brand owner
deciding. Extends `EXPERIMENT-RUNBOOK.md` for title and thumbnail tests on
videos and posts already live.

## The rules

1. **Control first.** The current title and thumbnail are the control arm. Every
   variant differs from it; duplicate arms are dropped.
2. **Approving the plan authorizes the rotation only.** The agent may swap arms
   on the agreed schedule. **Adopting a winner is a separate yes.** So is
   cancelling, which always restores the control.
3. **Real platform numbers only.** Impressions and clicks come from the
   platform's analytics. Missing data stays `unknown`, never 0.
4. **Every arm must reach the minimum** qualified impressions *and* clicks, or
   the result is **inconclusive**, not "the leader wins".
5. **Evidence bar:** a two-proportion z-test between the best arm and the
   runner-up. **z ≥ 1.96 (95%)** to call a winner; ≥ 2.576 is high confidence.
6. **Guardrails can veto a winner.** If the leading arm drops average view
   percentage by more than 5 points versus control, or shifts the traffic mix by
   more than 20 points, the result is inconclusive even with a strong CTR.
7. **Record the reason** either way ("did not clear 95%", "failed retention
   guardrail", "cleared evidence and guardrails") in the brand's
   `learnings.md`.

## How many impressions you need (computed 2026-09-27)

z-score by CTR gap, equal impressions per arm:

| Impressions per arm | 5% vs 4% CTR | 6% vs 4.5% CTR |
|---|---|---|
| 1,000 | 1.08 (inconclusive) | 1.50 (inconclusive) |
| 3,000 | 1.87 (just short) | 2.60 (winner) |
| 5,000 | 2.41 (winner) | 3.36 (high confidence) |

A small brand's video often won't reach 5,000 impressions per arm. Then run the
test across several videos with the same packaging pattern, or accept
"inconclusive" and don't change anything. **Never** call a winner at 1,000
impressions because it "looks better".

**Caveat on rotation:** arms that take turns on one video (A this week, B next)
are measured at different times. That is not a true split test. News cycles and
game days move CTR, so rotate over matched windows (same weekday and time
block) and treat a narrow win with suspicion.

## The publish gate (before anything is scheduled)

AgentTube blocks scheduling on any failed **blocking** check. The agency's
version, per piece:

| Check | Blocking | Fails when |
|---|---|---|
| Real media file | Yes | Placeholder, simulated or missing output |
| Narration/audio present | Yes (video) | Missing or placeholder audio |
| Facts resolved | Yes | Any claim without a source (no citation, no claim) |
| Media rights confirmed | Yes | Owner or permission of any clip, photo or music unknown |
| Metadata valid | Yes | Title, description or tags over the platform limits |
| Channel access | Yes | Token expired; reconnect first |
| Thumbnail present | No (warning) | Default frame used |

A warning doesn't block; a failed blocking check does, with the fix named.
Checks are re-run after any fix. A stale pass doesn't count.

## What not to borrow

AgentTube can research, write, generate video and publish on its own. The
agency does not adopt the autonomous publish path. Human approval stays on every
publish, per the brand's `about.md`. Its anonymous telemetry is opt-in upstream;
leave it off.
