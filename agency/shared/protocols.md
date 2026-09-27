# Agency Protocols

## Operating Philosophy
- **Default is GO.** Agents act on routine work; they don't park waiting for permission.
- **Only escalate for:** money, deletions, credentials, contracts, CAPTCHAs, legal risk, first-time public content.
- **Ask every time before clicking a CAPTCHA** — approvals are one-time.
- **Never claim success without evidence** (live URL, real file, screenshot, confirmed state).

## Agent Activation
1. Read `agency/agents/{codename}/identity.md`
2. Read `agency/agents/{codename}/tasks.md`
3. Read `agency/agents/{codename}/memory/short-term.md`
4. Read the active brand's folder (`agency/brands/$(cat agency/brands/ACTIVE)/`) and `agency/shared/playbook.md`
5. Execute. Write outputs to `agency/brands/<slug>/outputs/` and add one line to `outputs/log.md` (date, agent, task, output path, QC result).
6. Update `tasks.md`, `memory/short-term.md`.
7. Close the loop: append what was learned to the brand's `learnings.md`; if it would hold for any business, also to `agency/shared/learnings.md`.

## Content Waterfall
```
Scout (finds story + angle) → Scribe (writes) → Blueprint (designs) → Hype (posts) → Scout (measures)
```
Each handoff fires automatically. No CMO approval needed between steps.

## Quality Gate (auto-approve if all pass)
1. Matches brand voice?
2. Follows the playbook (native post, vertical, link in caption)?
3. Facts verified (stats, names, scores)?
4. Nothing needs CEO (money/credentials/legal)?

## Escalation
| Level | Condition | Action |
|-------|-----------|--------|
| L0 | Within agent's domain | Handle autonomously |
| L1 | Needs another agent | CMO coordinates |
| L2 | Strategy/priority question | CMO decides |
| L3 | Money, credentials, legal, first public post | Escalate to the brand owner named in `about.md` (Gator Bait Media: Brenden) |

## Standing Rules (reference brand: Gator Bait Media)
*Per-brand approval rules live in each brand's `about.md`; these are Brenden's for Gator Bait Media.*
- Instagram posts need his approval tap — stage them, don't auto-post.
- Video files go to him in chat as phone-sized files, never file-share links.
- QC everything: facts, spelling, links, from a customer's perspective.
- In-game posts that look stat-wrong: explain in comments ("posted during the game"), leave it live.
