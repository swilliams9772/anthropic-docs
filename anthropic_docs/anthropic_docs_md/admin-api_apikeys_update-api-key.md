---
title: 
source_url: https://docs.anthropic.com/en/api/admin-api/apikeys/update-api-key/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

API Keys

Update API Keys

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

  + Organization Member Management
  + Organization Invites
  + Workspace Management
  + Workspace Member Management
  + API Keys

    - [GET

      Get API Key](/en/api/admin-api/apikeys/get-api-key)
    - [GET

      List API Keys](/en/api/admin-api/apikeys/list-api-keys)
    - [POST

      Update API Keys](/en/api/admin-api/apikeys/update-api-key)

##### OpenAI SDK compatibility

* [OpenAI SDK compatibility (beta)](/en/api/openai-sdk)

##### Experimental APIs

* Prompt tools

##### Amazon Bedrock API

* [Amazon Bedrock API](/en/api/claude-on-amazon-bedrock)

##### Vertex AI

* [Vertex AI API](/en/api/claude-on-vertex-ai)

POST

/

v1

/

organizations

/

api\_keys

/

{api\_key\_id}

#### Headers

[​](#parameter-x-api-key)

x-api-key

string

required

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the [Console](https://console.anthropic.com/settings/admin-keys).

[​](#parameter-anthropic-version)

anthropic-version

string

required

The version of the Anthropic API you want to use.

Read more about versioning and our version history [here](https://docs.anthropic.com/en/api/versioning).

#### Path Parameters

[​](#parameter-api-key-id)

api\_key\_id

string

required

ID of the API key.

#### Body

application/json

[​](#body-name)

name

string

Name of the API key.

Required string length: `1 - 500`

[​](#body-status)

status

enum<string> | null

Status of the API key.

Available options:

`active`,

`inactive`,

`archived`

#### Response

200 - application/json

[​](#response-created-at)

created\_at

string

required

RFC 3339 datetime string indicating when the API Key was created.

[​](#response-created-by)

created\_by

object

required

The ID and type of the actor that created the API key.

Show child attributes

[​](#response-created-by-id)

created\_by.id

string

required

ID of the actor that created the object.

[​](#response-created-by-type)

created\_by.type

string

required

Type of the actor that created the object.

[​](#response-id)

id

string

required

ID of the API key.

[​](#response-name)

name

string

required

Name of the API key.

[​](#response-partial-key-hint)

partial\_key\_hint

string | null

required

Partially redacted hint for the API key.

[​](#response-status)

status

enum<string>

required

Status of the API key.

Available options:

`active`,

`inactive`,

`archived`

[​](#response-type)

type

enum<string>

default:

api\_key

required

Object type.

For API Keys, this is always `"api_key"`.

Available options:

`api_key`

[​](#response-workspace-id)

workspace\_id

string | null

required

ID of the Workspace associated with the API key, or null if the API key belongs to the default Workspace.

Was this page helpful?

YesNo

[List API Keys](/en/api/admin-api/apikeys/list-api-keys)[OpenAI SDK compatibility (beta)](/en/api/openai-sdk)