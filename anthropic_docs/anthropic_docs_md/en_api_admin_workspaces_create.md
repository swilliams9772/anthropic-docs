# Create Workspace

**Source:** https://platform.claude.com/docs/en/api/admin/workspaces/create

Copy page

# Create Workspace

post/v1/organizations/workspaces

Create Workspace

# Body ParametersExpand Collapse

name: string

Name of the Workspace.

maxLength40

minLength1

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

Create Workspace

```
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H 'Content-Type: application/json' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "name": "x"
        }'
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
