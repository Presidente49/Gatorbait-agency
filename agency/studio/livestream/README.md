<!-- Source: arifyaman/multistream (https://github.com/arifyaman/multistream) — MIT. Adapted for Gator Bait Agency. -->
# Livestream — OBS → relay → multi-platform RTMP, supervised

One machine or VPS supervises the whole live chain: OBS publishes once to
a local media-server relay, and the relay re-broadcasts to every platform
(YouTube, Twitch, etc.) over RTMP — with health checks and isolated
failures per destination.

## Architecture

```
OBS ──RTMP (one upload)──▶ mediamtx :1935 ──┬──▶ ffmpeg ──▶ YouTube
                        (relay)             ├──▶ ffmpeg ──▶ Twitch
                                            └──▶ ffmpeg ──▶ …
```

- **Upload once** — OBS pushes a single stream; your upload bandwidth stays
  flat no matter how many destinations you add.
- **Identical stream** — same bitrate/resolution/encoder everywhere.
- **Failures isolated** — one platform dropping does not affect the others.
- **Supervised** — one daemon spawns and watches an ffmpeg per platform
  (`-c copy`, no re-encoding) and optionally the relay itself.

## Commands

| Command | What it does |
|---|---|
| `status` | One-shot health table; exits `0` = healthy, `1` = anything down. `--watch` refreshes, `--json` for scripting. |
| `check` | Deployment probe: relay API reachable, daemon running, endpoints TCP-reachable, key files exist, away file present. |
| `daemon` | Run the supervisor in foreground (keep alive with systemd — see `VPS-SETUP.md`). |
| `restart <platform\|relay>` | Restart one destination or the relay (resets the restart limit). |
| `switch [profile]` | Show or set the enabled profile; restart the service to apply. |
| `config` | Print effective config — key values are **never** read or printed. |

## Keys & config

- One JSON config file; keys live in **0600 files** under a `keys_dir`
  (one `<platform>.env` per platform, `NAME=VALUE` lines). The config holds
  only `${NAME}` templates — never real keys.
- **Profiles** let multiple shows share one relay, each with its own ingest
  path, keys, and platforms (e.g. a profile per show).
- **Away file:** when OBS is not publishing, the relay can loop a short MP4
  on the ingest path so the channels show something instead of dead air.

## How it fits the agency pipeline

```
livestream (this) ──▶ recording ──▶ clipping pipeline ──▶ reels
      ▲                                                   ▲
  talk shows,        post-stream wrap feeds the same      agency/studio/reels/
  game-day shows      clip → caption → render flow
```

The live show is the content factory's front door. See `RUNBOOK.md` for
the full show-day procedure and `VPS-SETUP.md` for 24/7 deployment.

## OBS settings that matter

- **Encoder:** H.264 (x264 or hardware). **Not HEVC** — platforms reject
  H.265 RTMP ingest.
- **B-frames: 0** — a common silent failure is "stream is up but nobody can
  watch"; B-frames are the usual cause.
- **Rate control:** CBR, 6000 kbps is a safe ceiling for non-partner
  Twitch, Kick, and YouTube.
- **Resolution/audio:** 1080p30/60, AAC 160 kbps.

## Source

Adapted from [arifyaman/multistream](https://github.com/arifyaman/multistream)
(MIT). Docs only — distilled from the upstream README and config examples;
no source copied.
