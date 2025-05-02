---
title: 
source_url: https://docs.anthropic.com/en/docs/build-with-claude/context-windows/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Build with Claude

Context windows

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

[​](#understanding-the-context-window) Understanding the context window
-----------------------------------------------------------------------

The “context window” refers to the entirety of the amount of text a language model can look back on and reference when generating new text plus the new text it generates. This is different from the large corpus of data the language model was trained on, and instead represents a “working memory” for the model. A larger context window allows the model to understand and respond to more complex and lengthy prompts, while a smaller context window may limit the model’s ability to handle longer prompts or maintain coherence over extended conversations.

The diagram below illustrates the standard context window behavior for API requests1:

*1For chat interfaces, such as for [claude.ai](https://claude.ai/), context windows can also be set up on a rolling “first in, first out” system.*

* **Progressive token accumulation:** As the conversation advances through turns, each user message and assistant response accumulates within the context window. Previous turns are preserved completely.
* **Linear growth pattern:** The context usage grows linearly with each turn, with previous turns preserved completely.
* **200K token capacity:** The total available context window (200,000 tokens) represents the maximum capacity for storing conversation history and generating new output from Claude.
* **Input-output flow:** Each turn consists of:
  + **Input phase:** Contains all previous conversation history plus the current user message
  + **Output phase:** Generates a text response that becomes part of a future input

[​](#the-context-window-with-extended-thinking) The context window with extended thinking
-----------------------------------------------------------------------------------------

When using [extended thinking](/en/docs/build-with-claude/extended-thinking), all input and output tokens, including the tokens used for thinking, count toward the context window limit, with a few nuances in multi-turn situations.

The thinking budget tokens are a subset of your `max_tokens` parameter, are billed as output tokens, and count towards rate limits.

However, previous thinking blocks are automatically stripped from the context window calculation by the Anthropic API and are not part of the conversation history that the model “sees” for subsequent turns, preserving token capacity for actual conversation content.

The diagram below demonstrates the specialized token management when extended thinking is enabled:

* **Stripping extended thinking:** Extended thinking blocks (shown in dark gray) are generated during each turn’s output phase, **but are not carried forward as input tokens for subsequent turns**. You do not need to strip the thinking blocks yourself. The Anthropic API automatically does this for you if you pass them back.
* **Technical implementation details:**
  + The API automatically excludes thinking blocks from previous turns when you pass them back as part of the conversation history.
  + Extended thinking tokens are billed as output tokens only once, during their generation.
  + The effective context window calculation becomes: `context_window = (input_tokens - previous_thinking_tokens) + current_turn_tokens`.
  + Thinking tokens include both `thinking` blocks and `redacted_thinking` blocks.

This architecture is token efficient and allows for extensive reasoning without token waste, as thinking blocks can be substantial in length.

You can read more about the context window and extended thinking in our [extended thinking guide](/en/docs/build-with-claude/extended-thinking).

[​](#the-context-window-with-extended-thinking-and-tool-use) The context window with extended thinking and tool use
-------------------------------------------------------------------------------------------------------------------

The diagram below illustrates the context window token management when combining extended thinking with tool use:

1

First turn architecture

* **Input components:** Tools configuration and user message
* **Output components:** Extended thinking + text response + tool use request
* **Token calculation:** All input and output components count toward the context window, and all output components are billed as output tokens.

2

Tool result handling (turn 2)

* **Input components:** Every block in the first turn as well as the `tool_result`. The extended thinking block **must** be returned with the corresponding tool results. This is the only case wherein you **have to** return thinking blocks.
* **Output components:** After tool results have been passed back to Claude, Claude will respond with only text (no additional extended thinking until the next `user` message).
* **Token calculation:** All input and output components count toward the context window, and all output components are billed as output tokens.

3

Third Step

* **Input components:** All inputs and the output from the previous turn is carried forward with the exception of the thinking block, which can be dropped now that Claude has completed the entire tool use cycle. The API will automatically strip the thinking block for you if you pass it back, or you can feel free to strip it yourself at this stage. This is also where you would add the next `User` turn.
* **Output components:** Since there is a new `User` turn outside of the tool use cycle, Claude will generate a new extended thinking block and continue from there.
* **Token calculation:** Previous thinking tokens are automatically stripped from context window calculations. All other previous blocks still count as part of the token window, and the thinking block in the current `Assistant` turn counts as part of the context window.

* **Considerations for tool use with extended thinking:**
  + When posting tool results, the entire unmodified thinking block that accompanies that specific tool request (including signature/redacted portions) must be included.
  + The system uses cryptographic signatures to verify thinking block authenticity. Failing to preserve thinking blocks during tool use can break Claude’s reasoning continuity. Thus, if you modify thinking blocks, the API will return an error.

There is no interleaving of extended thinking and tool calls - you won’t see extended thinking, then tool calls, then more extended thinking, without a non-`tool_result` user turn in between. Additionally, tool use within the extended thinking block itself is not currently supported, although Claude may reason about what tools it should use and how to call them within the thinking block.

You can read more about tool use with extended thinking [in our extended thinking guide](/en/docs/build-with-claude/extended-thinking#extended-thinking-with-tool-use)

### [​](#context-window-management-with-newer-claude-models) Context window management with newer Claude models

In newer Claude models (starting with Claude 3.7 Sonnet), if the sum of prompt tokens and output tokens exceeds the model’s context window, the system will return a validation error rather than silently truncating the context. This change provides more predictable behavior but requires more careful token management.

To plan your token usage and ensure you stay within context window limits, you can use the [token counting API](/en/docs/build-with-claude/token-counting) to estimate how many tokens your messages will use before sending them to Claude.

See our [model comparison](/en/docs/models-overview#model-comparison) table for a list of context window sizes by model.

[​](#next-steps) Next steps
===========================

[Model comparison table
----------------------

See our model comparison table for a list of context window sizes and input / output token pricing by model.](/en/docs/models-overview#model-comparison)[Extended thinking overview
--------------------------

Learn more about how extended thinking works and how to implement it alongside other features such as tool use and prompt caching.](/en/docs/build-with-claude/extended-thinking)

Was this page helpful?

YesNo

[Develop test cases](/en/docs/build-with-claude/develop-tests)[Vision](/en/docs/build-with-claude/vision)

On this page

* [Understanding the context window](#understanding-the-context-window)
* [The context window with extended thinking](#the-context-window-with-extended-thinking)
* [The context window with extended thinking and tool use](#the-context-window-with-extended-thinking-and-tool-use)
* [Context window management with newer Claude models](#context-window-management-with-newer-claude-models)
* [Next steps](#next-steps)