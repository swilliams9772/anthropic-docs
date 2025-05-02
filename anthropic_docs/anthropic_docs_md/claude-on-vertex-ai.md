---
title: 
source_url: https://docs.anthropic.com/en/api/claude-on-vertex-ai/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Vertex AI

Vertex AI API

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

The Vertex API for accessing Claude is nearly-identical to the [Messages API](/en/api/messages) and supports all of the same options, with two key differences:

* In Vertex, `model` is not passed in the request body. Instead, it is specified in the Google Cloud endpoint URL.
* In Vertex, `anthropic_version` is passed in the request body (rather than as a header), and must be set to the value `vertex-2023-10-16`.

Vertex is also supported by Anthropic’s official [client SDKs](/en/api/client-sdks). This guide will walk you through the process of making a request to Claude on Vertex AI in either Python or TypeScript.

Note that this guide assumes you have already have a GCP project that is able to use Vertex AI. See [using the Claude 3 models from Anthropic](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) for more information on the setup required, as well as a full walkthrough.

[​](#install-an-sdk-for-accessing-vertex-ai) Install an SDK for accessing Vertex AI
-----------------------------------------------------------------------------------

First, install Anthropic’s [client SDK](/en/api/client-sdks) for your language of choice.

[​](#accessing-vertex-ai) Accessing Vertex AI
---------------------------------------------

### [​](#model-availability) Model Availability

Note that Anthropic model availability varies by region. Search for “Claude” in the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden) or go to [Use Claude 3](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) for the latest information.

#### [​](#api-model-names) API model names

| Model | Vertex AI API model name |
| --- | --- |
| Claude 3 Haiku | claude-3-haiku@20240307 |
| Claude 3 Sonnet | claude-3-sonnet@20240229 |
| Claude 3 Opus (Public Preview) | claude-3-opus@20240229 |
| Claude 3.5 Haiku | claude-3-5-haiku@20241022 |
| Claude 3.5 Sonnet | claude-3-5-sonnet-v2@20241022 |
| Claude 3.7 Sonnet | claude-3-7-sonnet@20250219 |

### [​](#making-requests) Making requests

Before running requests you may need to run `gcloud auth application-default login` to authenticate with GCP.

The following examples shows how to generate text from Claude 3.7 Sonnet on Vertex AI:

See our [client SDKs](/en/api/client-sdks) and the official [Vertex AI docs](https://cloud.google.com/vertex-ai/docs) for more details.

Was this page helpful?

YesNo

[Amazon Bedrock API](/en/api/claude-on-amazon-bedrock)

On this page

* [Install an SDK for accessing Vertex AI](#install-an-sdk-for-accessing-vertex-ai)
* [Accessing Vertex AI](#accessing-vertex-ai)
* [Model Availability](#model-availability)
* [API model names](#api-model-names)
* [Making requests](#making-requests)