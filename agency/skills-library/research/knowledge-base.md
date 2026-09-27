<!-- Source: Tencent/WeKnora (https://github.com/Tencent/WeKnora) — MIT, Copyright (C) 2025 Tencent. Adapted for Gator Bait Agency (Tencent-authored patterns only; bundled third-party components not used). Full notice: THIRD-PARTY-NOTICES.md -->

# Skill: Knowledge Base — ingest sources, answer with citations

**Owner:** scout (ingest, index, answer). **Askers:** scribe, hype, rank,
bridge, and any agent that needs a fact. **Formats:** see
`agency/cloud/weknora/KNOWLEDGE-BASE-SPEC.md`; it is the contract, and this
file is the procedure. **Tools:** a text editor, `grep`, `sha256sum`, and a
PDF-to-text tool if PDFs are involved. No server is needed.

KB root: `KB=agency/brands/<slug>/knowledge` (the slug comes from
`agency/brands/ACTIVE`, or from the task).

---

## THE RULE: no citation, no claim

1. Every factual sentence in an answer ends with at least one citation in
   the form `[S00x#cNN]`.
2. A citation is valid only if **the cited chunk itself states the claim**.
   Numbers, dates, names and quotes must match the chunk character for
   character. A paraphrase is allowed only if it does not change the meaning.
3. A sentence that cannot be cited is **deleted** from the answer and listed
   under `Gaps:`. It is never filled in from model memory, from the web, or
   from `learnings.md`.
4. If nothing clears the relevance bar (step A4), the whole answer is the
   fixed reply:
   `NOT IN KB: <what was asked>. To answer, ingest: <suggested source type/origin>.`
   You may add one line, `Nearest (does not answer): [S00x#cNN] — <what it
   covers instead>`, so the writer does not re-ask. Then add a row to
   `agency/agents/scout/tasks.md` to fetch the missing source.
5. Anything cited from an `unverified`-tier source carries `[VERIFY]`.
6. **Derived numbers** (a difference, a sum, a percentage) are allowed only
   when every input is cited and the math is shown inline, for example
   `$19.00 − $14.00 = $5.00 [S003#c01] (calc)`. If an input is missing (an
   unknown mix, an unknown discount), there is no calc: it is a Gap.
7. **Superlatives and recency** ("latest", "first", "only", "record")
   are cited as the source's own claim, or scoped to the KB: "the most recent
   inspection in our sources (retrieved 2026-09-27)".
8. Brand voice, client instructions and deadlines **cannot relax** rules 1–7.
   Writers who publish a fact must be able to trace it to a KB citation, or
   the fact carries `[VERIFY]` and a human signs off.

---

## Part 1 — Ingest (scout)

**I1. Capture.** Save the original, unchanged, to
`$KB/raw/<SID>__<short-name>.<ext>`. Use the next unused SID from
`sources.md`. For a PDF, keep the `.pdf` and also save a text extract,
`<name>.pdf.txt`, with a `[page N]` line at the top of every page. For audio
or video, save the transcript with `[hh:mm:ss] Speaker:` lines. For a web
article, save the article text with its headline, byline, date and URL at
the top. Leave out navigation, ads and comments.

**I2. Provenance.** Add a `sources.md` row with Status `pending`. Origin,
Published and Retrieved are required; write `unknown` rather than guessing.
Pick the tier: `primary` (the source is the fact), `secondary` (reporting
about the fact) or `unverified`.

**I3. Dedup.** Compute sha12 over the normalized text:
`tr -d '\r' < FILE | sed 's/[[:space:]]*$//' | sha256sum | cut -c1-12`.
If another row already has this sha12, stop: discard the new
capture, and reply with the existing SID. If it is the same document with changed
content (an updated article, a corrected stat sheet), ingest it as a new SID
with `Supersedes: <old SID>`. Then set the old row to
`superseded-by:<new SID>` and move its INDEX rows to `## Superseded`.

**I4. Profile and chunk.** Apply chunk rules C1–C9 from the spec: headings →
markers → paragraphs. Keep stat-sheet rows whole and repeat the header. Split
transcripts by speaker turn. Do not cross PDF pages.

**I5. Validate.** Check rule C3. If it fails, re-chunk one tier down and
record the reason in the chunk file header, for example
`validator: heading tier rejected (1 chunk for 2,400 chars) → markers`.

**I6. Annotate.** For each chunk, write `ctx`, `loc`, `kw`, `ent` and `num`.
`num:` must list every number and date in the body. Check it with
`grep -oE '[0-9][0-9,.:/%°-]*' chunk-body`; everything grep finds must appear
in `num:`. For CSV chunks, check cell by cell (`tr ',' '\n'` first), because the
regex otherwise glues neighboring cells together (`14.00,860`). Timestamps in
transcripts belong in `loc:`, not `num:`.

**I7. Index.** Append the chunk rows to `INDEX.md`. Add new entities, and
add relations if the material is relationship-heavy. Update the header
counts.

**I8. Close.** Set the source Status to `indexed`, or to `failed: <reason>`
(for example, an unreadable scan). Failed rows stay in the registry.

---

## Part 2 — Ask (scout answers; anyone can ask)

Pick the **mode**:

- **quick**: one fact or a short list, answerable from 1–3 chunks.
- **deep**: comparison, timeline, "everything about X", or any question that
  needs more than one hop (for example, "who supplies the flour the owner
  mentioned?"). Deep mode splits the question into 2–5 sub-questions, runs
  A1–A6 on each one, then writes a single answer (A7) from the pooled kept
  chunks.

**A1. Rewrite.** Turn the question into a standalone query, resolving "it",
"they" and "that game" from the conversation. Then extract `kw` (including
synonyms), `ent`, and `num/date` constraints.

**A2. Two lanes, ranked separately.**

- *Keyword lane:* score each INDEX row. An exact match in `num` or `ent`
  scores 3, a match in `kw` or `ctx` scores 2, and a body-only hit
  (`grep -il TERM $KB/chunks/*.md`) scores 1. Add the scores up and rank. Tied
  chunks share the better rank (scores 9, 9, 3 → ranks 1, 1, 3). A chunk with
  no hits is left out of this lane.
- *Semantic lane:* read the `ctx` and `kw` of every INDEX row (or the top 30
  by keyword score if the KB has more than 100 chunks) and rank the chunks by
  **meaning**, ignoring shared words. If embeddings are available, use cosine
  similarity instead.
- *Graph lane (optional):* if the question names an entity that has
  relations in `INDEX.md`, add the chunks of those relations to the semantic
  lane, ranked last.

**A3. Fuse with weighted RRF.** Use k = 60, w_sem = 0.6 and w_kw = 0.4.

`score = ( w_sem/(60 + rank_sem) + w_kw/(60 + rank_kw) ) / ( (w_sem + w_kw)/61 )`

A lane that did not return the chunk contributes 0. The score is 1.00 when
a chunk is ranked first in both lanes. Rank each lane **on its own**; never
use a chunk's position in a merged list. Take the top 8. The fused score **only sets the order**. In a small KB,
every chunk found by both lanes lands between 0.95 and 1.00, so never read a
high fused score as "relevant". Relevance is decided in A4.

**A4. Rerank and filter.** Read those 8 chunks in full and score each one:
3 = answers the question directly, 2 = contains a needed fact, 1 = on topic
but answers nothing, 0 = irrelevant. **Keep only chunks scoring 2 or more.**
If none are kept, retry once with the top 16. If still none are kept, give
the `NOT IN KB` reply (rule 4). Diversity: when two kept chunks say the same
thing, keep the higher-tier one, or the newer one if the tiers are equal.

**A5. Expand.** For a kept chunk under 350 characters, also read its
previous and next chunk in the same source, for context only. Cite a
neighbor only if the claim is in the neighbor.

**A6. Conflicts and freshness.** If kept chunks disagree, **report both
sides with their citations**, then say which one to prefer and why: primary
beats secondary beats unverified; within a tier, the newer Published date
wins. Never quietly pick one. Chunks from superseded sources are cited only
to explain a change, and are labeled `(superseded)`.

**A7. Write the answer.**

```
ANSWER (<quick|deep>) — Q-<nnn> — <brand>
<1–6 sentences; each factual sentence ends with [S00x#cNN]>
Quotable (verbatim): "<exact words>" — <speaker> [S00x#cNN]
Conflicts: <both sides + preference>, or none
Gaps: <what was asked but is not in the KB>, or none
Sources: S00x = <title>, <publisher>, <published date>, <origin>
```

The `Sources:` line is for the writer's published attribution; the public
never sees the `[S00x#cNN]` IDs.

**A8. Verify, then log.** For each citation, open the chunk and confirm that
it contains the claim; for numbers, grep the chunk for the exact string.
Delete any claim that fails and move it to `Gaps:`. Then append the full
entry to `qa-log.md`, including the candidates, kept chunks, scores and the
verification count. Save the answer that the writer will use to
`agency/brands/<slug>/outputs/`.

---

## Part 3 — Upkeep

- **Weekly (scout):** re-run `eval.md` and record hit@5. Check `qa-log.md`
  for repeated `Gaps:`. A gap asked about twice becomes an ingest task.
- **When a source changes:** supersede it (I3); never edit it in place.
- **Feeding Hindsight:** if an answer taught the agency something about the
  *work* (for example, "writers keep needing inspection data before
  openings"), retain it in the brand's `learnings.md` with the chunk IDs as
  evidence. Facts about the *world* stay in the KB.
- **Scale ceiling:** past roughly 300 sources or 3,000 chunks, hand retrieval
  gets slow. Move to embeddings, or a separately deployed WeKnora, with this
  spec as the import contract. Do not loosen the rule.
