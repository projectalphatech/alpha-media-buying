# Measurement and analytics

## The signal loop

```
Ad click ──► WhatsApp / form / site ──► CRM row (lead ID, click ID, UTM, ad ID)
                                             │
                    stage changes: qualified → next steps → paid
                                             │
                     Conversions API  ◄──────┘   (Meta learns who is valuable)
```

Two things must be true before spend scales:
1. **Every lead row carries its origin**: campaign, ad set, ad ID, and a click identifier (`leadgen_id` for forms, WhatsApp click ID for CTWA, `fbclid`/`_fbc` for web).
2. **Every stage change is sent back** to Meta within 7 days of happening.

Without (1) we cannot say which ad produced a customer. Without (2) Meta optimizes for whoever taps.

## Tracking checklist

| Item | Check |
|---|---|
| Pixel on site, standard events (`PageView`, `Lead`, `Contact`) | Events Manager shows them, no duplicates |
| Conversions API from the server (a small serverless function or backend is a natural host) | Same events, same `event_id` as the browser for dedup |
| Event match quality | Send hashed phone + email + `fbc`/`fbp` + IP + user agent where consent allows |
| Domain verified | Business settings |
| UTMs on every ad | `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.id}}&utm_content={{ad.id}}` |
| CRM stores ad ID + click ID per lead | Query a recent lead and confirm |
| CRM stage events reach Meta | Test event visible in the dataset |
| Phone numbers hashed (SHA-256, normalized, with country code) before sending | Never send raw PII |

## Metric map

Read top to bottom; each row explains the one below it.

| Layer | Metric | Formula | What it tells you | Does *not* tell you |
|---|---|---|---|---|
| Auction | CPM | spend ÷ impressions × 1000 | price of attention: competition, audience, creative quality | whether anyone cares |
| Auction | Reach, Frequency | impressions ÷ reach | how concentrated delivery is | fatigue by itself |
| Creative | Hook rate | 3s video views ÷ impressions | does the opening stop the scroll | intent |
| Creative | Hold rate | ThruPlays ÷ 3s views | does the body keep attention | intent |
| Creative | CTR (link) | link clicks ÷ impressions | does the message earn a click | lead quality |
| Traffic | CPC (link) | spend ÷ link clicks | CPM ÷ CTR - a consequence, not a lever | |
| Traffic | Landing page views ÷ link clicks | | page speed / accidental clicks | |
| Conversion | Conversations or leads | | top-of-funnel volume | value |
| Conversion | CPL | spend ÷ leads | price of a raw lead | whether it is a good price |
| **Quality** | **Qualified rate** | qualified ÷ leads (CRM) | targeting + message honesty | |
| **Quality** | **Cost per qualified lead** | spend ÷ qualified | **primary working metric** | |
| **Business** | Lead → customer rate | customers ÷ leads (cohort) | funnel health | |
| **Business** | **CAC** | all acquisition cost ÷ new customers | **the verdict** | |
| Business | Revenue per customer, gross profit | | what a customer is worth | |
| Business | ROAS (CRM revenue ÷ spend) | | return on ad spend, cash basis | margin |
| Business | MER | total revenue ÷ total marketing spend | blended truth across channels | which channel did it |
| Business | LTV, payback period | | how much CAC you can afford | |

Use **link** CTR and **link** CPC, never the "all" variants.

## Reading rules

1. **Start from the business row and walk up.** CAC bad → which arrow broke? Lead→customer, qualified rate, CPL, CTR, CPM. Fix the first broken arrow.
2. **Never judge one metric alone.** Low CPL with low qualified rate is worse than high CPL with high qualified rate. Compute cost per qualified lead.
3. **Cohort, don't snapshot.** Customers closed this week came from leads of earlier weeks. Tie outcomes to the week the lead arrived. Recent weeks always look worse than they are (conversion lag); mark them "immature".
4. **Small numbers lie.** With 3 customers vs 5, the difference is noise. State counts, not just rates. Give a range when n is small.
5. **CPM moves for reasons outside the ad**: seasonality, auctions, audience size, a frequency climb. Check before blaming creative.
6. **Frequency is context, not a threshold.** Rising frequency + falling CTR + rising cost per result over the same days is the pattern worth acting on. Any single number ("frequency above 3") is `[PRACTICE]` at best.
7. **Attribution setting and definition changes break history.** See the dates in `platform-state.md` §4.
8. **Platform numbers are Meta's claim.** Reconcile leads in Ads Manager against leads in the CRM every week; a persistent gap is a tracking bug.

## Diagnostic table

| Pattern | Likely cause | Alternatives to rule out | First move |
|---|---|---|---|
| CPM high, CTR normal | expensive audience / season / small pool | recent edit, restrictive targeting | check audience size, placements, dates |
| CTR low, CPM normal | hook or offer not landing | wrong audience for this message | new concept, not a tweak |
| CTR high, few leads | curiosity click, weak page or opener | slow page, broken form, mismatch between ad and destination | check destination before touching ads |
| Many leads, low qualified rate | offer attracts freebie seekers; event too shallow | form too easy, wrong geo | tighten offer/qualifying question; feed quality back |
| Qualified fine, few customers | sales process, pricing, offer quality, follow-up speed | too early to tell (lag) | this is not an ads problem; fix the funnel |
| Was good, now decaying | creative fatigue, saturation | seasonality, competitor, tracking break, an edit | compare by ad and by day; check change log |
| Spend not delivering | learning limited, cap too tight, policy, audience too small | payment issue | check delivery status and account quality |

## Incrementality

Meta's attributed number is not the number of customers ads *caused*. At small scale formal lift tests are underpowered, so use cheap checks:
- **CRM question**: ask every new lead how they found you; compare with attributed source.
- **Blended view**: when spend goes up or down, does total qualified-lead volume move with it?
- **Holdout by time or geo** when budget allows: pause one region or one week and compare.
- MMM (Robyn, Meridian, PyMC-Marketing) needs years of multi-channel data. Not for small accounts.
