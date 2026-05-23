# Delete project

**Source:** http://platform.claude.com/docs/en/api/compliance/apps/projects/delete

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Delete project

DELETE/v1/compliance/apps/projects/{project\_id}

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

* All project documents and files
* All role assignments
* Knowledge base (if RAG is enabled)
* Sync sources

Project must have no attached chats - returns 409 if chats exist.

Returns:
ClaudeProjectDeleteResponse confirming the deletion

Raises:
ConflictException: If project has chats attached
NotFoundException: If project doesn't exist or already deleted

# Path ParametersExpand Collapse

project\_id: string

The project ID (tagged ID, e.g., claude\_proj\_abc123)

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

id: string

The ID of the Claude project that was deleted

type: optional "claude\_project\_deleted"

Constant string confirming deletion.

Delete project

```
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "id": "id",
  "type": "claude_project_deleted"
}
```

# Returns Examples

Response 200

```
{
  "id": "id",
  "type": "claude_project_deleted"
}
```
