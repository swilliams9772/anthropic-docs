# Amazon Bedrock API - Anthropic

**Source:** https://docs.anthropic.com/en/api/claude-on-amazon-bedrock

Calling Claude through Bedrock slightly differs from how you would call Claude when using Anthropic’s client SDK’s. This guide will walk you through the process of completing an API call to Claude on Bedrock in either Python or TypeScript.

Note that this guide assumes you have already signed up for an [AWS account](https://portal.aws.amazon.com/billing/signup) and configured programmatic access.

# [​](#install-and-configure-the-aws-cli) Install and configure the AWS CLI

1. [Install a version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) at or newer than version `2.13.23`
2. Configure your AWS credentials using the AWS configure command (see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)) or find your credentials by navigating to “Command line or programmatic access” within your AWS dashboard and following the directions in the popup modal.
3. Verify that your credentials are working:

Shell

```
aws sts get-caller-identity

```

# [​](#install-an-sdk-for-accessing-bedrock) Install an SDK for accessing Bedrock

Anthropic’s [client SDKs](/en/api/client-sdks) support Bedrock. You can also use an AWS SDK like `boto3` directly.

Python

TypeScript

Boto3 (Python)

```
pip install -U "anthropic[bedrock]"

```

# [​](#accessing-bedrock) Accessing Bedrock

# [​](#subscribe-to-anthropic-models) Subscribe to Anthropic models

Go to the [AWS Console > Bedrock > Model Access](https://console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess) and request access to Anthropic models. Note that Anthropic model availability varies by region. See [AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for latest information.

# [​](#api-model-names) API model names

| Model | Bedrock API model name |
| --- | --- |
| Claude Opus 4.1 | anthropic.claude-opus-4-1-20250805-v1:0 |
| Claude Opus 4 | anthropic.claude-opus-4-20250514-v1:0 |
| Claude Sonnet 4 | anthropic.claude-sonnet-4-20250514-v1:0 |
| Claude Sonnet 3.7 | anthropic.claude-3-7-sonnet-20250219-v1:0 |
| Claude Haiku 3.5 | anthropic.claude-3-5-haiku-20241022-v1:0 |
| Claude Sonnet 3.5 ⚠️ | anthropic.claude-3-5-sonnet-20241022-v2:0 |
| Claude Opus 3 ⚠️ | anthropic.claude-3-opus-20240229-v1:0 |
| Claude Sonnet 3 ⚠️ | anthropic.claude-3-sonnet-20240229-v1:0 |
| Claude Haiku 3 | anthropic.claude-3-haiku-20240307-v1:0 |

# [​](#list-available-models) List available models

The following examples show how to print a list of all the Claude models available through Bedrock:

AWS CLI

Boto3 (Python)

```
aws bedrock list-foundation-models --region=us-west-2 --by-provider anthropic --query "modelSummaries[*].modelId"

```

# [​](#making-requests) Making requests

The following examples show how to generate text from Claude on Bedrock:

Python

TypeScript

Boto3 (Python)

```
from anthropic import AnthropicBedrock

client = AnthropicBedrock(
    # Authenticate by either providing the keys below or use the default AWS credential providers, such as
    # using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
    aws_access_key="<access key>",
    aws_secret_key="<secret key>",
    # Temporary credentials can be used with aws_session_token.
    # Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
    aws_session_token="<session_token>",
    # aws_region changes the aws region to which the request is made. By default, we read AWS_REGION,
    # and if that's not present, we default to us-east-1. Note that we do not read ~/.aws/config for the region.
    aws_region="us-west-2",
)

message = client.messages.create(
    model="anthropic.claude-opus-4-1-20250805-v1:0",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}]
)
print(message.content)

```

See our [client SDKs](/en/api/client-sdks) for more details, and the official Bedrock docs [here](https://docs.aws.amazon.com/bedrock/).

# [​](#activity-logging) Activity logging

Bedrock provides an [invocation logging service](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) that allows customers to log the prompts and completions associated with your usage.

Anthropic recommends that you log your activity on at least a 30-day rolling basis in order to understand your activity and investigate any potential misuse.

Turning on this service does not give AWS or Anthropic any access to your content.

# [​](#feature-support) Feature support

You can find all the features currently supported on Bedrock [here](/en/docs/build-with-claude/overview).

# [​](#pdf-support-on-bedrock) PDF Support on Bedrock

PDF support is available on Amazon Bedrock through both the Converse API and InvokeModel API. For detailed information about PDF processing capabilities and limitations, see the [PDF support documentation](/en/docs/build-with-claude/pdf-support#amazon-bedrock-pdf-support).

**Important considerations for Converse API users:**

* Visual PDF analysis (charts, images, layouts) requires citations to be enabled
* Without citations, only basic text extraction is available
* For full control without forced citations, use the InvokeModel API

For more details on the two document processing modes and their limitations, refer to the [PDF support guide](/en/docs/build-with-claude/pdf-support#amazon-bedrock-pdf-support).

# [​](#1m-token-context-window) 1M token context window

Claude Sonnet 4 supports the [1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window) on Amazon Bedrock.

The 1M token context window is currently in beta. To use the extended context window, include the `context-1m-2025-08-07` beta header in your [Bedrock API requests](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-request-response.html).
