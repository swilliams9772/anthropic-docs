# Delete File

**Source:** https://platform.claude.com/docs/en/api/beta/files/delete

Copy page

cURL

# Delete File

delete/v1/files/{file\_id}

Delete File

# Path ParametersExpand Collapse

file\_id: string

ID of the File.

# Header ParametersExpand Collapse

"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 16 more

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

# ReturnsExpand Collapse

DeletedFile = object { id, type }

id: string

ID of the deleted file.

type: optional "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

"file\_deleted"

Delete File

cURL

```
curl https://api.anthropic.com/v1/files/$FILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: files-api-2025-04-14' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200

```
{
  "id": "id",
  "type": "file_deleted"
}
```

# Returns Examples

Response 200

```
{
  "id": "id",
  "type": "file_deleted"
}
```
