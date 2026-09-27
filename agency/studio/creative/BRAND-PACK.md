<!-- Source: cgallic/visual-factory-kit (https://github.com/cgallic/visual-factory-kit) — MIT, Copyright (c) 2026 Visual Factory Kit contributors. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Brand Pack

## What a brand pack is

A **brand pack** is the client's brand system expressed as files the engine can
render: `brand.json` (tokens, logo roles, fonts, allowed templates, source
provenance), `tokens.css` (the palette as CSS variables), and `assets/`
(transparent logos, brand visuals, mascot or product art).

One pack per brand surface. A client with distinct identities (site, podcast,
campaign) gets separate packs — the engine rejects cross-surface fallback, so
colors, fonts, and logos can never leak between identities.

## What goes in a brand pack

| Item | Where it lives | Rules |
|---|---|---|
| **Brand identity** | `brand.json`: name, variant key, allowed templates, canonical/provenance URLs | The variant key is required on every render request and must match the pack exactly. Older packs only render when explicitly named — never as implicit fallback. |
| **Palette** | `tokens.css`: named CSS color tokens (e.g. `--brand-primary`) | Real brand colors, with enough contrast for small mobile previews. |
| **Logo (typed)** | `assets/` + `brand.json`: role (primary/icon/wordmark), color mode (light/dark/mono), orientation | Transparent PNG. No baked-in white backgrounds, no circular badge wrappers around transparent assets, no low-resolution logos. |
| **Brand visuals** | `assets/` + `brand.json`: typed imagery — mascot, product art, portrait, photography | Approved, real brand art. No generic AI imagery. |
| **Fonts** | `brand.json`: each family with local font file, weight, style, format, and **license** | Fonts are third-party assets under their own licenses — the license must be declared per font. |
| **Voice notes** | `brand.json` / sidecar: tone rules that shape CTA and headline wording | Voice informs *copy choices*, not layout. See "How the brand folder feeds it" below. |
| **Default CTA / contact** | `brand.json`: phone number, CTA label | Only if the client actually uses one. |
| **Source provenance** | `brand.json`: Figma or canonical URLs, asset origin | Every asset's origin is recorded so claims and art can be audited later. |

**Avoid:** low-resolution logos, baked-in white backgrounds, circular badge
wrappers around transparent assets, generic AI art, proof claims without a
source file.

## How the active brand folder (`agency/brands/<slug>/`) feeds it

The brand folder is the **source of truth**; the brand pack is a
**render-time compilation** of it. The pack never holds the brand strategy —
it holds only what the renderer needs.

```
agency/brands/<slug>/                    brand pack (render input)
─────────────────────                    ─────────────────────────
brand-style.md      ──colors, type,──────▶  tokens.css, fonts in brand.json
                     │  logo usage
brand-voice.md      ──tone, CTA rules───▶  voice notes, default CTA
audience.md         ──who it's for───────▶  (informs family choice, not the pack)
offers.md           ──what's on sale────▶  offer-stack family slots
goals.md            ──what matters──────▶  proof priorities
learnings.md        ──what performed────▶  which families to keep/retire
```

Rules:

1. **Edits happen in the brand folder, never directly in the pack.**
   Changing a color means updating `brand-style.md` and recompiling the pack —
   not hand-editing `tokens.css`. The folder is the record; the pack is the build.
2. **One pack per surface.** If `gator-bait-media` needs both a site identity and
   a show identity, they are two packs with two variant keys. Render requests name
   the key explicitly.
3. **Recompiling is cheap; drifting is expensive.** After any brand-folder change
   that affects colors, fonts, logos, or voice, regenerate the pack and re-render
   the brand's family reference set (see `TEMPLATE-FAMILIES.md`) so QA catches
   breakage before production creative.
4. **No secrets in the pack.** Placeholders only — never credentials, API keys,
   emails, or personal data in `brand.json`, `tokens.css`, or assets.

## Creating a pack for a new client

1. Copy the `_template` brand folder to `agency/brands/<new-slug>/` and fill in
   the six docs (audience, style, voice, goals, learnings, offers).
2. Gather the brand assets: transparent logo PNGs, brand visuals, licensed font
   files. Verify every font's license and record it.
3. Write `tokens.css` from the palette in `brand-style.md`.
4. Write `brand.json`: variant key, tokens path, logo roles, font declarations
   with licenses, allowed templates (start with the client's approved families),
   source provenance URLs.
5. Render the family's reference set against the new pack. Ship only when QA
   passes on every size.

## Reference

- `README.md` — what the creative engine is
- `TEMPLATE-FAMILIES.md` — defining families for a client brand
- `QA-PROVENANCE.md` — QA and provenance pattern
- Source: [visual-factory-kit](https://github.com/cgallic/visual-factory-kit) — MIT
