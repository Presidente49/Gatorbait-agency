<!-- Source: arifyaman/multistream (https://github.com/arifyaman/multistream) — MIT. Adapted for Gator Bait Agency. -->
# VPS Setup — 24/7-ready livestream relay

Run the relay and supervisor on a small VPS so the chain is always up,
even when the studio machine is off. Generic pattern — works on any
provider, no provider-specific secrets anywhere.

## Why a VPS

- Home/studio upload stays at 1× no matter how many platforms you add.
- Relay close to platform ingest servers → lower latency.
- 1–2 GB RAM is plenty for 3–4 destinations (the relay does `-c copy`,
  no re-encoding).

## Layout

```
/etc/multistream/config.json      # config (templates only, no keys)
/etc/multistream/keys/<profile>/  # 0600 <platform>.env files
/etc/multistream/away.mp4         # off-air loop
/usr/local/bin/multistream        # binary
```

## systemd unit (supervisor)

```ini
[Unit]
Description=Multistream relay supervisor
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/bin/multistream daemon -config /etc/multistream/config.json
Restart=always
RestartSec=5
User=multistream
Group=multistream

[Install]
WantedBy=multi-user.target
```

```bash
sudo useradd --system --no-create-home multistream
sudo systemctl enable --now multistream
sudo systemctl status multistream
```

The `daemon` command spawns and watches the per-platform ffmpeg processes
(and the relay itself when the config manages it). systemd keeps the
daemon alive; the daemon keeps everything else alive.

## Health alerts via cron

`multistream status` exits `0` when everything is healthy and `1` when
anything is down — made for cron:

```bash
# every 5 minutes: log when the chain degrades
*/5 * * * * /usr/local/bin/multistream status -config /etc/multistream/config.json >/dev/null || echo "$(date -Is) stream chain degraded" >> /var/log/multistream-alerts.log
```

For machine-readable monitoring, use `status --json` and feed it to
whatever alerting you already run.

## Key hygiene

- Every platform key lives in a **0600** file under `keys_dir`
  (`<platform>.env`, one `NAME=VALUE` per line).
- The config references only `${NAME}` templates — a `config` dump can be
  shared safely; it never prints key values.
- Rotate by editing the key file and restarting the daemon
  (`systemctl restart multistream`).

## Away loop

Place a short MP4 at the configured `away_file` path so channels show a
branded loop when OBS is not publishing (the relay needs its "always
available" mode on — handled by the daemon when `away_file` is set).

## OBS to VPS

Point OBS at `rtmp://<your-vps-ip>:1935/live/<ingest-path-name>` (the
long random ingest name from your config). Your stream key for OBS is
the ingest path, not a platform key.

## No secrets in the repo

Real hostnames, IPs, ingest paths, and keys stay on the VPS and the
operator's local files only. Everything committed here uses placeholders
like `<your-vps-ip>` and `REPLACE_WITH_YOUR_KEY`.

## Source

Adapted from [arifyaman/multistream](https://github.com/arifyaman/multistream)
(MIT). Supervisor/systemd and cron-alert patterns follow the upstream
README's VPS deployment and automation guidance.
