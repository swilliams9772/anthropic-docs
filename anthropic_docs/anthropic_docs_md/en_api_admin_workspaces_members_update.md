# Update Workspace Member

**Source:** https://platform.claude.com/docs/en/api/admin/workspaces/members/update

Copy page

# Update Workspace Member

post/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

Update Workspace Member

# Path ParametersExpand Collapse

workspace\_id: string

ID of the Workspace.

user\_id: string

ID of the User.

# Body ParametersExpand Collapse

workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_admin" or "workspace\_billing"

New workspace role for the User.

Accepts one of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_admin"

"workspace\_billing"

# ReturnsExpand Collapse

WorkspaceMember = object { type, user\_id, workspace\_id, workspace\_role }

type: "workspace\_member"

Object type.

For Workspace Members, this is always `"workspace_member"`.

Accepts one of the following:

"workspace\_member"

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_admin" or "workspace\_billing"

Role of the Workspace Member.

Accepts one of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_admin"

"workspace\_billing"

Update Workspace Member

```
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -H 'Content-Type: application/json' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "workspace_role": "workspace_user"
        }'
```

Response 200

```
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_user"
}
```

# Returns Examples

Response 200

```
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_user"
}
```
