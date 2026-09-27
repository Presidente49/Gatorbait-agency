<!-- Source: Tencent/WeKnora (https://github.com/Tencent/WeKnora) — MIT, Copyright (C) 2025 Tencent. Adapted for Gator Bait Agency (Tencent-authored patterns only; bundled third-party components not used). Full notice: THIRD-PARTY-NOTICES.md -->

# Knowledge Base Spec — file formats

This is the contract for a brand's knowledge base. It is plain markdown, it
works with grep, and the same files are the input to an optional future
WeKnora deploy. The procedure lives in
`agency/skills-library/research/knowledge-base.md`.

## Layout (one KB per brand, never shared across brands)

```
agency/brands/<slug>/knowledge/
  raw/<SID>__<short-name>.<ext>   # the original, verbatim; never edited
  chunks/<SID>.md                 # the chunks of one source
  sources.md                      # source registry (provenance)
  INDEX.md                        # chunk index + entity map
  qa-log.md                       # every question asked, with its answer and citations
  eval.md                         # golden questions → expected chunk IDs
```

`knowledge/` is a subfolder, so agent startup does **not** load it (startup
reads only the top-level `.md` files in the brand folder). Agents open it on
demand. Finished answers that a writer uses go to `outputs/` as usual.

## IDs

- **Source ID (SID):** `S` plus 3 digits, assigned in ingest order (`S001`).
  A SID is never reused, even after a source is superseded.
- **Chunk ID:** `<SID>#c<2 digits>` (`S003#c04`).
- **Citation:** the chunk ID in square brackets, `[S003#c04]`. This is the
  only citation form. Prose such as "per the article" does not count.

## `sources.md` — the provenance registry

```markdown
| SID | Title | Type | Origin | Author / publisher | Published | Retrieved | sha12 | Tier | Status | Supersedes | Raw file |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S001 | ... | article | https://... | Jane Doe / Outlet | 2026-09-01 | 2026-09-27 | 3fa9c2e81b0d | secondary | indexed | — | raw/S001__outlet-review.md |
```

- **Type:** `article` · `transcript` · `pdf` · `stat-sheet` · `note` (a note is
  the client's own words, from an email or call).
- **Origin:** a URL, or `client-provided:<how>`. A source with no origin is
  not ingested.
- **Published:** the date the source says it was published, or `unknown`.
- **Retrieved:** the date scout captured it.
- **sha12:** the first 12 hex characters of `sha256` over the normalized text
  (CRLF converted to LF, trailing whitespace trimmed). It is used for dedup.
  The same sha12 means the same source: do not ingest it again.
- **Tier:**
  - `primary`: the source *is* the fact (official stat sheet, inspection
    report, the subject's own words).
  - `secondary`: reporting about the fact.
  - `unverified`: social posts, anonymous sources. Anything cited from an
    `unverified` source must carry `[VERIFY]` in the answer, which extends
    scout's identity rule.
- **Status:** `pending` → `indexed`, or `failed: <reason>`, or
  `superseded-by:<SID>`. Rows are never deleted. A newer version of the same
  document gets a new SID with `Supersedes: S00x`, and the old row changes to
  `superseded-by:S00y`. This follows WeKnora's "a new attempt never destroys
  the old one" rule, and it keeps old citations resolvable.

## `chunks/<SID>.md` — chunk file

```markdown
# S003 — <title>
source: S003 · type: pdf · tier: primary · published: 2026-07-14

### S003#c01
ctx: Inspection Report > Summary
loc: pdf p.1
kw: inspection, passed, score, 96
ent: Scratch Pizza Co; Hillsborough County EH
num: 96/100; 2026-07-14

<verbatim text of the chunk, copied from raw/, not paraphrased>
```

Field rules:

- **`ctx:`** is the heading breadcrumb, `Doc title > H2 > H3`, stored
  **outside** the verbatim text, as WeKnora's `ContextHeader` is. It helps
  retrieval and never appears inside a quote.
- **`loc:`** says where the chunk is in the original. Use one form per type:
  - text or article: `lines 12-18` (line numbers in `raw/`)
  - pdf: `pdf p.3` (the page, from the `[page N]` markers of the extract)
  - stat sheet: `rows 2-9` (1-based, header row = 1), plus `sheet:<name>` if
    there are several sheets
  - transcript: `t=00:04:10-00:05:02`
- **`kw:`** has 3–8 lowercase search terms: the words a writer would type,
  including synonyms not in the text (for example, "ferment" for a chunk that
  says "proof").
- **`ent:`** lists named people, organizations, products and places, separated
  by semicolons.
- **`num:`** lists every number, date and money amount that appears
  **verbatim** in the chunk. Stats questions are answered from this field
  first.
- The body is **verbatim**. Fixing typos is not allowed. If the source is
  wrong, the answer says so; the chunk does not change.

## Chunking rules

| # | Rule |
|---|---|
| C1 | **Profile first.** If there are 3 or more headings → split at the dominant heading level (the shallowest level that appears 3+ times). Otherwise, if there are structural markers (`[page N]`, timestamps, numbered sections, ALL-CAPS lines, `---`) → split at those markers. Otherwise → split by paragraph, then by line, then by sentence. |
| C2 | **Maximum 900 characters** per chunk (hard limit 1,800 for an unsplittable table row or quote). A heading section that fits stays one chunk **even if it is short**, because topic purity beats size. Merge two adjacent sections only when both are under 200 characters and share the same parent heading. |
| C3 | **Validator:** redo the split one tier down if any of these hold: a source over 1,800 characters produced only 1 chunk; more than a quarter of chunks are under 80 characters; or any chunk is over 1,800 characters. |
| C4 | **Never split inside** a table row, a direct quote, a stat line, a list item, or one speaker turn in a transcript. |
| C5 | **Tables and stat sheets:** each chunk takes whole rows and **repeats the header row** at the top. Group rows by a natural key (category, game, month); aim for 5–15 rows per chunk. |
| C6 | **Atomic records** (Q&A pairs, schedule entries, single stat lines) have **zero overlap**. Narrative text (articles, transcripts) may repeat the last sentence of the previous chunk, capped at 200 characters. |
| C7 | **Transcripts:** one chunk = one **exchange**: a question turn plus the answer turn(s) that follow it, up to 900 characters. Never split a single turn. Single-turn chunks fail C3, because short host questions become tiny chunks. Keep speaker labels and timestamps inside the verbatim text. `loc:` = first to last timestamp. |
| C8 | **PDFs:** extract the text with `[page N]` markers, then save the extract as `raw/<SID>__name.pdf.txt` next to the original `.pdf`. A chunk must not cross a page boundary unless one sentence spans the boundary; in that case use `loc: pdf p.2-3`. |
| C9 | **Preamble:** title, byline, date, URL and recording credits go into `sources.md`, not into a chunk. Any other text before the first split point becomes chunk `c01`. |

## `INDEX.md` — chunk index and entity map

```markdown
# Knowledge index — <Brand>
updated: 2026-09-27 · sources: 4 indexed · chunks: 11

## Chunks
| Chunk | Source (tier, published) | ctx | kw | num |
|---|---|---|---|---|
| S001#c01 | S001 (secondary, 2026-09-01) | Review > Dough | dough, ferment, 72-hour | 72 hours |

## Entities
| Entity | Type | Chunks |
|---|---|---|
| Maria Delgado | person (owner) | S001#c02, S002#c01 |

## Relations
- Maria Delgado —owns→ Scratch Pizza Co [S002#c01]
```

- `INDEX.md` is the keyword lane, so it must be rebuilt, or appended to,
  every time a chunk is added or superseded. Rows for superseded chunks move
  to a `## Superseded` table; they are not deleted.
- **Relations** are optional. Use them only for relationship-heavy material
  (rosters, org charts, supplier chains). Each relation carries the chunk
  that states it, because relations are claims too.

## `qa-log.md` — every answer is logged

```markdown
## 2026-09-27 · Q-003 · asked by scribe · mode: quick
Q: <question as asked>
Rewritten: <standalone query> · kw: ... · ent: ... · num/date: ...
Candidates (fused): S002#c03 0.98 · S001#c02 0.71 · ...
Kept (score ≥ 2): S002#c03 (3), S001#c02 (2)
Answer: <the answer, with [citations]>
Verification: 2/2 citations checked ✓
Gaps: <facts asked for but not in the KB>, or none
```

## `eval.md` — keep retrieval honest

Keep 5–10 golden questions, each with the chunk IDs a correct answer must
cite. After changing any chunking or indexing rule, re-run them and record
**hit@5**: the share of golden questions where every expected chunk shows up
in the top 5 fused candidates. Change one variable at a time. If hit@5 drops,
revert the change.
