---
title: 
source_url: https://docs.anthropic.com/en/api/admin-api/apikeys/list-api-keys/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

API Keys

List API Keys

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

GET

/

v1

/

organizations

/

api\_keys

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

#### Query Parameters

[​](#parameter-before-id)

before\_id

string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

[​](#parameter-after-id)

after\_id

string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

[​](#parameter-limit)

limit

integer

default:

20

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

Required range: `1 < x < 1000`

[​](#parameter-status)

status

enum<string> | null

Filter by API key status.

Available options:

`active`,

`inactive`,

`archived`

[​](#parameter-workspace-id)

workspace\_id

string | null

Filter by Workspace ID.

[​](#parameter-created-by-user-id)

created\_by\_user\_id

string | null

Filter by the ID of the User who created the object.

#### Response

200 - application/json

[​](#response-data)

data

object[]

required

Show child attributes

[​](#response-data-created-at)

data.created\_at

string

required

RFC 3339 datetime string indicating when the API Key was created.

[​](#response-data-created-by)

data.created\_by

object

required

The ID and type of the actor that created the API key.

Show child attributes

[​](#response-data-created-by-id)

data.created\_by.id

string

required

ID of the actor that created the object.

[​](#response-data-created-by-type)

data.created\_by.type

string

required

Type of the actor that created the object.

[​](#response-data-id)

data.id

string

required

ID of the API key.

[​](#response-data-name)

data.name

string

required

Name of the API key.

[​](#response-data-partial-key-hint)

data.partial\_key\_hint

string | null

required

Partially redacted hint for the API key.

[​](#response-data-status)

data.status

enum<string>

required

Status of the API key.

Available options:

`active`,

`inactive`,

`archived`

[​](#response-data-type)

data.type

enum<string>

default:

api\_key

required

Object type.

For API Keys, this is always `"api_key"`.

Available options:

`api_key`

[​](#response-data-workspace-id)

data.workspace\_id

string | null

required

ID of the Workspace associated with the API key, or null if the API key belongs to the default Workspace.

[​](#response-first-id)

first\_id

string | null

required

First ID in the `data` list. Can be used as the `before_id` for the previous page.

[​](#response-has-more)

has\_more

boolean

required

Indicates if there are more results in the requested page direction.

[​](#response-last-id)

last\_id

string | null

required

Last ID in the `data` list. Can be used as the `after_id` for the next page.

Was this page helpful?

YesNo

[Get API Key](/en/api/admin-api/apikeys/get-api-key)[Update API Keys](/en/api/admin-api/apikeys/update-api-key)