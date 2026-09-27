# GatorBait design plan: Blueprint + Webmaster + Rank (2026-09-27)

> **Status, Sept. 27:** Brenden said "Deploy" and to optimize rather than take the plan as gospel.
> - **Post template v1 is live** as embed `14a887e3`. It was improved before shipping:
>   - the headline comes first, with the cover under it inside the panel;
>   - the kicker comes from the URL.
> - **Decisions 1–3 are applied:**
>   - Barlow Condensed replaces Anton in `brand-style.md`;
>   - the template is live;
>   - the kicker is on.
> - **Decision 4 is settled by the layout:** the cover sits under the real headline.

This is the plan from the three design roles for the next two game weeks:
**Missouri (Sat., Oct. 3)** and the week after. It is built on what's live
now: the sports-news homepage, the separate Magazine, and the Buddy Martin
lead. None of those change shape here. Every live-site step goes through the
one site writer (Master Control) after Brenden approves it.

## Where design stands (verified this week)

| Surface | State | Gap |
|---|---|---|
| Homepage | Wix-served, no first-paint flash; game-day band worked all Saturday | The band is rebuilt by hand each game |
| Article pages | Stock Wix Blog look | **Post template v1 is built and tested (14,425 of 15,000 chars) but not deployed** |
| Covers | 5 layout families proven on Ole Miss day (score panel, portrait diagonal, duotone editorial, quote card + filmstrip, stat card) | All 16:9 only; no vertical (4:5 / 9:16) version for Facebook and Instagram |
| Fonts | Site and covers use Barlow / Barlow Condensed | `brand-style.md` still says **Anton**, so agents following it would drift |
| SEO | Posts publish with titles and OG images; schema not re-checked this week | No routine audit, and no Search Console numbers in the weekly digest |

## Blueprint (creative): one look, every size

1. **Lock the 5 cover families as versioned templates.** Names:
   - `gator-final@v1` (broadcast score panel)
   - `gator-news@v1` (portrait diagonal)
   - `gator-column@v1` (duotone editorial)
   - `gator-presser@v1` (quote card + filmstrip)
   - `gator-stats@v1` (stat card)

   Each gets a size map: 1920x1080 site cover, **1080x1350 feed**, **1080x1920
   story**. Source them from this week's HTML covers in the newsroom repo
   (`gameday/2026-09-26-ole-miss/*/cover*.html`).
2. **Vertical first for social.** Every published story gets its 4:5 feed
   graphic from the same family, as `brand-style.md` requires. The drafts
   sheet from n8n gets a `graphic_url` column so the social draft and its
   graphic are approved together.
3. **Contact-sheet gate (LESSONS #40)** before any cover publishes:
   - no photo on two covers the same day;
   - no two consecutive covers from the same family;
   - a photo credit on every cover.
4. **Missouri game-day kit, built by Thursday:**
   - pregame `gator-news`
   - halftime `gator-stats`
   - FINAL `gator-final`
   - presser `gator-presser`
   - column `gator-column`

   Photo slots are left open for Chris Spears' game photos, with nothing reused from Ole Miss.

## Webmaster (site): ship what's built, then automate the repeat work

1. **Stage the post template v1** (the plan is in the newsroom repo's
   `design/blog-post-template-v1/README.md`):
   - Create a new embed "GBM - Post template v1": HEAD, ESSENTIAL, **disabled**.
   - Enable it and check 4 posts on phone and desktop: a quote, "By the
     numbers", no cover, and a video.
   - Rollback is one toggle.
   - Target: live by Wednesday, so Missouri week runs on it.
2. **Game-day band from data, not by hand.** Move the score, clock and
   updates into one JSON source the band, the post template's "Up next"
   strip and the weekly digest all read. The band stays; only the upkeep changes.
3. **Wix Site Styles as tokens** (`agency/cloud/wix/DESIGN-SYSTEM.md`):
   - bind orange `#FA4616`, navy `#081B35`, blue `#0021A5`, Barlow and Barlow Condensed;
   - native pages stop drifting from the custom embeds.
4. **Daily site watch** (read-only):
   - homepage lead matches the newest post;
   - no broken images or embeds;
   - no pregame wording after a final.

   Findings go to the existing issue, not straight to the site.

## Rank (SEO): every story findable the day it runs

1. **Per-article checklist before publish:**
   - title under 60 characters with the player or opponent name first;
   - meta description under 155 characters;
   - OG image 1200x630 or larger;
   - canonical URL;
   - NewsArticle schema with a named author (Buddy Martin, Carlton Reese, Franz Beard and the rest, never just "Staff" when a writer wrote it).
2. **Search Console into the weekly digest:** top queries and pages from
   Wix's Google Search Console API (read-only), added to the Monday email.
3. **Monthly audit:**
   - dead URLs and redirects;
   - indexing of `/post/` pages;
   - phone speed on the homepage and one article.

   The fix list is staged for the site writer.

## Order of work

| When | Who | What |
|---|---|---|
| Mon, Sept. 28 | Blueprint | Lock the 5 families plus 4:5 and 9:16 sizes; fix `brand-style.md` fonts (after decision 1) |
| Tue, Sept. 29 | Webmaster | Stage post template v1 (disabled), run the 4-post check |
| Wed, Sept. 30 | Webmaster | Enable post template v1 after Brenden's yes; Site Styles tokens |
| Wed, Sept. 30 | Rank | Per-article checklist in the publishing playbook; audit the last 20 posts |
| Thu, Oct. 1 | Blueprint | Missouri game-day kit, contact sheet checked |
| Sat, Oct. 3 | All | Game day on the new template; band from the single JSON source |
| Following week | Webmaster + Rank | Search Console in the digest; monthly audit |

## Decisions for Brenden

1. **Headline font:** keep **Barlow Condensed** everywhere (site, covers,
   social) and retire Anton from `brand-style.md`? *Recommended: yes.* It's
   what readers already see, and one font keeps the brand consistent.
2. **Post template v1:** OK to stage it disabled this week and turn it on
   Wednesday if the 4-post check passes?
3. **Kicker on articles:** show the category (e.g., "GATOR FOOTBALL") above
   the headline? *Recommended: yes.*
4. **Cover repeats headline:** should the cover art carry the headline text,
   or just the photo plus a small label so the article headline isn't said twice?
   *Recommended: small label only on article pages; full headline on social 4:5 graphics.*
