# Get Workspace

**Source:** https://platform.claude.com/docs/en/api/admin-api/workspaces/get-workspace

Copy page

# Get Workspace

get/v1/organizations/workspaces/{workspace\_id}

Get Workspace

# Path ParametersExpand Collapse

workspace\_id: string

ID of the Workspace.

# ReturnsExpand Collapse

Workspace = object { id, archived\_at, created\_at, 3 more }

id: string

ID of the Workspace.

archived\_at: string

RFC 3339 datetime string indicating when the Workspace was archived, or null if the Workspace is not archived.

formatdate-time

created\_at: string

RFC 3339 datetime string indicating when the Workspace was created.

formatdate-time

display\_color: string

Hex color code representing the Workspace in the Anthropic Console.

name: string

Name of the Workspace.

type: "workspace"

Object type.

For Workspaces, this is always `"workspace"`.

Accepts one of the following:

"workspace"

Get Workspace

```
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_color": "#6C5BB9",
  "name": "Workspace Name",
  "type": "workspace"
}
```

# Returns Examples

Response 200

```
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_color": "#6C5BB9",
  "name": "Workspace Name",
  "type": "workspace"
}
```
