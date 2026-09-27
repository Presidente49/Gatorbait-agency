<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Quote Post

**Owner:** blueprint (creative/design)

Two-step workflow for creating quote posts: draft original short quotes to accompany a caption, then produce an image generation prompt that bakes the chosen quote into a reference style.

## Trigger

Requests like "quote post", "quote graphic", "motivational post", "build me a quote", or a low-effort high-engagement graphic.

## Step 1. Get the caption

Ask: "Paste the caption this quote will accompany. The quote should reinforce the caption's message."

## Step 2. Generate quote options

Return 9 original quote options, grouped into 3 categories of 3:

1. **Growth and transformation** (e.g. "You don't find the time. You make it.")
2. **Resilience and grit** (e.g. "Your setback is someone else's setup.")
3. **Contrarian / bold** (e.g. "Stop asking for permission to start.")

Every quote must:

- Be under 15 words
- Feel human and authentic, not corporate
- Avoid jargon
- Work as a standalone line without context
- Punch hard in the first 3 words

Output:

```
QUOTE OPTIONS for your caption

1. Growth and transformation
   a. [quote]
   b. [quote]
   c. [quote]

2. Resilience and grit
   a. [quote]
   b. [quote]
   c. [quote]

3. Contrarian / bold
   a. [quote]
   b. [quote]
   c. [quote]
```

Then ask: "Which one lands best for your audience? Reply with the number and letter (e.g. 2b) or paste your own quote if none hit."

Tune the options to the brand voice if a voice file exists. If the brand voice is explicitly not motivational (analytical, contrarian-only, dry), flag the mismatch and confirm quote posts suit the positioning before generating.

## Step 3. Get the reference image

Ask: "Paste or describe the reference image you want to recreate. If you don't have one, I will suggest a style."

Suggested styles when none is supplied:

- **Notebook / hand-drawn**: simple sketch, cream background, pen marks
- **Minimalist editorial**: large serif type, lots of white space, one accent colour
- **Bold poster**: heavy sans-serif, solid colour block background, high contrast
- **Photo with text overlay**: polaroid or film-photo look

## Step 4. Output the image prompt

Output in a code block, with the quote filled in:

```
Recreate the attached reference image with the following quote:

"[CHOSEN QUOTE]"

Critical constraints:
- Output at exactly 1080 x 1350 pixels (4:5 vertical)
- Match the style, typography, and colour palette of the reference image
- Keep the quote as the focal point — centred and legible
- For an original quote, use no invented attribution. For a sourced quote, retain its verified attribution as approved in the brief.
- Maintain the visual tone of the original but with the new text

The quote must be perfectly spelled and punctuated exactly as written above.
```

Tell the client: "Paste this into an image generator with the reference image attached. Generate at 1080x1350."

## Step 5. Honest expectation-setting

"Performance for your audience is unverified until tested against your own posts."

## Rules

- Always 1080x1350. Horizontal quote graphics get lost in the feed.
- Never more than 15 words in the final quote.
- Never fabricate attribution. Quotes are written fresh, not sourced from real people, unless the client asks.
- Inspect the generated image at feed size before shipping. A prompt is not a finished asset.
