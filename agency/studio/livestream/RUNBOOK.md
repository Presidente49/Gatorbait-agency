<!-- Source: arifyaman/multistream (https://github.com/arifyaman/multistream) — MIT, Copyright (c) 2026 xlip. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Livestream Runbook — show day, step by step

The full procedure for a live production (talk show, game-day show).
Operator works this list top to bottom.

## Pre-stream checklist (30+ min before air)

- [ ] Run `multistream check` — green on all probes: relay API reachable,
      daemon running, endpoints TCP-reachable, key files exist, away file present.
- [ ] `multistream status` shows every destination healthy.
- [ ] Correct profile active (`multistream switch` shows the right show).
- [ ] OBS settings confirmed: H.264 encoder (not HEVC), **b-frames 0**,
      CBR ~6000 kbps, 1080p30/60, AAC 160 kbps.
- [ ] OBS pushes to the relay's ingest path (`rtmp://<relay>:1935/live/<name>`),
      not directly to a platform.
- [ ] Away file in place so channels aren't dead if OBS drops pre-show.
- [ ] Local recording enabled in OBS (this is the clipping source).

## Starting the chain

1. Ensure the daemon is running (`daemon` under systemd for 24/7 — see
   `VPS-SETUP.md`; it should already be up).
2. `multistream status` — all destinations green.
3. Start OBS → begin streaming to the relay ingest path.
4. Watch `multistream status --watch` for 60 seconds: relay ingests,
   every platform ffmpeg connects, no restarts.
5. If any destination shows down: `multistream restart <platform>` and
   re-watch. Escalate only if the restart loop trips (see Failover).

## Monitoring during the show

- Keep `multistream status --watch` on a second screen, or poll
  `status --json` on a cadence from your alerting.
- Green = leave it alone. The supervisor restarts dropped ffmpeg
  processes automatically up to its limit.
- Watch for: a single platform flapping (its problem, isolated — other
  destinations unaffected), or ALL platforms red (your relay or network —
  check OBS and the relay first).

## Failover — when a destination drops

1. One platform red, others green → it's the platform, not you.
   `multistream restart <platform>`; it usually reconnects on the next
   ingest cycle.
2. Restart hits its limit (daemon stops retrying a flapping destination)
   → leave it down, note it in the show log, keep the show going on the
   healthy platforms. Re-add it next show.
3. **All platforms red** → the failure is upstream of the relay: check OBS
   first (still streaming?), then the relay, then your network.
4. OBS crashes mid-show → restart OBS and re-push; the away-file loop
   covers the gap on channels if configured.

Never touch a healthy destination during a show to "fix" a broken one.

## Post-stream wrap

1. `multistream status` one last time — log which destinations were up
   for the whole show.
2. Stop OBS streaming; the away loop takes over the channels.
3. Grab the **local recording** — this is the master asset.
4. Recording → clipping pipeline: cut segments → captions →
   `agency/studio/reels/` render → publish per the Meta playbook.
   (A 2-hour show is a week of reels — clip the moments, don't post the
   whole thing.)

## Key rotation

Keys live in 0600 files (`<platform>.env` under `keys_dir`), never in the
config. To rotate: edit the key file, restart the daemon. The key is
resolved once at daemon start.

## Source

Adapted from [arifyaman/multistream](https://github.com/arifyaman/multistream)
(MIT). Procedures follow the upstream command model and OBS guidance.
