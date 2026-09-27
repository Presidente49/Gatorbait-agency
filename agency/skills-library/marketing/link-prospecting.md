<!-- Source: every-app/open-seo (https://github.com/every-app/open-seo) — MIT, Copyright (c) 2026 Ben Senescu. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
<!-- Modified from plugins/openseo/skills/link-prospecting/SKILL.md (commit 0ffff93): tool-agnostic, brand-first, split between rank (prospects) and bridge (outreach), drafts only; sending follows the brand's approval rules. -->
# Link Prospecting: Who Might Cite This, and Why?

**Owners:** rank finds and qualifies prospects; bridge (outreach) drafts the
messages. **Nothing is sent** by this skill. Outreach goes out only under the
brand's approval rules in `about.md`.

## Inputs

- The brand's domain and the **linkable asset**: a page, study, tool, guide,
  stat or story someone would reference.
- The reason someone would cite it (from the brand's positioning in
  `about.md`; if missing, ask the owner once and record the answer).
- Optional: competitors, market, language, location.

## Where prospects come from

- **Live results pages** for prospecting searches built from the asset:
  - `<topic> resources`
  - `best <category>`
  - `<competitor> alternatives`
  - `<topic> statistics`
  - `<topic> guide`
  - `<topic> examples`
  - `<topic> for <audience>`

  5–10 searches by default.
- **Competitor backlink profiles** (from an SEO data provider), strongest
  competitor pages first. Carry on without them if none is available.
- **Local:** chambers, associations, campus and community resources near the
  business (see `local-seo.md`).

## Workflow

1. Confirm the asset and why it is worth citing.
2. Run the prospecting searches; add competitor backlink evidence if available.
3. **Filter:**
   - Keep topical, editorial pages: articles, resource pages, lists,
     comparisons, statistics pages.
   - Drop homepages, logins, thin affiliate pages and spam.
   - Flag direct competitors and likely paid placements.
4. Give each good prospect an **angle**: missing or broken resource, better
   current data, a useful tool, inclusion in a comparison, or an expert quote.
5. For the strongest prospects, find a **public** contact path: the author page,
   contact page, editorial guidelines, masthead, or professional profile.
   Record the source URL for every contact detail.
6. Bridge drafts 2–3 reusable messages (list inclusion, article update,
   comparison mention), each personalized per page.

## Output

1. **The angle:** the best outreach angle and which prospect type to work first.
2. **Prospects:** table of URL, site, where it came from, angle, contact path
   (with source), priority.
3. **Why these:** the evidence that each prospect links to things like this, and
   the exact ask.
4. **Outreach drafts** (marked DRAFT, not sent).
5. **Limitations:** contacts not found, competitors, likely paid placements.
6. **Next steps:** who to contact first, pending approval.

## Guardrails

- **Never invent** an email address, handle or contact name. A contact detail
  without a source URL is not recorded.
- No mass outreach. Every message is personalized to its page and reason.
- Offering a link swap or payment for links is out of scope; refuse in one
  line.
- Obey anti-spam law and the brand's approval rules before anything is sent.
