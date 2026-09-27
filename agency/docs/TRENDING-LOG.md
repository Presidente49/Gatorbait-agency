# Trending Repo Watch — log (append-only)

## 2026-09-27 09:50 EDT — hourly scan

Sources checked: GitHub search API across 10 lanes (agent skills, AI agent framework, social media scheduler, short video clipper, caption tool video, n8n workflow marketing, design system agent skills, agent learning loop analytics, youtube shorts automation, SEO agent skills — created >2026-08-20, sorted by stars, 150 repos) + GitHub trending daily (JS-rendered list, API fallback used per prior runs).
Seen-list checked against `SOURCES.md` (#1–59 + rejections) and all prior log runs — the 3 qualifiers below are new to the registry.

### QUALIFIED (3) — all MIT, LICENSE file read in full via raw.githubusercontent.com (openshorts rule; grepped for carve-out keywords — zero hits)

1. **undefined-ui/second-brain-os** — https://github.com/undefined-ui/second-brain-os — MIT (LICENSE read in full; © 2026; standard MIT, no carve-outs) — ~711 stars — created 2026-09-07, pushed 2026-09-27 (today).
   Why: a self-maintaining AI "second brain" — starter vault + agent skills + scripts for a self-organizing knowledge base in Claude Code and Obsidian; research-agent knowledge substrate and learning-loop infrastructure beside hindsight (#8) and reef (#52).

2. **viettranx/3dviz-pro-max** — https://github.com/viettranx/3dviz-pro-max — MIT (LICENSE read in full; © 2026 Viettranx; standard MIT, no carve-outs) — ~564 stars — created 2026-09-10, pushed 2026-09-11 (stable skill content).
   Why: agent skill for creative 3D visualization — turn an idea into a Three.js/Blender scene worth exploring (223 recipes, 440 knowledge records, 37 runnable studies; Claude Code + Codex plugin) — a 3D content lane for studio creative beside dream-loop (#37).

3. **aleksandr-alhoff/seo-landing** — https://github.com/aleksandr-alhoff/seo-landing — MIT (LICENSE read in full; © 2026 Aleksandr Alhov; standard MIT, no carve-outs) — ~159 stars — created 2026-08-28, pushed 2026-08-30 (stable skill content).
   Why: agent skill that gives an AI coding agent the capabilities of a senior technical SEO engineer — high-performance, technically optimized SEO landing pages; landing-page lane for the webmaster + SEO agents.

### Checked, not qualified / skipped this round

- Pal-AI-Lab/Cortico (156★ MIT, pushed 2026-09-26) — event-stream persona-bot framework; not agency operational.
- QiantangCredit/heimdall-agent (94★ MIT) — autonomous agent for authorized CTF/security labs; security, not agency relevant.
- typesafe-ai/skills (2,249★ MIT) — TypeSafe vendor SDK skills; not agency operational (noted 08:50 run).
- Agenta-AI/awesome-ai-agent-platforms (331★ CC0-1.0) — curated list of agent platforms, not software; license out of policy scope.
- RectangleStory/Superpowers_Multi_AI (100★ bsd-3-clause) — BSD-3 is permissive but policy is MIT/Apache-2.0; Superpowers skill-pack is dev-focused anyway.
- kharmanskyi/open-steps (951★ MIT) — coding-agent output → plain-language reports; marginal, comms lane covered (noted 08:50 run).
- feitangyuan/motion-web (528★, license "other"/NOASSERTION) — excluded per policy. tigerless-labs/seo-ops (481★, license null) — unlicensed, excluded per policy.
- mcncarl/jianying-headless (2,798★ NOASSERTION), Vincentwei1021/video-talkcraft (1,253★ "other" PolyForm Noncommercial), QingYunA/agent-html (39★ license null) — already in rejections table / noted, no re-evaluation.
- Short-form video clipper lane: all results ≤4 stars (red16124724/Aurum-Clipper 4★ unlicensed, egga-fx/xclips 1★ MIT, etc.) — no traction; lane covered by autoclip/yukitorido/AI-Youtube-Shorts-Generator.
- n8n marketing workflows: all results 0–1 stars, mostly unlicensed "marketing-workflows-n8n" forks/spam — covered by YuriCrystal/n8n-marketing-flows (#57).
- Social schedulers: thin entries (1–5★); lane covered by cogsend (#25), shoutrrr (#22), social-stats manager.
- Caption/video-tool entries: thin (≤8★) or off-lane; covered by capite (#3), video-use (#20).
- All already-registered repos re-appearing in searches (sepia #34, scroll-craft #58, headcount #36, dream-loop #37, screenwriting-skills #38, golive-skill #39, hermes-jev-skills #40, linkedin-agent-skill #41, laya-clipper #46, jevcut #47, cogsend #25, equinor/thin entries) — no re-evaluation.

### License-policy notes this round
- All 3 qualifiers had LICENSE files fetched from raw.githubusercontent (main branch) and read in full; case-insensitive grep for (agpl|gpl-3|noncommercial|polyform|elastic|commercial license|proprietary) — zero hits in all three.
- NOASSERTION + null-license entries keep climbing in the video/clipper and SEO lanes (jianying-headless, tigerless-labs/seo-ops, Aurum-Clipper) — policy holds: described, never copied.

## 2026-09-26 23:50 EDT — hourly scan

Sources checked: GitHub trending daily, GitHub trending weekly, targeted web search (agent frameworks, agent skills, schedulers, video pipelines, n8n, design systems, learning loops).
Seen-list checked against `SOURCES.md` (#1–19 + rejections) — none of the qualifiers below are registered.

### QUALIFIED (7) — all MIT or Apache-2.0, LICENSE file actually read

1. **anthropics/commerce-agents** — https://github.com/anthropics/commerce-agents — Apache-2.0 (LICENSE read in full; © 2026 Anthropic PBC; no carve-outs) — ~3,057 stars — created 2026-09-01 (1 commit, reference implementation, not maintained).
   Why: shopping-agent + merchant-agent reference blueprints (5 skills each, staged-change approval gates, backend interfaces, MCP connector guidance) map directly onto the agency's merch lane (Medusa/Saleor storefronts).

2. **anthropics/knowledge-work-plugins** — https://github.com/anthropics/knowledge-work-plugins — Apache-2.0 (GitHub-detected; LICENSE file present) — ~25,690 stars — 1,066 commits, created 2026-01-23, on trending weekly.
   Why: ships a dedicated `marketing` plugin (content drafting, campaign planning, brand-voice enforcement, competitor briefs, performance reporting) plus `data`/`productivity`/`small-business` — file-based markdown skills drop straight into the agency skills-library for research/writing/SEO/outreach agents.

3. **Tencent/WeKnora** — https://github.com/Tencent/WeKnora — MIT (LICENSE read in full; project code MIT; third-party deps all permissive — Apache/MIT/CNRI/BSD family; NO copyleft, NO commercial carve-out; the GPL mention is inside the historical CNRI Python-license text) — ~30,373 stars — 3,264 commits; v0.8.2 released 2026-09-24.
   Why: self-hosted LLM knowledge platform (RAG + reasoning agent + self-maintaining wiki + built-in MCP server + cross-session memory) — research agent's knowledge base and a substrate for the agency learning loop.

4. **bytedance/deer-flow** — https://github.com/bytedance/deer-flow — MIT (GitHub-detected; MIT badge; LICENSE file present) — ~83,010 stars — 3,578 commits; 2.0 ground-up rewrite, #1 trending Feb 2026.
   Why: long-horizon "super agent" harness — sub-agent orchestration, message gateway, sandbox execution, long-term memory, skills, scheduled tasks — ops control-plane patterns alongside the paperclip evaluation.

5. **thesysdev/openui** — https://github.com/thesysdev/openui — MIT (GitHub-detected; LICENSE file present) — ~9,858 stars — 955 commits, created 2024-12-02.
   Why: generative-UI standard (streaming-first lang, ~67% fewer tokens than JSON) with a published Agent Skill, LangChain integration, and an `@openuidev/react-email` package for model-generated emails — feeds the creative/design agents and the newsletter lane.

6. **NousResearch/hermes-agent** — https://github.com/NousResearch/hermes-agent — MIT (GitHub-detected; LICENSE file present) — ~249,265 stars — 44,682 commits, created 2025-07-22.
   Why: self-improving agent with a genuine closed learning loop (autonomous skill creation from experience, agent-curated memory with nudges, FTS5 session search, evals), built-in cron scheduler, subagent delegation, and messaging gateway — the strongest learning-loop reference for the agency. (Migrates from OpenClaw.)

7. **stablyai/orca** — https://github.com/stablyai/orca — MIT (GitHub-detected; LICENSE file present) — ~78,998 stars — 11,878 commits, created 2026-03-17; ships daily.
   Why: parallel-agent orchestrator — fan one prompt across agents in isolated worktrees, design mode (click UI element → straight into agent prompt), scriptable Orca CLI, mobile companion — a model for running the agency's 8 agents in parallel and for Brenden to monitor from his phone.

### Checked, not qualified / skipped this round

- zhaoxuya520/reverse-skill (trending daily) — reverse-engineering/penetration-testing skill pack; not marketing-agency relevant.
- cloudflare/security-audit-skill (trending weekly) — security-audit skills; not agency relevant.
- addyosmani/agent-skills (trending weekly) — production-grade *engineering* skills for coding agents; skill pattern already covered by knowledge-work-plugins; marginal for a marketing agency.
- TencentCloud/Octop, affaan-m/ECC, superdesigndev/treg (trending weekly) — dev-tooling / tool-routing; marginal agency fit.
- davila7/claude-code-templates, alibaba/open-code-review, HKUDS/CLI-Anything, anthropics/financial-services, NVIDIA/Model-Optimizer, openbao/openbao — dev/infra, not agency relevant.
- All already-registered repos re-appearing on trending (paperclip, hindsight, univer, buzz, claude-code-action, mobile-mcp) — no re-evaluation.

### License-policy notes this round
- GitHub "NOASSERTION" handling (openshorts rule): WeKnora showed NOASSERTION, so the full LICENSE was read — clean MIT, no carve-out. GitHub-detected Apache-2.0/MIT with a LICENSE file present was accepted for the other five (commerce-agents' LICENSE read in full — clean Apache-2.0).

## 2026-09-27 01:00 EDT — hourly scan

Sources checked: GitHub trending daily, GitHub trending weekly digests, targeted searches (social media schedulers, video pipelines, SEO tools, YouTube automation).
Seen-list checked against `SOURCES.md` (#1–19 + rejections) — none of the qualifiers below are registered.

### QUALIFIED (4) — all MIT or Apache-2.0, LICENSE file actually read in full

1. **browser-use/video-use** — https://github.com/browser-use/video-use — MIT (LICENSE read in full; © 2026 Browser Use; no carve-outs) — ~27,340 stars — 22 commits; last commit 2026-09-24; created 2026-04-12.
   Why: edit-videos-with-coding-agents harness (SKILL.md): transcript→pack→LLM-reason→EDL→render→self-eval pipeline, filler-word cuts, 30ms audio fades, burned subtitles, HyperFrames/Remotion/Manim animation overlays via parallel subagents, session memory in project.md — agent-driven editing patterns for the studio reels/video pipeline.

2. **every-app/open-seo** — https://github.com/every-app/open-seo — MIT (LICENSE read in full; © 2026 Ben Senescu) — ~21,270 stars — 576 commits, 37 releases; last commit 2026-09-19; created 2026-02-27.
   Why: open Semrush/Ahrefs alternative with an MCP server + pre-built agent skills (keyword research, rank tracking, site audit, backlinks, AI visibility, strategy libraries) — pay-as-you-go DataForSEO + self-host — a ready-made toolchain for the SEO agent.

3. **coollabsio/shoutrrr** — https://github.com/coollabsio/shoutrrr — Apache-2.0 (LICENSE read in full; © 2026 coolLabs Solutions Kft; no carve-outs) — ~390 stars — 349 commits, 19 releases; created 2026-06-12.
   Why: self-hostable Buffer/Typefully/Hootsuite alternative (X, Bluesky, LinkedIn, Facebook, Instagram, Threads, Discord) with workspaces, teams, analytics, per-platform overrides, Coolify one-click deploy — and ships `.claude/skills` + `.mcp.json` out of the box. Stronger white-label client dashboard candidate than the existing Anil-matcha scheduler (#6).

4. **darkzOGx/youtube-automation-agent** ("AgentTube") — https://github.com/darkzOGx/youtube-automation-agent — MIT (LICENSE read in full; © 2025 YouTube Automation Agent Contributors) — ~3,849 stars — 71 commits, 4 releases; reliability hotfixes 2026-09-21; created 2025-08-14.
   Why: autonomous YouTube channel operator — research→script→narration→visuals→assemble→metadata→schedule→publish→analytics learning loop, approval-first gates, Shorts repurposing studio, safety gates blocking simulated video/missing narration/unresolved rights claims — a reference architecture for closing the studio→publish→learn loop on YouTube.

### Checked, not qualified / skipped this round

- jub0t/Concat (~3,750 stars, AGPL-3.0, read GitHub license page) — CapCut replacement with MCP API; would have filled the clipping-engine gap, but AGPL-3.0 kills white-label. NOT-INTEGRATED note written.
- calesthio/OpenMontage (~61,437 stars, AGPL-3.0, read GitHub license page) — agentic video production system (12 pipelines, 100+ tools, 700+ skills, Backlot storyboard); described, never copied. NOT-INTEGRATED note written.
- savior-systems/marketmind (MIT claimed, 1 star, 158 commits) — multi-agent social-media swarm (LangGraph); no traction, skipped.
- zhaoxuya520/reverse-skill (trending daily) — security/pentest skill pack; not agency relevant.
- All already-registered repos re-appearing on trending (paperclip, hindsight, univer, buzz, claude-code-action, mobile-mcp) — no re-evaluation.

## 2026-09-27 01:50 EDT — hourly scan

Sources checked: GitHub trending daily + weekly, targeted searches (agent skill packs, social schedulers, short-form video pipelines/caption tools, n8n marketing workflows, design systems/analytics).
Seen-list checked against `SOURCES.md` (#1–23 + rejections) — none of the qualifiers below are registered.

### QUALIFIED (5) — all MIT, LICENSE file read in full via raw.githubusercontent.com

1. **social-media-skills/skills** — https://github.com/social-media-skills/skills — MIT (LICENSE read in full; © 2026 Frank Heijdenrijk; standard MIT, no carve-outs) — ~104 stars — 7 commits; last updated ~9 days ago; created 2026-07-16.
   Why: 106-agent social-media skill pack (strategy, writing, video, design, platform growth, publishing, analytics) with a dedicated "Agency & Client Management" topic pack — a much bigger sibling to #1 (charlie947, 17 skills) for the skills-library, directly white-label.

2. **yukitorido/short-video-generator-AI** — https://github.com/yukitorido/short-video-generator-AI — MIT (LICENSE read in full; © 2026 yukitorido) — ~718 stars — 10 commits; created 2026-09-23 (4 days ago).
   Why: long-video → viral 9:16 shorts pipeline (faster-whisper local transcription, LLM virality-scored highlight detection, auto-crop, AI hooks, CLI + web UI) — the first CLEAN-MIT answer to the agency's open clipping-engine gap (Concat/OpenMontage were AGPL rejects).

3. **hassancs91/claude-youtube-editor** — https://github.com/hassancs91/claude-youtube-editor — MIT (LICENSE read in full; © 2026 Hasan Aboul Hasan) — ~305 stars — 6 commits; last updated ~39 days ago; created 2026-07-19.
   Why: Claude Code-driven video editor — record the talking head, the agent does the cut, visuals, voiceover, SFX, thumbnail, and YouTube upload, all screen moments built as Remotion TSX (never screen-recorded); agent-driven editing patterns for studio reels/video.

4. **yuricrystal/n8n-marketing-flows** — https://github.com/yuricrystal/n8n-marketing-flows — MIT (LICENSE read in full; © 2026 Yuri (@yuri.learns)) — ~178 stars — 7 commits; created 2026-06-26 (template library; ~3 months quiet, expected for static templates).
   Why: 79 importable n8n marketing-automation workflow templates — 19 runnable local-Ollama (hashtag gen, multi-platform drafts, SEO rewrite, news digest) + 59 architecture skeletons (social publish/analytics, FB ads auto-pause, comment management, YouTube, WordPress) — direct fuel for the agency's n8n cloud.

5. **cbsshekhawat18-lab/social-stats-social-media-manager** — https://github.com/cbsshekhawat18-lab/social-stats-social-media-manager — MIT (LICENSE read in full; © 2026 Chandrabhan Shekhawat — Gigai Kripa Services) — ~10 stars — 58 commits, 1 release; last updated ~9 days ago; created 2026-06-26.
   Why: full self-hostable Hootsuite alternative (Django + React): scheduler + content calendar, cross-platform analytics, unified inbox, WhatsApp/CTWA bot builder, Claude-powered AI Studio, and multi-client agency workspaces with approval flows — a white-label client-dashboard candidate beside #6 (Anil-matcha) and #22 (shoutrrr).

### Checked, not qualified / skipped this round

- Postiz (AGPL-3.0 per PRD doc) — copyleft, rejected (openshorts rule).
- mutonby/openshorts re-check (5,696 stars, NOASSERTION license) — still excluded; commercial carve-out documented 2026-09-27.
- deepak-ai-93/deepak-skill (MIT, 65 commits) — only 1 star, no traction; rich content-creator stack but marginal.
- nagacash/social-post-forge, virajsutar-marketer/social-media-agent, AvtandilMghebrishvili/YOUTUBETECHCRUSH — single-skill repos, low/no traction; covered by #1/#2 above.
- harry0703/MoneyPrinterTurbo (~104k stars, MIT claimed) — text→AI-video generator, not a long→short clipper; repo dates to 2024/25 (not new), LICENSE not re-verified this round.
- jzferrell26/auto-video-agent (MIT, 3 stars), BerniceMata/autoclip (MIT, 0 stars, fork, pre-1.0) — no traction; covered by #2.
- Trending daily/weekly re-checks: addyosmani/agent-skills, openbao/openbao, NVIDIA/Model-Optimizer, zhaoxuya520/reverse-skill, cloudflare/security-audit-skill — all dev/infra/security, not agency relevant.
- All already-registered repos re-appearing on trending (paperclip, hindsight, univer, buzz, claude-code-action, mobile-mcp, WeKnora, orca, knowledge-work-plugins, deer-flow, openui, hermes-agent) — no re-evaluation.

## 2026-09-27 02:50 EDT — hourly scan

Sources checked: GitHub trending daily + weekly, targeted GitHub API searches (short-form video clippers, social media schedulers, n8n marketing workflows, marketing agent skills — created recent, sorted by stars).
Seen-list checked against `SOURCES.md` (#1–23 + rejections) and prior log entries (23:50, 01:00, 01:50 runs) — the qualifier below is not registered.

### QUALIFIED (1) — MIT, LICENSE file read in full via GitHub API

1. **nextlevelbuilder/ui-ux-pro-max-skill** — https://github.com/nextlevelbuilder/ui-ux-pro-max-skill — MIT (LICENSE read in full via API; © 2024 Next Level Builder; standard MIT, no carve-outs) — ~130,895 stars — created 2025-11-30; last pushed 2026-09-26.
   Why: an AI skill that provides design intelligence for professional UI/UX across platforms — feeds the agency's creative/design agents and the "design systems" lane (carousel layouts, newsletter templates, web modules).

### Checked, not qualified / skipped this round

- Short-form video clipper search (created >2026-08-01): all results 0–4 stars (red16124724/Aurum-Clipper 4★ NOASSERTION, loe007007/video-quote-clipper 1★ MIT, jinlh060109-cyber/laya-clipper 1★ MIT, egga-fx/xclips 1★ MIT, etc.) — no traction; covered by yukitorido/short-video-generator-AI from the 01:50 run.
- n8n marketing workflows (created >2026-08-15): all 0–1 stars (spirit4d/marketing-workflows-n8n 0★, reynaldonikola/affiliate-marketing-automation 1★, etc.) — no traction; covered by yuricrystal/n8n-marketing-flows (79 templates, 01:50 run).
- Marketing agent skills (created >2026-08-15): LeeHueeng/store-screenshots (86★ MIT, app-store-screenshot niche), axelfreeman/marketing-mindset (33★ MIT), quocbao201104/marketing-agent-skills (11★ MIT), ztemerbekov/a1-marketing-skills (8★ MIT) — marginal traction, marketing-skill lane already covered by knowledge-work-plugins (marketing plugin) + social-media-skills/skills (106 skills, 01:50 run).
- Trending daily/weekly re-checks: addyosmani/agent-skills (engineering skills, skipped twice before), ECC, Octop, treg, cloudflare/security-audit-skill, openbao, NVIDIA/Model-Optimizer, zhaoxuya520/reverse-skill, anthropics/financial-services — dev/infra/security, not agency relevant.
- All already-registered repos re-appearing on trending (paperclip, hindsight, univer, buzz, claude-code-action, mobile-mcp, WeKnora, orca, knowledge-work-plugins, deer-flow, openui, hermes-agent) — no re-evaluation.

## 2026-09-27 03:50 EDT — hourly scan

Sources checked: GitHub trending daily, targeted GitHub API searches (ai agent framework, social media scheduler, short-form video clipper/captions, n8n marketing workflows, marketing agent skills, design system agent skills, agent learning loop — all created >2026-08-15, sorted by stars).
Seen-list checked against `SOURCES.md` (#1–24 + rejections) and prior log entries (23:50, 01:00, 01:50, 02:50 runs) — none of the qualifiers below are registered.

### QUALIFIED (2) — both MIT, LICENSE file read in full via raw.githubusercontent.com

1. **deepakness/cogsend** — https://github.com/deepakness/cogsend — MIT (LICENSE read in full; © 2026 DeepakNess; standard MIT, no carve-outs) — ~139 stars, 23 forks — created 2026-09-22; last pushed 2026-09-27 (active); SvelteKit/TypeScript.
   Why: self-hosted social media scheduler ("write once, publish to any connected platform") that runs on YOUR OWN Cloudflare account — a white-label client-dashboard candidate beside #6 (Anil-matcha), #22 (shoutrrr), and #23's social-stats manager; Cloudflare-deployed means near-zero infra cost per client brand.

2. **Tranz007/ux-skills** — https://github.com/Tranz007/ux-skills — MIT (LICENSE read in full; © 2026 Tony Moura; standard MIT, no carve-outs) — ~44 stars, 4 forks — created 2026-08-20; last pushed 2026-09-04 (quiet ~3 weeks).
   Why: agent skills for working UX designers — challenge ideas, find blind spots, use the real design system, preserve evidence and decisions, carry UX intent into engineering; feeds the creative/design agents' design lane and decision-preservation discipline (evidence loop adjacent). Low traction; treat as pattern reference, not core.

### Evaluated and REJECTED

- **Vincentwei1021/video-talkcraft** (~1,246 stars, 117 forks) — agent skill turning Claude Code/Codex into a motion-design studio for voiceover explainer videos (109 motion recipe cards, Remotion rendering) — LICENSE read in full: **PolyForm Noncommercial 1.0.0** — "noncommercial use is free; any commercial use of the toolkit requires prior authorization from the author." Commercial carve-out = rejected for white-label agency use. Described, never copied.
- **QingYunA/agent-html** (~39 stars, pushed 2026-09-26) — zero-dependency single-file HTML design system + agent skill (shadcn/ui-inspired) — GitHub API reports license:null; LICENSE file 404 on main and master branches = effectively unlicensed. Described, never copied.

### Checked, not qualified / skipped this round

- Short-form video clipper/caption searches (created >2026-08-15): Dante-Clippers-Ai (1★, no license), youtube-short-clipper (0★, no license), temonwkwk/clipper (no stars/license shown) — no traction; lane covered by yukitorido/short-video-generator-AI (01:50 run).
- n8n marketing workflows (created >2026-08-15): affiliate-marketing-automation (1★, no license), creator-marketing-automation (1★, no license), abandoned-cart-recovery-n8n — no traction, unlicensed; covered by yuricrystal/n8n-marketing-flows (01:50 run).
- Marketing agent skills: LeeHueeng/store-screenshots (86★ MIT, app-store-screenshot niche, already noted 02:50), axelfreeman/marketing-mindset (33★ MIT, already noted 02:50), zaferayan/app-store-screenshot-skill — marginal/niche; skills lane covered.
- Agent learning-loop search: Code-Agent-Learning (10★), mattwfog/harness (2★), ValentynaJasochka/adaptive-learning-agent — coding-agent learning/educational, no agency fit; covered by hermes-agent + hindsight.
- AI agent framework search: calmrocks/ai-engineer-notebooks (642★ MIT, educational notebooks — dev-focused, not agency operational), d4ncboz/github-farm (343★ MIT, OAuth harvesting — security-adjacent, not agency fit), Agenta-AI/awesome-ai-agent-platforms (curated list, no software).
- Trending daily: rohitg00/ai-engineering-from-scratch — educational; all other trending repos (paperclip, hindsight, univer, buzz, claude-code-action, mobile-mcp) already registered — no re-evaluation.

### License-policy notes this round
- GitHub-detected MIT accepted when the LICENSE file is present and read in full (cogsend, ux-skills — both read via raw.githubusercontent.com).
- NOASSERTION license (video-talkcraft) triggered the full-file read — caught a PolyForm Noncommercial carve-out. The openshorts rule holds.
- license:null + 404 on both LICENSE branch paths (agent-html) = unlicensed, excluded per policy.


## 2026-09-27 04:50 EDT — hourly scan

Sources checked: GitHub trending daily (repo list is JS-rendered — only filter lists readable via text fetch; used the GitHub search API as fallback), targeted GitHub API searches (agent skills created >2026-06-01, social media scheduler, n8n workflow, short-form video clipper/captions — all created recent, sorted by stars).
Seen-list checked against `SOURCES.md` (#1–26 + rejections) and prior log entries (23:50, 01:00, 01:50, 02:50, 03:50 runs) — all below are new to the registry.

### QUALIFIED (6) — MIT or Apache-2.0, LICENSE file read in full via raw.githubusercontent.com

1. **artbyjazi/autoclip** — https://github.com/artbyjazi/autoclip — MIT (LICENSE read in full; © 2026 Jad Ghazi; standard MIT, no carve-outs) — ~145 stars, 47 forks — created 2026-07-31; last pushed 2026-08-01 (~2 months quiet, young repo).
   Why: open-source LOCAL-FIRST AI video clipper — long video in, caption-burned speaker-tracked 9:16 clips out, fully offline with Whisper + Ollama or BYO key (FastAPI + React). A second clean-MIT answer to the agency's open clipping-engine gap beside yukitorido/short-video-generator-AI (01:50 run); the two should be A/B-compared for the studio reels lane.

2. **genspark-ai/genoffice** — https://github.com/genspark-ai/genoffice — Apache-2.0 (LICENSE read in full; © 2026 Mainfunc, Inc.; standard Apache-2.0, no carve-outs) — ~7,924 stars, 1,030 forks — created 2026-07-31; last pushed 2026-09-27 (today); TypeScript.
   Why: free open-source AI Office suite (Docs, Sheets, Slides, PDF, Markdown, HTML editors) with a built-in AI agent, a `genoffice` CLI, and an agent skill so coding agents create/edit real .docx/.xlsx/.pptx files locally — feeds the creative/design agents' deck, report, and newsletter-document lanes (complements univer, which is the spreadsheet/data canvas).

3. **jakubkrehel/skills** — https://github.com/jakubkrehel/skills — MIT (LICENSE read in full; © 2026 Jakub Krehel; standard MIT) — ~7,204 stars, 266 forks — created 2026-07-10; last pushed 2026-08-29; Markdown.
   Why: a collection of agent skills for building great interfaces — design-lane feed for the creative/design agents, beside ui-ux-pro-max-skill (#24), Tranz007/ux-skills (#26), and openui patterns.

4. **s1dashu/ip-as-logo-skill** — https://github.com/s1dashu/ip-as-logo-skill — MIT (LICENSE read in full; © 2026 s1dashu; standard MIT) — ~5,589 stars, 274 forks — created 2026-08-18; last pushed 2026-08-22.
   Why: compact Agent Skill for generating highly simplified, rounded, neo-skeuomorphic IP mascot logos — a brand-mascot/logo lane for the creative/design agents across white-label client brands.

5. **BuilderIO/skills** — https://github.com/BuilderIO/skills — MIT (LICENSE read in full; © 2026 Builder.io; standard MIT) — ~4,444 stars, 224 forks — created 2026-06-10; last pushed 2026-09-25.
   Why: composable Agent-Native skill set — `/visual-plan` and `/visual-recap` (rich interactive plans/diffs), `/agent-watchdog` (audit another agent's work), `/plan-arbiter` (pick winning plan across agents), `/plow-ahead` (autonomy through ordinary ambiguity), `/factory-*` (feedback→policy-gated delivery loop), `/stay-within-limits` (usage-budget guardrails). Direct patterns for the ops agent running the 8-agent fleet: cross-agent audits, plan arbitration, and bounded autonomy.

6. **banmu123/LoomFlow** — https://github.com/banmu123/LoomFlow — MIT (LICENSE read in full; © 2026 ForgeFlow contributors; standard MIT) — ~223 stars, 9 forks — created 2026-08-12; last pushed 2026-09-16; TypeScript/Next.js.
   Why: lightweight AI-native workflow builder ("describe your idea in natural language, get a runnable workflow on a visual canvas, publish it as an API") — an open-source alternative to Dify/n8n with one-command Docker self-hosting. Alternative/addition to the agency's n8n cloud lane.

### Evaluated and REJECTED

- **chuspeeism/dashi-ppt-skill** (~8,852 stars) — AI-agent skill generating browser-editable presentations from visual themes — **AGPL-3.0** (license file read). AGPL network copyleft = excluded. Described, never copied.
- **internet-court/internet-court-skill** (~6,226 stars) — trust layer / agent-to-agent commerce skill — GitHub API reports license "other"/**NOASSERTION** (no verified permissive license) = excluded per policy.
- **larashero3-dotcom/lieflat-charts** (~5,728 stars) — data-visualization skill turning data into polished HTML charts — **NOASSERTION** = excluded per policy.
- **feyzilim/clipfactory** (~105 stars) — topic+template → short vertical video from B-roll (AI script, voice, captions, FFmpeg render) — described license is **Elastic 2.0** (source-available, not MIT/Apache) = excluded for white-label.
- **ColinGPT9/clips-studio** (~64 stars, pushed today) — free open-source Opus Clip alternative (multimodal clip detection, speaker-aware face tracking, editable captions, AI edit chat, local-only) — **AGPL-3.0** = excluded (same treatment as Concat/OpenMontage rejects).
- **oktaydbk54/vibeclip** (~58 stars) — self-hosted AI video editor: long videos → captioned 9:16 shorts, edit by chatting — **AGPL-3.0** = excluded.
- **AhsanAyaz/ossclip** (~56 stars) — local-first CLI video producer (silence cutting, word-timed captions, face-aware framing) — **NOASSERTION** = excluded per policy.

### Checked, not qualified / skipped this round

- cloudflare/security-audit-skill — already evaluated in 23:50/01:50/02:50 runs; skipped as not agency-relevant (MIT re-verified this round but the relevance call stands).
- yuricrystal/n8n-marketing-flows — same repo as YuriCrystal/n8n-marketing-flows qualified in the 01:50 run (GitHub names case-insensitive); no re-registration.
- deepakness/cogsend — already registered (#25); re-appeared in the scheduler search, no re-evaluation.

### License-policy notes this round
- Three would-be clipper winners (ColinGPT9/clips-studio, oktaydbk54/vibeclip) plus dashi-ppt-skill all hit AGPL — the clipping lane keeps drawing copyleft entries; autoclip (#27) and yukitorido's pipeline (01:50 run) remain the clean options.
- NOASSERTION entries are growing (internet-court, lieflat-charts, ossclip) — policy holds: no permissive license file = described, never copied.

## 2026-09-27 05:50 EDT — hourly scan

Sources checked: GitHub trending daily (page fetched and read — mostly already-registered: paperclip, hindsight, univer, buzz, claude-code-action, mobile-mcp), GitHub search API for repos created >2026-08-27 sorted by stars across 8 query lanes (agent frameworks, agent skills, social schedulers, video clippers, n8n workflows, caption tools, design systems, analytics/learning loops) — 96 unique repos triaged.
Seen-list checked against `SOURCES.md` (#1–32 + rejections) — none of the qualifiers below are registered.

### QUALIFIED (14) — all MIT or Apache-2.0, LICENSE file actually read in full via API

1. **Nanako0129/sepia** — https://github.com/Nanako0129/sepia — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~2,878 stars — created 2026-08-28, pushed 2026-09-23.
   Why: 77+ de-AI writing skills for any Agent Skills-compatible agent — professionalizes the writing agent's copy lane.

2. **shadcn-ui/lint** — https://github.com/shadcn-ui/lint — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~2,849 stars — created 2026-09-02, pushed 2026-09-22.
   Why: agent-first linter for Tailwind design systems — design-QA guardrail for the creative/design agents' web and carousel output.

3. **cbrock84/headcount** — https://github.com/cbrock84/headcount — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~1,682 stars — created 2026-08-28, pushed 2026-09-17.
   Why: agent organization structured as a company — 15+ departments, 125+ skills, each independently deployable — a reference model for evolving the 8-agent fleet's org design.

4. **achimala/dream-loop** — https://github.com/achimala/dream-loop — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~1,569 stars — created 2026-09-07, pushed 2026-09-09.
   Why: agent skill for impressive 3D visuals (Blender + image gen + subagent critic loop) — adds a 3D capability to studio creative.

5. **jtydhr88/screenwriting-skills** — https://github.com/jtydhr88/screenwriting-skills — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~1,421 stars — created 2026-09-06, pushed 2026-09-22.
   Why: professional agent skills for screenwriting, television writing, and dramaturgy — script craft for studio reels and livestream segments.

6. **mikehasa/golive-skill** — https://github.com/mikehasa/golive-skill — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~990 stars — created 2026-09-23, pushed today (2026-09-27).
   Why: take an agent-built product live — hosting, database, domain, email, payments on your own accounts — a deployment-runbook skill for the webmaster agent.

7. **kerpopule/hermes-jev-skills** — https://github.com/kerpopule/hermes-jev-skills — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~855 stars — created 2026-09-18, pushed today (2026-09-27).
   Why: Jev-powered model routing, memory, compaction, skill selection, plus computer and browser use — ops-agent building blocks for fleet efficiency.

8. **Jakeschincariol/linkedin-agent-skill** — https://github.com/Jakeschincariol/linkedin-agent-skill — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~758 stars — created 2026-09-07, pushed 2026-09-17.
   Why: 11 free Claude skills that run a LinkedIn account (posts off 21 hook formulas, comments, replies) — a plug-in toolkit for the outreach agent.

9. **BoardUI/boardui** — https://github.com/BoardUI/boardui — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~532 stars — created 2026-09-01, pushed 2026-09-05.
   Why: React design system purpose-built for agentic interfaces, every component as source — component feed for webmaster/client-facing deliverables.

10. **bangtutorial/bang-motion** — https://github.com/bangtutorial/bang-motion — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~524 stars — created 2026-09-05, pushed 2026-09-15.
    Why: agent skill for browser motion graphics — openers, promos, bumpers, kinetic typography — a motion lane for studio reels.

11. **tin-computer/tin** — https://github.com/tin-computer/tin — Apache-2.0 (LICENSE read in full; the "commercial" hit is standard Apache §8 boilerplate "commercial damages", not a carve-out) — ~79 stars — created 2026-09-17, pushed 2026-09-26. Tree: ~1,100 files, real implementation.
    Why: open-source marketing system designed for coding agents with 26+ ready workflows — the closest thing to an out-of-box agency playbook library.

12. **umschaudhary/verticlip** — https://github.com/umschaudhary/verticlip — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~2 stars — created 2026-09-22, pushed 2026-09-22. Tree: 56 files, real pipeline (yt-dlp→Whisper→LLM pick→ffmpeg render→publish→submissions.csv).
    Why: lean CLI-first local clipper (Whisper+Ollama, no API key), 44-file footprint vs autoclip's backend-heavy 100 — a lighter third option for the clipping-gap A/B beside autoclip (#27) and yukitorido/short-video-generator-AI.

13. **jinlh060109-cyber/laya-clipper** — https://github.com/jinlh060109-cyber/laya-clipper — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~1 star — created 2026-09-25, pushed 2026-09-25. Tree: 121 files, real implementation.
    Why: local clipper (Whisper + any LLM scoring + ffmpeg) with an optional AI-director that adds Remotion motion graphics — clipper + motion lane in one for the studio reels pipeline.

14. **VBS2004/jevcut** — https://github.com/VBS2004/jevcut — MIT (LICENSE read in full, standard MIT, no carve-outs) — ~1 star — created 2026-09-26, pushed today (2026-09-27). Tree: 566 files incl. an eval harness.
    Why: auto-clipper that enumerates every possible cut and has an AI judge pick winners, with a benchmark suite — the eval-harness angle feeds the agency learning loop.

### Checked, not qualified / skipped this round

- GitHub trending daily newcomers: NVIDIA/Model-Optimizer (model optimization infra), rohitg00/ai-engineering-from-scratch (learning repo), openbao/openbao (secrets management — not an agency lane), zhaoxuya520/reverse-skill (security — not agency relevant), llvm, tensorflow, vscode, next.js — infra/dev, skipped.
- Already-registered repos re-appearing on trending daily (paperclip, hindsight, univer, buzz, claude-code-action, mobile-mcp) — no re-evaluation.
- deepakness/cogsend — already registered (#25); re-appeared in the scheduler search, no re-evaluation.
- mcncarl/jianying-headless (~2,780 stars, trending in the search) — NOASSERTION license = excluded per policy; described, never copied.
- Abhishek-B-R/social0-oss (3★) — AGPL-3.0 = excluded. muneebkhan08/Capite — same repo as registered #3 (case-insensitive name), skipped.
- Low-traction clipper/caption entries (0★, unlicensed, or stubs) — nothing with substance beyond the 3 qualified clippers above.
- NOTE: yukitorido/short-video-generator-AI (01:50 run, MIT, qualified) was never added to the SOURCES.md registry table — registered retroactively as #33 in this run.

### License-policy notes this round

- mcncarl/jianying-headless (~2,780★, biggest star count in the clipper search) is NOASSERTION — popularity doesn't override policy: no license = described, never copied.
- tin-computer/tin's Apache-2.0 file contains the word "commercial" — verified in context to be the standard Apache §8 liability boilerplate ("any and all other commercial damages or losses"), not a carve-out. Clean.
- All 14 qualifiers had their LICENSE file read in full (not badge-only) per the openshorts rule; all are standard MIT (~1,068 chars) or standard Apache-2.0, no carve-outs found.

## 2026-09-27 06:50 EDT — hourly scan

Sources checked: GitHub trending daily, targeted web searches (social schedulers, AI video clippers, n8n workflow packs, agent skills/marketing).
Seen-list checked against `SOURCES.md` (#1–47 + rejections) — none of the qualifiers below are registered.

### QUALIFIED (4) — all MIT or Apache-2.0, LICENSE file actually read in full

1. **Anil-matcha/AI-Youtube-Shorts-Generator** — https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator — MIT (LICENSE read in full; © 2026 Anil Chandra Naidu Matcha; standard MIT, no carve-outs) — ~5,152 stars, 940 forks — created 2024-06-28, pushed 2026-09-17.
   Why: open Opus Clip alternative — YouTube link in, viral 9:16 shorts out via LLM highlight detection + Whisper transcription + auto vertical crop; free, no watermarks, no per-clip credits. Strongest-trafficked clean-MIT clipper found so far — prime A/B contender for the clipping-engine gap. (Note: different repo from the same author's scheduler #6.)

2. **NaufalRizqullah/opensource-clipping** — https://github.com/NaufalRizqullah/opensource-clipping — MIT (LICENSE read in full; © 2026 Muhammad Naufal Rizqullah; standard MIT, no carve-outs) — 128 stars, 62 forks — created 2026-04-04, pushed 2026-09-26 (yesterday).
   Why: AI auto-clipper with smart face-tracking, kinetic karaoke subtitles, contextual B-roll, AI voice-overs, and auto-uploaders (YouTube/FB) — Whisper + Gemini + MediaPipe + Pyannote stack; the auto-uploader lane feeds the social-publishing agent. Another clipping-gap A/B option.

3. **heygen-com/hyperframes** — https://github.com/heygen-com/hyperframes — Apache-2.0 (LICENSE read in full; © 2026 HeyGen, Inc.; standard Apache-2.0, no carve-outs) — ~53,465 stars, 4,878 forks — created 2026-03-10, pushed 2026-09-27 (today).
   Why: "Write HTML. Render video. Built for agents" — agent-skill-driven video production loop (plan video, write valid HTML, wire seekable animations, add media, lint, preview, render; ffmpeg/GSAP/Puppeteer/MCP). Motion-graphics lane for studio reels — complements (and is more mature than) the smaller bang-motion skill (#43).

4. **ruvnet/ruflo** — https://github.com/ruvnet/ruflo — MIT (LICENSE read in full; © 2024-2026 ruvnet; standard MIT, no carve-outs) — ~73,355 stars, 8,710 forks — created 2025-06-02, pushed 2026-09-27 (today).
   Why: "original agent harness" — multi-player swarms, adaptive memory, self-learning intelligence, federation, vector RAG, native Claude Code/Codex/Hermes integration. Swarm-coordination + self-learning reference for the ops agent fleet and the agency learning loop, alongside the paperclip evaluation.

### Checked, not qualified / skipped this round

- GitHub trending daily: paperclip, hindsight, univer, buzz, claude-code-action, mobile-mcp (all registered — no re-evaluation); NVIDIA/Model-Optimizer, openbao/openbao, zhaoxuya520/reverse-skill, rohitg00/ai-engineering-from-scratch, tensorflow, vscode, next.js, llvm, actions/runner-images — infra/dev/security, not agency lanes.
- postmill-ai/postmill-app (AGPL-3.0, GitHub API license field, ~12 stars) — AI-native social scheduler with 45+ channels; AGPL → rejected, registered in rejections table. Described, never copied.
- getopenpost/openpost (AGPL-3.0-only) — self-hosted social publisher with agent MCP access; AGPL → rejected, registered.
- borghei/Claude-Skills (831★, 372 skills + fresh Sept 2026 marketing skills) — license NOASSERTION/"Other" → excluded per policy, registered in rejections table. Described, never copied.
- workflowammar/n8n-tools-template-by-ammar — unlicensed fork (1★) → skipped; n8n template searches otherwise surfaced the already-noted enescingoz/awesome-n8n-templates family and a paywalled Gumroad pack (medoxisto) → skipped.
- Search also surfaced: PriyeshPandey2000/ai-video-clipper (license unconfirmed, Mac-only app), authrain-cloud-ai-clipping-generator (0★, single commit), agra-aarav15/clipblitz-ai-shorts (0★) — thin traction, not qualified.
- Erricosiu/ai-marketing-skills short-form-pipeline updates — repo already registered (#14); new file contents fold into existing integration context.
- jub0t/Concat, calesthio/OpenMontage, openshorts etc. re-appearing in searches — already in rejections table, no re-evaluation.

### License-policy notes this round

- All 4 qualifiers had their LICENSE file read in full (raw.githubusercontent) — not badge-only; all standard MIT/Apache-2.0, no carve-outs.
- Borghei/Claude-Skills illustrates the rule: 831★ and actively maintained, but license:null/NOASSERTION = described, never copied.

## 2026-09-27 07:50 EDT — hourly scan

Sources checked: GitHub trending daily, recent-star search (created >2026-08-27, stars >10), targeted searches (self-hosted social schedulers, n8n workflow packs).
Seen-list checked against `SOURCES.md` (#1–51 + rejections) — none of the qualifiers below are registered.

### QUALIFIED (6) — all MIT or Apache-2.0, LICENSE file actually read in full

1. **Human-Agent-Society/reef** — https://github.com/Human-Agent-Society/reef — Apache-2.0 (LICENSE read in full; standard Apache, no carve-outs) — 6,265 stars, 564 forks — pushed 2026-09-27 (today).
   Why: "Infrastructure for continually self-improving agents" — learning-loop reference model (retain/recall/reflect) that sits alongside hindsight (#8); feeds the agency's self-improving-agent lane and the ops fleet.

2. **Albert-Weasker/niubigeo** — https://github.com/Albert-Weasker/niubigeo — Apache-2.0 (LICENSE read in full; standard Apache, no carve-outs) — 4,854 stars, 305 forks — pushed 2026-09-21.
   Why: open-source AI brand visibility and competitor reports — GEO/brand-mention analytics the research + outreach agents can run per client; first brand-visibility tool found.

3. **NVlabs/SoL-Pi** — https://github.com/NVlabs/SoL-Pi — MIT (LICENSE read in full; © 2026 NVIDIA CORPORATION & AFFILIATES; no carve-outs) — 3,124 stars, 248 forks — pushed 2026-09-27 (today).
   Why: "Scaling Auto-Research Loops for Efficient Agent Harnesses" — auto-research-loop patterns from NVIDIA for the research agent's deep-research harness design.

4. **Ryze-AI-Adgent/open-seo-mcp-skills** — https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills — MIT (LICENSE read in full; © 2026 Ryze AI; no carve-outs) — 2,254 stars, 355 forks — pushed 2026-09-24.
   Why: free SEO MCP server + SEO/GEO skills for Claude that run on the user's REAL GSC/GA4/ads data (not estimates) with DataForSEO built in for backlinks/SERPs — distinct from open-seo (#21)'s open-Semrush approach; SEO-agent toolchain upgrade.

5. **anthropics/claude-plugins-official** — https://github.com/anthropics/claude-plugins-official — Apache-2.0 (LICENSE read in full; standard Apache, no carve-outs) — 37,074 stars, 4,163 forks — pushed 2026-09-25.
   Why: Anthropic-managed official directory of high-quality Claude Code plugins (internal + vetted third-party marketplace) — a curated ongoing skill-sourcing lane for the 17-skill library.

6. **YuriCrystal/n8n-marketing-flows** — https://github.com/YuriCrystal/n8n-marketing-flows — MIT (LICENSE read in full; © 2026 Yuri (@yuri.learns); no carve-outs) — 178 stars, 51 forks — pushed 2026-06-27.
   Why: 79 import-ready n8n marketing automation templates (social/sentiment/news/ads/SEO) — first real n8n workflow pack found for the cloud lane. Recency note: last push 2026-06-27, but content is a stable template library, so it qualifies on substance.

### Checked, not qualified / skipped this round

- Recent-star scan mostly surfaced AI-infra/dev noise (NandhaKishorM/laya, browser-use/jev-ultrafast, zai-org/ZCode, NVIDIA/Model-Optimizer) — not agency lanes.
- Vincentwei1021/anything2explainer (~2.1k★, topic-in/narrated-explainer-video-out skill) — NOASSERTION license → rejected, registered in rejections table. Same author had a PolyForm-Noncommercial rejection earlier.
- realchandan/post-scheduler (17★, self-hosted social scheduler) — AGPL-3.0 → rejected, registered in rejections table.
- agno-agi/dash (~2.3k★, self-learning data agent, Apache-2.0) — pushed 2026-07-10, stale; skipped this round.
- Mfrostbutter/n8n-workflow-templates (18★, 5 forks, MIT, pushed 2026-09-21) — too low traction; skipped.
- cursor/agent-trace (YouTube trending mention) — 404 on GitHub API; repo doesn't exist or is renamed.
- deepakness/cogsend — already registered (#25); re-appeared in scheduler search, no re-evaluation.
- Previously-rejected repos re-appearing (borghei/Claude-Skills, postmill-app, openpost) — already in rejections table, no re-evaluation.

### License-policy notes this round

- All 6 qualifiers had their LICENSE file read in full (raw.githubusercontent) — not badge-only; all standard MIT/Apache-2.0, no carve-outs.
- anything2explainer illustrates the rule again: ~2.1k★ and actively maintained, but license:null = described, never copied.

## 2026-09-27 08:50 EDT — hourly scan

Sources checked: GitHub search API across 6 lanes (agent skills, social schedulers, short-form video clippers, n8n marketing workflows, video caption tools, design-system skills — created >2026-08-20, sorted by stars) + new-repos sweep (created >2026-09-13, >50 stars, 20 repos).
Seen-list checked against `SOURCES.md` (#1–57 + rejections) and all prior log runs — the 2 qualifiers below are new to the registry.

### QUALIFIED (2) — both MIT, LICENSE file read in full via raw.githubusercontent.com (openshorts rule)

1. **nateherkai/scroll-craft** — https://github.com/nateherkai/scroll-craft — MIT (LICENSE read in full; © 2026 Nate Herk; standard MIT, no carve-out keywords) — 2,808 stars, 403 forks — created 2026-08-22, pushed 2026-09-04.
   Why: agent skill for building premium, immersive, scroll-driven websites (works with Codex, Claude Code, and other coding agents) — a design+web lane for the creative/design and webmaster agents: campaign sites, landing pages, animated brand experiences.

2. **Devesh-Shirsath/spotkit** — https://github.com/Devesh-Shirsath/spotkit — MIT (LICENSE read in full; © 2026 Devesh Shirsath; standard MIT, no carve-out keywords) — 63 stars, 7 forks — created 2026-09-08, pushed 2026-09-11.
   Why: Claude Code skill that turns a feature description into minimal, abstract SVG product illustrations — brand-visual lane for the creative/design agents. Low traction; treat as pattern reference, not core.

### Checked, not qualified / skipped this round

- mcncarl/jianying-headless (2,793★) — NOASSERTION license; excluded per policy (flagged again in new-repo sweep). Described, never copied.
- typesafe-ai/skills (2,240★ MIT) — TypeSafe vendor SDK skills; not agency operational.
- kharmanskyi/open-steps (951★ MIT) — coding-agent output → plain-language reports; marginal for a marketing agency; comms lane covered.
- deonmenezes/edit-ai (2★ MIT) — AI video-edit harness; no traction; video-editing lane already covered.
- gulliblebui/OpusClip-Desktop---Opus-Clip-AI-2026 (8★ MIT) — clipper lane saturated with better options; skip.
- Curvechotunnel/CAPCUT-PRO-CRACK — license "other", name reads as a crack distribution; skipped on smell.
- egga-fx/xclips (1★ MIT), red16124724/Aurum-Clipper (4★, no license), Faruq1539/Dante-Clippers-Ai (1★, no license) — thin/no traction; clipper lane covered.
- fajrisilmi12-cyber/hermes-socmed-function (20★ MIT) — social posting skills; thin; scheduler lane well covered.
- Pinlyx/pinlyx-mcp (5★), profullstack/mynaposter (4★), AXT224/AXT-Social (2★) — thin scheduler/social-MCP entries; lanes covered.
- Abhishek-B-R/social0-oss (AGPL-3.0) — already noted as copyleft reject pattern; skipped.
- n8n lane: all results 0–1 stars, mostly unlicensed "testing Marketing Workflow" forks — no traction; covered by YuriCrystal/n8n-marketing-flows (#57).
- thakur698/universal-ui-skills (5★ MIT), pedroanze/slizdeck (6★ MIT, Spanish) — thin design-skill entries; lane covered.
- New-repo sweep (20 repos, last 2 weeks): all AI-infra/dev noise (NandhaKishorM/laya 26k★, browser-use/jev-ultrafast, jev-family decision models, coding harnesses, CopilotKit/openmuse personal agent, tiny browsers) — none in agency lanes.
- All already-registered repos re-appearing in searches (sepia #34, headcount #36, dream-loop #37, screenwriting-skills #38, golive-skill #39, hermes-jev-skills #40, linkedin-agent-skill #41, laya-clipper #46, jevcut #47, video-talkcraft reject, cogsend #25) — no re-evaluation.

### License-policy notes this round

- Both qualifiers had LICENSE files fetched from raw.githubusercontent and read in full; grepped for carve-out keywords (commercial/agpl/noncommercial/polyform/elastic) — zero hits in both.
- Tooling note: bare `>` in curl URLs gets eaten as a shell redirect — use `--data-urlencode` for GitHub search query parameters.

## 2026-09-27 10:50 EDT — hourly scan

Sources checked: GitHub search API across 10 lanes (agent skills marketing, ai agent framework orchestration, social media scheduler selfhosted, short video clipper ai, n8n workflow marketing, video caption tool agent, design system agent skill, agent learning loop memory, seo agent skill, ai video editor agent — created >2026-08-20, sorted by stars, ~120 repos) + new-repo sweep (created >2026-09-13, >50 stars, 25 repos) as trending fallback.
Seen-list checked against `SOURCES.md` (#1–62 + rejections) and all prior log runs — the 2 qualifiers below are new to the registry.

### QUALIFIED (2) — both MIT, LICENSE file read in full via raw.githubusercontent.com (openshorts rule; carve-out keyword grep — zero hits)

1. **kurbaitaev/ghost-editor** — https://github.com/kurbaitaev/ghost-editor — MIT (LICENSE read in full; © 2026 kurbaitaev; standard MIT, no carve-outs) — ~61 stars, 4 forks — created 2026-09-24 (3 days old); 88-file tree, real implementation (SKILL.md, scripts/, examples/gallery of 7 reel styles, library/manifests).
   Why: AI video editor for talking-head reels as a Claude Code / agent skill — 7 reel styles, face-safe captions, motion scenes, "reverse-engineer any reference edit." Built ON HyperFrames (#50), so it plugs straight into the studio reels/motion lane alongside bang-motion (#43) and the HyperFrames render loop.

2. **calven-ai/marketing-as-code** — https://github.com/calven-ai/marketing-as-code — MIT (LICENSE read in full; © 2026 Calven AI, LLC; standard MIT, no carve-outs) — ~8 stars, 1 fork — created 2026-08-31, pushed 2026-09-24.
   Why: starter repo for a marketing team that "runs on code" — strategy, content, and decisions plus 99 agent skills as plain text a coding agent reads/writes, with a human review gate. Conceptually on-target for the agency's ops/fleet patterns; low traction so treat as pattern reference, not core.

### Checked, not qualified / skipped this round

- robbietilton/Compositor (5,845★ MIT) — "The Photoshop alternative for Mac" — Mac-only desktop app, not an agent skill or white-label component; skipped.
- unreallabsai/unreal-agent (1,981★ MIT) — generic async-first agent harness; agent-harness lane covered (paperclip, ruflo, deer-flow, orca, hermes-agent); not marketing-agency operational.
- retrogtx/ai-marketing-videos (4★), matt-j-penny/ai-video-marketing (2★), 808enzo/chappie (2★), folson-marketing/folson-marketing-skills (5★) — thin marketing-skill entries; lanes covered by knowledge-work-plugins (#23:50 run) + social-media-skills/skills (#01:50).
- ztemerbekov/a1-marketing-skills (8★), axelfreeman/marketing-mindset (33★), zaferayan/app-store-screenshot-skill (28★), LeeHueeng/store-screenshots (86★), RankSpotAI/awesome-seo-agent-skills (66★ CC0) — niche/curated-list/marginal; noted before or out of policy scope.
- Video-lane thin entries: fancyism/hyperremoedit-toolkit (0★), deonmenezes/edit-ai (2★, already skipped 08:50), 0xPasho/agentcut (4★ NOASSERTION — excluded), tydude001/proofcut (4★ NOASSERTION — excluded), Panoptik-Studio/Panoptik (5★ AGPL-3.0 — excluded), jdilla1277/moviestar (5★ Apache-2.0 — no traction, lane covered), alexrdiansyah-oss/AI-Clipper-Tools (GPL-3.0 — excluded), alexrexby/ai-video-editor-agent (2★), Mas-inx/lumen-ai-video-editor (1★), VuDuyTienPhat10/agentic-video-editor (1★), reactvideoeditor/react-video-editor-agent-skills (1★), daydreamvideo/daydream-mcp (2★), MrFadiAi/kino-seedance-studio (12★) — clipper lane saturated with stronger clean-MIT options.
- Agent-framework noise: Esaadatmand/Photon_orchestrator (12★), PebbleLog/SimonAgent (10★, NOASSERTION), hiroqt/PixelCrew (10★), kamalesh404/AgentMesh (5★), Epsirom/braid (3★), mwb1219/mwb-ai-claw (2★), Monesgoda/offensive-Agent-s (8★, offensive-security framing) — thin, not agency operational.
- Learning-loop search: all 0–1 stars or educational/coding-focused; covered by hermes-agent + hindsight + reef.
- n8n marketing workflows: all results 0–1 stars, mostly unlicensed fork spam ("marketing-workflows-n8n" cluster) — covered by YuriCrystal/n8n-marketing-flows (#57).
- Short-form video clipper search: laya-clipper (#46) and jevcut (#47) re-appeared (registered, no re-evaluation); everything else 0–4 stars or unlicensed.
- Trending-fallback new-repo sweep: NandhaKishorM/laya, browser-use/jev-ultrafast, jaredpalmer/kev, tamaratran/fast-jev-compaction, zai-org/ZCode, jev-chat/jev-chat-jarvis, mizorewww/laya-mlx, TheoLeeCJ/SemIf-OpenJev, TianyuCodings/NanoJev, hydra-db/open-glean, tobi/disktree, QwenLM/Qwen-Image-2.1 — all Jev-model/infra/dev, not agency lanes; mcncarl/jianying-headless (2,807★) NOASSERTION — still excluded per policy.
- All already-registered repos re-appearing in searches (sepia #34, seo-landing #62, laya-clipper #46, jevcut #47, etc.) — no re-evaluation.

### License-policy notes this round
- ghost-editor's LICENSE (raw.githubusercontent, main branch, HTTP 200, read in full) is standard MIT — accepted.
- NOASSERTION entries (agentcut, proofcut) excluded without further work; AGPL-3.0 (Panoptik) and GPL-3.0 (AI-Clipper-Tools) excluded.
- Tooling lesson: curl `--data-urlencode` implies POST on the GitHub API (returns 404); must pair it with `--get`. Noted for future runs.

## 2026-09-27 11:50 EDT — hourly scan

Sources checked: GitHub search API across 10 lanes (agent skills marketing, ai agent framework orchestration, social media scheduler selfhosted, short video clipper ai, n8n workflow marketing, video caption tool agent, design system agent skill, agent learning loop memory, seo agent skill mcp, ai video editor agent skill — created >2026-08-20, sorted by stars, ~130 repos) + new-repo sweep (created >2026-09-25, >30 stars, 25 repos) as trending fallback.
Seen-list checked against `SOURCES.md` (#1–64 + rejections) and all prior log runs — the 4 qualifiers below are new to the registry.

### QUALIFIED (4) — all MIT or Apache-2.0, LICENSE file read in full via raw.githubusercontent.com (openshorts rule; carve-out keyword grep — zero hits in all four)

1. **Rieranthony/product-film-skill** — https://github.com/Rieranthony/product-film-skill — MIT (LICENSE read in full; © 2026 Rieranthony; standard MIT, no carve-outs) — ~295 stars, 21 forks — created 2026-09-26, pushed 2026-09-26 (yesterday).
   Why: agent skill that makes showreel-grade product films in code (Remotion): discovery of the product's real design tokens/components/logo → interview → `videos/BRAND.md` brand kit → story → beat-cut music → build → review → final render (240fps master, muted loop + music cut, WebM, poster). Landing-page loops, launch videos, promo/demo reels with logo animation, magic moves, punchlines. Strong client-video/studio-motion feed beside bang-motion (#43), hyperframes (#50), no-slop-motion (#67).

2. **kaankiziltug/logo-design-skill** — https://github.com/kaankiziltug/logo-design-skill — MIT (LICENSE read in full; © 2026 kaankiziltug; standard MIT, no carve-outs) — ~142 stars, 2 forks — created 2026-09-26, pushed 2026-09-27 (today).
   Why: comprehensive logo-design agent skill for Claude — principles, process, SVG craft, testing tools, 1,400+ logo reference library. Fills the general brand-logo lane for creative/design agents; ip-as-logo-skill (#30) only covers IP mascots.

3. **ferndesk/no-slop-motion** — https://github.com/ferndesk/no-slop-motion — MIT (LICENSE read in full; © 2026 Ferndesk; standard MIT, no carve-outs) — ~69 stars, 7 forks — created 2026-09-26, pushed 2026-09-26.
   Why: agent skill for launch and brand films that look directed, not AI-generated — a craft-discipline feed for the studio reels motion lane alongside bang-motion (#43), hyperframes (#50), product-film-skill (#65).

4. **Finderchangchang/brewreel** — https://github.com/Finderchangchang/brewreel — Apache-2.0 (LICENSE read in full; standard Apache-2.0, no carve-outs; repo bills itself "开源可商用" — open-source, commercially usable) — ~64 stars, 10 forks — created 2026-09-26, pushed 2026-09-27 (today); 538-file tree, real implementation (SKILL.md agent skill + prompt pipeline).
   Why: product-brief → vertical promo film in one command — AI shot selection, copywriting, 3 recipes, 6 industries, ad-law compliance check — tuned for cheap models (DeepSeek). Client-ad creative lane for studio reels; fastest brief-to-film loop found so far.

### Checked, not qualified / skipped this round

- breakstageaxe61/genspark-claw (96★ MIT) — community skill pack for OpenClaw-style agents (deep research, reports, slides, browser automation) — generic productivity, lanes covered by claude-plugins-official + genoffice + knowledge-work-plugins; skipped.
- hiroqt/PixelCrew (10★ Apache-2.0) — visual AI-agent orchestration with pixel-art dashboard — novelty UI; harness lane covered (paperclip, ruflo, deer-flow, orca, hermes-agent); skipped.
- kostja94/openblog (6★ MIT) — agent-native Git-based blog CMS module — low traction, content lane covered; skipped.
- dzhng/jevgrep (524★ MIT) — Jev-powered code-search CLI for coding agents — dev tooling, not agency operational.
- feitangyuan/onetake (489★ NOASSERTION) — excluded per policy. lemomo-ai/lemo-opuscar (314★ NOASSERTION, 39 AI-film style prompts) — popularity doesn't override policy; described, never copied.
- JoinArtisanVent/x-scraper-no-api (104★ GPL-3.0) — copyleft, excluded.
- zetaglobal/athena-skills (2★ NOASSERTION) — vendor marketing intelligence, license out of policy; skipped.
- Enixes/astra-frontend-design (3★ license null) — unlicensed, excluded; design lane covered. moreWax/dsh-prime-agent (0★ MIT) — DeepSeek-harness-specific, no traction; learning loop covered.
- langtang/ai-agent SEO entries (RouterGrowth/skills 2★ MIT, ilang-ai/agent-ready-geo 1★ MIT, etc.) — thin; SEO lane covered by open-seo (#21) + open-seo-mcp-skills (#55) + seo-landing (#62).
- Agent-framework entries: Esaadatmand/Photon_orchestrator (12★), PebbleLog/SimonAgent (10★ NOASSERTION), Monesgoda/offensive-Agent-s (8★, offensive-security framing) — thin or out of lane; skipped.
- Social-scheduler lane: search returned zero results this round; covered by cogsend (#25), shoutrrr (#22), social-stats (#01:50).
- n8n marketing workflows: all 0–1 stars, mostly unlicensed "marketing-workflows-n8n" fork spam — covered by YuriCrystal/n8n-marketing-flows (#57).
- Short-form video clipper search: laya-clipper (#46) and jevcut (#47) re-appeared (registered, no re-evaluation); rest 0–4 stars or unlicensed; lane covered.
- Vincentwei1021/video-talkcraft (1,255★ NOASSERTION — PolyForm Noncommercial reject) and QingYunA/agent-html (39★ license null — unlicensed reject) re-appearing in design-skill searches — already in rejections table, no re-evaluation.
- mcncarl/jianying-headless re-appearing — still NOASSERTION, excluded per policy.
- All already-registered repos re-appearing (ghost-editor #63, calven-ai #64, marketing-mindset/a1-marketing-skills noted before, edit-ai noted 08:50) — no re-evaluation.

### License-policy notes this round

- All 4 qualifiers had LICENSE fetched from raw.githubusercontent (main branch, HTTP 200) and read in full; grep for (agpl|gpl-3|noncommercial|polyform|elastic|proprietary|commercial license) — zero hits in all four.
- NOASSERTION exclusion struck two high-traction video entries this round (onetake 489★, lemo-opuscar 314★) — policy holds: no license file = described, never copied, no matter the stars.
- GitHub-detected MIT/Apache with a LICENSE file present, read in full, accepted (product-film-skill, logo-design-skill, no-slop-motion, brewreel).

## 2026-09-27 12:50 EDT — hourly scan

Seen-list checked against `SOURCES.md` (#1–68 + rejections) — the 6 qualifiers below are new to the registry.

### QUALIFIED (6) — all MIT or Apache-2.0, LICENSE file read in full via raw.githubusercontent.com (openshorts rule; carve-out grep clean in all six)

1. **mvschwarz/openrig** — https://github.com/mvschwarz/openrig — Apache-2.0 (LICENSE read in full; standard Apache-2.0, only "commercial damages" §8 boilerplate like tin #44, no carve-outs) — ~786 stars, 89 forks — created 2026-04-01, pushed 2026-09-27 (today), on GitHub trending daily.
   Why: multi-agent harness that runs Claude Code + Codex as one system — a dual-model control-plane pattern for the ops agent, comparing against paperclip (#7), ruflo (#51), LoomFlow (#32). First clean harness found that federates both coding agents rather than just one.

2. **minosdevs/copycat-skill** — https://github.com/minosdevs/copycat-skill — MIT (LICENSE read in full; © 2026 minosdevs; standard MIT, no carve-outs) — ~26 stars — created 2026-09-26, pushed 2026-09-26.
   Why: Claude Code skill — URL → pixel-perfect website clone via Playwright capture (3 viewports, folds, sections). Gives the webmaster agent a fast reference-rebuild lane; sits beside ui-ux-pro-max-skill (#24) and BoardUI (#42).

3. **charlie947/motion-graphics-skills** — https://github.com/charlie947/motion-graphics-skills — MIT (LICENSE read in full; © 2026 Charlie Hills, same author as integrated social-media-skills #1; standard MIT, no carve-outs) — ~9 stars — created 2026-09-26, pushed 2026-09-27.
   Why: 13 Claude Code skills for launch-grade motion graphics — every frame code, no After Effects. Feeds the studio reels motion lane alongside bang-motion (#43), hyperframes (#50), product-film-skill (#65), no-slop-motion (#67).

4. **blixvip/html-anime** — https://github.com/blixvip/html-anime — MIT (LICENSE read in full; © 2026 blixvip; standard MIT, no carve-outs) — ~7 stars — created 2026-09-27, pushed 2026-09-27.
   Why: prompt-an-anime shot-sheet harness — skills so Claude/Codex/Cursor/Grok draw animated sequences in code. Anime-style motion lane for studio reels (low traction, pattern reference).

5. **cloveric/claude-drawing-skill** — https://github.com/cloveric/claude-drawing-skill — MIT (LICENSE read in full; © 2026 cloveric; standard MIT, no carve-outs) — ~6 stars — created 2026-09-27, pushed 2026-09-27.
   Why: Claude Code skill for procedural illustration in 15 styles (ink wash, watercolor, etc.). Illustration lane for creative/design agents (low traction, pattern reference).

6. **promptadvisers/claude-codex-workflow-kit** — https://github.com/promptadvisers/claude-codex-workflow-kit — MIT (LICENSE read in full; © 2026 Prompt Advisers; standard MIT, no carve-outs) — ~5 stars — created 2026-09-26, pushed 2026-09-26.
   Why: six Claude + Codex workflows, nine prompts, public-safe prime and handoff skills. Dual-model fleet-workflow pattern for the ops agent, beside openrig (#69).

### REJECTED this round
- debpalash/VoiceStudio (~39.3k stars, trending daily, fully-local ElevenLabs alternative: voice cloning/design, video dubbing, transcription, 646 languages) — AGPL-3.0. Popularity doesn't override policy; described, never copied. Added to rejections table.

### Checked, not qualified / skipped this round
- Trending daily: paperclipai/paperclip and dream-num/univer (both registered, no re-evaluation); rohitg00/ai-engineering-from-scratch (learning resource, not a tool); InfinityLoop1308/PipePipe (Android YouTube client, out of lane); willfaust/Madeira (iOS x86 emulation, out of lane).
- feitangyuan/onetake (510★ NOASSERTION) — already rejected 11:50 run; still excluded per policy. zhuyansen/awesome-claude-video-skills (25★ NOASSERTION) and tuzhechen2005/opus-video-skills (8★ NOASSERTION) — unlicensed, excluded.
- Video-clipper search (created >2026-09-25): rest all 0–1★ NOASSERTION (Zeeshan-youtube-Ai-video, auto-shorts, SIDA-AI-, viral-text-video-generator, ClipCart-AI, Logo-Video-Generator) — unlicensed, excluded; bestaidrama/awesome-ai-video-generators (9★ NOASSERTION) — unlicensed list, excluded.
- Social-scheduler / n8n search (created >2026-09-20): only results were MIT prompt-collection "awesome" lists (minimax/seedance/grok/gemini/wan video prompts, 0–1★) — prompt lists, not schedulers or n8n packs; scheduler lane still covered by cogsend (#25), shoutrrr (#22), n8n lane by YuriCrystal (#57).
- ArefMozafari/pr-evidence (6★ MIT) — PR-change-visualization agent skill; dev tooling, not an agency lane; skipped.

### License-policy notes this round
- All 6 qualifiers' LICENSE files fetched from raw.githubusercontent (main branch, HTTP 200) and read in full; grep for (agpl|gpl-3.0|noncommercial|polyform|elastic license|proprietary|commercial license) — zero hits in all six.
- openrig's only "commercial" hit is Apache §8 "commercial damages" boilerplate — accepted per the tin (#44) precedent.
- Note: GitHub search API over urllib kept dropping connections this run; curl against the same endpoints worked reliably. Use curl for search API in future runs.

## 2026-09-27 13:50 EDT run — 6 new qualifiers (registered as SOURCES.md #75–80)

### QUALIFIED (all MIT or Apache-2.0, license files read in full)

1. **samyost1/3dicon** — https://github.com/samyost1/3dicon — MIT (LICENSE read in full; © 2026 Sam Yost; standard MIT, no carve-outs) — ~480 stars — created 2026-09-23, pushed 2026-09-23.
   Why: one-prompt looping animated 3D icon generator as a Claude Code skill, real transparency. Motion-visual lane for creative/design agents (animated logos, brand icons, social stickers).

2. **sno-ai/sno-station** — https://github.com/sno-ai/sno-station — Apache-2.0 (LICENSE read in full; only "commercial" hit is Apache §8 boilerplate, not a carve-out) — ~248 stars — created 2026-09-19, pushed 2026-09-26.
   Why: Claude Code + Codex working as one squad on own machine with shared encrypted state. Multi-agent fleet pattern for the ops agent; compare with openrig (#69).

3. **sevenevesai/riso-windowseat** — https://github.com/sevenevesai/riso-windowseat — MIT (LICENSE read in full; © 2026 sevenevesai; standard MIT, no carve-outs) — ~233 stars — created 2026-09-22, pushed 2026-09-25.
   Why: procedural risograph films in single HTML files via a Claude Code skill. Film-motion lane for studio reels alongside hyperframes (#50), bang-motion (#43), ghost-editor (#63).

4. **mariagorskikh/talking-head-reel** — https://github.com/mariagorskikh/talking-head-reel — MIT (LICENSE read in full; © 2026 mariagorskikh; standard MIT, no carve-outs) — ~56 stars — created 2026-09-22, pushed 2026-09-22.
   Why: Claude Code skill turning a messy phone recording into an edited vertical reel (best takes, captions). Raw-footage-to-reel lane for studio, fits talking-head content like the Buddy Martin Show cuts.

5. **AndyShiu/claude-skill-playwright-browser** — https://github.com/AndyShiu/claude-skill-playwright-browser — MIT (LICENSE read in full; © 2026 AndyShiu; standard MIT, no carve-outs) — ~36 stars — created 2026-09-24, pushed 2026-09-26.
   Why: background Playwright browser skill for screenshots (desktop/tablet/mobile). Visual-QA lane for the webmaster agent, beside copycat-skill (#70).

6. **adifsgaid/socialfaktory-mcp** — https://github.com/adifsgaid/socialfaktory-mcp — MIT (LICENSE read in full; © 2026 Moduslab; standard MIT, no carve-outs) — ~1 star — created 2026-09-22, pushed 2026-09-22.
   Why: social-media MCP server (brand-voice post writing, short-video generation, scheduling). MCP-driven publishing pattern for the social publishing agent (low traction, pattern reference).

### REJECTED this round
- op7418/guizang-product-video-skill (452★) — AGPL-3.0; ilien-dev/quiron (51★) — AGPL-3.0; alexrdiansyah-oss/AI-Clipper-Tools (0★) — GPL-3.0. Copyleft, excluded.
- red16124724/Aurum-Clipper (4★), kulwantdevops/clipper (0★) — NOASSERTION (no license); unlicensed, excluded.
- Barty-Bart/motion-graphics (178★), brumar/chess-postmortem-skills (57★), Dicklesworthstone/skillranker (121★) — license "other"; no verified permissive license, excluded.
- junaidshah78/social-media-automation (1★) — NOASSERTION; excluded.

### Checked, not qualified / skipped this round
- Clipper search: laya-clipper, jevcut (both registered); AI-Clipper-Tools (GPL, above).
- Scheduler search: cogsend (registered, now ~140★); lexusvp/social-media-smm-automation (0★ MIT, generic, low signal — skipped); Abhishek-B-R/social0-oss (3★ AGPL-3.0 — rejected above via license).
- n8n marketing search: only empty/spam test repos ("marketing-workflows-n8n" ×10, 0★, unlicensed) — excluded; n8n lane still covered by YuriCrystal/n8n-marketing-flows (#57).
- Agent-framework search: no strong new fit — Vibe-Coding-Production-Kit (30★ MIT, generic vibe-coding), ElasticEmail examples (out of lane), phpclaw-monorepo (11★ MIT PHP agent engine, PHP-only — skipped), haulynx8/jest-for-ai-agents (1★ MIT, testing framework — borderline dev tooling, skipped).
- Skill search: Oldcircle/geo-sleuth (474★ MIT, photo geolocation — out of agency lane); majidmanzarpour/blender-game-skills (93★ MIT, game dev — out of lane); UditAkhourii/quicksilver (70★ MIT, bulk-judgment token saver — overlaps hermes-jev-skills #40, skipped); nahid-sparktales/agent-dispatcher (52★ MIT, repo retrieval context engine — generic dev tooling, skipped); leepokai/jev-guard (41★ MIT, tool-call risk scoring — overlaps #40 governance lane, skipped); yanauto/opus-manager (40★ MIT, delegate-to-cheaper-CLIs — overlaps #40 efficiency lane, skipped); kishormorol/cli-faq-shortcuts (106★ Apache-2.0, CLI aliases — dev convenience, skipped).

### License-policy notes this round
- All 6 qualifiers' LICENSE files fetched from raw.githubusercontent (main branch, HTTP 200) and read in full; grepped for commercial carve-out language — zero hits. sno-station's Apache-2.0 "commercial" hit is §8 boilerplate, accepted per the tin (#44) precedent.
- github.com/trending page is JS-rendered and yields no repo entries via browser.open; used curl against api.github.com search endpoints instead (works reliably with --max-time).

## 2026-09-27 14:50 EDT — hourly scan

Sources checked: GitHub search API across 13 lanes (agent skills marketing, ai agent framework orchestration, social media scheduler selfhosted, short video clipper ai, n8n workflow marketing, video caption tool agent, design system agent skill, agent learning loop memory, seo agent skill, ai video editor agent skill, social media publish mcp, whatsapp telegram posting agent — created >2026-08-27, sorted by stars, ~330 repos) + new-repo sweep (created >2026-09-25, >30 stars, 30 repos) as trending fallback.
Seen-list checked against `SOURCES.md` (#1–80 + rejections) and all prior log runs — the 2 qualifiers below are new to the registry (registered as #81–82).

### QUALIFIED (2) — MIT/Apache-2.0, LICENSE file read in full via raw.githubusercontent.com (openshorts rule; carve-out grep — zero hits in both)

1. **ZJU-REAL/Easel** — https://github.com/ZJU-REAL/Easel — Apache-2.0 (LICENSE read in full; standard Apache-2.0, carve-out keyword grep zero hits) — ~1,794 stars, 261 forks — created 2026-08-28, pushed 2026-09-24; Zhejiang/Peking REAL lab.
   Why: OpenClaw-powered social-media content workbench — one agent runs the full chain: discover (trend radar across hot lists), plan (topics, hooks, scripts, content calendar), create (copy, cards, posters, audio, video, captions, long→short slicing), publish (pre-flight checks, multi-platform adaptation, 7 China platforms: Xiaohongshu/Douyin/Kuaishou/Zhihu/Bilibili/WeChat Channels/WeChat official accounts), attribute (playback/interaction/comment analytics fed back into account personas). 113 runnable skills, account-profile memory, projectized outputs. Maps onto the agency's social-publishing + analytics/learning-loop lanes; the 113-skill library is pattern fuel for the skills-library. Caveat: publisher is China-platform-only — patterns transfer, not a drop-in for US brands.

2. **alphaparkinc/genpark-autonomous-marketing-campaign-optimizer-skill** — https://github.com/alphaparkinc/genpark-autonomous-marketing-campaign-optimizer-skill — MIT (LICENSE read in full; © 2026 GenPark AI; standard MIT, no carve-outs) — ~7 stars, 0 forks — created+pushed 2026-09-18 (single commit, ~10 days quiet).
   Why: agent skill — autonomous cross-channel marketing campaign optimizer, closed-loop ad rebalancing, generative creative orchestration. On-lane for the agency's learning-loop + creative-ops lanes; low traction and single-commit, so treat as pattern reference and verify before any core use.

### REJECTED this round
- JoinArtisanVent/x-scraper-no-api (114★) — GPL-3.0; Farayzin/FlowCut (0★) — GPL-3.0; hacktheseo/wordpress-seo-skills (2★) — GPL-2.0. Copyleft, excluded.
- Abhishek-B-R/social0-oss (3★) — AGPL-3.0 = excluded. alexrdiansyah-oss/AI-Clipper-Tools (0★) — GPL-3.0 = excluded.
- feitangyuan/onetake (518★), lemomo-ai/lemo-opuscar (333★), xikhar/spiderbench (185★), DanFessler/trellis (115★), yihui-dev/awesome-opus5-5-videos (263★) — NOASSERTION/"other"/null license; popularity doesn't override policy, excluded.
- No new rejections added to SOURCES.md (x-scraper GPL-3.0 follows established copyleft rule; NOASSERTION entries follow policy).

### Checked, not qualified / skipped this round
- axelfreeman/marketing-mindset (33★ MIT) — already noted 02:50 run, still marginal/niche.
- zaferayan/app-store-screenshot-skill (29★ MIT) — app-store-screenshot niche, lane covered by store-screenshots noted 02:50.
- jahidulislamseo/antigravity-ai-skills (4★ MIT, 127 local-SEO skills) — thin; SEO lane covered by open-seo (#21) + open-seo-mcp-skills (#55).
- matt-j-penny/ai-video-marketing (2★ MIT, pushed today) — thin; video lane saturated.
- jayeshmahawer/n8n-ai-automation-templates (0★ MIT, "49 curated n8n workflows for AI marketing agents") — 0 stars; n8n lane covered by YuriCrystal (#57); Mfrostbutter (18★) already skipped 07:50 as too thin.
- reactvideoeditor/react-video-editor-agent-skills (1★ MIT) — thin vendor SDK; video lane covered.
- SYasJ/claude-practice-skills (1★ MIT, 587+ skills, created today) — too thin; skill-sourcing lane covered by claude-plugins-official (#56).
- feimacode/open-design-agent-kit (1★ MIT, pushed today) — thin; design lane saturated.
- graygnatconsole/mcp-audit-tool (104★ MIT) — MCP security audit; not agency operational.
- AgentSystemLabs/agent-office (95★ MIT) — novelty 3D office visualization for Claude workers; harness lane covered.
- yihui-dev/awesome-opus5-5-videos (263★, no license) — curated prompt list; excluded per policy anyway.
- Shayanthn/skills (1★ MIT, 74 marketing/SEO/GEO skills), automateswithuday/GTM-Skills (1★ MIT), matt-j-penny, agentik-os/claude-code-skills (1★), 808enzo/chappie (2★), folson-marketing-skills (5★), retrogtx/ai-marketing-videos (4★), Hiberius/competitor-ad-intelligence (1★), AY-kkk/ad-gtm (1★), growthinsiderpl (1★) — thin marketing-skill entries; lanes covered by knowledge-work-plugins (#23:50) + social-media-skills/skills (#01:50).
- Agent-framework lane: Esaadatmand/Photon_orchestrator (12★), PebbleLog/SimonAgent (10★ NOASSERTION), hiroqt/PixelCrew (10★), Epsirom/braid (3★) — all noted before; harness lane well covered (paperclip, ruflo, deer-flow, orca, hermes-agent, openrig, sno-station).
- Clipper lane: red16124724/Aurum-Clipper (4★, no license — excluded); laya-clipper (#46) and jevcut (#47) re-appeared (registered, no re-evaluation); rest 0★/unlicensed — lane saturated with clean-MIT options.
- Caption/video-tool lane: deonmenezes/edit-ai (2★ MIT, noted 08:50), fancyism/hyperremoedit-toolkit (0★ MIT — 7-skill vertical-video pipeline, 0 stars, skip), thenavidm/vimeo-mcp-cli (0★ MIT, Vimeo MCP — niche).
- Social-scheduler/Publish-MCP lane: cogsend (#25), shoutrrr (#22), socialfaktory-mcp (#80) registered; postzen plugins + publora (0★, vendor plugins) thin.
- n8n marketing workflows: affiliate-marketing-automation (1★, unlicensed), mihailprobots-ai (0★), abandoned-cart-recovery-n8n (1★ MIT), growth-marketing-automations (0★), Elie-Ander/n8n-workflows (0★, French GEO/leads templates, unlicensed) — thin; covered by YuriCrystal (#57). "marketing-workflows-n8n" fork-spam cluster (10×, all 0★, unlicensed) still excluded.
- Learning-loop search: only 0–1★ educational entries — covered by hermes-agent + hindsight + reef.
- Design-skill lane: avestura/boxy-design-skill (1★), chrisjohnleah/govuk-design-system-skill (1★), fracazo/design-system (1★), equinor/skills (2★), Woffluon/system-design-compass (3★) — thin/niche; lane saturated.
- QingYunA/agent-html (39★ license null — reject) and mcncarl/jianying-headless (2,807★ NOASSERTION) still excluded per policy.
- All already-registered repos re-appearing (product-film-skill #65, logo-design-skill #66, no-slop-motion #67, brewreel #68, ghost-editor #63, calven-ai #64, robertogx/breakstage #65-ish genspark-claw noted 11:50) — no re-evaluation.

### License-policy notes this round
- Both qualifiers had LICENSE files fetched from raw.githubusercontent (main branch, HTTP 200) and read in full; carve-out keyword grep (agpl|gpl|noncommercial|polyform|elastic|proprietary|commercial license|all rights reserved) — zero hits in both.
- Easel's platform limitation (China-only publishers) is a fit note, not a license issue; worth flagging for the integration pass.
