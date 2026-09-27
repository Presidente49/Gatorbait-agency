# About — Gator Bait Media

*Facts from the live production repo (Presidente49/gatorbait-media-redesign),
recorded 2026-09-27. Where this file and an agent/shared file disagree, the
production rules here win until the owner decides otherwise (see REVIEW.md,
"Needs a human decision").*

## The business
- **What it is:** Florida Gators sports media — free sports-news site, a
  separate Gator Bait Magazine, The Buddy Martin Show.
- **Owner / decision maker:** Brenden Martin.

## Accounts and platforms
- **Website:** https://www.gatorbaitmedia.com on **Wix**. Changed only through
  the Wix API by **one production writer** — the Claude Code "Master
  Control" controller. No agent in this repo writes to the live site.
- **Recurring work:** runs as Claude Code cloud routines under that one
  controller. Do not reactivate n8n, FCC or local queues merely because
  scaffolding exists here; add a layer only for a defined job.
- **Social:** Facebook page, Instagram @gatorbaitmedia, YouTube (The Buddy Martin Show).

## Approvals — who signs off on what
| Action | Who approves | Notes |
|---|---|---|
| Routine drafting, research, QC | Default is GO | Drafts only |
| Publishing an article / site change | Controller + owner gate | One production writer |
| Instagram posts | Brenden's approval tap | Stage, never auto-post |
| Email sends | Approval gate | **One email per story.** The story-alert automations are off — do not turn them on. |
| Money, account changes, credentials | Brenden | Always escalated |

## Newsroom
- **Buddy Martin** — editorial lead.
- **Writers:** Franz Beard, Carlton Reese, Eddie Gilley, Loren Meadows.
- **Muse** — drafts only; never publishes.
- **Jon Sumrall** (spelled **Jon**) — Florida's head coach.

## Facts and sources
- Verify every fact against primary sources: ESPN box scores / game data and
  UF's ASAP Sports transcripts for quotes. Mark anything unverified [VERIFY].
- **Photo credit:** real Chris Spears photography is always credited to him.
- **Covers/graphics:** never repeat the same photo across covers.
- **Logo:** use the supplied logo files only — never type or redraw it.
- **Credentials:** never in prompts, logs, commits or this repo.
