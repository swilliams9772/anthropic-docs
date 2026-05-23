# Update User

**Source:** http://platform.claude.com/docs/en/api/admin/users/update

Copy page

# Update User

POST/v1/organizations/users/{user\_id}

Update User

# Path ParametersExpand Collapse

user\_id: string

ID of the User.

# Body ParametersJSONExpand Collapse

role: "user" or "developer" or "billing" or "claude\_code\_user"

New role for the User. Cannot be "admin".

One of the following:

"user"

"developer"

"billing"

"claude\_code\_user"

# ReturnsExpand Collapse

User object { id, added\_at, email, 3 more }

id: string

ID of the User.

added\_at: string

RFC 3339 datetime string indicating when the User joined the Organization.

email: string

Email of the User.

name: string

Name of the User.

role: "user" or "developer" or "billing" or 2 more

Organization role of the User.

One of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"

type: "user"

Object type.

For Users, this is always `"user"`.

Update User

```
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "role": "user"
        }'
```

Response 200

```
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "user",
  "type": "user"
}
```

# Returns Examples

Response 200

```
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "user",
  "type": "user"
}
```
