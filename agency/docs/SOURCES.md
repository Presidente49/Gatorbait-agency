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
| 8 | vectorize-io/hindsight | https://github.com/vectorize-io/hindsight | MIT (LICENSE read, © 2025 Vectorize AI, Inc.) | Agent-memory model: banks, retain/recall/reflect, evidence-backed observations; AGENCY-MEMORY-MODEL.md upgrades the learning loop (concepts only) | `agency/cloud/hindsight/` | 2026-09-27 |
| 9 | dream-num/univer | https://github.com/dream-num/univer | Apache-2.0 (LICENSE read) | "Office harness for AI agents" concept: agents write into real spreadsheets/docs/dashboards; agency mapping for Rank/Wrench/Blueprint outputs (concepts only) | `agency/cloud/univer/` | 2026-09-27 |
| 10 | block/buzz | https://github.com/block/buzz | Apache-2.0 (LICENSE read) | Human+agent shared rooms, one signed event log, agent identity scoping; client-room pattern for white-label transparency (concepts only) | `agency/cloud/buzz/` | 2026-09-27 |
| 11 | mobile-next/mobile-mcp | https://github.com/mobile-next/mobile-mcp | Apache-2.0 (LICENSE read) | MCP-driven native mobile automation; phone-only task pattern with hard approval rules (concepts only, no deployment) | `agency/cloud/mobile-mcp/` | 2026-09-27 |
| 12 | anthropics/claude-code-action | https://github.com/anthropics/claude-code-action | MIT (LICENSE read, © 2025 Anthropic, PBC) | CI pattern: automatic Claude Code PR review + weekly repo health check + @claude mentions, with agency-specific review checklist (concepts only) | `agency/cloud/claude-code-action/` | 2026-09-27 |
| 13 | coreyhaines31/marketingskills | https://github.com/coreyhaines31/marketingskills | MIT (LICENSE read, © 2025 Corey Haines) | Growth playbook system: CRO playbook, copy patterns + persuasion psychology, analytics loop + readback discipline, offer design (Value Equation), experiment runbook, 9-part marketing-loop spec + Tier-1/Tier-2 guardrails — all adapted brand-agnostic, mapped to owning agents | `agency/growth/` + `agency/skills-library/marketing/brand-first.md` | 2026-09-27 |
| 14 | ericosiu/ai-marketing-skills | https://github.com/ericosiu/ai-marketing-skills | MIT (LICENSE read, © 2026 Single Grain) | Closed-loop learning concepts: expert-panel quality gate (90+ recursive scoring) → scribe; content→revenue attribution (first-touch/linear/time-decay) → wrench; YouTube outlier analysis + packaging readback → scout/hype. Vendor code not vendored, telemetry stripped | `agency/skills-library/marketing/quality-gate.md`, `revenue-attribution.md`, `youtube-outliers.md` | 2026-09-27 |
| 15 | medusajs/medusa | https://github.com/medusajs/medusa | MIT (LICENSE read, © 2021 Medusajs; Enterprise materials carved out commercially, core is MIT) | Storefront platform comparison + Medusa v2 as agency merch default (concepts only) | `agency/merch/` | 2026-09-27 |
| 16 | legenki/print2medusa | https://github.com/legenki/print2medusa | MIT (LICENSE read, © 2026 Andy Legenki) | Printful→Medusa v2 integration pattern: event-driven order submit, webhook loop, live rates + fallback, parcel fulfillments | `agency/merch/PRINT-ON-DEMAND.md` | 2026-09-27 |
| 17 | greedychipmunk/medusa-plugin-printify | https://github.com/greedychipmunk/medusa-plugin-printify | MIT (LICENSE read, © 2026 Dawson Blackhouse) | Printify→Medusa v2 integration pattern; plugin structure (modules/providers/subscribers/workflows) | `agency/merch/PRINT-ON-DEMAND.md` | 2026-09-27 |
| 18 | amandamartin-dev/pdfkit-demo-wixstudio | https://github.com/amandamartin-dev/pdfkit-demo-wixstudio | MIT (LICENSE read, © 2024 Amanda) | Velo backend web-module pattern (webMethod + Permissions), npm-in-backend, page↔backend async UX lifecycle | `agency/cloud/wix/VELO-PATTERNS.md` | 2026-09-27 |
| 19 | cganh/openpage | https://github.com/cganh/openpage | MIT (LICENSE read, © 2026 Federico De Ponte) | JSON-first site documents (blocks/variants/themes), AI site-generation API pattern, agent-editable design formats | `agency/studio/web/WEB-DESIGN-TRENDS.md` | 2026-09-27 |

## Evaluated and REJECTED

| Repo | URL | Reason |
|---|---|---|
| mutonby/openshorts | https://github.com/mutonby/openshorts | LICENSE claims MIT but carves `cloud/` (api_keys, mcp_oauth, autopilot, billing) into a commercial license forbidding white-label/resale/redistribution; agent-control hooks live in the restricted dir; GitHub shows NOASSERTION. See `agency/studio/clipping/NOT-INTEGRATED.md`. |
| vendure-ecommerce/vendure | https://github.com/vendure-ecommerce/vendure | GPLv3 Community Edition default (LICENSE.md read — third-party writeups claiming MIT are stale); copyleft incompatible with white-label. See `agency/cloud/vendure/NOT-INTEGRATED.md`. |
| saleor/saleor | https://github.com/saleor/saleor | BSD 3-Clause (LICENSE read) — permissive, no copyleft risk, but outside the strict MIT/Apache-2.0 allow-list. Re-evaluate first if policy widens. See `agency/cloud/saleor/NOT-INTEGRATED.md`. |
| loeiks/awesome-wix | https://github.com/loeiks/awesome-wix | No LICENSE file (unlicensed) — described, never copied. See `agency/cloud/awesome-wix/NOT-INTEGRATED.md`. |
| amandamartin-dev/velo-tensorflow | https://github.com/amandamartin-dev/velo-tensorflow | No LICENSE file (unlicensed); same author's MIT repo integrated instead. See `agency/cloud/velo-tensorflow/NOT-INTEGRATED.md`. |
## Rules for future scans

1. Read the full LICENSE file after cloning — never trust the badge alone (openshorts rule).
2. AGPL/GPL/copyleft and no-license repos: describe, never copy.
3. Every borrowed file carries an attribution header (repo, URL, license) as its first lines.
4. Add every new evaluation to this table, integrated or rejected, with the date.
