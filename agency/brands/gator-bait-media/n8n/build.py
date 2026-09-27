#!/usr/bin/env python3
# Generates the three GatorBait n8n workflow files in this folder.
# Run: python3 build.py   (then re-import the changed JSON into n8n Cloud)
import json, os
OUT = os.path.dirname(os.path.abspath(__file__))
DRAFTS_SHEET = '1RuwMQk1n0daDZGX905wieKntx5NJRVGuH6bWeK8a04M'
REPLY_SHEET = '1tycM-ETkxcA30aUiyDFbaED3EpKyB7MGdU_CmINNMts'
GRAPH = 'https://graph.facebook.com/v21.0'
SETTINGS = {'executionOrder': 'v1', 'saveExecutionProgress': True, 'saveManualExecutions': True, 'timezone': 'America/New_York'}
OWNER_EMAIL = 'SET_OWNER_EMAIL_IN_N8N'
META_NOTE = "Credential: 'GatorBait Meta Page token' (Query Auth, name access_token, value = the Page access token). A Page token answers /me as the Page itself, so no Page ID is needed."

def node(id, name, type_, ver, params, pos, notes=None, **extra):
    n = {'id': id, 'name': name, 'type': 'n8n-nodes-base.' + type_, 'typeVersion': ver, 'position': pos, 'parameters': params}
    if notes: n['notes'] = notes
    n.update(extra)
    return n

def chain(names):
    return {a: {'main': [[{'node': b, 'type': 'main', 'index': 0}]]} for a, b in zip(names, names[1:])}

def sheet(id, name, doc, columns, pos, notes):
    return node(id, name, 'googleSheets', 4.5, {
        'operation': 'append',
        'documentId': {'__rl': True, 'mode': 'id', 'value': doc},
        'sheetName': {'__rl': True, 'mode': 'list', 'value': 'gid=0', 'cachedResultName': 'Sheet1'},
        'columns': {'mappingMode': 'defineBelow', 'value': columns},
        'options': {}}, pos, notes)

def gmail(id, name, subject, message, pos, notes):
    return node(id, name, 'gmail', 2.1, {
        'sendTo': OWNER_EMAIL, 'subject': subject, 'emailType': 'text', 'message': message,
        'options': {'appendAttribution': False}}, pos, notes)

def http_meta(id, name, url, query, pos, notes, on_error=False):
    extra = {'onError': 'continueRegularOutput'} if on_error else {}
    return node(id, name, 'httpRequest', 4.2, {
        'method': 'GET', 'url': url, 'authentication': 'genericCredentialType', 'genericAuthType': 'httpQueryAuth',
        'sendQuery': True, 'queryParameters': {'parameters': [{'name': k, 'value': v} for k, v in query]},
        'options': {'timeout': 30000}}, pos, notes, **extra)

def wf(name, nodes, order, extra_conn=None):
    c = chain(order); c.update(extra_conn or {})
    return {'name': name, 'active': False, 'nodes': nodes, 'connections': c, 'settings': SETTINGS,
            'pinData': {}, 'meta': {'templateCredsSetupCompleted': False},
            'tags': []}

# ---------------- 1. Article -> social drafts ----------------
PROMPT_SYSTEM = ("You draft Facebook posts for GatorBait Media, an independent Florida Gators news site. "
 "Voice: confident, fan-first, punchy, AP style; player-name wordplay is welcome. "
 "Use ONLY facts in the headline and excerpt you are given. Never invent a score, stat, quote, injury or name. "
 "Never say 'breaking' unless the headline does. The post must drive readers to the article link. "
 "Return only JSON: {\"hooks\": [3 short opening lines], \"caption\": \"2-3 sentences, no link\", \"hashtags\": [\"#GoGators\", up to 3 more]}.")
rss_code_filter = r"""// Only articles published in the last 6 hours. Stops the first run from
// drafting the whole feed; dedupe below stops repeats after that.
const cutoff = Date.now() - 6 * 60 * 60 * 1000;
return $input.all().filter(i => {
  const t = Date.parse(i.json.isoDate || i.json.pubDate || '');
  return !isNaN(t) && t >= cutoff;
});"""
rss_parse = r"""// Turn Claude's reply into sheet columns. A reply that isn't valid JSON is
// still queued (status needs_edit) so nothing is silently lost.
const src = $('Dedupe by link').item.json;
let d = {};
let status = 'draft';
try {
  const text = ($json.content || []).filter(b => b.type === 'text').map(b => b.text).join('');
  d = JSON.parse(text.slice(text.indexOf('{'), text.lastIndexOf('}') + 1));
} catch (e) { status = 'needs_edit'; }
const hooks = Array.isArray(d.hooks) ? d.hooks : [];
return { json: {
  created_at: $now.toISO(), status, title: src.title, article_url: src.link,
  hook_1: hooks[0] || '', hook_2: hooks[1] || '', hook_3: hooks[2] || '',
  caption: d.caption || '', hashtags: Array.isArray(d.hashtags) ? d.hashtags.join(' ') : '',
  approved_by: '', notes: status === 'needs_edit' ? 'AI reply was not valid JSON; write by hand' : ''
}};"""
rss_summary = r"""// One email per run, however many drafts were queued.
const rows = $input.all().map(i => i.json);
const lines = rows.map(r => `- ${r.title}\n  ${r.article_url}\n  Hook: ${r.hook_1}`);
return [{ json: { count: rows.length, body:
  `${rows.length} new social draft(s) are waiting for approval in the "GatorBait n8n - Social drafts queue" sheet.\n\n` +
  lines.join('\n\n') + `\n\nNothing has been posted. Approve in the sheet, then post from the Page.` } }];"""
body_expr = "={{ JSON.stringify({ model: 'claude-opus-5', max_tokens: 700, system: " + json.dumps(PROMPT_SYSTEM) + ", messages: [{ role: 'user', content: 'Headline: ' + $json.title + '\\nExcerpt: ' + String($json.contentSnippet || '').slice(0, 1500) + '\\nLink: ' + $json.link }] }) }}"
nodes = [
 node('rss-trigger', 'Every 2 hours', 'scheduleTrigger', 1.2, {'rule': {'interval': [{'field': 'hours', 'hoursInterval': 2}]}}, [0, 300]),
 node('rss-read', 'GatorBait blog feed', 'rssFeedRead', 1.2, {'url': "={{ 'https://www.gatorbaitmedia.com/blog-feed.xml?cb=' + $now.toMillis() }}", 'options': {}}, [220, 300],
      "GatorBait's own article feed. The cache-buster matters: Wix caches /blog-feed.xml hard."),
 node('rss-recent', 'Only last 6 hours', 'code', 2, {'mode': 'runOnceForAllItems', 'jsCode': rss_code_filter}, [440, 300]),
 node('rss-dedupe', 'Dedupe by link', 'removeDuplicates', 2, {'operation': 'removeItemsRepeatedWithinPreviousExecutions', 'dedupeValue': '={{ $json.link }}', 'options': {'scope': 'workflow'}}, [660, 300],
      'Remembers every article link it has drafted, across runs.'),
 node('rss-claude', 'Claude drafts the post', 'httpRequest', 4.2, {
      'method': 'POST', 'url': 'https://api.anthropic.com/v1/messages', 'authentication': 'genericCredentialType', 'genericAuthType': 'httpHeaderAuth',
      'sendHeaders': True, 'headerParameters': {'parameters': [{'name': 'anthropic-version', 'value': '2023-06-01'}]},
      'sendBody': True, 'specifyBody': 'json', 'jsonBody': body_expr, 'options': {'timeout': 90000}}, [880, 300],
      "Credential: 'Anthropic API key' (Header Auth, name x-api-key, value = the key). DRAFT ONLY: this never posts anything.",
      retryOnFail=True, maxTries=3, waitBetweenTries=5000),
 node('rss-parse', 'Parse draft', 'code', 2, {'mode': 'runOnceForEachItem', 'jsCode': rss_parse}, [1100, 300]),
 sheet('rss-sheet', 'Add to drafts sheet', DRAFTS_SHEET, {k: '={{ $json.%s }}' % k for k in
       ['created_at','status','title','article_url','hook_1','hook_2','hook_3','caption','hashtags','approved_by','notes']}, [1320, 300],
       "Credential: 'Google (GatorBait)'. Sheet: GatorBait n8n - Social drafts queue, first tab."),
 node('rss-summary', 'One summary', 'code', 2, {'mode': 'runOnceForAllItems', 'jsCode': rss_summary}, [1540, 300]),
 gmail('rss-mail', 'Email Brenden', "={{ 'GatorBait: ' + $json.count + ' social draft(s) to approve' }}", '={{ $json.body }}', [1760, 300],
       "Credential: 'Gmail (GatorBait)'. Set To = your own address after import."),
]
order = ['Every 2 hours','GatorBait blog feed','Only last 6 hours','Dedupe by link','Claude drafts the post','Parse draft','Add to drafts sheet','One summary','Email Brenden']
W1 = wf('GatorBait - Article to social drafts', nodes, order)

# ---------------- 2. Comment monitor ----------------
flatten = r"""// Flatten comments from the Page's recent posts. Only comments from the last
// 45 minutes (runs are 30 apart); dedupe below drops any already queued.
const cutoff = Date.now() - 45 * 60 * 1000;
const out = [];
for (const post of ($input.first().json.data || [])) {
  for (const c of ((post.comments || {}).data || [])) {
    if (Date.parse(c.created_time) < cutoff) continue;
    out.push({ json: {
      comment_id: c.id, post_id: post.id,
      commenter: (c.from && c.from.name) || 'Facebook user',
      comment_text: c.message || '', comment_link: c.permalink_url || post.permalink_url || '',
      created_at: c.created_time
    }});
  }
}
return out;"""
cm_summary = r"""const rows = $input.all().map(i => i.json);
const lines = rows.map(r => `- ${r.commenter}: "${String(r.comment_text).slice(0, 200)}"\n  ${r.comment_link}`);
return [{ json: { count: rows.length, body:
  `${rows.length} new comment(s) on the GatorBait Page. They're queued in "GatorBait n8n - Comment reply queue".\n\n` +
  lines.join('\n\n') + `\n\nNothing was replied to automatically.` } }];"""
nodes = [
 node('cm-trigger', 'Every 30 minutes', 'scheduleTrigger', 1.2, {'rule': {'interval': [{'field': 'minutes', 'minutesInterval': 30}]}}, [0, 300],
      'DETECTOR ONLY. This workflow never replies. Do not add a comment-posting node without Brenden\'s sign-off.'),
 http_meta('cm-fetch', 'Recent posts + comments', GRAPH + '/me/feed',
      [('fields', 'id,permalink_url,comments.order(reverse_chronological).limit(25){id,message,from,created_time,permalink_url}'), ('limit', '10')],
      [220, 300], META_NOTE),
 node('cm-flatten', 'New comments only', 'code', 2, {'mode': 'runOnceForAllItems', 'jsCode': flatten}, [440, 300]),
 node('cm-dedupe', 'Dedupe comments', 'removeDuplicates', 2, {'operation': 'removeItemsRepeatedWithinPreviousExecutions', 'dedupeValue': '={{ $json.comment_id }}', 'options': {'scope': 'workflow'}}, [660, 300]),
 sheet('cm-sheet', 'Add to reply queue', REPLY_SHEET, {**{k: '={{ $json.%s }}' % k for k in ['created_at','commenter','comment_text','comment_link','post_id','comment_id']},
       'handled': 'false', 'suggested_reply': '', 'notes': ''}, [880, 300], "Credential: 'Google (GatorBait)'. Sheet: GatorBait n8n - Comment reply queue."),
 node('cm-summary', 'One summary', 'code', 2, {'mode': 'runOnceForAllItems', 'jsCode': cm_summary}, [1100, 300]),
 gmail('cm-mail', 'Email Brenden', "={{ 'GatorBait: ' + $json.count + ' new Page comment(s)' }}", '={{ $json.body }}', [1320, 300],
       "Credential: 'Gmail (GatorBait)'. Set To = your own address after import."),
]
W2 = wf('GatorBait - Comment monitor', nodes, ['Every 30 minutes','Recent posts + comments','New comments only','Dedupe comments','Add to reply queue','One summary','Email Brenden'])

# ---------------- 3. Weekly digest ----------------
digest = r"""// Weekly numbers in plain English. Any source that failed shows as
// "unavailable" instead of stopping the report.
const get = (n) => { try { return $(n).first().json; } catch (e) { return {}; } };
const page = get('Page + Instagram IDs');
const fb = get('Facebook insights (7 days)');
const ig = get('Instagram insights (7 days)');
const wix = get('Wix site traffic (7 days)');
const n = (v) => (typeof v === 'number' ? v.toLocaleString('en-US') : 'unavailable');
const fbSum = (name) => { const m = (fb.data || []).find(x => x.name === name); return m ? (m.values || []).reduce((a, v) => a + (Number(v.value) || 0), 0) : undefined; };
const igVal = (name) => { const m = (ig.data || []).find(x => x.name === name); return m && m.total_value ? m.total_value.value : undefined; };
const wixTot = (t) => { const m = (wix.data || []).find(x => x.type === t); return m ? m.total : undefined; };
const errs = [fb, ig, wix].filter(x => x.error).map(x => (x.error.message || JSON.stringify(x.error)).slice(0, 160));
const week = $now.minus({ days: 7 }).toFormat('MMM d') + ' - ' + $now.minus({ days: 1 }).toFormat('MMM d, yyyy');
const body = [
  `GatorBait weekly numbers, ${week}`, '',
  `WEBSITE (Wix)`,
  `  Sessions: ${n(wixTot('TOTAL_SESSIONS'))}`,
  `  Unique visitors: ${n(wixTot('TOTAL_UNIQUE_VISITORS'))}`, '',
  `FACEBOOK (${page.name || 'Page'})`,
  `  Followers: ${n(page.followers_count)}`,
  `  Post engagements: ${n(fbSum('page_post_engagements'))}`,
  `  Views: ${n(fbSum('page_media_view'))}`, '',
  `INSTAGRAM`,
  `  Followers: ${n((page.instagram_business_account || {}).followers_count)}`,
  `  Reach: ${n(igVal('reach'))}`,
  `  Profile views: ${n(igVal('profile_views'))}`, '',
  errs.length ? 'Sources with errors (numbers above show "unavailable"):\n  ' + errs.join('\n  ') : 'All sources reported.',
  '', 'Read-only report. Nothing was posted or changed.'
].join('\n');
return [{ json: { body, week } }];"""
since = "={{ $now.minus({days: 7}).startOf('day').toSeconds() }}"
until = "={{ $now.startOf('day').toSeconds() }}"
nodes = [
 node('wd-trigger', 'Monday 8 a.m.', 'scheduleTrigger', 1.2, {'rule': {'interval': [{'field': 'cronExpression', 'expression': '0 8 * * 1'}]}}, [0, 300]),
 http_meta('wd-ids', 'Page + Instagram IDs', GRAPH + '/me', [('fields', 'id,name,followers_count,instagram_business_account{id,followers_count}')], [220, 300], META_NOTE, on_error=True),
 http_meta('wd-fb', 'Facebook insights (7 days)', GRAPH + '/me/insights', [('metric', 'page_post_engagements,page_media_view'), ('period', 'day'), ('since', since), ('until', until)], [440, 300],
      'Meta retires Page Insights metrics from time to time. If this errors, the digest still sends and names the error.', on_error=True),
 http_meta('wd-ig', 'Instagram insights (7 days)', "={{ 'https://graph.facebook.com/v21.0/' + (($('Page + Instagram IDs').first().json.instagram_business_account || {}).id || 'missing-instagram-link') + '/insights' }}",
      [('metric', 'reach,profile_views'), ('period', 'day'), ('metric_type', 'total_value'), ('since', since), ('until', until)], [660, 300],
      'Instagram account ID comes from the Page (instagram_business_account); nothing to fill in.', on_error=True),
 node('wd-wix', 'Wix site traffic (7 days)', 'httpRequest', 4.2, {
      'method': 'GET', 'url': 'https://www.wixapis.com/analytics/v2/site-analytics/data',
      'authentication': 'genericCredentialType', 'genericAuthType': 'httpHeaderAuth',
      'sendHeaders': True, 'headerParameters': {'parameters': [{'name': 'wix-site-id', 'value': '18fb3a4e-d7f6-414a-aeb9-3047db3ea115'}]},
      'sendQuery': True, 'queryParameters': {'parameters': [
          {'name': 'dateRange.startDate', 'value': "={{ $now.minus({days: 7}).toFormat('yyyy-MM-dd') }}"},
          {'name': 'dateRange.endDate', 'value': "={{ $now.minus({days: 1}).toFormat('yyyy-MM-dd') }}"},
          {'name': 'measurementTypes', 'value': 'TOTAL_SESSIONS'},
          {'name': 'measurementTypes', 'value': 'TOTAL_UNIQUE_VISITORS'}]},
      'options': {'timeout': 30000}}, [880, 300],
      "Credential: 'Wix API key (read-only analytics)' (Header Auth, name Authorization, value = a Wix API key with only Site Analytics read permission).",
      onError='continueRegularOutput'),
 node('wd-compile', 'Write the digest', 'code', 2, {'mode': 'runOnceForAllItems', 'jsCode': digest}, [1100, 300]),
 gmail('wd-mail', 'Email Brenden', "={{ 'GatorBait weekly numbers, ' + $json.week }}", '={{ $json.body }}', [1320, 300],
       "Credential: 'Gmail (GatorBait)'. Set To = your own address after import."),
]
W3 = wf('GatorBait - Weekly numbers digest', nodes, ['Monday 8 a.m.','Page + Instagram IDs','Facebook insights (7 days)','Instagram insights (7 days)','Wix site traffic (7 days)','Write the digest','Email Brenden'])

for fn, w in [('article-to-social-drafts.json', W1), ('comment-monitor.json', W2), ('weekly-numbers-digest.json', W3)]:
    json.dump(w, open(os.path.join(OUT, fn), 'w'), indent=2, ensure_ascii=False); print('wrote', fn, len(w['nodes']), 'nodes')
