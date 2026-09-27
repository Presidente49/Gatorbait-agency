# Gator Bait Agency — white-label multi-agent marketing agency

A persistent multi-agent marketing agency that runs inside any AI assistant
(Muse, Claude, etc.). **White-label by design:** the agents, playbooks, and
learnings work for any business — brand-specific material lives in
`agency/brands/<slug>/`. Ships with Gator Bait Media as the example brand.

## The Team

| Agent | Codename | Role |
|-------|----------|------|
| Scout | `scout` | Research & Analytics — finds stories, tracks performance, runs A/B test reports |
| Scribe | `scribe` | Content Writer — articles, transcripts, show notes |
| Hype | `hype` | Social Media Manager — Facebook, Instagram, TikTok posts and reels |
| Blueprint | `blueprint` | Creative Strategist — graphics, thumbnails, video concepts |
| Rank | `rank` | SEO Specialist — SEO, keywords, site health |
| Bridge | `bridge` | Outreach — guests, partnerships, cross-promos |
| Wrench | `wrench` | Ops & Tech — automations, pipelines, site tooling |
| Webmaster | `webmaster` | Backend agency — website day-to-day, full coding ability |

The human is the CEO. The AI running the agency is the CMO — it
orchestrates agents, runs the playbook, and only escalates what truly
needs a human. Agents are narrow workers; the operator's judgment
directs them.

Behind the team sits the **STUDIO** — the production company
([STUDIO.md](STUDIO.md)): clip → caption → reel → publish pipelines,
the deterministic brand-creative engine, and livestream operations.
Under everything runs the **CLOUD** layer ([CLOUD.md](CLOUD.md)):
24/7 n8n automation, the self-hosted scheduler/client dashboard.

## Quick Start (for Claude or any AI)

1. Read `agency/brands/ACTIVE` → the brand slug.
2. Read every `.md` file in `agency/brands/<slug>/` — voice, style, goals, audience, offers, learnings.
3. Read `agency/shared/playbook.md` (Meta rules), `protocols.md` (operating rules), `learnings.md` (earned principles).
4. Read `agency/shared/campaign-board.md` — what's in flight.
5. Run the content waterfall: Scout finds the story → Scribe writes → Blueprint designs → Hype posts → Scout measures.

## White-label a new business

See **[WHITE-LABEL.md](WHITE-LABEL.md)**. Fifteen minutes:

```bash
./new-brand.sh <business-slug>
# fill in agency/brands/<business-slug>/, done
```

The shared learnings — every earned principle from every brand the
agency has run — travel with it. That's the compounding asset.

## Key Files

- White-label guide: `WHITE-LABEL.md`
- Production company: `STUDIO.md` → `agency/studio/` (clipping, captions, reels, creative, livestream)
- Cloud layer: `CLOUD.md` → `agency/cloud/` (n8n 24/7 automation, scheduler/client dashboard)
- Skills library: `agency/skills-library/` (17 agent skills + `SKILLS-INDEX.md` mapping skills to agents)
- Brands: `agency/brands/<slug>/` (`ACTIVE` selects the current one)
- Brand template: `agency/brands/_template/`
- Meta playbook: `agency/shared/playbook.md`
- Operating rules: `agency/shared/protocols.md`
- Shared learnings: `agency/shared/learnings.md`
- Goals: per-brand, in `agency/brands/<slug>/goals.md`
- Task board: `agency/shared/campaign-board.md`
- Roster: `agency/shared/roster.md`
- Agent files: `agency/agents/{codename}/identity.md`, `tasks.md`, `memory/`

## How It Runs

- **Default is GO.** Agents act; they don't wait for permission on routine work.
- **Escalate only for:** money, deletions, credentials, contracts, CAPTCHAs, first-time public content.
- **Every post follows the playbook.** Native post, never a bare link share.
- **Measure everything.** Scout tracks reach/engagement per post and reports what won.
- **Learnings compound.** Every campaign appends to the brand's `learnings.md`
  and, when transferable, to `agency/shared/learnings.md`.

## Origin

Adapted from the open-source [Virtual Marketing Agency skill](https://github.com/avioflagos/marketing-agency-skill) (MIT), rebuilt as a
white-label agency. The Meta best-practices research was compiled
September 2026; Gator Bait Media (Florida Gators sports media) is the
reference brand.

## Borrowed with thanks (all MIT — copyright lines + license text in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md))

- [charlie947/social-media-skills](https://github.com/charlie947/social-media-skills) — 17 agent skills → `agency/skills-library/`
- [cgallic/visual-factory-kit](https://github.com/cgallic/visual-factory-kit) — creative engine concept → `agency/studio/creative/`
- [muneebkhan08/capite](https://github.com/muneebkhan08/capite) — caption pipeline → `agency/studio/captions/`
- [ronin1770/reel-quick](https://github.com/ronin1770/reel-quick) — reel renderer pattern → `agency/studio/reels/`
- [arifyaman/multistream](https://github.com/arifyaman/multistream) — livestream chain → `agency/studio/livestream/`
- [Anil-matcha/Free-AI-Social-Media-Scheduler](https://github.com/Anil-matcha/Free-AI-Social-Media-Scheduler) — scheduler docs → `agency/cloud/scheduler/`

Excluded on license grounds: mutonby/openshorts (commercial carve-out on
its agent-control components — see `agency/studio/clipping/NOT-INTEGRATED.md`).
