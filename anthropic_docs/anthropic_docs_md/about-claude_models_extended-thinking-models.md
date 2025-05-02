---
title: 
source_url: https://docs.anthropic.com/en/docs/about-claude/models/extended-thinking-models/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Models & pricing

Extended thinking models

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

Claude 3.7 Sonnet is a hybrid model capable of both standard thinking as well as extended thinking modes. In standard mode, Claude 3.7 Sonnet operates similarly to other models in the Claude 3 family. In extended thinking mode, Claude will output its thinking before outputting its response, allowing you insight into its reasoning process.

[​](#claude-3-7-overview) Claude 3.7 overview
---------------------------------------------

Claude 3.7 Sonnet operates in two modes:

* **Standard mode**: Similar to previous Claude models, providing direct responses without showing internal reasoning
* **Extended thinking mode**: Shows Claude’s reasoning process before delivering the final answer

### [​](#when-to-use-standard-mode) When to use standard mode

Standard mode works well for most general use cases, including:

* General content generation
* Basic coding assistance
* Routine agentic tasks
* Computer use guidance
* Most conversational applications

### [​](#when-to-use-extended-thinking-mode) When to use extended thinking mode

Extended thinking mode excels in these key areas:

* **Complex analysis**: Financial, legal, or data analysis involving multiple parameters and factors
* **Advanced STEM problems**: Mathematics, physics, research & development
* **Long context handling**: Processing and synthesizing information from extensive inputs
* **Constraint optimization**: Problems with multiple competing requirements
* **Detailed data generation**: Creating comprehensive tables or structured information sets
* **Complex instruction following**: Chatbots with intricate system prompts and many factors to consider
* **Structured creative tasks**: Creative writing requiring detailed planning, outlines, or managing multiple narrative elements

To learn more about how extended thinking works, see [Extended thinking](/en/docs/build-with-claude/extended-thinking).

[​](#getting-started-with-claude-3-7-sonnet) Getting started with Claude 3.7 Sonnet
-----------------------------------------------------------------------------------

If you are trying Claude 3.7 Sonnet for the first time, here are some tips:

1. **Start with standard mode**: Begin by using Claude 3.7 Sonnet without extended thinking to establish a baseline performance
2. **Identify improvement opportunities**: Try turning on extended thinking mode at a low budget to see if your use case would benefit from deeper reasoning. It might be the case that your use case would benefit more from more detailed prompting in standard mode rather than extended thinking from Claude.
3. **Gradual implementation**: If needed, incrementally increase the thinking budget while testing performance against your requirements.
4. **Optimize token usage**: Once you reach acceptable performance, set appropriate token limits to manage costs.
5. **Explore new possibilities**: Claude 3.7 Sonnet, with and without extended thinking, is more capable than previous Claude models in a variety of domains. We encourage you to try Claude 3.7 Sonnet for use cases where you previously experienced limitations with other models.

[​](#building-on-claude-3-7-sonnet) Building on Claude 3.7 Sonnet
-----------------------------------------------------------------

### [​](#general-model-information) General model information

For pricing, context window size, and other information on Claude 3.7 Sonnet and all other current Claude models, see [All models overview](/en/docs/about-claude/models/all-models).

### [​](#max-tokens-and-context-window-changes-with-claude-3-7-sonnet) Max tokens and context window changes with Claude 3.7 Sonnet

In older Claude models (prior to Claude 3.7 Sonnet), if the sum of prompt tokens and `max_tokens` exceeded the model’s context window, the system would automatically adjust `max_tokens` to fit within the context limit. This meant you could set a large `max_tokens` value and the system would silently reduce it as needed.

With Claude 3.7 Sonnet, `max_tokens` (which includes your thinking budget when thinking is enabled) is enforced as a strict limit. The system will now return a validation error if prompt tokens + `max_tokens` exceeds the context window size.

### [​](#extended-output-capabilities-beta) Extended output capabilities (beta)

Claude 3.7 Sonnet can also produce substantially longer responses than previous models with support for up to 128K output tokens (beta)—more than 15x longer than other Claude models. This expanded capability is particularly effective for extended thinking use cases involving complex reasoning, rich code generation, and comprehensive content creation.

This feature can be enabled by passing an `anthropic-beta` header of `output-128k-2025-02-19`.

When using extended thinking with longer outputs, you can allocate a larger thinking budget to support more thorough reasoning, while still having ample tokens available for the final response.

[​](#migrating-to-claude-3-7-sonnet-from-other-models) Migrating to Claude 3.7 Sonnet from other models
-------------------------------------------------------------------------------------------------------

If you are transferring prompts from another model, whether another Claude model or from another model provider, here are some tips:

### [​](#standard-mode-migration) Standard mode migration

* **Simplify your prompts**: Claude 3.7 Sonnet requires less steering. Remove any model-specific guidance language you’ve used with previous versions, such as language around handling verbosity - such language is likely unnecessary and will save tokens and reduce costs.

Otherwise, generally no prompt changes are needed if you’re using Claude 3.7 Sonnet with extended thinking turned off. If you encounter issues, apply general [prompt engineering best practices](/en/docs/build-with-claude/prompt-engineering/overview).

### [​](#extended-thinking-mode-migration) Extended thinking mode migration

When using extended thinking, start by removing all chain-of-thought (CoT) guidance from your prompts. Claude 3.7 Sonnet’s thinking capability is designed to work effectively without explicit reasoning instructions.

* Instead of prescribing thinking patterns, observe Claude’s natural thinking process first, then adjust your prompts based on what you see.
* If you then want to provide thinking guidance, you can include guidance in natural language in your prompt and Claude will be able to generalize such instructions into its own thinking.
* For more tips on how to prompt for extended thinking, see [Extended thinking tips](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).

### [​](#migrating-from-other-model-providers) Migrating from other model providers

Claude 3.7 Sonnet may respond differently to prompting patterns optimized for other providers’ models. We recommend focusing on clear, direct instructions rather than provider-specific prompting techniques. Removing such instructions tailored for specific model providers may lead to better performance, as Claude is generally good at complex instruction following out of the box.

You can use our optimized prompt improver at [console.anthropic.com](https://console.anthropic.com) for assistance with migrating prompts.

[​](#next-steps) Next steps
---------------------------

[Try the extended thinking cookbook
----------------------------------

Explore practical examples of thinking in our cookbook.](https://github.com/anthropics/anthropic-cookbook/tree/main/extended_thinking)[Extended thinking documentation
-------------------------------

Learn more about how extended thinking works and how to implement it alongside other features such as tool use and prompt caching.](/en/docs/build-with-claude/extended-thinking)

Was this page helpful?

YesNo

[All models overview](/en/docs/about-claude/models/all-models)[Security and compliance](/en/docs/about-claude/security-compliance)

On this page

* [Claude 3.7 overview](#claude-3-7-overview)
* [When to use standard mode](#when-to-use-standard-mode)
* [When to use extended thinking mode](#when-to-use-extended-thinking-mode)
* [Getting started with Claude 3.7 Sonnet](#getting-started-with-claude-3-7-sonnet)
* [Building on Claude 3.7 Sonnet](#building-on-claude-3-7-sonnet)
* [General model information](#general-model-information)
* [Max tokens and context window changes with Claude 3.7 Sonnet](#max-tokens-and-context-window-changes-with-claude-3-7-sonnet)
* [Extended output capabilities (beta)](#extended-output-capabilities-beta)
* [Migrating to Claude 3.7 Sonnet from other models](#migrating-to-claude-3-7-sonnet-from-other-models)
* [Standard mode migration](#standard-mode-migration)
* [Extended thinking mode migration](#extended-thinking-mode-migration)
* [Migrating from other model providers](#migrating-from-other-model-providers)
* [Next steps](#next-steps)