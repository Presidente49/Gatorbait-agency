# Hero Overlay: Headline Over Photo for the Lead Story

**Primary owner:** blueprint (spec), with webmaster (deploy). Use it for any big centerpiece: the front-page lead, a magazine cover story, a landing-page hero.

Owner direction (GatorBait, Sept. 27, 2026): "if it's gonna be that big of a centerpiece we need text over picture." A large photo with the headline sitting underneath reads as a blog; the headline on the photo reads as a publication.

## Spec

| Element | Desktop | Phone (≤820px) |
|---|---|---|
| Photo | full width of its column, `aspect-ratio:16/10` (magazine 16/9), `object-fit:cover`, `object-position:center 30%` | `aspect-ratio:4/5` |
| Copy block | absolutely positioned at the bottom, left 0 / right 0 | same |
| Gradient | navy, transparent at the top, about 75% opaque at 40%, about 95% at the bottom | same |
| Top padding of the copy | about 130–140px (the gradient's run-up) | about 100px |
| Kicker | light brand orange (on navy) | same |
| Headline | white, 30–44px, subtle text-shadow | 26px |
| Deck | clamped to 3 lines | clamped to 2 lines |
| Photo credit | top-right corner, white at 85%, shadowed | same |

## Rules

- **Real photography only.** A graphic, chart or AI illustration under a headline overlay looks broken. If the lead story's cover isn't a photo, replace the cover (see `research/photo-sourcing.md`) before shipping the overlay.
- Scope every selector to the page's root ID so nothing leaks sitewide.
- **Specificity trap:** older rules with more specific selectors (`article.sh-lead figure{margin:0 0 18px}`) beat the overlay's. The symptom is a strip of background under the photo. Check computed margins and use `!important` only on the properties that lose.
- Verify with a local render at 390px and 1280px using the production CSS. Checks: the copy block's bottom equals the photo's bottom, there's no horizontal overflow, and the headline is readable over the brightest part of the photo.
