# List Compliance Group Members

**Source:** http://platform.claude.com/docs/en/api/compliance/groups/members/list

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# List Compliance Group Members

GET/v1/compliance/groups/{group\_id}/members

List Compliance Group Members

# Path ParametersExpand Collapse

group\_id: string

The group ID (tagged ID, e.g., rbac\_group\_abc123)

# Query ParametersExpand Collapse

limit: optional number

Maximum results (default: 500, max: 1000)

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

data: array of object { created\_at, email, updated\_at, user\_id }

List of group members

created\_at: string

Membership creation timestamp (ISO 8601)

email: string

Member email address

updated\_at: string

Membership last-updated timestamp (ISO 8601)

user\_id: string

Member user identifier (tagged ID)

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string

Token to retrieve the next page. Use this as the 'page' parameter in your next request

List Compliance Group Members

```
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID/members \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "data": [
    {
      "created_at": "created_at",
      "email": "email",
      "updated_at": "updated_at",
      "user_id": "user_id"
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
      "created_at": "created_at",
      "email": "email",
      "updated_at": "updated_at",
      "user_id": "user_id"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```
