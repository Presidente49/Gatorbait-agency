# NOT INTEGRATED — Concat (jub0t/Concat)

**Status:** Excluded from the Gator Bait Agency. Nothing from this project was copied, vendored, or integrated.
**Decision date:** 2026-09-27
**Investigated by:** trending-repo-watch (hourly scan)

## What Concat is (in our own words)

Concat is a free, open-source, cross-platform video editor pitched as a CapCut replacement (macOS, Windows, Linux, Android). Native Rust engine with GPU compositor; covers the short-form workflow: auto-captions (local Whisper), text-to-speech + voice cloning, background removal, keyframe animation, 170+ GPU effects/transitions, multi-track timeline, 4K export. Exposes a JSON-RPC, gRPC, and **MCP API** plus a CLI so scripts and AI agents can cut video programmatically. For the agency it was the leading candidate to fill the known clipping-engine gap (openshorts was excluded on license grounds).

## Why it was excluded

The GitHub license page for jub0t/Concat reports **GNU Affero General Public License v3.0 (AGPL-3.0)** (repo badge and README badge both say AGPL-3.0-or-later). AGPL's network-copyleft clause is incompatible with the white-label agency model: any hosted service built on it for clients would trigger source-disclosure obligations. Per the SOURCES.md vet rule, AGPL repos are described, never copied.

## If the license ever changes

Re-evaluate only if the project relicenses the engine to MIT/Apache-2.0 without carve-outs. Do not re-evaluate on GitHub-detected badges alone — re-read the LICENSE file.
