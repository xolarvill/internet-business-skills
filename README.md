# internet-business-skills

This repository is a pack of commercial analysis skills designed for Codex and Claude Code. Every skill follows one rule: research must be narrow and fact-based.

- Keep claims proportional to publicly visible evidence.
- Distinguish evidence collection from business judgment.
- When a request is too broad, ask one clarification at a time, then proceed.

## Installation

### Codex plugin

This repository is also a Codex plugin. The plugin manifest lives at
`.codex-plugin/plugin.json` and points to the same `skills/` directory used by
the `npx skills` workflow.

### Skills CLI

Install to Codex:

```bash
npx skills add xolarvill/internet-business-skills -a codex -g -y
```

Install to Codex and Claude Code:

```bash
npx skills add xolarvill/internet-business-skills  -a codex -a claude-code -g -y
```

## Updating

When this repository adds new skills or updates existing ones, bring your local installation up to date:

```bash
# Update all installed skills to latest versions
npx skills update -g -y

# If new skills were added to the pack, re-run add to pick them up
npx skills add xolarvill/internet-business-skills -a codex -g -y
```

`skills update` refreshes skills you already have. Re-running `skills add` picks up new skills that weren't in the pack when you first installed.

The plugin manifest and `npx skills` installer do not conflict: both consume the same skill files without requiring duplicated copies.

## Skills

### `find-bad-review`

Research representative public negative reviews for a product across channels such as Amazon, Walmart, Reddit, TikTok, forums, and brand or retailer sites.

Best for:

- voice-of-customer complaint mining
- product weakness research
- objection discovery before merchandising or creative work

Use:

```text
$find-bad-review Analyze the public bad reviews for a dog leash across Amazon, Walmart, Reddit, TikTok, forums, and brand sites.
```

### `analyze-competitor`

Compare a target product or brand against public competitors using structured evidence from websites, marketplaces, reviews, social proof, and visible positioning.

Best for:

- competitor teardown
- offer and positioning comparison
- product-page and assortment comparison
- public market framing before launch or iteration

Use:

```text
$analyze-competitor Compare our dog leash offer against Ruffwear, Max and Neo, and TUG. Focus on price ladder, product claims, review proof, and likely conversion differences.
```

### `portray-audience`

Portray the likely target audience for a product or brand using public evidence from official pages, reviews, communities, and social surfaces.

Best for:

- audience-cluster analysis
- buyer motivation and objection mapping
- target-customer portrayal grounded in public signals
- identifying who the brand seems to attract, miss, or repel

Use:

```text
$portray-audience Analyze this dog leash brand and portray the likely audience clusters, buying motivations, objections, and which audience seems strongest or weakest.
```

### `verify-idea`

Verify a commercial idea using current public internet evidence, a claim ledger, and a disciplined verdict instead of a generic opinion.

Best for:

- fact-checking startup or product ideas
- pressure-testing market-entry theses
- checking demand, channel, and competition assumptions
- identifying what is supported versus still unclear

Use:

```text
$verify-idea Verify the idea of launching a premium retractable dog leash brand on TikTok Shop in the US. Focus on demand, channel fit, competition, and trust burden.
```

## Best Practice

These skills output Markdown reports. An [Obsidian](https://obsidian.md/download) vault is recommended as a research workspace — Markdown-native and link-friendly.

Create a blank folder, open Claude Code inside it, then prompt:
```plain
/init This is a knowledge vault for Obsidian. I'm trying to research [xxx]. My goal is [xxx]. All research should be written in Markdown. Use obsidian-cli to manage notes. All research follows skills from `github.com/xolarvill/internet-business-skills`, which are already installed.
```

## Examples

- [Representative bad review report](examples/dog-leash-report.md)
- [Representative competitor report](examples/dog-leash-competitor-report.md)
- [Representative audience portrait report](examples/dog-leash-audience-report.md)
- [Representative idea verification report](examples/premium-retractable-leash-idea-report.md)
