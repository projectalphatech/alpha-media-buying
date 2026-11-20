# Operating system

## The loop

```
Research → Strategy → Creation → Launch → Monitoring → Analysis → Testing → Optimization → Scaling → Reporting
    ▲                                                                                              │
    └──────────────────────────── learnings log ◄──────────────────────────────────────────────────┘
```

Each stage produces a written artifact. The next stage reads it. A campaign is a chain of files, not a chain of chats.

| # | Stage | Input | Output (artifact) | Gate to pass |
|---|---|---|---|---|
| 1 | Research | customer conversations, CRM, Ad Library, past learnings | `research.md`: customer language, pains, objections, competitor patterns | at least 3 distinct angles grounded in real quotes |
| 2 | Strategy | research, unit economics | `strategy.md`: offer, funnel, optimization event, structure, budget, max CPL / CPQL / CAC | economics computed, owner approves |
| 3 | Creation | strategy | creative briefs + copy, naming + tags, test cards | each ad maps to an angle and a hypothesis |
| 4 | Launch | briefs, assets | pre-launch checklist signed, change-log entry | tracking verified end to end with a test lead |
| 5 | Monitoring | daily pull | pacing + anomaly notes | only break-fix edits in the first days |
| 6 | Analysis | ad data + CRM join | weekly report (format below) | counts stated, cohorts mature enough |
| 7 | Testing | analysis | test cards with pre-written decision rules | one variable |
| 8 | Optimization | test results | drafted changes with reasons | explicit approval per change |
| 9 | Scaling | stable CPQL ≤ target, capacity to serve | budget / creative / market expansion plan | CAC on mature cohort under break-even |
| 10 | Reporting | all of the above | report + learnings-log lines | filed |

## Pre-launch checklist

- [ ] Unit economics written; max CPL and CPQL known
- [ ] Pixel + CAPI events firing, deduplicated; test event seen in Events Manager
- [ ] A test lead travels the whole path and lands in the CRM with ad ID and click ID
- [ ] CRM stage events reach Meta
- [ ] UTMs on every ad
- [ ] Naming convention and creative tags applied
- [ ] Existing customers and open leads excluded
- [ ] Reply path ready: new leads get a first reply within minutes, handoff rules clear
- [ ] Kill / hold / scale thresholds written for this campaign
- [ ] Budget, billing method and tax checked
- [ ] Ads comply with policy (no personal-attribute claims, no misleading promises)
- [ ] Change-log entry created; first review date set

## Cadence

| When | Do | Don't |
|---|---|---|
| Daily (5 min) | spend pacing, delivery errors, rejected ads, unanswered leads | edit on one day of data |
| Twice a week | per-ad view against kill thresholds | restructure |
| Weekly | full report, CRM reconciliation, decide tests | declare winners on thin data |
| Monthly | cohort CAC, lead→client rates, update unit economics, creative-tag analysis, refresh `platform-state.md` | |
| Quarterly | offer and market review, tool review, incrementality check | |

## Report template

```
REPORT - <account> - <date range> - attribution: <setting> - data pulled: <date>

PERFORMANCE
  Spend | Leads | CPL | Qualified | CPQL | Customers | CAC   (with counts, vs previous period, vs target)
  Cohort note: weeks still immature: ...

DIAGNOSIS
  Seeing:        ...
  Likely means:  ...
  Evidence:      ...
  Alternatives:  ...

PRIORITY
  The one thing that matters most right now.

ACTIONS
  1. <change> - reason - expected effect - watch <metric> - review on <date>

DON'T TOUCH
  <thing> - working, or not enough evidence to judge (state which)

NEXT TEST
  Hypothesis → Variable → Control → Test → Success metric → Window → Decision rule

SUCCESS CRITERIA
  The result that would validate the action, as a number and a date.

CONFIDENCE & GAPS
  What we could not see; which claims are [OBSERVED] vs [HYPOTHESIS].
```

Keep it to one screen. Numbers before narrative. If the data is too thin for a verdict, the report says so and names what is needed.

## Files the system keeps (per account)

```
<account>/
  economics.md       unit economics, targets
  research.md
  strategy.md
  creative-log.csv   ad → offer/angle/concept/format/hook tags
  tests/T-YYYY-NNN.md
  changes.md         every edit, with reason and review date
  learnings.md       one line per concluded test
  reports/YYYY-MM-DD.md
```

## Skill changelog

One dated line per change to this skill, newest last.

- 2026-11-20 - Public release.
