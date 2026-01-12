# Create Invite

**Source:** https://platform.claude.com/docs/en/api/admin/invites/create

Copy page

# Create Invite

post/v1/organizations/invites

Create Invite

# Body ParametersExpand Collapse

email: string

Email of the User.

formatemail

role: "user" or "developer" or "billing" or "claude\_code\_user"

Role for the invited User. Cannot be "admin".

Accepts one of the following:

"user"

"developer"

"billing"

"claude\_code\_user"

# ReturnsExpand Collapse

Invite = object { id, email, expires\_at, 4 more }

id: string

ID of the Invite.

email: string

Email of the User being invited.

expires\_at: string

RFC 3339 datetime string indicating when the Invite expires.

formatdate-time

invited\_at: string

RFC 3339 datetime string indicating when the Invite was created.

formatdate-time

role: "user" or "developer" or "billing" or 2 more

Organization role of the User.

Accepts one of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"

status: "accepted" or "expired" or "deleted" or "pending"

Status of the Invite.

Accepts one of the following:

"accepted"

"expired"

"deleted"

"pending"

type: "invite"

Object type.

For Invites, this is always `"invite"`.

Accepts one of the following:

"invite"

Create Invite

```
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'Content-Type: application/json' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "email": "user@emaildomain.com",
          "role": "user"
        }'
```

Response 200

```
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "role": "user",
  "status": "pending",
  "type": "invite"
}
```

# Returns Examples

Response 200

```
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "role": "user",
  "status": "pending",
  "type": "invite"
}
```
