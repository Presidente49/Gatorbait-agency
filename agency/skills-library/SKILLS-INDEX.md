<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Skills Index

All skills are adapted from [charlie947/social-media-skills](https://github.com/charlie947/social-media-skills) (MIT) for Gator Bait Agency white-label use. Every skill file carries the attribution header. Brand files referenced live in `agency/brands/<slug>/` (`about.md`, `brand-voice.md`, `audience.md`, `brand-style.md`, `goals.md`, `offers.md`, `learnings.md`).

## Skill → Agent mapping

| Skill file | Primary owner | What it does |
|---|---|---|
| [analytics-dashboard.md](./analytics-dashboard.md) | scout | Turn an analytics export into an interactive dashboard + written strategy with 5 data-backed recommendations |
| [content-matrix.md](./content-matrix.md) | scribe | Generate 24-40 post ideas from content pillars x 8 proven formats |
| [carousel-builder.md](./carousel-builder.md) | blueprint | Slide-by-slide carousel brief + per-slide image prompts (1080x1350) |
| [infographic-builder.md](./infographic-builder.md) | blueprint | Hand-drawn whiteboard infographic image prompt from source content |
| [graphic-designer.md](./graphic-designer.md) | blueprint | HTML/CSS structured graphic or AI infographic to pair with a post |
| [hook-generator.md](./hook-generator.md) | scribe | 6 two-line hook variations (40 chars per line) for any topic |
| [newsletter-voice.md](./newsletter-voice.md) | scribe | Build `newsletter-voice.md` from newsletter samples or 6 archetypes |
| [niche-research.md](./niche-research.md) | scout | 20 verified stories in the niche from the last 7 days, with shareable angles |
| [pinned-comment.md](./pinned-comment.md) | hype | Deadpan pinned comment + matching image prompt for a post |
| [post-formatter.md](./post-formatter.md) | scribe | Framework post (PAS, AIDA, BAB, STAR, SLAY), max 20 nonblank lines |
| [post-scorer.md](./post-scorer.md) | scout | Score a draft against the brand's real post performance data |
| [post-writer.md](./post-writer.md) | scribe | Draft posts in the brand's voice, no framework constraints |
| [profile-optimizer.md](./profile-optimizer.md) | bridge | Rebuild a social profile: headline, bio, credentials, link strategy, visual prompts |
| [quote-post.md](./quote-post.md) | blueprint | 9 original quote options + image prompt baking the chosen quote into a reference style |
| [reels-scripting.md](./reels-scripting.md) | scribe | Reverse-engineer a reference Reel into a 30-45s script with a 95/100 QA gate |
| [voice-builder.md](./voice-builder.md) | scribe | Brand interview + sample analysis → `brand-voice.md` + `about.md` |
| [video-thumbnail.md](./video-thumbnail.md) | blueprint | Thumbnail brief + image prompt (16:9 and 9:16) from a video title |

## By agent

- **scout** (research/analytics): analytics-dashboard, niche-research, post-scorer
- **scribe** (writing): content-matrix, hook-generator, newsletter-voice, post-formatter, post-writer, reels-scripting, voice-builder
- **hype** (social publishing): pinned-comment
- **blueprint** (creative/design): carousel-builder, infographic-builder, graphic-designer, quote-post, video-thumbnail
- **rank** (SEO): none yet
- **bridge** (outreach/partnerships): profile-optimizer
- **webmaster** (website/backend): none yet
- **wrench** (ops/automation): none yet

## Notes

- **Where outputs go:** every saved artifact lands in `agency/brands/<slug>/outputs/<skill-name>/` (dated filenames), and every run adds one line to `agency/brands/<slug>/outputs/log.md` — date, skill, agent, output path, QC result. "Brand workspace" in any skill means this folder.
- **Learnings loop:** `analytics-dashboard` and `post-scorer` write proven patterns to the brand's `learnings.md` (and transferable ones to `agency/shared/learnings.md`). Other skills read `learnings.md`; they do not write hypotheses into it.
- **Drafts, not publishing:** no skill publishes, sends email or spends money. Output goes to the approval path in the brand's `about.md`.

- Each skill reads the active brand's files from `agency/brands/<slug>/` before personalised work and never inherits another client's identity, accounts, or private files.
- No credentials, API keys, emails, or personal data anywhere in this library. Integrations (scraping, video analysis) are described as capabilities the client authorises, with cost confirmation before paid runs.
- Common skill chains: `niche-research` → `post-writer`/`post-formatter` → `post-scorer` → `graphic-designer`/`carousel-builder` → `pinned-comment`.
