<!-- Source: every-app/open-seo (https://github.com/every-app/open-seo) — MIT, Copyright (c) 2026 Ben Senescu. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
<!-- Modified from plugins/openseo/skills/keyword-clustering/SKILL.md (commit 0ffff93): made tool-agnostic (any SEO data source, not only the OpenSEO MCP), brand-first, read-only, with the agency's unknown-is-not-zero rule. -->
# Keyword Clustering: Which Page Should Win Which Searches?

**Primary owner:** rank (SEO). Hands page changes to the brand's designated
site writer (`about.md`). **Read-only**: this skill never edits the live site
or applies tags without a yes.

## Goal

Group searches into clusters that one page can satisfy, then map each cluster
to an existing page, a new page, or "not now". This is page mapping, not word
grouping.

## Before you start (brand-first)

1. Read the brand's `about.md`, `goals.md` and `offers.md`. The business and its
   goals decide which clusters are worth targeting.
2. You need the brand's **key pages** (the pages that matter). If none are
   recorded, propose a shortlist from the site and confirm it with the owner,
   then record it in the brand folder.
3. Check the brand's `learnings.md` and research log: if the same research ran
   in the last 30 days, reuse it and say so instead of paying for it again.

## Data sources (use what the brand has; say which you used)

- **Search Console** (free, best): real queries and the pages already earning
  impressions for them. Pull query + page together.
- **An SEO data provider** (paid per call, e.g. OpenSEO with DataForSEO):
  keyword ideas from a seed, a domain's ranking keywords, and live results
  pages (SERPs) to check intent.
- **Local results** when location decides the page (see `local-seo.md`).

No provider? Cluster from Search Console alone and label every volume
`unknown (no provider)`. Never invent search volumes or difficulty scores.

## Workflow

1. Gather the candidate searches (Search Console first, then provider ideas).
2. Remove duplicates, off-topic terms, and terms for a different product or
   audience.
3. Cluster by **search intent and page type**:
   - Same intent and similar ranking pages → same cluster.
   - Different intent, buying stage or result format → split.
   - Similar words do not mean the same cluster; the results page decides.
4. For important borderline terms, check a small batch of live results pages
   for overlap.
5. Assign each cluster: existing URL, proposed new page, or do-not-target.
6. Flag **cannibalization** (two pages competing for one intent). With Search
   Console, confirm it from real data: the same query splitting clicks across
   URLs.
7. Ask before saving any cluster tags.

## Output

Title: the site or keyword set.

1. **The map:** 1–2 sentences: clusters, pages to create, pages to update,
   cannibalization found.
2. **Clusters:** table of cluster, primary search, intent, target page,
   priority.
3. **Page briefs:** per cluster, the searcher's problem, the page to create or
   update, required sections and internal links.
4. **Cannibalization:** query, competing URLs, which one keeps it. Only with
   real evidence.
5. **Next steps:** ordered list, ending with the explicit ask before tagging.
6. **How this was made:** data sources, date, anything `unknown`.

## Guardrails

- Under 10 usable terms: a simple map, not clusters.
- Results-page intent beats word similarity.
- Label pages `proposed` when you have no URL data.
- Write durable results (key pages, research log entry) to the brand folder
  and transferable lessons to `learnings.md`.
