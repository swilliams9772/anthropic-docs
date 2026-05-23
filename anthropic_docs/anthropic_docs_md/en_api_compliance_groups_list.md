# List Compliance Groups

**Source:** http://platform.claude.com/docs/en/api/compliance/groups/list

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# List Compliance Groups

GET/v1/compliance/groups

List Compliance Groups

# Query ParametersExpand Collapse

limit: optional number

Maximum results (default: 500, max: 1000)

name\_prefix: optional string

Filter groups by name prefix

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

data: array of object { id, created\_at, description, 4 more }

List of groups

id: string

Group identifier (tagged ID)

created\_at: string

Group creation timestamp (ISO 8601)

description: string

Group description

name: string

Group name

roles: array of string

Role IDs assigned to this group.

source\_type: string

How the group was created ('direct' or 'scim')

updated\_at: string

Group last-updated timestamp (ISO 8601)

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string

Token to retrieve the next page. Use this as the 'page' parameter in your next request

List Compliance Groups

```
curl https://api.anthropic.com/v1/compliance/groups \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "data": [
    {
      "id": "id",
      "created_at": "created_at",
      "description": "description",
      "name": "name",
      "roles": [
        "string"
      ],
      "source_type": "source_type",
      "updated_at": "updated_at"
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
      "created_at": "created_at",
      "description": "description",
      "name": "name",
      "roles": [
        "string"
      ],
      "source_type": "source_type",
      "updated_at": "updated_at"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```
