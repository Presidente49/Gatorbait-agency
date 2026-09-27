<!-- Source: thesysdev/openui (https://github.com/thesysdev/openui) — MIT, Copyright (c) 2011-2024 Thesys Inc. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Newsletter Runbook — brief → spec → email-safe HTML → human approval

**Trigger:** "write the newsletter", "draft this month's email", a scheduled
newsletter task from the controller.
**Owners:** scribe (steps 1–4) · blueprint (steps 5–8) · the approver named in
the brand's `about.md` (step 9). **No step in this runbook sends email.**

Library + schema + render rules: `NEWSLETTER-SPEC.md`.
Why it works this way: `agency/studio/creative/GENERATIVE-UI-SPECS.md`.

## 0. Preconditions — stop if any is missing

- [ ] `agency/brands/<slug>/about.md` names who approves **Email sends**.
- [ ] `about.md` has a **postal address** (needed in every footer). No address
      → stop and ask the owner; do not invent one.
- [ ] `brand-voice.md`, `audience.md`, `offers.md`, `brand-style.md` are filled
      (not template text). `newsletter-voice.md` exists — if not, run
      `agency/skills-library/newsletter-voice.md` first.
- [ ] A hosted logo URL (https) and any photos you plan to use are in the
      brand pack or on the brand's own site.
- [ ] `distribution.md` names the ESP and list. You will not touch the ESP.

## 1. Write the brief (scribe, 5 minutes)

In `outputs/newsletter-<issue_id>.brief.md`, answer:

1. **The one action** this issue exists for → becomes `meta.primary_cta_href`
   (must be a link from `offers.md` or the brand site).
2. **2–4 things worth saying** (new item, event, story, tip), each with its
   fact source (file path in the brand folder or public URL).
3. **Archetype / section flow** from `newsletter-voice.md`.
4. Anything the owner said must or must not appear.

## 2. Collect sources

List every fact the issue will state — prices, dates, hours, stats, quotes —
as `meta.sources[]`: `{ "id": "s1", "claim": "...", "source": "outputs/menu-2026-09.md" }`.
If a fact has no source, it doesn't go in. If you think it's true but can't
find it, write it as `[VERIFY] …` — the validator will block the render until
a human resolves it.

## 3. Fill the spec (scribe + model)

Give the model, in this order:

1. §1–§3 and the business rules of `NEWSLETTER-SPEC.md` (the library);
2. the brand's `brand-voice.md`, `newsletter-voice.md`, `offers.md`,
   `brand-style.md`, and the brief + sources from steps 1–2;
3. one valid example spec (the brand's last approved issue; for a new brand,
   the minimal example in §Appendix below);
4. this instruction:

> Return one JSON object that validates against newsletter-spec@1. Use only
> the block types in the library. Write block order first (header → body →
> footer), then fill props. Every price, stat, date or quote must carry a
> `source_ref` from meta.sources. Do not invent numbers, testimonials, images
> or URLs — if something is missing, write "[VERIFY] <what is missing>".
> Set status to "draft", approved_by and approved_at to null. Output JSON only.

Save as `outputs/newsletter-<issue_id>.spec.json`.

Theme values are **copied** from `brand-style.md` / brand pack, never chosen by
the model. If the model changes a theme value, overwrite it with the brand's.

## 4. Validate (scribe) — three layers, every error coded

1. **Parse:** the file is valid JSON (`python3 -m json.tool file.json` or
   `jq . file.json`).
2. **Schema:** validate against the §4 schema with any JSON Schema 2020-12
   validator (e.g. Python `jsonschema`, `ajv-cli`) — whatever the brand's
   environment already has; don't install globally for one run. Record errors
   as `unknown-component`, `missing-required`, `excess-prop`, `bad-enum`,
   `too-long`, `bad-pattern`.
3. **Business rules** B1–B11 (plus the human B7b read in step 7) from `NEWSLETTER-SPEC.md` — check by script or by
   hand against the list. B6/B7 (sources resolve, prices match `offers.md`)
   are never skipped.

## 5. Repair (max 2 rounds)

Send the model its spec + the coded error list:

> Fix only these errors and return the full corrected spec. Do not change any
> block that has no error.

Re-run step 4. After 2 failed rounds, stop: a human edits the spec. Log the
recurring error in the brand's `learnings.md`; if it recurs across brands, add
one rule to the library (see GENERATIVE-UI-SPECS.md, "Rules").

## 6. Render (blueprint)

Render the valid spec to `outputs/newsletter-<issue_id>.html` using the §5
render contract — the brand's renderer script if wrench has built one, MJML
via the block→MJML mapping, or by hand with the block snippets. Never
hand-edit the HTML afterwards: fix the spec and re-render.

## 7. QA gate (blueprint) — write `outputs/newsletter-<issue_id>.qa.md`

Automated/grep checks (each must pass):

- [ ] No `<script`, `<form`, `<iframe`, `<object`, `<embed`, `<svg`, `<video`,
      `<link rel="stylesheet"`, `@import`, ` on[a-z]+=`, `javascript:`.
- [ ] Layout uses `<table role="presentation"`; content width 600.
- [ ] Every `<img` has a non-empty `alt=` and a `width=`.
- [ ] `{{UNSUBSCRIBE_URL}}` appears exactly in the footer link; the postal
      address appears in the footer.
- [ ] Preheader text present and equals `meta.preview_text`; `<title>` equals
      `meta.subject`.
- [ ] All `href`/`src` are `https://` or merge-tag placeholders.
- [ ] Own-domain links carry `utm_campaign=<issue_id>`.
- [ ] File size < 100 KB.
- [ ] No `[VERIFY]`, `TODO`, `lorem`, placeholder-image hosts.

Human-eye checks (blueprint, then the approver):

- [ ] Reads correctly with images off (alt text carries the message).
- [ ] Mobile preview (≤ 400px wide): nothing cut off, buttons tappable.
- [ ] Contrast of button text and body text ≥ 4.5:1.
- [ ] Every price/date matches `offers.md` / the cited source today.
- [ ] **B7b:** read every sentence of body copy and strike any fact or
      backstory not in `meta.sources` (models add color like "we tested it
      for a month" — that is an invented claim, not voice).
- [ ] Voice matches `newsletter-voice.md`; passes
      `agency/skills-library/marketing/quality-gate.md`.
- [ ] Client inbox test: the **approver** (or wrench, on the approver's
      instruction) sends a *test* from the ESP to internal addresses and checks
      Gmail web, Gmail mobile, Apple Mail and Outlook desktop. Agents do not
      trigger test sends on their own.

All automated checks pass → agent sets `meta.status` to `qa-passed` and
re-renders nothing (status doesn't change the HTML).

## 8. Hand to the approver

Post the spec, the HTML, the QA file and a 3-line summary (subject, the one
action, sources used) to the approval path in `about.md`. Say explicitly:
"Draft — not scheduled, not sent."

## 9. Approval and send (human only)

The approver sets `approved_by` / `approved_at` in the spec (or tells the
agent to record it), imports the HTML into the ESP, maps the merge-tag
placeholders to the ESP's syntax, and schedules or sends. An approval covers
**this issue to this list** only — not future issues, not other lists.

## 10. Learn

After the send, when the ESP shows results (48–72h): record opens (treat as
directional — Apple Mail Privacy inflates them), clicks on the primary CTA,
unsubscribes, and any orders/conversions attributed to `utm_campaign` in the
brand's `learnings.md`. Promote a pattern (block order, subject style, CTA
wording) to the brand's example spec only after it wins twice; transferable
lessons go to `agency/shared/learnings.md`.

## Appendix — minimal valid example (few-shot for a new brand)

Replace every value with the brand's own; keep the shape.

```json
{
  "spec_version": "newsletter-spec@1",
  "meta": {
    "brand_slug": "your-brand",
    "issue_id": "2026-10-01-launch",
    "subject": "Something new this week",
    "preview_text": "One sentence that adds information the subject line doesn't.",
    "from_name": "Your Brand",
    "status": "draft",
    "approved_by": null,
    "approved_at": null,
    "primary_cta_href": "https://your-brand.example/offer",
    "ai_assistance": "Copy drafted by scribe model from brief; human review pending.",
    "sources": [{ "id": "s1", "claim": "Offer details", "source": "offers.md" }]
  },
  "theme": {
    "bg": "#F4F4F4", "surface": "#FFFFFF", "text": "#1A1A1A", "muted": "#555555",
    "accent": "#1F3A2E", "accent_text": "#FFFFFF",
    "font_heading": "Georgia, 'Times New Roman', serif",
    "font_body": "Arial, Helvetica, sans-serif", "width": 600
  },
  "blocks": [
    { "id": "b01", "type": "header", "props": { "logo_src": "https://your-brand.example/logo.png", "logo_alt": "Your Brand", "logo_width": 180, "href": "https://your-brand.example" } },
    { "id": "b02", "type": "text", "props": { "paragraphs": ["One short paragraph in the brand's newsletter voice."] } },
    { "id": "b03", "type": "button", "props": { "label": "See the offer", "href": "https://your-brand.example/offer", "align": "center" } },
    { "id": "b04", "type": "footer", "props": { "org_name": "Your Brand", "postal_address": "Street, City, ST 00000", "reason": "You signed up for news from Your Brand.", "unsubscribe_href": "{{UNSUBSCRIBE_URL}}" } }
  ]
}
```
