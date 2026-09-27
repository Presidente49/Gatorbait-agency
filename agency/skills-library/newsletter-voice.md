<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT, Copyright (c) 2026 Charlie Hills. Adapted for Gator Bait Agency. Full notice: THIRD-PARTY-NOTICES.md -->
# Newsletter Voice

**Owner:** scribe (writing)

Build newsletter writing instructions for the active brand. Runs after `voice-builder.md`. Produces a `newsletter-voice.md` file in the brand folder that the agent references when drafting newsletters in the brand's voice.

## Trigger

Requests like "build my newsletter voice", "learn my newsletter style", "set up my newsletter system", "train on my newsletters", "newsletter onboarding", or newsletter samples dropped in asking for an analysis.

## Prerequisites check

Requires the brand folder to already have `brand-voice.md` and `audience.md` (or the equivalent from a `voice-builder` run). If either is missing, stop and redirect to `voice-builder.md` first.

## Step 1. Check for samples

Ask: "Do you have 2 to 3 past newsletter issues I can learn from? Yes: paste them here. No: type 'archetype' and I will build from a template tuned to your voice."

- 2+ samples: go to Step 2a.
- "archetype": go to Step 2b.
- 1 sample: ask for at least one more; if they only have one, offer archetype mode using the single sample as a reference point.

## Step 2a. Sample-based analysis

Read every newsletter fully. Look for patterns across issues, not one-off quirks:

- **Opening formula**: what the first 3 sentences do, length before the first structural break, credibility move, value promise
- **Section structure**: problem/contrast setup, named frameworks, steps, examples, bonus sections, closing formula and signoff
- **Data philosophy**: specific numbers per issue, source attribution style, example-to-abstraction ratio, failure acknowledgements
- **Formatting**: headers, lists, bold/italic usage, code blocks, blockquotes, visual markers
- **Length**: word count range and section counts
- **Voice markers unique to newsletter format**: callouts, forward-looking closings, consistent signoff, meta-transparency
- **Absence signals**: words, constructions, or structures absent from every sample; topics never touched

Then go to Step 3.

## Step 2b. Archetype selection

Ask which of these 6 newsletter archetypes fits what they want to write:

1. **Data tutorial**: numbers, frameworks, step-by-step methods
2. **Contrarian essay**: take a position, defend it, name the opposition
3. **Case study teardown**: one subject per issue, unpacked in depth
4. **Curated digest**: 5 to 7 links with commentary each issue
5. **Personal essay**: reflection on a theme, story-first
6. **Interview or profile**: one person per issue, Q and A or narrative

Load the matching defaults from the Newsletter Archetypes appendix at the end of this file. Tune every field using the brand's voice and audience files. Flag in the output that archetype defaults were used and recommend revisiting after 5 published issues.

## Step 3. Write newsletter-voice.md

Save to the brand folder. Target 800 to 1,200 words. Structure:

```
# Newsletter Voice

## Source
[Sample-based: analysed X newsletter issues] OR [Archetype-based: [archetype name] tuned to brand voice. Revisit after 5 published issues.]

## Audience and purpose
[Who reads this newsletter and what they get from it. 2 to 3 sentences from the brand files.]

## Voice principles
[3 to 5 core principles the writing always holds. Short declarative sentences.]

## Opening formula
[How issues start. Include 2 concrete templates with bracketed placeholders, e.g. "[Specific result with number]. [Credibility marker]. [Value promise for this issue]." Target word count for the opening section.]

## Section flow
[Standard structure of an issue, 5 to 8 sections max, with notes on what each does and how long it runs.]

## Data and evidence
[How numbers and examples are used. Specific rules: source style, example-to-abstraction ratio.]

## Formatting rules
[Headers, lists, bold, italic, code blocks, visual markers. What to use, what to avoid.]

## Closing and signoff
[How issues end. Signoff phrase only if consistent across samples — never invent one.]

## What this newsletter never does
[3 to 5 behaviours from absence patterns. Behaviours only, not a banned-words list.]

## Length
[Word count target for standard issues. Separate target for long guides if the brand writes both.]
```

Fill every section from the samples (or tuned archetype defaults). No generic filler. Where samples show no pattern, say "no clear pattern across samples" rather than guessing. Do not duplicate `brand-voice.md`; newsletter-voice.md adds newsletter-specific rules only.

## Step 4. Confirm and hand off

Tell the client: "Your newsletter voice is built. newsletter-voice.md is in your brand folder alongside your voice files. When you want to draft an issue, say 'write a newsletter' and I will use all of them together." If archetype mode was used, remind them to re-run with real samples after ~5 published issues.

## Rules

- Require voice and audience files before running. Minimum 2 newsletter samples for sample mode.
- Keep newsletter-voice.md under 1,200 words. Tight beats exhaustive.
- Do not invent voice signals. Work only from samples or archetype defaults tuned to the brand voice.
- Do not bake in specific names, URLs, or signoff phrases unless consistent across 2+ samples.

---

## Appendix: Newsletter Archetype Defaults

Loaded when the client runs without sample newsletters. Tune every field to the brand voice before writing newsletter-voice.md.

### 1. Data tutorial

Best for: teaching with numbers, frameworks, step-by-step methods.

- **Opening**: Lead with a specific result (impressions, revenue, time saved). Add a credibility marker. End with a value promise. Template: "[Specific number and result]. [Credibility marker in one line]. By the end of this issue, you will [concrete outcome]."
- **Sections**: Hook + promise (50-100 words) > Problem (100-200) > Framework introduction (100-150) > Step-by-step breakdown (200-400 per step) > Examples with results (100-200 each) > Bonus application (200-300) > Closing (50-100)
- **Data**: every claim backed by a specific number. Sources linked inline. Example-to-abstraction ratio roughly 3:1.
- **Formatting**: headers for sections, numbered lists for steps, blockquotes or code blocks for prompts, arrow bullets for benefit lists, minimal bold.
- **Length**: 1,500 to 2,500 words standard.
- **Never**: vague claims without numbers, generic tips without steps, motivational-summary closings, filler padding.

### 2. Contrarian essay

Best for: strong opinions that stake positions.

- **Opening**: name the conventional wisdom, state the counter-position, flag what is at stake. Template: "[Everyone believes X]. [You believe Y]. [If Y is right, here is what changes]."
- **Sections**: The consensus (150-250 words) > Why it is wrong (300-500) > The counter-position (100-200) > Evidence (300-500) > Objections and responses, steel-manned (200-400) > Implication (150-250) > Closing, no fence-sitting (50-100)
- **Data**: evidence weighted toward the counter-position but include opposing data honestly. Named examples only.
- **Formatting**: headers, blockquotes for opposing views or quotes, minimal lists, prose-heavy.
- **Length**: 1,200 to 2,000 words.
- **Never**: straw-manning the opposition, hedging the main position, concluding without a clear stance.

### 3. Case study teardown

Best for: unpacking one subject per issue in depth.

- **Opening**: name the subject and the outcome. Frame the lesson. Template: "[Subject] did [X] and got [result]. Here is what worked, what failed, and what transfers."
- **Sections**: Hook (100-150 words) > Background (200-300) > Teardown (400-700) > What worked (200-400) > What failed (200-400) > Transferable lessons (200-300) > Closing (50-100)
- **Data**: quote metrics, timelines, decisions. Link sources. Flag speculation as speculation.
- **Formatting**: headers for phases, numbered takeaways, pull quotes for standout facts.
- **Length**: 1,500 to 2,500 words.
- **Never**: speculating without flagging it, praising without critique, reducing the case to a single cause.

### 4. Curated digest

Best for: aggregating and commenting on the week or month.

- **Opening**: set the period's theme, tease the most interesting item. Template: "[Theme of the week in one line]. The piece you most need to read is [item]."
- **Sections**: Theme paragraph (50-100 words) > 5 to 7 main items (80-150 words each: link, title, 2-3 sentences of commentary, not summary) > 2 to 4 quick hits (100-200 words total) > Closing (50-100)
- **Data**: attribution on every link. No link without commentary. Commentary adds a point the original did not make.
- **Formatting**: headers per item, links inline, bold only for item titles.
- **Length**: 800 to 1,500 words.
- **Never**: summarising without adding an opinion, skipping attribution, ordering by recency instead of importance.

### 5. Personal essay

Best for: reflection through story.

- **Opening**: in medias res. Drop into a scene. No setup. Template: "[Concrete scene, one paragraph]. [Question or tension the scene raises]."
- **Sections**: Opening scene (150-300 words) > Question or tension (100-200) > Exploration (400-700) > Turn: insight or realisation (150-300) > Closing reflection (100-200)
- **Data**: specifics over abstractions. Names, places, dates, sensory details. No made-up numbers.
- **Formatting**: minimal, prose-heavy, section breaks only where pacing needs them, no lists.
- **Length**: 800 to 1,800 words.
- **Never**: wrapping with a neat moral, explaining the insight before showing the story, using a story as decoration.

### 6. Interview or profile

Best for: featuring one person per issue.

- **Opening**: a specific moment or direct quote from the subject, plus why they matter. Template: "[Subject quote or specific moment]. [Why they matter, in one line]."
- **Sections**: Who they are and why now (100-200 words) > Origin (200-400) > Work (300-500) > Views (300-500) > Lessons, 3 to 5 transferable insights (200-400) > What is next (100-200)
- **Data**: direct quotes over paraphrase. Specific milestones. Named projects. Timelines with dates.
- **Formatting**: Q and A or narrative with pull quotes, bold for the subject name on first mention only.
- **Length**: 1,500 to 2,500 words.
- **Never**: fawning, generic questions, skipping pushback on strong claims.

To build the issue itself, follow `agency/studio/newsletter/NEWSLETTER-RUNBOOK.md` (typed newsletter spec → email-safe HTML → QA → human approval; never auto-send).
