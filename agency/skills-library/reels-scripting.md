<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Reels Scripting

**Owner:** scribe (writing)

Turn a reference Reel into a script for the client's own Reel, tuned to their voice and repurposed from their own content (newsletter, article, or post).

## Trigger

Requests like "script a reel", "reels scripting", "turn this into a reel", or a Reel URL pasted as a format reference.

## Prerequisites

The full video-analysis route needs an authorised video-scraping integration and an AI video-analysis model. Check only the capabilities needed for the chosen route:

- A supplied video file can skip the scrape stage.
- A supplied transcript or analysis can skip the scrape and analysis stages; label the result transcript-based, not video-analysed.
- Missing credentials, a private video, or an unavailable model leaves that stage pending. Explain what is missing. Never modify account configuration, print credentials, or silently substitute a provider.

Never scrape comments or replies on any platform. Video and metadata only.

## Step 1. Get the reference

Ask: "Paste the reference Reel URL. This is the outlier Reel you want to reverse-engineer the format from."

A single Reel is a reference, not a verified outlier. Call it an outlier only when supplied data establishes its performance relative to the same creator's recent posts.

## Step 2. Get the source material

Ask: "What content do you want to repurpose into this Reel? Paste the relevant newsletter section, article, or post, or type the core idea in a sentence."

Read the brand's voice, audience, and content files so the script matches the brand.

## Step 3. Scrape and download the Reel (if authorised)

Save to a brand workspace outputs folder. For the single requested Reel:

1. Use the authorised scraping route to fetch the Reel. Verify the provider supports video-only collection before calling; do not guess actor inputs.
2. Extract the video URL and download the video file.
3. Save raw scrape metadata (views, likes, caption first 200 characters, date) to a JSON file.

Confirm file size and metadata before continuing. If this stage fails, report the failed stage and offer supplied video/transcript input. Never fabricate video analysis.

## Step 4. Analyse the reference

Send the video to the authorised AI video-analysis model with this prompt:

```
I'm studying this Reel to write my own script in a similar style for my audience of [AUDIENCE FROM brand files].

## Full Transcript
- Transcribe EVERY word with timestamps

## Hook
- Exact first words spoken
- Word count of the hook
- What makes it stop the scroll?

## Language Patterns
- Average sentence length
- You/your vs I/me ratio
- Transitions between points
- Where are the minimiser words?

## Structure
- Total duration
- Section breakdown with timings
- What's the before/after moment?
- What's the CTA?

## One key insight
- The single most important technique to learn from this Reel
```

Save the analysis to a markdown file alongside the download.

## Step 5. Write the new Reel script

Using the analysis, the source material, and the brand voice files, write the script. Apply these rules (non-negotiable):

### Hook
- Never open with "I". Use "this", "you", a fact, or a name drop.
- Proven formats: "This changed... forever" / negative flip ("X is useless unless...") / capability statement.
- Creates curiosity or pattern interrupt within 3 seconds.
- Mirror the reference hook's word count and structure.

### Body
- Short sentences. No semicolons.
- Use "you" conversationally.
- Never merge three or more staccato fragments. Combine into one flowing sentence.
- Never state the conclusion. Let the facts do the work.
- Use a comment CTA only if the client has a real deliverable and a confirmed working automation. Otherwise use a next action that makes no delivery promise.

### Comment trigger (only when supported)
- Single caps word only (SCRIPT, WIKI, PROMPTS, VIDEO).
- Must directly relate to what is promised. No quotes, no "below", no trailing punctuation.

### CTA
- "Comment [WORD] and I'll send you [specific thing]"
- Short. No padding.

### Duration and structure
- Target 30 to 45 seconds total.
- 2 key points maximum, not 3.
- Caption mirrors the script. Update both together.

### Script file structure

```
# Reel: [title]

## Reference analysis
- URL: [reel url]
- Views: [number]
- Key technique: [from analysis]

## Duration target
30-45 seconds

## Hook (0-3s)
[Exact words]

## Point 1 ([start]-[end]s)
[Exact words]

## Point 2 ([start]-[end]s)
[Exact words]

## CTA ([start]-[end]s)
[Exact next action, with a comment promise only when delivery is confirmed]

---

## Caption
[Mirror the script, formatted for the platform]

## Comment trigger (only if configured)
[WORD or not applicable]

## Deliverable (only if promised)
[The real available resource or not applicable]

---

## Visual notes
[Cuts, B-roll ideas, text overlays]
```

## Step 6. QA loop

Score out of 100: source accuracy (30), brand voice match (25), hook and structure (20), spoken duration and clarity (15), caption/CTA consistency (10). Cite evidence for each score. Fix actual violations and re-score, up to three passes. Gate is 95/100; if unresolved, report a draft with the specific blockers rather than inflating the score. Time a spoken read when available; otherwise label duration estimated.

Common violations: opens with "I"; three or more staccato fragments; states the conclusion; multi-word comment trigger; over 45 seconds; 3 points instead of 2; caption does not mirror script.

## Step 7. Hand off the script

Deliver the reviewed script and matching caption with reference source, analysis method, and any unresolved checks. The client records it or requests their own production workflow. This skill does not ship an editing or publishing pipeline.

## Rules

- Never skip the 95/100 QA gate.
- Always read the brand voice and audience files before writing.
- Never invent metrics from the reference Reel. Use only verified metadata; mark absent metrics unavailable.
- Every script includes the matching caption; include a comment trigger only when the promised delivery works.
