<!-- Source: paperclipai/paperclip (https://github.com/paperclipai/paperclip) — MIT. Adapted for Gator Bait Agency. -->

# Paperclip — Deploy

## Requirements

- Node.js 24.11+ and pnpm 9+ (local dev / contributors)
- No external database required — embedded PostgreSQL by default
- For production: a VPS with Docker, or any host that can run Node

## Quickstart (recommended path)

```sh
npx paperclipai onboard --yes
```

Walks through setup, configures the environment, starts Paperclip.
To start again later:

```sh
npx paperclipai run
```

Then: create company → define goal → create CEO agent + adapter →
build org chart → set budgets → assign tasks → go. Agents start their
heartbeats and the company runs. UI at `http://localhost:3100`.

## Local development (contributors)

```sh
git clone https://github.com/paperclipai/paperclip
cd paperclip
pnpm install
pnpm dev
```

## Production notes

- **Co-locate with the agency cloud stack**: Paperclip runs alongside
  n8n on the same VPS (`agency/cloud/n8n/docker-compose.yml` pattern —
  add a `paperclip` service with a named volume, `restart:
  unless-stopped`, reverse-proxy via the existing Caddy for TLS).
- **Data**: embedded Postgres is fine to start; back up its volume
  like the n8n volumes. If you outgrow it, point at managed Postgres.
- **Adapters**: wire each of the 8 agents to a real adapter —
  Claude Code adapter for the heavy agents, shell/HTTP adapters for
  narrow scheduled jobs (watches, digests).
- **Secrets**: scoped per company (Paperclip supports scoped secrets
  and company boundaries) — a brand's API keys never leak to another
  brand's agents. Mirrors our white-label isolation.
- **Budgets first**: set per-agent and per-company monthly budgets
  *before* the first heartbeat. An uncapped agent fleet is a credit
  card with no limit.
- **Start with one company** (Gator Bait Media), prove the heartbeat
  loop, then clone the pattern per brand via `new-brand.sh`.
- **Phone ops**: Paperclip's UI is designed for managing from a phone
  — this fits Brenden's phone-first workflow.

## What we are NOT doing yet

- We have **not vendored** the Paperclip app into this repo. These
  docs capture the concepts and the mapping. Running Paperclip is a
  deploy-time decision (needs a VPS + Node), not a repo change.
- The Agent Companies spec (`COMPANY.md`/`TEAM.md`/etc.) is noted as a
  future alignment target — our layout already rhymes with it; a
  mechanical rename pass can adopt it later without breaking anything.
