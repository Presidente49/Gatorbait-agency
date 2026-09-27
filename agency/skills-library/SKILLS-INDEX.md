<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Skills Index

Top-level skills are adapted from [charlie947/social-media-skills](https://github.com/charlie947/social-media-skills) (MIT); `marketing/` skills come from the sources named in each file's header (coreyhaines31/marketingskills and ericosiu/ai-marketing-skills, MIT; anthropics/knowledge-work-plugins, Apache-2.0; every-app/open-seo, MIT) — all for Gator Bait Agency white-label use. Every skill file carries the attribution header. Brand files referenced live in `agency/brands/<slug>/` (`about.md`, `brand-voice.md`, `audience.md`, `brand-style.md`, `goals.md`, `offers.md`, `learnings.md`).

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
| [marketing/campaign-plan.md](./marketing/campaign-plan.md) | blueprint | Goal → campaign brief, dated calendar, kill rule, and PROPOSED campaign-board rows (owner approves before anything runs) |
| [marketing/competitive-brief.md](./marketing/competitive-brief.md) | scout | Evidence-logged competitor research → messaging matrix, gaps, review-complaint map, counter-positioning card |
| [marketing/email-sequence.md](./marketing/email-sequence.md) | scribe | Multi-email flow (welcome/nurture/launch/win-back): drafts, branching, compliance check, sample-size gate, approval block |
| [marketing/keyword-clustering.md](./marketing/keyword-clustering.md) | rank | Searches → intent clusters mapped to existing/new pages, cannibalization from Search Console; no invented volumes (every-app/open-seo, MIT) |
| [marketing/link-prospecting.md](./marketing/link-prospecting.md) | rank + bridge | Link prospects from results pages and competitor backlinks, sourced contact paths, DRAFT outreach only (every-app/open-seo, MIT) |
| [marketing/local-seo.md](./marketing/local-seo.md) | rank | Maps/local-pack audit: profile vs top competitors, reviews, rank grid (paid calls costed first), the one fix (every-app/open-seo, MIT) |
| [marketing/seo-audit.md](./marketing/seo-audit.md) | rank | Read-only SEO + AI-visibility audit → top-5 paste-ready fixes (titles, robots, schema, llms.txt) for the site writer |
| [research/knowledge-base.md](./research/knowledge-base.md) | scout | Ingest sources (articles, transcripts, PDFs, stat sheets) → chunked index → cited answers; no citation, no claim (Tencent/WeKnora patterns, MIT) |
| [editorial/copy-desk-audit.md](./editorial/copy-desk-audit.md) | scribe | Names, facts, copy, excerpt, cover and tag sweep across every live front-page story; fix-in-place rules (never over unpublished edits, no email) |
| [design/hero-overlay.md](./design/hero-overlay.md) | blueprint + webmaster | Headline-over-photo lead spec (16:10 desktop, 4:5 phone, navy gradient); real photos only; specificity trap and render check |
| [web/embed-patch.md](./web/embed-patch.md) | webmaster | Custom-embed patch loop: read live, unique-match replace, cap, revision PATCH, publish, byte-exact repo sync; headless-fetch trap |
| [research/photo-sourcing.md](./research/photo-sourcing.md) | scout + blueprint | Find and verify credited photos (media library, staff galleries); unknown credit means don't publish; no AI art on news |
| [marketing/email-delivery-check.md](./marketing/email-delivery-check.md) | wrench + scribe | Owner yes, dedupe, source gates, draft preview, publish, IN_DETECTION to DISTRIBUTED, delivered-count proof |
| [marketing/brand-first.md](./marketing/brand-first.md) | all | Read the active brand's context files before asking the user anything |
| [marketing/quality-gate.md](./marketing/quality-gate.md) | scribe | Expert-panel recursive scoring gate for drafts (90+ to ship) |
| [marketing/revenue-attribution.md](./marketing/revenue-attribution.md) | wrench | Content→revenue attribution: first-touch/linear/time-decay + CPA by type |
| [marketing/youtube-outliers.md](./marketing/youtube-outliers.md) | scout | 2x outlier rule + packaging readback windows (CTR, watch time, subs) |

## By agent

- **scout** (research/analytics): analytics-dashboard, niche-research, post-scorer, marketing/competitive-brief, marketing/youtube-outliers, research/knowledge-base, research/photo-sourcing
- **scribe** (writing): content-matrix, hook-generator, newsletter-voice, post-formatter, post-writer, reels-scripting, voice-builder, marketing/email-sequence, marketing/quality-gate, editorial/copy-desk-audit
- **hype** (social publishing): pinned-comment
- **blueprint** (creative/design): carousel-builder, infographic-builder, graphic-designer, quote-post, video-thumbnail, marketing/campaign-plan, design/hero-overlay
- **rank** (SEO): marketing/seo-audit, marketing/keyword-clustering, marketing/link-prospecting, marketing/local-seo
- **bridge** (outreach/partnerships): profile-optimizer, marketing/link-prospecting (outreach drafts)
- **webmaster** (website/backend): web/embed-patch, design/hero-overlay (deploy)
- **wrench** (ops/automation): marketing/revenue-attribution, marketing/email-delivery-check

## Notes

- **Where outputs go:** every saved artifact lands in `agency/brands/<slug>/outputs/<skill-name>/` (dated filenames), and every run adds one line to `agency/brands/<slug>/outputs/log.md` — date, skill, agent, output path, QC result. "Brand workspace" in any skill means this folder.
- **Learnings loop:** `analytics-dashboard` and `post-scorer` write proven patterns to the brand's `learnings.md` (and transferable ones to `agency/shared/learnings.md`). Other skills read `learnings.md`; they do not write hypotheses into it.
- **Drafts, not publishing:** no skill publishes, sends email or spends money. Output goes to the approval path in the brand's `about.md`.

- Each skill reads the active brand's files from `agency/brands/<slug>/` before personalised work and never inherits another client's identity, accounts, or private files.
- No credentials, API keys, emails, or personal data anywhere in this library. Integrations (scraping, video analysis) are described as capabilities the client authorises, with cost confirmation before paid runs.
- Common skill chains: `niche-research` → `post-writer`/`post-formatter` → `post-scorer` → `graphic-designer`/`carousel-builder` → `pinned-comment`. Campaign chain: `marketing/competitive-brief` + `marketing/seo-audit` → `marketing/campaign-plan` → `marketing/email-sequence` + post skills → `marketing/quality-gate` → owner approval.
