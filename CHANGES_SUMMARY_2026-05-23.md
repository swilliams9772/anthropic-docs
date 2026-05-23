# Anthropic Documentation Changes Summary

**Scraped:** May 23, 2026
**Compared against:** January 9, 2026 snapshot
**Window:** ~4.5 months

| Metric                       | Old (Jan 9) | New (May 23) | Δ            |
| ---------------------------- | ----------- | ------------ | ------------ |
| Markdown pages               | 692         | 1,138        | **+446**     |
| Files added                  | —           | —            | **+446**     |
| Files modified               | —           | —            | **+427**     |
| Files unchanged              | —           | —            | 265          |
| Total URLs visited           | —           | 1,348        | —            |
| Pages with scrape errors     | —           | 79           | —            |

Top-level sections present in the May 23 snapshot but not in the January 9 snapshot:

- **`managed-agents/`** — entirely new section for Claude Managed Agents (24 pages)
- **`manage-claude/`** — admin/governance docs (Admin API, WIF providers, data residency, compliance)
- Plus several new top-level pages: `overview.md`, `troubleshooting.md`

---

## Headline platform changes (Jan 9 → May 23, 2026)

These are pulled from `en_release-notes_api.md` in the new snapshot — chronological.

### Models

- **Jan 29, 2026** — Structured outputs **generally available** on the Claude API for Sonnet 4.5, Opus 4.5, and Haiku 4.5. `output_format` moved to `output_config.format`; no beta header required.
- **Feb 5, 2026** — **Claude Opus 4.6** launched. Recommends [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`thinking: {type: "adaptive"}`); manual `budget_tokens` deprecated. Does **not** support assistant message prefilling.
- **Feb 17, 2026** — **Claude Sonnet 4.6** launched. Improved agentic-search performance at lower token consumption; supports extended thinking and the 1M token context window (beta).
- **April 16, 2026** — **Claude Opus 4.7** launched ($5 / $25 per MTok). First Claude model with **high-resolution image support** (2576px / 3.75MP). New **`xhigh` effort level**. Introduces [task budgets](https://platform.claude.com/docs/en/build-with-claude/task-budgets) (beta header `task-budgets-2026-03-13`). **Breaking:** extended thinking budgets removed — `thinking: {type: "enabled", budget_tokens: N}` now returns a 400.
- **April 14, 2026** — Sonnet 4 (`claude-sonnet-4-20250514`) and Opus 4 (`claude-opus-4-20250514`) deprecated; retirement scheduled **June 15, 2026**. Migrate to Sonnet 4.6 / Opus 4.7.
- **April 20, 2026** — **Claude Haiku 3** retired.
- **Feb 19, 2026** — **Claude Sonnet 3.7** and **Claude Haiku 3.5** retired.
- **Jan 5, 2026** — **Claude Opus 3** retired.

### Context, caching, and output controls

- **Feb 19, 2026** — **Automatic caching** for the Messages API: pass a single `cache_control` on the request body and the platform automatically advances the cache prefix as conversations grow. No manual breakpoint bookkeeping. Available on the Claude API and Microsoft Foundry (preview).
- **Feb 5, 2026** — **Compaction API** (beta) launched — server-side context summarization for effectively infinite conversations (Opus 4.6).
- **Mar 13, 2026** — **1M token context window GA** for Opus 4.6 and Sonnet 4.6 at standard pricing (no beta header). Dedicated 1M rate limits removed.
- **Mar 16, 2026** — `thinking.display: "omitted"` lets you suppress thinking content from streamed responses while preserving signatures for multi-turn continuity.
- **Mar 30, 2026** — `max_tokens` cap raised to **300k** on the Message Batches API for Opus 4.6 / Sonnet 4.6 (`output-300k-2026-03-24` beta).
- **April 30, 2026** — 1M-token context beta (`context-1m-2025-08-07`) **retired** on Sonnet 4.5 / Sonnet 4. Migrate to Sonnet 4.6 / Opus 4.6.
- **May 13, 2026** — **Cache diagnostics** (public beta): `diagnostics.previous_message_id` + `cache-diagnosis-2026-04-07` header makes the API surface a `cache_miss_reason` explaining why the prefix diverged.

### Speed and effort tuning

- **Feb 5, 2026** — **Effort parameter GA**; supports Opus 4.6. Replaces `budget_tokens` on new models.
- **Feb 7, 2026** — **Fast mode** (research preview) for Opus 4.6 — `speed: "fast"` for up to 2.5x faster token generation at premium pricing.
- **May 12, 2026** — Fast mode now supports **Opus 4.7**.

### Agents, tools, and skills

- **Feb 17, 2026** — Code execution **free when used with web search or web fetch**. Web search, web fetch, code execution, tool search, memory tool, programmatic tool calling, and tool-use examples all become **generally available** (no beta header). Web search/fetch gain **dynamic filtering** via code execution.
- **Feb 5, 2026** — **Fine-grained tool streaming** GA on all models and platforms.
- **April 7, 2026** — **Messages API on Amazon Bedrock** launches as a research preview; new `/anthropic/v1/messages` endpoint shares the first-party request shape, runs on AWS-managed infra with zero operator access.
- **April 8, 2026** — 🆕 **Claude Managed Agents** in public beta. Fully managed agent harness with secure sandboxing, built-in tools, and SSE streaming. All endpoints require `managed-agents-2026-04-01`. Includes Cloud Containers, Memory, Multi-agent sessions, Outcomes, Vaults, Webhooks. New section: `managed-agents/` (24 pages).
- **April 8, 2026** — **`ant` CLI** released — a command-line client for the Claude API with native Claude Code integration and YAML resource versioning.
- **April 9, 2026** — **Advisor tool** (public beta, `advisor-tool-2026-03-01`). Pairs a fast executor model with a higher-intelligence advisor model for mid-generation strategic guidance.
- **April 23, 2026** — **Memory for Claude Managed Agents** (public beta).
- **May 6, 2026** — **Multiagent sessions** and **Outcomes** in public beta. Vault credential background refresh for `mcp_oauth`. **Webhooks** for Managed Agents.
- **May 18, 2026** — Web search tool returns **richer SEC filing data** for financial-research agents.
- **May 19, 2026** — 🆕 **MCP tunnels** (Research Preview) to connect to MCP servers in your private network. Self-hosted sandboxes available for Claude Managed Agents. Active-session MCP/tool reconfiguration. Tool outputs > 100K tokens spill to sandbox files.

### Platform / cloud distribution

- **Nov 18, 2025** *(pre-window context)* — Claude in Microsoft Foundry launched.
- **April 7, 2026** — Claude **Mythos Preview** (Project Glasswing) for defensive cybersecurity, invitation-only.
- **April 16, 2026** — **Claude in Amazon Bedrock** opens to all Bedrock customers (Opus 4.7 + Haiku 4.5 self-serve, `/anthropic/v1/messages` in 27 AWS regions).
- **May 11, 2026** — 🆕 **Claude Platform on AWS** launches — Claude API on Anthropic-managed infra accessible through AWS with AWS billing and IAM auth.

### Admin / governance

- **Feb 5, 2026** — **Data residency controls** (`inference_geo`); US-only inference at 1.1x pricing for models released after Feb 1, 2026.
- **Mar 18, 2026** — Models API adds `max_input_tokens`, `max_tokens`, and a `capabilities` object.
- **April 24, 2026** — **Rate Limits API** released — programmatic access to org/workspace rate-limit configuration.

### Documentation infrastructure

- **Jan 12, 2026** — `console.anthropic.com` now redirects to `platform.claude.com`. (Already in effect when the previous snapshot was scraped.)
- **Nov 19, 2025** *(pre-window context)* — Docs platform moved to platform.claude.com/docs.

---

## Where the file diff lives (by section)

The full per-file breakdown is in [`changes_report.json`](changes_report.json) and the human-readable dump in [`changes_analysis.txt`](changes_analysis.txt). Highlights below.

### New sections / large additions

- **Managed Agents (`en_managed-agents_*`, 23 files)** — `overview`, `quickstart`, `agent-setup`, `cloud-containers`, `define-outcomes`, `dreams`, `environments`, `events-and-streaming`, `files`, `github`, `mcp-connector`, `memory`, `migration`, `multi-agent`, `onboarding`, `permission-policies`, `self-hosted-sandboxes(-security)`, `sessions`, `skills`, `tools`, `vaults`, `webhooks`.
- **Manage Claude (`en_manage-claude_*`, 25 files)** — Admin API, authentication, claude-code analytics API, compliance API (activity feed, access, content data, errors, FAQ, integration patterns, org data), data residency, rate-limits API, usage-cost API, workspaces, plus **Workload Identity Federation** providers: AWS, Azure, GCP, GitHub Actions, Kubernetes, Okta, SPIFFE.
- **MCP tunnels (`en_agents-and-tools_mcp-tunnels_*`, 7 files)** — `overview`, `quickstart`, `console`, `deploy-compose`, `deploy-helm`, `reference`, `security`, `troubleshooting`.
- **Beta admin endpoints (`en_api_admin_*`, ~30 files)** — full CRUD for `admin/mcp_tunnels`, `admin/mcp_tunnels/tunnel_certificates`, `admin/rate_limits`, `admin/workspaces/rate_limits`, `admin/invites`, `admin/api_keys`, `admin/workspaces`, `admin/cost_report`.
- **Beta agent / managed-agent endpoints (`en_api_beta_*`, ~100 files)** — `agents`, `agents/versions`, `environments`, `permission_policies`, `sessions`, `sessions/events`, `sessions/files`, `vaults` (full CRUD per resource).
- **New build-with-claude pages (11 files)** — `adaptive-thinking`, `api-and-data-retention`, `cache-diagnostics`, `claude-in-amazon-bedrock`, `claude-on-amazon-bedrock-legacy`, `claude-platform-on-aws`, `compaction`, `fast-mode`, `prompt-engineering/claude-prompting-best-practices`, `prompt-engineering/prompting-tools`, `task-budgets`.
- **Models pages** — `whats-new-claude-4-6`, `whats-new-claude-4-7`, `model-ids-and-versions`, `migration-guide`.
- **Agent SDK additions** — `agent-loop`, `claude-code-features`, `observability`, `session-storage`, `streaming-output`, `tool-search`.
- **Tool-use deep-dives (added)** — `advisor-tool`, `build-a-tool-using-agent`, `define-tools`, `handle-tool-calls`, `how-tool-use-works`, `manage-tool-context`, `parallel-tool-use`, `server-tools`, `strict-tool-use`, `tool-combinations`, `tool-reference`, `tool-runner`, `tool-use-with-prompt-caching`, `troubleshooting-tool-use`.
- **Support articles** — 214 new help-center articles covering enterprise plans, Claude for Education / Financial Services / Life Sciences / Nonprofits, connectors, SSO/JIT/SCIM, custom data retention, Microsoft 365 connector, etc.

### Heavily modified files (biggest content deltas)

| File                                             | Old      | New        | Δ           |
| ------------------------------------------------ | -------- | ---------- | ----------- |
| `en_api_beta.md`                                 | 539,537  | 1,301,183  | **+761,646** |
| `en_api_messages.md`                             | 239,384  | 508,503    | **+269,119** |
| `en_api_messages_create.md` / batches / etc.     | —        | —          | substantial expansions for new beta headers and model fields |

The growth in `en_api_beta.md` corresponds to the rollout of new beta headers in this window: `fast-mode-2026-02-01`, `output-300k-2026-03-24`, `user-profiles-2026-03-24`, `advisor-tool-2026-03-01`, `managed-agents-2026-04-01`, `cache-diagnosis-2026-04-07`, `task-budgets-2026-03-13`, plus the schema expansion for managed-agents-related types.

---

## Files generated / updated by this run

- `anthropic_docs/anthropic_docs_md/` (1,138 markdown files)
- `anthropic_docs/anthropic_docs_html/` (cleaned HTML)
- `anthropic_docs/anthropic_docs_full_html/` (full HTML)
- `anthropic_docs/page_metadata.json`
- `scraper_v4.log` (and timestamped sibling)
- `changes_report.json` — machine-readable diff inventory
- `changes_analysis.txt` — full human-readable diff dump with examples
- This file — `CHANGES_SUMMARY_2026-05-23.md`

A pre-run snapshot of the previous state was preserved at `anthropic_docs_backup_20260523_124122/` so the diff can be regenerated at any time.
