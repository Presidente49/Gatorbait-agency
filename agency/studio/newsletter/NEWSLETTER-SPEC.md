<!-- Source: thesysdev/openui (https://github.com/thesysdev/openui) — MIT, Copyright (c) 2011-2024 Thesys Inc. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Newsletter Spec — the component library a model fills

**Owners:** scribe fills the copy · blueprint owns this library, the renderer
and QA · wrench maintains any renderer script · the brand's approver (per
`about.md`) is the only one who approves a send.

This is the email library for the loop in
`agency/studio/creative/GENERATIVE-UI-SPECS.md`. It is adapted from openui's
44-component React Email library (`packages/react-email/src/library.ts`), cut
down to the 13 blocks a newsletter actually needs, with compliance, proof and
brand tokens added. The runbook is `NEWSLETTER-RUNBOOK.md`.

Spec files live at `agency/brands/<slug>/outputs/newsletter-<issue_id>.spec.json`.

## 1. Root: `newsletter`

```json
{
  "spec_version": "newsletter-spec@1",
  "meta":   { "...": "issue facts, status, sources" },
  "theme":  { "...": "brand-pack tokens, email-safe fonts" },
  "blocks": [ { "id": "b01", "type": "header", "props": { } } ]
}
```

| `meta` field | Rule |
|---|---|
| `brand_slug` | Must equal the brand folder name. |
| `issue_id` | `YYYY-MM-DD-short-slug`; used in file names and UTM `utm_campaign`. |
| `subject` | ≤ 60 characters recommended (hard max 90). No ALL CAPS, no "Re:"/"Fwd:" tricks. |
| `preview_text` | 40–110 characters. Must add information, not repeat the subject. |
| `from_name` | The brand name as subscribers know it. |
| `status` | `draft` → `qa-passed` → `approved`. Agents set only `draft` / `qa-passed`. |
| `approved_by`, `approved_at` | `null` until the approver named in `about.md` signs off. |
| `primary_cta_href` | The one action this issue exists for. At least one `button`/`article`/`product` must link to it. |
| `sources[]` | `{ "id": "s1", "claim": "...", "source": "path or URL in the brand folder" }`. Every price, stat, date, quote and offer in `blocks` points at one of these by `source_ref`. |
| `ai_assistance` | One line: what the model did (e.g. "copy drafted by scribe model, human edited"). |

## 2. Theme = brand-pack tokens

Filled from `brand-style.md` (or the brand pack's `tokens.css`) — never
invented. Fonts must be **email-safe stacks**; web fonts are not relied on.

| Token | Example | Used for |
|---|---|---|
| `bg` | `#FFF8EE` | page background (outer table) |
| `surface` | `#FFFFFF` | 600px content column |
| `text` / `muted` | `#1A1A1A` / `#555555` | body copy / captions, footer |
| `accent` / `accent_text` | `#B3261E` / `#FFFFFF` | buttons, kickers, links |
| `font_heading` / `font_body` | `Georgia, 'Times New Roman', serif` / `Arial, Helvetica, sans-serif` | |
| `width` | `600` | content width in px (fixed: 600) |

Contrast rule: `accent_text` on `accent` and `text` on `surface` must be ≥
4.5:1. Check with any WCAG contrast tool before promoting a theme.

## 3. Blocks (the component catalog)

Every block is `{ "id": "b01", "type": "<type>", "props": { ... } }`. `id`s are
unique and stable across edits (see "Edits are patches" in
GENERATIVE-UI-SPECS.md). Text fields are **plain text** except `text.paragraphs`,
which allows exactly two inline marks: `**bold**` and `[label](https://…)`.

| Group | `type` | Props (`?` = optional) | Placement / limits | Openui origin |
|---|---|---|---|---|
| Structure | `header` | `logo_src`, `logo_alt`, `logo_width` (≤ 300), `href` | First block, exactly once | `EmailHeaderSideNav/CenteredNav` (nav links dropped) |
| Structure | `divider` | — | Between sections; never two in a row | `EmailDivider` |
| Structure | `columns` | `columns[]`: 2 arrays of leaf blocks (`image`, `heading`, `text`, `button`) | Max 2 columns; stacks on mobile | `EmailColumns/Column` |
| Content | `hero` | `image_src?`, `image_alt?` (required if image), `kicker?` (≤ 24), `headline` (≤ 70), `dek?` (≤ 160) | At most one, right after header | new (from `EmailArticle`) |
| Content | `heading` | `text` (≤ 80), `level` (`1`\|`2`) | One `level: 1` per issue max | `EmailHeading` |
| Content | `text` | `paragraphs[]` (each ≤ 600 chars) | — | `EmailText` + limited `EmailMarkdown` |
| Content | `image` | `src`, `alt`, `width` (≤ 600), `href?`, `caption?`, `credit?` | — | `EmailImage` |
| Content | `button` | `label` (≤ 30, verb-first), `href`, `align` (`left`\|`center`) | — | `EmailButton` (bulletproof table button) |
| Content | `article` | `image_src?`, `image_alt?`, `kicker?`, `title` (≤ 90), `summary` (≤ 280), `cta_label`, `cta_href` | One per linked story | `EmailArticle` |
| Proof | `product` | `image_src`, `image_alt`, `name`, `description` (≤ 200), `price`, `cta_label`, `cta_href`, `source_ref` | Price must match `offers.md` / source exactly | `EmailProductCard` |
| Proof | `stats` | `items[]` 1–3 of `{ value, label, source_ref }` | No stat without a source | `EmailStats/StatItem` |
| Proof | `quote` | `quote` (≤ 280), `attribution`, `source_ref` | Approved testimonial/quote only, verbatim | `EmailTestimonial` (avatar dropped) |
| Proof | `list` | `title?`, `numbered` (bool), `items[]` 2–7 of `{ title, body? }` | — | `EmailList`, `EmailNumberedSteps` |
| Footer | `footer` | `org_name`, `postal_address`, `reason` (why they get this email), `unsubscribe_href` = `"{{UNSUBSCRIBE_URL}}"`, `preferences_href?` = `"{{PREFERENCES_URL}}"`, `social[]?` of `{ label, href }` | **Last block, exactly once. Required.** | `EmailFooterCentered` + compliance fields openui lacks |

Not in this library on purpose (openui has them): pricing cards, checkout
tables, customer-review bars, survey ratings, bento grids, avatar stacks, code
blocks, nav links. They serve transactional or SaaS email, not a brand
newsletter. Add one only through the "adding a block" steps in §7.

### Merge tags

The spec uses neutral placeholders; the human who imports the HTML into the
ESP maps them to that ESP's syntax (record the mapping once in the brand's
`distribution.md`):

| Placeholder | Meaning |
|---|---|
| `{{UNSUBSCRIBE_URL}}` | one-click unsubscribe link (required) |
| `{{PREFERENCES_URL}}` | manage-preferences link (optional) |
| `{{VIEW_IN_BROWSER_URL}}` | hosted copy (optional; renderer adds a top link if present in `meta.view_in_browser: true`) |

Never put a real subscriber's name, email or personal data in a spec.

## 4. JSON Schema (validator contract)

Draft 2020-12. Keep in sync with §1–3 in the same commit. Blocks dispatch on
`type` with `if/then` (not `oneOf`) so every error names the exact block and
field — `oneOf` only says "not valid under any schema", which gives the
repair step nothing to fix. An unknown `type` fails the `enum` (code
`unknown-component`).

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "newsletter-spec@1",
  "type": "object",
  "additionalProperties": false,
  "required": ["spec_version", "meta", "theme", "blocks"],
  "properties": {
    "spec_version": { "const": "newsletter-spec@1" },
    "meta": {
      "type": "object",
      "additionalProperties": false,
      "required": ["brand_slug", "issue_id", "subject", "preview_text", "from_name", "status", "approved_by", "approved_at", "primary_cta_href", "sources", "ai_assistance"],
      "properties": {
        "brand_slug": { "type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$" },
        "issue_id": { "type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}-[a-z0-9-]+$" },
        "subject": { "type": "string", "minLength": 5, "maxLength": 90 },
        "preview_text": { "type": "string", "minLength": 40, "maxLength": 110 },
        "from_name": { "type": "string", "minLength": 1, "maxLength": 60 },
        "status": { "enum": ["draft", "qa-passed", "approved"] },
        "approved_by": { "type": ["string", "null"] },
        "approved_at": { "type": ["string", "null"] },
        "primary_cta_href": { "$ref": "#/$defs/url" },
        "view_in_browser": { "type": "boolean" },
        "ai_assistance": { "type": "string" },
        "sources": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": ["id", "claim", "source"],
            "properties": {
              "id": { "type": "string", "pattern": "^s[0-9]+$" },
              "claim": { "type": "string" },
              "source": { "type": "string", "minLength": 3 }
            }
          }
        }
      }
    },
    "theme": {
      "type": "object",
      "additionalProperties": false,
      "required": ["bg", "surface", "text", "muted", "accent", "accent_text", "font_heading", "font_body", "width"],
      "properties": {
        "bg": { "$ref": "#/$defs/hex" }, "surface": { "$ref": "#/$defs/hex" },
        "text": { "$ref": "#/$defs/hex" }, "muted": { "$ref": "#/$defs/hex" },
        "accent": { "$ref": "#/$defs/hex" }, "accent_text": { "$ref": "#/$defs/hex" },
        "font_heading": { "type": "string" }, "font_body": { "type": "string" },
        "width": { "const": 600 }
      }
    },
    "blocks": { "type": "array", "minItems": 3, "items": { "$ref": "#/$defs/block" } }
  },
  "$defs": {
    "hex": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" },
    "url": { "type": "string", "pattern": "^https://" },
    "img": { "type": "string", "pattern": "^https://" },
    "srcref": { "type": "string", "pattern": "^s[0-9]+$" },
    "id": { "type": "string", "pattern": "^[a-z0-9_-]{1,32}$" },
    "leaf": {
      "type": "object", "required": ["id", "type", "props"],
      "properties": { "type": { "enum": ["image", "heading", "text", "button"] } },
      "allOf": [
        { "if": { "properties": { "type": { "const": "image" } } }, "then": { "$ref": "#/$defs/b_image" } },
        { "if": { "properties": { "type": { "const": "heading" } } }, "then": { "$ref": "#/$defs/b_heading" } },
        { "if": { "properties": { "type": { "const": "text" } } }, "then": { "$ref": "#/$defs/b_text" } },
        { "if": { "properties": { "type": { "const": "button" } } }, "then": { "$ref": "#/$defs/b_button" } }
      ]
    },
    "block": {
      "type": "object", "required": ["id", "type", "props"],
      "properties": { "type": { "enum": ["header", "divider", "columns", "hero", "heading", "text", "image", "button", "article", "product", "stats", "quote", "list", "footer"] } },
      "allOf": [
        { "if": { "properties": { "type": { "const": "header" } } }, "then": { "$ref": "#/$defs/b_header" } },
        { "if": { "properties": { "type": { "const": "divider" } } }, "then": { "$ref": "#/$defs/b_divider" } },
        { "if": { "properties": { "type": { "const": "columns" } } }, "then": { "$ref": "#/$defs/b_columns" } },
        { "if": { "properties": { "type": { "const": "hero" } } }, "then": { "$ref": "#/$defs/b_hero" } },
        { "if": { "properties": { "type": { "const": "heading" } } }, "then": { "$ref": "#/$defs/b_heading" } },
        { "if": { "properties": { "type": { "const": "text" } } }, "then": { "$ref": "#/$defs/b_text" } },
        { "if": { "properties": { "type": { "const": "image" } } }, "then": { "$ref": "#/$defs/b_image" } },
        { "if": { "properties": { "type": { "const": "button" } } }, "then": { "$ref": "#/$defs/b_button" } },
        { "if": { "properties": { "type": { "const": "article" } } }, "then": { "$ref": "#/$defs/b_article" } },
        { "if": { "properties": { "type": { "const": "product" } } }, "then": { "$ref": "#/$defs/b_product" } },
        { "if": { "properties": { "type": { "const": "stats" } } }, "then": { "$ref": "#/$defs/b_stats" } },
        { "if": { "properties": { "type": { "const": "quote" } } }, "then": { "$ref": "#/$defs/b_quote" } },
        { "if": { "properties": { "type": { "const": "list" } } }, "then": { "$ref": "#/$defs/b_list" } },
        { "if": { "properties": { "type": { "const": "footer" } } }, "then": { "$ref": "#/$defs/b_footer" } }
      ]
    },
    "b_header": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "header" },
      "props": { "type": "object", "additionalProperties": false, "required": ["logo_src", "logo_alt", "logo_width", "href"], "properties": {
        "logo_src": { "$ref": "#/$defs/img" }, "logo_alt": { "type": "string", "minLength": 2 },
        "logo_width": { "type": "integer", "minimum": 60, "maximum": 300 }, "href": { "$ref": "#/$defs/url" } } } } },
    "b_divider": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "divider" },
      "props": { "type": "object", "additionalProperties": false, "maxProperties": 0 } } },
    "b_columns": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "columns" },
      "props": { "type": "object", "additionalProperties": false, "required": ["columns"], "properties": {
        "columns": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "array", "minItems": 1, "items": { "$ref": "#/$defs/leaf" } } } } } } },
    "b_hero": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "hero" },
      "props": { "type": "object", "additionalProperties": false, "required": ["headline"], "dependentRequired": { "image_src": ["image_alt"] }, "properties": {
        "image_src": { "$ref": "#/$defs/img" }, "image_alt": { "type": "string", "minLength": 5 },
        "kicker": { "type": "string", "maxLength": 24 }, "headline": { "type": "string", "maxLength": 70 },
        "dek": { "type": "string", "maxLength": 160 } } } } },
    "b_heading": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "heading" },
      "props": { "type": "object", "additionalProperties": false, "required": ["text", "level"], "properties": {
        "text": { "type": "string", "maxLength": 80 }, "level": { "enum": [1, 2] } } } } },
    "b_text": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "text" },
      "props": { "type": "object", "additionalProperties": false, "required": ["paragraphs"], "properties": {
        "paragraphs": { "type": "array", "minItems": 1, "items": { "type": "string", "minLength": 1, "maxLength": 600 } } } } } },
    "b_image": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "image" },
      "props": { "type": "object", "additionalProperties": false, "required": ["src", "alt", "width"], "properties": {
        "src": { "$ref": "#/$defs/img" }, "alt": { "type": "string", "minLength": 5 },
        "width": { "type": "integer", "minimum": 40, "maximum": 600 }, "href": { "$ref": "#/$defs/url" },
        "caption": { "type": "string", "maxLength": 160 }, "credit": { "type": "string", "maxLength": 80 } } } } },
    "b_button": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "button" },
      "props": { "type": "object", "additionalProperties": false, "required": ["label", "href", "align"], "properties": {
        "label": { "type": "string", "minLength": 2, "maxLength": 30 }, "href": { "$ref": "#/$defs/url" },
        "align": { "enum": ["left", "center"] } } } } },
    "b_article": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "article" },
      "props": { "type": "object", "additionalProperties": false, "required": ["title", "summary", "cta_label", "cta_href"], "dependentRequired": { "image_src": ["image_alt"] }, "properties": {
        "image_src": { "$ref": "#/$defs/img" }, "image_alt": { "type": "string", "minLength": 5 },
        "kicker": { "type": "string", "maxLength": 24 }, "title": { "type": "string", "maxLength": 90 },
        "summary": { "type": "string", "maxLength": 280 }, "cta_label": { "type": "string", "maxLength": 30 },
        "cta_href": { "$ref": "#/$defs/url" } } } } },
    "b_product": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "product" },
      "props": { "type": "object", "additionalProperties": false, "required": ["image_src", "image_alt", "name", "description", "price", "cta_label", "cta_href", "source_ref"], "properties": {
        "image_src": { "$ref": "#/$defs/img" }, "image_alt": { "type": "string", "minLength": 5 },
        "name": { "type": "string", "maxLength": 60 }, "description": { "type": "string", "maxLength": 200 },
        "price": { "type": "string", "maxLength": 40 }, "cta_label": { "type": "string", "maxLength": 30 },
        "cta_href": { "$ref": "#/$defs/url" }, "source_ref": { "$ref": "#/$defs/srcref" } } } } },
    "b_stats": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "stats" },
      "props": { "type": "object", "additionalProperties": false, "required": ["items"], "properties": {
        "items": { "type": "array", "minItems": 1, "maxItems": 3, "items": { "type": "object", "additionalProperties": false, "required": ["value", "label", "source_ref"], "properties": {
          "value": { "type": "string", "maxLength": 12 }, "label": { "type": "string", "maxLength": 40 }, "source_ref": { "$ref": "#/$defs/srcref" } } } } } } } },
    "b_quote": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "quote" },
      "props": { "type": "object", "additionalProperties": false, "required": ["quote", "attribution", "source_ref"], "properties": {
        "quote": { "type": "string", "maxLength": 280 }, "attribution": { "type": "string", "maxLength": 80 },
        "source_ref": { "$ref": "#/$defs/srcref" } } } } },
    "b_list": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "list" },
      "props": { "type": "object", "additionalProperties": false, "required": ["numbered", "items"], "properties": {
        "title": { "type": "string", "maxLength": 80 }, "numbered": { "type": "boolean" },
        "items": { "type": "array", "minItems": 2, "maxItems": 7, "items": { "type": "object", "additionalProperties": false, "required": ["title"], "properties": {
          "title": { "type": "string", "maxLength": 80 }, "body": { "type": "string", "maxLength": 240 } } } } } } } },
    "b_footer": { "type": "object", "additionalProperties": false, "required": ["id", "type", "props"], "properties": {
      "id": { "$ref": "#/$defs/id" }, "type": { "const": "footer" },
      "props": { "type": "object", "additionalProperties": false, "required": ["org_name", "postal_address", "reason", "unsubscribe_href"], "properties": {
        "org_name": { "type": "string" }, "postal_address": { "type": "string", "minLength": 10 },
        "reason": { "type": "string", "minLength": 10, "maxLength": 200 },
        "unsubscribe_href": { "const": "{{UNSUBSCRIBE_URL}}" },
        "preferences_href": { "const": "{{PREFERENCES_URL}}" },
        "social": { "type": "array", "maxItems": 5, "items": { "type": "object", "additionalProperties": false, "required": ["label", "href"], "properties": {
          "label": { "type": "string" }, "href": { "$ref": "#/$defs/url" } } } } } } } }
  }
}
```

### Business rules (checked after the schema; the schema can't express them)

| Code | Rule |
|---|---|
| `B1 header-first` | `blocks[0].type == "header"`. |
| `B2 footer-last` | Exactly one `footer`, and it is the last block. |
| `B3 unique-ids` | Every block `id` (including inside `columns`) is unique. |
| `B4 primary-cta` | At least one `button.href` / `article.cta_href` / `product.cta_href` equals `meta.primary_cta_href`. |
| `B5 cta-budget` | ≤ 3 distinct CTA destinations per issue (one primary + up to two secondary). |
| `B6 sources-resolve` | Every `source_ref` matches a `meta.sources[].id`, and every source path exists in the brand folder or is a public URL. |
| `B7 facts-match` | Every `product.price` appears verbatim in `offers.md` or the cited source. |
| `B7b prose-claims` | (human/QA check) Every factual sentence in `text`, `hero`, `list` and `article` copy — dates, hours, ingredients, backstory ("we tested this for a month") — traces to a `meta.sources` entry. Models embellish; the schema can't see it. |
| `B8 no-verify-tags` | No `[VERIFY]`, `TODO`, `lorem`, `ipsum` or `example.com` in any string. |
| `B9 no-placeholder-media` | No image `src` / `*_src` or link `href` on a placeholder host (`picsum.photos`, `placehold.co`, `via.placeholder.com`, `unsplash.it`, AI-stock generators). Check URL fields only, not prose. Images come from the brand pack / brand-hosted URLs. |
| `B10 one-h1` | At most one `heading.level == 1` (the `hero.headline` counts as the H1 when present). |
| `B11 no-double-divider` | Never two `divider` blocks in a row. |

## 5. Render contract — email-safe HTML (or MJML)

The renderer is deterministic: spec + theme in, one HTML file out. It may be a
wrench-maintained template script, MJML, or an agent hand-rendering with the
snippets below — the output rules are identical.

### Document rules (all renderers)

1. `<!DOCTYPE html>`, `<html lang="en">`, `<meta charset="utf-8">`,
   `<meta name="viewport" content="width=device-width, initial-scale=1">`,
   `<meta name="color-scheme" content="light">`, `<title>` = `meta.subject`.
2. **Layout is tables.** Outer `<table role="presentation" width="100%">` with
   `bgcolor = theme.bg`; inner centered `<table role="presentation"
   width="600">` with `bgcolor = theme.surface`. Every layout table has
   `role="presentation" cellpadding="0" cellspacing="0" border="0"`. No
   `<div>`-based layout, no flexbox, no grid, no `position`.
3. **Styles inline** on each element. The only `<style>` block allowed is in
   `<head>` for a mobile media query (`@media (max-width:620px)`) and link
   color resets — the email must still read correctly if the client strips it.
4. **Preheader** = `meta.preview_text` in a hidden block as the first child of
   `<body>`:
   `<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">…</div>`.
   (Openui's `EmailTemplate` accepts `previewText` but its component never
   renders it — don't repeat that bug.)
5. **Forbidden anywhere:** `<script>`, `<form>`, `<input>`, `<iframe>`,
   `<object>`, `<embed>`, `<video>`, `<svg>`, `<link rel="stylesheet">`,
   `@import`, `on*=` event attributes, `javascript:` URLs, CSS
   `background-image` as the only carrier of content.
6. **Images:** absolute `https://` `src`, `width` attribute (px, no unit),
   `alt` always present, `style="display:block;border:0;outline:none;
   max-width:100%;height:auto;"`. Text must not live inside images.
7. **Links:** absolute `https://` (or the merge-tag placeholders). Add
   `utm_source=newsletter&utm_medium=email&utm_campaign=<issue_id>` to
   links on the brand's own domain (not to social or third-party links):
   start with `?` if the URL has no query, `&` if it does, and insert
   before any `#fragment` (`/menu?utm_…#item`, never `/menu#item?utm_…`).
   Write `&` as `&amp;` inside `href`.
8. **Escaping:** every text prop is HTML-escaped (`&`, `<`, `>`, `"`). Only
   the two inline marks in `text.paragraphs` become `<strong>` / `<a>`.
9. **Size:** final HTML < 100 KB (Gmail clips longer messages).

### Block → HTML snippets

`T` = theme. Each snippet is one `<tr>` inside the 600px table.

| Block | HTML (inline styles abbreviated only where marked `…`) | MJML equivalent |
|---|---|---|
| `header` | `<tr><td align="center" style="padding:24px 32px;"><a href="{href}"><img src="{logo_src}" width="{logo_width}" alt="{logo_alt}" style="display:block;border:0;…"></a></td></tr>` | `mj-image` |
| `hero` | optional `<img … width="600">` row, then `<td style="padding:24px 32px 8px;font-family:{T.font_heading};">` with kicker `<p>` in `T.accent`, 12px uppercase; headline `<h1 style="margin:0;font-size:30px;line-height:36px;color:{T.text};">`; dek `<p>` 17px `T.muted` | `mj-image` + `mj-text` |
| `heading` | `<h1>`/`<h2>` inside `<td style="padding:8px 32px;">`; level 1 = 28px, level 2 = 22px, `T.font_heading`, `T.text` | `mj-text` |
| `text` | one `<p style="margin:0 0 16px;font-family:{T.font_body};font-size:16px;line-height:24px;color:{T.text};">` per paragraph, in `<td style="padding:0 32px;">` | `mj-text` |
| `image` | `<td align="center" style="padding:8px 32px;">` + optional `<a>` + `<img>`; caption/credit as 13px `T.muted` `<p>` | `mj-image` |
| `button` (bulletproof) | `<td align="{align}" style="padding:8px 32px 24px;"><table role="presentation" …><tr><td bgcolor="{T.accent}" style="border-radius:6px;"><a href="{href}" style="display:inline-block;padding:14px 28px;font-family:{T.font_body};font-size:16px;font-weight:bold;color:{T.accent_text};text-decoration:none;border-radius:6px;">{label}</a></td></tr></table></td>` | `mj-button` |
| `article` | image row (if any) + kicker + `<h2>` title + summary `<p>` + button snippet with `cta_*` | `mj-image` + `mj-text` + `mj-button` |
| `product` | 2-cell row: image 200px left, name/description/price (bold)/button right; stacks on mobile via media query class | `mj-section` > 2 × `mj-column` |
| `stats` | nested table, one `<td width="{600/n}%" align="center">` per item: value 28px bold `T.accent`, label 13px `T.muted` | `mj-section` > n × `mj-column` |
| `quote` | `<td style="padding:16px 32px;border-left:4px solid {T.accent};">` quote in 18px italic, attribution 14px `T.muted` prefixed "— " | `mj-text` |
| `list` | `<table>` rows: marker cell (number or "•", `T.accent`, 32px wide) + title (bold) + body | `mj-text` |
| `columns` | nested 2-cell table, each `<td width="50%" valign="top">`, leaf snippets inside; class for mobile stacking | `mj-section` > 2 × `mj-column` |
| `divider` | `<td style="padding:8px 32px;"><table role="presentation" width="100%"><tr><td style="border-top:1px solid {T.muted};font-size:0;line-height:0;">&nbsp;</td></tr></table></td>` | `mj-divider` |
| `footer` | `<td align="center" style="padding:24px 32px;font-family:{T.font_body};font-size:12px;line-height:18px;color:{T.muted};">` org name, postal address, reason, social text links, then `<a href="{{UNSUBSCRIBE_URL}}">Unsubscribe</a>` (+ ` · <a href="{{PREFERENCES_URL}}">Manage preferences</a>`) | `mj-text` |

## 6. Example spec (valid)

The minimal valid example is the appendix of `NEWSLETTER-RUNBOOK.md`; copy its
shape, never its content. Once a brand's first issue is approved, that spec
(in `agency/brands/<slug>/outputs/`) becomes the brand's few-shot example.

## 7. Adding or changing a block

1. Write the row in §3 (type, props with limits, placement, why it exists).
2. Add its `$defs/b_<type>` to the schema in §4 and to `block.oneOf`.
3. Add its render snippet in §5.
4. Add or update one valid example that uses it; run the validator on it.
5. Bump `spec_version` only for breaking changes (renamed/removed props).
   Old specs keep rendering against the old version — never silently mutate.
