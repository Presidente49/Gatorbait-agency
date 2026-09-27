<!-- Source: amandamartin-dev/pdfkit-demo-wixstudio (https://github.com/amandamartin-dev/pdfkit-demo-wixstudio) — MIT License. Adapted for Gator Bait Agency. -->

# Velo Patterns

Production Velo patterns the agency's webmaster agent uses on Wix and
Wix Studio sites. The sibling redesign repo already covers custom CSS
conventions — these are the net-new backend/code patterns.

## Pattern 1 — Backend web modules (`*.web.js`)

The single most important Velo pattern: code that must run server-side
lives in backend `.web.js` files and is exposed to page code via
`webMethod` with an explicit permission.

```javascript
// backend/generatePdf.web.js
import { Permissions, webMethod } from "wix-web-module";

export const generateDownloadLink = webMethod(
  Permissions.Anyone,
  async (fileName) => {
    // runs on Wix backend: npm packages, secrets, media APIs
    const buffer = await generatePdf();
    const file = await uploadFile(fileName, buffer);
    return await getDownload(file);
  }
);
```

```javascript
// page code
import { generateDownloadLink } from 'backend/generatePdf.web';

$w('#btnPdf').onClick(async () => {
  const url = await generateDownloadLink($w('#fileName').value);
  if (url) { $w('#btnPdf').link = url; }
});
```

Rules:
- **Never import backend-only APIs in page code.** `wix-media-backend`,
  secrets, and npm packages like PDFKit live behind the web module.
- **Permissions are the security model.** `Permissions.Anyone` for
  public actions, `Permissions.SiteMember` / admin-only for the rest.
  The permission sits on the exported function, not in page code.
- **Validate at the page, authorize at the backend.** Page-level input
  validation (regex patterns on inputs, disabled-until-valid buttons)
  is UX; the backend re-validates because page code is bypassable.

## Pattern 2 — npm packages in Velo backend

Wix backend supports npm packages (PDFKit, etc.) installed via the
Packages section. The pattern: heavy lifting (PDF generation, image
processing, crypto) runs in the backend web module, the page only
passes parameters and receives a URL. Keep backend functions small
and single-purpose — one `.web.js` file per capability.

## Pattern 3 — Async UX states

Every backend call from page code follows the same button lifecycle:
`disable + "Please wait..." → await → link/label update → re-enable`.
Users on slow connections otherwise double-submit. Standardize this
in the brand's Velo snippets, not per page.

## Pattern 4 — Velo code in git (Wix CLI sync)

<!-- Agency-original synthesis: pattern is public Wix tooling, described here for agency use. -->

Author Velo code in git, sync it into the Wix site — never treat the
in-browser editor as the source of truth:

- Layout mirrors what Wix expects under the site's backend
  (`backend/http-functions.js`, `backend/*.web.js`, page code files).
- Sync via the Wix CLI (`wix dev` / `wix push`) or the Wix Studio ↔
  GitHub integration. Reviewable diffs, rollback, and the agency's
  webmaster agent can generate and QC code without touching the editor.
- Secrets (API keys, tokens) live in Wix Secrets Manager only —
  referenced by name from backend code, never hard-coded, never in
  frontend code, never in git.

This is how the agency scales Velo work across brands: one repo per
brand site, code-reviewed Velo, deployed through the CLI. The editor
stays for layout; logic lives in version control.

## Pattern 5 — Backend as API surface (`http-functions.js`)

For integrations (n8n workflows, external dashboards, the agency's own
tooling), expose Wix CMS data through `http-functions.js` REST
endpoints rather than scraping the site:

- One function per resource (`/blog-posts`, `/events`), backed by
  `wix-data` queries in a shared services module.
- Authenticate inbound calls (JWT validated against a secret in
  Secrets Manager) — a public Wix site endpoint is a public endpoint.
- This is the sanctioned way for the agency's cloud layer
  (`agency/cloud/n8n/`) to read/write brand site content.
