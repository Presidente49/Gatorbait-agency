# Mentor notes — targeted roundup 2026-09-28 (rows #150–156)

These are Marlow's teaching notes for Claude. Read them before touching any of the #150–156 integrations. The design directives in SOURCES.md are the spec; this file is the *judgment* — the stuff a senior tells a junior so the work lands right.

## Non-repo recommendations (do NOT become registry rows — no repo to register)

1. **Official Wix MCP** (`https://mcp.wix.com/mcp`) — Wix's own remote MCP: search Wix docs, write Velo/platform code, call site APIs. This is the strongest Wix lever available and it's a service, not a repo. Wire it into the agent stack as the primary Wix interface; `wix/velo-external-db` (#150) covers the data-sync half. Owner: site-data agent.
2. **Restream.io direct REST wrapper** — no MIT/Apache Restream-native client exists (verified: the BSD one failed the license rule, the MCP-server one was unverifiable, the a11y one is archived). Build a thin wrapper against the official Restream REST API using the endpoint table documented in `tonygeb23/restream-a11y`'s README as the reference (`/v2/user`, `/v2/user/events`, start/stop, channel updates, analytics). Owner: livestream agent. Acceptance: start/stop stream, list/update destinations, and pull analytics through one module with the token in the vault.

## Runner-ups (checked, not crowned — revisit when the need is real)

- **postalserver/postal** (16,831 stars, pushed 2026-09-19, API-level MIT — raw file NOT read): self-hosted mail-delivery platform, the Listmonk-class "pipe." Ghost (#151) covers the immediate newsletter need. Take Postal when sending volume justifies running your own MTA — a real ops commitment, not a weekend project.
- **datarhei/restreamer** (5,205 stars, pushed 2026-05-22, API-level Apache-2.0 — raw file NOT read): productized self-hosted streaming server with web UI + REST API. MediaMTX (#154) won on license-certainty and fit; restreamer is the fallback if the agency wants a UI-driven appliance instead of a config-driven engine.
- **puckeditor/puck** (13,372 stars, API-level MIT — raw file NOT read): visual React page builder. Cut because the main site builds natively in Wix; revisit for the real-estate vertical's landing pages.
- **dimsemenov/PhotoSwipe** (25,265 stars, MIT per API, pushed 2025-12-04): the canonical gallery lightbox. First alternate for the multimedia category; Wix's native galleries cover the near term.

## Rejections worth learning from (2026-09-28 roundup)

- `obsproject/obs-websocket` is **GPL-2.0**, not MIT — the license gate caught a misremembering. Never trust memory on licenses; read the file.
- `langchain-ai` acquisition note: Langfuse's copyright now reads "ClickHouse, Inc." (acquired 2026) and its core has an `ee/` carve-out — this is why we read LICENSE files, not badges.
- `knadh/listmonk` is AGPL-3.0: the obvious newsletter answer was wrong for white-label. The discipline of rejecting the obvious answer is what makes the registry trustworthy.

## THE NO-MORE-STATIC MANDATE (owner's order, 2026-09-28)

Brenden: "We should be having these really amazing looking websites. We don't have anything cool, nothing that's different, nothing that's amazing — moving backgrounds, no motion, nothing. It's just static."

This is now an acceptance criterion on every web-facing build:

- **Every page Claude builds must MOVE.** Scroll-triggered reveals, animated backgrounds, page transitions, living heroes — motion is not decoration, it's the difference between a site people remember and one they bounce from.
- **Premium motion, not cheap motion.** Cheap = everything sliding in from the left at once, spinners, bouncy easings. Premium = one confident hero moment, staggered reveals tied to scroll position, motion that serves the story (a stat counting up, a background drifting as you read). When in doubt, do LESS motion but do it perfectly.
- **Motion must survive the phone.** Brenden reads everything on his phone. If an effect tanks mobile performance or breaks touch, it's cut — no exceptions.
- **Static is a failed build.** If a page ships with zero motion, the QC gate fails it and it goes back. No debate.

A dedicated motion-design tool hunt is running to give Claude the actual ammunition (WebGL backgrounds, scroll-animation patterns, award-level components). When it lands, those rows join this registry and this mandate gets its toolbox.
