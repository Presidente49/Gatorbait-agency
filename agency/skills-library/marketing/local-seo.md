<!-- Source: every-app/open-seo (https://github.com/every-app/open-seo) — MIT, Copyright (c) 2026 Ben Senescu. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
<!-- Modified from plugins/openseo/skills/local-seo/SKILL.md (commit 0ffff93): tool-agnostic, brand-first, read-only; profile edits go to the owner. Written for white-label brands with a storefront or service area (the pizza-shop case). -->
# Local SEO: Why Does (or Doesn't) This Business Show Up in Maps?

**Primary owner:** rank. **Read-only.** Google Business Profile changes are
made by the owner (or whoever the brand's `about.md` names), never by this
skill.

Use it when rankings depend on a location or service area: restaurants, shops,
clinics, contractors. For national search, use `keyword-clustering.md` and
`seo-audit.md`.

## Inputs

- The business name, ideally its Maps ID (CID or place ID). Match on the ID;
  names collide with chains and look-alikes.
- Its storefront coordinate (from a local search result for the business).
- 1–3 searches customers actually type ("pizza delivery", not the brand name).
- The brand's `about.md` for what it does and where it serves.

## Data sources

A local-search data provider (e.g. OpenSEO with DataForSEO) gives: nearby
listings, the Maps result set near a point, profile details, reviews, and a
**rank grid** (rank at each point around the storefront). **Every grid point is
a paid search.** A 3×3 grid is 9 searches; tell the owner the cost before a 5×5
or several keywords.

No provider? Do the profile comparison by hand from public Maps listings and
mark the grid `unknown (no provider)`.

## Workflow

1. Find the listing and its ID. Several locations means a chain (see below).
2. Pull the Maps results for the main search near the storefront. Record the
   top 3–5 competitors and the business's own position.
3. **Compare against the top two competitors:**
   - primary and additional categories;
   - review count;
   - hours completeness;
   - photo count;
   - claimed status.
4. Check the listing's website link: it should go to this location's page, not
   a homepage or old domain.
5. **Reviews:** volume, recency, average rating, and the share with an owner
   reply, for the business and its strongest competitor.
6. **Rank grid** for the main search: does it rank only at the storefront or
   across the service area? Who wins where it doesn't?
7. Only when the basics are competitive: profile Q&A and posting cadence.
8. Prioritize. **Category and claim problems always outrank posting cadence.**

**Chains:** one snapshot table for every location. Deep-dive all of them up to
5; above 5, recommend 1–3 (e.g. the weakest profile in the busiest market) and
ask.

## Output

1. **Snapshot:** category, rating, review count, claimed status (a row per
   location).
2. **The one fix:** the single change that matters most.
3. **Head to head:** signal, this business, best competitor, gap.
4. **Maps coverage:** where visibility drops off and who wins there, with every
   value labeled.
5. **Next steps:** ordered, owner-actionable.
6. **How this was made:** sources, date, cost of paid calls, anything `unknown`.

## Reading the grid honestly

A missing rank means the business wasn't in the results returned at that point.
Read it with that point's result count: a full list means outranked, a
near-empty one means a thin results page, not proof of invisibility. Confirm the
grid is centered on the real storefront before spending on it.

## Guardrails

Never recommend review gating, fake or incentivized reviews, or keyword-stuffed
business names. Don't infer local-pack strength from national rankings.
