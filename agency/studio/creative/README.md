<!-- Source: cgallic/visual-factory-kit (https://github.com/cgallic/visual-factory-kit) — MIT. Adapted for Gator Bait Agency. -->

# Creative Engine — Deterministic Branded Graphics

## What it is

The creative engine is a **deterministic image factory** for branded social creative.
Give it two inputs — a JSON creative request (the message) and a brand pack
(the brand system) — and it renders **platform-ready PNGs** for every surface the
agency posts to: social posts, ads, YouTube thumbnails, carousels, Stories, and
Reels covers.

It is not an AI image generator. Creative direction stays human (or
Blueprint-authored); the engine handles the mechanical part — correct dimensions,
brand tokens, text fit, and QA — so one approved message becomes every format
without being redesigned twenty times by hand.

## Inputs and outputs

```
┌──────────────────┐   ┌──────────────────┐        ┌───────────────────────┐
│  Request JSON    │ + │   Brand Pack     │  ──▶   │  platform PNGs +      │
│  (the message:   │   │  (brand.json,    │        │  provenance files +   │
│   headline,      │   │   tokens.css,    │        │  QA report            │
│   subhead, proof │   │   logos, fonts,  │        │                       │
│   label, CTA,    │   │   brand visuals) │        │                       │
│   alt text,      │   │                  │        │                       │
│   format list)   │   │                  │        │                       │
└──────────────────┘   └──────────────────┘        └───────────────────────┘
```

**Input 1 — Request JSON.** One file per creative job. Contains:

- `message`: `headline`, `subhead`, `proof_label` (+ `proof_source`), `cta`,
  `phone_number` where relevant
- `formats`: keys from the platform-size matrix
  (e.g. `instagram_reel`, `facebook_feed_square`, `pinterest_pin`,
  `google_business_post`, `linkedin_article_hero`, `x_post_landscape`,
  `youtube_thumbnail`)
- `output`: `alt_text` (required — accessibility), `destination_dir`,
  `filename_prefix`

**Input 2 — Brand pack.** The brand's design system as files: `brand.json`
(tokens, logo roles, font declarations, allowed templates, source provenance),
`tokens.css` (the palette as CSS variables), and `assets/` (transparent logos,
brand visuals, mascot/product art).

**Output.** For each format: a PNG at exact platform dimensions, a
`.provenance.json` sidecar (request ID, content ID, template, dimensions, brand
assets used, font stack, proof source, render timestamp, approval status), and
one request-level QA report. See `QA-PROVENANCE.md`.

## How it fits the agency

| Agency need | How the engine serves it |
|---|---|
| **Blueprint agent** (agency/agents/blueprint) | Blueprint authors the request JSON — headline, subhead, proof, CTA — from the client's messaging brief. It never draws anything by hand; it *specifies* creative. |
| **Brand folder → brand pack** | `agency/brands/<slug>/` (voice, style, audience docs) is the source of truth; the render-time pack is compiled from it. See `BRAND-PACK.md`. |
| **Multi-format publishing** | One request + one pack renders the full platform matrix: feed, story, reel cover, thumbnail, ad variants, OG card, blog header, carousel slides. |
| **Template families** | The engine ships a library of template families (one layout system × every platform size). New client brands get a new family instead of one-off designs. See `TEMPLATE-FAMILIES.md`. |
| **QC before publish** | Every render is gated by QA (exact dimensions, text overflow, mobile legibility, alt text, proof source, banned terms). Nothing ships on `"passed": false`. See `QA-PROVENANCE.md`. |

## Operating notes for the Blueprint agent

1. **One message, one request file.** Batch work by writing one request JSON per
   creative concept, then render the full format list from it. Reusing the same
   message block across families keeps copy consistent.
2. **Proof is mandatory, not decorative.** Every request that makes a claim
   carries `proof_label` *and* `proof_source`. QA fails renders whose proof
   source is missing — that is by design (claims, attribution, brand safety).
3. **Keep `output` honest.** `alt_text` must describe the actual graphic; it is a
   QA gate, not metadata decoration. Use `filename_prefix` per concept so
   provenance files stay traceable (`gatorbait-olemiss-recap-*`, not `img-01`).
4. **Text fit is automatic.** Templates measure text in-browser and
   shrink-to-fit before screenshot; do not pre-shrink copy. If QA reports
   overflow, shorten the message — do not override the fit.
5. **Do not vendor the harness here.** The Playwright render harness
   (`render.py`, template HTML, platform-size matrix, schemas) lives outside
   these runbooks. These docs describe *how to operate* the engine, not the code.

## Reference

- `TEMPLATE-FAMILIES.md` — the template-family concept; how to define one per client
- `BRAND-PACK.md` — what goes in a brand pack and how `agency/brands/<slug>/` feeds it
- `QA-PROVENANCE.md` — provenance sidecars and the publish QA checklist
- Source: [visual-factory-kit](https://github.com/cgallic/visual-factory-kit) — MIT
