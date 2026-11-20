# Tool landscape (GitHub review)

**Reviewed: 2026-10-02.** Stars / last push are from the GitHub API on that date. Review depth: README, license, file tree and repo metadata. **No repository was installed or executed, and no source code was audited line by line** - do that before adopting anything in category A or B.

About 60 repositories surveyed across: Marketing API SDKs, MCP servers, CLIs, agent skills, Conversions API, ETL, reporting, Ad Library, fatigue detection, experimentation, MMM.

Not on GitHub but first in line: **Meta's own Ads MCP server and Ads CLI** (see `platform-state.md` §6).

## A. Use directly

| Repo | What | Stars · last push · license | Why / how | Limits and risks |
|---|---|---|---|---|
| [facebook/facebook-python-business-sdk](https://github.com/facebook/facebook-python-business-sdk) | Official Python SDK for the Marketing API and Conversions API | 1.6k · 2026-09-21 · Meta platform license | Generated from Meta's API spec, tracks each version. Use for the read-only pull job and for CAPI events. | Verbose, thin docs, 128 open issues. Custom license - fine for using Meta's API. |
| [facebook/facebook-nodejs-business-sdk](https://github.com/facebook/facebook-nodejs-business-sdk) | Official Node SDK | 620 · 2026-09-21 · same | Fits a Node pull script. | Heavy for edge/serverless runtimes; there, call the Graph API with plain `fetch`. |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Large agent-skill library; `ads`, `ad-creative`, `ab-testing` are relevant | 52k · 2026-10-01 · MIT | Plain markdown, no code to run. Read `ads/references/meta-decision-system.md`, `b2b-paid-playbook.md`, `audit-guardrails.md`, `ad-creative/references/hook-system.md`, `ab-testing/references/sample-size-guide.md` alongside this skill. | Its thresholds are one practitioner's; treat as `[PRACTICE]`. Don't install the whole pack - it would compete with this skill for triggering. |
| [growthbook/growthbook](https://github.com/growthbook/growthbook) | Experimentation + feature flags | 8.5k · 2026-10-02 · MIT core with enterprise dir | Landing-page A/B tests with proper statistics. | Only worth it once a landing page has real traffic. Self-hosting is an extra service. |

## B. Adapt

| Repo | What | Stars · last push · license | What to take | Limits and risks |
|---|---|---|---|---|
| [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | Multi-platform paid-media skill for Claude Code; read-only by default, writes behind approval/verify/rollback gates | 9.7k · 2026-09-25 · MIT | The governance design: evidence lineage per finding, `unknown` / `not_applicable` instead of guessed scores, cold-start contract (account vs pixel vs conversion maturity judged separately), draft-only mutations, a capability manifest. Its Meta control list (M01-M53) is a good audit checklist. | 12 platforms and a heavy JSON/validation control plane - far more than a single Meta account needs. Ships an installer script and Python; review before running. Tied to a paid community. |
| [EfrainTorres/armavita-meta-ads-mcp](https://github.com/EfrainTorres/armavita-meta-ads-mcp) | Self-hosted MCP, Marketing API v26, 125 tools, reviewable write plans, token redaction | 74 · 2026-09-16 · **AGPL-3.0** | Most current self-hosted option: change history, async reports, lead forms, CAPI. Candidate if Meta's own MCP proves unsuitable. | Release candidate. Needs a Rust toolchain to build. Browser login not supported on Windows (token env var instead). AGPL matters if you modify and offer it as a service. Small project - audit before trusting with a write token. |
| [brandu-mos/konquest-meta-ads-mcp](https://github.com/brandu-mos/konquest-meta-ads-mcp) | "Supervised" MCP: tools classed read-only / supervised / advisory, everything created paused, post-write verification, rollback references | 44 · 2026-04-23 · MIT | The safety-tier model and naming enforcement - mirror it in your write gate. | Open-core with a paid bundle; quiet since April; API version likely behind. |
| [gomarble-ai/facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server) | Simple Python MCP, mostly read/insights | 366 · 2026-08-05 · MIT | Small enough to read end to end; a base for a minimal read-only server with your own `ads_read` token. | Use only the manual-token path. The "one-click installer" obtains the token through GoMarble's server - don't. |
| [fivetran/dbt_facebook_ads](https://github.com/fivetran/dbt_facebook_ads) | dbt models for Facebook Ads reporting | 52 · 2026-08-18 · Apache-2.0 | Table design for account/campaign/ad set/ad/url daily reports - copy the schema ideas into your own database. | Assumes Fivetran's source schema and a warehouse. |
| [dlt-hub/verified-sources](https://github.com/dlt-hub/verified-sources) (`facebook_ads`) | Python loader for Marketing API → any database | 124 · 2026-07-03 · Apache-2.0 | Incremental insights loading with attribution-window re-pull already solved. | Python pipeline to host somewhere; for one account a 100-line script may be simpler. |
| [lsb11/shopify-capi-validator](https://github.com/lsb11/shopify-capi-validator) | Zero-dependency CLI that validates CAPI payloads locally | 3 · 2026-09-28 · MIT | Idea: validate your event payloads in CI before they reach Meta. | Tiny, ecommerce-shaped. Take the idea, not the code. |

## C. Learn from

| Repo | Lesson |
|---|---|
| [loganriebel/meta-ads-agent](https://github.com/loganriebel/meta-ads-agent) (5★, MIT) | Staged skills where each stage writes a file and ends in a human approval; a `learnings/` folder read by the next strategy stage; kill/scale rules in config; API payloads as paused drafts only. This skill's operating loop follows the same shape. Aimed at B2B trials/demos. |
| [the-baweja/ad-fatigue-detector](https://github.com/the-baweja/ad-fatigue-detector) (MIT) | Fatigue judged on 7-day rolling *trend* per ad, baselined against the account's own decay by format × funnel stage, with a cheapest-fix-first ladder. Its "template vs message fatigue" split is a useful hypothesis; its Andromeda claims are unverified. |
| [mikusnuz/meta-ads-mcp](https://github.com/mikusnuz/meta-ads-mcp) (82★, MIT) | Reference for how v26 endpoints map to tools (135 of them). Runs via `npx` from npm - supply-chain exposure, so reference only. |
| [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) (1.3k★) | Most-used community MCP; tool naming and "confirm every write, create paused" contract. **Business Source License 1.1** (not open source until 2029) and the product is steered toward their hosted service. |
| [facebookresearch/Ad-Library-API-Script-Repository](https://github.com/facebookresearch/Ad-Library-API-Script-Repository) (344★), [Paularossi/AdDownloader](https://github.com/Paularossi/AdDownloader) (GPL-3.0) | How the official Ad Library API works. It returns full data mainly for political/issue ads and EU-delivered ads, so it may not cover commercial competitors in your market; browse the Ad Library manually instead. |
| [googleads/google-ads-mcp](https://github.com/googleads/google-ads-mcp) (1k★, Apache-2.0) | Google's official MCP is read-only by design - the model for a safe analytics connector. |
| [facebookincubator/GeoLift](https://github.com/facebookincubator/GeoLift), [google/CausalImpact](https://github.com/google/CausalImpact) | Geo holdout and time-series methods for incrementality. For when spend is large enough to hold a region out. |
| [facebookexperimental/Robyn](https://github.com/facebookexperimental/Robyn), [google/meridian](https://github.com/google/meridian), [pymc-labs/pymc-marketing](https://github.com/pymc-labs/pymc-marketing) | Marketing mix modelling. Needs ~2 years of weekly multi-channel data. Not for small accounts. |
| [stape-io/facebook-tag](https://github.com/stape-io/facebook-tag), [facebookincubator/ConversionsAPI-Tag-for-GoogleTagManager](https://github.com/facebookincubator/ConversionsAPI-Tag-for-GoogleTagManager) | Field mapping and dedup logic for CAPI. If you send from your own backend instead of server-side GTM, but the mapping is the same. |
| [gabrielbarretodev/piperun-meta-capi-webhook](https://github.com/gabrielbarretodev/piperun-meta-capi-webhook) | A CRM-stage → CAPI webhook bridge; the same shape as the stage-3 service in `api-integration.md`. No license - read, don't copy. |
| [singer-io/tap-facebook](https://github.com/singer-io/tap-facebook), [airbytehq/airbyte](https://github.com/airbytehq/airbyte) | How mature connectors handle async insights jobs, lookback re-pulls and throttling. |

## D. Ignore

| Repo | Why |
|---|---|
| [irinabuht12-oss/google-ads-meta-ads-mcp](https://github.com/irinabuht12-oss/google-ads-meta-ads-mcp) and `irinabuht12-oss/marketing-skills` (3.3k / 2.9k★) | **No server code in the repo** - README, configs and a link to a hosted commercial connector (Ryze). Installing it routes ad-account access with write permission through a third party. Star counts are out of proportion to the content. The skills pack bundles the same connector. |
| Third-party hosted MCPs in general (Pipeboard hosted, Windsor, Composio, Coupler, Adspipe…) | Your token and client data pass through someone else's servers. Meta now offers a first-party server. |
| Ad Library *scrapers* (Selenium/Playwright/Apify repos) | Break Meta's terms, fragile, risk to the account. |
| [fredericharnois/facebook-ads-reporting-google-apps-script](https://github.com/fredericharnois/facebook-ads-reporting-google-apps-script) (179★) | Last updated 2022; API version long expired. |
| [maraujo/pySocialWatcher](https://github.com/maraujo/pySocialWatcher), [tophatter/facebook-ruby-ads-sdk](https://github.com/tophatter/facebook-ruby-ads-sdk), [google/lightweight_mmm](https://github.com/google/lightweight_mmm), [facebookresearch/Radlibrary](https://github.com/facebookresearch/Radlibrary) | Abandoned or archived. |
| The long tail of `meta-ads-agent` / `meta-ads-dashboard` repos with 0-2 stars | Personal experiments, no tests, no maintenance. |
| Framework-specific CAPI packages (Laravel, Magento, PrestaShop, Symfony) | Wrong stack. |

## Gaps found - things worth building yourself

1. **WhatsApp lead → CRM → Conversions API bridge.** Nothing reusable exists in the open for the click-to-WhatsApp path. Worth building if you sell through chat.
2. **Ad ↔ CRM join for a services business** (cost per qualified lead and CAC per ad). Open tools stop at Meta's own numbers.
3. **Creative tag analysis** (performance by angle / hook / format). Only commercial products do this well.
4. A **read-only daily monitor** that posts alerts to your chat or email.

## Review rule for any new repo

License → last commit → who maintains it → does it contain the code it claims → where do credentials go → what does it install or execute → read the code path that touches tokens and writes. Stars are not evidence.

## GitHub scan 2026-10-23 (deep-research, README-level, no code audited)

| Repo | Stars | Does | Safety | Use? |
|---|---|---|---|---|
| AgriciDaniel/claude-ads | ~10.3k | Audit/plan from exports; writes only behind full mutation gate | read-only default, no delete | Learn from: audit flow + mutation gate design |
| kostja94/marketing-skills (meta-ads SKILL.md) | ~1k | Playbook only | n/a | Skim for checklist |
| pipeboard-co/meta-ads-mcp | 1.3k | Read/write MCP, hosted or self-host | confirm every write, PAUSED default, no dry-run | Candidate self-host (own app) |
| attainmentlabs/meta-ads-mcp | 17 | 6 read + 7 write tools | PAUSED, dry_run default, confirm=True, budget cap env, JSONL audit | Best safety model; small, review code first |
| byadsco/meta-ads-mcp | 23 | 142 tools, v26.0, multi-tenant | quota guards only, not money | Skip for now |
| mathiaschu/meta-ads-analyzer | 454 | Analysis skill, wants write scopes, plaintext token | none | Ignore |
| Varnan-Tech/meta-ads-skill | 23 | Skill + self-hosted OAuth MCP, can write | prompt-only guardrail | Ignore |

Meta official Ads AI Connectors (open beta 2026-04-29): hosted MCP `mcp.facebook.com/ads`, Business OAuth, no app needed, writes from day one; CLI uses system-user token. Write-approval behaviour unverified.
Gap no repo fills: Conversions API for Business Messaging (`action_source=business_messaging`, `messaging_channel=whatsapp`, `ctwa_clid` from webhook referral; events LeadSubmitted/QualifiedLead/Purchase). Some unofficial WhatsApp libraries may not expose `ctwa_clid` - check yours.
Dev-mode app blocks creative creation via API (error subcode 1885183, seen 2026-10-23) - app must be Live to create ads.
