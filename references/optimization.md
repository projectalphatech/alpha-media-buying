# Optimization and scaling

All thresholds here are **starting defaults `[PRACTICE]`**, expressed relative to *your own* targets. Replace them with `[OBSERVED]` values as account history builds. None of them is a Meta rule.

Definitions: **tCPL** = target cost per lead, **tCPQL** = target cost per qualified lead (both from `scripts/unit_economics.py`).

## When NOT to touch (the default)

Leave it alone when any of these hold:
- The ad set is in learning and nothing is broken.
- Fewer than ~3 days since the last edit.
- Spend on the thing being judged is below ~2× tCPL (ad) or ~3× tCPQL (ad set).
- The "problem" is one bad day. Judge on 3-7 day windows.
- The newest cohort has not had time to qualify or close.
- It is working. Do not "improve" a profitable ad set by editing it; duplicate to test instead.

Every edit costs learning. The burden of proof is on the change.

## Kill / hold / scale an ad

| Evidence | Decision |
|---|---|
| Spent ≥ 2× tCPL, zero leads | Kill |
| Spent ≥ 3× tCPL, CPL > 2× target, link CTR in the bottom of the ad set | Kill |
| Leads cheap, but ≥ 10 leads with qualified rate far below the account's | Kill or rework the offer line; cheap unqualified leads are a cost |
| Mixed signals, spend < thresholds | Hold, no verdict |
| Meta gives it almost no spend after 5-7 days next to funded siblings | Treat as a loss in *this* ad set; retest the concept only with a reason |
| CPQL at or under target over ≥ 7 days and ≥ 5 qualified leads | Winner: keep, and make variations of its *concept* |

Pause rather than delete. Record the reason in the log.

## When to change what

| Symptom (sustained 5-7 days) | Change |
|---|---|
| Hook rate / CTR falling on the same ads, frequency rising | **Creative** - new concepts, not copy tweaks on the same visual |
| All creatives weak from day one, CPM normal | **Offer or message** before anything else |
| CPM high and pool small, frequency high early | **Audience** - widen, remove restrictions |
| Leads plentiful, unqualified | **Offer / qualifying friction / optimization event** |
| Several ad sets each short of learning | **Structure** - consolidate |
| Clicks fine, no conversions | **Destination** - page, opener message, response time |
| Qualified leads fine, no clients | **Not ads.** Sales process |

Change the layer the evidence points at, one layer at a time.

## Budget moves

| Situation | Move |
|---|---|
| CPQL ≤ target for 7+ days, lead→client holding, delivery stable | Raise budget. Default step 20-30%, then wait 3-4 days. Larger jumps are allowed when volume is strong; expect a few unstable days. |
| CPQL 1-1.5× target, trend flat | Hold. Work on creative. |
| CPQL > 1.5× target for 7+ days with enough spend | Cut 30-50% or pause; diagnose. |
| CAC over break-even on a mature cohort | Stop scaling regardless of how the ad metrics look. |
| Sales capacity is full (nobody can follow up fast enough) | Hold budget. Unanswered leads are wasted spend. |

Raising budget usually raises CPM and marginal cost. Scale is judged on **marginal** CPQL (cost of the extra leads), not the average.

## Scaling paths

1. **Vertical** - more budget on what works. Simplest; watch marginal cost.
2. **Creative** - more winning *concepts*. At small scale this is the main lever: new concepts reach new people inside the same broad audience.
3. **Horizontal** - new offer, product line, or geography in its own ad set with its own economics.
4. **Funnel** - raise lead→client rate (better opener, faster reply, stronger sample or demo). Doubling close rate halves CAC without touching ads; usually the cheapest win.
5. **Consolidation** - merge ad sets that each lack volume; move winners into one funded ad set.

## Fatigue

Detect on **trend per ad**, not on a snapshot: over a rolling 7 days, hook rate and CTR falling while frequency and cost per result rise, with no account-wide cause.

Response ladder, cheapest first: confirm it isn't tracking or seasonality → check sibling ads → new hook on the same idea → new visual concept → retire.

`[HYPOTHESIS]` from practitioner writing: changing only the copy on the same visual does not refresh delivery. Test it in your account before treating it as true.

## Change log discipline

Every change is logged before it is made: date, object, what changed, why, the metric expected to move, and the review date. Without the log, diagnosis two weeks later is guesswork.
