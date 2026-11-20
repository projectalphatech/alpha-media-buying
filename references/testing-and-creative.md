# Testing and creative intelligence

## Test card (required for every test)

```
ID:            T-2026-001
Hypothesis:    Because <evidence>, we believe <change> will improve <metric> for <audience>.
Variable:      the ONE thing that differs
Control:       what runs today
Test:          the variant(s)
Success metric: primary = cost per qualified lead (or the stated one); guardrail = qualified rate
Minimum evidence: spend ≥ __ and ≥ __ qualified leads per arm
Evaluation window: __ days, plus __ days for leads to qualify
Decision rule: written BEFORE launch - what result means adopt / reject / inconclusive
Result:        numbers, counts, date range
Decision:      adopt / reject / inconclusive -> next step
Learning:      one sentence, filed in the learnings log
```

Rules:
- Decision rule is written before launch. No moving the goalposts.
- "Inconclusive" is a legitimate result. Most small-budget tests end there; say so instead of crowning a winner.
- A difference between two arms with a handful of conversions each is noise. As a rough guide, with fewer than ~20-30 primary conversions per arm, only very large differences (2× or more) mean anything.
- A result is a claim about *this* account, offer and time. Mark it `[OBSERVED]` with the date.

## How to run a test on Meta

| Method | Use when | Note |
|---|---|---|
| Several creatives in one ad set | routine creative exploration | Meta allocates spend unevenly; this finds what *Meta prefers*, not a fair comparison. Good enough for exploration. |
| Meta A/B test (Experiments) | a decision that matters: offer, destination, optimization event, structure | splits the audience cleanly; costs more budget |
| Before/after | only when a split is impossible | weakest; confounded by time. State that. |

## What to test, in order of leverage

For a business with low volume, the order usually is:

1. **Offer** - what you promise and what the next step is (free sample vs audit vs price-led vs case study)
2. **Angle / concept** - which problem we lead with
3. **Hook** - first 1-3 seconds or the headline line
4. **Format** - talking-head video, screen demo, before/after, static, carousel
5. **Destination** - WhatsApp vs form vs landing page
6. **Optimization event**
7. Audience, placement, budget, structure - usually last; automation handles much of this now

Copy tweaks and button colours are not worth budget at low volume.

## Creative system

Work in a hierarchy so results accumulate into knowledge:

```
Offer  →  Angle (problem/desire)  →  Concept (the idea of the ad)  →  Hook variants  →  Format/edit
```

Name every ad so it can be analysed later:
`{offer}_{angle}_{concept}_{format}_{hook#}_{YYMMDD}` e.g. `freesample_slowreply_chatdemo_vid_h2_261005`

Tag each ad in the creative log with: offer, angle, concept, format, hook type, length, language/dialect, presenter, proof used, CTA. Analysis is then by **tag**, not by ad: "which angle wins" survives long after individual ads die.

### Angles to explore (`[HYPOTHESIS]` until tested)

Build your own list from real customer language. Neutral starting set:

| Angle | Lead idea |
|---|---|
| Pain | the problem your offer removes, in the customer's words |
| Cost of doing nothing | what the current situation costs per month |
| See it first | a sample, demo or preview before they commit |
| Speed | result in days, not months |
| Proof | a real customer's before/after |
| Simplicity | how little effort it takes the customer |
| Risk reversal | guarantee, trial or easy exit |

Different angles reach different people. Variations of one angle mostly do not.

### Reviewing a creative

| Element | Question |
|---|---|
| First 1-3 seconds | Does it name the viewer's problem or show something they have not seen? Understandable with sound off? |
| Visual pattern | Does it look native to Reels/Feed or like an advert? |
| Problem → solution | Is the problem theirs, in their words? |
| Offer | Clear what they get and what it costs them to ask? |
| Proof | Real result, real name, real screen? |
| Demonstration | Do we show the thing working? |
| CTA | One action, matching the destination |
| Copy | First line carries the hook; the audience's own language and dialect |
| Length / edit | Earns its length; captions burned in |
| Branding | Present, not leading |
| Placement fit | 9:16 for Reels/Stories, 4:5 or 1:1 for Feed; safe zones clear |

### Reading creative data

| Signal | Reading |
|---|---|
| Low hook rate | opening fails; nothing after it was seen |
| Good hook, low hold | promise in the hook is not paid off |
| Good hold, low CTR | interesting, but no reason to act: offer/CTA |
| High CTR, low qualified rate | attracts the wrong people or over-promises |
| High CTR, good qualified rate | scale the concept; make siblings |

## Research before creative

1. **Customer language**: read real conversations with leads (chat history, call notes, reviews). Pain points, objections and exact phrases come from there, not from brainstorming.
2. **Competitors**: Meta Ad Library (`facebook.com/ads/library`) for competitors in your market. Note what has been running longest; long-running usually means working. Record offer, angle, format, hook. The Ad Library API returns full data mainly for political/social-issue ads and EU delivery; for commercial ads outside those categories, browse manually.
3. **Patterns, not copies**: collect patterns across many ads; never reproduce a competitor's ad.
4. **Objections**: price, trust, "I have a nephew who does websites", time, fear of tech. Each is an angle for retargeting.

## Learnings log

One line per concluded test:
`date | test ID | what we learned | evidence (n, spend) | confidence | applies to`

Read the log before planning any new campaign. It is the memory of the system.
