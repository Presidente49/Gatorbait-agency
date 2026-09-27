# Email Delivery Check (Campaign Send and Proof of Delivery)

**Primary owner:** wrench (send mechanics and proof), with scribe (content). Use it for every one-off newsletter or story email.

## Before sending

1. **Owner's yes** for this specific send. An earlier approval doesn't carry over to a new email.
2. **Dedupe:** list recent campaigns and check none covers the same stories. Re-check just before publishing.
3. **Gates on the source:** strict template compile with zero errors; every tracked link carries a complete, clean UTM set (no `amp;utm`); every article slug resolves to a live post; no image repeated in the issue.
4. **Create as a DRAFT, then preview.** Check the headline, every image, every call to action, no unresolved placeholders, and the opt-out footer. The Wix footer says "change your email preferences", not the word "unsubscribe", so check for the provider's actual wording before treating it as missing.

## Send and prove

5. Publish to the subscriber label.
6. Status runs IN_DETECTION (the provider's pre-send screening), then PUBLISHED / DISTRIBUTED. A publish call or "accepted" is not delivery.
7. **Delivered counts climb for several minutes.** Compare against the list's normal reach (GatorBait: about 1,810 per send). A send stuck far below that after an hour is an incident.
8. Record the campaign ID, the source file, the gate results and the delivered/opened/clicked/bounced counts in the event's log.

## Never

Send because an automation "should have" fired. Turn alert automations on or off to fix a missed send. Resend without delivery evidence that the first one failed.
