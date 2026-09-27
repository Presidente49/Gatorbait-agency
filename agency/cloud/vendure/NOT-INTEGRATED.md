<!-- Source: vendure-ecommerce/vendure (https://github.com/vendure-ecommerce/vendure) — GPLv3. Evaluated, NOT integrated. -->

# NOT INTEGRATED — vendure-ecommerce/vendure

- **Repo:** https://github.com/vendure-ecommerce/vendure
- **Evaluated:** 2026-09-26
- **License (read in full):** GPLv3 Community Edition by default,
  with a separate commercial Vendure Commercial License (VCL).
  (The LICENSE.md states: "This software is available under two
  different licenses: GNU General Public License version 3 (GPLv3)
  as Vendure Community Edition / Vendure Commercial License (VCL).
  The default Vendure license, without a valid Vendure Commercial
  License agreement, is the Open-Source GPLv3 license.")
- **Why rejected:** GPLv3 copyleft. Integrating Vendure concepts or
  code into the agency's white-label stack would attach copyleft
  obligations to brand deployments — incompatible with the
  brand-agnostic, resellable model. (Note: some third-party writeups
  still describe Vendure as MIT — stale. The actual LICENSE.md in
  the repo is GPLv3-first. This is exactly why the agency rule says
  read the license file, never the badge.)
- **What we did instead:** Medusa v2 (MIT) is the agency's merch
  backend default. See `agency/merch/STOREFRONT-OPTIONS.md`.
