---
title: 
source_url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Prompt engineering

Giving Claude a role with a system prompt

[Welcome](/en/home)[User Guides](/en/docs/welcome)[API Reference](/en/api/getting-started)[Prompt Library](/en/prompt-library/library)[Release Notes](/en/release-notes/overview)

- [Developer Console](https://console.anthropic.com/)
- [Developer Discord](https://www.anthropic.com/discord)
- [Support](https://support.anthropic.com/)

##### Get started

* [Overview](/en/docs/welcome)
* [Initial setup](/en/docs/initial-setup)
* [Intro to Claude](/en/docs/intro-to-claude)

##### Learn about Claude

* Use cases
* Models & pricing
* [Security and compliance](https://trust.anthropic.com/)

##### Build with Claude

* [Define success criteria](/en/docs/build-with-claude/define-success)
* [Develop test cases](/en/docs/build-with-claude/develop-tests)
* [Context windows](/en/docs/build-with-claude/context-windows)
* [Vision](/en/docs/build-with-claude/vision)
* Prompt engineering

  + [Overview](/en/docs/build-with-claude/prompt-engineering/overview)
  + [Prompt generator](/en/docs/build-with-claude/prompt-engineering/prompt-generator)
  + [Use prompt templates](/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables)
  + [Prompt improver](/en/docs/build-with-claude/prompt-engineering/prompt-improver)
  + [Be clear and direct](/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct)
  + [Use examples (multishot prompting)](/en/docs/build-with-claude/prompt-engineering/multishot-prompting)
  + [Let Claude think (CoT)](/en/docs/build-with-claude/prompt-engineering/chain-of-thought)
  + [Use XML tags](/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
  + [Give Claude a role (system prompts)](/en/docs/build-with-claude/prompt-engineering/system-prompts)
  + [Prefill Claude's response](/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)
  + [Chain complex prompts](/en/docs/build-with-claude/prompt-engineering/chain-prompts)
  + [Long context tips](/en/docs/build-with-claude/prompt-engineering/long-context-tips)
  + [Extended thinking tips](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips)
* [Extended thinking](/en/docs/build-with-claude/extended-thinking)
* [Multilingual support](/en/docs/build-with-claude/multilingual-support)
* Tool use (function calling)
* [Prompt caching](/en/docs/build-with-claude/prompt-caching)
* [PDF support](/en/docs/build-with-claude/pdf-support)
* [Citations](/en/docs/build-with-claude/citations)
* [Token counting](/en/docs/build-with-claude/token-counting)
* [Batch processing](/en/docs/build-with-claude/batch-processing)
* [Embeddings](/en/docs/build-with-claude/embeddings)

##### Agents and tools

* Claude Code
* [Computer use (beta)](/en/docs/agents-and-tools/computer-use)
* [Model Context Protocol (MCP)](/en/docs/agents-and-tools/mcp)
* [Google Sheets add-on](/en/docs/agents-and-tools/claude-for-sheets)

##### Test and evaluate

* Strengthen guardrails
* [Using the Evaluation Tool](/en/docs/test-and-evaluate/eval-tool)

##### Administration

* [Admin API](/en/docs/administration/administration-api)

##### Resources

* [Glossary](/en/docs/resources/glossary)
* [Model deprecations](/en/docs/resources/model-deprecations)
* [System status](https://status.anthropic.com/)
* [Claude 3 model card](https://assets.anthropic.com/m/61e7d27f8c8f5919/original/Claude-3-Model-Card.pdf)
* [Claude 3.7 system card](https://anthropic.com/claude-3-7-sonnet-system-card)
* [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
* [Anthropic Courses](https://github.com/anthropics/courses)
* [API features](/en/docs/resources/api-features)

##### Legal center

* [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)

While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).

When using Claude, you can dramatically improve its performance by using the `system` parameter to give it a role. This technique, known as role prompting, is the most powerful way to use system prompts with Claude.

The right role can turn Claude from a general assistant into your virtual domain expert!

**System prompt tips**: Use the `system` parameter to set Claude’s role. Put everything else, like task-specific instructions, in the `user` turn instead.

[​](#why-use-role-prompting) Why use role prompting?
----------------------------------------------------

* **Enhanced accuracy:** In complex scenarios like legal analysis or financial modeling, role prompting can significantly boost Claude’s performance.
* **Tailored tone:** Whether you need a CFO’s brevity or a copywriter’s flair, role prompting adjusts Claude’s communication style.
* **Improved focus:** By setting the role context, Claude stays more within the bounds of your task’s specific requirements.

[​](#how-to-give-claude-a-role) How to give Claude a role
---------------------------------------------------------

Use the `system` parameter in the [Messages API](/en/api/messages) to set Claude’s role:

```bash
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=2048,
    system="You are a seasoned data scientist at a Fortune 500 company.", # <-- role prompt
    messages=[
        {"role": "user", "content": "Analyze this dataset for anomalies: <dataset>{{DATASET}}</dataset>"}
    ]
)

print(response.content)
```

**Role prompting tip**: Experiment with roles! A `data scientist` might see different insights than a `marketing strategist` for the same data. A `data scientist specializing in customer insight analysis for Fortune 500 companies` might yield different results still!

[​](#examples) Examples
-----------------------

### [​](#example-1-legal-contract-analysis) Example 1: Legal contract analysis

Without a role, Claude might miss critical issues:

Legal contract analysis without role prompting

| Role | Content |
| --- | --- |
| User | Analyze this software licensing agreement for potential risks:<contract>{{CONTRACT}}</contract>Focus on indemnification, liability, and IP ownership. |
| Assistant | Here’s a summary of the key points in the software licensing agreement:1. Indemnification (Section 8): - We indemnify the vendor against claims arising from our use.2. Limitation of Liability (Section 9): - Damages capped at $500.3. IP Ownership (Section 12): - We retain ownership of our modifications.Overall, the agreement seems standard. The indemnification and liability clauses are typical, and we maintain our IP rights. |

With a role, Claude catches critical issues that could cost millions:

Legal contract analysis with role prompting

| Role | Content |
| --- | --- |
| User | You are the General Counsel of a Fortune 500 tech company. We’re considering this software licensing agreement for our core data infrastructure:<contract>{{CONTRACT}}</contract>Analyze it for potential risks, focusing on indemnification, liability, and IP ownership. Give your professional opinion. |
| Assistant | I’ve reviewed the software licensing agreement, and I have serious concerns that could expose our company to significant risks:1. Indemnification (Section 8): - Critical Issue: We indemnify the vendor against “any and all claims” arising from our use. - Risk: This could hold us liable even for the vendor’s negligence or product defects. - Recommendation: Reject. Limit our indemnity to claims arising from our violation of the agreement.2. Limitation of Liability (Section 9): - Critical Issue: Damages capped at $500, including direct damages. - Risk: Grossly inadequate. A critical failure in our data infrastructure could cost us millions in lost revenue and reputational damage. - Recommendation: Reject. Negotiate for cap at 12 months of fees for direct damages, and carve-outs for data breaches.3. IP Ownership (Section 12): - Critical Issue: Vendor gains joint ownership of our modifications and integrations. - Risk: They could use or sell our proprietary algorithms or data insights to competitors. - Recommendation: Reject. We must retain full ownership of our work.Professional Opinion: Do not sign this agreement. It is grossly unfavorable and exposes us to unacceptable levels of risk. If the vendor refuses to renegotiate these terms, I strongly advise exploring alternative providers or accelerating our in-house solution. The potential costs of proceeding with this agreement far outweigh any short-term gains. |

### [​](#example-2-financial-analysis) Example 2: Financial analysis

Without a role, Claude’s analysis lacks depth:

Financial analysis without role prompting

| Role | Content |
| --- | --- |
| User | Analyze this dataset of our Q2 financials:<data>{{FINANCIALS}}</data>Highlight key trends and recommend actions. |
| Assistant | Here’s a summary of your Q2 financials:1. Revenue: $15.2M, up 22% YoY. Enterprise client base grew 30%.2. Gross Margin: 72%, up 3% from Q1.3. EBITDA Margin: 18%, down 2% due to R&D investments.4. Cash Flow: $4.1M operating, $28M in reserves.Overall, financials look strong with revenue growth and healthy margins. Increased R&D spending is impacting profitability but could pay off long-term. Maintain current course. |

With a role, Claude delivers actionable insights:

Financial analysis with role prompting

| Role | Content |
| --- | --- |
| User | You are the CFO of a high-growth B2B SaaS company. We’re in a board meeting discussing our Q2 financials:<data>{{FINANCIALS}}</data>Analyze key trends, flag concerns, and recommend strategic actions. Our investors want aggressive growth but are wary of our burn rate. |
| Assistant | Board members, here’s my analysis of our Q2 financials:1. Revenue ($15.2M, +22% YoY): - Insight: Enterprise growth (+30%) is outpacing overall growth. - Flag: SMB segment declined 5%. - Action: Reallocate 20% of SMB marketing budget to enterprise sales. Task product to simplify SMB onboarding.2. Margins (Gross: 72%, +3% QoQ; EBITDA: 18%, -2% QoQ): - Insight: Infrastructure optimizations boosted gross margins. - Flag: R&D spend on AI features dented EBITDA. - Action: No change. Our AI roadmap is critical for enterprise stickiness.3. Cash ($4.1M OCF, $28M reserves): - Insight: 15-month runway at current burn. - Flag: CAC up 20%, eroding LTV/CAC. - Action: Freeze non-essential hires. Implement sales funnel analytics to cut CAC by 15% in Q3.Strategic Stance: We’re threading the needle between growth and burn. Enterprise focus is our growth engine—invest there. But watch SMB churn; it could bleed into enterprise. Our AI bet is sound, but we must convert it to ARR by Q4, or we cut R&D by 30%.In sum: Double down on enterprise, streamline SMB, optimize sales, and monetize AI. Questions? |

[Prompt library
--------------

Get inspired by a curated selection of prompts for various tasks and use cases.](/en/prompt-library/library)[GitHub prompting tutorial
-------------------------

An example-filled tutorial that covers the prompt engineering concepts found in our docs.](https://github.com/anthropics/prompt-eng-interactive-tutorial)[Google Sheets prompting tutorial
--------------------------------

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8)

Was this page helpful?

YesNo

[Use XML tags](/en/docs/build-with-claude/prompt-engineering/use-xml-tags)[Prefill Claude's response](/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

On this page

* [Why use role prompting?](#why-use-role-prompting)
* [How to give Claude a role](#how-to-give-claude-a-role)
* [Examples](#examples)
* [Example 1: Legal contract analysis](#example-1-legal-contract-analysis)
* [Example 2: Financial analysis](#example-2-financial-analysis)