# alpha-media-buying

A skill that makes your AI agent run Meta (Facebook / Instagram / WhatsApp) ads like a careful senior media buyer.

## What it does

1. **Judges ads by paying customers.** It joins ad data to your CRM and ranks by cost per qualified lead, cost per paying customer and CAC. CPL, CTR and CPC are diagnostics, never the verdict.
2. **Tags every claim** as `[OFFICIAL]` (Meta docs), `[OBSERVED]` (your own data), `[PRACTICE]` (practitioner convention) or `[HYPOTHESIS]`, so you can see what is fact and what is folklore.
3. **Never touches a live ad account without your approval** for that specific change. Drafts first, new objects created PAUSED, one approval per change.
4. **No verdict without enough data.** It states the sample size, treats "not enough data yet" as a valid answer, and will not kill a working ad over a couple of bad days.

It also covers one-variable test design, a fixed reasoning and report format, kill/hold/scale rules, measurement (Pixel, Conversions API, click-to-WhatsApp signal loop), creative testing, Marketing API / MCP access, a tool landscape, organic-to-paid boosting, and a unit-economics calculator (`scripts/unit_economics.py`).

## Install

**Claude Code**

```
git clone https://github.com/projectalphatech/alpha-media-buying ~/.claude/skills/alpha-media-buying
```

**Codex, Cursor, Gemini CLI and other agents**

Clone the repo anywhere, then either point the agent at `SKILL.md`, or copy it to `AGENTS.md` (or your tool's rules file) at your project root. Keep the `references/` and `scripts/` folders next to it; `SKILL.md` links to them.

## First prompts to try

- "Fill in `references/strategy.md` with me: my offer, price, margin and funnel stages."
- "Here is my Ads Manager export and my CRM leads. Which ads bring paying customers, and which only bring cheap leads?"
- "Run `scripts/unit_economics.py` for me and tell me my break-even CPL and target CAC."
- "Audit my Pixel / Conversions API setup against the signal loop in the skill."
- "Design one test for my next creative round, with the decision rule written before launch."

## Safety

Read-only by default. The skill asks for approval before every write to an ad account (create, edit, pause, budget, delete). Give it a token that cannot write (`ads_read`) until you trust the setup. Keep tokens in a local `.env` or CI secrets, never in chat or commits. `references/platform-state.md` is dated; the agent is told to re-verify it when it is older than about 30 days.

## License

MIT. See `LICENSE`.

---
Published by Project Alpha Tech.
