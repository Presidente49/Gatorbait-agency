<!-- Source: thesysdev/openui (https://github.com/thesysdev/openui) — MIT, Copyright (c) 2011-2024 Thesys Inc. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->

# Generative UI Specs — the model fills a typed spec, the renderer draws it

**Owners:** blueprint (component libraries, rendering, QA) · scribe (copy that
fills the specs) · webmaster (landing blocks) · wrench (renderer scripts)

## The idea in one paragraph

Never ask a model to *write* a graphic, a landing page or an email. Give it a
**component library** — a short, closed list of named components, each with a
one-line description and typed props — and ask it to **fill a spec**: a JSON
document that only uses those components. A **deterministic renderer** turns
the spec into pixels or HTML. Same spec in, same output out. The model decides
*what to say and which block says it*; the renderer owns *how it looks*. This
is the pattern openui calls Generative UI (their flow: component library →
system prompt → LLM → structured output → renderer). It is the same bet the
agency already made in `agency/studio/web/WEB-DESIGN-TRENDS.md` (JSON-first
site documents) and `agency/studio/creative/README.md` (request JSON + brand
pack → PNGs). This file makes it one discipline across all three surfaces.

## The five parts of a component library

Every surface (graphics, landing blocks, newsletters) defines its library in
markdown with these five parts. Openui builds the same five from code
(`packages/react-email/src/library.ts`: `componentGroups`, examples,
`additionalRules`, `createLibrary`); the agency keeps them as a document so any
agent can read them.

| Part | What it is | Rule |
|---|---|---|
| 1. Root | The one component every spec starts from (e.g. `newsletter`, `landing_page`, `creative_request`) with its required meta (subject, brand slug, status…) | Exactly one root. If the root is missing, nothing renders — fail, don't guess. |
| 2. Components | `type` name + one-line description + props with types, enums, max lengths, required/optional | Distinct names, focused props, enums instead of free text wherever a choice is finite. No two components that do the same job. |
| 3. Groups + placement notes | Components grouped by job ("structure", "content", "proof", "footer") with notes like "footer is always the last block" | Placement rules live here, not in the model's imagination. |
| 4. Valid examples | 2–3 complete, valid specs | Every example must pass the validator. Openui's reliability notes: one wrong example caused double-digit regressions; one targeted rule gained 13 points. Test examples like code. |
| 5. Rules | Short imperative rules for recurring failures | Add a rule only after the same failure shows up twice. Delete rules that no longer fire. |

From parts 1–3 you also publish a **JSON Schema** (openui exports one with
`openui generate --json-schema` / `library.toJSONSchema()`). The schema is the
validator's contract; the markdown is the model's prompt. They must describe
the same library — when you change one, change the other in the same commit.

## The fill → validate → repair → render loop

```
brand folder + brief ──▶ [1 FILL]  model writes spec JSON (only library components)
                              │
                              ▼
                         [2 VALIDATE]  JSON parses? matches schema? business rules?
                              │  errors ──▶ [3 REPAIR] send the error list back, max 2 rounds
                              ▼                          still failing ──▶ stop, human fixes
                         [4 RENDER]  deterministic renderer → PNG / HTML
                              │
                              ▼
                         [5 QA GATE]  surface checklist (QA-PROVENANCE.md, newsletter QA)
                              │
                              ▼
                         [6 HUMAN APPROVAL]  approver per brand about.md — nothing ships before this
```

1. **Fill.** Prompt = the library markdown (parts 1–5) + the brand's voice,
   style, offers and fact sources + the brief. Output = one JSON spec, nothing
   else. Layout-first ordering (root and block order first, then block
   contents) — openui generates top-down so partial output is still a valid
   skeleton; the agency uses it so a truncated response is obvious.
2. **Validate** in three layers, and record every error with a code:
   - `parse` — not valid JSON.
   - `schema` — `unknown-component` (type not in library), `missing-required`,
     `excess-prop` (prop not in schema), `bad-enum`, `too-long`.
   - `business` — surface rules the schema can't express (footer last, one
     primary CTA, every claim has a source, no placeholder images).
   Openui's renderer silently *drops* unknown components and unresolved
   references from arrays and still renders. **The agency does not** — a
   dropped block is a silent content change. Every validation error blocks
   rendering until repaired.
3. **Repair.** Send the model its own spec plus the coded error list: "Fix
   only these errors; return the full spec." Max 2 rounds, then a human fixes
   the spec by hand. (Openui sells this step as a hosted Autofix/Gateway API;
   the agency runs it locally with whatever model wrote the spec — no extra
   vendor, no API key.)
4. **Render** deterministically: the renderer reads only the spec + brand
   pack. No model call inside the renderer. Re-rendering an unchanged spec
   gives byte-identical output (except timestamps in provenance).
5. **QA gate** per surface (below). A failed QA check is a work order on the
   spec, never a hand-edit of the rendered output.
6. **Human approval.** Specs carry `status`. Agents may set `draft` or
   `qa-passed`. Only the approver named in the brand's `about.md` sets
   `approved`. Nothing is sent, posted or published by this loop.

## Edits are patches by block id

Every block carries a stable `id`. To change a spec, the model returns only
the changed blocks (openui "incremental editing" merge rules, adapted):

- **Same id** → the new block replaces the old one.
- **New id** → added; its position is set by the root's block order.
- **Id not in the patch** → kept unchanged (never deleted by omission).
- **Delete** → remove the id from the block order explicitly.

After merging, run the full validate → render → QA loop again. The spec diff
is what a human reviews ("changed hero headline, removed quote block"), not
two HTML files.

## Where each surface's library lives

| Surface | Root | Library + schema | Renderer | QA |
|---|---|---|---|---|
| Campaign graphics | creative request JSON | `TEMPLATE-FAMILIES.md` — each family is a component; its `template_data` is the props schema | creative engine (Playwright harness, outside this repo) | `QA-PROVENANCE.md` |
| Landing blocks / microsites | `{ name, theme, blocks[] }` | `agency/studio/web/WEB-DESIGN-TRENDS.md` block list (`hero`, `features`, `cta`…) | site renderer / Wix section presets | webmaster's page QA + brand-pack token check |
| Email newsletters | `newsletter` | `agency/studio/newsletter/NEWSLETTER-SPEC.md` | email-safe table HTML or MJML, per that file | `agency/studio/newsletter/NEWSLETTER-RUNBOOK.md` |

For graphics: when a family's `template_data` grows beyond 3–4 fields, write
it as a proper component (type, description, typed props, max lengths) so
blueprint can have a model fill it and the validator can check it before a
render is wasted.

## Wire format: JSON with named props (not OpenUI Lang)

Openui's own format, OpenUI Lang, is a line-per-component language with
**positional** arguments (`EmailButton("Order", "https://…", "#B3261E")`). Its
benchmark claims ~50% fewer tokens than JSON and it streams nicely into a live
React preview. The agency still uses JSON with named props because:

- agency specs are reviewed as diffs in git and validated by stock JSON
  Schema tools — both need named keys;
- positional arguments map to props by schema key order, so reordering a
  schema silently changes meaning in old specs;
- the agency does not stream UI into a chat window; token savings on a
  one-off newsletter draft are not the bottleneck — correctness is.

Revisit if a brand ever needs live, streamed previews inside a client app.

## What we did NOT take from openui (and why)

- **"Generate realistic/plausible data" as a prompt rule** (their email
  library's first rule). Rejected: it tells the model to invent numbers. Every
  stat, price, quote or claim in an agency spec must reference a source from
  the brand folder; missing data becomes `[VERIFY]`, which fails QA.
- **Placeholder images** (`picsum.photos` URLs in their rules and examples).
  Rejected: specs use brand-pack or brand-hosted assets only.
- **React at runtime / hosted Gateway, Autofix, Cloud prompt API** (the email
  example needs a `THESYS_API_KEY`). Not adopted: renderers here are
  deterministic templates; repair runs locally. No new vendor dependency.
- **Silent drop of invalid blocks.** Replaced with block-and-repair (above).
- **Hardcoded component colors** (e.g. `#4F46E5` buttons in their email
  components). Replaced with brand-pack theme tokens.
- **The code itself.** Nothing from `packages/` is vendored; this file adapts
  concepts and the component-library structure only.

## Reference (upstream paths, thesysdev/openui @ faf911b)

- `README.md` — Generative UI flow; packages table
- `packages/react-email/src/library.ts` — component groups, examples, rules for email
- `packages/react-email/src/components/*.tsx` — per-component Zod prop schemas
- `docs/content/docs/openui-lang/specification-v05.mdx` — core rules (one root, top-down)
- `docs/content/docs/openui-lang/incremental-editing.mdx` — merge rules
- `docs/content/docs/openui-lang/reliability.mdx` — schema/prompt reliability advice
- `docs/content/docs/openui-lang/renderer.mdx` — error codes, drop behavior
- `packages/openui-cli/src/commands/generate/command.ts` — `--json-schema`, `--spec`
