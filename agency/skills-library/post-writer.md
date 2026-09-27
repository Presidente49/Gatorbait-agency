<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Post Writer

**Owner:** scribe (writing)

Write social posts in the active brand's voice. Drafts from the brand's voice and audience files without framework constraints (see post-formatter for strict framework posts).

## Trigger

Requests like "write a post", "draft a post", "post about [topic]", "content idea", or a context dump (notes, transcripts, bullets) to turn into a post.

## Step 1. Gather inputs

Read `brand-voice.md` and `audience.md` from the active brand folder. If they do not exist, run `voice-builder.md` first, then stop.

Ask:

- **Topic**: the client types it, pastes a context dump, or asks for 5 suggested topics (read the brand's pillars and goals, suggest 5 specific topics with a one-line angle each, then let them pick).
- **References**: optional. The client can paste example posts for structural inspiration; note the structural patterns, then proceed.

## Step 2. Research and plan

Use supplied evidence first. Verify additional claims when needed; unavailable sources leave those claims pending. Look for: data points that support the angle, contrarian takes, real examples, common misconceptions to challenge.

Then present 3 candidate angles (each with a one-line description and hook) and a choice of framework: PAS, how-to list, story-to-lesson, or contrarian take. Fill in real options, never placeholder text. Let the client pick before writing.

## Step 3. Write the draft

- Read the brand voice for tone, rhythm, hook style, CTA style, and absence patterns (what the voice never does).
- Read the audience file for reader context.
- Match sentence length and paragraph rhythm from the voice file.
- Avoid every banned word, structure, and pattern in the voice file's absence section.
- Use the hook pattern that fits the chosen angle.
- End with the CTA style from the voice file.

Output the post inside a plain code block. After it, add 2 to 3 sentences on why you chose this hook and structure, referencing specific voice patterns.

Before presenting, review the draft against the supplied facts, voice, and requested format. For posts with required items, map every item to its passage and check ordering, duplicates, and omissions.

## Step 4. Iterate

Ask: "How does this feel? Tell me what to change, or say 'ship it' and I will save the final version."

Maximum 3 revision rounds. When approved, save the final post as a markdown file in the brand workspace.

Then: "Post saved. Say 'design a graphic' to create a visual, or 'score my post' to get feedback before publishing."

## Rules

- Always read the brand voice and audience files before writing.
- Always output posts in a plain code block.
- Do not add hashtags unless the brand voice explicitly uses them.
- Do not add engagement-bait CTAs unless they appear in the brand voice.
- Keep posts between 150 and 300 words unless the client requests otherwise.
- Plan before writing. Never skip Step 2.
