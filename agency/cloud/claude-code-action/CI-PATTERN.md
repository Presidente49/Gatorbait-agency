<!-- Source: anthropics/claude-code-action (https://github.com/anthropics/claude-code-action) — MIT. Adapted for Gator Bait Agency. -->

# Claude Code Action — CI Pattern for the Agency Repo

**What it is:** Anthropic's official GitHub Action that runs Claude Code on
PRs and issues — answers questions, implements changes, reviews code. MIT.
Triggers on @claude mentions, issue assignment, or scheduled automation;
authenticates via Anthropic API, Bedrock, Vertex, or Foundry; runs on your
own runner.

**Why it's here:** `FOR-CLAUDE-CODE.md` already invites Claude Code to review
the agency repo. This action makes that review *structural* instead of
manual — every PR and every push gets a reviewer that never sleeps.

**Recommended workflows for this repo:**

1. **Automatic PR review** — every PR touching `agency/` gets a Claude review
   against the repo's own standards: white-label completeness (no
   brand-specific leakage into shared paths), attribution headers present on
   borrowed material, license compliance (permissive licenses only — MIT, Apache-2.0, BSD, ISC; flag anything
   else), privacy grep (no emails/phones/secrets).
2. **Scheduled repo health check** — weekly run: verify every link in
   `SOURCES.md` still resolves, flag stale docs, check that each agent's
   identity files still match the white-label contract.
3. **@claude mentions** — Brenden or a maintainer can ask questions about the
   stack directly on issues/PRs and get answers with receipts.

**Custom review checklist** (encode as the action's prompt):

- Is anything brand-specific leaking into `agency/shared/` or templates?
- Does every borrowed file carry its attribution header?
- Is every new external source registered in `agency/docs/SOURCES.md` with a
  verified license?
- Privacy: any emails, phone numbers, secrets, revenue figures, personal data?
- Does the change match the white-label contract in `WHITE-LABEL.md`?

**Setup notes:** requires repo admin (Brenden) to install the GitHub App and
add the API secret once. After that it's autonomous. This is the standing
kind of work that should never wait on a human — wire it, then forget it.
