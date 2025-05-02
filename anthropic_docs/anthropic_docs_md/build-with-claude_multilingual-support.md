---
title: 
source_url: https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Build with Claude

Multilingual support

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

[​](#overview) Overview
-----------------------

Claude demonstrates robust multilingual capabilities, with particularly strong performance in zero-shot tasks across languages. The model maintains consistent relative performance across both widely-spoken and lower-resource languages, making it a reliable choice for multilingual applications.

Note that Claude is capable in many languages beyond those benchmarked below. We encourage testing with any languages relevant to your specific use cases.

[​](#performance-data) Performance data
---------------------------------------

Below are the zero-shot chain-of-thought evaluation scores for Claude 3.7 Sonnet and Claude 3.5 models across different languages, shown as a percent relative to English performance (100%):

| Language | Claude 3.7 Sonnet1 | Claude 3.5 Sonnet (New) | Claude 3.5 Haiku |
| --- | --- | --- | --- |
| English (baseline, fixed to 100%) | 100% | 100% | 100% |
| Spanish | 97.6% | 96.9% | 94.6% |
| Portuguese (Brazil) | 97.3% | 96.0% | 94.6% |
| Italian | 97.2% | 95.6% | 95.0% |
| French | 96.9% | 96.2% | 95.3% |
| Indonesian | 96.3% | 94.0% | 91.2% |
| German | 96.2% | 94.0% | 92.5% |
| Arabic | 95.4% | 92.5% | 84.7% |
| Chinese (Simplified) | 95.3% | 92.8% | 90.9% |
| Korean | 95.2% | 92.8% | 89.1% |
| Japanese | 95.0% | 92.7% | 90.8% |
| Hindi | 94.2% | 89.3% | 80.1% |
| Bengali | 92.4% | 85.9% | 72.9% |
| Swahili | 89.2% | 83.9% | 64.7% |
| Yoruba | 76.7% | 64.9% | 46.1% |

1 With [extended thinking](/en/docs/build-with-claude/extended-thinking) and 16,000 `budget_tokens`.

These metrics are based on [MMLU (Massive Multitask Language Understanding)](https://en.wikipedia.org/wiki/MMLU) English test sets that were translated into 14 additional languages by professional human translators, as documented in [OpenAI’s simple-evals repository](https://github.com/openai/simple-evals/blob/main/multilingual_mmlu_benchmark_results.md). The use of human translators for this evaluation ensures high-quality translations, particularly important for languages with fewer digital resources.

[​](#best-practices) Best practices
-----------------------------------

When working with multilingual content:

1. **Provide clear language context**: While Claude can detect the target language automatically, explicitly stating the desired input/output language improves reliability. For enhanced fluency, you can prompt Claude to use “idiomatic speech as if it were a native speaker.”
2. **Use native scripts**: Submit text in its native script rather than transliteration for optimal results
3. **Consider cultural context**: Effective communication often requires cultural and regional awareness beyond pure translation

We also suggest following our general [prompt engineering guidelines](/en/docs/build-with-claude/prompt-engineering/overview) to better improve Claude’s performance.

[​](#language-support-considerations) Language support considerations
---------------------------------------------------------------------

* Claude processes input and generates output in most world languages that use standard Unicode characters
* Performance varies by language, with particularly strong capabilities in widely-spoken languages
* Even in languages with fewer digital resources, Claude maintains meaningful capabilities

[Prompt Engineering Guide
------------------------

Master the art of prompt crafting to get the most out of Claude.](/en/docs/build-with-claude/prompt-engineering/overview)[Prompt Library
--------------

Find a wide range of pre-crafted prompts for various tasks and industries. Perfect for inspiration or quick starts.](/en/prompt-library)

Was this page helpful?

YesNo

[Extended thinking](/en/docs/build-with-claude/extended-thinking)[Overview](/en/docs/build-with-claude/tool-use/overview)

On this page

* [Overview](#overview)
* [Performance data](#performance-data)
* [Best practices](#best-practices)
* [Language support considerations](#language-support-considerations)