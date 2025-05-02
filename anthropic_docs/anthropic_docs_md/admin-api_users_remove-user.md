---
title: 
source_url: https://docs.anthropic.com/en/api/admin-api/users/remove-user/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Organization Member Management

Remove User

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

    - [GET

      Get User](/en/api/admin-api/users/get-user)
    - [GET

      List Users](/en/api/admin-api/users/list-users)
    - [POST

      Update User](/en/api/admin-api/users/update-user)
    - [DEL

      Remove User](/en/api/admin-api/users/remove-user)
  + Organization Invites
  + Workspace Management
  + Workspace Member Management
  + API Keys

##### OpenAI SDK compatibility

* [OpenAI SDK compatibility (beta)](/en/api/openai-sdk)

##### Experimental APIs

* Prompt tools

##### Amazon Bedrock API

* [Amazon Bedrock API](/en/api/claude-on-amazon-bedrock)

##### Vertex AI

* [Vertex AI API](/en/api/claude-on-vertex-ai)

DELETE

/

v1

/

organizations

/

users

/

{user\_id}

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

[​](#parameter-user-id)

user\_id

string

required

ID of the User.

#### Response

200 - application/json

[​](#response-id)

id

string

required

ID of the User.

[​](#response-type)

type

enum<string>

default:

user\_deleted

required

Deleted object type.

For Users, this is always `"user_deleted"`.

Available options:

`user_deleted`

Was this page helpful?

YesNo

[Update User](/en/api/admin-api/users/update-user)[Get Invite](/en/api/admin-api/invites/get-invite)