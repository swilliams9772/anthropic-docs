---
title: 
source_url: https://docs.anthropic.com/en/docs/resources/api-features/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Resources

API feature overview

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

[​](#batch-processing) Batch processing
---------------------------------------

Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Each batch is processed in less than 24 hours and costs 50% less than standard API calls. [Learn more](/en/api/creating-message-batches).

**Available on:**

* Anthropic API
* Amazon Bedrock
* Google Cloud’s Vertex AI

[​](#citations) Citations
-------------------------

Ground Claude’s responses in source documents. With Citations, Claude can provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs. [Learn more](/en/docs/build-with-claude/citations).

**Available on:**

* Anthropic API
* Google Cloud’s Vertex AI

[​](#computer-use-public-beta) Computer use (public beta)
---------------------------------------------------------

Computer use is Claude’s ability to perform tasks by interpreting screenshots and automatically generating the necessary computer commands (like mouse movements and keystrokes). [Learn more](/en/docs/agents-and-tools/computer-use).

**Available on:**

* Anthropic API
* Amazon Bedrock
* Google Cloud’s Vertex AI

[​](#pdf-support) PDF support
-----------------------------

Process and analyze text and visual content from PDF documents. [Learn more](/en/docs/build-with-claude/pdf-support).

**Available on:**

* Anthropic API
* Google Cloud’s Vertex AI

[​](#prompt-caching) Prompt caching
-----------------------------------

Provide Claude with more background knowledge and example outputs to reduce costs by up to 90% and latency by up to 85% for long prompts. [Learn more](/en/docs/build-with-claude/prompt-caching).

**Available on:**

* Anthropic API
* Amazon Bedrock
* Google Cloud’s Vertex AI

[​](#token-counting) Token counting
-----------------------------------

Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. [Learn more](/en/api/messages-count-tokens).

**Available on:**

* Anthropic API
* Google Cloud’s Vertex AI

[​](#tool-use) Tool use
-----------------------

Enable Claude to interact with external tools and APIs to perform a wider variety of tasks. [Learn more](/en/docs/build-with-claude/tool-use/overview).

**Available on:**

* Anthropic API
* Amazon Bedrock
* Google Cloud’s Vertex AI

Was this page helpful?

YesNo

[Anthropic Courses](/en/docs/resources/courses)[Anthropic Privacy Policy](/en/docs/legal-center/privacy)

On this page

* [Batch processing](#batch-processing)
* [Citations](#citations)
* [Computer use (public beta)](#computer-use-public-beta)
* [PDF support](#pdf-support)
* [Prompt caching](#prompt-caching)
* [Token counting](#token-counting)
* [Tool use](#tool-use)