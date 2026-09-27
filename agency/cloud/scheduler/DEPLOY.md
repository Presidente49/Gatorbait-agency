<!-- Source: Anil-matcha/Free-AI-Social-Media-Scheduler (https://github.com/Anil-matcha/Free-AI-Social-Media-Scheduler) — MIT, Copyright (c) 2023 Anil Chandra Naidu Matcha. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Deploy — Free AI Social Media Scheduler

Upstream: https://github.com/Anil-matcha/Free-AI-Social-Media-Scheduler
License: MIT. Deploy from the upstream repo (or your per-client fork);
nothing is vendored here.

## Option A — VPS with Node.js (recommended)

Any $6+/mo VPS with Node.js (LTS) installed. Upstream is a Next.js app
run with npm; Docker is only needed if you run Postgres locally.

```bash
# 1. Clone
git clone https://github.com/Anil-matcha/Free-AI-Social-Media-Scheduler
cd Free-AI-Social-Media-Scheduler
npm install

# 2. Env
cp .env.example .env
# Fill in .env — see "Environment variables" below.
# NEVER commit .env. Real secrets live on the server only.

# 3. Database (Postgres)
# Use managed Postgres (Neon, Supabase, RDS) or docker-run one locally.
# Then migrate:
npx prisma migrate deploy

# 4. Build & run
npm run build
npm start
# or: pm2 start npm --name scheduler -- start
```

Put Caddy or nginx in front for HTTPS (see `../n8n/docker-compose.yml`
for the Caddy pattern we use for n8n — same shape works here).

## Option B — Next.js platform + managed Postgres

Deploy the app to Vercel / Netlify / Railway; point `DATABASE_URL` at a
managed Postgres (Neon, Supabase). Run `npx prisma migrate deploy`
against the same URL before first boot. Cheapest zero-ops path.

## Environment variables (placeholders ONLY)

Copy the upstream `.env.example`, fill in real values **on the server**:

| Variable | Example placeholder | Notes |
|----------|--------------------|-------|
| `DATABASE_URL` | `postgresql://USER:PASSWORD@HOST:5432/scheduler?pgbouncer=true` | Real credentials on server only |
| `DIRECT_URL` | `postgresql://USER:PASSWORD@HOST:5432/scheduler` | Non-pooled connection for migrations |
| `NEXTAUTH_URL` | `https://social.example.com` | Public URL of the instance |
| `NEXTAUTH_SECRET` | `<generated 32-byte secret>` | `openssl rand -base64 32` |
| `GOOGLE_CLIENT_ID` | `<google-oauth-client-id>` | Google Cloud Console OAuth app |
| `GOOGLE_CLIENT_SECRET` | `<google-oauth-client-secret>` | Google Cloud Console OAuth app |
| `MUAPIAPP_API_KEY` | `<muapi-key>` | https://muapi.ai/access-keys — AI content generation |
| `WEBHOOK_URL` | `https://social.example.com/api/webhook` | App's own webhook endpoint |
| `STRIPE_SECRET_KEY` | `sk_test_...` | Only if using the credits system |
| `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` | `pk_test_...` | Only if using the credits system |
| `STRIPE_WEBHOOK_SECRET` | `whsec_...` | Only if using the credits system |

If you're not billing clients through the app, skip the three Stripe
vars entirely.

## Agency handoff: Hype agent → Scheduler

This is how approved content flows from the agency workflow into the
client dashboard. **The scheduler never creates content; it only
schedules and publishes what the agency approved.**

1. **Hype drafts** the post per the agency playbook (original hook,
   excerpt, image/video, link) and QC-passes it per protocols.
2. **Approval:** the CEO (human) or the brand's approval rules sign off.
   For Gator Bait Media: Instagram drafts still need Brenden's approval
   tap before anything goes out.
3. **Load into the dashboard:**
   - Open the scheduler Composer on the instance for that brand.
   - Upload the media (or paste the URL), paste the approved caption,
     pick target platforms + times, save as **draft** (client-facing
     review) or **scheduled**.
4. **Client review (white-label instances):** the client logs in with
   Google OAuth, reviews drafts in their calendar, approves or comments.
   The AI agent (`/agents`) can generate caption variants — final copy
   still comes from the agency's approved text.
5. **Publish:** on the scheduled time, the app publishes to each
   connected platform account. Failures show in Post History with status
   indicators — Hype checks and re-queues failures.

**Platform connections:** each brand/client connects its own social
accounts inside its own dashboard instance (YouTube, TikTok, IG, FB,
X, LinkedIn, Threads, Pinterest). Agency staff never share one login
across brands — that's the whole point of separate instances.

## Backups

- **Database:** `pg_dump` nightly (managed Postgres usually has this
  built in). Uploaded media lives in the app's storage — back that up
  with whatever the host provides.
- Keep the `.env` values in a password manager (Bitwarden/1Password),
  never in the repo.

## Upgrades

```bash
cd Free-AI-Social-Media-Scheduler
git pull
npm install
npx prisma migrate deploy
npm run build
# restart the process
```

Check the upstream releases/changelog before pulling — test on a
staging instance first for client dashboards.
