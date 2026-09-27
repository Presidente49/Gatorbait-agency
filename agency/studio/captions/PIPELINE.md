<!-- Source: muneebkhan08/capite (https://github.com/muneebkhan08/capite) — MIT. Adapted for Gator Bait Agency. -->

# Caption Pipeline — Operator Runbook

The step-by-step procedure an agent or operator follows to take a finished
video through captions and hand it to the reels step. Nothing here uploads
footage anywhere — every step runs on our own host.

## 0. Pre-flight

- Confirm the caption studio is running: web UI reachable at
  `http://localhost:3000`, backend healthy (`GET /api/health`).
- Confirm the input video is final: correct cut, correct audio mix, no
  placeholder audio. Captions bake to word timings — re-editing the cut after
  captioning means re-running transcription.
- Check limits for the job: file size and duration within the instance config
  (defaults 500 MB / 30 min; adjustable via environment), Whisper model size set
  for the quality/speed tradeoff needed.

## 1. Ingest

1. Open the studio and drag the finished video (`.mp4`, `.mov`, or `.webm`)
   into the upload dropzone.
2. Pick a **starting caption style** — it can be changed freely later without
   re-transcribing, so pick the closest brand fit and move on. (See `STYLES.md`.)
3. Set the **caption position** (vertical placement on screen, e.g. bottom
   third for vertical video; keep clear of platform UI overlays like the
   like/comment rail and the progress bar).
4. Click **Generate Captions** and let the pipeline run:
   probe → transcribe (`faster-whisper`, word timestamps) → build ASS script →
   burn-in (FFmpeg + libass, CRF 18).

## 2. Transcribe (automatic — monitor, don't babysit)

- The worker reports progress per stage; transcription is the long pole
  (CPU-bound, serialized by the concurrent-job limit).
- When the Studio Editor opens automatically, transcription is done.

## 3. Review and edit — word level (the quality step)

This is the step that separates agency output from auto-caption sludge. Do not
skip it.

1. **Read the whole transcript** while the video plays. Use click-to-seek on
   word chips to jump to any moment.
2. **Fix every error:**
   - Names, brands, and technical terms (transcription mangles these first —
     player names, coach names, show names).
   - Homophones and punctuation that changes meaning.
   - Use find-and-replace for repeated misspellings.
3. **Check timings:** nudge segment boundaries ±0.1s where a caption lands
   early/late on a cut or a beat.
4. **Check line breaks:** words are packed into short lines (max 2); if a line
   reads awkwardly, adjust. Keep captions out of faces and lower-third
   graphics.
5. Set text casing per brand convention (e.g. UPPERCASE for hype cuts, Title
   Case for interviews).

## 4. Pick the style

1. Choose the style per the brand's caption style guide — or, if none exists
   yet, per `STYLES.md` archetypes: which of the 7 motion engines and which
   color family fits the brand and the video's energy.
2. Preview in the **live phone mockup** against a representative frame of the
   actual video (not just the mock backdrops). Check:
   - Readability over the busiest background in the video.
   - Active-word highlight is visible but not garish at phone size.
   - Position doesn't collide with faces, logos, or platform chrome.
3. Fine-tune only if needed: font, weight, casing, colors, outline, position.
   Prefer the brand's locked preset over one-off tweaks — consistency across a
   client's catalog matters more than per-video flair.

## 5. Render

1. Click **Apply & Re-render**. This skips transcription and re-burns from the
   edited transcript — seconds, not minutes.
2. Watch the finished burn once through at 1x: captions track speech, no
   overlapping lines, no words stuck on screen across a cut, no emoji or
   rendering artifacts (emoji are stripped at generation — confirm nothing
   important was lost).
3. If anything is off, fix the transcript/style and re-render again. Re-renders
   are cheap; a published typo is not.

## 6. QC

- [ ] Every spoken word that matters is captioned; no dropped sentences
- [ ] Names, brands, terms spelled correctly
- [ ] Timings track speech (no early/late captions on cuts)
- [ ] Style matches the brand's caption preset; position clears platform UI
- [ ] Full watch-through of the burned video at 1x with no artifacts
- [ ] Exports verified: burned MP4 plays; SRT opens clean in a text editor
      (spot-check timestamps); VTT/TXT/ASS present if the distribution plan
      needs them

## 7. Hand to the reels step

Deliver the finished package to the reels/distribution workflow:

- **Burned-in MP4** — the primary deliverable for Reels/TikTok/Shorts.
- **SRT** — for platforms or editors that want toggleable sidecar captions
  (and for YouTube uploads where burned-in isn't wanted).
- **Transcript TXT** — feeds show notes, article copy, and SEO descriptions.
- Note the **style ID and version** used (in the handoff message or filename),
  so the next video in the series matches.

## Failure handling

| Symptom | Response |
|---|---|
| Transcription stalls (job never completes) | Check backend logs; restart the worker. Note: stuck jobs can hold a concurrency slot — clear before re-queueing. |
| Burned captions don't match the preview | Font mismatch: the render host must have the style's fonts installed (libass silently substitutes otherwise). Fix fonts, re-render. |
| Gibberish transcript on music/noise | Whisper hallucinates on non-speech. Trim or mute non-speech sections and re-transcribe, or delete the phantom segments in the editor. |
| Wrong language detected | Override the language at ingest; check script-aware font fallback for non-Latin scripts. |

## Reference

- `README.md` — what the caption pipeline is
- `STYLES.md` — the animated caption style system
- Source: [capite](https://github.com/muneebkhan08/capite) — MIT
