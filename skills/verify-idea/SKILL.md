---
name: verify-idea
description: Verify a commercial idea or business thesis using current public internet evidence from search results, websites, marketplaces, communities, reviews, and other visible market signals. Use when Codex needs to fact-check a startup idea, product concept, market-entry thesis, channel strategy, demand hypothesis, unit-economics risk, operational drag, content fit, or brand potential and produce a claim-by-claim verdict with evidence, confidence notes, and explicit unsupported or unclear areas.
---

# Verify Idea

## Overview

Use this skill to evaluate whether a business idea is supported, weakened, or still unresolved by current public evidence.

The goal is not to give a vague opinion. The goal is to turn an idea into testable commercial claims, search the current internet for evidence, and return a disciplined verdict with explicit `supported`, `contradicted`, or `unclear` outcomes.

Treat the idea as a commercial system, not just an audience or use-case story. A useful verification pass should ask why the market exists, why buyers would choose this product, whether the offer is differentiated, whether acquisition and LTV look plausible, whether content and reviews can compound, whether logistics, compliance, margin, or after-sales drag can break the business, and whether the idea can become a brand.

## Workflow

1. Restate the idea and the decision context.
2. Extract 3-7 testable claims.
3. Choose the validation lenses and required commercial viability dimensions.
4. Search for current public evidence.
5. Vet and cross-check sources, then score each claim and each viability dimension.
6. Write the verdict, confidence, and next validation step.

Do not skip claim extraction. Do not jump from raw search results straight to a yes or no answer.

## Clarification Gate

If the request is too broad or ambiguous, do not start live research immediately. Ask one clarification question at a time, and prefer 2-3 concrete options plus room for the user to add extra context.

Ask only when the missing detail materially affects evidence collection or the final commercial judgment. Good reasons to clarify include a vague idea statement, missing target customer, unknown geography, unclear channel, no price or value posture, or uncertainty about whether the decision is launch, positioning, channel selection, or product selection.

Do not ask a fixed number of questions. If a safe default is available, state the assumption and proceed. If the ambiguity makes the idea impossible to turn into testable claims, clarify before searching.

Example clarification:

Question: What decision should this idea verification support?

- A. Whether to pursue this product or market (recommended): best for a practical go/no-go readout.
- B. Which channel or audience to prioritize: best when the idea is plausible but go-to-market is uncertain.
- C. What assumptions are riskiest: best when the user wants a claim-led validation agenda.

Extra context: The user can provide target market, buyer, channel, price posture, competitors, or any assumption they most want tested.

## Step 1: Confirm The Idea And Context

Restate the idea in a way that can actually be tested. Capture:

- idea statement
- target product or service
- geography
- target customer
- channel or go-to-market path
- price or value posture when relevant

Examples:

- `Launch a premium retractable dog leash brand on TikTok Shop in the US`
- `Sell a B2B AI call-summary product to SMB dental clinics`
- `Build a low-price electrolyte drink for runners on Amazon`

If the idea is too broad, narrow it before searching. "Start a pet brand" is not a searchable proposition.

## Step 2: Extract Testable Claims

Turn the idea into a small claim ledger. Good claims are falsifiable and externally checkable.

Common claim types:

- the market exists for a stable reason, not only a temporary product fad
- demand exists
- buyers have a clear reason to choose the product over substitutes
- the audience is reachable through the chosen channel
- competitors do not already saturate the position
- the value proposition is differentiated enough to matter
- the price or trust burden is viable
- CAC proxy and reasonable LTV logic are not obviously broken
- content, SEO, photography, UGC, review, or AI discoverability can compound
- logistics, margin, compliance, or after-sales drag are manageable
- the idea has some route to brand memory or category expansion
- obvious regulatory or platform constraints are manageable

Load [references/validation-lenses.md](references/validation-lenses.md) for lens definitions and claim examples.

Bad claim shapes:

- `This idea is good`
- `People will probably like it`
- `The market looks interesting`

Good claim shapes:

- `There is visible public demand for retractable leashes among US dog owners`
- `TikTok Shop is a plausible acquisition channel for this product type`
- `Premium positioning is not fully occupied by dominant incumbents`

## Step 3: Choose Validation Lenses

Pick the lenses needed to test the idea. Every report must include a compact commercial viability snapshot covering the baseline dimensions below. If public evidence is unavailable for a dimension, mark it `unclear` and explain the evidence gap; do not omit the dimension.

Baseline dimensions:

- market existence and need stability
- buyer motivation
- demand signal
- audience fit
- competitor pressure
- differentiation
- channel reality
- acquisition economics and CAC proxy
- LTV or repeat-purchase plausibility
- content and discoverability fit
- trust and proof burden
- regulatory or policy friction
- logistics, margin, and operational plausibility when visible in public signals
- after-sales or support complexity
- brand compounding potential

The point is not to do a full market study. The point is to pressure-test the core claims while preserving enough commercial coverage that the answer does not over-index on scene, persona, or generic demand.

## Step 4: Search Current Public Evidence

**You must read actual page content.** Navigate to and load source pages directly. Never rely on WebSearch snippets to characterize evidence — snippets are truncated and often misrepresent content. If a page is inaccessible, mark the gap. Follow the evidence standard in [../../references/evidence-standard.md](../../references/evidence-standard.md).

This skill depends on current internet search and live public browsing. Always prefer current sources and note the dates when the freshness matters.

Good public evidence sources include:

- official company and product pages
- marketplaces
- retailer pages
- search-result and SEO surfaces when discoverability matters
- app stores or product directories
- Reddit and community discussions
- Meta ad Library and similar ad transparency tools
- public social content
- public pricing pages
- FAQs, warranty, returns, support, and shipping pages
- current news or policy pages when constraints matter

Capture these fields for each useful source:

- source URL
- source type
- date if visible and relevant
- which claim it informs
- what it supports or weakens
- evidence quality score: `1-10`
- corroboration status: `corroborated`, `partly corroborated`, or `single-source`
- caveat if the source may reflect misuse, seller-specific friction, shipping damage, stale data, or a non-representative edge case

For source-specific heuristics, load [references/source-adapters.md](references/source-adapters.md).

## Step 5: Score Each Claim

Every claim must land in exactly one bucket:

- `supported`
- `contradicted`
- `unclear`

`unclear` is a normal result, not a failure mode. Use it when:

- evidence is sparse
- evidence conflicts
- the claim depends on private data
- freshness matters and public evidence is stale

Do not promote an `unclear` claim to `supported` just because the overall idea feels plausible.

For confidence and verdict rules, load [references/research-rules.md](references/research-rules.md).

## Step 6: Write The Final Verdict

Use the report shape in [references/report-format.md](references/report-format.md). The output should usually include:

- idea statement
- claim ledger
- commercial viability snapshot
- coverage summary
- strongest supporting facts
- strongest weakening facts
- verdict
- confidence and gaps
- suggested next validation step

When useful, generate a starter report skeleton with:

```bash
python3 scripts/render_report_stub.py --idea "Launch a premium retractable dog leash brand on TikTok Shop in the US" --lenses demand differentiation acquisition economics content operations brand
```

## Output Standard

The final output should answer questions like:

- Which parts of the idea are currently supported by public evidence?
- Which parts are actively weakened by public evidence?
- Which parts remain unresolved without private or primary research?
- Is the main issue demand, buyer motivation, differentiation, CAC/LTV, content fit, logistics, compliance, after-sales drag, brand potential, or feasibility?

Good verdict shapes:

- `Promising but under-verified`
- `Demand-supported but channel-weakened`
- `Crowded and weakly differentiated`
- `Too early to validate from public evidence alone`

Avoid absolute language unless the evidence truly justifies it.

## Guardrails

- Use current internet evidence, not static memory.
- Extract claims before searching.
- Do not confuse competitor existence with proof of demand.
- Do not confuse social chatter with commercial validation.
- Do not confuse lack of evidence with positive evidence.
- Mark stale evidence and missing dates clearly.
- Include links to the sources used.

## Claude Code Portability

This skill is written to be portable. When adapting it to Claude Code or another agent system:

- keep the workflow unchanged
- preserve the claim-led structure
- preserve confidence and caveat requirements
- ensure the environment has live public search capability
- adapt only invocation syntax

Use [../../platforms/claude-code.md](../../platforms/claude-code.md) and [../../platforms/codex.md](../../platforms/codex.md) as lightweight portability notes when packaging this workflow elsewhere.

## Resources

### `scripts/render_report_stub.py`

Generate a reusable Markdown starter for an idea-verification report.

### `references/validation-lenses.md`

Lens definitions for turning an idea into testable commercial claims.

### `references/source-adapters.md`

Channel-specific collection notes and evidence caveats.

### `references/research-rules.md`

Verdict rules, confidence rules, and anti-handwaving constraints.

### `references/report-format.md`

Canonical report shape and field expectations.

### `assets/report-template.md`

Reusable Markdown template for report authoring.
