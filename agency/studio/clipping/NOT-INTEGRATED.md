# NOT INTEGRATED — openshorts (mutonby/openshorts)

**Status:** Excluded from the Gator Bait Agency. Nothing from this project was copied, vendored, or integrated.
**Decision date:** 2026-09-26
**Investigated by:** Studio workstream (clipping engine)

## What openshorts is (in our own words)

OpenShorts is a self-hosted AI video tool that takes a long-form video (a podcast, an interview, a live show) and automatically finds the moments most likely to go viral as vertical short-form clips. It picks clip candidates, detects who is speaking, tracks faces to keep them framed, reframes the footage into a 9:16 vertical layout, and generates burned-in subtitles (Whisper-style transcription). It also ships a web dashboard and claims agent-control hooks — MCP endpoints, API keys, and automation hooks (n8n-style) so agents or pipelines can drive clip jobs programmatically.

For the agency's purposes, it was a candidate reference architecture for a **long video in → viral shorts out** pipeline, with exactly the agent-control surface we want (submit a job, poll for clips).

## What the license investigation found

Cloned `https://github.com/mutonby/openshorts` (depth 1) on 2026-09-26 and read the license files in full.

**Root `LICENSE` — opens with a valid MIT header, then carves it back:**

> License name line: `MIT License`
> Copyright line: `Copyright (c) 2024 OpenShorts`
> Followed immediately by: an `EXCEPTION` stating that everything under the `cloud/` directory is licensed under a separate license defined in `cloud/LICENSE` (the OpenShorts Commercial License), *not* under the MIT text below.

**`cloud/LICENSE` — a source-restricted commercial license, which states in part:**

> License name line: `The OpenShorts Commercial License (the "Commercial License")`
> Copyright line: `Copyright (c) 2024-present OpenShorts (openshorts.app)`

It permits viewing, study, modification, and self-hosting for *personal or internal* business use only. Under "Prohibited use" it explicitly forbids, without a separate written agreement:

- offering the Commercial Software or derivatives to third parties as a hosted/managed/paid service, **"including but not limited to Software-as-a-Service, resale, white-labeling"**;
- selling, sublicensing, or **redistributing** the Commercial Software, on its own or as part of another product or service.

**The contradiction problem:**

1. The README badge claims plain `License: MIT`, and the README's feature table says self-hosted is "Free forever, MIT" — but the LICENSE file's own EXCEPTION removes `cloud/` from MIT coverage. The badge overclaims.
2. GitHub license detection returns **NOASSERTION** for the repo (non-standard license file with a custom EXCEPTION block defeats SPDX detection), so there is no machine-verifiable clean-MIT signal.
3. The exact components the agency needs — the agent-control surface (`cloud/api_keys.py`, `cloud/mcp_oauth.py`, `cloud/autopilot.py`, billing/metering, hosted API machinery) — live under `cloud/` and are the parts most explicitly prohibited from white-labeling and redistribution. Integrating the MIT-only remainder would give us a clipping engine **without** the MCP/API/n8n hooks the workstream calls for.
4. There is no clear individual author in the copyright lines ("OpenShorts" / "openshorts.app" — a product brand, not a person or company with a verifiable CLA chain), which muddies provenance of the MIT portion.

## Why it was excluded

The decision rule for this workstream is: integrate only on a **clean, whole-repo** MIT (or Apache-2.0) grant with a coherent copyright line. This repo fails that bar three ways:

- **Not whole-repo MIT** — a material subdirectory (the agent-control/API layer we actually want) is explicitly commercial-licensed and white-labeling it is forbidden.
- **Contradictory claims** — README badge says MIT; the license file says otherwise for `cloud/`; GitHub detects NOASSERTION. Contradiction = unverifiable.
- **The needed surface is the restricted surface** — we cannot strip out `cloud/`, take the MIT remainder, and still deliver the "MCP/API/n8n control hooks" the workstream requires. That would be integrating a degraded engine under a false pretense of full provenance.

White-labeling any part of this into the agency's white-label repo carries a license-compliance risk the task explicitly told us not to take. So: **nothing was integrated, no code was copied.**

## Recommended posture

- **Treat openshorts as inspiration-only.** Its pipeline architecture (ingest → moment detection → ranking → face-tracked 9:16 reframe → subtitle → QC → hand-off to reels) is a sound design to reimplement clean-room in the agency's own code, under the agency's own license. No source from openshorts enters the repo.
- **Do not self-host `cloud/`** in any client-facing or white-labeled offering without a written commercial agreement with the copyright holder.
- **If this changes:** the author would need to (a) relicense `cloud/` under a clean MIT/Apache-2.0 grant, or (b) grant Gator Bait Media a written white-label/redistribution agreement. Either would be grounds to reopen this file and do the integration.

## Update 2026-09-27: partial coverage from video-use (MIT)

[browser-use/video-use](https://github.com/browser-use/video-use) (MIT, © 2026 Browser Use) is now the agency's **edit** step: `agency/studio/video-edit/VIDEO-EDIT-RUNBOOK.md`. With a word-level transcript, an agent can propose which moments of a long video to cut, but a person approves the plan before any cut. It does **not** detect viral moments automatically, track faces or reframe to 9:16 on its own. So the automatic long-video-to-shorts engine is still a gap. Keep hunting.

Also evaluated 2026-09-27 and rejected (AGPL-3.0, LICENSE read): jub0t/Concat (a CapCut replacement with MCP) and calesthio/OpenMontage (agentic video production). See `agency/docs/SOURCES.md`.
