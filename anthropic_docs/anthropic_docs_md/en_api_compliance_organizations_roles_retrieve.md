# Get Compliance Role

**Source:** http://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Get Compliance Role

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

Get Compliance Role

# Path ParametersExpand Collapse

org\_uuid: string

The organization UUID

role\_id: string

The role ID (tagged ID, e.g., rbac\_role\_abc123)

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

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

Get Compliance Role

```
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "updated_at": "updated_at"
}
```

# Returns Examples

Response 200

```
{
  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "updated_at": "updated_at"
}
```
