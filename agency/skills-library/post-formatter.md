<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Post Formatter

**Owner:** scribe (writing)

Turn a topic into a ready-to-publish social post using a strict framework: PAS, AIDA, BAB, STAR, or SLAY. Up to 20 nonblank lines, mobile-formatted with blank lines between sentences.

Different from post-writer: post-formatter applies a strict framework. post-writer drafts in the brand's voice without framework constraints.

## Trigger

Requests like "format this as a post", "turn this into a post", "write it as PAS" or any named framework.

## Step 1. Gather inputs

- **Topic**: the subject as a single sentence, or a context dump (notes, stats, transcripts) to turn into a post.
- **Framework**: PAS (Problem, Agitation, Solution), AIDA (Attention, Interest, Desire, Action), BAB (Before, After, Bridge), STAR (Situation, Task, Action, Result), SLAY (Story, Lesson, Actionable advice, You), or pick the best one for the topic.
- **Context**: facts, stats, tone notes, who the post is for.

## Step 2. Write the post

Global rules for every output:

- Maximum 20 nonblank lines. Target 150 to 200 words where the line limits allow; do not pad. Supplied copy and required facts take precedence.
- Blank line after every line.
- Most lines: one sentence, 55 characters or fewer.
- Up to 4 lines may be mini-paragraphs (2 to 3 sentences, 110 characters or fewer).
- Short simple words. Zero jargon, zero fluff.
- No questions unless the hook itself is a question.
- No emojis except checkmarks for numbered lists and the recycle symbol in the CTA.
- Rule of Three: at most two trios per post.
- Vary sentence starts. Do not over-use "I".

## Step 3. Structure

- **Line 1 (Hook)**: 50 characters or fewer, plain text ready to paste.
- **Line 2 (Twist / Contrast)**: 50 characters or fewer. Opposes or surprises the hook.
- **Lines 3 to 18 (Core)**: the chosen framework, 3 to 5 lines per stage. Keep the actual number and order of required steps or items; do not force a trio. Use arrows to show flow where useful.
  - PAS: Problem -> Agitation -> Solution
  - AIDA: Attention -> Interest -> Desire -> Action
  - BAB: Before -> After -> Bridge
  - STAR: Situation -> Task -> Action -> Result
  - SLAY: Story -> Lesson -> Actionable advice -> You
- **Final 1 to 2 lines (Wrap and CTA)**: close the lesson within the 20-line total, in the brand's closing style from `brand-voice.md`.

## Step 4. Output

Output the finished post inside a code block. Keep any next-step question outside the paste-ready copy.

## Step 5. Offer the next move

"Want a matching graphic (graphic-designer skill) or want me to score it against your post history (post-scorer skill)?"

## Rules

- The code block contains only the finished post.
- Enforce line length, word count, and line count limits. Count them in the exact final copy.
- If the brand has a voice file, tune tone and rhythm to match it.
- Preserve required item coverage.
