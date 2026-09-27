<!-- Source: coollabsio/shoutrrr (https://github.com/coollabsio/shoutrrr) — Apache-2.0 (LICENSE read: standard text, no copyright line, no NOTICE file; holder coollabsio per repository). Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
<!-- Concepts and deployment notes from README.md, app/Mcp/Tools/, app/Services/Publishing/BackoffSchedule.php and app/Services/Billing/WorkspaceSubscriptionGate.php (commit 86308ed). No code vendored. Runtime UNVERIFIED: Docker was unavailable in the test environment. -->
# Shoutrrr: Multi-Client Social Scheduler (Second Option)

A self-hosted, Apache-2.0 alternative to Buffer and Hootsuite that runs as one
Docker container. It publishes to **X, Bluesky, LinkedIn, Facebook Pages,
Instagram, Threads and Discord**.

## When to pick it over the default scheduler

The default client dashboard is `../scheduler/` (video-first, including YouTube,
TikTok and Pinterest, one instance per client). Pick Shoutrrr when:

| Need | Default scheduler | Shoutrrr |
|---|---|---|
| YouTube, TikTok, Pinterest | Yes | **No**: keep the default |
| Many clients on one server | One instance each | **Workspaces**: one instance, each client walled off |
| Client approves a draft without an account | Log in | **Share link** to a single post |
| Failed post handling | Status flag | **Per-account retry**, one network's failure doesn't block the others |
| Account security | Google OAuth | Email + 2FA (TOTP) + passkeys |
| Agent access | App's own agent page | **MCP server** (tools below) |

For a text-and-image brand (restaurant, local shop, B2B), Shoutrrr's workspaces
make it the cheaper way to host many small clients. For video-first brands, keep
the default.

## Agency rules for running it

1. **One workspace per brand** (named after `agency/brands/<slug>/`). Never mix
   brands in one workspace.
2. **Agents draft, people publish.** Its MCP server exposes both kinds of tool.
   Give agents only the draft-side tools:

   | Allowed for agents | Human only |
   |---|---|
   | list workspaces, accounts, account sets, posts; get post, calendar, posting schedule | **publish post, schedule post, queue post** |
   | create post, update post, add/remove post media (drafts) | delete post, delete share, delete account set |
   | create share link (for client approval) | retry a failed target (only after the cause is known) |

   A publishing or scheduling tool on the agent side needs Brenden's
   sign-off (the same rule as the n8n workflows).
3. **Client approval by share link:** hype drafts, creates a share link, and the
   client approves the post there. Share links are public, so set an expiry and
   don't put unannounced news in them.
4. **Retries:** each network retries on its own with exponential backoff
   (starting at 60 s, doubling, capped near 1 hour, with up to 10% jitter).
   Watch the in-app alerts for "account needs reconnecting". A token expiry is
   not something to retry.
5. **Billing module:** leave `subscriptions.enabled` off for self-hosted
   clients. It meters X posts and exists for a hosted service.
6. **Secrets:** `APP_KEY`, OAuth app secrets and platform tokens live in the
   server's `.env` / encrypted database only. Never in this repo or a brand
   folder.

## Deploy (per upstream README)

- Image: `ghcr.io/coollabsio/shoutrrr:latest`. The web app, queue worker and
  scheduler run in one container.
- SQLite by default; move to Postgres/Redis when a server hosts many clients.
- Generate `APP_KEY` with the image's `artisan key:generate --show`.
- Persistent volumes for `storage` and `database/sqlite`.
- Public deployment: HTTPS `APP_URL` and `SESSION_SECURE_COOKIE=true`, behind
  the agency's Caddy.
- Each network needs its own developer app (X, Meta, LinkedIn, Threads OAuth).
  The platform's own review can take days; plan it before a client launch.

## Status

- License: Apache-2.0, read in full; no carve-outs; billing is optional config.
- Tested: code read only. **Runtime UNVERIFIED** (no Docker in the test
  environment). Before the first client install, bring it up on a scratch
  server and post to a test Discord webhook first.
