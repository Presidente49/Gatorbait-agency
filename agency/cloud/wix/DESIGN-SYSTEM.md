<!-- Agency-original synthesis for Gator Bait Agency. -->

# Wix Design System

How the agency keeps Wix and Wix Studio sites on-brand without
fighting the editor. The sibling redesign repo owns custom CSS
conventions; this is the token-and-system layer above that.

## Tokens first, CSS second

Wix Studio's Site Styles (colors, text styles, button styles) are the
design tokens. The rule:

1. **Define the palette once** in Site Styles from the brand pack —
   primary, accent, neutrals, success/error. Every section, strip,
   and button references a token, never a hex value typed by hand.
2. **Lock the type scale** — display, H1–H3, body, caption — with the
   brand's fonts. No ad-hoc font pickers on individual text boxes.
3. **Custom CSS is the escape hatch, not the system.** The sibling
   repo's CSS conventions handle what tokens can't (animations,
   complex layouts). If a style needs custom CSS in more than one
   place, it should have become a token or a saved section instead.

Why: editor-built sites rot when every page invents its own styles.
Tokens make a brand's site re-skinnable and let the agency hand a
site to a brand operator without a style guide document.

## Section presets, not pages

Build a library of saved sections per brand — hero variants,
article cards, video embeds, newsletter signup, merch strip —
each bound to tokens. New pages assemble from presets. This is the
Wix-native equivalent of the creative studio's template families:
one layout system, every page.

## Responsive rules

- Design desktop-first in the editor, then check the two
  breakpoints that matter: tablet and mobile. Stretched full-bleed
  strips break most often — pin their inner content with max-width.
- Text over images needs a contrast guard (overlay or scrim) at
  every breakpoint, not just desktop.
- Repeaters are the CMS workhorse (blog feeds, product grids,
  schedules). Style the repeater item once; the CMS fills the rest.

## Brand-pack binding

Every new brand site starts from `agency/studio/creative/BRAND-PACK.md`:
logo, colors, fonts, voice. The webmaster agent's first job on a
brand site is binding the pack into Site Styles + section presets.
A site whose tokens match the pack is a site the brand can extend
without the agency.
