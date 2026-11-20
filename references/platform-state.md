# Meta platform state

**Researched: 2026-10-02.** Re-verify anything here before relying on it if this date is more than ~30 days old.

Confidence column: **A** = read on a Meta page during research · **B** = several independent secondary sources agree, Meta page not read · **C** = single secondary source or vendor claim.

Meta now publishes machine-readable docs. Start verification here:
`https://developers.facebook.com/documentation/ads-commerce/llms.txt` (index of `.md` pages that fetch cleanly).
Version table: `https://developers.facebook.com/docs/graph-api/changelog`.
Out-of-cycle changes: `https://developers.facebook.com/docs/marketing-api/out-of-cycle-changes/occ-2026`.

## 1. API versions

| Fact | Conf. |
|---|---|
| Latest Graph + Marketing API is **v26.0**, released 2026-07-29 | A |
| v25.0 released 2026-02-18 | A |
| Marketing API **v24.0 sunsets 2026-10-06** - do not build on it | A |
| v26 reportedly: special-ad-category ad sets must set `targeting_automation.advantage_audience` explicitly; Instagram Explore Feed placement request errors; `country`/`location_spec` in `lookalike_spec` ignored; `is_adset_budget_sharing_enabled` required when creating a campaign without a campaign budget; some of these apply to all versions from 2026-10-27 | **C** - the v26 changelog page could not be read; an open-source maintainer flagged the same claims as unverified. Check the changelog before coding against these. |
| Messenger Stories placement removed across API versions (Aug 2026) | B |

## 2. Campaign structure: Advantage+ is the default

| Fact | Conf. |
|---|---|
| Legacy Advantage+ Shopping (ASC) and Advantage+ App (AAC) APIs are deprecated. From v25 they cannot be created; by v26 un-migrated legacy campaigns are paused and blocked from edits. | A |
| A campaign's automation level is exposed as `advantage_state`: `ADVANTAGE_PLUS_SALES`, `ADVANTAGE_PLUS_APP`, `ADVANTAGE_PLUS_LEADS`, or `DISABLED`. | A |
| It is Advantage+ only when **all three** levers are on: **budget** at campaign level (`advantage_budget_state`), **audience** via `targeting_automation.advantage_audience = 1` or geo-only targeting (`advantage_audience_state`), **placements** with no placement targeting or exclusions (`advantage_placement_state`). | A |
| Allowed bid strategies: `LOWEST_COST_WITHOUT_CAP` (Meta's recommended), `COST_CAP`, `LOWEST_COST_WITH_BID_CAP`, `LOWEST_COST_WITH_MIN_ROAS`. | A |
| **Leads campaigns have the same Advantage+ structure** (`ADVANTAGE_PLUS_LEADS`). This is the one relevant to lead-generation businesses. | A |
| Ads Manager merged the manual and Advantage+ creation flows into one. | B |
| Meta is testing removal of placement exclusions at ad-set level for Sales/Leads (in-product notice, Aug 2026). | C |

Meaning: "manual vs Advantage+" is no longer a campaign type, it is three switches. Turning any one off is a deliberate choice that should be justified by data.

## 3. Delivery system (Andromeda / GEM)

| Fact | Conf. |
|---|---|
| Meta describes Andromeda as its ads *retrieval* system and GEM as a large ranking foundation model (Meta engineering posts, 2024-2025). | B |
| Practitioner consensus: fewer ad sets + more *conceptually distinct* creatives beats fragmented structures; near-duplicate creatives are treated as one asset. | B, `[PRACTICE]` |
| Specific numbers in circulation ("10-15 concepts per campaign", "25 creatives beat 5 ad sets by 17%", "ad lifespan fell from ~80 to ~7 days") | **C** - vendor/blog claims. Treat as hypotheses to test, never as rules. |
| Ads Manager now surfaces a creative-diversity indicator (Help Center, Aug 2026). | B |

## 4. Attribution and measurement

| Fact | Conf. |
|---|---|
| 2026-01-12: 7-day-view and 28-day-view windows removed from the Insights API. Reported conversions dropped with no real change. | B |
| 2026-03-03: **click-through attribution now requires a real link click.** Likes, shares, saves, profile taps no longer count as clicks. | B |
| Former "engaged-view" is now **engage-through**: non-link engagement or a ≥5-second video view (was 10s), fixed 1-day window. | B |
| Default attribution setting for website conversions: 7-day click, 1-day engage-through, 1-day view. | B |
| **Incremental attribution** exists as an ad-set attribution setting (model-estimated incremental conversions; website conversions, maximize conversions/value). Availability varies. | B |
| Insights breakdowns `impression_device`, `hourly_stats_aggregated_by_audience_time_zone`, `frequency_value` require opt-in from 2026-08-06; without it non-managed accounts may get **empty results silently**. | A |
| `breakdowns=dma` replaced by `comscore_market` (US only). | A |

Rules that follow:
- Any comparison across **Jan 12** or **Mar 3, 2026** is not like-for-like. Say so in the report.
- Always state the attribution setting next to a conversion number.
- Platform-reported conversions are a *claim*. The CRM is the ledger.

## 5. Lead generation and WhatsApp (lead-gen lane)

| Fact | Conf. |
|---|---|
| **Conversion Leads** optimization: send CRM stage changes back through the Conversions API so delivery optimizes for leads that progress, not for form fills. | A |
| CRM event payload: `event_name` = your stage name (send every stage, in order), `event_time` unix seconds (max 7 days old), `action_source: "system_generated"`, `custom_data.event_source: "crm"`, `custom_data.lead_event_source: "<CRM name>"`, `user_data.lead_id` = the 15-17 digit `leadgen_id` (or click ID / hashed email / hashed phone). | A |
| Click-to-WhatsApp: Meta attaches a click ID (`ctwa_clid`) to the first inbound message; sending it back with Lead/Purchase events through the Conversions API for business messaging lets Meta optimize beyond "conversation started". | B - Meta's business-messaging page 404'd during research; mechanism described consistently by BSPs. Verify payload fields against Meta docs before building. |
| "Lead Capture" AI agent for Instant Forms announced (Jul 2026). | C |
| WhatsApp marketing messages available in the Marketing API (Aug 2026). | B |

## 6. AI tooling from Meta itself

| Fact | Conf. |
|---|---|
| **Official Ads MCP server** at `https://mcp.facebook.com/ads`. Categories: reporting, campaign/ad set/ad create + edit, catalogs, signal health, Help Center search, A/B tests and lift studies, activity log. | A |
| Auth: Facebook Login for Business (OAuth) or a user access token as `Authorization: Bearer`. Scopes requested: `ads_mcp_management, ads_read, ads_management, catalog_management, business_management, pages_show_list, instagram_basic`. | A |
| Claude Code: `claude mcp add --transport http --client-id <META_APP_ID> meta-ads https://mcp.facebook.com/ads` | A |
| **It is read *and* write.** The pages read do not document a read-only switch. | A (absence noted) |
| **Official Ads CLI**: `meta ads <resource> <action>`; authenticates with a **system user access token**; resources include campaigns, ad sets, ads, creatives, insights, datasets, accounts, pages; output `table` / `json` / `plain`; `--no-input` and `--force` suppress prompts. | A |
| "Granular security controls for AI connectors" help page (Aug 2026); Meta AI in Ads Manager can analyse campaigns (Aug 2026). | C |

## 7. Rate limits

| Fact | Conf. |
|---|---|
| Development tier: 60-point ceiling, 300s decay, 300s block. Standard tier: 9,000 points, 60s block; requires 500+ calls in 15 days with <15% errors. Read = 1 point, write = 3. | A |
| Per-account hourly quota: insights 600 (dev) / 190,000 (standard) + 400 × active ads; management 300 / 100,000 + 40 × active ads. | A |
| Headers: `X-Ad-Account-Usage`, `X-Business-Use-Case-Usage`, `X-FB-Ads-Insights-Throttle`. Errors: 17, 613, 4, 80000-80014. Back off using the header reset time. | A |

## 8. Learning phase

| Fact | Conf. |
|---|---|
| Ad sets exit learning after roughly **50 optimization events in 7 days**; significant edits restart it. | B - Meta's help page would not render; long-standing and widely cited. |
| "Advantage+ threshold lowered to 25 conversions/week (Apr 2026)" | **C** - one blog. Do not rely on it. |
| "Never raise budget more than 20% at a time" | `[PRACTICE]` - not a Meta rule. Meta says only that large budget changes can be significant edits. |

Why it matters: a business that closes a handful of customers a month will rarely reach 50 *customer* events a week, so the optimization event must sit higher in the funnel and quality must be fed back as signal. See `strategy.md`.

## 9. Billing notes

| Fact | Conf. |
|---|---|
| From 2026-07-01 Meta adds "location fees" where ads are *delivered* (UK 2%; FR/IT/ES 3%; AT/TR 5%). Check whether your delivery countries are listed. | B |
| Advertisers in many countries are charged VAT or similar tax on ad spend; the rate can depend on tax registration on the account. | **C** - sources are old and inconsistent. Confirm on an actual invoice and with your accountant; count it in CAC either way. |

## Still to verify (do this before it matters)

- [ ] v26 breaking-change list, read on Meta's own changelog
- [ ] Business-messaging Conversions API payload for WhatsApp
- [ ] Whether the official MCP/connector offers per-tool or read-only controls
- [ ] Current learning-phase wording on Meta's help page
- [ ] Your real invoice: tax rate, currency, payment method

## 7. Targeting controls (researched 2026-10-23)

| Fact | Conf. |
|---|---|
| Under Advantage+ audience, hard controls are only: location, minimum age (18-25 max), custom-audience exclusions, language. Age max, gender, detailed targeting, lookalikes are suggestions. | B (Jon Loomer 2026-03-24 + others; Meta page not read) |
| A minimum age above 25 (e.g. 35) is enforced only after switching to original audience options (Advantage+ audience off) and leaving "reach beyond" unticked. | B |
| Detailed-targeting *exclusions* removed (Mar 2025). Detailed targeting itself is a suggestion for most goals even with Advantage+ off. | B |
| Location is always "living in or recently in"; residents and visitors cannot be separated. City/region targeting has a "reach more people likely to respond" box that can deliver outside the area - untick it. | B |
| **To check in your own Ads Manager:** whether "Switch to original audience options" still exists; what the minimum-age Control caps at; whether "Include people of unknown age on WhatsApp" is ticked by default and widens reach past the age floor; whether manual placements are still available for your ad set. Record what you see with the date as `[OBSERVED]`. | - |

## 2026-11-15 check (CTWA setup, vendor sources only — confirm in UI)
- Click-to-message ads: Message Template section holds the greeting text + either a pre-filled message or ice breakers. Sources disagree on whether both can coexist `[PRACTICE, conflicting]` — check the UI when building.
- Welcome Message Sequence (text + pre-fill + FAQs) attachable to CTWA ads; the old greeting option was removed from conversational components in March 2026 `[PRACTICE, vendor]`.
- Free entry-point window reportedly up to 7 days after a reply since 2026-10-01 `[PRACTICE, single vendor — verify on Meta pricing page]`.

## Performance goals for WhatsApp ads (to check in your account)
- Which performance goals does each objective offer with a WhatsApp-only destination (for example Conversations, "Maximize number of leads through messaging", Link clicks)? Vendors report that the list differs by objective and by manual vs automatic destination `[PRACTICE]`. Check in Ads Manager, record the date, and note that the performance goal on a live ad set is generally locked.
- What Meta counts as a "lead" for a messaging goal is not always shown. Do not assume it matches your qualified-lead definition; verify with CRM data.
