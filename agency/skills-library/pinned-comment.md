<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Pinned Comment

**Owner:** hype (social publishing)

Write a pinned comment plus a matching image generation prompt in the brand's voice. The post delivers value; the pinned comment builds personality, trust, and rewatch value with a real, self-deprecating aside.

## Trigger

Requests like "pinned comment", "first comment", or a first comment for a social post.

## The core insight

The image carries the joke. The comment captions the image. If the comment makes sense without the image, the comment is doing too much work. If the image needs the comment to be funny, the image is too weak.

Develop the image prompt first. Actual generation is a separate step; a prompt alone is never claimed as an asset.

## Step 1. Find the admission

Read the supplied post and brand context. Every strong post hides one quiet confession (e.g. "the tool does most of my actual job", "I am embarrassingly dependent on this workflow", "I gave away the product for free").

Write the admission as one sentence before doing anything else. **If you cannot name the admission in one sentence, stop. The post is not pinned-comment material yet.**

Never invent an admission, sponsorship, or personal experience the client has not supplied. Work only from the brand's confirmed facts and voice.

## Step 2. Build the image first

Three rules:

1. **One clear visual gag.** The eye lands on it in under a second.
2. **Played completely straight.** No winking, no thumbs up, no exaggerated faces. The humour comes from treating the absurd as normal.
3. **The brand is the lower-status figure.** The brand loses with quiet dignity. (If the brand voice is not self-deprecating at all, flag the mismatch and confirm the tone direction before generating.)

Image prompt format:

> "Using the person in the attached reference image, create a photorealistic image of [scene]. [One clear visual gag described in detail]. [the person's posture and expression, played straight]. [Lighting and framing notes]."

Image gag patterns that work: status reversal at the desk (the tool in the chair wearing a tie, the creator on the floor), the shrine (candles and a framed logo, creator kneeling), the banquet table (every other seat a competitor logo), the therapist's couch, the boardroom of logos.

## Step 3. Caption the image with the 4-line comment

Fixed structure:

```
📌 [Line 1: Describe the absurd thing as normal fact]
[Line 2: Flip the brand's status downward]
[Line 3: A sad flex, the smallest possible win]
[Line 4: Resigned acceptance, no punchline reach]
```

## Step 4. Run the 5 tests before sending

1. **Image gag test.** Can you describe the visual gag in 5 words? If not, simplify the image.
2. **Caption test.** Does line 1 caption the image as fact? If line 1 sets up a separate joke, rewrite.
3. **Loser test.** Is the brand the lower-status figure in every line? If it wins anywhere, rewrite.
4. **Reach test.** Does line 4 try too hard for a punchline? Make it smaller and sadder. Resigned beats clever.
5. **Boring-on-its-own test.** Read the 4 lines without the image. Is the comment boring alone? Good. The image is doing the heavy lifting.

Fix any failure before sending.

## The 4-line rules (non-negotiable)

- Exactly 4 lines. No more, no less.
- Each line is one complete sentence.
- Each line is 40 characters max.
- Start with 📌 on line 1.
- No P.S. (line 4 IS the punchline).
- No blank lines between sentences (they sit tight together).
- No hashtags, no semicolons.
- Follow the brand's voice prohibitions from `brand-voice.md`.

## Gold standard example

**The image:** The creator sitting cross-legged on the floor in striped pyjamas eating cereal, looking up at their own desk chair where an open laptop sits with a knotted necktie draped over the keyboard. Morning light, played completely straight.

**The comment:**

```
📌 The tool wears the tie now.
I wear the pyjamas.
The cereal was my idea, at least.
Small wins where you find them.
```

Why it works: line 1 captions the image as fact; line 2 is the deadpan status flip; line 3 is the saddest possible flex; line 4 lands without reaching. Read alone, mildly amusing; with the image, it sings.

## Output format

Always output: (1) the admission, one sentence; (2) the full image prompt; (3) the 4-line comment; (4) a one-line note on the five textual checks and whether an actual image was inspected.

Optionally provide 2-3 variations if the first attempt is borderline.
