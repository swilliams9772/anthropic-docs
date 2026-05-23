# Download artifact content

**Source:** http://platform.claude.com/docs/en/api/compliance/apps/artifacts/download

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Download artifact content

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}/content

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

# Path ParametersExpand Collapse

artifact\_version\_id: string

The artifact version ID (tagged ID, e.g., claude\_artifact\_version\_abc123)

# Header ParametersExpand Collapse

"x-api-key": optional string

Download artifact content

```
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

# Returns Examples
