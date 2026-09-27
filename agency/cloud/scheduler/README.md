<!-- Source: Anil-matcha/Free-AI-Social-Media-Scheduler (https://github.com/Anil-matcha/Free-AI-Social-Media-Scheduler) — MIT, Copyright (c) 2023 Anil Chandra Naidu Matcha. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Client Dashboard — AI Social Media Scheduler

The agency's white-label **client dashboard** option: a free, self-hosted
AI social media scheduler that clients can log into to see their content
calendar, approve drafts, and view scheduled/published posts — without the
agency paying for Buffer, Hootsuite, or Later seats.

## What it is

**Free-AI-Social-Media-Scheduler** by Anil Chandra Naidu Matcha
([GitHub](https://github.com/Anil-matcha/Free-AI-Social-Media-Scheduler),
MIT licensed, Copyright (c) 2023 Anil Chandra Naidu Matcha).

A video-first, multi-platform social scheduler with a built-in AI agent
workspace:

- **Multi-platform publishing** — YouTube, TikTok, Instagram (Reels &
  Posts), Facebook (Pages & Reels), X, LinkedIn, Threads, Pinterest.
- **Video & post scheduling** — upload media or paste a URL, pick target
  platforms and times, publish automatically.
- **Multi-account management** — connect multiple social accounts per
  platform from one dashboard.
- **AI Social Marketing Agent** (`/agents`) — conversational marketing
  assistant with persistent context memory; generates platform-tailored
  hooks, captions, and hashtag strategies; 1-click post proposals that
  open in the Composer and schedule with one click.
- **Post history & calendar** — track scheduled, published, and failed
  posts with status indicators and direct published URLs.
- **Credits system** — Stripe-powered pay-as-you-go credits (optional;
  skip if you don't want client billing through the app).

## Tech stack

Next.js 16 (App Router + Turbopack) · NextAuth.js (Google OAuth) ·
PostgreSQL + Prisma ORM · Stripe · MuAPI (AI content generation) ·
Tailwind CSS.

## How the agency uses it

1. **Internal use (Gator Bait Media as reference brand):** the Hype agent
   approves content through the agency workflow (playbook → QC → CEO
   sign-off), then hands the approved assets + copy to the scheduler for
   multi-platform publishing and the client-visible calendar. See
   `DEPLOY.md` for the handoff protocol.
2. **White-label client dashboard:** each client gets their own instance
   on their own subdomain (e.g. `social.clientname.com`), rebranded per
   `WHITE-LABEL-NOTES.md`. The client sees only their calendar, drafts,
   and analytics — never the agency's internals.

## What we did NOT do

The upstream app was **not vendored** into this repo (per agency policy:
white-label references stay lean; we deploy from the upstream source).
These docs describe how to deploy it per its own docs and how the
agency's agents hand content to it. If the app is forked for a client,
the fork lives outside this repo and the fork's `LICENSE` must retain
the MIT attribution to Anil Chandra Naidu Matcha.

## Deploying

See `DEPLOY.md` for full deploy instructions (VPS + Docker, or any
Next.js host + managed Postgres).

## Rebranding for a client

See `WHITE-LABEL-NOTES.md` — name, logo, colors, domain, auth, Stripe.
