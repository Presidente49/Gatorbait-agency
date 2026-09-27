<!-- Source: mobile-next/mobile-mcp (https://github.com/mobile-next/mobile-mcp) — Apache-2.0. Adapted for Gator Bait Agency. -->

# mobile-mcp — Overview

**What it is:** An MCP server that lets agents and LLMs drive native iOS and
Android apps — simulators, emulators, and real devices — through a
platform-agnostic interface. Accessibility-first (reads the native
accessibility tree, no vision-model tokens burned), with screenshot +
coordinate fallback. Works with Claude Code, Codex, Gemini, Copilot, or any
MCP client. Apache-2.0.

**The concept that matters for us:** some doors only open from a phone.

Meta Business Suite, Instagram native features, app-only publishing flows,
2FA-gated settings screens — the agency repeatedly hits tasks that are
phone-only. Today those wait on Brenden's thumbs. mobile-mcp is the pattern
for the day an agent needs its own hands on a device: taps, swipes, form
fills, deep links, screen recording, structured UI extraction.

**Rules of engagement (non-negotiable):**

1. A device-driving agent acts *as* the brand's operator — every action it
   takes is attributable. Approval gates from the Paperclip model apply
   doubly here.
2. Never drive auth flows, payment screens, or account-deletion paths without
   explicit human approval per action. No standing authorization, ever.
3. Accessibility-tree first: deterministic UI reads beat screenshots for both
   cost and reliability.
4. One device profile per brand — never mix brand sessions on one device.

**Deploy path:** not today. This is a capability to reach for when a
phone-only task becomes a bottleneck (e.g. a recurring native-app publish
flow). Needs a Mac (Xcode + simulator) or Android SDK host on the LAN, or a
cloud-device provider. Document the need first; deploy when the ROI is obvious.
