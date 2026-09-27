<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Voice Builder

**Owner:** scribe (writing)

Build a brand voice profile from a short interview plus 3 to 5 sample pieces of writing. Produces `brand-voice.md` (and an `about.md` if the brand folder lacks one), saved into the brand folder. Run this at the start of any client engagement where the agent must write in the client's voice before drafting new content.

## Trigger

Requests like "build my voice", "learn my voice", "set up my content system", "onboard me", "train on my writing", or writing samples dropped in at the start of an engagement.

## CRITICAL: Auto-start on load

When this workflow is requested, go straight to Step 1. No preamble, no summary, no "want me to run this now?". The first message is the interview questions.

## Step 1. Run the brand interview

Two batches of questions (max 4 per batch). Ask in chat or with the available question tool.

### Batch 1 (the first message, nothing before it)

1. **About the brand**: What is the business name and what does it do?
   - Options: solo creator / agency or consultancy / media brand / local business
2. **Audience**: Who are they writing for?
   - Options: founders and decision makers / marketers / consumers and fans / job seekers / other
3. **Topic pillars**: What are the 3 to 5 topics they want to be known for? (multi-select; let them type their own)
4. **Point of view**: What do they believe that others in their space do not?
   - Options: the consensus is broken / people overcomplicate it / a big shift is coming / other

### Batch 2 (immediately after Batch 1 answers, no commentary between)

5. **Brand promise**: The one thing they want people to think when they see the brand name.
   - Options: this brand is practical / this brand is honest / this brand is ahead of everyone / other
6. **Off limits**: One thing they refuse to write about (politics, personal life, competitors, other).

If any answer is blank, ask that specific question once more in chat, then move on.

## Step 2. Write the brand profile

Save an `about.md` in the brand folder (skip if one already exists with equivalent content):

```
# About

## Name and business
[From question 1]

## Audience
[From question 2, expanded into 2 to 3 sentences on who the reader is]

## Topic pillars
[3 to 5 topics from question 3, one line each]

## Point of view
[From question 4, written as a clear statement]

## Brand promise
[From question 5]

## Off limits
[From question 6]
```

Keep it under 300 words. Every line should be something the agent references when writing.

## Step 3. Ask for the samples

"Now paste 3 to 5 pieces of writing I should learn from: posts, newsletter issues, essays, emails, or any published writing. One piece per message or all at once. They can be yours or someone whose voice you want to borrow (tell me which, so it is labelled as borrowed)."

Minimum 3 samples before analysis. If fewer than 3, ask for more. If the client has no samples, offer to write a neutral starter set the brand can swap out later; label it clearly as a starter, never as the brand's voice.

## Step 4. Analyse the samples

Read every sample. Look for patterns across all of them, not quirks from one piece:

- **Voice signals**: average sentence length; paragraph rhythm; hook/opening style; point of view; tone; signature phrases; CTA or closing style
- **Structural signals**: length range; lists vs prose; how they open, transition, and close
- **Topic signals**: subjects across samples; who the audience appears to be; what the brand stands for
- **Absence signals**: words and punctuation consistently absent; hook types never used; tones never hit; structures avoided

## Step 5. Write brand-voice.md

Single integrated profile covering how the voice writes and what it avoids. No separate absence file.

```
# Brand Voice

## Who we sound like
[2 to 3 sentences describing the overall voice in plain language]

## Tone
[3 to 5 attributes consistently hit, plus 1 to 2 tones the voice never hits, drawn from gaps]

## Sentence rhythm
[Average length, pacing, paragraph structure. Avoidance patterns: e.g. no staccato fragments, no sentences over 25 words]

## Hook patterns
[3 to 5 hook types observed, one example each. Note hook types absent across all samples]

## How we open
[1 to 2 sentences. Note opening moves avoided if a clear pattern exists]

## How we close
[1 to 2 sentences, include CTA style. Note closing moves avoided]

## Signature phrases
[Recurring words or phrases from the samples]

## Off-limits
[Words, punctuation, or constructions absent from every sample. Only items clearly avoided]

## What this voice never does
[3 to 5 specific behaviours from gaps in the samples]
```

Fill every section from the actual samples. No generic filler. Where a pattern is not present, say so. Separate explicit client prohibitions from patterns merely absent in a small sample; label the latter provisional with sample counts.

Keep `about.md` under 300 words and `brand-voice.md` under 500 words.

## Step 6. Confirm and hand off

"Your voice profile is built. brand-voice.md (and about.md) are in your brand folder. These skills read both files when invoked; edit either anytime.

What you can do next:
- Say 'build my newsletter voice' for newsletter-specific instructions
- Say 'write a post' to draft a post in this voice
- Say 'design a graphic' to create a visual for a post
- Say 'score my post' to get feedback on a draft
- Say 'optimize my profile' to rebuild the brand's profile"

## Rules

- When triggered, go straight to Step 1. No summary, no explanation, no preamble.
- Work from what is in the samples. Never invent patterns that are not there.
- Minimum 3 samples for pattern detection.
- If samples contradict each other, note the contradiction in brand-voice.md rather than smoothing it over.
- If samples are borrowed from another writer, label that clearly; starter or borrowed samples never describe the client's experiences or established voice.
