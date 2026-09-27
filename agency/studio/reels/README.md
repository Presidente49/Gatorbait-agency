<!-- Source: ronin1770/reel-quick (https://github.com/ronin1770/reel-quick) — MIT, Copyright (c) 2026 ronin1770. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Reel Builder — API-driven short-form renderer

The agency's render farm for short-form video. Submit a render job over a
REST API, get back a finished 1080×1920 reel — no manual editing.

**Stack (upstream):** FastAPI backend + FFmpeg + Redis/ARQ job queue.
Workers render asynchronously outside the request cycle; a Next.js frontend
exists upstream but the agency drives the API directly.

## What it does

- **Trims, arranges, and merges** multiple source clips into one vertical video
- **FFmpeg-powered transitions** between scenes (named transition registry —
  list them with `GET /available-transitions`, register new ones with `POST`)
- **Text overlays & burned-in captions** styled per job
- **Async rendering:** enqueue a job, poll for status, download the result

## How it fits the agency pipeline

```
clipping ──▶ captions ──▶ REEL RENDER (this) ──▶ publish
   ▲              ▲               ▲                    ▲
 show DVR      whisper/        reel-quick           Meta Playbook
  cuts       caption engine      API                  (Hype)
```

1. **Clipping** — Blueprint/Wrench cut the source footage (show DVR, presser
   feed, game highlights) into ordered clips.
2. **Captions** — caption text is produced (85% of viewers watch muted —
   captions are burned in, never optional).
3. **Reel render** — clips + captions + brand theme are submitted as one job
   to this builder; the result is a finished MP4.
4. **Publish** — Hype publishes via the Meta playbook rules (IG ≤ ~18MB at
   CRF 24 H.264, 1080×1920, +faststart).

## Building blocks (adapted)

| Agency step | Upstream component |
|---|---|
| Submit render job | `POST /videos` → `POST /videos/{id}/enqueue` |
| Attach clips | `POST /video-parts` per clip |
| Attach overlays/captions | `POST /videos/{id}/text-overlays` |
| Choose transitions | `GET/POST /available-transitions` |
| Background render | ARQ workers (`video_maker`, `text_overlay_worker`) |
| Check status | `GET /videos/{id}` |
| Fetch result | `GET /videos/{id}/download` |

## Brand fit

Every render job names a **theme** that resolves brand colors, fonts,
lower-thirds, and progress-bar styling from the active brand pack
(`agency/brands/<slug>/brand-style.md`). See `THEMES.md`. A reel rendered
for any brand looks on-brand automatically — the operator only picks
clips and text.

## Ops notes

- QC every render like any other build: visually read the final before it
  ships. Contact-sheet style spot checks (a frame grid) catch bad overlays
  faster than scrubbing.
- Upstream ships systemd units for backend, frontend, and both workers —
  run the backend + workers as services for a 24/7 pipeline (pattern is the
  same as the livestream `VPS-SETUP.md`).
- Never put real stream keys, API keys, or personal data in configs or
  job JSON — placeholders only (see `API-PATTERN.md`).

## Source

Derived from [ronin1770/reel-quick](https://github.com/ronin1770/reel-quick)
(MIT). Docs only — nothing was copied verbatim, and the pipeline has not
been deployed on this box yet; the API pattern in `API-PATTERN.md` was
written from the upstream endpoint list.
