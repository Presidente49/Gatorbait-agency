# Trending Repo Watch — log (append-only)

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
