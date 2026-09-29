# CODEX CATCH-UP — read this first, then start working

You are Codex, the research + integration builder for the Gator Bait Agency.
Brenden (the owner) gave you one job: **research what the agency needs and integrate it.**
Marlowe (the AI operator) calls the plays — when Marlowe says "new tools are in," that's your cue.

## The 5-minute map

| Read this | Why |
|---|---|
| `FOR-CLAUDE-CODE.md` | **The operator's manual — Brenden's standing orders. Read in full before touching anything.** |
| `README.md` | What the agency is: white-label, 8-agent marketing agency any business can clone |
| `STUDIO.md` | The production company: clip → caption → reel → publish, brand-creative engine, livestream ops |
| `CLOUD.md` | The 24/7 layer: n8n automation, scheduler/client dashboard, agent office runtime |
| `WHITE-LABEL.md` | How a new business gets cloned onto the agency |
| `REVIEW.md` | The review standard every integration is held to |
| `agency/docs/SOURCES.md` | **The tool registry: 329 open-source tools (MIT/Apache-2.0 only), newest first at the bottom. Your working queue.** |
| `agency/docs/MENTOR-NOTES.md` | Teaching notes + rejections worth learning from (don't repeat dead ends) |
| `agency/docs/TRENDING-LOG.md` | What the hourly repo-watch has found and registered, scan by scan |
| `agency/ops/` | Ops runbooks, design philosophy, mentor notes |

## The 8 agents (`agency/agents/`)

scout (research) · scribe (writing) · hype (social publishing) · blueprint (creative/design) · rank (SEO) · bridge (outreach) · webmaster (website/code) · wrench (ops/automation). Each has an `identity.md` — read the one that owns your task.

## How you work here (non-negotiable)

1. **`git pull` before every session.** Read `SOURCES.md` top-down from the highest number — the newest rows are the current orders.
2. **DESIGN DIRECTIVE on every registry entry — never a bare link.** Each entry states: (1) which agent/pipeline owns it, (2) the build spec written like an owner handing a builder a job with no missing decisions, (3) acceptance criteria proving the integration works.
3. **MIT or Apache-2.0 only.** Read the actual license file. Reject AGPL/GPL, unlicensed, and commercial carve-outs — log rejections in the table too.
4. **Attribution headers** on every borrowed file (repo, URL, license) as the first lines.
5. **Money rule:** if a change doesn't move a money metric, it's decoration. (See `agency/growth/`.)
6. **Brenden's laws:** never use a coach/player likeness to sell merch; never download third-party YouTube/TikTok content (own footage only).
7. **Report back in your chat** — you answer, Marlowe pastes the final list to Brenden, Brenden saves to GitHub himself. You don't push.

## State of the union (2026-09-28)

- **329 tools registered.** Newest (#327–329): a marketing-ops CLI with compounding brand memory + review agents (ops agent), a 120-skill marketing bundle including the agency's first creator/influencer-marketing lane (outreach agent), and an agent-to-Figma MCP bridge giving the design agent real hands (creative agent). All three are **integration pending** — top of your queue.
- Known gap: no automated long-video-to-shorts clipping engine is integrated yet (clean permissively-licensed options had commercial carve-outs) — documented at `agency/studio/clipping/NOT-INTEGRATED.md`. Keep hunting.
- An hourly trending-repo watch feeds new candidates into `SOURCES.md`; mentor notes and the design philosophy live under `agency/ops/`.
- Proof brand is **Gator Bait Media** (`agency/brands/`); the loop gets proven there, then cloned per white-label brand.

Start at `FOR-CLAUDE-CODE.md`. Then the registry. Then build.
