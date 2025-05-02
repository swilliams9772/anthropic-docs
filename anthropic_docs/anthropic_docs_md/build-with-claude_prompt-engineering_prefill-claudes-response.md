---
title: 
source_url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Prompt engineering

Prefill Claude's response for greater output control

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

Prefilling is only available for non-extended thinking modes. It’s not currently supported with extended thinking.

When using Claude, you have the unique ability to guide its responses by prefilling the `Assistant` message. This powerful technique allows you to direct Claude’s actions, skip preambles, enforce specific formats like JSON or XML, and even help Claude maintain character consistency in role-play scenarios.

In some cases where Claude is not performing as expected, a few prefilled sentences can vastly improve Claude’s performance. A little prefilling goes a long way!

[​](#how-to-prefill-claudes-response) How to prefill Claude’s response
----------------------------------------------------------------------

To prefill, include the desired initial text in the `Assistant` message (Claude’s response will continue from where the `Assistant` message leaves off):

```bash
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is your favorite color?"},
        {"role": "assistant", "content": "As an AI assistant, I don't have a favorite color, But if I had to pick, it would be green because"}  # Prefill here
    ]
)
```

The prefill content cannot end with trailing whitespace. A prefill like `"As an AI assistant, I "` (with a space at the end) will result in an error.

### [​](#examples) Examples

#### [​](#example-1-controlling-output-formatting-and-skipping-the-preamble) Example 1: Controlling output formatting and skipping the preamble

**Power user tip**: Prefilling `{` forces Claude to skip the preamble and directly output the JSON object. This is cleaner, more concise, and easier for programs to parse without additional processing.

Example: Structured data extraction without prefilling

| Role | Content |
| --- | --- |
| User | Extract the name, size, price, and color from this product description as a JSON object:<description>The SmartHome Mini is a compact smart home assistant available in black or white for only $49.99. At just 5 inches wide, it lets you control lights, thermostats, and other connected devices via voice or app—no matter where you place it in your home. This affordable little hub brings convenient hands-free control to your smart devices.</description> |
| Assistant | Here’s the extracted information in JSON format:```json{ “name”: “SmartHome Mini”, “size”: “5 inches wide”, “price”: “$49.99”, “colors”: [“black”, “white”]}```I’ve extracted the following details from the product description:- **Name**: SmartHome Mini- **Size**: 5 inches wide- **Price**: $49.99- **Colors**: Available in black and whiteThe JSON object provides a structured format that’s easy for programs to parse and use. Let me know if you need any modifications or have any other questions! |

Example: Structured data extraction with prefilling

| Role | Content |
| --- | --- |
| User | Extract the name, size, price, and color from this product description as a JSON object:<description>The SmartHome Mini is a compact smart home assistant available in black or white for only $49.99. At just 5 inches wide, it lets you control lights, thermostats, and other connected devices via voice or app—no matter where you place it in your home. This affordable little hub brings convenient hands-free control to your smart devices.</description> |
| Assistant (prefill) | { |
| Assistant (Claude’s response) | “name”: “SmartHome Mini”,“size”: “5 inches wide”,“price”: “$49.99”,“colors”: [ “black”, “white”]} |

#### [​](#example-2-maintaining-character-in-roleplay-scenarios) Example 2: Maintaining character in roleplay scenarios

**Role-play tip**: Prefilling a bracketed `[ROLE_NAME]` can remind Claude stay in character, even for longer and more complex conversations. This is especially powerful when combined with role prompting in the `system` parameter.

Example: Maintaining character without role prompting

| Role | Content |
| --- | --- |
| User (50 conversation turns in with “Sherlock Holmes” Claude) | What do you deduce about the owner of this shoe? <image>muddy\_shoe.jpg</image> |
| Assistant | As an AI assistant, I would be happy to analyze the image of a muddy shoe as if you had provided it. Here’s my deduction… |

Example: Maintaining character with role prompting

| Role | Content |
| --- | --- |
| User (50 conversation turns in with “Sherlock Holmes” Claude) | What do you deduce about the owner of this shoe? <image>muddy\_shoe.jpg</image> |
| Assistant (prefill) | [Sherlock Holmes] |
| Assistant (Claude’s response) | Ah, what have we here? A most curious specimen, Watson! Let us examine this shoe with a discerning eye. The mud, you see, is not your common London clay, but rather the distinctive reddish hue of the iron-rich soil found only in the environs of Hampstead Heath. And yet, the wear on the sole suggests a gait more suited to the cobblestones of Whitechapel than the gentle slopes of the Heath.Now, observe the laces! They are tied with a particular knot favored by those in the medical profession—doubtless a habit acquired during years of tying surgical gowns. But the scuff marks on the toe box tell a different tale: they are consistent with the kicking motion one might employ in the martial arts, specifically Baritsu.We may conclude, then, that our absent shoe owner is a doctor, possibly a surgeon, who resides in Whitechapel but frequents Hampstead Heath—perhaps for a secret Baritsu practice, away from prying eyes. A most intriguing case, Watson! We must make haste; the game is afoot! |

[Prompt library
--------------

Get inspired by a curated selection of prompts for various tasks and use cases.](/en/prompt-library/library)[GitHub prompting tutorial
-------------------------

An example-filled tutorial that covers the prompt engineering concepts found in our docs.](https://github.com/anthropics/prompt-eng-interactive-tutorial)[Google Sheets prompting tutorial
--------------------------------

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8)

Was this page helpful?

YesNo

[Give Claude a role (system prompts)](/en/docs/build-with-claude/prompt-engineering/system-prompts)[Chain complex prompts](/en/docs/build-with-claude/prompt-engineering/chain-prompts)

On this page

* [How to prefill Claude’s response](#how-to-prefill-claudes-response)
* [Examples](#examples)
* [Example 1: Controlling output formatting and skipping the preamble](#example-1-controlling-output-formatting-and-skipping-the-preamble)
* [Example 2: Maintaining character in roleplay scenarios](#example-2-maintaining-character-in-roleplay-scenarios)