<!-- Source: block/buzz (https://github.com/block/buzz) — Apache-2.0. Adapted for Gator Bait Agency. -->

# Buzz — Overview

**What it is:** Buzz (from Block) is a self-hostable workspace where humans
and AI agents share the same rooms. Under the hood it's a Nostr relay: every
message, reaction, workflow step, review approval, and git event is a signed
event in one log — same shape, same identity model, same audit trail, whether
the author is a person or a process. Apache-2.0, Rust.

**The concepts that matter for us:**

1. **Agents as teammates, not tools.** Agents have their own keys, their own
   channel memberships, their own audit trail — scoped by identity, the way
   you'd scope a teammate. "Let an agent triage without giving it the keys to
   the kingdom" is exactly our standing rule about what agents may touch.
2. **One event log.** Conversation, patch, workflow run, approval — all the
   same kind of event, searchable in one place. Our ops log
   (`ops/log/<date>.md` + `lessons.md`) is the markdown version of this
   instinct; Buzz shows what it looks like as infrastructure.
3. **The channel is the record.** Turn a campaign into a room where the brief,
   the drafts, the approvals, and the results live together — so the channel
   becomes the record of *why* the campaign exists.

**Agency mapping — the client room pattern:**

For white-label clients, the most valuable Buzz concept is the **shared
room**: a place where the client and the agents coordinate a campaign with
full receipts. The client asks a question, the agent answers with the threads
(the evidence), not vibes. Every agent action is signed and auditable, so
"what did the agency do this week?" is always answerable.

**Deploy path:** concepts now. If a client ever wants a window into the
machine, a Buzz-style room (or Buzz itself, self-hosted per brand) is the
pattern — not screenshots of chat logs.
