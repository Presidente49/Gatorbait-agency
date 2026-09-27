<!-- Source: ronin1770/reel-quick (https://github.com/ronin1770/reel-quick) — MIT, Copyright (c) 2026 ronin1770. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Reel API Pattern

The render flow, adapted from reel-quick's REST API. Examples below are
**illustrative** (written for the agency, not copied from upstream).
Base URL in examples: `http://localhost:8000`.

## Render flow

1. Create the job → `POST /videos`
2. Attach source clips in order → `POST /video-parts`
3. Attach text overlays/captions → `POST /videos/{video_id}/text-overlays`
4. Start the render → `POST /videos/{video_id}/enqueue`
5. Poll status → `GET /videos/{video_id}`
6. Download the finished reel → `GET /videos/{video_id}/download`

### 1. Create the job

```http
POST /videos
Content-Type: application/json
```

```json
{
  "video_title": "Sumrall presser — work the cut",
  "video_size": "1080x1920",
  "video_introduction": "Hook: strongest punchline first",
  "transition_name": "slam-cut",
  "transition_duration": 0.25,
  "theme": "gator-bait-media",
  "video_tags": ["reel", "sumrall", "presser"],
  "active": true
}
```

Response: the job record with `video_id` (hex string), `status: "created"`,
`output_file_location: null`.

### 2. Attach source clips (in play order)

```http
POST /video-parts
Content-Type: application/json
```

```json
{
  "video_id": "<video_id from step 1>",
  "part_order": 0,
  "source_path": "/mnt/cuts/sumrall_workthecut_01.mp4",
  "trim_start": "00:00:04.200",
  "trim_end": "00:00:11.800",
  "transition_name": "slam-cut"
}
```

Repeat for each clip, incrementing `part_order`. Trim before render — the
worker assembles the parts in order.

### 3. Attach text overlays / captions

```http
POST /videos/<video_id>/text-overlays
Content-Type: application/json
```

```json
{
  "overlays": [
    {
      "kind": "caption",
      "text": "WORK THE CUT.",
      "start": 0.0,
      "end": 2.4,
      "style": "caption-pop"
    },
    {
      "kind": "lower-third",
      "text": "Jon Sumrall — Florida Gators head coach",
      "start": 2.4,
      "end": 7.0,
      "style": "lower-third-brand"
    }
  ]
}
```

`kind: "caption"` is burned-in dialogue text (for muted viewing).
`kind: "lower-third"` is the branded name strap. Named `style`s come from
the active theme — see `THEMES.md`.

### 4. Start the render

```http
POST /videos/<video_id>/enqueue
```

The job enters the Redis/ARQ queue; the `video_maker` worker picks it up
and renders with FFmpeg.

### 5. Poll status

```http
GET /videos/<video_id>
```

```json
{
  "video_id": "…",
  "status": "rendering",
  "output_file_location": null,
  "error_reason": null
}
```

`status` moves `created → rendering → done` (or an error state with
`error_reason` set). On error, `POST /videos/<video_id>/retry`.

### 6. Download the result

```http
GET /videos/<video_id>/download
```

Returns the finished MP4. Post-process before publish: verify it is
1080×1920, ~9–18MB (CRF 24 H.264, +faststart) for Instagram staging,
and visually QC it.

## Supporting endpoints

| Endpoint | Use |
|---|---|
| `GET /available-transitions` | list registered transition names |
| `POST /available-transitions` | register a new FFmpeg transition |
| `GET /videos/{id}/text-overlays` | inspect current overlays |
| `GET /videos/{id}/text-overlays/download` | overlay-only preview pass |
| `PATCH /videos/{id}`, `DELETE /videos/{id}` | edit / retire a job |

## Placeholders, always

Job JSON, configs, and sample env files must use placeholders — e.g.
`"/path/to/clip.mp4"`, `"YOUR_API_KEY"` — never real keys, emails, or
personal data. Upstream ships a `sample.env`; the agency's rule is the
same: real secrets live only in the operator's local env, never in the repo.

## Source

Adapted from [ronin1770/reel-quick](https://github.com/ronin1770/reel-quick)
(MIT) — endpoint names/verbs mirror the upstream API; request bodies are
agency-authored illustrations, not upstream fixtures.
