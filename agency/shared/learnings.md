# Agency Learnings — transferable across every brand

These are earned principles, not theory. They were learned running Gator Bait
Media (a Florida Gators sports media business, 27K Facebook followers,
monetized via Meta Content Monetization) and they apply to any business
this agency runs. New learnings append here; brand-specific learnings live
in each brand's own `learnings.md`.

## Content & distribution

- **Never post a bare link.** Build the native post: original hook + excerpt
  copied into the post + native image/video + URL at the end. Native posts
  earn reach; link drops get buried.
- **Every post links to something** — the store, the site, an article.
  No linkless posts, ever. Every impression should have somewhere to go.
- **Stat-led hooks beat quote-led hooks for reach; clean photos beat
  headline graphics for engagement.** (Hypothesis from Sep 2026 A/B test —
  confirm per brand, don't assume.)
- **Real photography beats polished graphics.** Audiences trust photos;
  over-designed creative reads as an ad and gets scrolled past.
- **Video hook in the first 2–3 seconds, captions burned in.** Most
  viewers never unmute.
- **Keep vertical-video text out of the top/bottom overlay zones**
  (profile info, captions, and buttons cover them).
- **Max 5 hashtags.** More looks desperate and adds nothing.
- **Game day / event day is the exception** to normal posting-frequency
  restraint. When the audience is live and emotional, post.
- **Stale content kills trust.** Audit in-game posts after the final
  whistle: explain in the comments that a post went up mid-event, correct
  the record, leave it live. Deleting looks like hiding.

## Engagement

- **Reply to comments as the brand, fast.** Early replies double as
  distribution — every reply re-surfaces the post.
- **One reply per comment, max.** Short, warm, in the brand's voice.
- **Engage the critics playfully; skip the abusers.** Rival-fan smack
  talk and troll bait drive the most interaction when met with confident
  humor. Genuine hate, threats, and spam get nothing — liability, not
  engagement.
- **Invite post engagers to follow the page.** Cheapest follower
  acquisition there is.
- **Never promise anything in a reply** you can't deliver.

## Testing

- **Run everything as an A/B test until you have a winner.** Change one
  variable at a time (hook style OR image style, never both).
- **Organic only for tests.** Boosting contaminates the data.
- **Same article, same URL per variant pair** — the only difference is
  the hook and the image.
- **Space variants apart** so they don't cannibalize each other's reach.
- **Record results in a tracking sheet** (reach, reactions, comments,
  shares, link clicks) ~24h after posting, then write the report naming
  the winner and the new default format.

## Operations

- **Default answer is GO** for reversible work. Only stop for: money
  movement, deletions, credentials, contracts, or the irreversible.
- **Never claim success without evidence** — a live URL, a screenshot,
  an existing file. "Done" means verifiable.
- **Log everything**: task, actions, outputs + paths, status, QC result.
  If it isn't logged, it didn't happen.
- **QC like a customer, not like the author.** Read the site as a
  stranger would: misspellings, stale framing, broken links, wrong stats.
  Stats errors are the fastest way to lose credibility — verify against
  the final box score and multiple sources.
- **API-safe fixes can be automated; editorial copy changes get staged**
  as exact copy-paste fixes unless there's a tested, reversible path.
- **Pace outbound distribution** (~1 group share/hour) with varied
  captions so the algorithm doesn't read it as spam.

## Monetization

- **The Page is where the money is; groups are distribution.**
  Groups have no direct ad payouts — they exist to funnel eyeballs to
  monetized surfaces.
- **One post per asset.** Splitting content across posts maximizes
  revenue-share surface area.
- **Short-form feeds long-form.** Reels/Shorts drive subscribers and
  watch time; long-form descriptions link back to owned properties.
- **Never use someone's likeness to sell product** without a clear
  right to do so. Editorial use and commerce are different legal
  universes — when in doubt, ask.

## Borrowed infrastructure (Sep 2026 integration round)

- **Skills beat job descriptions.** Giving an agent a focused skill file
  (hook generator, post scorer, carousel builder) outperforms a long
  identity doc. Map every skill to exactly one owning agent so two
  agents never fight over the same job.
- **Adapt, don't vendor.** When borrowing open-source material, write
  runbooks and patterns — don't paste whole repos. The repo stays small,
  brand-agnostic, and legally clean; the upstream project stays the
  source of truth for code.
- **Verify the LICENSE file, not the badge.** A README can claim MIT
  while the license file carves out commercial restrictions (we caught
  exactly this: a clipping engine whose agent-control components were
  commercial-licensed with white-labeling forbidden). Read the file.
  When in doubt, exclude and document why.
- **Separate creation from publishing, always.** The studio produces;
  Hype publishes; the scheduler only schedules approved content; the
  comment monitor only drafts replies. Every gate is a separate step
  with a separate owner. Nothing auto-publishes, nothing auto-replies.
- **Caption everything.** Burned-in captions are non-negotiable on
  short-form — most viewers never unmute. Offline transcription keeps
  footage on our machines and costs nothing per video.
- **Deterministic creative wins client trust.** JSON request + brand
  pack → render, with a QA checklist and a provenance file on every
  asset. "The AI made it" is not a QA process.
- **Automate the detector, never the actor.** Comment watches, RSS
  monitors, and analytics digests run 24/7 and queue work for
  humans/agents. The moment automation takes the public-facing action
  itself, you've lost control of the brand voice.
- **Back up the encryption key, not just the data.** For n8n: losing
  `N8N_ENCRYPTION_KEY` orphans every stored credential with no recovery.
  Key + volumes + workflows-as-code, or the backup is theater.
- **Paperclip is the control plane the agency was missing.** 8 agents + skills + studio + cloud automation is a fleet with no management layer. Paperclip's model (org chart, heartbeat wakes, per-agent budgets, atomic task checkout, governance gates, audit trail) maps 1:1 onto what the agency needs — and its multi-company tenancy IS the white-label model (one company per brand). Adopt the concepts now; deploy the app when a VPS is ready.
- **Heartbeats beat loops.** Agents shouldn't run continuously — short wake-windows (schedule, assignment, @-mention, manual, approval) with a fixed protocol (check identity → review assignments → checkout task → work → update status) are cheaper, more auditable, and easier to reason about than always-on daemons.
- **Budgets are a governance feature, not finance.** Per-agent monthly caps that hard-stop the agent turn "don't run up the API bill" from a hope into a mechanism. Set caps before the first heartbeat, per brand.
- **Atomic checkout prevents double-work.** One agent owns a task at a time or nobody does. Our no-duplicate-posts/no-double-reel rules are the content-side version — make the invariant structural wherever the runtime allows it.
- **Keep a sources registry.** Every external repo evaluated (integrated OR rejected, with license verdict and date) goes in `agency/docs/SOURCES.md`. Future scans check it first — never pay the evaluation cost twice, and never accidentally re-admit a rejected license.
- **Memory is a system, not a diary.** Hindsight's model (banks, retain/recall/reflect, evidence-backed observations with proof counts) is how the learning loop graduates: one bank per brand, observations refined by new evidence instead of overwritten, quarterly reflection promoting repeats into mental models. A lesson without evidence is a hypothesis — label it so.
- **Chat is for decisions, documents are for records.** Anything a human re-reads, compares week-over-week, or shares with a client belongs in a real document that agents write (Univer's "office harness" insight). The weekly analytics digest should be a workbook, not a chat message.
- **Make the review structural.** FOR-CLAUDE-CODE.md invites review; the Claude Code GitHub Action makes it automatic — every PR reviewed against the white-label contract, attribution headers, and license rules. Standing work should never wait on a human.
- **Agents get keys, not the kingdom.** Buzz's identity-scoped agents (own keys, own memberships, own audit trail) are the infrastructure version of our standing rule. When an agent needs phone-level access (mobile-mcp pattern), approval gates apply doubly — never standing authorization on auth, payments, or deletions.
## Growth & monetization (from marketingskills + ai-marketing-skills, 2026-09-26)

- **The offer is the thing, not the page.** Better copy on a weak offer compounds slowly; a stronger offer with average copy converts immediately. When someone asks for "better copy," diagnose the offer first — score the Value Equation (dream outcome × perceived likelihood ÷ time delay × effort), fix the lowest lever one iteration at a time. (agency/growth/OFFER-DESIGN.md)
- **A loop isn't closed until the change is judged.** Platform truth wins over opinions: every test, content change, or strategy shift gets a readback (baseline vs. candidate, primary metric defined up front, caveats named) before its lesson enters the playbook. Only the author liking it is not evidence. (agency/growth/ANALYTICS-LOOP.md)
- **Two-tier action model for every scheduled loop:** Tier 1 (read, analyze, draft, stage) runs unattended; Tier 2 (spend, send, publish, delete, change live settings) is gated behind human approval unless explicitly authorized with caps + allowlist. Every loop has a kill switch and logs no raw PII. (agency/growth/LOOP-SPEC.md)
- **Nothing publishable ships without the quality gate:** a 7–10 expert panel scores recursively to 90/100 (AI-slop detector weighted 1.5x, brand-voice match non-negotiable, max 3 rounds). Rejections become permanent rules in the brand's learnings — that is how quality compounds. (agency/skills-library/marketing/quality-gate.md)
- **Attribute revenue to content before buying more of it:** run first-touch, linear, and time-decay attribution together — where they disagree is where each content type actually works. CPA by content type decides future budget; the top 10% of pieces get repurposed. (agency/skills-library/marketing/revenue-attribution.md)
- **On YouTube, steal what's proven, then package it better:** anything at 2x+ channel-average views is an outlier — extract its title/thumbnail/hook pattern. Never call packaging validated until the readback window checks out (24–48h CTR, 7-day watch time, 28-day subscriber gain). (agency/skills-library/marketing/youtube-outliers.md)
- **Brand-first convention:** every marketing skill reads the brand's context files (brand-voice, audience, offers, learnings) before asking the owner a single question. Shared skills, per-brand context — that is what makes white-label possible. (agency/skills-library/marketing/brand-first.md)
- **Don't peek at experiments early:** pre-commit to sample size; checking results early manufactures false positives. Test one variable at a time, judge on the primary metric, and promote winners to the playbook as reusable patterns with segment deltas. (agency/growth/EXPERIMENT-RUNBOOK.md)
- **Never discount to acquire:** discount-askers churn ~2x the rate of full-price customers and a coupon anchors the product as cheap. Raise value with the offer instead — bonuses that are additive (not inflated), guarantees matched to the business model, scarcity that's real. (agency/growth/OFFER-DESIGN.md)
- **Clarity beats cleverness in copy:** specific > vague, benefits > features, customer language > company language. One idea per section. Banned pattern-matches: "game-changing", "10x", "secret", "limited time" with no real limit, invented "$X value" claims. (agency/growth/COPY-PATTERNS.md)
<!-- lanes-learnings fragment — bullets for agency/shared/learnings.md, lane scan 2026-09-26. Append under a new "## Repo shopping" section or the closest fit. -->

## Repo shopping (2026-09-26 lane scan)

- **Medusa v2 is the agency's merch backend default** (MIT core).
  One deployment per brand — no native multi-tenancy. Pair with a
  Next.js storefront skinned from the brand pack, or the brand's
  existing site via API.
- **POD wiring pattern:** event-driven order submit (`order.placed`
  → provider API), idempotent webhooks back into fulfillments, live
  shipping rates with flat-rate fallback, one fulfillment per parcel.
  Printful via `print2medusa`, Printify via `medusa-plugin-printify`
  (both MIT). No ads until a full test order per hero SKU passes.
- **Velo rule:** backend-only APIs, secrets, and npm packages live
  behind `*.web.js` web modules with explicit `Permissions`; page
  code passes parameters and receives URLs. Author Velo in git and
  sync via the Wix CLI — the in-browser editor is not the source
  of truth.
- **Wix design system:** tokens first (Site Styles from the brand
  pack), saved section presets, custom CSS only as the escape hatch.
- **JSON-first site documents are the web trend to bet on:**
  `{ name, theme, blocks[] }` that humans, editors, and agents all
  read and write (OpenPage, MIT). Generate the JSON, never the code —
  review becomes diffing, which agents do reliably.
- **License discipline, again:** Vendure's third-party writeups say
  MIT; its actual LICENSE.md is GPLv3-first. Read the file, never
  the badge. Saleor is BSD-3 (permissive) but outside the strict
  MIT/Apache-2.0 allow-list — rejected on the rule, flagged for
  re-evaluation if policy widens.
- **A merch store earns a bigger catalog only after hero SKUs prove
  conversion.** Breadth before proof is inventory thinking in a
  no-inventory business.

## 2026-09-27 — License policy widened (Brenden's call)
- **Rule is now: permissive licenses only** (MIT, Apache-2.0, BSD,
  ISC) — not just MIT/Apache-2.0. Still permanently out: GPL/AGPL,
  unlicensed, ambiguous, commercial carve-outs.
- **Saleor (BSD-3) integrated** on the widened rule: headless
  GraphQL commerce, and its multichannel model (per-channel pricing /
  currency / stock) is white-label native — one channel per brand.
- Lesson: write rejections as reversible. The Saleor NOT-INTEGRATED
  file said "re-evaluate first if policy widens" — because it did,
  integration took minutes instead of a re-scan.

## 2026-09-27 — Seven-repo integration (hunt → vet → test → integrate)
Each lane was drafted in a disposable copy, tested on a scratch brand
(`zz-scratch-test`, "Scratch Pizza Co", never committed), fixed until a
markdown-reading agent could run it, then integrated. Sources #20–26.
- **Licenses: read the file, again.** Two Anthropic Apache-2.0 repos carry no
  copyright line or NOTICE; WeKnora is MIT only for Tencent's own code and
  bundles "nolicense"/"unknown" components — borrow the owner's patterns,
  never the bundle.
- **"Completed" is not "accepted"; a worker's "pass" is a claim.** Grade every
  criterion holds / does not hold / UNVERIFIED against the artifact; the
  controller's fan-in caught wrong hours a worker had marked passing
  (deer-flow, orca).
- **Unattended runs never guess owned facts.** Stage drafts and return a
  BLOCKED report naming the missing decision; an empty approver means blocked
  (deer-flow).
- **Parallelize only on disjoint write sets and zero live writes;** one writer
  per surface, claims via create-if-absent, silence is not failure (orca).
- **Unknown is not zero.** Missing cost, revenue, volume or benchmark stays
  `unknown (reason)`; an invented threshold slipped into a draft and was caught
  only against the experiment runbook (commerce-agents, knowledge-work-plugins).
- **A margin floor beats a discount cap:** max safe depth =
  1 − (unit_cost / (1 − floor)) / price — check both (commerce-agents).
- **Check every offer link first;** a 404 on a live offer page was the most
  expensive defect in the test (knowledge-work-plugins).
- **No citation, no claim;** a newer secondary source can still be stale, and
  retrieval scores are ordering, not confidence (WeKnora).
- **Models fill specs; renderers draw** — and schemas can't see invented prose:
  only the human read caught made-up backstory in a newsletter (openui).
- **Capture needs a trigger and curation needs a janitor;** keep a
  do-not-capture list; a lesson becomes a skill only as a proven, repeated
  procedure with human approval (hermes-agent).

