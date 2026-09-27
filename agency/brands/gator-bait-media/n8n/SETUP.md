# GatorBait on n8n Cloud: setup

These are three GatorBait-specific workflows, built from the white-label
starters in `agency/cloud/n8n/workflows/`. They run on **n8n Cloud**, so there
is no server, Docker or Caddy to maintain.

| File | Runs | What it does | Output |
|---|---|---|---|
| `article-to-social-drafts.json` | Every 2 hours | New gatorbaitmedia.com articles → Claude drafts 3 hooks, a caption and hashtags | Row in **GatorBait n8n — Social drafts queue** plus one email |
| `comment-monitor.json` | Every 30 min | New comments on the Facebook Page | Row in **GatorBait n8n — Comment reply queue** plus one email |
| `weekly-numbers-digest.json` | Mon 8 a.m. ET | Wix sessions and visitors, plus Facebook and Instagram followers, reach and engagement | One email |

**None of them post, reply, publish or email subscribers.** They draft,
detect and report, and every email goes only to the owner. A post leaves a
sheet only when a person approves it and posts it from the Page. Adding a
posting or replying node needs Brenden's sign-off; see the production rules
in `../about.md`.

Both queue sheets already exist in Brenden's Google Drive, private to him.
Their IDs are set in the workflows; a sheet ID gives no access without his Google login.

## 1. Sign up (Brenden, about 3 minutes)

1. Go to n8n.io and start **n8n Cloud**. These schedules come to about 1,800
   executions a month (1,440 comment checks, 360 feed checks, 4 digests).
   Pick the cheapest plan whose monthly execution cap covers that; check
   n8n's pricing page, since plan limits change.
2. Set the instance time zone to **America/New_York** (Settings → General).

## 2. Create four credentials (Brenden only; never paste keys into chat or the repo)

In n8n: **Credentials → Add credential**. Use these exact names so the workflows find them.

| Name | Type | What goes in it |
|---|---|---|
| `GatorBait Meta Page token` | **Query Auth** | Name `access_token`; Value = a **Page** access token for the GatorBait Media Page, with `pages_read_engagement`, `read_insights` and `instagram_manage_insights`. Get it in Meta's Graph API Explorer: pick the Page under "User or Page", then extend it to a long-lived token. |
| `Anthropic API key` | **Header Auth** | Name `x-api-key`; Value = an API key from console.anthropic.com. |
| `Wix API key (read-only analytics)` | **Header Auth** | Name `Authorization`; Value = a Wix API key (Wix → Settings → API Keys) with **only** the Site Analytics read permission. |
| `Google (GatorBait)` and `Gmail (GatorBait)` | Google Sheets OAuth2 / Gmail OAuth2 | Click **Sign in with Google** and use brenden@ (the account that owns the two sheets). |

## 3. Import and connect (about 5 minutes)

For each JSON file: **Workflows → Import from file**. Then:

1. Open each node that shows a red credential warning and pick the matching credential above.
2. In each **Email Brenden** node, set **To** to your own address (it's `SET_OWNER_EMAIL_IN_N8N` in the file so no address sits in this public repo).
3. Leave the workflow **inactive**.

## 4. First run, before switching on

Click **Execute workflow** once for each workflow, and check:

- **Weekly digest:** an email arrives. If Facebook shows "unavailable" with a
  `valid insights metric` error, Meta has retired a metric name. Swap it in the
  "Facebook insights" node (the Graph API changelog lists replacements). The rest of the report still arrives.
- **Comment monitor:** with no comments in the last 30 minutes it stops
  quietly, which is correct. (It looks back 45 minutes each run, with dedupe.) Comment on a Page post from a personal account, run it again, and a row plus an email should appear.
- **Social drafts:** only articles published in the last 6 hours are
  drafted. If nothing is that new, it stops quietly. After the first real run,
  check the sheet row: the hooks must match facts in the headline and excerpt only.

Then flip each workflow to **Active**.

## Costs

- n8n Cloud Starter, billed by n8n.
- Claude: one short call per new article (about 5 to 15 a day), cents per day.
- Meta, Wix and Google APIs: free at this volume.

## Changing them

Edit `build.py`, run `python3 build.py`, re-import, and re-select
credentials. Record every change's lesson in `../learnings.md`.
