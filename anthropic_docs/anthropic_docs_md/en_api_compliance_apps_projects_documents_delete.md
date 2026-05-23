# Delete project document

**Source:** http://platform.claude.com/docs/en/api/compliance/apps/projects/documents/delete

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Delete project document

DELETE/v1/compliance/apps/projects/documents/{document\_id}

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

Returns:
ComplianceProjectDocumentDeleteResponse confirming the deletion

# Path ParametersExpand Collapse

document\_id: string

The document ID (tagged ID, e.g., claude\_proj\_doc\_abc123)

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

id: string

The ID of the project document that was deleted

type: "claude\_project\_document\_deleted"

Constant string confirming deletion.

Delete project document

```
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```

# Returns Examples

Response 200

```
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```
