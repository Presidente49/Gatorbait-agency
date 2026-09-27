# REVIEW — Gator Bait Agency repo

Reviewed 2026-09-27 on branch `claude/chat-analysis-continuation-hucefx`,
against base commit `4b00574`. Line references in "What's broken" are to
that base commit unless marked. The fixes below are local commits. Nothing
was pushed, deployed, run in Docker, or sent to an external write API.

The review also checks this repo against the live GatorBait operation's rules
(production repo `Presidente49/gatorbait-media-redesign`). Where the two
conflict, this review does not change the owner's intent. Each conflict is
listed under **Needs a human decision**.

## How it was checked

- `python -m json.tool` on every JSON file: all 3 workflows valid before and after.
- `docker-compose.yml` parsed with PyYAML: valid before and after. The folded
  Caddy `command:` renders to the intended Caddyfile. `docker compose config`
  was not run because Docker was out of bounds for this review.
- The n8n Code node JavaScript was extracted and syntax-checked with `node --check`.
- Workflow connections were checked: every source and target node exists, and node IDs are unique.
- Secret scan: grep for API-key, token, private-key, JWT/Stripe/Meta/Telegram
  token shapes, emails, IPs and `password=` assignments. **No real secret,
  email or IP is in the repo.** Only placeholders were found (`CHANGE_ME_…`,
  `YOUR_…`, `n8n.example.com`, `127.0.0.1`).
- `.env.example` holds placeholders only. One exception: `N8N_BASIC_AUTH_USER=admin`
  was a guessable default, and that variable has been removed (see below).
- Relative markdown links and backtick paths: none are broken. Only
  `{codename}` template paths don't resolve, which is intended.
- Upstream licenses: all 7 `LICENSE` files were fetched read-only from
  raw.githubusercontent.com and read. All 7 are standard MIT, and the bodies
  are identical apart from the copyright line. The openshorts exclusion
  reasoning is sound.
- `new-brand.sh` was run against scratch slugs (`zz-test-pizza`,
  `zz-joes-pizza "Joe's Pizza & Subs / Tampa"`, `../evil`, `_template`).
  Every result was deleted and `ACTIVE` was restored to `gator-bait-media`.

## What's solid

- **Layout.** The split between brand-agnostic `agents/`, `shared/`,
  `skills-library/` and `studio/` and per-brand `brands/<slug>/` is right.
  So is the one-line `ACTIVE` switch.
- **Separation of creation and publishing is stated clearly.** See
  `shared/learnings.md` ("Automate the detector, never the actor"),
  `STUDIO.md` ("The studio never publishes"), and the comment monitor, which
  only detects and never replies.
- **Skills library.** The 17 skills are unusually disciplined about evidence.
  They say "never invent metrics", mark missing data as pending rather than
  zero, never scrape comments, and confirm cost before paid runs. Every skill
  maps to exactly one owning agent.
- **Creative QA and provenance.** The `studio/creative/` gate (a
  `"passed": true` result, a provenance sidecar, and a recorded proof source)
  is a good fit for a newsroom that must verify facts.
- **License diligence.** `studio/clipping/NOT-INTEGRATED.md` is a model
  exclusion record. No upstream code is vendored; only docs and patterns are adapted.
- **Compose basics were already right.** Postgres healthcheck gates n8n,
  n8n is bound to loopback only, Caddy handles HTTPS, volumes are named, and
  required secrets fail fast with `:?`.
- **Secrets hygiene is good in intent.** Livestream keys live in 0600 files,
  configs hold `${NAME}` templates, and every doc says "placeholders only".
- **The Gator Bait Media brand folder is rich and specific.** It holds real
  revenue numbers, real A/B learnings and correct spellings (`Jon Sumrall` in `studio/reels/API-PATTERN.md`).

## What's broken, with file:line

### Cloud / n8n (all fixed)
| Where | Problem |
|---|---|
| `agency/cloud/n8n/workflows/weekly-analytics-digest.json:1` (Code node) | **JS syntax error.** `'…the client's KPI summary…'` has an apostrophe inside a single-quoted string, so the node could never run. |
| `weekly-analytics-digest.json:1` (connections) | Three parallel branches feed one Code node, so n8n runs it once per branch: **3 digests and 3 Telegram sends a week**. `$('Metrics: …').first()` also fails for branches that haven't run yet. |
| `weekly-analytics-digest.json:1` (FB/IG nodes) | `/insights` was called with `fields=` instead of `metric=`/`period=`, so the Graph API rejects it. |
| `comment-monitor.json:1` (fetch node) | URL `/{PAGE_ID}/conversations` is the **Messenger inbox**, not post comments. The response's `data` array was never split, so dedupe ran on `undefined`. The notify node read `$json.from.name`, which doesn't exist after the Sheets append. |
| `rss-to-social-drafts.json:1` (Keyword filter) | The regex was in an invented `operator.regex` field with an empty `rightValue`. It also used `(?i)`, which JavaScript regex doesn't support. |
| `rss-to-social-drafts.json:1` (AI summarizer) | Headlines were interpolated raw into a JSON body, so any `"` in a title breaks the request. |
| all 3 workflows (Remove Duplicates nodes) | `mode`/`dedupeScope` aren't v2 parameters. The node fell back to within-run dedupe only, so **every RSS item would be re-queued every 2 hours**. |
| all 3 workflows (HTTP Request nodes) | `queryParameters` sat under `options`, which v4 ignores. The access token was designed to be pasted into a URL parameter of a workflow the README says to commit back to the repo. |
| `docker-compose.yml:56-58` | `N8N_BASIC_AUTH_*` has been ignored since n8n 1.0, yet `:?` made the stack refuse to start without it. That gave a false sense of editor protection (also claimed in `CLOUD.md:57` and `n8n/README.md:94`). |
| `docker-compose.yml:33,45` | Unpinned `n8nio/n8n:latest`. `WEBHOOK_URL` defaulted to `n8n.example.com` instead of following `N8N_HOST`. `N8N_HOST`, `N8N_PROTOCOL` and `N8N_PROXY_HOPS` were missing behind Caddy. |
| `CLOUD.md:55` | Says `.env` is "gitignored by convention", but **no `.gitignore` existed**. |

### White-label / onboarding (fixed)
| Where | Problem |
|---|---|
| `new-brand.sh:15` | No slug validation: `./new-brand.sh ../../evil` wrote a brand **outside the repo** and pointed `ACTIVE` at it. `_template` was also accepted. |
| `new-brand.sh:15` | Relative paths meant it only worked from the repo root. |
| `new-brand.sh:15`, `WHITE-LABEL.md:46` | Copied `_template/README.md` into the brand. Agents "read every .md in the brand folder", so the template guidance became brand facts. |
| `_template/` | Nowhere to record approvals (who signs off on posts, site changes, email or spend). Nowhere to record the site platform, location or hours (a pizza shop's most important facts), fact sources, photo credit or logo rules. `about.md` was read by `voice-builder` and `video-thumbnail` but didn't exist. |
| `agents/*/identity.md`, `shared/playbook.md:25` | Gator-only rules were hardwired into "brand-agnostic" files. Examples: Anton headlines (`blueprint:14`), The Buddy Martin Show (`bridge:14`), "Gator groups only" (`hype:17`), "Gator Bait voice" and box scores (`scribe:14-16`), Wix and "Brenden applies edits" (`rank`, `webmaster:25`). A pizza shop onboarded through the script would inherit them. |
| `WHITE-LABEL.md:94`, `shared/protocols.md:14`, skills | The "brand's log", "designated location" and "brand workspace outputs folder" (`post-scorer.md:33`, `post-writer.md:44`, `reels-scripting.md:36`) were undefined. |
| `agents/*/tasks.md`, `memory/*.md` | All 24 files were 0 bytes, with no format for agents to follow. |

### Learnings loop (fixed in docs; partly open)
- Nothing wrote to `learnings.md`. None of the protocols, skills or workflows
  had a step that appends a learning. That step now exists (see fixes). The
  n8n digest and the studio runbooks still don't close the loop on their own.
  Scout does that after reading the digest.

### Attribution / licenses (fixed)
- The 32 attribution headers had the repo, URL and license, but **no copyright
  holder**. No MIT permission text was anywhere in the repo, and MIT requires both.
- `agency/cloud/scheduler/DEPLOY.md:1` and `WHITE-LABEL-NOTES.md:1` had no attribution header.
- `avioflagos/marketing-agency-skill` (the base the agency was adapted from)
  was credited only in `README.md`.
- The repo has **no LICENSE of its own**. See Needs a human decision.

### Studio (flagged, not fixable here)
- **None of the studio tools are installed or deployed:** capite, reel-quick,
  multistream, or the visual-factory render harness.
  `studio/reels/README.md:71-73` says so. Every runbook is a plan, not a runnable pipeline.
- `studio/captions/PIPELINE.md:20-31,73-76` is **GUI-only** ("drag into the
  dropzone", "Click Generate Captions"). A markdown-reading agent can't do
  these steps unless someone documents the backend API.
- The clipping stage is an acknowledged gap (`STUDIO.md`), so the
  clip → caption → reel chain has no automated first step.
- `studio/reels/THEMES.md`: there's no defined path for theme JSON files.
  The transitions `slam-cut`, `whip` and `dip-black` must be registered
  upstream (`POST /available-transitions`) before any job can name them.
- `studio/creative/README.md:77-79`: the render harness "lives outside these
  runbooks", but no location is named. `brand.json` and `tokens.css` have no defined path either.
- `studio/creative/BRAND-PACK.md:22` said "Logo (typed)". It meant
  role-typed, but it reads as "type the logo". Reworded (fixed).
- `cloud/scheduler/DEPLOY.md:7-9` said "VPS with Docker", but the steps are npm/pm2 (fixed).

### Stale / minor (not changed)
- `shared/campaign-board.md`: the Ole Miss blitz tasks (H-001..H-003
  "QUEUED" posts) are dated Sep 26. Confirm what actually posted before any agent acts on this board.
- `gator-bait-media/goals.md:1` is titled "Agency Goals", not "Goals — Gator Bait Media".
- n8n node parameter names were corrected from n8n's documented v1 node
  schemas. **Import each workflow into a disposable n8n and run it manually
  before trusting the fixes.** JSON validity isn't the same as "works in n8n".

## What I fixed (commits)

| Commit | What |
|---|---|
| `083bfcc` | **Onboarding.** `new-brand.sh` now validates the slug (blocks traversal and `_template`), works from any cwd, skips the template README, creates `outputs/`, accepts an optional display name (tested with `&` and `/`), and reports the previous `ACTIVE`. New `_template/about.md` holds facts, platforms, the approval matrix, fact sources, photo credit and logo rules. New `gator-bait-media/about.md` records the live production rules and newsroom. Adds a root `.gitignore`. Seeds agent `tasks.md` and memory files. |
| `c8177ae` | **n8n.** All the workflow bugs above: syntax error, triple-send, wrong Graph endpoints and params, split-out, cross-run dedupe, regex, JSON escaping, and tokens moved into n8n Credentials (Query/Header Auth) instead of parameters. Workflows are explicitly `active: false`. Compose: dead basic-auth removed, `WEBHOOK_URL` derived from `N8N_HOST`, proxy settings added, `N8N_VERSION` pin. Docs updated to match. |
| `80b7ad0` | **Attribution.** `THIRD-PARTY-NOTICES.md` has all 7 upstreams, verbatim copyright lines and the MIT text. The copyright holder was added to the 32 headers, and the missing scheduler headers were added. |
| `2cd6acb` | **White-label and loop.** Gator-specific rules moved out of the agents, playbook and protocols into brand-file pointers (Gator rules kept in `gator-bait-media/about.md`, and no approval gate was loosened). `outputs/` and `outputs/log.md` are defined as the brand workspace. The learnings step was added to protocols, `analytics-dashboard` and `post-scorer`. Creative QA gained a photo-credit field, a no-repeat-cover-photo check and a supplied-logo-only check. Scheduler deploy heading fixed. |
| (this commit) | `REVIEW.md` |

## Needs a human decision

Each of these is a conflict between this repo and the live GatorBait
production rules. Nothing below was changed. The recommendation is mine; the
decision is Brenden's.

1. **"Marlowe", a CMO agent that "runs the stack", would be a second
   controller.** Sources: `FOR-CLAUDE-CODE.md:4,34`; `README.md:21-23` ("The AI
   running the agency is the CMO"); `shared/protocols.md:21,33-34`.
   Production has exactly one controller, Claude Code Master Control, and it
   forbids competing controllers.
   **Recommendation:** make "CMO" a *role that Master Control plays* when it
   runs this repo, not a separate agent. Remove "Marlowe" from the
   directive, or define Marlowe as a draft-only persona with no production
   authority.
2. **24/7 n8n cloud layer versus "don't reactivate n8n merely because
   scaffolding exists".** Sources: `CLOUD.md`, `README.md:30`, `agency/cloud/n8n/`.
   The owner now runs recurring work as Claude Code cloud routines.
   **Recommendation:** keep `agency/cloud/` as a dormant, white-label option
   for *other clients*. Mark it "not used for Gator Bait Media". For GBM,
   re-express the weekly digest and RSS watch as read-only Claude Code routines
   that record findings, and only if there is a defined job for them.
3. **The auto-publishing chain bypasses the publish, email and account gates.**
   Sources: `shared/protocols.md:4-5,21,23` ("Default is GO", "Each handoff
   fires automatically. No CMO approval needed", "auto-approve if all pass",
   with escalation only for "first-time public content"); `README.md:70-71`;
   `cloud/scheduler/DEPLOY.md:83` (the scheduler auto-publishes);
   `gator-bait-media/goals.md:13` and `playbook.md:19` (reply to every comment
   within the hour, which implies unattended posting).
   **Recommendation:** keep "Default is GO" for drafting, research and QC only.
   Change the waterfall so Hype *stages* every public post, and publishing
   needs an approval step per `about.md` for every brand. Adopt the production rule:
   publishing, email sends, money and account changes are always gated.
4. **Webmaster "full coding ability, no ceiling" plus "API-safe fixes can be
   automated" could make a second Wix writer.** Sources:
   `agents/webmaster/identity.md:14,25`; `shared/learnings.md:69-70`;
   `shared/roster.md:19` ("Backend Loop (always on)");
   `gator-bait-media/learnings.md:44-45` (browser work on Brenden's Google
   session). Production allows exactly one writer to the Wix site, through the
   Wix API. **Recommendation:** for GBM, Webmaster and Rank are read-only
   auditors that stage fixes into an existing issue for Master Control.
   Remove "always on", and drop the browser-session route.
5. **Wrench is "autonomous" over email lists.** Source:
   `agents/wrench/identity.md:21` ("don't ask about routine cleaning"). It
   touches the send infrastructure, where production allows one email per
   story, has the alert automations off, and gates sends.
   **Recommendation:** make list cleaning report-only for GBM (counts plus a
   proposed suppression list), and have the owner apply changes.
6. **Muse as a host that "runs the agency".** Source: `README.md:4` ("runs
   inside any AI assistant (Muse, Claude, etc.)"). Production says Muse
   drafts only. **Recommendation:** name Muse as a drafting tool only, never the
   operator.
7. **Too many agent layers for a small newsroom.** There are 8 agents,
   17 skills, a studio and a cloud layer, while production says to avoid
   agent swarms and redundant specialist layers. Hype and Scribe overlap the
   real newsroom (Buddy Martin as editorial lead; writers Franz Beard,
   Carlton Reese, Eddie Gilley and Loren Meadows).
   **Recommendation:** for GBM, run the skills as tools under Master Control
   rather than instantiating 8 standing agents. Keep the agent roster for
   white-label clients who have no newsroom.
8. **Repo license.** The repo has none, but it is meant to be white-labeled
   to clients. **Recommendation:** choose one (proprietary "all rights
   reserved" plus client terms, or MIT). Until then, don't hand the repo to a client.
9. **Personal data in a brand file.** `gator-bait-media/learnings.md:41-45`
   names third parties (Chris Spears, Scott Burns) and roles. Also, "one
   post per asset" and "one game photo = one post" should be reconciled with
   the new "no repeated photos across covers" rule. **Recommendation:** keep
   the names (credit is required), drop the access and credential-routing
   details, and confirm the photo rules with Brenden.

## Suggested next steps

1. Decide items 1 to 3 above. They determine whether `cloud/` and the
   auto-waterfall stay in the GBM path at all.
2. Import the three workflows into a throwaway n8n (not production) and run
   each manually with placeholder credentials. Fix any node-parameter drift. Pin `N8N_VERSION`.
3. Walk one real non-sports brand end to end: `./new-brand.sh`, fill
   `about.md` first, then run `voice-builder`, `content-matrix` and `post-writer`.
   Note every place an agent still assumes sports.
4. For each studio tool, either deploy it and document its API endpoints in
   place of GUI clicks, or mark the runbook "not deployed", so agents don't
   report steps they can't perform.
5. Define the paths for brand packs and themes (suggested:
   `agency/brands/<slug>/pack/` and `…/pack/themes/`).
6. Add a small CI check: `json.tool` on `workflows/*.json`, a YAML parse of
   the compose file, a secret-pattern grep, and a test that `new-brand.sh`
   rejects `../x`.
7. Refresh `shared/campaign-board.md` from live state before any agent reads it.
