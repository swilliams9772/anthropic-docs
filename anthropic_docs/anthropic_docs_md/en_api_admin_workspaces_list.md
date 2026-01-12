# List Workspaces

**Source:** https://platform.claude.com/docs/en/api/admin/workspaces/list

Copy page

# List Workspaces

get/v1/organizations/workspaces

List Workspaces

# Query ParametersExpand Collapse

after\_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before\_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

include\_archived: optional boolean

Whether to include Workspaces that have been archived in the response

limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

# ReturnsExpand Collapse

data: array of [Workspace](/docs/en/api/$shared#workspace) { id, archived\_at, created\_at, 3 more }

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

first\_id: string

First ID in the `data` list. Can be used as the `before_id` for the previous page.

has\_more: boolean

Indicates if there are more results in the requested page direction.

last\_id: string

Last ID in the `data` list. Can be used as the `after_id` for the next page.

List Workspaces

```
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```
{
  "data": [
    {
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_color": "#6C5BB9",
      "name": "Workspace Name",
      "type": "workspace"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

# Returns Examples

Response 200

```
{
  "data": [
    {
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_color": "#6C5BB9",
      "name": "Workspace Name",
      "type": "workspace"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```
