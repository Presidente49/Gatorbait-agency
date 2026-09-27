<!-- Source: charlie947/social-media-skills (https://github.com/charlie947/social-media-skills) — MIT. Adapted for Gator Bait Agency. -->
# Hook Generator

**Owner:** scribe (writing)

Generate 6 click-worthy hook variations for any topic. Two-line hooks: a 40-character opening line plus a 40-character bold contrast line. Fast output, no preamble.

## Trigger

Requests like "write me hooks", "hook ideas", "generate hooks", "I need a hook for a post about...", or a topic pasted with a request for openers.

## Step 1. Get the topic

If the topic is already supplied, use it. Otherwise ask: "What topic do you want hooks for?"

## Step 2. Write 6 hook variations

Every hook has the same structure:

- **Line 1 (Opening)**: 40 characters maximum. No questions. States something unexpected, specific, or punchy.
- **Line 2 (Contrast)**: 40 characters maximum. Contradicts, reframes, or undercuts the opening.

Every variation must:

- Use first-person experience only when the brand has supplied it. Otherwise use an evidence-backed nonpersonal angle.
- Include a digit or metric where possible.
- Build tension: curiosity gap, stakes, surprise.

Produce 6 variations covering different angles:

1. **Number-led**: lead with a specific number or metric
2. **Contrarian**: state a belief, then flip it
3. **Before/after**: transformation with a digit
4. **Authority reference**: reference a name, tool, or brand
5. **Admission**: confess a mistake or loss
6. **Future shock**: a prediction or "X is about to change"

## Step 3. Output format

```
HOOKS for [topic]

1. [Number-led]
[Line 1]
[Line 2]

2. [Contrarian]
[Line 1]
[Line 2]

3. [Before/after]
[Line 1]
[Line 2]

4. [Authority reference]
[Line 1]
[Line 2]

5. [Admission]
[Line 1]
[Line 2]

6. [Future shock]
[Line 1]
[Line 2]
```

## Step 4. Offer the next move

Ask: "Want me to build one of these into a full post? Call the post-formatter skill with the hook number."

## Rules

- 40 characters maximum per line. Count them with a text tool before delivery.
- No questions in the opening line.
- No filler words. Every word earns its place.
- Prefer digits over spelled numbers (3, not three).
- Preserve uncertainty in the source. Never invent a result or certainty to make a hook stronger.
