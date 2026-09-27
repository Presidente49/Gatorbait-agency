# Brand Template — copy this folder to onboard a new business

Preferred: from the repo root run `./new-brand.sh <your-business-slug> "Business Name"`
(it validates the slug, skips this README, fills in the name and sets ACTIVE).

Manual route:
1. Copy every file in this folder **except this README** to `../<your-business-slug>/`
   (agents read every `.md` in the brand folder — this guidance must not come along).
2. Fill in each file below — delete the guidance in italics as you go.
   Start with `about.md`: it says who approves what.
3. Set your slug as the active brand: `echo "<your-business-slug>" > ../ACTIVE`
4. Done. Every agent reads the active brand folder at startup. Agent outputs
   and the run log go in `../<your-business-slug>/outputs/`.

---

## about.md

*The facts: what the business is, location/hours, which platforms it uses,*
*who approves posts / site changes / email sends / spend, where facts are*
*verified, photo-credit and logo rules. No credentials.*

---

## brand-voice.md

*How this business sounds. Write 5–10 rules. Examples: warm vs. clinical,*
*first person vs. third, emoji policy, slang policy, how it handles critics.*

---

## brand-style.md

*Visual identity. Colors (hex), fonts, logo usage, photo vs. graphic*
*preference, image specs per platform, thumbnail rules.*

---

## goals.md

*What this business is trying to achieve. Revenue targets, follower targets,*
*launch dates, campaigns. Update monthly.*

---

## audience.md

*Who the customer is. Age, interests, pain points, where they hang out*
*online, what makes them buy/share/follow.*

---

## offers.md

*What this business sells. Products, services, price points, links to*
*store/booking pages. Agents link posts to these — every post must link*
*to something.*

---

## learnings.md

*Starts empty. This is where the agency writes down what it learns running*
*YOUR business — winning hooks, best post times, top content themes.*
*It compounds. Never delete it; this is the asset.*
