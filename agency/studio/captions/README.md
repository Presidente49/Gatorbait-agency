<!-- Source: muneebkhan08/capite (https://github.com/muneebkhan08/capite) — MIT, Copyright (c) 2026 Capite Contributors. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Caption Pipeline — Local AI Captions for Video

## What it is

The caption pipeline is the agency's **self-hosted animated caption studio**.
It turns spoken video into editable, word-timed animated captions and exports
burned-in MP4, SRT, VTT, TXT, and ASS — with **zero per-video cost** and
**footage that never leaves our machines**.

It replaces paid per-video caption services (Submagic, CapCut auto-captions,
OpusClip-style caption tiers) with software we run, audit, and own.

## How it works

Three stages, all local:

1. **Transcribe.** `faster-whisper` (a CTranslate2-optimized Whisper
   implementation) produces millisecond-accurate word timestamps, offline, in
   100+ languages with automatic language detection. No API keys, no upload.
2. **Style.** The transcript is converted into an animated subtitle script
   (`pysubs2` + ASS). Words are grouped into short lines; each spoken word gets
   an animation tag (word highlight, karaoke wipe, pop, bounce, neon glow, and
   more). A live phone-mockup preview shows exactly how it will look before
   rendering.
3. **Render.** FFmpeg with `libass` burns the subtitle layer into the video at
   visually lossless quality (CRF 18, original audio stream-copied). Standard
   subtitle files (SRT/VTT/TXT/ASS) export alongside for editors and platforms.

## The studio loop (the part that makes it fast)

Transcription is the slow step (minutes). Everything after it is seconds:

- **Word-level transcript editor** — click any word to jump playback to it,
  fix typos and names inline, nudge timings ±0.1s, find-and-replace.
- **Instant in-place re-render** — change words, pick a new style, move caption
  position: the pipeline *skips transcription* and re-burns in seconds.

This means the real workflow is: transcribe once, iterate on words and style
cheaply, export everything.

## Key properties

| Property | Detail |
|---|---|
| **Cost** | $0 per video. One machine, Dockerized. No credits, no subscription, no watermark. |
| **Privacy** | Transcription and rendering happen on our hardware. Client footage is never sent to a third-party caption service. |
| **Accuracy** | Word-level millisecond timestamps; human review step before render. |
| **Languages** | 100+ via Whisper; script-aware font fallback (Latin, CJK, Arabic, Devanagari, Thai, Hebrew, Cyrillic). |
| **Exports** | Burned-in HD MP4 + `.srt` (editors/YouTube) + `.vtt` (web) + `.txt` (show notes) + `.ass` (styled subtitles). |
| **Vertical-first** | Layout math is calibrated for 9:16 (1080×1920); horizontal works, vertical is the design target. |
| **Caption styles** | 27 built-in animated presets across Trending / Clean & Tech / Editorial & Film / Pop & Expressive categories. See `STYLES.md`. |

## Deployment shape

Docker Compose, one host: a web studio (frontend, port 3000) + a Flask backend
(port 5000) that runs the transcription/render worker. Configurable limits —
max file size, max duration, concurrent jobs, output retention TTL, Whisper
model size (`tiny` → `large-v3`). Keep the backend off the public internet:
there is no auth layer by design; it is a single-user local tool.

## Where it fits the agency

The caption pipeline sits **between the edit and the reels step**: finished
video goes in, captioned video (plus SRT for platforms that want sidecar
captions) comes out, ready for the distribution workflow. The full operator
runbook is `PIPELINE.md`; the style system is `STYLES.md`.

## Reference

- `PIPELINE.md` — step-by-step operator runbook
- `STYLES.md` — the animated caption style system
- Source: [capite](https://github.com/muneebkhan08/capite) — MIT
