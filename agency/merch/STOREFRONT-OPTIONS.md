<!-- Source: medusajs/medusa (https://github.com/medusajs/medusa) — MIT License. Adapted for Gator Bait Agency. -->

# Merch Storefront Options

How the agency picks an e-commerce backend when a white-label brand
needs a merch store. Opinions are earned: the default is Medusa v2;
everything else is here so we can say why we didn't pick it.

## The shortlist

| Platform | Stack | License (verified) | Verdict |
|---|---|---|---|
| **Medusa v2** | Node.js / TypeScript, modular | **MIT** (core; Enterprise materials carved out under a separate commercial license — we stay on the MIT core) | ✅ Agency default |
| Saleor | Python, GraphQL-first | BSD 3-Clause (permissive) | ✅ Integrated — multichannel maps to one channel per brand. See `agency/cloud/saleor/OVERVIEW.md`. |
| Vendure | TypeScript / NestJS, GraphQL | GPLv3 Community Edition + commercial VCL | ❌ Rejected (copyleft). See `agency/cloud/vendure/NOT-INTEGRATED.md`. |
| WooCommerce | PHP / WordPress | GPLv2 | ❌ Copyleft, legacy stack — no fit for new brand builds. |
| Shopify (Hydrogen) | SaaS core, React storefront | Proprietary | ❌ Rent, don't own. Fine for clients who already have Shopify; not the agency's self-host default. |

## Why Medusa v2 is the default

- **Truly headless:** backend (products, orders, customers) is fully
  decoupled from the storefront. The storefront can be Next.js,
  a Wix embed, or a React Native app — the agency reuses the same
  backend per brand.
- **Modular core:** payments, fulfillment, notifications are swappable
  modules. Brand-specific logic (e.g. a POD fulfillment provider)
  ships as a plugin, never as a core patch — upgrades stay painless.
- **Plugin system:** Stripe, PayPal, and print-on-demand fulfillment
  (Printful via `print2medusa`, Printify via `medusa-plugin-printify`)
  all exist as installable plugins. See `PRINT-ON-DEMAND.md`.
- **No GMV tax:** self-hosted = no platform percentage. Infrastructure
  + engineering only, which is the white-label pitch to brands.
- **React admin included:** brand operators get a real back office
  without the agency building one.

Known limits (from the 2026 competitive landscape — plan around them):
- No native multi-tenancy. One Medusa backend per brand (or per
  portfolio). Multi-brand under one roof needs the agency to run
  separate deployments, not one shared instance.
- Medusa v2 is still maturing operationally (event-loss modes,
  saga bugs reported in the wild). For a merch store doing
  hundreds of orders/day this is fine; for flash-sale traffic
  spikes, load-test before launch.

## When to pick something else

- **Brand already on Shopify:** don't fight it. Use Hydrogen or the
  brand's existing theme; the agency's value is creative + ads, not
  re-platforming.
- **Tiny catalog, no dev budget:** a hosted page (Printful/Printify
  storefront, or the brand's existing site) beats running a backend.
- **Marketplace-style needs:** Medusa's marketplace module covers it,
  but budget real engineering time.

## Storefront pairing

The agency's standard pair is Medusa v2 backend + a Next.js storefront
skinned from the brand pack (see `agency/studio/creative/BRAND-PACK.md`),
or the brand's existing site (e.g. Wix) with Medusa behind it via API.
The storefront is disposable and re-skinnable; the product/order data
is the durable asset.
