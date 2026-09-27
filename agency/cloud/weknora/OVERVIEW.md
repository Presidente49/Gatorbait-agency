<!-- Source: Tencent/WeKnora (https://github.com/Tencent/WeKnora) — MIT, Copyright (C) 2025 Tencent. Adapted for Gator Bait Agency (Tencent-authored patterns only; bundled third-party components not used). Full notice: THIRD-PARTY-NOTICES.md -->

# WeKnora — Overview (scout's knowledge base)

**What it is:** WeKnora (Tencent, v0.8.2, commit `4df7ccb`, read 2026-09-27) is
a self-hosted document-understanding and retrieval-augmented Q&A platform: Go
backend, document-reader sidecar, Postgres/pgvector+BM25 (or Qdrant, Milvus,
Elasticsearch, etc.), optional Neo4j knowledge graph, and a web UI.

**What we took:** the *design*, not the application. Scout gets a per-brand,
plain-markdown knowledge base that any agent can build and query by hand (or
with grep). No server, no vector database and no Docker are needed. The full
format is in `KNOWLEDGE-BASE-SPEC.md`. The procedure is in
`agency/skills-library/research/knowledge-base.md`.

## Patterns borrowed, with upstream location

| Pattern | Upstream (Tencent-authored docs/code, read only) | Our version |
|---|---|---|
| Ingest lifecycle: hash dedup → `pending` → parse → chunk → index → `indexed`/`failed`; re-parse starts a new attempt and never destroys the old one | `website-docs/02-architecture/03-document-pipeline.md` (§2.4 dedup, §2.5 status) | `sources.md` registry with `sha12`, status, `supersedes` |
| Adaptive chunking: profile the document → heading tier → heuristic tier → recursive fallback; a validator rejects bad splits | `website-docs/03-features/04-chunking.md`; `internal/infrastructure/chunker/{profiler,strategy,validator}.go` | Chunk rules C1–C9 in the spec (plus exchange-based transcript chunks, our addition) |
| Context header (heading breadcrumb) stored apart from the verbatim chunk text | `04-chunking.md` §4; `internal/types/chunk.go` (`ContextHeader`) | `ctx:` field on every chunk |
| Table header tracking: every table fragment repeats its column header | `04-chunking.md` §3.4; `internal/infrastructure/chunker/header_tracker.go` | Stat-sheet rule C5 |
| Atomic records (FAQ) are one chunk each, with zero overlap | `04-chunking.md` §6 | Rule C6 (stat rows, Q&A, schedules) |
| Source locator: a chunk points back to the exact place in the original (PDF page, sheet rows, time range, text range) plus a short quote | `internal/types/source_locator.go` (`SourceLocator`, quote ≤ 300 runes) | `loc:` field and citation IDs |
| Hybrid retrieval: separate keyword and semantic lanes fused by weighted RRF, normalized to 0–1 | `website-docs/03-features/05-retrieval-engines.md` §5.2; `internal/application/service/knowledgebase_search_fusion.go` | Ask step A3 |
| Rerank with a threshold, then a diversity pass (MMR) and near-duplicate removal | `website-docs/02-architecture/04-rag-pipeline.md` §3.4, §3.6 | Ask step A4 |
| Short-hit neighbor expansion (a hit under 350 characters pulls its previous/next chunk from the same source) | `04-rag-pipeline.md` §3.6 step 7 (`merge_expand.go`) | Ask step A5 |
| References are emitted *before* the answer; "search found nothing" is a first-class outcome with a fixed reply | `04-rag-pipeline.md` §2.5 (`ErrSearchNothing`, `FallbackStrategyFixed`) | "No citation, no claim" rule |
| Business instructions never override the citation or factuality rules | `internal/types/prompt_instructions.go` | Brand voice cannot relax citation rules |
| Entity/relation extraction for relationship-heavy material, as an optional lane | `website-docs/03-features/09-knowledge-graph.md` | `## Entities` block in `INDEX.md` |
| Quick-answer vs. multi-step "smart reasoning" modes | `website-docs/03-features/07-agent.md` | `quick` / `deep` ask modes |
| Evaluation on a fixed golden set, changing one variable at a time | `website-docs/03-features/15-evaluation.md` | `eval.md` hit@k check |

General techniques are credited where they belong. RRF is from Cormack et al.
(2009) and MMR is from Carbonell & Goldstein (1998); neither is Tencent's
invention. We take WeKnora's specific *application* of them, such as
normalizing RRF by its theoretical maximum and never ranking a list by its
concatenated position.

## How it fits with Hindsight (not a duplicate)

| | WeKnora-style KB (this) | Hindsight memory (`agency/cloud/hindsight/`) |
|---|---|---|
| Holds | What **outside sources say**: articles, transcripts, PDFs, stat sheets | What **the agency experienced and concluded**: results, observations, mental models |
| Unit | Chunk with a source locator | Observation with a proof count |
| Owner | scout (ingest and answer), writers (ask) | Every agent retains; wrench reflects |
| Truth test | "Does the cited chunk say this?" | "How much evidence backs this belief?" |
| Location | `agency/brands/<slug>/knowledge/` | Brand `learnings.md` and the memory banks |

The two connect in one direction only. A Hindsight observation may cite KB
chunks as evidence (`Evidence: [S004#c03]`). A KB answer never cites
learnings, because learnings are our opinions and not sources.

## Deliberately NOT taken

- **The application itself** (Go services, docreader, Docker/Helm, frontend,
  desktop apps, MCP server). It is concepts only; nothing is vendored or
  deployed. If a brand outgrows markdown (roughly more than 300 sources), the
  deploy path is to run WeKnora as separate infrastructure under its own
  license and keep this spec as the contract.
- **Every bundled third-party component**, including `third_party/anydoc-go`
  (MIT, © Sideguide Technologies), go-sql-driver/mysql and go-m1cpu (MPL-2.0),
  OpenCC dictionary data (Apache-2.0), go-urn (listed as "nolicense"),
  python-docx (listed as "unknown"), and the long Apache/BSD/MIT/CC-BY list in
  upstream `LICENSE`. None of their code, data or text was copied.
- **Model free-answer fallback** (`FallbackStrategyModel`). When retrieval
  finds nothing, WeKnora can let the model answer from its own knowledge. For
  writers, that is how invented stats get published. Rejected, see the
  no-citation-no-claim rule.
- **Memory-affinity boost** (`memory_affinity.go`), which up-weights
  documents that past answers cited often. It is a popularity loop that
  buries new sources. Rejected.
- **Web search merged into answers.** A web result must be ingested as a
  source first, so it gets an ID, a hash and a locator. Only then can it be
  cited.
- **Auto long-term memory extraction** (`23-memory.md`). Hindsight already
  owns memory.
