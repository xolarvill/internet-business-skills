# Codex Notes

- Keep the skill in a discoverable `skills/` path.
- Use `SKILL.md` as the canonical workflow.
- Keep references one level deep and load them only as needed.
- Validate the skill after updates.

## Platform-Specific Tool Guidance

**Fresh runs:** If Codex has no remembered tool inventory for this workspace, quickly check the available direct-internet capabilities before researching: built-in web/search/fetch tools, installed CLIs such as `gh` when GitHub evidence matters, configured MCP tools, and requestable browser/computer-use plugins. Choose based on the investigation and target site; do not default to the most resource-heavy option.

**Reading pages:** All research skills in this pack (`find-bad-review`, `verify-idea`, `analyze-competitor`, `portray-audience`) require reading actual page content. Use Codex's page-fetching or browser tools to load target pages directly. Never rely on search result snippets alone — search summaries are truncated and often misrepresent content. If Codex does not have a browser tool available, use the equivalent page-reading capability (e.g., a fetch/read-url tool) to load the full page. See `references/evidence-standard.md` for the full evidence philosophy.
