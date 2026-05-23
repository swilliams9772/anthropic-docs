# Get Workspace

**Source:** http://platform.claude.com/docs/en/api/admin/workspaces/retrieve

Copy page

# Get Workspace

GET/v1/organizations/workspaces/{workspace\_id}

Get Workspace

# Path ParametersExpand Collapse

workspace\_id: string

ID of the Workspace.

# ReturnsExpand Collapse

Workspace object { id, archived\_at, created\_at, 5 more }

id: string

ID of the Workspace.

archived\_at: string

RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Workspace was created.

data\_residency: object { allowed\_inference\_geos, default\_inference\_geo, workspace\_geo }

Data residency configuration.

allowed\_inference\_geos: array of string or "unrestricted"

Permitted inference geo values. 'unrestricted' means all geos are allowed.

One of the following:

array of string

"unrestricted"

default\_inference\_geo: string

Default inference geo applied when requests omit the parameter.

workspace\_geo: string

Geographic region for workspace data storage. Immutable after creation.

display\_color: string

Hex color code representing the Workspace in the Anthropic Console.

name: string

Name of the Workspace.

tags: map[string]

User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

type: "workspace"

Object type.

For Workspaces, this is always `"workspace"`.

Get Workspace

```
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
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
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```
