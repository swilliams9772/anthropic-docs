---
title: 
source_url: https://docs.anthropic.com/en/api/openai-sdk/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

OpenAI SDK compatibility

OpenAI SDK compatibility (beta)

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

Submit feedback or bugs related to the OpenAI SDK compatibility feature [here](https://forms.gle/oQV4McQNiuuNbz9n8).

[​](#before-you-begin) Before you begin
---------------------------------------

This compatibility layer is intended to test and compare model capabilities with minimal development effort and is not considered a long-term or production-ready solution for most use cases. For the best experience and access to Anthropic API full feature set ([PDF processing](/en/docs/build-with-claude/pdf-support), [citations](/en/docs/build-with-claude/citations), [extended thinking](/en/docs/build-with-claude/extended-thinking), and [prompt caching](/en/docs/build-with-claude/prompt-caching)), we recommend using the native [Anthropic API](/en/api/getting-started).

[​](#getting-started-with-the-openai-sdk) Getting started with the OpenAI SDK
-----------------------------------------------------------------------------

To use the OpenAI SDK compatibility feature, you’ll need to:

1. Use an official OpenAI SDK
2. Change the following
  * Update your base URL to point to Anthropic’s API
  * Replace your API key with an [Anthropic API key](https://console.anthropic.com/settings/keys)
  * Update your model name to use a [Claude model](/en/docs/about-claude/models#model-names)
3. Review the documentation below for what features are supported

### [​](#quick-start-example) Quick start example

[​](#important-openai-compatibility-limitations) Important OpenAI compatibility limitations
-------------------------------------------------------------------------------------------

#### [​](#api-behavior) API behavior

Here are the most substantial differences from using OpenAI:

* The `strict` parameter for function calling is ignored, which means the tool use JSON is not guaranteed to follow the supplied schema.
* Audio input is not supported; it will simply be ignored and stripped from input
* Prompt caching is not supported, but it is supported in [the Anthropic SDK](/en/api/client-sdks)
* System/developer messages are hoisted and concatenated to the beginning of the conversation, as Anthropic only supports a single initial system message.

Most unsupported fields are silently ignored rather than producing errors. These are all documented below.

#### [​](#output-quality-considerations) Output quality considerations

If you’ve done lots of tweaking to your prompt, it’s likely to be well-tuned to OpenAI specifically. Consider using our [prompt improver in the Anthropic Console](https://console.anthropic.com/dashboard) as a good starting point.

#### [​](#system-developer-message-hoisting) System / Developer message hoisting

Most of the inputs to the OpenAI SDK clearly map directly to Anthropic’s API parameters, but one distinct difference is the handling of system / developer prompts. These two prompts can be put throughout a chat conversation via OpenAI. Since Anthropic only supports an initial system message, we take all system/developer messages and concatenate them together with a single newline (`\n`) in between them. This full string is then supplied as a single system message at the start of the messages.

#### [​](#extended-thinking-support) Extended thinking support

You can enable [extended thinking](/en/docs/build-with-claude/extended-thinking) capabilities by adding the `thinking` parameter. While this will improve Claude’s reasoning for complex tasks, the OpenAI SDK won’t return Claude’s detailed thought process. For full extended thinking features, including access to Claude’s step-by-step reasoning output, use the native Anthropic API.

[​](#rate-limits) Rate limits
-----------------------------

Rate limits follow Anthropic’s [standard limits](/en/api/rate-limits) for the `/v1/messages` endpoint.

[​](#detailed-openai-compatible-api-support) Detailed OpenAI Compatible API Support
-----------------------------------------------------------------------------------

### [​](#request-fields) Request fields

#### [​](#simple-fields) Simple fields

| Field | Support status |
| --- | --- |
| `model` | Use Claude model names |
| `max_tokens` | Fully supported |
| `max_completion_tokens` | Fully supported |
| `stream` | Fully supported |
| `stream_options` | Fully supported |
| `top_p` | Fully supported |
| `parallel_tool_calls` | Fully supported |
| `stop` | All non-whitespace stop sequences work |
| `temperature` | Between 0 and 1 (inclusive). Values greater than 1 are capped at 1. |
| `n` | Must be exactly 1 |
| `logprobs` | Ignored |
| `metadata` | Ignored |
| `response_format` | Ignored |
| `prediction` | Ignored |
| `presence_penalty` | Ignored |
| `frequency_penalty` | Ignored |
| `seed` | Ignored |
| `service_tier` | Ignored |
| `audio` | Ignored |
| `logit_bias` | Ignored |
| `store` | Ignored |
| `user` | Ignored |
| `modalities` | Ignored |
| `top_logprobs` | Ignored |
| `Reasoning_effort` | Ignored |

#### [​](#tools-functions-fields) `tools` / `functions` fields

Show fields

* Tools
* Functions

`tools[n].function` fields

| Field | Support status |
| --- | --- |
| `name` | Fully supported |
| `description` | Fully supported |
| `parameters` | Fully supported |
| `strict` | Ignored |

#### [​](#messages-array-fields) `messages` array fields

Show fields

* Developer role
* System role
* User role
* Assistant role
* Tool role
* Function role

Fields for `messages[n].role == "developer"`

Developer messages are hoisted to beginning of conversation as part of the initial system message

| Field | Support status |
| --- | --- |
| `content` | Fully supported, but hoisted |
| `name` | Ignored |

### [​](#response-fields) Response fields

| Field | Support status |
| --- | --- |
| `id` | Fully supported |
| `choices[]` | Will always have a length of 1 |
| `choices[].finish_reason` | Fully supported |
| `choices[].index` | Fully supported |
| `choices[].message.role` | Fully supported |
| `choices[].message.content` | Fully supported |
| `choices[].message.tool_calls` | Fully supported |
| `object` | Fully supported |
| `created` | Fully supported |
| `model` | Fully supported |
| `finish_reason` | Fully supported |
| `content` | Fully supported |
| `usage.completion_tokens` | Fully supported |
| `usage.prompt_tokens` | Fully supported |
| `usage.total_tokens` | Fully supported |
| `usage.completion_tokens_details` | Always empty |
| `usage.prompt_tokens_details` | Always empty |
| `choices[].message.refusal` | Always empty |
| `choices[].message.audio` | Always empty |
| `logprobs` | Always empty |
| `service_tier` | Always empty |
| `system_fingerprint` | Always empty |

### [​](#error-message-compatibility) Error message compatibility

The compatibility layer maintains consistent error formats with the OpenAI API. However, the detailed error messages will not be equivalent. We recommend only using the error messages for logging and debugging.

### [​](#header-compatibility) Header compatibility

While the OpenAI SDK automatically manages headers, here is the complete list of headers supported by Anthropic’s API for developers who need to work with them directly.

| Header | Support Status |
| --- | --- |
| `x-ratelimit-limit-requests` | Fully supported |
| `x-ratelimit-limit-tokens` | Fully supported |
| `x-ratelimit-remaining-requests` | Fully supported |
| `x-ratelimit-remaining-tokens` | Fully supported |
| `x-ratelimit-reset-requests` | Fully supported |
| `x-ratelimit-reset-tokens` | Fully supported |
| `retry-after` | Fully supported |
| `x-request-id` | Fully supported |
| `openai-version` | Always `2020-10-01` |
| `authorization` | Fully supported |
| `openai-processing-ms` | Always empty |

Was this page helpful?

YesNo

[Update API Keys](/en/api/admin-api/apikeys/update-api-key)[Generate a prompt](/en/api/prompt-tools-generate)

On this page

* [Before you begin](#before-you-begin)
* [Getting started with the OpenAI SDK](#getting-started-with-the-openai-sdk)
* [Quick start example](#quick-start-example)
* [Important OpenAI compatibility limitations](#important-openai-compatibility-limitations)
* [API behavior](#api-behavior)
* [Output quality considerations](#output-quality-considerations)
* [System / Developer message hoisting](#system-developer-message-hoisting)
* [Extended thinking support](#extended-thinking-support)
* [Rate limits](#rate-limits)
* [Detailed OpenAI Compatible API Support](#detailed-openai-compatible-api-support)
* [Request fields](#request-fields)
* [Simple fields](#simple-fields)
* [tools / functions fields](#tools-functions-fields)
* [messages array fields](#messages-array-fields)
* [Response fields](#response-fields)
* [Error message compatibility](#error-message-compatibility)
* [Header compatibility](#header-compatibility)