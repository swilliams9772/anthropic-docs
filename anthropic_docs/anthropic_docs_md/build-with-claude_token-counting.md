---
title: 
source_url: https://docs.anthropic.com/en/docs/build-with-claude/token-counting/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Build with Claude

Token counting

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

Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. With token counting, you can

* Proactively manage rate limits and costs
* Make smart model routing decisions
* Optimize prompts to be a specific length

[​](#how-to-count-message-tokens) How to count message tokens
-------------------------------------------------------------

The [token counting](/en/api/messages-count-tokens) endpoint accepts the same structured list of inputs for creating a message, including support for system prompts, [tools](/en/docs/build-with-claude/tool-use), [images](/en/docs/build-with-claude/vision), and [PDFs](/en/docs/build-with-claude/pdf-support). The response contains the total number of input tokens.

The token count should be considered an **estimate**. In some cases, the actual number of input tokens used when creating a message may differ by a small amount.

### [​](#supported-models) Supported models

The token counting endpoint supports the following models:

* Claude 3.7 Sonnet
* Claude 3.5 Sonnet
* Claude 3.5 Haiku
* Claude 3 Haiku
* Claude 3 Opus

### [​](#count-tokens-in-basic-messages) Count tokens in basic messages

JSON

```json
{ "input_tokens": 14 }
```

### [​](#count-tokens-in-messages-with-tools) Count tokens in messages with tools

JSON

```json
{ "input_tokens": 403 }
```

### [​](#count-tokens-in-messages-with-images) Count tokens in messages with images

JSON

```json
{ "input_tokens": 1551 }
```

### [​](#count-tokens-in-messages-with-extended-thinking) Count tokens in messages with extended thinking

See [here](/en/docs/build-with-claude/extended-thinking#how-context-window-is-calculated-with-extended-thinking) for more details about how the context window is calculated with extended thinking

* Thinking blocks from **previous** assistant turns are ignored and **do not** count toward your input tokens
* **Current** assistant turn thinking **does** count toward your input tokens

JSON

```json
{ "input_tokens": 88 }
```

### [​](#count-tokens-in-messages-with-pdfs) Count tokens in messages with PDFs

Token counting supports PDFs with the same [limitations](/en/docs/build-with-claude/pdf-support#pdf-support-limitations) as the Messages API.

JSON

```json
{ "input_tokens": 2188 }
```

[​](#pricing-and-rate-limits) Pricing and rate limits
-----------------------------------------------------

Token counting is **free to use** but subject to requests per minute rate limits based on your [usage tier](https://docs.anthropic.com/en/api/rate-limits#rate-limits). If you need higher limits, contact sales through the [Anthropic Console](https://console.anthropic.com/settings/limits).

| Usage tier | Requests per minute (RPM) |
| --- | --- |
| 1 | 100 |
| 2 | 2,000 |
| 3 | 4,000 |
| 4 | 8,000 |

Token counting and message creation have separate and independent rate limits — usage of one does not count against the limits of the other.

[​](#faq) FAQ
-------------

Does token counting use prompt caching?

No, token counting provides an estimate without using caching logic. While you may provide `cache_control` blocks in your token counting request, prompt caching only occurs during actual message creation.

Was this page helpful?

YesNo

[Citations](/en/docs/build-with-claude/citations)[Batch processing](/en/docs/build-with-claude/batch-processing)

On this page

* [How to count message tokens](#how-to-count-message-tokens)
* [Supported models](#supported-models)
* [Count tokens in basic messages](#count-tokens-in-basic-messages)
* [Count tokens in messages with tools](#count-tokens-in-messages-with-tools)
* [Count tokens in messages with images](#count-tokens-in-messages-with-images)
* [Count tokens in messages with extended thinking](#count-tokens-in-messages-with-extended-thinking)
* [Count tokens in messages with PDFs](#count-tokens-in-messages-with-pdfs)
* [Pricing and rate limits](#pricing-and-rate-limits)
* [FAQ](#faq)