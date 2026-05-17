---
name: portray-audience
description: Portray the likely target audience for a product, brand, or offer using public internet evidence from official pages, marketplaces, reviews, communities, and social surfaces. Use when Codex needs a structured audience analysis, target-customer readout, buyer-motivation map, objection profile, audience-segmentation view, or a commercially grounded persona-style report with evidence, confidence notes, and explicit hypotheses.
---

# Portray Audience

## Overview

Use this skill to infer who a product or brand is really for, who seems most responsive to it, and where the audience fit breaks down.

The goal is not to invent a glossy persona card. The goal is to turn public evidence into commercially useful audience clusters, motivations, objections, and fit or misfit signals.

## Workflow

1. Confirm the focal target and the audience question.
2. Gather public evidence about positioning, buyers, and reactions.
3. Separate intended audience from observed audience signals.
4. Build audience clusters and motivation patterns.
5. Identify objections, exclusion signals, and misalignment.
6. Write the final report with confidence notes and hypotheses.

Do not present speculative demographic fiction as fact. This skill should stay evidence-backed and honest about where audience portrayal is strong versus thin.

## Clarification Gate

If the request is too broad or ambiguous, do not start live research immediately. Ask one clarification question at a time, and prefer 2-3 concrete options plus room for the user to add extra context.

Ask only when the missing detail materially affects evidence collection or the final commercial judgment. Good reasons to clarify include missing focal product or brand, unclear market, no channel context, or uncertainty about whether the user wants intended audience, observed audience response, conversion blockers, or weak-fit segments.

Do not ask a fixed number of questions. If a safe default is available, state the assumption and proceed. If the ambiguity changes the audience interpretation, clarify before searching.

Example clarification:

Question: Which audience angle should this analysis prioritize?

- A. Likely buyer clusters and motivations (recommended): best for positioning and merchandising work.
- B. Conversion blockers and objections: best for page, ad, or offer optimization.
- C. Audience mismatch or weak-fit segments: best when the brand may be speaking to the wrong buyers.

Extra context: The user can provide a product URL, brand, target country, channel, or the decision this audience readout should support.

## Step 1: Confirm The Focal Target

Start by pinning down what exactly is being analyzed. Use:

- product name
- brand
- specific SKU or offer when relevant
- category
- geography or market context
- target channel when relevant

Restate the question in the right shape. Good examples:

- `Who does this product seem to be for?`
- `What audience is this brand attracting versus trying to attract?`
- `What kind of buyer would convert on this page, and who would bounce?`
- `What audience segments seem strongest or weakest for this offer?`

If the user asks for demographic precision that public evidence cannot support, narrow to audience behavior, motivation, and positioning signals instead.

## Step 2: Gather Public Evidence

**You must read actual page content.** Navigate to and load source pages directly. Never rely on WebSearch snippets to characterize evidence — snippets are truncated and often misrepresent content. If a page is inaccessible, mark the gap. Follow the evidence standard in [../../references/evidence-standard.md](../../references/evidence-standard.md).

Collect only enough evidence to support a useful audience portrait. Good public sources include:

- official brand and product pages
- collection pages and merchandising language
- pricing context
- visible reviews and FAQs
- Reddit or community discussions
- public TikTok, YouTube, or creator content
- competitor pages when they clarify category expectations

Capture these fields for each usable source:

- channel
- source URL
- page type
- what the source suggests about audience or buyer intent
- evidence quality: `high`, `medium`, or `low`

For source-specific heuristics, load [references/source-adapters.md](references/source-adapters.md).

## Step 3: Separate Intended Audience From Observed Signals

Keep at least three layers distinct:

- who the brand appears to target
- who seems to respond positively in public signals
- who appears unconvinced, excluded, or mismatched

This separation is critical. Brand positioning and audience response are related, but not identical.

Examples:

- a page may clearly target premium, design-conscious buyers
- reviews may reveal strong adoption by practical gift shoppers
- community discussion may show experts dismissing the product as under-specced

Do not collapse these into one flat persona.

## Step 4: Build Audience Clusters

Prefer audience clusters over a single fictional persona. Good clusters usually combine:

- use case
- motivation
- trust threshold
- price sensitivity
- identity or self-image signal

Examples:

- performance-first owners
- budget-conscious practical buyers
- style-led gift shoppers
- cautious first-time buyers

Load [references/audience-lenses.md](references/audience-lenses.md) for recommended cluster dimensions.

## Step 5: Identify Motivations, Objections, And Misfit

For each meaningful audience cluster, ask:

- what are they trying to get done
- what makes the offer feel credible to them
- what would block conversion
- what language or proof likely matters most
- which adjacent audiences are being excluded or underserved

Also ask whether the evidence suggests:

- audience clarity
- audience confusion
- audience mismatch
- audience overreach

For confidence and hypothesis rules, load [references/research-rules.md](references/research-rules.md).

## Step 6: Write The Final Report

Use the output shape in [references/report-format.md](references/report-format.md). The report should usually include:

- focal target
- coverage summary
- intended audience signals
- observed audience clusters
- motivations and objection patterns
- excluded or weak-fit audiences
- commercial judgments
- confidence and gaps
- suggested next move

When useful, generate a starter report skeleton with:

```bash
python3 scripts/render_report_stub.py --target "Dog leash brand" --lenses positioning motivations objections fit-signals
```

## Output Standard

The final output should answer questions like:

- Who seems to be the most likely buyer for this offer?
- What motivations are most visible or best supported?
- Which audience segments appear weak-fit or unconvinced?
- Is the brand speaking clearly to one audience, or trying to speak to too many?

When the evidence is strong, commercial judgments are required. They should answer:

- Is the problem lack of demand, weak proof, fuzzy targeting, or audience mismatch?
- Which audience cluster looks most commercially promising?
- What is the clearest audience gap to address next?

Use explicit labels such as `observed signal` and `hypothesis` when needed. Do not let speculative inferences masquerade as facts.

## Guardrails

- Prefer public primary sources when available.
- Separate brand intent from audience response.
- Separate demographic inference from behavior and motivation signals.
- Do not invent false precision around age, income, or lifestyle.
- Mark thin evidence and weak audience matching clearly.
- Avoid generic persona theater; keep the output commercially grounded.

## Claude Code Portability

This skill is written to be portable. When adapting it to Claude Code or another agent system:

- keep the workflow unchanged
- preserve the report structure
- preserve confidence and caveat requirements
- adapt only invocation syntax

Use [../../platforms/claude-code.md](../../platforms/claude-code.md) and [../../platforms/codex.md](../../platforms/codex.md) as lightweight portability notes when packaging this workflow elsewhere.

## Resources

### `scripts/render_report_stub.py`

Generate a reusable Markdown starter for an audience-portrait report.

### `references/audience-lenses.md`

Lens definitions for how to segment and portray audience clusters.

### `references/source-adapters.md`

Channel-specific collection notes and audience-evidence caveats.

### `references/research-rules.md`

Confidence rules, cluster rules, and observed-vs-hypothesis discipline.

### `references/report-format.md`

Canonical report shape and field expectations.

### `assets/report-template.md`

Reusable Markdown template for report authoring.
