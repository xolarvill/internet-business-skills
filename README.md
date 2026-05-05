# internet-business-skills

This repository is a pack of commercial analysis skills designed for Codex and Claude Code.

## Installation

Install to Codex:

```bash
npx skills add xolarvill/internet-business-skills -a codex -g -y
```

Install to Codex and Claude Code:

```bash
npx skills add xolarvill/internet-business-skills  -a codex -a claude-code -g -y
```

## Skills

### `find-bad-review`

Research representative public negative reviews for a product across channels such as Amazon, Chewy, Walmart, Reddit, TikTok, and brand or retailer sites.

Best for:

- voice-of-customer complaint mining
- product weakness research
- objection discovery before merchandising or creative work

Use:

```text
$find-bad-review Analyze the public bad reviews for a dog leash across Amazon, Chewy, Walmart, Reddit, TikTok, and brand sites.
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

## Package Shape

Each skill stays self-contained under `skills/`:

```text
skills/
  find-bad-review/
  analyze-competitor/
  portray-audience/
platforms/
examples/
```

Each skill should carry its own:

- `SKILL.md` as the canonical workflow
- `agents/openai.yaml` for UI metadata
- `references/` for method notes and report shapes
- `scripts/` only when a repeated output is worth templating
- `assets/` for reusable report templates

This repository is intentionally a skill pack, not a shared runtime. A small amount of duplication between skills is acceptable if it keeps each skill installable and understandable on its own.

## Skill Design Principles

- Keep skills narrow and triggerable.
- Prefer one commercial research job per skill.
- Reuse tone and report discipline across skills, not a giant all-in-one prompt.
- Keep claims proportional to publicly visible evidence.
- Distinguish evidence collection from business judgment.

## Current Scope

This package is optimized for human-triggered public research, not:

- private API ingestion
- login-dependent scraping
- ongoing monitoring jobs
- full autonomous agent orchestration

## Examples

- [Representative bad review report](examples/dog-leash-report.md)
- [Representative competitor report](examples/dog-leash-competitor-report.md)
- [Representative audience portrait report](examples/dog-leash-audience-report.md)

## Portability

Use `platforms/codex.md` and `platforms/claude-code.md` as lightweight notes for packaging the same skill workflow across agent systems.

Note: the concrete skill names remain `find-bad-review`, `analyze-competitor`, and `portray-audience`; `internet-business-skills` is the package or repository name.
