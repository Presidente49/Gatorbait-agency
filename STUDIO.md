# STUDIO — the production company behind the marketing team

The agency (8 agents) is the marketing team. The STUDIO is the production
company right behind it: the video factory that turns raw footage into
finished, on-brand, captioned short-form content at scale.

## The pipeline

```
RAW FOOTAGE
    │  (game film, show recordings, interviews, livestreams)
    ▼
agency/studio/clipping/     — long video → candidate shorts
    │  (viral-moment detection, 9:16 reframe, face tracking)
    │  NOTE: openshorts was EXCLUDED on license grounds —
    │  see clipping/NOT-INTEGRATED.md. This stage is currently
    │  a documented gap: manual clipping or a clean-room build.
    ▼
agency/studio/captions/     — transcription + animated captions
    │  (offline faster-whisper, word-level review, brand-locked styles,
    │  MP4/SRT/VTT/ASS export — zero per-video cost)
    ▼
agency/studio/reels/       — API-driven reel renderer
    │  (submit job: clips + theme + overlays → finished 1080×1920 reel)
    ▼
agency/studio/creative/    — deterministic brand creative engine
    │  (JSON request + brand pack → platform-ready PNGs:
    │  thumbnails, carousels, stories, ads — every render QA'd,
    │  every render carries a provenance file)
    ▼
PUBLISH  (Hype agent → scheduler → platforms)
```

A parallel track: `agency/studio/livestream/` — run a live show once
(OBS → media server → multi-platform RTMP) and feed the recording
straight back into the top of this pipeline.

## Who does what

| Stage | Owner | Does |
|---|---|---|
| Clipping | Scout + Scribe | Find the moments worth cutting; rank candidate shorts |
| Captions | Wrench | Run the pipeline; word-level review is the quality step |
| Reels | Blueprint | Art-direct themes; submit render jobs; QC output |
| Creative | Blueprint | Own the brand pack + template families; QA gate |
| Livestream | Webmaster | Own the chain, health checks, failover |
| Publish | Hype | Schedule approved content; never publishes unapproved work |

## Rules

- **Captions are non-negotiable.** Every short-form video ships captioned.
  Most viewers never unmute.
- **One brand pack per client.** All creative and reel themes read from
  `agency/brands/<slug>/` — never hardcode colors, fonts, or logos.
- **QA gate:** a render with `"passed": false` doesn't ship. Provenance
  file on every creative asset (template version, asset hashes, timestamp).
- **Footage stays on our machines** for the caption stage (offline
  transcription). Client footage is not training data for anyone's cloud.
- **The studio never publishes.** It produces. Hype publishes, and only
  what the operator/owner approved.
