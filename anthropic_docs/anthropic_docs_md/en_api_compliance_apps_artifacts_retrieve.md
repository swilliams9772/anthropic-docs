# Get artifact metadata

**Source:** http://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Get artifact metadata

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}

Returns metadata for an artifact version, without the content body.

Use the sibling `/content` endpoint to fetch the artifact text. The
`md5` and `size_bytes` fields here are computed over the UTF-8
encoding of that text, so a DLP consumer can dedupe or match hashes
without downloading every artifact.

# Path ParametersExpand Collapse

artifact\_version\_id: string

The artifact version ID (tagged ID, e.g., claude\_artifact\_version\_abc123)

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string

MIME-like artifact type e.g. 'application/vnd.ant.code'

claude\_chat\_id: string

The chat this artifact belongs to

created\_at: string

Artifact version creation timestamp

md5: string

Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

size\_bytes: number

Size in bytes of the artifact content (UTF-8 encoded)

title: string

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'

Get artifact metadata

```
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "id": "id",
  "artifact_type": "artifact_type",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "md5": "md5",
  "size_bytes": 0,
  "title": "title",
  "version_id": "version_id"
}
```

# Returns Examples

Response 200

```
{
  "id": "id",
  "artifact_type": "artifact_type",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "md5": "md5",
  "size_bytes": 0,
  "title": "title",
  "version_id": "version_id"
}
```
