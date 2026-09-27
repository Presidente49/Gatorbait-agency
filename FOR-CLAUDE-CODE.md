# FOR CLAUDE CODE — review directive from Brenden

Brenden's orders: **give this repo a good looking over.** You have the
whole thing. Marlowe (the CMO agent) runs the stack on it — you review,
harden, and improve the machinery.

## What to review

1. **Structure** — `agency/` layout: `agents/` (8), `shared/`,
   `brands/` (white-label system), `skills-library/`, `studio/`
   (production company), `cloud/` (n8n + scheduler). Does it hang
   together? What's missing or redundant?
2. **White-label completeness** — can a new business really onboard in
   15 minutes via `new-brand.sh` + `_template/`? Try it mentally with a
   non-sports business (e.g., a pizza shop). Fix gaps.
3. **Agent identities** — each `agents/<codename>/identity.md`: is the
   role sharp, are duties executable, do the startup steps work?
4. **Skills library** — `skills-library/`: are the skills genuinely
   usable by an AI agent reading markdown? Cut or fix anything vague.
5. **Studio pipelines** — `studio/`: clipping → captions → reels →
   publish. Are the runbooks something an agent can actually follow
   step by step? Flag missing tooling or impossible steps.
6. **Cloud** — `cloud/n8n/`: docker-compose correctness, workflow JSON
   validity, secrets handling (nothing hardcoded — ever).
7. **Learnings loop** — does every workflow append to the brand's
   `learnings.md` and, when transferable, to `shared/learnings.md`?
8. **Attribution & licenses** — every borrowed file needs repo name,
   URL, license. Nothing AGPL/GPL/unlicensed gets copied in.

## How to report

Write your findings to `REVIEW.md` at repo root: what's solid, what's
broken, what you fixed, what needs a human decision. Fix what you can;
flag what you can't. Then Marlowe runs the stack on it.
