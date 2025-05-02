---
title: 
source_url: https://docs.anthropic.com/en/docs/resources/model-deprecations/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Resources

Model deprecations

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

As we launch safer and more capable models, we regularly retire older models. Applications relying on Anthropic models may need occasional updates to keep working. Impacted customers will always be notified by email and in our documentation.

This page lists all API deprecations, along with recommended replacements.

[​](#overview) Overview
-----------------------

Anthropic uses the following terms to describe the lifecycle of our models:

* **Active**: The model is fully supported and recommended for use.
* **Legacy**: The model will no longer receive updates and may be deprecated in the future.
* **Deprecated**: The model is no longer available for new customers but continues to be available for existing users until retirement. We assign a retirement date at this point.
* **Retired**: The model is no longer available for use. Requests to retired models will fail.

[​](#migrating-to-replacements) Migrating to replacements
---------------------------------------------------------

Once a model is deprecated, please migrate all usage to a suitable replacement before the retirement date. Requests to models past the retirement date will fail.

To help measure the performance of replacement models on your tasks, we recommend thorough testing of your applications with the new models well before the retirement date.

[​](#notifications) Notifications
---------------------------------

Anthropic notifies customers with active deployments for models with upcoming retirements. We provide at least 6 months† notice before model retirement for publicly released models.

[​](#auditing-model-usage) Auditing model usage
-----------------------------------------------

To help identify usage of deprecated models, customers can access an audit of their API usage. Follow these steps:

1. Go to <https://console.anthropic.com/settings/usage>
2. Click the “Export” button
3. Review the downloaded CSV to see usage broken down by API key and model

This audit will help you locate any instances where your application is still using deprecated models, allowing you to prioritize updates to newer models before the retirement date.

[​](#model-status) Model status
-------------------------------

All publicly released models are listed below with their status:

| API Model Name | Current State | Deprecated | Retired |
| --- | --- | --- | --- |
| `claude-1.0` | Retired | September 4, 2024 | November 6, 2024 |
| `claude-1.1` | Retired | September 4, 2024 | November 6, 2024 |
| `claude-1.2` | Retired | September 4, 2024 | November 6, 2024 |
| `claude-1.3` | Retired | September 4, 2024 | November 6, 2024 |
| `claude-instant-1.0` | Retired | September 4, 2024 | November 6, 2024 |
| `claude-instant-1.1` | Retired | September 4, 2024 | November 6, 2024 |
| `claude-instant-1.2` | Retired | September 4, 2024 | November 6, 2024 |
| `claude-2.0` | Deprecated | January 21, 2025 | N/A |
| `claude-2.1` | Deprecated | January 21, 2025 | N/A |
| `claude-3-sonnet-20240229` | Deprecated | January 21, 2025 | N/A |
| `claude-3-haiku-20240307` | Active | N/A | N/A |
| `claude-3-opus-20240229` | Active | N/A | N/A |
| `claude-3-5-sonnet-20240620` | Active | N/A | N/A |
| `claude-3-5-haiku-20241022` | Active | N/A | N/A |
| `claude-3-5-sonnet-20241022` | Active | N/A | N/A |
| `claude-3-7-sonnet-20250219` | Active | N/A | N/A |

[​](#deprecation-history) Deprecation history
---------------------------------------------

All deprecations are listed below, with the most recent announcements at the top.

### [​](#2025-01-21-claude-2-claude-2-1-and-claude-3-sonnet-models) 2025-01-21: Claude 2, Claude 2.1, and Claude 3 Sonnet models

On January 21, 2025, we notified developers using Claude 2, Claude 2.1, and Claude 3 Sonnet models of their upcoming retirements.

| Retirement Date | Deprecated Model | Recommended Replacement |
| --- | --- | --- |
| July 21, 2025 | `claude-2.0` | `claude-3-5-sonnet-20241022` |
| July 21, 2025 | `claude-2.1` | `claude-3-5-sonnet-20241022` |
| July 21, 2025 | `claude-3-sonnet-20240229` | `claude-3-5-sonnet-20241022` |

### [​](#2024-09-04-claude-1-and-instant-models) 2024-09-04: Claude 1 and Instant models

On September 4, 2024, we notified developers using Claude 1 and Instant models of their upcoming retirements.

| Retirement Date | Deprecated Model | Recommended Replacement |
| --- | --- | --- |
| November 6, 2024 | `claude-1.0` | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-1.1` | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-1.2` | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-1.3` | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-instant-1.0` | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-instant-1.1` | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-instant-1.2` | `claude-3-5-haiku-20241022` |

[​](#best-practices) Best practices
-----------------------------------

1. Regularly check our documentation for updates on model deprecations.
2. Test your applications with newer models well before the retirement date of your current model.
3. Update your code to use the recommended replacement model as soon as possible.
4. Contact our support team if you need assistance with migration or have any questions.

† The Claude 1 family of models have a 60-day notice period due to their limited usage compared to our newer models.

Was this page helpful?

YesNo

[Glossary](/en/docs/resources/glossary)[System status](/en/docs/resources/status)

On this page

* [Overview](#overview)
* [Migrating to replacements](#migrating-to-replacements)
* [Notifications](#notifications)
* [Auditing model usage](#auditing-model-usage)
* [Model status](#model-status)
* [Deprecation history](#deprecation-history)
* [2025-01-21: Claude 2, Claude 2.1, and Claude 3 Sonnet models](#2025-01-21-claude-2-claude-2-1-and-claude-3-sonnet-models)
* [2024-09-04: Claude 1 and Instant models](#2024-09-04-claude-1-and-instant-models)
* [Best practices](#best-practices)