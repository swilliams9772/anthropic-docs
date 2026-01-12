# Download a File - Anthropic

**Source:** https://docs.anthropic.com/en/api/files-content

The Files API allows you to upload and manage files to use with the Anthropic API without having to re-upload content with each request. For more information about the Files API, see the [developer guide for files](/en/docs/build-with-claude/files).

The Files API is currently in beta. To use the Files API, you’ll need to include the beta feature header: `anthropic-beta: files-api-2025-04-14`.

Please reach out through our [feedback form](https://forms.gle/tisHyierGwgN4DUE9) to share your experience with the Files API.

# Headers

[​](#parameter-anthropic-beta)

anthropic-beta

string[]

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

[​](#parameter-anthropic-version)

anthropic-version

string

required

The version of the Anthropic API you want to use.

Read more about versioning and our version history [here](https://docs.anthropic.com/en/api/versioning).

Your unique API key for authentication.

This key is required in the header of all API requests, to authenticate your account and access Anthropic's services. Get your API key through the [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a Workspace.

# Path Parameters

[​](#parameter-file-id)

file\_id

string

required

ID of the File.

# Response

200

2004XX

application/octet-stream

Successful Response

The response is of type `string`.
