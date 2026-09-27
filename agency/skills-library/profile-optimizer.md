<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT. Adapted for Gator Bait Agency. -->
# Profile Optimizer

**Owner:** bridge (outreach/partnerships)

Rebuild a social profile for maximum conversions. Works for LinkedIn, Instagram, X, TikTok, or YouTube channel pages. Produces new headline/bio options, about section, experience/credentials section, featured/section-link strategy, and image generation prompts for banner, profile picture, and featured tiles.

## Trigger

Requests like "optimize my profile", "fix my profile", "rewrite my headline", "profile review", "profile audit", or a profile PDF/screenshot uploaded for review.

## Step 1. Gather inputs

Read the active brand folder (`brand-voice.md`, `audience.md`, `goals.md`, `offers.md`) and pre-fill from it. Then ask:

- **Primary goal** of the profile: booked calls, inbound leads, newsletter subscribers, job opportunities, product sales, or community growth.
- **Main offer**: coaching, consulting, agency services, freelance, physical product, digital product, or content.
- **Brand colours**: hex codes, or offer to suggest from positioning.
- **Social proof**: years of experience, client results, media features, or custom proof points the client pastes.
- **External links** (max 2): primary conversion goal (booking page, application form, sales page) plus a secondary trust/lead builder (newsletter signup, free resource, portfolio, case study).
- **Current profile**: client pastes their headline, bio, and experience; starts fresh from brand files; or uploads a screenshot.

Wait for all inputs before proceeding.

## Step 2. The headline / bio

Write 3 options in a code block. Constraints:

- Max 50 characters (LinkedIn/X style) or the platform's limit.
- Sentence casing only (not Title Case).
- Lead with core value. Include the target audience where character count allows.
- No job titles (no "Founder" / "CEO" / "Designer"). No fluff words.
- Format: [Core value] + [for target audience].

```
Option 1 (Direct): [outcome + audience]
Option 2 (Pain-focused): [problem + audience]
Option 3 (Differentiator): [unique angle + audience]
```

Let the client pick one before continuing.

## Step 3. The about section

Output in a code block. Full sentences; one line break between sentences or short phrases; double line break between sections (hook, story, authority, CTA). Do not manually wrap lines; the platform handles it.

Structure: Hook > Struggle/Empathy > Method/Philosophy > Authority > CTA.

Tone: punchy, direct, human. Not corporate. Use supplied facts only, never invented biography.

## Step 4. The experience / credentials section

Rewrite the top 2 roles in a code block. Storytelling format, not bullet points. 8 to 15 sentences per role maximum.

Structure per role: Context > Challenge > Action > Result.

## Step 5. Featured / link strategy

2 items maximum, both external links:

- **Item 1**: primary conversion goal. Title 3 to 5 words, benefit-focused.
- **Item 2**: secondary value builder. Title 3 to 5 words, benefit-focused.

No "DM me" items, no internal posts.

## Step 6. Visual design brief

Output image generation prompts, each in its own code block, fully self-contained (the client pastes each cold into an image generator). State the brand colours at the top with one line on why they fit the positioning.

### Asset 1: Banner (platform-native size, e.g. 1584x396 for LinkedIn, 1500x500 for X)

- Use the attached photo of the client, exact dimensions stated.
- Chosen headline text, centre-right (or per composition).
- A 5 to 8 word tagline below the headline.
- A CTA button element (3 to 4 words).
- Only supplied, confirmed social proof. Omit when absent.
- Brand colours, specified background style.

### Asset 2: Profile picture (platform size, e.g. 400x400, works cropped to circle)

- Attached headshot as the base. Brand colour background. Face at 60 to 70% of frame. Works cropped to a circle.

### Assets 3 and 4: Featured/link tiles (e.g. 552x368)

- Title text from each featured item as the focal point. Brand colours. Simple clickable cue (arrow icon). Clean, minimal. Tile 2 visually distinct from tile 1 (swap primary/secondary).

After the prompts: "Copy each prompt into an image generator one at a time. For the banner and profile picture, attach your headshot alongside the prompt. The tiles do not need a photo."

## Rules

- All profile copy (headline, about, experience) goes in code blocks.
- Write full sentences. No forced mid-sentence line breaks.
- No job titles in headlines. No block paragraphs anywhere.
- Never use another client's voice files, identity, or private files. Confirm the intended brand if files conflict.
- End at the design brief. Do not auto-offer a launch post or engagement strategy.
