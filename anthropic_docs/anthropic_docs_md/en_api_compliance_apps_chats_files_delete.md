# Delete file

**Source:** http://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Delete file

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

Permanently deletes a specific file. This is a destructive
operation that cannot be undone.

# Path ParametersExpand Collapse

claude\_file\_id: string

The file ID (tagged ID, e.g., claude\_file\_abc123)

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

id: string

The ID of the file that was deleted

type: optional "claude\_file\_deleted"

Constant string confirming deletion

Delete file

```
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"
}
```

# Returns Examples

Response 200

```
{
  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"
}
```
