---
title: 
source_url: https://docs.anthropic.com/en/api/admin-api/invites/create-invite/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Organization Invites

Create Invite

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

    - [GET

      Get Invite](/en/api/admin-api/invites/get-invite)
    - [GET

      List Invites](/en/api/admin-api/invites/list-invites)
    - [POST

      Create Invite](/en/api/admin-api/invites/create-invite)
    - [DEL

      Delete Invite](/en/api/admin-api/invites/delete-invite)
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

POST

/

v1

/

organizations

/

invites

**The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.

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

#### Body

application/json

[​](#body-email)

email

string

required

Email of the User.

[​](#body-role)

role

enum<string>

required

Role for the invited User. Cannot be "admin".

Available options:

`user`,

`developer`,

`billing`

#### Response

200 - application/json

[​](#response-email)

email

string

required

Email of the User being invited.

[​](#response-expires-at)

expires\_at

string

required

RFC 3339 datetime string indicating when the Invite expires.

[​](#response-id)

id

string

required

ID of the Invite.

[​](#response-invited-at)

invited\_at

string

required

RFC 3339 datetime string indicating when the Invite was created.

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

[​](#response-status)

status

enum<string>

required

Status of the Invite.

Available options:

`accepted`,

`expired`,

`deleted`,

`pending`

[​](#response-type)

type

enum<string>

default:

invite

required

Object type.

For Invites, this is always `"invite"`.

Available options:

`invite`

Was this page helpful?

YesNo

[List Invites](/en/api/admin-api/invites/list-invites)[Delete Invite](/en/api/admin-api/invites/delete-invite)