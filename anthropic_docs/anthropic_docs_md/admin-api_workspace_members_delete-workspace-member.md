---
title: 
source_url: https://docs.anthropic.com/en/api/admin-api/workspace_members/delete-workspace-member/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Workspace Member Management

Delete Workspace Member

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

    - [GET

      Get Workspace Member](/en/api/admin-api/workspace_members/get-workspace-member)
    - [GET

      List Workspace Members](/en/api/admin-api/workspace_members/list-workspace-members)
    - [POST

      Add Workspace Member](/en/api/admin-api/workspace_members/create-workspace-member)
    - [POST

      Update Workspace Member](/en/api/admin-api/workspace_members/update-workspace-member)
    - [DEL

      Delete Workspace Member](/en/api/admin-api/workspace_members/delete-workspace-member)
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

workspaces

/

{workspace\_id}

/

members

/

{user\_id}

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

#### Path Parameters

[​](#parameter-user-id)

user\_id

string

required

ID of the User.

[​](#parameter-workspace-id)

workspace\_id

string

required

ID of the Workspace.

#### Response

200 - application/json

[​](#response-type)

type

enum<string>

default:

workspace\_member\_deleted

required

Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

Available options:

`workspace_member_deleted`

[​](#response-user-id)

user\_id

string

required

ID of the User.

[​](#response-workspace-id)

workspace\_id

string

required

ID of the Workspace.

Was this page helpful?

YesNo

[Update Workspace Member](/en/api/admin-api/workspace_members/update-workspace-member)[Get API Key](/en/api/admin-api/apikeys/get-api-key)