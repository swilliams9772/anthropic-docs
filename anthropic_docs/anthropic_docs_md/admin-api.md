---
title: 
source_url: https://docs.anthropic.com/en/api/admin-api/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Organization Member Management

Get User

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

GET

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

[​](#response-added-at)

added\_at

string

required

RFC 3339 datetime string indicating when the User joined the Organization.

[​](#response-email)

email

string

required

Email of the User.

[​](#response-id)

id

string

required

ID of the User.

[​](#response-name)

name

string

required

Name of the User.

[​](#response-role)

role

enum<string>

required

Organization role of the User.

Available options:

`user`,

`developer`,

`billing`,

`admin`

[​](#response-type)

type

enum<string>

default:

user

required

Object type.

For Users, this is always `"user"`.

Available options:

`user`

Was this page helpful?

YesNo

[Prompt validation](/en/api/prompt-validation)[List Users](/en/api/admin-api/users/list-users)