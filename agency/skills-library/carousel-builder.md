<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Carousel Builder

**Owner:** blueprint (creative/design)

Turn source content into a slide-by-slide carousel brief, get approval, then output per-slide AI image generation prompts. 1080x1350 vertical format (4:5), works for Instagram, Facebook, and LinkedIn carousels.

## Trigger

Requests like "carousel", "build a carousel", "turn this into a carousel", or multi-slide social content for the active brand.

## Step 1. Gather inputs

Ask for the source content: a post, newsletter section, research notes, or a framework all work.

Then gather:
- **Brand style**: pull from the active brand's `brand-style.md` first. If it lacks colours/typography, ask for hex codes and font preferences, or offer to suggest a palette based on the content.
- **Slide count**: 6 (concise), 8 (standard), or 10 (deep dive).

## Step 2. Build the design brief

Slide-by-slide brief:

- **Slide 1 (Cover)**: hook, large bold text, visual direction
- **Slides 2 to N-1 (Body)**: one idea per slide. Concise copy plus a specific illustration or diagram that explains it. Preserve every required item and qualification; propose more slides rather than cutting content.
- **Slide N (Ending)**: useful conclusion or next action, with a CTA only for a real approved offer or link

For each slide include: slide number, headline (max 8 words), body (max 15 words), visual suggestion (icon, colour block, illustration, diagram).

Present the brief and wait for approval: "Here is the design brief. Tell me what to change, or say 'generate' when you are happy." Do not proceed until approved.

## Step 3. Output per-slide prompts

Once approved, output one image generation prompt per slide, each in its own code block, numbered clearly. Template:

```
Act as an expert graphic designer. Create a carousel slide at 1080x1350 pixels (4:5 aspect ratio).

Brand style:
- Primary colour: [HEX]
- Secondary colour: [HEX]
- Accent colour: [HEX]
- Typography: [headline font, body font]
- Aesthetic: [from brand-style.md]

Slide [N of M]: [slide purpose]

Content:
- Headline: "[headline text]"
- Body: "[body text]"
- Visual element: [specific visual suggestion]

Layout instructions:
- [Headline placement and size]
- [Body placement and size]
- [Visual placement]
- [Background treatment]

Constraints:
- Vertical 4:5 aspect ratio at exactly 1080x1350 pixels
- No watermarks, no logos unless specified
- Maintain visual consistency with the other slides in the set
```

Then offer: "Want a single combined prompt that generates the full carousel in one shot? Faster but less visual consistency. Say 'combine' and I will rewrite."

## Step 4. Inspect before shipping

When images are generated, inspect each export at full size and at feed size (~360px wide). Check exact copy, dimensions, clipping, legibility, brand colours, and font appearance. Fix and re-inspect failed exports. A prompt is not a finished asset; never claim a carousel is done until the exports are visually verified.

## Rules

- Always gate on brief approval before outputting image prompts.
- 1080x1350 per slide. No other aspect ratio.
- Keep brand style identical across every slide prompt so the set looks like one carousel.
- Cover (1) and CTA (last) slides must be visually distinct from body slides.
- Never remove a required fact to hit a word target. Split the content during briefing instead.
