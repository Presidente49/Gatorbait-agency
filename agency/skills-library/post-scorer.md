<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Post Scorer

**Owner:** scout (research/analytics)

Score a social post using the brand's real performance data. Pulls post history via available integrations (or uses a supplied export) to find what actually performs, then scores the draft against those patterns.

## Trigger

Requests like "score my post", "review my post", "rate this post", "give me feedback", "how good is this post", or a post pasted in asking for critique.

## Step 1. Get the post

If already pasted, use it. Otherwise ask: "Paste the post you want scored."

## Step 2. Load scoring data

The scorer needs two things: the brand's voice system and real performance data.

### Voice system

Read `brand-voice.md` and `audience.md` from the brand folder. If missing, note it and score without voice matching.

### Performance data

Check for client-supplied exports or cached post data in the brand folder. Verify the account, collection date, and coverage before using it. Never use another client's data or generic benchmarks.

If data is missing, offer:
1. The client uploads an export of their posts with engagement counts.
2. Fetch post bodies and aggregate counts through an available authorised scraping integration, after confirming account, scope, and cost with the client.
3. An editorial review now, with performance comparison marked unavailable.

Request post bodies and aggregate counts only. Never scrape comments or replies. Save permitted post data under an outputs folder in the brand workspace with the account and collection date. If no fetch capability exists, do not claim the history was fetched.

## Step 3. Analyse the top performers

When performance data is available, before scoring:

1. Calculate an engagement score per post: reactions + (comment count x 3), an editorial weighting rather than private reach analytics.
2. Identify the top 10% by engagement score.
3. From those, extract: hook types (contrarian, number-led, bold claim, personal story, question, news), average word count, format distribution (text, image, carousel, video), CTA patterns, topic clusters that over-index, sentence rhythm (average sentence length, paragraph breaks).
4. Note the bottom 10% patterns to identify what fails.

Record the source, date, sample size, and patterns. Unknown counts are missing, not zero. If the sample is too small, say so. No numerical total implies predicted performance.

## Step 4. Score the post

Score across 5 criteria, 1 to 10 each. Separate editorial judgement from measured historical comparisons. If neither a voice profile nor confirmed post samples exist, mark Voice match unavailable and report the total over 40; otherwise over 50.

### Hook strength (1 to 10)
Does the opening use a hook type that performs for this brand? Is it specific with a number, name, or detail? Cite the pattern when history exists; without history, label the score editorial.

### Voice match (1 to 10)
Does the post match tone, rhythm, sentence length from the brand voice? Any violations of the voice's absence patterns? If no voice files, use confirmed post samples. If neither, mark unavailable.

### Value density (1 to 10)
Do the brand's best posts teach, give steps, share data, or tell stories? Does this draft match that value pattern? Is the takeaway specific enough to save or share? Compare word count to the top 10% average.

### Structure and format (1 to 10)
What format gets the most engagement for this brand? Does the draft's structure match the rhythm of top posts? Is it scannable on mobile? Does the CTA match best-performer patterns?

### Publish readiness (1 to 10)
Are all claims supported and required items covered? Would it blend naturally into the brand's feed? Any red flags (banned words, generic phrases, corporate tone)? Right length vs top performers?

## Step 5. Output the scorecard

Output in a code block:

```
POST SCORE

Data source: [verified export / verified fetch results / editorial only]
Posts analysed: [number or unavailable]
Top 10% avg engagement: [measured number or unavailable]

Hook strength:         [X] / 10  [hook type detected]
Voice match:           [X] / 10
Value density:         [X] / 10
Structure and format:  [X] / 10  [format: text/image/carousel]
Publish readiness:     [X] / 10
----------------------------------------
TOTAL:                 [XX] / [50 or 40, excluding unavailable voice]

VERDICT: [One sentence referencing specific data]

TOP PERFORMER COMPARISON:
Your top posts average [X] words, use [hook type] hooks,
and include [CTA pattern]. This draft [matches/differs] because [specific reason].

FIXES:
1. [Specific fix backed by data, e.g. "Your top 10% posts open with numbers. This opens with a question. Switch to a stat."]
2. [Second fix backed by data]
3. [Third fix if needed]
```

For editorial-only review, omit the top-performer comparison and give specific copy/structure fixes labelled editorial. Never fill the template with invented metrics.

## Step 6. Offer next steps

"Want me to rewrite the weakest section using patterns from your top posts, or ship it?" If rewrite requested, apply the fixes and output the revised post in a code block.

## Rules

- Always try real data before falling back to generic advice.
- Mark each finding as history-based or editorial judgement.
- A high editorial score does not establish historical fit or predict reach.
- Be honest. A generous scorer is useless.
- If data is stale (14+ days old), suggest a refresh before scoring.
- Inform the client before running any paid scrape.
