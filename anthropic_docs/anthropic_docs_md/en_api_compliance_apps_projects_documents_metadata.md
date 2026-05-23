# Get project document metadata

**Source:** http://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Get project document metadata

GET/v1/compliance/apps/projects/documents/{document\_id}/metadata

Returns metadata for a project document, without the content body.

Use the sibling `GET /v1/compliance/apps/projects/documents/{document_id}`
endpoint to fetch the document text. The `md5` and `size_bytes`
fields here are computed over the UTF-8 encoding of that text, so a DLP
consumer can dedupe or match hashes without downloading every document.

# Path ParametersExpand Collapse

document\_id: string

The document ID (tagged ID, e.g., claude\_proj\_doc\_abc123)

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

id: string

Project document identifier (tagged ID)

claude\_project\_id: string

The project this document belongs to

created\_at: string

Document creation timestamp

filename: string

Document filename

md5: string

Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

mime\_type: "text/plain"

MIME type of the document content, always plain text

size\_bytes: number

Size in bytes of the document content (UTF-8 encoded)

user: object { id, email\_address }

User information for project creator.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

Get project document metadata

```
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID/metadata \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "id": "id",
  "claude_project_id": "claude_project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "text/plain",
  "size_bytes": 0,
  "user": {
    "id": "id",
    "email_address": "email_address"
  }
}
```

# Returns Examples

Response 200

```
{
  "id": "id",
  "claude_project_id": "claude_project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "text/plain",
  "size_bytes": 0,
  "user": {
    "id": "id",
    "email_address": "email_address"
  }
}
```
