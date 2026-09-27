# n8n Automation Layer

The agency's always-on automation backbone. n8n runs 24/7 on a VPS,
talking to the client's platforms through credentials the operator
connects per client. This layer handles the repetitive machinery —
polling, queueing, compiling reports — so the agents spend their time
on judgment, not fetching.

## What runs here

| Service | Role |
|---------|------|
| `postgres` | n8n's database (workflows, executions, encrypted credentials) |
| `n8n` | The automation engine — workflow editor + runners |
| `caddy` | Reverse proxy with automatic HTTPS (Let's Encrypt) |

Named persistent volumes: `n8n-data` (n8n's home dir), `n8n-postgres-data`
(the database), plus Caddy's `n8n-caddy-data`/`n8n-caddy-config`. All
services `restart: unless-stopped`.

## Deploy

On any VPS with Docker installed:

```bash
cp .env.example .env
# Edit .env — fill in REAL values. Every placeholder must be replaced.
docker compose up -d
```

Then open `https://<N8N_HOST>` and create the n8n owner account.
Import the starter workflows from `workflows/` (Workflows → ⋯ →
Import from file) and connect each node's credentials per the
`"notes"` on the node.

### Requirements on the VPS

- Docker + Docker Compose plugin.
- Ports 80/443 open (Caddy needs them for HTTPS certificates).
- DNS A record: `<N8N_HOST>` → the VPS IP.
- ~1 GB RAM minimum, 2 GB comfortable.

## Starter workflows (`workflows/`)

These are **starter scaffolds, not production-ready**. Every stub node
says what the operator must connect. They were authored for this
agency — not copied from any n8n template collection.

| Workflow | What it does | Agency role |
|----------|--------------|-------------|
| `rss-to-social-drafts.json` | RSS poll (2h) → dedupe → keyword filter → AI summarizer stub → draft queue (Sheet/Notion stub) → notify | Feeds the Scout → Scribe handoff: raw stories become queued drafts |
| `comment-monitor.json` | Every 15 min → fetch recent post comments (Meta Graph API stub) → dedupe handled → reply-draft queue → notify | **Detector only.** Never auto-replies — a human/agent drafts each reply |
| `weekly-analytics-digest.json` | Monday 8am → FB/IG/site metrics stubs → compile markdown digest → send to operator | Data source for Scout's weekly performance report |

### Wiring a workflow for a client

1. Import the JSON.
2. Open each stub node, read its `"notes"`.
3. Add real credentials (n8n Credentials panel — OAuth2/API key/basic
   auth), replace placeholder IDs/URLs (PAGE_ID, Sheet ID, chat IDs).
4. Run a manual execution, fix the errors, then activate the workflow.
5. One consideration per client: some nodes (comment monitor, metrics)
   are per-brand — duplicate and re-point the workflow per client
   rather than mixing brands in one workflow.

## Backups

**This is the part that bites if you skip it.**

1. **N8N_ENCRYPTION_KEY** — in `.env` on the server AND in a password
   manager. Without it, every credential stored in n8n is unrecoverable.
   Rotate deliberately: changing it orphans all credentials.
2. **Volumes** — back up `n8n-data` and `n8n-postgres-data` regularly:
   ```bash
   docker run --rm -v n8n-data:/data -v $(pwd):/backup alpine \
     tar czf /backup/n8n-data-$(date +%F).tar.gz /data
   docker exec n8n-postgres pg_dump -U n8n n8n > n8n-db-$(date +%F).sql
   ```
3. **Workflows as code** — keep the exported/edited workflow JSONs in
   this `workflows/` directory (in the agency repo) so a rebuild is
   `docker compose up` + import.

## Restore

1. New VPS, same `.env` (same `N8N_ENCRYPTION_KEY` — non-negotiable).
2. `docker compose up -d`.
3. Restore volumes / re-import `workflows/`.
4. Re-verify each workflow's credentials still validate.

## Security notes

- `.env` never enters the repo (`.gitignore` it). Real secrets live on
  the server + password manager only.
- Basic auth guards the editor; Caddy forces HTTPS.
- Keep n8n updated: `docker compose pull && docker compose up -d`.
- The `comment-monitor` workflow is deliberately detector-only —
  auto-replying from n8n bypasses the agency's comment rules; don't add
  a create-comment node without CEO sign-off.
