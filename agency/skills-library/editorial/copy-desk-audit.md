# Copy Desk Audit: Facts, Names and Copy Across Everything Live

**Primary owner:** scribe (the copy desk). Run it on every story in the current front-page rotation after each publishing burst (postgame, breaking news), and on any writer submission before it is published.

Built from the Sept. 27, 2026 GatorBait audit. A writer published a postgame piece with an AI cartoon as its cover, four misspelled names and a wrong return yardage, and it went straight to the lead slot of the front page because the front page leads with the newest story.

## Inputs

- The brand's **editorial desk file** (`agency/brands/<slug>/editorial-desk.md`): the canonical name list (players, coaches, staff, opponents, with suffixes), this week's verified game facts (score, records, key stat lines, with sources), approved photo sources and the known-typo list.
- The stories to audit: the newest 10–15 published posts (everything a reader can reach from the front page), plus any drafts submitted for review.

## Step 1: Automated sweep (every story, every run)

For each story, check the title, the excerpt and every paragraph for:

1. **Names:** any variant spelling from the canonical list (for example "Jaden" for "Jadan"), a missing suffix on first reference (Jr., III), or an opponent's name spelled wrong.
2. **Game facts:** a score, record or key stat that contradicts the verified facts table.
3. **Copy:** double spaces, a space before punctuation, a repeated word, and common homophones ("know one", "would of", "there team").
4. **Excerpt:** it must be a real one- or two-sentence summary. An excerpt that starts with the byline ("By ...") or with "GatorBaitMedia.com" gets rewritten.
5. **Cover art:** it must exist and must not repeat another live post's cover. The filename or content must not be AI-generated illustration for a news story ("chasing", "cartoon" and similar), and the photo credit must be known.
6. **Tags:** a story with zero tags is a finding.

Write the hits as `story → location → rule → snippet`. Expect false positives: surname-only second references ("Singleton") are correct AP style, so drop them.

## Step 2: Human-grade read (new stories only)

Read the new stories in full. Check every number and every quote against the source (box score, official transcript). Quotes must match the transcript word for word; paraphrase anything that doesn't.

## Step 3: Fix rules

- **Fix in place** only what is confirmed: names, arithmetic against the box score, typos, a missing suffix, the excerpt, tags. Keep the slug (URL) unchanged, even if the title changes.
- **Never publish over someone's in-progress edits.** If the post has unpublished changes pending, skip it and flag it; your save would push their half-finished edits live.
- **Don't rewrite claims you can't verify.** Leave them as written and send the writer a list ("unverified: first SEC back since ... — source?").
- Replace wrong-for-news art (AI cartoons) with a credited real photo from the approved sources. If no credited photo exists, use a branded graphic cover, never an uncredited photo.
- No email, alert or social post goes out because of a fix.

## Step 4: Record

Log one line per story (clean / fixed: list / flagged: list) in the brand's audit log. Tell the writer what changed in their piece.
