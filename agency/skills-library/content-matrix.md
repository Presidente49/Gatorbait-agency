<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Content Matrix

**Owner:** scribe (writing)

Generate 24 to 40 post ideas in a single table by pairing the client's content pillars with 8 proven content formats.

## Trigger

Requests like "give me post ideas", "content matrix", "what should I post", "generate post ideas", "content ideation", or monthly content planning for the active brand.

## Step 1. Gather inputs

Read the active brand folder (`brand-voice.md`, `audience.md`, `goals.md`, `offers.md`) and pre-fill who the brand is, who it serves, and what it sells.

Get the brand's 3 to 5 content pillars. If they are not already documented, either ask the client or propose 4 based on the brand files and ask them to confirm or edit before continuing.

## Step 2. Build the matrix

Generate a markdown table:

- **Columns (formats, in this order):** Actionable, Motivational, Analytical, Contrarian, Observation, X vs Y, Present vs Future, Listicle
- **Rows:** the 3 to 5 pillars

Every cell holds one specific, concrete post headline tailored to that pillar AND format. Not generic, not reusable across pillars.

Format definitions:

- **Actionable**: ultra-specific how-to. Teaches the reader to do one thing.
- **Motivational**: story about someone who did something extraordinary in the niche.
- **Analytical**: breakdown of why something works the way it does.
- **Contrarian**: goes against common advice in the niche, backed up.
- **Observation**: a hidden or under-discussed trend the brand has noticed.
- **X vs Y**: compares two entities (tools, styles, teams, approaches).
- **Present vs Future**: current state vs a specific prediction, with the why.
- **Listicle**: a list of resources, tips, mistakes, lessons, or steps.

Good cell: "A 3-line hook formula for product launches". Bad cell: "Hooks".

Do not wrap the table in a code fence; render it as a real markdown table. If an interactive table surface is available, use that instead and skip the markdown dump.

Below the table, add one sentence naming the single strongest idea across the matrix and why.

## Step 3. Offer the next move

Ask which cell to write as a full post (referenced by pillar + format, e.g. "Hooks x Contrarian") and hand it to `post-writer.md` or `post-formatter.md`.

## Rules

- 3 to 5 pillars. More dilutes the matrix.
- Every cell idea specific to that pillar AND that format. No reuse across pillars.
- Tune language to the active brand's `brand-voice.md`.
