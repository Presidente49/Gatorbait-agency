<!-- Source: Anil-matcha/Free-AI-Social-Media-Scheduler (https://github.com/Anil-matcha/Free-AI-Social-Media-Scheduler) — MIT, Copyright (c) 2023 Anil Chandra Naidu Matcha. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# White-Label Notes — Client Dashboard Rebrand

The scheduler is the client's visible dashboard, so it must look like
**the client's brand**, not the agency's. Checklist per client instance.

## Rebrand checklist

- [ ] **Instance name** — app title / tab title. (Search the `src/`
      tree for the upstream name "Free AI Social Media Scheduler" and
      replace.)
- [ ] **Logo** — swap `public/` logo assets for the client's logo
      (favicon, header logo, login screen). Match `next.config.mjs` /
      layout metadata.
- [ ] **Colors** — Tailwind theme. Replace the upstream accent palette
      with the client's brand colors (buttons, calendar highlights,
      status chips). Keep contrast/accessibility.
- [ ] **Domain** — dedicated subdomain: `social.<clientdomain>.com`
      (or `app.<clientdomain>.com`). Set `NEXTAUTH_URL` and the Caddy/
      nginx reverse proxy + DNS A record to match.
- [ ] **Login screen copy** — "Sign in to continue to <Client>" rather
      than the upstream wording. Google OAuth button stays (NextAuth).
- [ ] **OAuth consent screen** — the Google Cloud OAuth app name should
      match the client-facing name if the client sees it.
- [ ] **AI agent persona** (`/agents`) — seed its persistent context
      memory with the client's brand voice, tone guidelines, and
      campaign rules (from `agency/brands/<slug>/`). It generates
      platform copy, so it must know the brand.
- [ ] **Default platforms** — enable only the platforms the client
      actually uses; disable the rest in the dashboard settings.
- [ ] **Stripe credits** — either disable the credits UI (agency
      bills separately) or brand it with the client's name if the
      client self-funds scheduling credits.
- [ ] **Footer / about** — replace upstream links with the client's
      site, privacy policy, and support contact.

## Keep the agency invisible

- The client never sees other brands, other instances, or the agency's
  n8n/automation layer.
- One instance per client (separate DB, separate env). Never
  multi-tenant one instance across clients — OAuth tokens and media
  libraries must not mix.

## Upstream changes

If we maintain a per-client fork, rebase it onto upstream periodically
for security fixes, then re-apply the rebrand diff. Keep the rebrand as
a small, documented patch set so rebasing stays cheap.

## License note

MIT requires the original copyright notice (Anil Chandra Naidu Matcha,
2023) to be retained in copies/substantial portions. Keep the
`LICENSE` file and a "based on" note in the fork — it can live in an
About page or footer credit, e.g. *"Powered by Gator Bait Agency ·
based on Free AI Social Media Scheduler (MIT)"*.
