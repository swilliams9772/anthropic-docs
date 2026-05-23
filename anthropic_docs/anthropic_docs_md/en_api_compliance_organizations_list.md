# List organizations

**Source:** http://platform.claude.com/docs/en/api/compliance/organizations/list

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# List organizations

GET/v1/compliance/organizations

List organizations under the parent organization.

Returns a list of organizations sorted by creation date in ascending order.
This endpoint does not support pagination and will return an error if the
response would exceed 1,000 organizations.

# Header ParametersExpand Collapse

"x-api-key": optional string

# ReturnsExpand Collapse

data: array of object { created\_at, name, uuid }

List of organizations sorted by creation date, ascending

created\_at: string

Organization creation time (RFC 3339 format)

name: string

Organization name

uuid: string

Unique identifier for the organization (UUID format)

List organizations

```
curl https://api.anthropic.com/v1/compliance/organizations \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```
{
  "data": [
    {
      "created_at": "created_at",
      "name": "name",
      "uuid": "uuid"
    }
  ]
}
```

# Returns Examples

Response 200

```
{
  "data": [
    {
      "created_at": "created_at",
      "name": "name",
      "uuid": "uuid"
    }
  ]
}
```
