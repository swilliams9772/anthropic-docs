---
title: 
source_url: https://docs.anthropic.com/en/docs/about-claude/models/all-models/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Models & pricing

All models overview

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

  + [All models overview](/en/docs/about-claude/models/all-models)
  + [Extended thinking models](/en/docs/about-claude/models/extended-thinking-models)
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

Introducing Claude 3.7 Sonnet- our most intelligent model yet. 3.7 Sonnet is the first hybrid [reasoning](/en/docs/build-with-claude/extended-thinking) model on the market. Learn more in our [blog post](http://www.anthropic.com/news/claude-3-7-sonnet).

[Claude 3.5 Haiku
----------------

Our fastest model

* Text and image input
* Text output
* 200k context window](/en/docs/about-claude/models/all-models#model-comparison-table)[Claude 3.7 Sonnet
-----------------

Our most intelligent model

* Text and image input
* Text output
* 200k context window
* [Extended thinking](en/docs/build-with-claude/extended-thinking)](/en/docs/about-claude/models/all-models#model-comparison-table)

[​](#model-names) Model names
-----------------------------

| Model | Anthropic API | AWS Bedrock | GCP Vertex AI |
| --- | --- | --- | --- |
| Claude 3.7 Sonnet | `claude-3-7-sonnet-20250219` (`claude-3-7-sonnet-latest`) | `anthropic.claude-3-7-sonnet-20250219-v1:0` | `claude-3-7-sonnet@20250219` |
| Claude 3.5 Haiku | `claude-3-5-haiku-20241022` (`claude-3-5-haiku-latest`) | `anthropic.claude-3-5-haiku-20241022-v1:0` | `claude-3-5-haiku@20241022` |

| Model | Anthropic API | AWS Bedrock | GCP Vertex AI |
| --- | --- | --- | --- |
| Claude 3.5 Sonnet v2 | `claude-3-5-sonnet-20241022` (`claude-3-5-sonnet-latest`) | `anthropic.claude-3-5-sonnet-20241022-v2:0` | `claude-3-5-sonnet-v2@20241022` |
| Claude 3.5 Sonnet | `claude-3-5-sonnet-20240620` | `anthropic.claude-3-5-sonnet-20240620-v1:0` | `claude-3-5-sonnet-v1@20240620` |
| Claude 3 Opus | `claude-3-opus-20240229` (`claude-3-opus-latest`) | `anthropic.claude-3-opus-20240229-v1:0` | `claude-3-opus@20240229` |
| Claude 3 Sonnet | `claude-3-sonnet-20240229` | `anthropic.claude-3-sonnet-20240229-v1:0` | `claude-3-sonnet@20240229` |
| Claude 3 Haiku | `claude-3-haiku-20240307` | `anthropic.claude-3-haiku-20240307-v1:0` | `claude-3-haiku@20240307` |

Models with the same snapshot date (e.g., 20240620) are identical across all platforms and do not change. The snapshot date in the model name ensures consistency and allows developers to rely on stable performance across different environments.

For convenience during development and testing, we offer “`-latest`” aliases for our models (e.g., `claude-3-7-sonnet-latest`). These aliases automatically point to the most recent snapshot of a given model. While useful for experimentation, we recommend using specific model versions (e.g., `claude-3-7-sonnet-20250219`) in production applications to ensure consistent behavior. When we release new model snapshots, we’ll migrate the -latest alias to point to the new version (typically within a week of the new release). The -latest alias is subject to the same rate limits and pricing as the underlying model version it references.

### [​](#model-comparison-table) Model comparison table

To help you choose the right model for your needs, we’ve compiled a table comparing the key features and capabilities of each model in the Claude family:

| Feature | Claude 3.7 Sonnet | Claude 3.5 Sonnet | Claude 3.5 Haiku | Claude 3 Opus | Claude 3 Haiku |
| --- | --- | --- | --- | --- | --- |
| **Description** | Our most intelligent model | Our previous most intelligent model | Our fastest model | Powerful model for complex tasks | Fastest and most compact model for near-instant responsiveness |
| **Strengths** | Highest level of intelligence and capability with toggleable extended thinking | High level of intelligence and capability | Intelligence at blazing speeds | Top-level intelligence, fluency, and understanding | Quick and accurate targeted performance |
| **Multilingual** | Yes | Yes | Yes | Yes | Yes |
| **Vision** | Yes | Yes | Yes | Yes | Yes |
| **[Extended thinking](/en/docs/build-with-claude/extended-thinking)** | Yes | No | No | No | No |
| **API model name** | `claude-3-7-sonnet-20250219` | **Upgraded version:** `claude-3-5-sonnet-20241022`**Previous version:** `claude-3-5-sonnet-20240620` | `claude-3-5-haiku-20241022` | `claude-3-opus-20240229` | `claude-3-haiku-20240307` |
| **Comparative latency** | Fast | Fast | Fastest | Moderately fast | Fastest |
| **Context window** | 200K | 200K | 200K | 200K | 200K |
| **Max output** | 64000 tokens | 8192 tokens | 8192 tokens | 4096 tokens | 4096 tokens |
| **Training data cut-off** | Nov 20241 | Apr 2024 | July 2024 | Aug 2023 | Aug 2023 |

*1 - While trained on publicly available information on the internet through November 2024, Claude 3.7 Sonnet’s knowledge cut-off date is the end of October 2024. This means the model’s knowledge base is most extensive and reliable on information and events up to October 2024.*

Include the beta header `output-128k-2025-02-19` in your API request to increase the maximum output token length to 128k tokens for Claude 3.7 Sonnet.

We strongly suggest using our [streaming Messages API](/en/api/messages-streaming) or [Batch API](/en/docs/build-with-claude/batch-processing) to avoid timeouts when generating longer outputs.
See our guidance on [long requests](/en/api/errors#long-requests) for more details.

### [​](#model-pricing) Model pricing

The table below shows the price per million tokens for each supported model:

| Model | Base Input Tokens | Cache Writes | Cache Hits | Output Tokens |
| --- | --- | --- | --- | --- |
| Claude 3.7 Sonnet | $3 / MTok | $3.75 / MTok | $0.30 / MTok | $15 / MTok |
| Claude 3.5 Sonnet | $3 / MTok | $3.75 / MTok | $0.30 / MTok | $15 / MTok |
| Claude 3.5 Haiku | $0.80 / MTok | $1 / MTok | $0.08 / MTok | $4 / MTok |
| Claude 3 Haiku | $0.25 / MTok | $0.30 / MTok | $0.03 / MTok | $1.25 / MTok |
| Claude 3 Opus | $15 / MTok | $18.75 / MTok | $1.50 / MTok | $75 / MTok |

[​](#prompt-and-output-performance) Prompt and output performance
-----------------------------------------------------------------

Claude 3.7 Sonnet excels in:

* **​Benchmark performance**: Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the [Claude 3.7 blog post](http://www.anthropic.com/news/claude-3-7-sonnet) for more information.
* **Engaging responses**: Claude models are ideal for applications that require rich, human-like interactions.

  + If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to our [prompt engineering guides](/en/docs/build-with-claude/prompt-engineering) for details.
* **Output quality**: When migrating from previous model generations to the Claude 3.7 Sonnet, you may notice larger improvements in overall performance.

[​](#get-started-with-claude) Get started with Claude
-----------------------------------------------------

If you’re ready to start exploring what Claude can do for you, let’s dive in! Whether you’re a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, we’ve got you covered.

Looking to chat with Claude? Visit [claude.ai](http://www.claude.ai)!

[Intro to Claude
---------------

Explore Claude’s capabilities and development flow.](/en/docs/intro-to-claude)[Quickstart
----------

Learn how to make your first API call in minutes.](/en/docs/quickstart)[Anthropic Console
-----------------

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)

If you have any questions or need assistance, don’t hesitate to reach out to our [support team](https://support.anthropic.com/) or consult the [Discord community](https://www.anthropic.com/discord).

Was this page helpful?

YesNo

[Legal summarization](/en/docs/about-claude/use-case-guides/legal-summarization)[Extended thinking models](/en/docs/about-claude/models/extended-thinking-models)

On this page

* [Model names](#model-names)
* [Model comparison table](#model-comparison-table)
* [Model pricing](#model-pricing)
* [Prompt and output performance](#prompt-and-output-performance)
* [Get started with Claude](#get-started-with-claude)