# List organization users

**Source:** http://platform.claude.com/docs/en/api/compliance/organizations/users/list

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# List organization users

GET/v1/compliance/organizations/{org\_uuid}/users

List current user members of an organization.

Returns:
List of user members with pagination info

# Path ParametersExpand Collapse

org\_uuid: string

The organization UUID

# Query ParametersExpand Collapse

limit: optional number

Maximum results (default: 500, max: 1000)

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

data: array of object { id, created\_at, email, 2 more }

List of current organization members sorted by organization join date ascending

id: string

User identifier (tagged ID)

created\_at: string

User account creation timestamp

email: string

User's current email address

full\_name: string

User's current full name

organization\_role: "admin" or "billing" or "claude\_code\_user" or 6 more

User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

One of the following:

"admin"

"billing"

"claude\_code\_user"

"developer"

"managed"

"membership\_admin"

"owner"

"primary\_owner"

"user"

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string

Token to retrieve the next page. Use this as the 'page' parameter in your next request

List organization users

```
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "email": "email",
      "full_name": "full_name",
      "organization_role": "admin"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

# Returns Examples

Response 200

```
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "email": "email",
      "full_name": "full_name",
      "organization_role": "admin"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```
