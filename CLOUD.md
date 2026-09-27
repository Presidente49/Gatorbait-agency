# CLOUD — what runs 24/7 and how to deploy it

The agency's brain (agents + playbooks) lives in this repo and runs inside
an AI assistant. The CLOUD layer is everything that runs on its own,
around the clock, on a VPS: automation, scheduling, and the client
dashboard.

## What's in agency/cloud/

```
agency/cloud/
├── n8n/
│   ├── docker-compose.yml   # n8n + PostgreSQL + Caddy (auto-HTTPS), 24/7
│   ├── .env.example         # every variable the operator must set
│   ├── README.md            # deploy, backup, restore, per-client wiring
│   └── workflows/           # 3 starter workflows (authored from scratch)
│       ├── rss-to-social-drafts.json   # RSS → draft queue (Scout→Scribe)
│       ├── comment-monitor.json        # comment watch → draft-reply queue
│       └── weekly-analytics-digest.json# Monday metrics digest
└── scheduler/
    ├── README.md            # the white-label client dashboard option
    ├── DEPLOY.md            # VPS (Node) or Vercel+Postgres paths
    └── WHITE-LABEL-NOTES.md # per-client rebrand checklist
```

## The 24/7 stack

| Service | Role | Notes |
|---|---|---|
| n8n | Automation engine | Workflows: draft pipelines, comment watch, digests, publishing |
| PostgreSQL | n8n's database | Named volume; healthcheck gates n8n startup |
| Caddy | Reverse proxy | Automatic HTTPS; n8n port bound to loopback only |
| Scheduler app | Client dashboard | Self-hosted social scheduler; one instance per client |

## Deploy (n8n)

```bash
cd agency/cloud/n8n
cp .env.example .env
# Edit .env: set N8N_HOST, N8N_VERSION, N8N_ENCRYPTION_KEY (generate once,
# back it up), GENERIC_TIMEZONE, Postgres password. Create the n8n owner
# account (long password + 2FA) on first open.
docker compose up -d
```

**Back up two things:** the `N8N_ENCRYPTION_KEY` (lose it and every stored
credential is orphaned) and the named volumes. Workflows live as JSON in
`workflows/` — commit finished ones back to the repo as code.

## Security rules

- The comment-monitor workflow is **detector-only**. It queues draft
  replies for a human/agent to approve. Nothing auto-replies, ever.
- The scheduler **never creates content**. It schedules what Hype
  approved. Creation and publishing are separate gates.
- No credentials in the repo. `.env` is gitignored (root `.gitignore`); only
  `.env.example` (placeholders) is committed. Tokens live in n8n Credentials,
  never in workflow node parameters.
- n8n's editor UI sits behind the owner login + HTTPS. Webhook URLs are
  unguessable tokens.

## Scaling later

Single VPS handles the starter load. When executions queue up: add Redis
and run n8n in queue mode (`EXECUTIONS_MODE=queue`) with worker
containers. The compose file is structured to grow that way.
