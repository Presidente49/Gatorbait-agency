<!-- Registry of every external open-source source evaluated for or integrated into the Gator Bait Agency. Future repo-shopping scans check against this list first — never re-evaluate without new information. -->

# External Sources Registry

| # | Repo | URL | License (verified) | What we took | Where it lives | Date |
|---|---|---|---|---|---|---|
| 1 | charlie947/social-media-skills | https://github.com/charlie947/social-media-skills | MIT (LICENSE read, © 2026 Charlie Hills) | 17 markdown skills adapted brand-agnostic, mapped to 8 agents | `agency/skills-library/` | 2026-09-27 |
| 2 | cgallic/visual-factory-kit | https://github.com/cgallic/visual-factory-kit | MIT (LICENSE read) | Template-family concept, brand-pack spec, QA + provenance runbooks (no code vendored) | `agency/studio/creative/` | 2026-09-27 |
| 3 | muneebkhan08/capite | https://github.com/muneebkhan08/capite | MIT (LICENSE read) | Offline Whisper → animated captions operator pipeline + style archetypes | `agency/studio/captions/` | 2026-09-27 |
| 4 | ronin1770/reel-quick | https://github.com/ronin1770/reel-quick | MIT (LICENSE read) | API-driven reel render pattern + example payloads, per-brand theme contract | `agency/studio/reels/` | 2026-09-27 |
| 5 | arifyaman/multistream | https://github.com/arifyaman/multistream | MIT (LICENSE read) | OBS → mediamtx → multi-RTMP runbook, VPS health pattern | `agency/studio/livestream/` | 2026-09-27 |
| 6 | Anil-matcha/Free-AI-Social-Media-Scheduler | https://github.com/Anil-matcha/Free-AI-Social-Media-Scheduler | MIT (LICENSE read, © 2023 Anil Chandra Naidu Matcha) | Positioned as white-label client dashboard; deploy + rebrand docs (app not vendored) | `agency/cloud/scheduler/` | 2026-09-27 |
| 7 | paperclipai/paperclip | https://github.com/paperclipai/paperclip | MIT (LICENSE read, © 2025 Paperclip AI) | Control-plane concepts: org chart, heartbeats, budgets, governance, Agent Companies spec; agency mapping + deploy docs (app not vendored) | `agency/cloud/paperclip/` | 2026-09-27 |

## Evaluated and REJECTED

| Repo | URL | Reason |
|---|---|---|
| mutonby/openshorts | https://github.com/mutonby/openshorts | LICENSE claims MIT but carves `cloud/` (api_keys, mcp_oauth, autopilot, billing) into a commercial license forbidding white-label/resale/redistribution; agent-control hooks live in the restricted dir; GitHub shows NOASSERTION. See `agency/studio/clipping/NOT-INTEGRATED.md`. |

## Rules for future scans

1. Read the full LICENSE file after cloning — never trust the badge alone (openshorts rule).
2. AGPL/GPL/copyleft and no-license repos: describe, never copy.
3. Every borrowed file carries an attribution header (repo, URL, license) as its first lines.
4. Add every new evaluation to this table, integrated or rejected, with the date.
