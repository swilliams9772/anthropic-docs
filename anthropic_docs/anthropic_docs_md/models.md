---
title: 
source_url: https://docs.anthropic.com/en/api/models/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Models

Get a Model

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

  + [GET

    List Models](/en/api/models-list)
  + [GET

    Get a Model](/en/api/models)
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

GET

/

v1

/

models

/

{model\_id}

#### Headers

[​](#parameter-anthropic-version)

anthropic-version

string

required

The version of the Anthropic API you want to use.

Read more about versioning and our version history [here](https://docs.anthropic.com/en/api/versioning).

[​](#parameter-x-api-key)

x-api-key

string

required

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a Workspace.

#### Path Parameters

[​](#parameter-model-id)

model\_id

string

required

Model identifier or alias.

#### Response

200 - application/json

[​](#response-created-at)

created\_at

string

required

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

[​](#response-display-name)

display\_name

string

required

A human-readable name for the model.

[​](#response-id)

id

string

required

Unique model identifier.

[​](#response-type)

type

enum<string>

default:

model

required

Object type.

For Models, this is always `"model"`.

Available options:

`model`

Was this page helpful?

YesNo

[List Models](/en/api/models-list)[Create a Message Batch](/en/api/creating-message-batches)