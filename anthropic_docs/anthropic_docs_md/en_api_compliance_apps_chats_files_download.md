# Download file content

**Source:** http://platform.claude.com/docs/en/api/compliance/apps/chats/files/download

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Download file content

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

Downloads the binary content of a file referenced in chat messages.

# Path ParametersExpand Collapse

claude\_file\_id: string

The file ID (tagged ID, e.g., claude\_file\_abc123)

# Header ParametersExpand Collapse

"x-api-key": optional string

Download file content

```
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

# Returns Examples
