<!-- Source: cgallic/visual-factory-kit (https://github.com/cgallic/visual-factory-kit) — MIT, Copyright (c) 2026 Visual Factory Kit contributors. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# QA + Provenance

## The pattern

**Every render gets two companions: a provenance file and a QA verdict.
Nothing publishes unless both exist and QA passes.**

- **Provenance** answers: *what exactly is this image, and where did it come
  from?*
- **QA** answers: *is it safe to publish?*

This is how the agency avoids "it looked fine on my screen" creative handoffs.

## Provenance: the `.provenance.json` sidecar

Every PNG the engine writes gets a `.provenance.json` sidecar with the same
filename prefix. It records:

| Field | Why it matters |
|---|---|
| `request_id` / `content_id` | Trace the image back to the creative brief that produced it |
| `template` (+ version, e.g. `gator-gameday-recap@v1`) | Know exactly which layout grammar rendered it |
| `dimensions` | The platform size actually rendered (not assumed) |
| `brand assets used` (with SHA-256 hashes) | Prove which logo/visual/font files went in — font, visual, logo, and token-file hashes |
| `brand catalog SHA-256` + `brand_variant_key` | Prove which pack and which identity variant |
| `font stack` | The type actually used |
| `proof source` | Where the claim on the graphic came from |
| `photo credit` | Photographer + source for every real photo (credit rules in the brand's `about.md`) |
| `render timestamp` | When it was produced |
| `AI assistance notes` | What (if anything) AI did in the loop |
| `approval status` | Who signed it off and when |

Older brand packs remain renderable when explicitly named (for legacy assets)
but are never selected as implicit fallback — and provenance always records
which pack version rendered the image, so a re-render from a stale pack is
visible in the record.

## QA: the publish gate

Each request writes one request-level QA report. The checks:

1. **Exact platform dimensions** — the PNG matches the format key's required size.
2. **Text overflow** — no headline, subhead, or CTA clipped or spilling its zone
   (templates shrink-to-fit; if overflow still fails, the copy is too long).
3. **Mobile preview readability** — legible at phone-thumbnail size, sufficient
   contrast.
4. **Alt text present** — required, descriptive, and accurate to the graphic.
5. **Proof source present** — any claim on the graphic has a recorded source.
6. **Provenance sidecar present** — no image without its record.
7. **Banned public-facing terms** — client-specific denylist honored
   (unapproved superlatives, competitor names, regulated claims, etc.).

**Gate rule:** publish only when the report says `"passed": true`. A failed
check is a work order, not a judgment call — fix the input (usually copy length,
alt text, or proof source) and re-render.

## The QA checklist before publish

For every creative job, before anything ships to a platform, confirm:

- [ ] QA report exists and `"passed": true` for **every** format in the job
- [ ] Provenance sidecar exists for every PNG (spot-check: template version +
      brand variant key correct)
- [ ] Alt text reads accurately against the actual graphic
- [ ] Proof label matches an approved source; source recorded in provenance
- [ ] Brand variant key matches the intended client surface (no cross-surface leak)
- [ ] Copy is free of banned terms and unapproved claims
- [ ] Text is fully legible in a mobile-size preview
- [ ] Every real photo carries its `photo credit`; the same photo is not reused across covers in one campaign
- [ ] Logo comes from the pack's supplied files (not retyped or redrawn)
- [ ] Approval status in provenance is set (who approved, when)

## Retention

Keep provenance files with the images they describe, for the life of the asset.
When a client asks "where did this claim come from" or "which logo version is
this," the answer should be one file lookup, not a memory hunt.

## Reference

- `README.md` — what the creative engine is
- `TEMPLATE-FAMILIES.md` — template versioning (what provenance records)
- `BRAND-PACK.md` — brand variant keys and pack provenance
- Source: [visual-factory-kit](https://github.com/cgallic/visual-factory-kit) — MIT
