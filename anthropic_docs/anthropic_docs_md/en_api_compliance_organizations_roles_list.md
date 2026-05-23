# List Compliance Roles

**Source:** http://platform.claude.com/docs/en/api/compliance/organizations/roles/list

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# List Compliance Roles

GET/v1/compliance/organizations/{org\_uuid}/roles

List Compliance Roles

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

data: array of object { id, created\_at, description, 2 more }

List of roles

id: string

Role identifier (tagged ID)

created\_at: string

Role creation timestamp (ISO 8601)

description: string

Role description

name: string

Role name

updated\_at: string

Role last-updated timestamp (ISO 8601)

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string

Token to retrieve the next page. Use this as the 'page' parameter in your next request

List Compliance Roles

```
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles \
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
      "updated_at": "updated_at"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```
