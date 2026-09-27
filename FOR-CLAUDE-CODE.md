# FOR CLAUDE CODE — operator's manual & standing orders from Brenden

Brenden's orders: **you run the machinery; Marlowe calls the plays.**
This repo is the Gator Bait Agency — a white-label, 8-agent marketing
agency any business can clone. Your job: keep it sharp, keep it honest,
and never stop making it better.

## The stack as it stands (2026-09-27)

**Management — Paperclip control plane** (`agency/cloud/paperclip/`)
The agency's runtime: org chart, task queue, budgets, heartbeats,
governance. Marlowe = CEO/controller, the 8 agents = direct reports.
One Paperclip "company" per white-label brand. Budgets are set BEFORE
the first heartbeat. Start with Gator Bait Media, prove the loop, then
clone per brand. Concepts only — Paperclip itself runs as separate
infrastructure, not vendored here.

**The 8 agents** (`agency/agents/`)
scout (research), scribe (writing), hype (social publishing),
blueprint (creative/design), rank (SEO), bridge (outreach),
webmaster (website), wrench (ops/automation). Each has an identity.md
with role, duties, startup steps.

**Growth department** (`agency/growth/`) — the money brain
CRO-PLAYBOOK, COPY-PATTERNS, OFFER-DESIGN, EXPERIMENT-RUNBOOK,
ANALYTICS-LOOP, LOOP-SPEC. Every brand doesn't just publish — it
runs experiments, measures revenue attribution, and compounds wins.
If a change doesn't move a money metric, it's decoration.

**Merch layer** (`agency/merch/`)
MERCH-PLAYBOOK, PRINT-ON-DEMAND, STOREFRONT-OPTIONS. Any brand can
spin up a merch store. Rule: never use a coach/player likeness to sell
merch — Brenden's law.

**Studio** (`agency/studio/`) — the production company
clipping → captions → reels → publish. Runbooks an agent can follow
step by step. Note: no automated long-video-to-shorts clipping engine
is integrated yet (the open-source options had commercial carve-outs).
This gap is documented at `agency/studio/clipping/NOT-INTEGRATED.md`
— keep hunting for a clean permissively-licensed one.

**Skills library** (`agency/skills-library/`)
Reusable markdown skills any agent can read and execute. Includes 4
marketing skills: brand-first, quality-gate, revenue-attribution,
youtube-outliers. Registered in SKILLS-INDEX.md.

**Memory** (`agency/cloud/hindsight/`)
Agent memory that learns — the agency remembers what worked.

**Comms & runtime** (`agency/cloud/buzz/`, `agency/cloud/univer/`,
`agency/cloud/mobile-mcp/`, `agency/cloud/claude-code-action/`)
Team communication patterns, agent office runtime, mobile automation,
CI patterns for Claude Code through GitHub Actions.

**Web & Wix** (`agency/studio/web/WEB-DESIGN-TRENDS.md`,
`agency/cloud/wix/`)
Design trends + Wix design system + Velo patterns. Brenden's flagship
brand runs on Wix — the agency must be dangerous there.

**Cloud** (`agency/cloud/n8n/`)
n8n + Postgres + Caddy + scheduler. Three starter workflows: RSS to
social drafts, comment monitor, weekly analytics digest.

**White-label system** (`agency/brands/`, `new-brand.sh`)
`new-brand.sh` + `_template/` onboards a business in ~15 minutes.
Every brand gets its own `learnings.md`.

**The loop** (`agency/shared/learnings.md`, `agency/docs/SOURCES.md`)
Every workflow appends lessons to the brand's learnings.md and, when
transferable, to shared/learnings.md — so every future brand inherits
every past win. SOURCES.md registers every borrowed idea with repo,
URL, license. 30 sources and counting.

## How it all works together

1. Paperclip assigns tasks; agents execute from their identity.md +
   the skills library.
2. Studio produces content; growth measures it against money metrics.
3. Winners go into learnings.md; learnings compound across brands.
4. The hourly trending-repo watch finds new fuel; you evaluate, test,
   and integrate what earns its place.

## What to review (this week)

1. **Structure** — does `agency/` hang together? What's missing or
   redundant?
2. **White-label completeness** — mentally onboard a non-sports
   business (e.g., a pizza shop) via `new-brand.sh` + `_template/`.
   Fix gaps.
3. **Agent identities** — are the 8 roles sharp, duties executable,
   startup steps real?
4. **Skills usability** — can an AI agent actually execute each skill
   from the markdown alone? Cut or fix anything vague.
5. **Studio pipelines** — are the runbooks truly step-by-step?
   Flag missing tooling or impossible steps.
6. **Cloud correctness** — docker-compose, workflow JSON validity,
   secrets handling (nothing hardcoded — ever).
7. **Growth rigor** — do the experiments have real control groups and
   kill criteria? Is revenue attribution honest?
8. **Learnings loop** — does every workflow feed learnings.md?
9. **Attribution & licenses** — every borrowed file: repo name, URL,
   license. Permissive licenses only (MIT, Apache-2.0, BSD, ISC). NOTHING GPL/AGPL/unlicensed/
   commercially carved-out gets copied in — ever. Rejections live in
   `NOT-INTEGRATED.md` files; respect them.

## The never-ending job: hunt, test, integrate

This is standing orders, not a one-time task:

- **Hunt.** There's an hourly `trending-repo-watch` job scanning
  GitHub Trending for agent frameworks, social schedulers,
  short-form-video systems, caption tools, n8n workflows, design
  systems, analytics, merch tooling, and web-design trends. Treat its
  findings as your inbox. You can also hunt yourself — trending pages,
  awesome-lists, Product Hunt, wherever the sharp stuff surfaces.
- **Vet.** Read the full LICENSE first, every time. MIT or
  Apache-2.0 only. Reject GPL, AGPL, unlicensed, ambiguous, or
  commercially carved-out code — write a `NOT-INTEGRATED.md`
  explaining why.
- **Test.** Don't integrate on stars alone. Test in a scratch brand
  directory first: does it actually do what it claims? Does it fit
  the 8-agent model? Does it move a money metric or save real time?
  If it fails the test, it doesn't ship — note why in learnings.
- **Integrate.** Concepts and runbooks, not whole applications.
  Attribution header on every borrowed file (repo, URL, license).
  Register it in `agency/docs/SOURCES.md`. Append transferable
  lessons to `agency/shared/learnings.md`.
- **Priority hunting grounds** (Brenden's words: "so much awesome
  stuff out there right now"): AI-integrated website design, cooler
  Wix/Velo patterns, merch/e-commerce tooling, the missing
  long-video-to-shorts clipping engine, and anything that makes the
  growth department smarter about revenue.

## How to report

Write findings to `REVIEW.md` at repo root: what's solid, what's
broken, what you fixed, what needs a human decision. Fix what you
can; flag what you can't. Then keep hunting.
