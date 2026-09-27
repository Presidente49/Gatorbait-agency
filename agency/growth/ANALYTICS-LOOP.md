<!-- Source: coreyhaines31/marketingskills (https://github.com/coreyhaines31/marketingskills) — MIT. Adapted for Gator Bait Agency. -->
<!-- Source: ericosiu/ai-marketing-skills (https://github.com/ericosiu/ai-marketing-skills) — MIT. Adapted for Gator Bait Agency. -->
# Analytics Loop — Track for Decisions, Close the Loop

**Primary owner:** wrench (implements tracking, runs readbacks). Every other agent reads the data this loop produces; nobody acts on vibes when numbers exist.

## Principle 1: track for decisions, not data

Every event must inform a decision. Vanity metrics are clutter. Work backwards: *What do I need to know? What action will I take based on it? What must I track to know it?*

## Principle 2: a loop isn't closed until the change is judged

A workflow is not a closed loop until it checks whether the change worked and updates the playbook from that evidence. Platform truth wins over opinions. Every change gets a **readback** (see below) before its lesson enters the agency playbook.

## Event naming: object_action

Lowercase, underscores, specific. Context goes in properties, not the event name.

```
cta_hero_clicked        (not "button_clicked")
form_submitted          + properties: form_type, form_location
article_read            + properties: article_id, read_depth
checkout_payment_completed + properties: product_id, value
signup_completed        + properties: method, source
```

**Rules:** no spaces/special characters, no PII in properties, document naming decisions where the brand's tracking plan lives.

## Essential events by surface

| Surface | Events |
|---|---|
| Site / store | `page_viewed`, `cta_clicked` (button_text, location), `article_read`, `product_viewed`, `add_to_cart`, `checkout_payment_completed`, `newsletter_subscribed` |
| Social funnel | `post_published`, `link_clicked` (utm), `profile_visited`, `follower_gained`, `comment_replied` |
| Video | `video_published`, `hook_style`, `cta_type`, `watch_time_bucket`, `subscriber_gained` |
| Paid | `ad_served`, `ad_clicked`, `landing_arrived`, `conversion_completed` — always with full UTM set |

## UTM strategy

`utm_source` (google, newsletter, meta) · `utm_medium` (cpc, email, social) · `utm_campaign` (name it per real campaign) · `utm_content` (differentiate versions: `hero_cta`, `carousel_slide_2`) · `utm_term` (paid search keywords).

Conventions: lowercase everything, consistent separators, specific over generic (`blog_footer_cta` not `cta1`). Document all UTMs — an undocumented UTM is a dead end.

## Validation checklist (before trusting any data)

- [ ] Events fire on the correct triggers (and only once — no duplicates)
- [ ] Properties populate with real values
- [ ] Works across browsers and mobile
- [ ] Conversions recorded correctly
- [ ] No PII leaking into properties
- [ ] Consent handling in place where required (EU/UK/CA)

Common failure order when numbers look wrong: broken trigger → wrong variable → duplicate container → real behavior change. Check in that order.

## The readback — how every change gets judged

Run a readback after every test, content change, or strategy shift. No readback, no lesson.

```markdown
# Readback: <what changed>

## Verdict
Promote / keep testing / rollback / unproven

## Change tested
<what changed, who owned it>

## Data pulled
| Source | Window | Status |

## Baseline vs candidate
| Metric | Baseline | Candidate | Delta | Interpretation |

## Caveats
<confounders: seasonality, campaigns running in parallel, dirty attribution, low volume>

## Patch
<what changes in the skill/playbook/runbook>

## Next readback
<date + metric>
```

### Promotion rules

Promote when: the candidate beats baseline on the **primary metric** and downside metrics aren't meaningfully worse — or it exposes a repeatable audience signal.

Do NOT promote when: volume is too low · attribution is too dirty · the result is explained by seasonality or unrelated campaigns · the data source failed · **only the author liked it.** (That last one is harsh but important.)

### Analytics by surface — what to track where

- **Social:** impressions, engagement rate, replies, shares, bookmarks, profile clicks, follower delta — plus creative metadata: post length, hook style, proof number, CTA type, topic bucket. Use it for hook formulas, CTA patterns, post timing, topic scoring.
- **Video:** impressions, CTR, average view duration, retention curve, watch time, subscribers gained, comments, traffic source — plus title/thumbnail/hook metadata, length, topic bucket. Use it for title formulas, thumbnail rules, first-15-second hooks, retention beats, Shorts cutdowns.
- **SEO:** clicks, impressions, CTR, average position, query/page mix, sessions, conversions — plus a change log of what was edited and when. Use it for content refresh patterns, internal linking, query prioritization, rollback decisions.
- **Revenue:** pipeline movement, content-assisted revenue, CPA by content type. Use it for content investment decisions.

## Safety boundary

Read-only analytics pulls are always fine. External writes still need approval: publishing/editing site content, changing ad accounts/bids/budgets/targeting, mutating CRM/email tools, sending messages. This matches the agency's standing rule: only interrupt the owner for money, deletions, credentials, CAPTCHAs, and licensing.
