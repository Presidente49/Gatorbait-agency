<!-- Source: saleor/saleor (https://github.com/saleor/saleor) — BSD 3-Clause. Evaluated, NOT integrated. -->

# NOT INTEGRATED — saleor/saleor

- **Repo:** https://github.com/saleor/saleor
- **Evaluated:** 2026-09-26
- **License (read in full):** BSD 3-Clause License
  (Copyright (c) 2020-2023, Saleor Commerce).
- **Why rejected:** BSD 3-Clause is permissive and carries no copyleft
  risk — but the agency's license policy for this scan is a strict
  MIT/Apache-2.0 allow-list, and BSD-3 is outside it. Rejected on the
  rule, not on the risk. If the policy is ever widened to all
  permissive licenses, Saleor (Python, GraphQL-first, most mature
  open-source commerce API) is the first candidate to re-evaluate.
- **What we did instead:** Medusa v2 (MIT) is the agency's merch
  backend default. See `agency/merch/STOREFRONT-OPTIONS.md`.
