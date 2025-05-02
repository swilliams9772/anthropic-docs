---
title: 
source_url: https://docs.anthropic.com/en/api/migrating-from-text-completions-to-messages/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Messages

Migrating from Text Completions

[Welcome](/en/home)[User Guides](/en/docs/welcome)[API Reference](/en/api/getting-started)[Prompt Library](/en/prompt-library/library)[Release Notes](/en/release-notes/overview)

- [Developer Console](https://console.anthropic.com/)
- [Developer Discord](https://www.anthropic.com/discord)
- [Support](https://support.anthropic.com/)

##### Using the API

* [Getting started](/en/api/getting-started)
* [IP addresses](/en/api/ip-addresses)
* [Versions](/en/api/versioning)
* [Errors](/en/api/errors)
* [Rate limits](/en/api/rate-limits)
* [Client SDKs](/en/api/client-sdks)
* [Supported regions](/en/api/supported-regions)
* [Getting help](/en/api/getting-help)

##### Anthropic APIs

* Messages

  + [POST

    Messages](/en/api/messages)
  + [POST

    Count Message tokens](/en/api/messages-count-tokens)
  + [Streaming Messages](/en/api/messages-streaming)
  + [Migrating from Text Completions](/en/api/migrating-from-text-completions-to-messages)
  + [Messages examples](/en/api/messages-examples)
* Models
* Message Batches
* Text Completions (Legacy)
* Admin API

##### OpenAI SDK compatibility

* [OpenAI SDK compatibility (beta)](/en/api/openai-sdk)

##### Experimental APIs

* Prompt tools

##### Amazon Bedrock API

* [Amazon Bedrock API](/en/api/claude-on-amazon-bedrock)

##### Vertex AI

* [Vertex AI API](/en/api/claude-on-vertex-ai)

When migrating from from [Text Completions](/en/api/complete) to [Messages](/en/api/messages), consider the following changes.

### [​](#inputs-and-outputs) Inputs and outputs

The largest change between Text Completions and the Messages is the way in which you specify model inputs and receive outputs from the model.

With Text Completions, inputs are raw strings:

Python

```bash
prompt = "\n\nHuman: Hello there\n\nAssistant: Hi, I'm Claude. How can I help?\n\nHuman: Can you explain Glycolysis to me?\n\nAssistant:"
```

With Messages, you specify a list of input messages instead of a raw prompt:

Each input message has a `role` and `content`.

**Role names**

The Text Completions API expects alternating `\n\nHuman:` and `\n\nAssistant:` turns, but the Messages API expects `user` and `assistant` roles. You may see documentation referring to either “human” or “user” turns. These refer to the same role, and will be “user” going forward.

With Text Completions, the model’s generated text is returned in the `completion` values of the response:

Python

```bash
>>> response = anthropic.completions.create(...)
>>> response.completion
" Hi, I'm Claude"
```

With Messages, the response is the `content` value, which is a list of content blocks:

Python

```bash
>>> response = anthropic.messages.create(...)
>>> response.content
[{"type": "text", "text": "Hi, I'm Claude"}]
```

### [​](#putting-words-in-claudes-mouth) Putting words in Claude’s mouth

With Text Completions, you can pre-fill part of Claude’s response:

Python

```bash
prompt = "\n\nHuman: Hello\n\nAssistant: Hello, my name is"
```

With Messages, you can achieve the same result by making the last input message have the `assistant` role:

Python

```bash
messages = [
  {"role": "human", "content": "Hello"},
  {"role": "assistant", "content": "Hello, my name is"},
]
```

When doing so, response `content` will continue from the last input message `content`:

JSON

```json
{
  "role": "assistant",
  "content": [{"type": "text", "text": " Claude. How can I assist you today?" }],
  ...
}
```

### [​](#system-prompt) System prompt

With Text Completions, the [system prompt](/en/docs/system-prompts) is specified by adding text before the first `\n\nHuman:` turn:

Python

```bash
prompt = "Today is January 1, 2024.\n\nHuman: Hello, Claude\n\nAssistant:"
```

With Messages, you specify the system prompt with the `system` parameter:

Python

```bash
anthropic.Anthropic().messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    system="Today is January 1, 2024.", # <-- system prompt
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
```

### [​](#model-names) Model names

The Messages API requires that you specify the full model version (e.g. `claude-3-opus-20240229`).

We previously supported specifying only the major version number (e.g. `claude-2`), which resulted in automatic upgrades to minor versions. However, we no longer recommend this integration pattern, and Messages do not support it.

### [​](#stop-reason) Stop reason

Text Completions always have a `stop_reason` of either:

* `"stop_sequence"`: The model either ended its turn naturally, or one of your custom stop sequences was generated.
* `"max_tokens"`: Either the model generated your specified `max_tokens` of content, or it reached its [absolute maximum](/en/docs/models-overview#model-comparison).

Messages have a `stop_reason` of one of the following values:

* `"end_turn"`: The conversational turn ended naturally.
* `"stop_sequence"`: One of your specified custom stop sequences was generated.
* `"max_tokens"`: (unchanged)

### [​](#specifying-max-tokens) Specifying max tokens

* Text Completions: `max_tokens_to_sample` parameter. No validation, but capped values per-model.
* Messages: `max_tokens` parameter. If passing a value higher than the model supports, returns a validation error.

### [​](#streaming-format) Streaming format

When using `"stream": true` in with Text Completions, the response included any of `completion`, `ping`, and `error` server-sent-events. See [Text Completions streaming](https://anthropic.readme.io/claude/reference/streaming) for details.

Messages can contain multiple content blocks of varying types, and so its streaming format is somewhat more complex. See [Messages streaming](https://anthropic.readme.io/claude/reference/messages-streaming) for details.

Was this page helpful?

YesNo

[Streaming Messages](/en/api/messages-streaming)[Messages examples](/en/api/messages-examples)

On this page

* [Inputs and outputs](#inputs-and-outputs)
* [Putting words in Claude’s mouth](#putting-words-in-claudes-mouth)
* [System prompt](#system-prompt)
* [Model names](#model-names)
* [Stop reason](#stop-reason)
* [Specifying max tokens](#specifying-max-tokens)
* [Streaming format](#streaming-format)