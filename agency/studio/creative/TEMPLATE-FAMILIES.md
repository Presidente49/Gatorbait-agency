<!-- Source: cgallic/visual-factory-kit (https://github.com/cgallic/visual-factory-kit) — MIT. Adapted for Gator Bait Agency. -->

# Template Families

## The concept

A **template family** is **one layout system rendered at every platform size**.

It is not one graphic. It is not one aspect ratio. It is a layout grammar —
grid, typography scale, brand signature placement, proof-block treatment, motion
of the eye — that holds together whether it comes out as a 1:1 feed square, a
4:5 portrait, a 9:16 story, or a 16:9 thumbnail. The same message rendered
through the same family on ten platforms still reads as one campaign.

**Family = layout system × every platform size.**

## Why families, not templates

Single templates rot. A "YouTube thumbnail" one-off drifts from the "Instagram
story" one-off until the client's feed looks like ten different brands. Families
fix the production-consistency problem the engine was built for: approve one
layout grammar per brand, then every surface is a variant of it, automatically.

## Anatomy of a family definition

A family definition has five parts:

1. **Purpose and voice.** What this layout is *for* in one line
   (e.g. "game-day score recap", "coach quote pull", "offer stack"). One family
   = one job; don't make a family do three jobs.
2. **Layout grammar.** The fixed rules: grid zones (header / hero / proof /
   CTA), type scale ratios, the brand-signature placement (logo or wordmark,
   always small, never competing), spacing rhythm. These rules are what make a
   1:1 and a 9:16 still feel like siblings.
3. **Content slots.** The named fields the family consumes from the request JSON
   — the shared message block (`headline`, `subhead`, `proof_label`, `cta`) plus
   an optional family-specific `template_data` object (e.g. `messages`,
   `metrics`, `events`, `nodes`). Shared fields stay shared: existing requests
   must keep rendering without migration.
4. **Platform size map.** Which family variant covers each platform surface:
   e.g. family `gator-recap` → `facebook_feed_square`, `instagram_reel`,
   `youtube_thumbnail`, `x_post_landscape`, `story_cover`. Sizes live in the
   platform-size matrix; the family points at sizes, it doesn't redefine them.
5. **Variant behavior.** How the family adapts when a surface is smaller or
   taller: what truncates, what drops (CTA on stories?), what gets
   shrink-to-fit. Text blocks are measured in-browser and shrink-to-fit before
   render; the family's job is to say *which* blocks and the minimum acceptable
   sizes.

## Two family archetypes (from the source kit)

**Campaign-card families.** Brand-forward campaign graphics: headline + proof +
CTA on the brand's token colors. These are the workhorse — launch announcements,
weekly post batches, ad variants, article heroes, OG cards. One request renders
the full platform matrix.

**Social-native families.** Interface- or editorial-inspired metaphors — a notes
sheet for a founder insight, a message thread for objection handling, a receipt
audit for cost-of-inaction, a metrics scorecard for proof, a whiteboard for a
framework explainer, a launch calendar for events, a before/after for
transformations, a testimonial pull quote for approved social proof. These vary
texture and hierarchy across the feed while keeping one small brand signature
and mobile legibility. They are illustrative abstractions, not mockups of live
accounts.

**Privacy guardrail (non-negotiable):** interface-inspired families (message
threads, inboxes, receipts, reviews, maps, documents) must use fictional or
approved client content only. Never use the factory to imply access to a real
person's private account, device, messages, transactions, reviews, or location
data.

## Carousel families

Carousels are a family of their own: a 12-role slide system built around
**hook → substance → action** — cover hook, pattern interrupt, problem, mistake,
framework, step, checklist, proof, before/after, myth/truth, quote, CTA. One
idea per slide, recurring grid and typography, slide numbering, a specific
closing action. The cover makes a 4–9-word promise; the deck keeps it.

## Defining a new family for a client brand

1. **Name it after the job.** `slug-job` — e.g. `gator-gameday-recap`,
   `gator-quote-card`, `gator-stat-card`. The family name becomes part of
   provenance.
2. **Sketch the grammar on paper first.** Zones, type scale, brand mark
   position, proof treatment. A family is a design decision, not a config file.
3. **Pick the platform map.** List the exact format keys the family must ship
   (from the platform-size matrix). Start with the brand's top 3–5 surfaces;
   add aspect-ratio variants only after performance data says which ones earn.
4. **Define the content slots.** Reuse the shared message block; add a
   `template_data` schema only for family-specific copy. Document defaults for
   optional fields so old requests still render.
5. **Lock the variant behavior.** Which text blocks shrink-to-fit, minimum
   sizes, what drops at small widths. If the headline can't fit at minimum size,
   the answer is shorter copy — not a new layout.
6. **Render the full family once.** One request, every mapped size. Run the QA
   gate (see `QA-PROVENANCE.md`). Only promote the family to the brand's
   `allowed_templates` list after every size passes.
7. **Version it.** Families are versioned (`gator-gameday-recap@v1`). Provenance
   records the template version; when the grammar changes, bump the version and
   keep the old one renderable for legacy assets — never silently mutate.

## Reference

- `README.md` — what the creative engine is
- `BRAND-PACK.md` — how the active brand folder feeds the render pack
- `QA-PROVENANCE.md` — QA and provenance pattern
- Source: [visual-factory-kit](https://github.com/cgallic/visual-factory-kit) — MIT
