---
title: 
source_url: https://docs.anthropic.com/en/api/admin-api/workspaces/update-workspace/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Workspace Management

Update Workspace

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

    - [GET

      Get Workspace](/en/api/admin-api/workspaces/get-workspace)
    - [GET

      List Workspaces](/en/api/admin-api/workspaces/list-workspaces)
    - [POST

      Update Workspace](/en/api/admin-api/workspaces/update-workspace)
    - [POST

      Create Workspace](/en/api/admin-api/workspaces/create-workspace)
    - [POST

      Archive Workspace](/en/api/admin-api/workspaces/archive-workspace)
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

workspaces

/

{workspace\_id}

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

[​](#parameter-workspace-id)

workspace\_id

string

required

ID of the Workspace.

#### Body

application/json

[​](#body-name)

name

string

required

Name of the Workspace.

Required string length: `1 - 40`

#### Response

200 - application/json

[​](#response-archived-at)

archived\_at

string | null

required

RFC 3339 datetime string indicating when the Workspace was archived, or null if the Workspace is not archived.

[​](#response-created-at)

created\_at

string

required

RFC 3339 datetime string indicating when the Workspace was created.

[​](#response-display-color)

display\_color

string

required

Hex color code representing the Workspace in the Anthropic Console.

[​](#response-id)

id

string

required

ID of the Workspace.

[​](#response-name)

name

string

required

Name of the Workspace.

[​](#response-type)

type

enum<string>

default:

workspace

required

Object type.

For Workspaces, this is always `"workspace"`.

Available options:

`workspace`

Was this page helpful?

YesNo

[List Workspaces](/en/api/admin-api/workspaces/list-workspaces)[Create Workspace](/en/api/admin-api/workspaces/create-workspace)