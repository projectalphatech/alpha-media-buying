# Strategy (template)

Fill this in with the user before designing any campaign. Keep the filled copy per account (see `operating-system.md`, "Files the system keeps"). Until real numbers exist, mark every rate `[HYPOTHESIS]` and replace it with `[OBSERVED]` after roughly 30 leads per stage.

## 1. Your business

| Field | Your answer |
|---|---|
| Offer (what you sell, in one sentence) | |
| Price / average first-order revenue | |
| Gross margin (after delivery cost) | |
| Sales cycle (days from lead to payment) | |
| Where the sale happens (chat, call, site, store) | |
| Capacity: how many new customers you can serve per month | |
| Repeat / retainer value (optional, for LTV) | |

Write down the implication: few large conversions or many small ones? Is the sale made in conversation? Will lead quality vary a lot? A cheap lead who wanted something free is a cost, not an asset.

## 2. Funnel stages

Name your own stages and the CRM event for each. Example shape:

```
Ad (hook + offer)
  -> conversation / form / landing page
    -> qualified (real need, budget signal)
      -> intermediate step (demo, quote, sample, trial) - optional
        -> paid customer
```

| Stage | CRM event name | Rate to next stage | Cost of this stage to you |
|---|---|---|---|
| Lead | | | |
| Qualified | | | |
| (optional step) | | | |
| Paid customer | | | |

Each arrow is a measured rate. A problem is always located at one arrow before anything is changed. If you give something away before the sale (a sample, an audit, a trial), its cost belongs in CAC.

## 3. Unit economics

Compute with `scripts/unit_economics.py` and write the outputs here: gross profit per customer, break-even CAC, target CAC, max CPL, max cost per qualified lead.

## 4. Choosing the destination

| Destination | For | Against |
|---|---|---|
| **Click-to-WhatsApp (or Messenger/DM)** | Businesses that sell in conversation; low friction where chat is the norm; instant reply possible | Low-intent taps; attribution needs the click ID captured |
| **Instant Form** | Cheap leads, fields give qualification data, `leadgen_id` makes Conversion Leads straightforward | Lowest intent; needs fast follow-up |
| **Website (landing page)** | Highest intent, Pixel + CAPI events, page pre-qualifies | Highest friction, fewer leads, page must be good |

Default starting position `[HYPOTHESIS]`: pick the destination that matches where you already close sales, with one other lane as a quality comparison. Decide by cost per **qualified** lead, not cost per conversation.

## 5. Choosing the optimization event

Constraint: delivery needs a steady flow of the chosen event (roughly 50/week per ad set is the commonly cited figure `[PRACTICE]`). Paying customers will often never reach that.

| Stage | Volume | Quality signal | Use as |
|---|---|---|---|
| Conversation started / form submitted | high | weak | optimization event at launch |
| Qualified lead | medium | good | send back as a CRM/CAPI event from day one; switch optimization to it once volume supports it |
| Intermediate step | low-medium | strong | CAPI event, reporting, audience seed |
| Paid customer | very low | strongest | CAPI event with value; reporting and seeds, rarely the optimization event at small scale |

Principle: **optimize on the deepest event that still has enough volume, and feed every deeper stage back as signal.**

## 6. Campaign architecture

Start consolidated. Structure is earned by data, not assumed.

```
Campaign 1 - Leads, prospecting (campaign budget)
  Ad set: your geo, broad, Advantage+ audience, all placements
    Ads: 4-8 conceptually different creatives (see testing-and-creative.md)

Campaign 2 - Retargeting (only once audiences are large enough)
  Ad set: engaged / visited / messaged, excluding customers
    Ads: proof, objections, deadline
```

- One prospecting ad set per genuinely different **offer or market**, not per interest.
- Split by product line only when offers, creatives and economics differ enough to need separate budgets.
- Exclude existing customers and current open leads from prospecting.
- Audience suggestions (job titles, industries, interests) are hints to Advantage+ audience, not fences. Hard restrictions only for geography, age floor, language where needed.
- Do not build retargeting before the pools exist; a 2,000-person audience on a daily budget just buys frequency. Gates and budgets for warm audiences: `organic-to-paid.md`.

## 7. Budget

- Budget must be able to produce a learnable number of the optimization event. Rough check: `daily budget x 7 / expected cost per optimization event`. If far below ~50, move the event up the funnel, consolidate ad sets, or accept slow learning and judge on longer windows.
- Decide the **test budget** in advance as a number of *qualified leads* you are buying information with, not a number of days.
- Spend counts tax and fees. CAC = (ad spend + tax + cost of any free step + human sales time) / new customers.

## 8. Prospecting vs retargeting vs client work

| Lane | Job | Judge by |
|---|---|---|
| Prospecting | find new people with the problem | cost per qualified lead, lead-to-customer rate |
| Retargeting | finish conversations already started | incremental closes, frequency |
| Client accounts (if you run ads for others) | same system, the client's economics | the client's own paying-customer metric |

For client accounts, use the client's unit economics and get their written approval for spend changes.
