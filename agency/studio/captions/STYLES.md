<!-- Source: muneebkhan08/capite (https://github.com/muneebkhan08/capite) — MIT, Copyright (c) 2026 Capite Contributors. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Caption Styles

## The style system

A **caption style** is a named preset that defines how spoken words look and
move on screen: font, size, colors (primary + active-word highlight), outline,
background treatment, casing, positioning — and, most importantly, the
**motion engine** that animates each word as it is spoken.

Styles are data, not code: they live in a shared JSON config consumed by both
the live phone-mockup preview and the FFmpeg burn-in, so what you preview is
what gets rendered. Adding a style means adding a config entry (both copies
kept in sync) — no pipeline changes.

The source system ships 27 built-in presets. The agency does not need all of
them memorized; what matters is the system underneath: **7 motion engines ×
color/font treatments**, organized into four style families. Pick the engine
for the video's energy, pick the treatment for the brand.

## The 7 motion engines

| Engine | What the viewer sees | Best for |
|---|---|---|
| **Word highlight** | Current word changes color; the rest of the line stays static | Talking heads, interviews, explainers — the default workhorse |
| **Karaoke wipe** | Color sweeps across the active word left-to-right | Music, sing-alongs, rhythmic delivery |
| **Pop / spring** | Active word pops slightly larger with a springy settle | High-energy hooks, reactions, hype cuts |
| **Elastic bounce** | Word bounces in with elastic physics | Playful vlogs, lifestyle, creator content |
| **Smooth zoom / scale** | Active word gently scales up | Cinematic, luxury, documentary pacing |
| **Neon glow** | Active word glows (blur + color) | Gaming, tech, sci-fi, night-footage energy |
| **Accent highlight box** | Active word sits in an opaque pill/box | Maximum readability over busy backgrounds |

## The 4 style families

- **Trending** — the viral short-form look: bold word highlights, punchy
  colors. For Reels/TikTok/Shorts hooks and motivation/business content.
- **Clean & Tech** — minimal, precise, terminal-inspired. For tutorials,
  SaaS/product walkthroughs, minimalist talking heads.
- **Editorial & Film** — cinematic restraint: off-whites, golds, smooth scale.
  For documentaries, vlogs, dramatic storytelling.
- **Pop & Expressive** — loud color, bounce and pop motion. For lifestyle,
  beauty, streetwear, gaming, nostalgia edits.

## Example style archetypes (brand-agnostic)

Use these as the selection vocabulary — map each client brand to one primary
archetype and one alternate:

1. **Business Hook** — white base, single electric accent color, word
   highlight. (The Hormozi-shape: authority + retention.)
2. **High-Energy Pop** — yellow/orange base, box-pop or bounce, heavy weight.
   (The MrBeast-shape: gaming, hype, reactions.)
3. **Podcast Clip** — white base, lime/electric accent, word highlight,
   bottom-third position. (Interview clips: readable, neutral, repeatable.)
4. **Cinematic Editorial** — off-white base, gold/champagne accent, smooth
   scale. (Documentary pacing, luxury, film.)
5. **Neon Tech** — dark-friendly base, neon accent, glow engine. (Gaming,
   streams, tech reviews, night footage.)
6. **Clean Minimal** — pure white, one soft accent, plain word highlight.
   (Minimalist talking heads, SaaS walkthroughs — never fights the footage.)
7. **Storyteller Bounce** — warm cream base, vivid accent, elastic bounce.
   (Narrative reels, founder stories, warm brand voices.)
8. **Karaoke** — white base, electric-blue wipe across the active word.
   (Music-driven cuts, chants, sing-alongs — e.g. stadium audio.)

## Choosing a style per brand

1. **Match the brand's energy first, the trend second.** A hype sports brand
   and a luxury client should never share a caption style. Start from the
   archetype list, then tune colors to the brand's tokens.
2. **Lock one primary + one alternate per brand** in the brand folder
   (`agency/brands/<slug>/brand-style.md`). The alternate covers special
   formats (e.g. karaoke for stadium-audio cuts) without breaking catalog
   consistency.
3. **Preview against real footage.** Styles are judged on the client's actual
   backgrounds — busy stadium crowd vs. clean studio — not on mock backdrops.
   The #1 failure mode is a style that's unreadable over the brand's real
   footage.
4. **Respect the preview/render contract.** The phone mockup and the burned
   video agree only if the render host has the style's fonts installed and both
   style-config copies are in sync. If burned output drifts from preview, check
   fonts first.
5. **Re-style is free.** Changing style never re-runs transcription — iterate
   in the studio until it reads right at phone size.

## Defining a new style

1. Start from the closest archetype above (copy its config entry).
2. Set: font family (must be installed on the render host), font size and
   scale, primary color, highlight color, outline thickness/color, background
   treatment (none / box / pill), text casing, motion engine, default position.
3. Keep both config copies identical (preview + render must agree).
4. Render a 15-second test clip of real brand footage; QC at phone size.
5. Record the style ID in the brand folder so every operator picks the same one.

## Reference

- `README.md` — what the caption pipeline is
- `PIPELINE.md` — the operator runbook (style selection is step 4)
- Source: [capite](https://github.com/muneebkhan08/capite) — MIT
