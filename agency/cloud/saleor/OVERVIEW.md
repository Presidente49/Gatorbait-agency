<!-- Source: saleor/saleor (https://github.com/saleor/saleor) — BSD 3-Clause. Concepts adapted for Gator Bait Agency. -->

# Saleor — Overview

**What it is:** Saleor Core — headless, GraphQL-native commerce API.
Python/Django, ~23K stars, in development since 2013. BSD 3-Clause
(permissive, no copyleft). Initially held out of the agency under the
old MIT/Apache-2.0-only rule; integrated 2026-09-27 after Brenden
widened the policy to all permissive licenses.

## Why it fits the agency

- **Multichannel is white-label native.** Per-channel control of
  pricing, currencies, stock, and products. One Saleor instance can
  serve many brands the way Paperclip serves many companies.
- **API-only.** No theme lock-in, no plugin monolith — the storefront
  is whatever the brand needs (Next.js reference storefront included).
- **Promotion engine:** sales, vouchers, cart rules, gift cards —
  the growth department's offer designs plug straight in.
- **Payment orchestration:** multi-gateway, extensible — no single
  processor dependency.
- **No commercial carve-out.** Single open version, no feature
  fragmentation. (Contrast: Medusa v2 keeps Enterprise materials
  commercial; Vendure is GPL.)

## Agency pattern

- Saleor = the self-hosted merch engine behind `agency/merch/`.
- One channel per brand. Brand onboarding (`new-brand.sh`) gains a
  future step: provision channel + wire storefront.
- Print-on-demand (PRINT-ON-DEMAND.md) connects via webhooks/apps —
  Saleor's app system keeps custom logic out of the core, so upgrades
  don't break brand customizations.
- Dashboard is a separate decoupled project — brand managers get
  their own login without touching the API.

## Tradeoff (from Saleor's own README)

Service-oriented API commerce is heavier than a WordPress/WooCommerce
quick start for a single small shop. It pays off when you run many
brands, deploy often, and need uptime — i.e., exactly the agency model.

## Docs

- https://docs.saleor.io
- Storefront example: https://github.com/saleor/react-storefront
- Dashboard: https://github.com/saleor/saleor-dashboard
