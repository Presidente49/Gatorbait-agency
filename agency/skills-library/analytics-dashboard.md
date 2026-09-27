<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Analytics Dashboard

**Owner:** scout (research/analytics)

Turn a platform analytics export into an interactive dashboard plus a written strategic analysis with 5 data-backed content recommendations.

## Trigger

Whenever a request mentions analysing performance, reviewing analytics, building a dashboard, or an analytics export file (xlsx/csv) is supplied for the active brand's social accounts.

## Step 1. Get the export file

Ask the client (or check the brand folder) for the analytics export. Any platform works: LinkedIn Analytics, Meta Business Suite export, Instagram Insights, YouTube Studio, TikTok analytics. A 30, 60, or 90 day window works best.

## Step 2. Parse the data

Read every sheet or section in the file. Confirm the account, reporting window, units, and actual column names before calculating. Export schemas vary; typical pieces are:

- **Overview**: impressions/reach over time
- **Engagement**: daily impressions, likes, comments, shares
- **Top posts**: ranked by engagement and by impressions (merge into one dataset per post, de-duplicate)
- **Followers**: daily new followers plus total count
- **Demographics**: titles, locations, industries, seniority (where available)

Top-post tables are samples, not the full posting history. Keep their denominators separate from account-wide metrics; do not infer best posting times from daily aggregates. Clean messy headers. Zero or missing denominators are "unavailable", never zero.

## Step 3. Build the dashboard

Build charts using whatever surface the agent has (React/Recharts artifact, or plain computed tables as a fallback). Dark theme where styled. Include in this order:

### Headline metrics
Total impressions, total reach, new followers, average daily impressions, average daily engagements, overall engagement rate (engagements / impressions over the same window), total posts tracked.

### Engagement trend (line)
Daily impressions and engagements over the full range. Mark the top 3 spike days.

### Follower growth (area)
Daily new followers, 7-day moving average trendline, cumulative gain.

### Post performance scatter
X = impressions, Y = engagements. Colour-code four quadrants:
- **Stars**: high reach + high engagement
- **Viral but shallow**: high reach + low engagement
- **Niche gold**: low reach + high engagement
- **Underperformers**: low reach + low engagement

### Day-of-week breakdown
Average impressions and engagements by weekday. Highlight the strongest days.

### Audience breakdown
Titles, industries, seniority, locations (whatever the export provides).

### Formatting
Format numbers compactly (`67K`, `1.2M`). Total follower count prominent. Dark background `#0f1117`, high-contrast chart colours.

## Step 4. Written strategic analysis

### Performance summary
Trajectory (growing, plateauing, declining) with trendline evidence. Current engagement rate, benchmarked only against a verified, dated source using the same metric definition.

### Top post patterns
Analyse top 10 by impressions and top 10 by engagements: posting day, time, content themes, formats. Interpret high-reach/low-engagement and low-reach/high-engagement signals.

### Audience-content fit
Who the core audience is from demographics. Which topics and formats fit them. Segments to lean into or away from.

### Growth velocity
Average daily follower growth. 30/60/90-day extrapolations (labelled extrapolations, not forecasts). Acceleration or deceleration.

### Day and timing strategy
Best days for impressions, best days for engagement, and an optimal posting schedule from the data.

### 5 specific content recommendations
Each includes: content angle, why the data supports it, target audience segment, evidence, and a testable hypothesis (never a guaranteed outcome).

## Step 5. Record the learnings

Save the dashboard and analysis to `agency/brands/<slug>/outputs/analytics/<YYYY-MM-DD>/`. Then append each finding the data supports (not the hypotheses) to the brand's `learnings.md` under a dated heading with the window and sample size. If a finding would hold for any business (not just this brand), also append it to `agency/shared/learnings.md`. Add a line to `agency/brands/<slug>/outputs/log.md`.

## Step 6. Offer the next move

Offer to draft one of the 5 recommendations as a full post using `post-writer.md` or `post-formatter.md`.

## Rules

- Use numbers, not adjectives. "Engagement rate is 2.3%" beats "engagement is healthy."
- Direct and concise. No fluff.
- Never invent metrics not in the export.
- Flag data-quality issues (missing columns, odd date ranges) instead of silently working around them.
- Run monthly. Patterns only surface over time.
