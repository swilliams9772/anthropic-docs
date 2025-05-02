---
title: 
source_url: https://docs.anthropic.com/en/api/claude-on-amazon-bedrock/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Amazon Bedrock API

Amazon Bedrock API

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

Calling Claude through Bedrock slightly differs from how you would call Claude when using Anthropic’s client SDK’s. This guide will walk you through the process of completing an API call to Claude on Bedrock in either Python or TypeScript.

Note that this guide assumes you have already signed up for an [AWS account](https://portal.aws.amazon.com/billing/signup) and configured programmatic access.

[​](#install-and-configure-the-aws-cli) Install and configure the AWS CLI
-------------------------------------------------------------------------

1. [Install a version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) at or newer than version `2.13.23`
2. Configure your AWS credentials using the AWS configure command (see [Configure the AWS CLI](https://alpha.www.docs.aws.a2z.com/cli/latest/userguide/cli-chap-configure.html)) or find your credentials by navigating to “Command line or programmatic access” within your AWS dashboard and following the directions in the popup modal.
3. Verify that your credentials are working:

Shell

```bash
aws sts get-caller-identity
```

[​](#install-an-sdk-for-accessing-bedrock) Install an SDK for accessing Bedrock
-------------------------------------------------------------------------------

Anthropic’s [client SDKs](/en/api/client-sdks) support Bedrock. You can also use an AWS SDK like `boto3` directly.

[​](#accessing-bedrock) Accessing Bedrock
-----------------------------------------

### [​](#subscribe-to-anthropic-models) Subscribe to Anthropic models

Go to the [AWS Console > Bedrock > Model Access](https://console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess) and request access to Anthropic models. Note that Anthropic model availability varies by region. See [AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for latest information.

#### [​](#api-model-names) API model names

| Model | Bedrock API model name |
| --- | --- |
| Claude 3 Haiku | anthropic.claude-3-haiku-20240307-v1:0 |
| Claude 3 Sonnet | anthropic.claude-3-sonnet-20240229-v1:0 |
| Claude 3 Opus | anthropic.claude-3-opus-20240229-v1:0 |
| Claude 3.5 Haiku | anthropic.claude-3-5-haiku-20241022-v1:0 |
| Claude 3.5 Sonnet | anthropic.claude-3-5-sonnet-20241022-v2:0 |
| Claude 3.7 Sonnet | anthropic.claude-3-7-sonnet-20250219-v1:0 |

### [​](#list-available-models) List available models

The following examples show how to print a list of all the Claude models available through Bedrock:

### [​](#making-requests) Making requests

The following examples shows how to generate text from Claude 3 Sonnet on Bedrock:

See our [client SDKs](/en/api/client-sdks) for more details, and the official Bedrock docs [here](https://docs.aws.amazon.com/bedrock/).

Was this page helpful?

YesNo

[Templatize a prompt](/en/api/prompt-tools-templatize)[Vertex AI API](/en/api/claude-on-vertex-ai)

On this page

* [Install and configure the AWS CLI](#install-and-configure-the-aws-cli)
* [Install an SDK for accessing Bedrock](#install-an-sdk-for-accessing-bedrock)
* [Accessing Bedrock](#accessing-bedrock)
* [Subscribe to Anthropic models](#subscribe-to-anthropic-models)
* [API model names](#api-model-names)
* [List available models](#list-available-models)
* [Making requests](#making-requests)