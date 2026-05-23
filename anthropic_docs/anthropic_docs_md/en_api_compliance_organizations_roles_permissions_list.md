# List Compliance Role Permissions

**Source:** http://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# List Compliance Role Permissions

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}/permissions

List Compliance Role Permissions

# Path ParametersExpand Collapse

org\_uuid: string

The organization UUID

role\_id: string

The role ID (tagged ID, e.g., rbac\_role\_abc123)

# Query ParametersExpand Collapse

limit: optional number

Maximum results (default: 500, max: 1000)

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

data: array of object { action, resource\_id, resource\_type }

List of permissions

action: string

Action permitted on the resource

resource\_id: string

Identifier of the resource the permission applies to

resource\_type: string

Type of resource the permission applies to

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string

Token to retrieve the next page. Use this as the 'page' parameter in your next request

List Compliance Role Permissions

```
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID/permissions \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "data": [
    {
      "action": "action",
      "resource_id": "resource_id",
      "resource_type": "resource_type"
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
      "action": "action",
      "resource_id": "resource_id",
      "resource_type": "resource_type"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```
