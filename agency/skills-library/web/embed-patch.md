# Embed Patch Protocol (Wix Custom Embeds)

**Primary owner:** webmaster. Use it for any change to a site built from custom-code embeds (Wix, or any CMS with injected HTML/JS).

## The loop

1. **Read live first.** List embeds as a projection only (id, name, revision, length). Never dump the full list; it truncates. Fetch the one embed you'll change by ID.
2. **Find the real renderer.** Several embeds may style or draw the same thing. Grep them for the selector or text, and check which one actually runs on the route and viewport in question. A rule inside `@media(max-width:820px){.x{display:none}}` means a desktop-only element, not what a phone user is looking at.
3. **Patch in code:** GET → string replacement that asserts **exactly one** match per edit (abort the whole patch on any miss) → length check against the cap (Wix: 15,000 characters) → PATCH with the current `revision`, re-sending `category: ESSENTIAL`. Record base and result fingerprints.
4. **Publish** the site. On Wix, embed changes don't go live until you do.
5. **Sync the repo copy** from live and confirm the byte length matches the live length exactly. Repo copies drift; a mismatch means the repo was stale.
6. **Verify** with a real render. A local render with the production CSS works for layout; a real browser is needed for the full page.

## Verification traps

- **Headless fetchers (content-extraction APIs) usually don't run custom JS renderers.** They show the native CMS layer the custom renderer hides. Before trusting their output, check that the renderer's root ID is in it; if it isn't, the result says nothing about what visitors see. (GatorBait, Sept. 27: a "Today's Edition" block a fetcher reported was the hidden native layer.)
- The live renderer can differ from the repo copy. Read logic such as lead selection and rotation from the live embed, not the repo.
- Blog feeds and CDN pages cache. Cache-bust with a query string and `cache: 'no-store'`.

## Never

Delete an embed because its name says "old" or "backup"; some still hold live adapters. Stack a second fix layer on top of an existing guard without reading the guard. Change routing or automations as a side effect of a design patch.
