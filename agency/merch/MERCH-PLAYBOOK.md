<!-- Agency-original synthesis for Gator Bait Agency. -->

# Merch Playbook — launching a brand's store

The operator runbook for taking a white-label brand from "we want
merch" to a live, ad-fed store. Concepts only — the store itself is
deployed per brand; this playbook is brand-agnostic.

## Phase 0 — Brand pack first

No store work starts without the brand pack
(`agency/studio/creative/BRAND-PACK.md`): logo lockups, colors,
fonts, voice. Every garment design, mockup, and storefront skin
pulls from the pack. A store without a pack ships generic
Printful-template merch and dies.

## Phase 1 — Catalog design (days 1–3)

- Pick 3–5 hero SKUs, not 50. Best sellers for media brands:
  classic tee, hoodie, hat, and one novelty item (flag, koozie, sticker).
- Designs come from the creative agent using the template-family
  system (`agency/studio/creative/TEMPLATE-FAMILIES.md`):
  one layout system, every garment size.
- Generate mockups brand-side (don't rely on POD flat renders for
  ads — they read as generic). Real photography of real garments
  beats renders for social creative (see agency learnings: real
  photography beats polished graphics).

## Phase 2 — Backend + POD (days 3–7)

- Deploy Medusa v2 (see `STOREFRONT-OPTIONS.md`).
- Wire print-on-demand per `PRINT-ON-DEMAND.md`:
  plugin install → API token in secret manager → catalog sync →
  markup set → webhooks configured → test orders placed.
- Stripe (or brand's processor) as the payment module.
- QC gate: a full test order for every hero SKU, tracking email
  received, margin visible in admin. No ads until this passes.

## Phase 3 — Storefront (days 5–10)

- Skin the storefront from the brand pack. One page that matters:
  the product page — big photos, size chart, shipping estimate,
  reviews if they exist.
- Every product page links back to the brand's content engine
  (site, socials) and vice versa — merch is a funnel, not a silo.
- Install the brand's Meta Pixel on every storefront page before
  launch (retargeting + conversion tracking from day one).

## Phase 4 — Launch with paid + organic (day 10+)

- Launch creative: unboxing / wear-test reels cut from real product
  (studio reels pipeline), posted natively — never a bare link drop.
- Paid: start with a small daily budget on the hero SKU creative;
  scale what converts. Never pair athlete/coach presser likeness
  with product sales creative — licensing risk is always the
  brand owner's call.
- Organic: the brand's social engine pushes the store on the
  standing cadence; every post links to the store.

## Phase 5 — Operate

- Weekly: margins per SKU (POD cost drift happens), dead-SKU
  pruning, new design drops tied to brand moments (wins, events,
  launches).
- Monthly: review fulfillment health (webhook dashboard), shipping
  time complaints, returns handled as brand-ops.
- Scale rule: a store earns a bigger catalog only after the hero
  SKUs prove conversion. Breadth before proof is inventory
  thinking in a no-inventory business — it just adds confusion.
