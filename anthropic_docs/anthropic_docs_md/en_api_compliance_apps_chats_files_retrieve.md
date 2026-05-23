# Get file metadata

**Source:** http://platform.claude.com/docs/en/api/compliance/apps/chats/files/retrieve

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Get file metadata

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

Retrieves metadata for a file referenced in chat messages, without
downloading the file content. Use the sibling `/content` endpoint to
download the bytes.

# Path ParametersExpand Collapse

claude\_file\_id: string

The file ID (tagged ID, e.g., claude\_file\_abc123)

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

id: string

File ID

created\_at: string

File creation timestamp

filename: string

Display name of the file, if set

md5: string

Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

message\_ids: array of string

Chat message IDs this file is attached to. A file can be referenced by multiple messages.

mime\_type: string

MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

size\_bytes: number

Size in bytes of the file's preferred downloadable variant, if known

Get file metadata

```
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "id": "claude_file_xyz789",
  "filename": "quarterly_report.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1048576,
  "md5": "5d41402abc4b2a76b9719d911017c592",
  "created_at": "2024-01-15T10:30:00Z",
  "message_ids": [
    "claude_chat_msg_abc123"
  ]
}
```

# Returns Examples

Response 200

```
{
  "id": "claude_file_xyz789",
  "filename": "quarterly_report.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1048576,
  "md5": "5d41402abc4b2a76b9719d911017c592",
  "created_at": "2024-01-15T10:30:00Z",
  "message_ids": [
    "claude_chat_msg_abc123"
  ]
}
```
