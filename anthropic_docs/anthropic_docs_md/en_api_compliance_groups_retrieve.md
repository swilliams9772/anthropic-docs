# Get Compliance Group

**Source:** http://platform.claude.com/docs/en/api/compliance/groups/retrieve

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Get Compliance Group

GET/v1/compliance/groups/{group\_id}

Get Compliance Group

# Path ParametersExpand Collapse

group\_id: string

The group ID (tagged ID, e.g., rbac\_group\_abc123)

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

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

Get Compliance Group

```
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
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
```

# Returns Examples

Response 200

```
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
```
