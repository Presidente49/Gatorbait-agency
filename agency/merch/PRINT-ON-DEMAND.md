<!-- Source: legenki/print2medusa (https://github.com/legenki/print2medusa) — MIT License. Adapted for Gator Bait Agency. -->
<!-- Source: greedychipmunk/medusa-plugin-printify (https://github.com/greedychipmunk/medusa-plugin-printify) — MIT License. Adapted for Gator Bait Agency. -->

# Print-on-Demand for Brand Stores

Concepts from the two production-grade open-source Medusa v2 POD
plugins: `@legenki/print2medusa` (Printful) and
`medusa-plugin-printify` (Printify). Nothing is vendored — this is the
integration pattern the agency follows when wiring POD into a brand's
Medusa store.

## The architecture (same in both plugins)

```
Brand storefront (Next.js / Wix)
        │  order.placed
        ▼
Medusa v2 ──► POD plugin ──► Printful / Printify API
        │                         │ webhooks
        │  fulfillment + tracking ◄┘
        ▼
Medusa admin: per-parcel tracking, cost vs retail, margin
```

- **Products sync from the POD catalog** into Medusa; the store never
  holds inventory. Publish/unpublish is stock-driven.
- **Order submit is event-driven:** a subscriber on Medusa's
  `order.placed` event pushes the order to the POD provider.
  This is the seam where "brand sells, POD prints and ships" happens.
- **Webhooks close the loop:** `package_shipped`, `order_failed`,
  `order_canceled`, `package_returned` events flow back into Medusa as
  fulfillments/shipments with tracking numbers and carrier URLs.
  Webhook redelivery must be idempotent — derive an `event_id`,
  store every inbound event under a unique index, absorb duplicates.
- **Admin visibility:** a good plugin shows POD cost, retail total,
  and margin per order right in the Medusa admin. Margin is only
  shown when both figures are in the same currency — never guess
  an exchange rate.

## Printful vs Printify (agency pick: brand's call, both work)

| | Printful | Printify |
|---|---|---|
| Plugin | `print2medusa` (MIT) | `medusa-plugin-printify` (MIT) |
| API style | Manual-order/API platform, private token (`orders`, `sync_products` scopes) | API with shop management |
| Live shipping rates | Yes, with flat-rate fallback when the API is unreachable | Pattern supports it; verify per version |
| Mockups | API endpoints exist; flat renders are basic — brands usually generate their own mockups | Similar; brand-side mockup generation recommended |

## Hard-won details worth copying

- **Live rates need a fallback.** If the POD API is down at checkout,
  the cart must still price — configure flat fallback rates or
  checkout breaks during a provider outage.
- **Shipping method must round-trip.** The customer picks and pays for
  a method; confirm it with the provider when submitting the order.
  If the provider can't confirm, send nothing and let the provider
  choose — an unconfirmed method override risks a rejected order.
- **Retry webhooks on a schedule.** Events can arrive before their
  order link exists. A 5-minute scheduled job with exponential
  backoff (capped ~6 hours / ~20 attempts) keeps the dashboard honest.
- **Parcel-level fulfillments.** POD providers split orders across
  facilities — model one fulfillment per parcel, each with its own
  tracking, not one fulfillment per order.
- **Returns are an API gap.** Printful API v1 has no returns endpoint
  (only a `package_returned` webhook after the fact). Returns stay a
  brand-ops process, not an API flow.

## Brand runbook (POD half)

1. Brand opens a Printful or Printify account; agency stores the API
   token in the deployment's secret manager (never in the repo).
2. Install the matching plugin in the brand's Medusa backend,
   register it as the fulfillment provider.
3. Sync the catalog; design garments using the brand pack
   (colors, logo, fonts from `agency/studio/creative/BRAND-PACK.md`).
4. Set retail prices with a markup target (e.g. ~30% over POD cost)
   and verify margins in the admin on test orders.
5. Configure webhooks; place test orders; confirm tracking lands
   in Medusa and the customer gets shipping emails.
6. Only then point ads at the store.
