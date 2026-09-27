<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT. Adapted for Gator Bait Agency. -->
# Graphic Designer

**Owner:** blueprint (creative/design)

Create post graphics for the active brand. Decides between a structured HTML/CSS graphic or an AI-generated infographic based on the post content.

## Trigger

Requests like "design a graphic", "create a visual", "make an image", "graphic for my post", or a matching graphic after a post draft is finished.

## Step 1. Read the post

Read the supplied post before designing. The graphic must recap the post content, not illustrate an abstract concept. If the post is not supplied, ask for it.

Then ask which type fits best:

- **HTML/CSS graphic**: clean structured layout for frameworks, comparisons, steps, data. Fully editable, exported via screenshot.
- **Whiteboard infographic**: hand-drawn marker style. Recaps the post visually.
- **Branded infographic**: professional infographic using the brand's colours.
- **Auto-pick**: analyse the post. Numbered steps, frameworks, comparisons, or data tables go HTML/CSS. Workflows, tips, concepts, or stories go AI image prompt.

## Path A: HTML/CSS structured graphic

Design constraints:

- 1200x1400 pixels by default (follow an explicit client size if given)
- Dark background (`#1a1a2e` or the brand's colour) with high-contrast text
- Clean sans-serif font (Inter, system-ui)
- White or light text on dark; one accent colour for highlights and dividers
- 40px minimum padding on all sides. No stock photo backgrounds.
- Sections follow the content: 3 steps = 3 blocks, 10 tips = 10 blocks. The constraint is legibility on mobile, not a fixed count.

Single self-contained HTML file with inline CSS, including viewport meta tag. Distil the post into a short headline (5 to 8 words), key points as visual blocks, and a footer with the brand name from the brand folder.

Export a PNG using the available browser screenshot or local renderer. Wait for fonts and images to load. Inspect the PNG at full resolution and at 360px feed width: headline, every item, clipping, contrast, fonts, attribution. Fix the HTML and re-export until those checks pass. Keep the editable HTML alongside the inspected PNG. If no render capability exists, return the HTML as **render pending** and name the missing capability. Never call unrendered HTML visually verified.

## Path B: Image generation prompt

The graphic must summarise the key information from the post in a scannable visual format. It is not an abstract illustration.

Extract from the post: the hook (5 to 10 words), all required key points in order (aim for concise lines; propose a split if content will not fit), any stats worth highlighting, and a footer line (brand name + CTA if appropriate).

### Style 1: Whiteboard infographic

```
Generate a single image of a physical, hand-drawn infographic on a large whiteboard or notebook page.

Crucial Style Instructions (Read First):
Medium: The image must look like a photograph of a real whiteboard or large paper notepad.
Texture: All elements must look created by hand using colored marker pens (black, blue, red, green) and highlighters (yellow/orange). Lines should be slightly imperfect, wobbly, and have the texture of ink on a surface.
No Digital Fonts: All text, headings, and bullet points must appear handwritten or hand-printed in marker pen.

Layout: Structure the 1080x1350 image as follows:

TITLE (large, bold marker, top of page):
[Insert headline from the post]

CONTENT (hand-drawn sections with marker pen):
[Insert 3 to 6 key points, each as a short hand-written line with a bullet, number, or small icon drawn next to it]

[If there are stats or numbers, draw them large with a circle or box around them]

Use multi-colored markers for emphasis. Keep text large and legible. Make everything look hand-drawn with slight imperfections. Make it look like a photograph of an actual notebook page.

If confirmed in the brief, include the handwritten text "[verified brand name and approved CTA]" at the bottom of the image, in the same hand-drawn marker style.
```

### Style 2: Branded infographic

Pull colours from the active brand's `brand-style.md`; ask the client if not documented.

```
Generate a professional infographic image at 1080x1350 pixels.

Style: Clean, modern, editorial. Flat design with sharp edges and strong typography. No 3D effects, no gradients, no stock photos.

Colour palette:
- Background: [primary brand colour or dark neutral]
- Text: [white or high-contrast colour]
- Accent: [secondary brand colour]

Layout:
HEADLINE (top, large bold text):
[Insert headline from the post]

BODY (structured sections, each with an icon or number):
[Insert 3 to 6 key points as short lines, each with a visual marker: numbered circle, checkmark, or simple icon]

[If there are stats, display them as large feature numbers with a label underneath]

FOOTER:
[Brand name] | [CTA or tagline if appropriate]

Keep text large and scannable. Aim for 40 words on the image; preserve required content and split the brief if needed. No decorative borders. No watermarks. No logos unless the client provides one.
```

## After either path

Report the actual state: **HTML render pending**, **HTML + inspected PNG**, or **prompt-ready**. Link the files that actually exist. List any unresolved visual defects.

## Rules

- Always read the post before designing.
- Path A output is a single HTML file with inline CSS.
- Path B prompts are fully self-contained; the client pastes one cold into their image generator and gets the graphic.
- Distil the post content into the graphic. Do not copy the full post text.
