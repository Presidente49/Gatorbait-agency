# White-Label Guide — run this agency for ANY business

This agency is brand-agnostic. The agents, playbooks, protocols, and
learnings in `agency/shared/` work for any business. Everything
brand-specific lives in `agency/brands/<slug>/`. To onboard a new
business takes about 15 minutes.

## How it works

```
agency/
├── agents/          # 8 agents — brand-agnostic, read the active brand at startup
├── shared/          # playbook, protocols, learnings — apply to every brand
│   ├── playbook.md      # Meta (Facebook/Instagram) content playbook
│   ├── protocols.md     # operating protocols
│   ├── learnings.md     # earned principles, transferable across brands
│   ├── roster.md        # agent roster
│   └── campaign-board.md
├── skills-library/  # 17 agent skills (SKILLS-INDEX.md maps skills → agents)
├── studio/          # the production company: clipping, captions, reels,
│                    # creative engine, livestream — see STUDIO.md
├── cloud/           # 24/7 layer: n8n automation + scheduler dashboard
│                    # — see CLOUD.md
└── brands/
    ├── ACTIVE               # one line: the active brand slug
    ├── _template/           # blank templates — copy to start a new brand
    ├── gator-bait-media/    # example: fully filled-in brand
    └── <your-brand>/        # your business goes here
```

**Every agent's first step:** read `agency/brands/ACTIVE`, then read
every file in that brand's folder. The agent speaks in that brand's
voice, follows its style, pursues its goals, and appends new learnings
to that brand's `learnings.md`.

## Onboard a new business

**Option A — script:**
```bash
./new-brand.sh <business-slug>
# then fill in the files in agency/brands/<business-slug>/
```

**Option B — manual:**
```bash
cp -r agency/brands/_template agency/brands/<business-slug>
echo "<business-slug>" > agency/brands/ACTIVE
```

Then fill in: `brand-voice.md`, `brand-style.md`, `goals.md`,
`audience.md`, `offers.md`. Leave `learnings.md` empty — the agency
starts writing there on day one.

## Switching brands

```bash
echo "<business-slug>" > agency/brands/ACTIVE
```

Agents pick up the new brand on their next run. Nothing else changes.
One agency, unlimited businesses — just don't run two brands'
campaigns in the same session without switching ACTIVE first.

## What travels with the white label

- **The 8 agents** — Scout, Scribe, Hype, Blueprint, Rank, Bridge,
  Webmaster, Wrench. Narrow workers; the operator's judgment directs them.
- **The skills library** — 17 drop-in agent skills (hooks, carousels,
  analytics, voice, thumbnails…), each mapped to its owning agent.
- **The studio** — the production company: caption pipeline, reel
  renderer, deterministic creative engine, livestream operations.
- **The cloud layer** — 24/7 n8n automation (starter workflows included)
  and the self-hosted scheduler/client dashboard option.
- **The Meta playbook** — researched Facebook/Instagram best practices.
- **The shared learnings** — every earned principle from every brand
  the agency has ever run. This is the compounding asset.
- **The protocols** — QC loops, logging, evidence rules, A/B testing
  methodology.

## What does NOT travel

- Brand voice, style, goals, audience, offers — those are per-brand.
- Credentials, logins, API keys — never in the repo. Ever.
- Any single brand's private data — audience lists, revenue figures
  beyond what's needed, personal information.

## Starting a session (for Claude / the operator)

```
1. Read agency/brands/ACTIVE → the brand slug.
2. Read every .md file in agency/brands/<slug>/.
3. Read agency/shared/playbook.md, protocols.md, learnings.md, roster.md.
4. Read the identity.md + tasks.md of whichever agents you're deploying.
5. Work. Log to the brand's log. Append learnings to the brand's learnings.md.
```
