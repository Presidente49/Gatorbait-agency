<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Infographic Builder

**Owner:** blueprint (creative/design)

Turn source content into a single hand-drawn whiteboard infographic via an AI image generation prompt.

## Trigger

Requests like "whiteboard infographic", "hand-drawn graphic", "turn this into a whiteboard", or an AI-generated infographic for a social post.

## Step 1. Get the source content

Ask for the content: a post, newsletter section, blog, research note, or raw bullet points all work.

## Step 2. Build the brief

Produce a brief in plain language:

- **Title**: 6 words or fewer, punchy
- **Subtitle**: optional, one line of context
- **Core structure**: steps, framework, comparison, stats, or list
- **Key points**: 3 to 7 short bullets. Preserve every required item and qualification; if they will not fit legibly, propose a split rather than silently dropping content.
- **Visual suggestions**: arrows, boxes, highlighted numbers, icons, colour accents. Specific about placement and colour.
- **Footer CTA**: only from confirmed brand context (name + tagline from the brand folder). Omit unknown fields.

Present the brief and wait for approval: "Here is the brief. Tell me what to change, or say 'generate' when you're happy."

## Step 3. Output the image prompt

Once approved, output the full prompt in a code block:

```
Generate a single image of a physical, hand-drawn infographic on a large whiteboard or notebook page.

Crucial Style Instructions (Read First):

Medium: The image must look like a photograph of a real whiteboard or large paper notepad.

Texture: All elements must look created by hand using colored marker pens (black, blue, red, green) and highlighters (yellow/orange). Lines should be slightly imperfect, wobbly, and have the texture of ink on a surface.

No Digital Fonts: All text, headings, and bullet points must appear handwritten or hand-printed in marker pen.

Layout: Structure the 1080x1350 image as follows:

[INSERT THE BRIEF HERE — title, subtitle, core structure, key points, visual suggestions]

Use multi-colored markers for emphasis. Keep text large and legible. Make everything look hand-drawn with slight imperfections. Make it look like a photograph of an actual notebook page.

If approved in the brief, include the handwritten footer "[verified name and approved CTA]" at the bottom of the image, in the same hand-drawn marker style.
```

## Step 4. Inspect and iterate

When the image is generated, inspect it at full size and feed size (~360px wide). Check copy accuracy, legibility, and layout. If it misses, ask what to adjust and rewrite the prompt. Common fixes: fewer colours, bigger title, different layout direction. A prompt is not a finished asset until the export is visually verified.

## Rules

- 1080x1350 output. Vertical format.
- Bullets under 10 words without losing meaning. Readability and accurate coverage both pass.
- Always wait for brief approval before outputting the final prompt.
- If the brand has brand colours in `brand-style.md`, bake them into the visual suggestions.
