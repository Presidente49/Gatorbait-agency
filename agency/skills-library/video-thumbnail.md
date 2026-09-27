<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT. Adapted for Gator Bait Agency. -->
# Video Thumbnail

**Owner:** blueprint (creative/design)

Generate a branded video thumbnail from a video title. Uses a reference photo of the creator, high-CTR thumbnail principles, and brand colours to produce a ready-to-generate image prompt. Works for YouTube (1280x720) and short-form covers (Reels/Shorts/TikTok, 1080x1920).

## Trigger

Requests like "thumbnail", "youtube thumbnail", "build me a thumbnail", or a video cover image before the script is written. The thumbnail-first workflow sells the video before anyone hears a word of the script.

## Step 1. Gather inputs

Check the brand folder for a reference photo path, `brand-style.md` for colours, and `about.md` for the creator's name and positioning.

If no reference photo path is stored, ask: "Upload or provide the path to the reference photo you want used in the thumbnail. Ideally a clear shot with distinctive lighting and expression you plan to reuse across videos for brand consistency."

Then ask:

- **Video title**: the client types the full working title, or asks for 3 click-worthy title suggestions first.
- **Emotional tone**: shock/surprise (wide eyes, bold reaction), curious/thinking (slight smirk, raised eyebrow), confident/direct (eye contact, calm), or strong take (intense gaze, hand gesture).

Confirm the title and promise against the video's supplied content. Never invent a result, imply a demonstration exists, or use an unprovided face or brand mark. A missing reference photo leaves photo-based generation pending; a composition brief can still be drafted.

## Step 2. Apply thumbnail best practices

- **Face fills 30 to 50 percent** of the frame. Readable at small sizes.
- **3 to 5 words maximum** of large text. 6 if absolutely necessary.
- **Two colours dominate**: brand primary + one high-contrast accent.
- **One clear focal element** besides the face: bold number, arrow, prop, or symbol.
- **High contrast** between face, text, and background. Test by squinting.
- **Text is a hook phrase, not a sentence.** Examples: "I fired my team", "Never do this", "The 3-minute fix".
- **No small text, no logos bottom-right** (the watch-time/duration badge sits there).

## Step 3. Build the thumbnail brief

Output a concise brief for review:

```
THUMBNAIL BRIEF: [video title]

Composition: [face position, % of frame, direction of gaze]
Text: "[hook phrase, 3-5 words]"
Text placement: [left, right, top, wraps around face]
Colour palette: [primary hex], [accent hex], [background hex]
Supporting element: [prop / arrow / number]
Emotional tone: [tone from Step 1]
```

Then: "Here's the brief. Say 'generate' to output the image prompt or tell me what to change."

## Step 4. Output the image prompt

Once approved, output in a code block:

```
Using the attached reference photo of me, generate a video thumbnail at 1280 x 720 pixels (16:9).

Composition:
- Place me [left / right / centre] filling [30-50]% of the frame
- My expression: [tone details — e.g., shocked with wide eyes and open mouth]
- My gaze: [direction — e.g., looking directly at camera / looking off-frame toward the text]

Text:
- Display "[hook phrase]" in large bold sans-serif typography
- Text colour: [hex]
- Text outline: [colour, thickness for readability]
- Text placement: [specific area]

Colour palette:
- Primary: [hex]
- Accent: [hex]
- Background: [hex] — [describe treatment: flat, gradient, blurred scene, etc.]

Supporting element: [specific description of the supporting visual]

Constraints:
- Face must be clear and sharp
- Text must be readable at 320px wide (mobile size)
- No watermarks, no platform UI elements, no bottom-right corner text
- High contrast between face, text, and background
```

Tell the client: "Paste this into an image generator, attach your reference photo, and generate at 1280x720."

For short-form covers, swap the size to 1080x1920 (9:16) and the same structure.

## Step 5. Offer the next move

"Want me to outline the video next? Hook, mid, CTA from the thumbnail."

## Rules

- 1280x720 (16:9) for YouTube, 1080x1920 (9:16) for short-form covers.
- Never include the reference photo path in the prompt itself; the client attaches the photo separately.
- Never more than 6 words of text. 5 is ideal, 3 is best.
- Face must always be a visible focal point.
- Recommend a consistent thumbnail style across videos for channel recognition.
- Inspect the generated thumbnail at mobile size before shipping. A prompt is not a finished asset.
