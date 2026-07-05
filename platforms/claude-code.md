# Claude Code Notes

Reuse the same workflow and report structure from the core skill. Port the trigger description and guardrails into your local Claude Code skill or agent prompt format without changing the logic.

## Copy-Ready Prompt Core

Use this as the starting prompt body for a Claude Code version of the skill:

```md
Collect and summarize representative public negative reviews for a product across channels such as Amazon, Walmart, Reddit, TikTok, forums, and brand or retailer sites. Use this workflow when researching product complaints, voice-of-customer themes, review-based weaknesses, channel-specific objections, or when creating a structured bad-review report with evidence, confidence notes, and source links.

Workflow:
1. Confirm the product target.
2. Choose channels and search strategy.
3. Collect negative evidence from public pages.
4. Normalize, de-duplicate, and cluster complaints.
5. Select representative examples.
6. Write the final report with confidence and gaps.

Guardrails:
- Prefer public pages and primary sources.
- Distinguish product complaints from shipping, seller, or packaging complaints unless asked otherwise.
- Separate frequency from severity.
- Mark weak product matching and weak evidence explicitly.
- Do not simplify this into generic sentiment analysis.
```

## Porting Rules

- Preserve confidence labels, evidence notes, and explicit caveats.
- Keep the source-adapter logic and report format aligned with the files in `skills/find-bad-review/references/`.
- Treat `skills/find-bad-review/SKILL.md` as the canonical workflow source.

## Platform-Specific Tool Guidance

**Fresh runs:** If Claude Code has no remembered tool inventory for this workspace, quickly check the available direct-internet capabilities before researching: `WebSearch`/`WebFetch`, Playwright/browser tools, installed CLIs such as `gh` when GitHub evidence matters, and configured MCP tools. Choose based on the investigation and target site; do not default to the most resource-heavy option.

**Reading pages:** All research skills in this pack (`find-bad-review`, `verify-idea`, `analyze-competitor`, `portray-audience`) require reading actual page content. Use Playwright (`browser_navigate` + `browser_snapshot`) or `WebFetch` to load target pages directly. Never rely on `WebSearch` snippets alone — search summaries are truncated and often misrepresent content. See `references/evidence-standard.md` for the full evidence philosophy.
