---
title: 
source_url: https://docs.anthropic.com/en/api/prompt-tools-generate/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Prompt tools

Generate a prompt

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

  + [POST

    Generate a prompt](/en/api/prompt-tools-generate)
  + [POST

    Improve a prompt](/en/api/prompt-tools-improve)
  + [POST

    Templatize a prompt](/en/api/prompt-tools-templatize)

##### Amazon Bedrock API

* [Amazon Bedrock API](/en/api/claude-on-amazon-bedrock)

##### Vertex AI

* [Vertex AI API](/en/api/claude-on-vertex-ai)

POST

/

v1

/

experimental

/

generate\_prompt

The prompt tools APIs are in a closed research preview. [Request to join the closed research preview](https://forms.gle/LajXBafpsf1SuJHp7).

[​](#before-you-begin) Before you begin
---------------------------------------

The prompt tools are a set of APIs to generate and improve prompts. Unlike our other APIs, this is an experimental API: you’ll need to request access, and it doesn’t have the same level of commitment to long-term support as other APIs.

These APIs are similar to what’s available in the [Anthropic Workbench](https://console.anthropic.com/workbench), and are intented for use by other prompt engineering platforms and playgrounds.

[​](#getting-started-with-the-prompt-generator) Getting started with the prompt generator
-----------------------------------------------------------------------------------------

To use the prompt generation API, you’ll need to:

1. Have joined the closed research preview for the prompt tools APIs
2. Use the API directly, rather than the SDK
3. Add the beta header `prompt-tools-2025-04-02`

This API is not available in the SDK

[​](#generate-a-prompt) Generate a prompt
-----------------------------------------

#### Headers

[​](#parameter-anthropic-beta)

anthropic-beta

string[]

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

[​](#parameter-x-api-key)

x-api-key

string

required

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a Workspace.

#### Body

application/json

[​](#body-task)

task

string

required

Description of the prompt's purpose.

The `task` parameter tells Claude what the prompt should do or what kind of role or functionality you want to create. This helps guide the prompt generation process toward your intended use case.

Example:

```json
{"task": "a chef for a meal prep planning service"}
```

[​](#body-target-model)

target\_model

string | null

default:

The model this prompt will be used for. This optional parameter helps us understand which models our prompt tools are being used with, but it doesn't currently affect functionality.

Example:

```bash
"claude-3-7-sonnet-20250219"
```

Required string length: `1 - 256`

#### Response

200 - application/json

* Response Generate Prompt V1 Experimental Generate Prompt Post
* Response Generate Prompt V1 Experimental Generate Prompt Post

[​](#response-messages)

messages

object[]

required

The response contains a list of message objects in the same format used by the Messages API. Typically includes a user message with the complete generated prompt text, and may include an assistant message with a prefill to guide the model's initial response.

These messages can be used directly in a Messages API request to start a conversation with the generated prompt.

Example:

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "You are a chef for a meal prep planning service..."
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "<recipe_planning>"
        }
      ]
    }
  ]
}
```

Show child attributes

[​](#response-messages-content)

messages.content

stringobject[]

required

[​](#response-messages-role)

messages.role

enum<string>

required

Available options:

`user`,

`assistant`

[​](#response-system)

system

string

default:

required

Currently, the `system` field is always returned as an empty string (""). In future iterations, this field may contain generated system prompts.

Directions similar to what would normally be included in a system prompt are included in `messages` when generating a prompt.

[​](#response-usage)

usage

object

required

Usage information

Show child attributes

[​](#response-usage-cache-creation-input-tokens)

usage.cache\_creation\_input\_tokens

integer | null

required

The number of input tokens used to create the cache entry.

Required range: `x > 0`

[​](#response-usage-cache-read-input-tokens)

usage.cache\_read\_input\_tokens

integer | null

required

The number of input tokens read from the cache.

Required range: `x > 0`

[​](#response-usage-input-tokens)

usage.input\_tokens

integer

required

The number of input tokens which were used.

Required range: `x > 0`

[​](#response-usage-output-tokens)

usage.output\_tokens

integer

required

The number of output tokens which were used.

Required range: `x > 0`

Was this page helpful?

YesNo

[OpenAI SDK compatibility (beta)](/en/api/openai-sdk)[Improve a prompt](/en/api/prompt-tools-improve)