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
