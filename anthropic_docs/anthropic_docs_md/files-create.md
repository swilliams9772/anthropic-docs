# Create a File - Anthropic

**Source:** https://docs.anthropic.com/en/api/files-create

- [Documentation](/en/home)
- [Developer Console](https://console.anthropic.com/)
- [Developer Discord](https://www.anthropic.com/discord)
- [Support](https://support.anthropic.com/)

# API reference

* Messages
* Models
* Message Batches
* Files

  + [POST

    Create a File](/en/api/files-create)
  + [GET

    List Files](/en/api/files-list)
  + [GET

    Get File Metadata](/en/api/files-metadata)
  + [GET

    Download a File](/en/api/files-content)
  + [DEL

    Delete a File](/en/api/files-delete)
* Text Completions (Legacy)

# SDKs

* [Client SDKs](/en/api/client-sdks)
* [OpenAI SDK compatibility (beta)](/en/api/openai-sdk)

# Examples

* [Messages examples](/en/api/messages-examples)
* [Message Batches examples](/en/api/messages-batch-examples)

POST

/

v1

/

files

cURL

Python

JavaScript

PHP

Go

Java

```
curl -X POST "https://api.anthropic.com/v1/files" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -F "file=@/path/to/document.pdf"
```

200

4XX

```
{
  "created_at": "2023-11-07T05:31:56Z",
  "downloadable": false,
  "filename": "<string>",
  "id": "<string>",
  "mime_type": "<string>",
  "size_bytes": 1,
  "type": "file"
}
```

The Files API allows you to upload and manage files to use with the Anthropic API without having to re-upload content with each request. For more information about the Files API, see the the [developer guide for files](/en/docs/build-with-claude/files).

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

# Body

multipart/form-data

[​](#body-file)

file

file

required

The file to upload

# Response

200

2004XX

application/json

Successful Response

[​](#response-created-at)

created\_at

string

required

RFC 3339 datetime string representing when the file was created.

[​](#response-filename)

filename

string

required

Original filename of the uploaded file.

Required string length: `1 - 500`

[​](#response-id)

id

string

required

Unique object identifier.

The format and length of IDs may change over time.

[​](#response-mime-type)

mime\_type

string

required

MIME type of the file.

Required string length: `1 - 255`

[​](#response-size-bytes)

size\_bytes

integer

required

Size of the file in bytes.

Required range: `x >= 0`

[​](#response-type)

type

enum<string>

required

Object type.

For files, this is always `"file"`.

Available options:

`file`

[​](#response-downloadable)

downloadable

boolean

default:false

Whether the file can be downloaded.

Was this page helpful?

YesNo

Delete a Message Batch[List Files](/en/api/files-list)

cURL

Python

JavaScript

PHP

Go

Java

```
curl -X POST "https://api.anthropic.com/v1/files" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -F "file=@/path/to/document.pdf"
```

200

4XX

```
{
  "created_at": "2023-11-07T05:31:56Z",
  "downloadable": false,
  "filename": "<string>",
  "id": "<string>",
  "mime_type": "<string>",
  "size_bytes": 1,
  "type": "file"
}
```
