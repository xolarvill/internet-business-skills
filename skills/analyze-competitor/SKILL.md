---
name: analyze-competitor
description: Compare a target product, brand, or offer against public competitors using structured internet evidence from websites, marketplaces, review surfaces, social proof, and visible positioning. Use when Codex needs a competitor teardown, offer comparison, pricing or assortment comparison, claim differentiation analysis, conversion-oriented public market framing, or a structured competitor report with evidence, confidence notes, and commercial judgments.
---

# Analyze Competitor

## Overview

Use this skill to compare a focal product or brand against public competitors and turn scattered market signals into a structured commercial readout.

The goal is not to produce a generic "market research" summary. The goal is to answer commercially useful questions such as:

- who is positioned higher or lower
- what claims and proof points competitors lean on
- what the focal offer is missing or over-indexing on
- where conversion friction or differentiation likely comes from

## Workflow

1. Confirm the focal target and the comparison question.
2. Define or validate the competitor set.
3. Choose the comparison lenses.
4. Collect public evidence.
5. Normalize findings into a comparison table.
6. Extract differences, patterns, and gaps.
7. Write the final report with commercial judgments.

Do not promise exhaustive market coverage unless the user explicitly asks for it and the evidence supports that claim. The default is a useful, evidence-backed competitor report.

## Clarification Gate

If the request is too broad or ambiguous, do not start live research immediately. Ask one clarification question at a time, and prefer 2-3 concrete options plus room for the user to add extra context.

Ask only when the missing detail materially affects evidence collection or the final commercial judgment. Good reasons to clarify include missing focal target, no competitor set, unclear geography or channel, or uncertainty about whether the user wants positioning, pricing, offer structure, product-page conversion, or proof gaps.

Do not ask a fixed number of questions. If a safe default is available, state the assumption and proceed. If the ambiguity changes the comparison outcome, clarify before searching.

Example clarification:

Question: What competitor set should anchor the comparison?

- A. Direct substitutes in the same channel (recommended): best for conversion and positioning decisions.
- B. Premium reference brands: best for understanding higher-end claims and proof expectations.
- C. Value-priced challengers: best for price pressure and offer-structure analysis.

Extra context: The user can provide competitor names, URLs, target country, sales channel, or the decision this comparison should support.

## Step 1: Confirm The Focal Target

Start by pinning down what exactly is being compared. Use:

- product name
- brand
- variant or SKU family
- category
- target geography
- target channel when relevant

If the user is vague, restate the interpretation clearly. Examples:

- `brand vs brand`
- `one product vs named competitors`
- `one product page vs peer product pages`
- `one offer structure vs category norms`

Treat target ambiguity as a real research issue. If multiple plausible focal targets exist, either narrow to the best-supported one or compare them separately.

## Step 2: Define The Competitor Set

Prefer a user-specified competitor list when one exists.

If the competitor set is incomplete, you may add a small number of public competitors, but only when the matching logic is clear. Good reasons to include a competitor:

- same product type
- same buyer intent
- same price neighborhood
- same channel or marketplace context
- repeatedly surfaced in search, retailer comparison, or category discussion

State why each competitor is included. Avoid mixing fundamentally different competitors into one flat comparison without calling out the mismatch.

Good competitor-set framing:

- direct substitutes
- premium references
- value-priced challengers
- channel-dominant incumbents

## Step 3: Choose Comparison Lenses

Pick only the lenses that answer the user's real question. Default lenses often include:

- positioning
- pricing
- offer structure
- assortment depth
- feature or claim emphasis
- proof and trust signals
- review profile
- likely conversion strengths or weaknesses

Load [references/comparison-lenses.md](references/comparison-lenses.md) for lens definitions and when to use them.

Do not compare everything just because it is visible. The point is decision usefulness, not page transcription.

## Step 4: Collect Public Evidence

**You must read actual page content.** Navigate to and load source pages directly. Never rely on WebSearch snippets to characterize evidence — snippets are truncated and often misrepresent content. If a page is inaccessible, mark the gap. Follow the evidence standard in [../../references/evidence-standard.md](../../references/evidence-standard.md).

Collect enough evidence to support confident comparison, not a full crawl. Good public sources include:

- official brand or product pages
- category or collection pages
- Amazon or major marketplace listings
- Trustpilot, G2, or other review sites
- retailer pages
- public review surfaces
- Reddit threads or other community discussions
- public TikTok or YouTube content when it clearly shows messaging, reactions, or objections

Capture these fields for each usable source:

- competitor
- channel
- source URL
- page type
- what the source supports
- evidence quality: `high`, `medium`, or `low`

When working across heterogeneous sources, keep page roles distinct. A product page and a Reddit thread are not interchangeable evidence.

For source-specific collection notes, load [references/source-adapters.md](references/source-adapters.md).

## Step 5: Normalize Into A Comparison Table

Turn raw notes into a compact comparison structure. At minimum, normalize:

- competitor name
- role in the market
- price or price band
- flagship offer or focal SKU
- main claims
- trust proof
- notable weakness or gap

If the user's question is conversion-oriented, also normalize:

- hero messaging
- page clarity
- bundle or offer strategy
- review count or visible social proof
- objection handling

Do not force fake precision. If pricing varies, use a price band. If the evidence is incomplete, mark it plainly.

## Step 6: Extract Commercial Differences

After table-building, step up one level and ask:

- Which competitors are winning on trust?
- Which competitors are differentiated on product, not just branding?
- Which offer is easiest to understand quickly?
- Where is the focal target underpowered, overcomplicated, or undifferentiated?
- Which visible gaps look commercial, not merely aesthetic?

Good synthesis is comparative and actionable. Weak synthesis is just restating rows.

For judgment and confidence rules, load [references/research-rules.md](references/research-rules.md).

## Step 7: Write The Final Report

Use the report shape in [references/report-format.md](references/report-format.md). The report should usually include:

- focal target
- competitor set and inclusion logic
- coverage summary
- comparison table
- key differences
- commercial judgments
- confidence and gaps
- suggested next move

When useful, generate a starter report skeleton with:

```bash
python3 scripts/render_report_stub.py --target "Dog leash brand" --competitors Ruffwear "Max and Neo" TUG --lenses positioning pricing claims reviews
```

## Output Standard

The final output should answer questions like:

- What kind of market position does each competitor occupy?
- What is the focal target clearly better or worse at?
- What visible signals likely help or hurt conversion?
- Which differences are cosmetic, and which are commercially meaningful?

Commercial judgments are required when the evidence supports them. They should answer:

- Is the focal target under-positioned, over-priced, under-proven, or merely less legible?
- Are competitors competing on product quality, offer engineering, or brand trust?
- What is the most important visible gap to close next?

Every commercial judgment must be traceable to the evidence.

## Guardrails

- Prefer public primary sources when available.
- Separate brand messaging from customer reaction.
- Separate price from value communication.
- Do not pretend incomplete competitor coverage is complete market coverage.
- Mark weak product matching and missing evidence clearly.
- Avoid inflated strategy theater; make claims only as strong as the evidence allows.

## Claude Code Portability

This skill is written to be portable. When adapting it to Claude Code or another agent system:

- keep the workflow unchanged
- preserve the report structure
- preserve confidence and caveat requirements
- adapt only invocation syntax

Use [../../platforms/claude-code.md](../../platforms/claude-code.md) and [../../platforms/codex.md](../../platforms/codex.md) as lightweight portability notes when packaging this workflow elsewhere.

## Resources

### `scripts/render_report_stub.py`

Generate a reusable Markdown starter for a competitor report.

### `references/comparison-lenses.md`

Lens definitions for deciding what dimensions to compare.

### `references/source-adapters.md`

Channel-specific collection notes and evidence caveats.

### `references/research-rules.md`

Normalization, confidence, and commercial-judgment rules.

### `references/report-format.md`

Canonical report shape and field expectations.

### `assets/report-template.md`

Reusable Markdown template for report authoring.
