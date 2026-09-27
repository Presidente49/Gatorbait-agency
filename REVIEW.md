# REVIEW.md — Marlowe's review pass, 2026-09-27

Brenden asked why Claude couldn't "just go in and do it." It can't —
it's not connected to anything. So I did the review myself.

## What's solid

- **Structure.** `agency/` hangs together: agents, brands, cloud,
  growth, merch, studio, skills-library, shared. 122 files, no
  orphans, no dead directories.
- **Agent identities.** All 8 roles are sharp, duties executable,
  startup steps real and consistent (read ACTIVE → read brand files →
  read shared playbook/protocols/learnings).
- **Cloud.** docker-compose uses env vars everywhere, no hardcoded
  secrets. All 3 n8n workflow JSONs are valid.
- **Growth rigor.** The experiment runbook is legit: pre-committed
  sample sizes, no peeking, guardrail metrics with kill criteria,
  control groups. Revenue attribution covers first-touch, linear,
  and time-decay.
- **Attribution.** Borrowed files carry Source headers (repo, URL,
  license). SOURCES.md registers 19 sources. Rejections documented
  in NOT-INTEGRATED.md files with reasons.
- **Learnings loop.** Every agent identity mandates appending to the
  brand's learnings.md; shared/learnings.md collects transferable wins.

## What was broken — fixed

**Brand-specific leaks in shared agent identities.** Four lines
hardcoded Gator Bait-isms into the white-label core:

1. `scribe/identity.md` — "Write site articles in Gator Bait voice"
   → now "the active brand's voice (per brand-voice.md)".
2. `scribe/identity.md` — "Embed the matching YouTube video in every
   article" → now conditional on the brand publishing video.
3. `hype/identity.md` — "Gator groups only" → now "on-brand groups
   only (per the brand's distribution list)".
4. `bridge/identity.md` — "Guest booking for The Buddy Martin Show"
   → now "the brand's show/podcast".

A pizza shop onboarding tomorrow would previously have been told to
write in Gator Bait voice and share to Gator groups. That's fixed.

## What still needs work

- **Missing clipping engine.** No clean MIT/Apache long-video-to-
  shorts clipper found yet. Still the #1 hunting priority.
- **`new-brand.sh` flips ACTIVE to the new brand on creation.**
  Creating a brand shouldn't switch the live brand. Needs a flag
  (`--no-activate`) — small fix, queued.
- **Brand template has no `distribution.md`.** Hype now references
  "the brand's distribution list" but the template doesn't define
  one. The _template needs a distribution file (groups, pages,
  cadence) — queued.
- **Paperclip is docs-only.** The control-plane mapping is written,
  but no live Paperclip instance exists yet. Phase 1 (Gator Bait
  Media, heartbeat + task loop, budgets first) is still ahead.
- **White-label pizza-shop test (mental):** passes on structure,
  fails on two details above (distribution.md, ACTIVE flip). After
  those fixes it should be a clean 15-minute onboard.

## Needs a human decision (Brenden)

1. **Vendure vs Saleor for merch.** Vendure is GPL — permanently out.
   Saleor is BSD-3 (permissive, no copyleft risk) but outside the
   strict MIT/Apache allow-list. If you widen the policy to "all
   permissive licenses," Saleor is the best merch engine available.
   Your call.
2. **Paperclip go-live.** Docs are done; running it as real
   infrastructure is a bigger step. Say when.
