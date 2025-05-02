---
title: 
source_url: https://docs.anthropic.com/en/api/admin-api/users/list-users/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Organization Member Management

List Users

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

[​](#parameter-email)

email

string

Filter by user email.

#### Response

200 - application/json

[​](#response-data)

data

object[]

required

Show child attributes

[​](#response-data-added-at)

data.added\_at

string

required

RFC 3339 datetime string indicating when the User joined the Organization.

[​](#response-data-email)

data.email

string

required

Email of the User.

[​](#response-data-id)

data.id

string

required

ID of the User.

[​](#response-data-name)

data.name

string

required

Name of the User.

[​](#response-data-role)

data.role

enum<string>

required

Organization role of the User.

Available options:

`user`,

`developer`,

`billing`,

`admin`

[​](#response-data-type)

data.type

enum<string>

default:

user

required

Object type.

For Users, this is always `"user"`.

Available options:

`user`

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

[Get User](/en/api/admin-api/users/get-user)[Update User](/en/api/admin-api/users/update-user)