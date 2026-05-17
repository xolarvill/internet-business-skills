---
name: find-bad-review
description: Collect and summarize representative public negative reviews for a product across channels such as Amazon, Walmart, Reddit, TikTok, forums, and brand or retailer sites. Use when Codex needs to research product complaints, voice-of-customer themes, review-based weaknesses, channel-specific objections, or create a structured bad-review report with evidence, confidence notes, and source links.
---

# Find Bad Review

## Overview

Use this skill to research what customers dislike about a product and to turn scattered negative feedback into a structured complaint report. Prioritize evidence-backed public sources, representative complaint themes, and honest confidence notes over broad sentiment summaries.

The goal is not just to list complaints. The goal is to turn complaints into higher-value commercial understanding: what kind of product or subtype is structurally weak, what objections are likely to suppress conversion or repeat purchase, and what a rational operator should conclude from the evidence.

## Workflow

1. Confirm the product target.
2. Select channels and search strategy.
3. Collect negative evidence from public pages.
4. Normalize, de-duplicate, and cluster complaints.
5. Select representative examples.
6. Translate findings into commercial judgments.
7. Write the final report with confidence and gaps.

Do not claim exhaustive coverage unless the user explicitly asks for it and you actually achieved it. The default goal is a useful research report, not a full crawl.

## Clarification Gate

If the request is too broad or ambiguous, do not start live research immediately. Ask one clarification question at a time, and prefer 2-3 concrete options plus room for the user to add extra context.

Ask only when the missing detail materially affects evidence collection or the final commercial judgment. Good reasons to clarify include missing product identity, broad category scope, unknown target market, unclear channels, or uncertainty about whether the user wants product complaints, seller friction, or category-level risk.

Do not ask a fixed number of questions. If a safe default is available, state the assumption and proceed. If the ambiguity changes the research outcome, clarify before searching.

Example clarification:

Question: What should the complaint research focus on?

- A. Product failure modes and negative reviews (recommended): best for product or merchandising decisions.
- B. Seller, shipping, and packaging friction: best when operational friction matters too.
- C. Category-level weak subtypes: best when choosing what product direction to avoid or pursue.

Extra context: The user can provide a product URL, brand, target country, marketplace, or specific decision they are trying to make.

## Step 1: Confirm The Product Target

Start by pinning down the product as tightly as the user context allows. Use:

- product name
- brand
- variant or size
- category terms
- candidate URLs or listings when available

If identity is ambiguous, state the ambiguity and either:

- narrow to the best-supported listing, or
- compare multiple likely listings separately

Treat "same product across channels" as a research problem, not a solved fact. Use exact identifiers when present; otherwise explain the matching logic.

## Step 2: Choose Channels And Search Strategy

Default target channels:

- Amazon
- Walmart
- Reddit
- TikTok
- X (formerly Twitter)
- category-specific retailer leaders when relevant
- specialty forums when relevant (e.g. dog training forums for a dog leash)
- brand or retailer review pages

When one source is weak or inaccessible, broaden through public search and visible page navigation. Keep the search focused around the product and complaint intent. Good search patterns include:

- `<product> reviews complaints`
- `<product> one star review`
- `<brand> <product> reddit`
- `<product> tiktok review problem`
- `<product> site:amazon.com review`

Avoid promising coverage of sites that require login, aggressive scraping, or non-public APIs unless the user explicitly asks for a heavier implementation.

For source-specific heuristics, load [references/source-adapters.md](references/source-adapters.md).

## Step 3: Collect Negative Evidence

**You must read actual page content.** Navigate to and load review pages, product pages, and forum threads directly. Never rely on WebSearch snippets or search result summaries to characterize a review or complaint — snippets are truncated, decontextualized, and often misrepresent the actual content. If a page is inaccessible, mark the evidence gap rather than substituting a snippet. Follow the evidence standard in [../../references/evidence-standard.md](../../references/evidence-standard.md).

Collect only enough material to support a confident summary. Favor:

- review pages with visible rating context
- threads with firsthand product complaints
- public product pages with review sorting or filtering
- public videos or comments only when the complaint is clearly visible and attributable

Capture these fields for each usable piece of evidence:

- channel
- source URL
- page title or listing name
- complaint text or concise paraphrase
- rating or visible negative cue
- product match confidence: `high`, `medium`, or `low`
- evidence quality: `high`, `medium`, or `low`

If you cannot quote safely or the page is noisy, paraphrase the complaint instead of copying large text.

## Step 4: Normalize And Cluster Complaints

Merge semantically similar complaints into stable themes. Prefer concrete failure modes over vague sentiment labels.

Good complaint themes:

- clasp breaks or unlocks
- leash frays after short use
- retractable tape tangles
- handle is uncomfortable for large dogs
- hardware is too heavy for small dogs

Weak complaint themes:

- bad quality
- people do not like it
- negative sentiment

De-duplicate repeats across channels and avoid counting near-identical syndicated reviews as independent evidence.

When the target is a broad product category or spans multiple listings, also look for one level up of synthesis:

- high-complaint subtypes
- high-risk use cases
- failure-prone design patterns

Example: for `dog leash`, do not stop at listing isolated issues. Notice when `retractable leashes` emerge as a distinct high-complaint subtype with repeated mechanism and safety complaints.

Then go one step further: ask what business conclusion follows. Example:

- `Retractable leashes are not just risky; they appear to be a structurally complaint-heavy subcategory, which makes them a weaker hero-SKU candidate unless differentiated on reliability and control.`

For clustering and confidence rules, load [references/research-rules.md](references/research-rules.md).

## Step 5: Select Representative Examples

For each theme, choose a small number of examples that best represent the complaint, ideally across more than one channel. "Representative" means at least one of:

- frequently repeated
- high consequence or safety risk
- clearly worded and specific
- repeated across multiple channels

Do not select examples just because they are dramatic. The point is signal, not entertainment.

## Step 6: Write The Final Report

Use the report format in [references/report-format.md](references/report-format.md). The final report must include:

- product target and matching notes
- channel coverage
- category-level readout when applicable
- commercial judgments grounded in evidence
- top complaint themes
- example pages directly under each issue
- confidence and evidence notes
- gaps, caveats, and likely blind spots

When useful, generate a starter report skeleton with:

```bash
python scripts/render_report_stub.py --product "Dog leash" --channels amazon walmart reddit tiktok retailer forum
```

## Output Standard

Default report sections:

1. Product target
2. Coverage summary
3. Category-level readout
4. Commercial judgments
5. Key problems
6. Cross-channel patterns
7. Confidence and gaps
8. Suggested next research step

Keep claims proportional to evidence. If only Reddit and one retailer page were available, say so plainly.

Commercial judgments are required when the evidence supports them. They should answer questions such as:

- Is this a weak subcategory or merely a weak listing?
- Is the complaint pattern likely to hurt conversion, retention, or review velocity?
- Does the evidence suggest a positioning problem, a product-design problem, or a merchandising problem?
- What would a sensible operator avoid, change, or investigate next?

Do not present vague strategy fluff. Every commercial judgment must be traceable to the investigated evidence.

For each key problem, prefer this shape:

- problem statement as the section title
- why it matters
- confidence
- where it shows up
- `Example pages:` immediately below, with direct links

## Guardrails

- Prefer public pages and official or primary sources when available.
- Treat Reddit, TikTok comments, and forums as useful but noisier evidence.
- Separate complaint frequency from complaint severity.
- Do not pretend "no evidence found" means "no problem exists."
- Mark weak product matching explicitly.
- Distinguish product complaints from shipping, seller, or packaging complaints unless the user wants all friction sources.

## Claude Code Portability

This skill is written to be portable. When adapting it to Claude Code or another agent system:

- keep the workflow unchanged
- preserve the output structure
- preserve confidence and caveat requirements
- adapt only platform-specific invocation syntax

Use [../../platforms/claude-code.md](../../platforms/claude-code.md) and [../../platforms/codex.md](../../platforms/codex.md) as lightweight portability notes when packaging this workflow elsewhere.

## Resources

### `scripts/render_report_stub.py`

Generate a reusable Markdown starter for a complaint report.

### `references/source-adapters.md`

Channel-specific collection notes and failure modes.

### `references/research-rules.md`

Clustering, confidence, and de-duplication rules.

### `references/report-format.md`

Canonical report format and field expectations.

### `assets/report-template.md`

Reusable Markdown template for report authoring.
