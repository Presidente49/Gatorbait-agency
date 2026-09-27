<!-- Source: cganh/openpage (https://github.com/cganh/openpage) — MIT License. Adapted for Gator Bait Agency. -->

# Web Design Trends — what the agency is stealing from 2026

Scanned September 2026: GitHub trending plus targeted hunts for
AI-generated sites, AI-integrated design tools, and modern design
systems. Most of trending is agent infrastructure right now —
below is what actually strengthens the agency's web work.

## The one pattern that matters: JSON-first site documents

From **OpenPage** (MIT, © 2026 Federico De Ponte) — an open-source
site builder whose whole thesis fits the agency's agent-driven model:

> A website is a single typed JSON document: `{ name, theme, blocks[] }`.
> The visual editor reads and writes it, the AI endpoint generates it,
> the renderer turns it into a page. Every mutation — human drag or
> agent API call — produces the same structured, diffable output.

Why this beats both incumbents for an agency:
- **vs code generators** (Lovable, v0, Bolt): no hallucinated imports,
  no broken builds, no unmergeable diffs. Agents output JSON, not code.
- **vs visual editors** (Framer, Webflow): the format is portable and
  agent-readable, not a proprietary black box.

### The block schema (worth copying)

- **Block = `{ id, type, variant, props }`.** ~19 types cover the real
  web: `navbar`, `hero` (centered/split/gradient/minimal), `features`
  (grid/list/alternating), `pricing`, `cta`, `testimonials`,
  `stats`, `faq` (accordion), `team`, `contact`, `newsletter`,
  `logocloud`, `content` (markdown), `image`, `video` (youtube/vimeo),
  `gallery`, `divider`, `banner`, `footer`.
- **Theme = flat tokens:** `bg0`, `text0`, `accent`, `fontSans`,
  `fontDisplay`, `radius` — plus full customization of colors,
  fonts, spacing. Maps 1:1 onto a brand pack.
- **Export = standalone HTML, zero runtime deps.** A generated site
  is a shippable artifact, not a hosted dependency.

### Agency application

This is the blueprint for how the agency's Blueprint (creative) and
Webmaster agents should generate sites going forward:

1. **Generate the JSON, not the code.** Prompts produce a validated
   block document; the renderer is deterministic. Review = diffing
   JSON, which agents do reliably.
2. **Brand pack → theme tokens.** A new brand's site starts by
   translating its pack into the theme object; every block inherits.
3. **AI generation endpoint as a service.** The `POST /api/generate`
   pattern (prompt in, full site JSON out) is how the agency can offer
   "instant brand microsites" — landing pages for merch drops, event
   pages, sponsor pages — without a designer in the loop.
4. **Version everything.** JSON diffs in git give the agency
   rollback and review for generated sites, the same discipline as
   the Velo-in-git pattern (`agency/cloud/wix/VELO-PATTERNS.md`).

## What's hot but not (yet) agency-grade

- **AI site generators are everywhere** (dozens of new repos/month)
  but most are demo-quality or proprietary-API-locked. OpenPage
  stands out because it's MIT, self-hostable, and the JSON-first
  architecture is the actual innovation — the rest are wrappers.
- **Agent skill packaging** dominates trending (ECC, skills repos).
  Relevant to the agency's skills-library direction, not to web
  design per se — noted, not integrated here.
- **Component libraries** (shadcn-style, animated component kits)
  keep churning but add nothing the agency's template-family system
  doesn't already cover. Skipped deliberately.

## Bottom line

The durable trend is **agent-editable design formats**: JSON documents
that humans, editors, and agents all read and write. The agency's web
output — Wix sites, merch storefronts, brand microsites — should all
move toward structured, diffable, token-driven formats. OpenPage is
the reference implementation to study before building the agency's
own.
