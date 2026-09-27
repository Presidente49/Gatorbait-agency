<!-- Source: browser-use/video-use (https://github.com/browser-use/video-use) — MIT, Copyright (c) 2026 Browser Use. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
<!-- Concepts and production rules from SKILL.md (commit b877063), restated for the agency. No code vendored. Tested 2026-09-27: 26/26 upstream tests pass; a two-cut render with burned captions produced the expected 4.54 s output. -->
# Video Edit Runbook: Raw Footage In, Finished Cut Out

**Owner:** blueprint (creative), with hype receiving the approved cut for publishing.
**Where it sits:** `clipping → captions → reels → publish`. This runbook is the
**edit** step for footage a person has already picked. It does not solve the
open clipping gap (finding the best moments in a long video on its own), see
`../clipping/NOT-INTEGRATED.md`.

**Upstream tool (optional):** [video-use](https://github.com/browser-use/video-use)
is a Claude Code skill that runs this whole loop. The agency uses its rules and
process; install the tool per client only when that client needs it (it is MIT,
so white-label use is fine). It needs `ffmpeg`/`ffprobe`, Python and an
ElevenLabs API key for word-level transcripts. The key lives in the tool's
`.env` on the operator's machine, never in a brand folder or this repo.

## The loop (never skip step 4)

1. **Inventory.** Probe every source (length, resolution, frame rate, portrait
   or landscape). Transcribe each once, word level, and cache it per source.
2. **Pack the transcript.** One phrase per line with `[start-end]` times,
   breaking on silence of 0.5 s or more or a speaker change. The editor reads
   this, not the raw JSON.
3. **Talk it through.** Say what the footage is in plain English and ask the
   questions this footage raises: target length and shape, must-keep and
   must-cut moments, brand look, subtitle style.
4. **Propose the strategy in 4–8 sentences and wait for a yes.** No cut
   happens before the person approves the plan.
5. **Execute.** Build the edit decision list (source, start, end, beat per
   range), grade per segment, add overlays, then render.
6. **Self-check before showing anyone** (see below). Cap at 3 fix passes,
   then report what is still wrong.
7. **Iterate on feedback, never re-transcribe.** Append decisions to the
   brand's `project.md` in the edit folder, and transferable lessons to the
   brand's `learnings.md`.

## Hard rules (correctness, not taste)

| # | Rule | What breaks without it |
|---|---|---|
| 1 | Burn subtitles **last**, after every overlay | Overlays cover captions |
| 2 | Extract each segment, then join losslessly | Every overlay re-encodes the whole video |
| 3 | 30 ms audio fade in and out at every cut | An audible pop at each cut |
| 4 | Shift each overlay so its first frame starts at its window | The middle of the animation shows |
| 5 | Caption times = word start − segment start + segment's place in the output | Captions drift after the first cut |
| 6 | Never cut inside a word; snap to word boundaries | Clipped syllables |
| 7 | Pad every cut edge 30–200 ms | Transcript timing drifts 50–100 ms |
| 8 | Word-level, verbatim transcripts only (keep the "um"s) | You lose the gaps that tell you where to cut |
| 9 | Transcribe each source once and cache it | Wasted cost, changed timings |
| 10 | Approved plan before any cut | Rework and wasted renders |
| 11 | Session output goes in `<footage>/edit/`, never in the tool folder | Client footage mixed into the tool |

## Cut craft (defaults, not mandates)

- Cut from the audio first: word boundaries and silences. Silences of 400 ms or
  more are the cleanest; under 150 ms is mid-phrase and unsafe.
- Keep the reaction after the punchline; the laugh is the beat.
- Leave 400–600 ms of air when the speaker changes.
- Every cut has to work for picture and sound together.

## Self-check before anyone sees it

Check the **rendered file**, not the sources:

- A filmstrip and waveform around every cut (±1.5 s): no flash or jump, no
  waveform spike, no caption hidden behind an overlay.
- The first 2 s, last 2 s and 2–3 points in the middle: grade and captions
  consistent and readable at phone size.
- Duration matches the edit list.
- **Measure loudness, don't guess:** `ffmpeg -i out.mp4 -af ebur128=peak=true
  -f null -`. Social target: about −14 LUFS integrated, −1 dBTP peak. An end
  card 15 dB under the dialogue is a bug. An agent cannot listen, so it reports
  the numbers.
- For anything that will be published, one fresh reviewer (a person or a
  separate agent) gets the file and the edit list with one brief: "find what is
  wrong", ranked with timecodes.

## Gates before publish (agency rules on top of the tool)

- **Rights:** every source clip and music bed has a known owner and permission.
  Brand rules on league/school footage apply (embed-only where the brand says
  so). No coach or player likeness in anything that sells merch.
- **No invented captions:** burned captions come from the transcript. A
  caption that fixes a quote needs a person to check it against the audio.
- **Resolution:** the tool renders 1080p by default; a 720p source gets
  upscaled. Say so in the hand-off instead of calling it native 1080p.
- **Approval:** the cut goes to hype as a draft. Publishing follows the brand's
  approval rules in `about.md`.

## Hand-off to hype

`edit/final.mp4`, the caption file, the loudness numbers, the source list with
rights notes, and one line on what the cut is for.
