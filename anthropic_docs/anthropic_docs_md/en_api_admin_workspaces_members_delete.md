# Delete Workspace Member

**Source:** https://platform.claude.com/docs/en/api/admin/workspaces/members/delete

Copy page

# Delete Workspace Member

delete/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

Delete Workspace Member

# Path ParametersExpand Collapse

workspace\_id: string

ID of the Workspace.

user\_id: string

ID of the User.

# ReturnsExpand Collapse

type: "workspace\_member\_deleted"

Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

Accepts one of the following:

"workspace\_member\_deleted"

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

Delete Workspace Member

```
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -X DELETE \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

# Returns Examples

Response 200

```
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```
