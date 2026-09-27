<!-- Source: ronin1770/reel-quick (https://github.com/ronin1770/reel-quick) — MIT, Copyright (c) 2026 ronin1770. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Theme System — on-brand reels automatically

Upstream (reel-quick) provides the **mechanics**: a named transition
registry, a per-job text-overlay engine, and caption rendering. The agency
adds the **meaning**: every theme is defined per brand, so a render job
that names a theme inherits the brand's colors, fonts, lower-thirds, and
progress bars without the operator restyling anything.

## The rule

**A theme belongs to a brand.** Each theme file declares where its tokens
come from:

```
theme: <brand-slug>           # resolves to agency/brands/<slug>/
```

Colors and fonts are never hardcoded in a job — they are read from the
active brand pack's `brand-style.md` (colors + typography) at render time.
Switch the active brand (via `agency/brands/ACTIVE`) and the same clips
render in the new brand's look.

## Theme definition

```json
{
  "theme": "gator-bait-media",
  "tokens": {
    "color_primary": "#FA4616",
    "color_secondary": "#0021A5",
    "color_text_on_dark": "#FFFFFF",
    "font_headline": "Anton",
    "font_body": "system"
  },
  "lower_third": {
    "style": "lower-third-brand",
    "position": "bottom-safe",
    "bar_color": "<color_primary>",
    "text_color": "<color_text_on_dark>",
    "font": "<font_headline>"
  },
  "captions": {
    "style": "caption-pop",
    "font": "<font_headline>",
    "color": "<color_text_on_dark>",
    "stroke": "black",
    "stroke_width": 4
  },
  "progress_bar": {
    "style": "bar-brand",
    "position": "top",
    "color": "<color_primary>",
    "height_px": 8
  },
  "transitions": {
    "default": "slam-cut",
    "allowed": ["slam-cut", "whip", "dip-black"]
  }
}
```

`color_primary` etc. are looked up from the brand pack — the example values
above are Gator Bait Media's (orange #FA4616, blue #0021A5, Anton
headlines). A new brand keeps the same JSON shape and fills its own
tokens; `new-brand.sh <slug>` scaffolding + `brand-style.md` give the
values.

## Overlay kinds

| Kind | What it is | Rule |
|---|---|---|
| `caption` | Burned-in dialogue text, word/phrase synced | Always on — 85% watch muted. Large, high contrast, stroke for legibility. |
| `lower-third` | Name/title strap over the lower frame | Brand bar color + headline font; keep clear of the bottom ~250px safe zone on 1080×1920 (Meta overlays cover it). |
| `progress_bar` | Thin elapsed-time bar | Brand primary color; sits at the very top, outside the caption area. |

## Transitions

Named transitions live in the registry (`GET/POST /available-transitions`
in the API). A theme declares a `default` plus an `allowed` list — jobs
can only pick from the brand's approved transitions, so the motion
language stays consistent across reels.

## New-brand onboarding

1. Run `./new-brand.sh <slug>`; fill in `agency/brands/<slug>/brand-style.md`
   (colors, headline/body fonts).
2. Copy this theme skeleton, set `"theme": "<slug>"`, and map the token
   names to the brand's colors/fonts.
3. Render one test reel and visually QC: legibility on phone, safe zones,
   brand bar alignment. Only then is the theme approved for the pipeline.

## Source

Derived from [ronin1770/reel-quick](https://github.com/ronin1770/reel-quick)
(MIT). The transition registry and overlay mechanics are upstream
concepts; the per-brand theme contract is agency-authored.
