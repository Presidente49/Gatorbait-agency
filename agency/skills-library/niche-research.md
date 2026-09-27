<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Niche Research

**Owner:** scout (research/analytics)

Surface the 20 most relevant stories in a client's niche from the last 7 days. Verified dates, real links, shareable angles.

## Trigger

Requests like "research my niche", "what's trending", "find stories", "this week's news", "content research", or a niche dropped in asking what's happening.

## Prerequisites

Use the live web search and browser capabilities actually available. Browser feed access and indexed web search are different evidence surfaces: if feeds are unavailable, continue with indexed public results and label the missing feed coverage. If no live source access exists, current research is pending; supplied dated sources can support a clearly labelled limited brief.

Never scrape comments or replies on any platform. Read original post bodies and article text only. Aggregate engagement counts may be recorded when visible.

## Step 1. Gather the niche

Read the active brand folder first; the brand's niche and audience may already be documented there. If not, ask the client to name the exact niche phrase.

## Step 2. Research like a human

Work these sources, skipping inaccessible ones with an explicit coverage note. Verify publish dates on every item. Exclude anything older than 7 days without exception.

### 2a. Reddit

1. Scan the home feed and r/popular, load more posts.
2. Open niche-relevant posts, check the "posted X days ago" timestamp, discard anything over 7 days.
3. Repeat in niche-specific subreddits.

### 2b. X (Twitter)

1. Scan the For You feed, multiple screens.
2. Open original niche-relevant posts (author-authored continuations are context; do not collect reply threads).
3. Check each post's timestamp. Discard anything over 7 days.

### 2c. Web search

Run these queries one by one with the date filter set to the past week, open top results, verify publish dates:

- `[niche] news`
- `[niche] launch`
- `[niche] controversy`
- `[niche] research`
- `[niche] regulation`

If a date is missing, unclear, or older than 7 days, exclude the item.

## Step 3. Synthesise into themes

Group verified in-window items into themes. Each theme may combine social discussion and news coverage. Select themes showing at least two of: strong attention, clear disagreement or debate, novel insight, real-world implications.

Target 20 themes. Fewer is acceptable if genuinely limited; never pad with weak items.

## Step 4. Output

First line:

```
As of [YYYY-MM-DD]
```

Then a markdown table with these exact columns:

```
| Theme / Emerging Story | Platforms (Reddit, X, News) | Key Communities / Accounts / Sources | Representative Links | Attention Signals | What's Happening or Being Debated | Why It Matters for [NICHE] | Shareable Angle |
```

Add a short coverage note outside the table naming which feeds or indexed searches were actually used, the date window, and any inaccessible sources.

## Step 5. Offer the next move

"Any row here you want me to turn into a post? Call post-writer with the row number, or post-formatter to apply a framework."

## Rules

- Never invent links, metrics, or dates.
- Exclude anything older than 7 days without exception.
- Verify every publish date before including an item.
- Indexed results do not prove a full feed scan. Missing feed access is a limitation, not evidence of no relevant stories.
