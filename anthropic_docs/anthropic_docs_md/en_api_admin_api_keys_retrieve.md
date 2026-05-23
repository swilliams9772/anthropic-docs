# Get API Key

**Source:** http://platform.claude.com/docs/en/api/admin/api_keys/retrieve

Copy page

# Get API Key

GET/v1/organizations/api\_keys/{api\_key\_id}

Get API Key

# Path ParametersExpand Collapse

api\_key\_id: string

ID of the API key.

# ReturnsExpand Collapse

APIKey object { id, created\_at, created\_by, 6 more }

id: string

ID of the API key.

created\_at: string

RFC 3339 datetime string indicating when the API Key was created.

created\_by: object { id, type }

The ID and type of the actor that created the API key.

id: string

ID of the actor that created the object.

type: string

Type of the actor that created the object.

expires\_at: string

RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

name: string

Name of the API key.

partial\_key\_hint: string

Partially redacted hint for the API key.

status: "active" or "inactive" or "archived" or "expired"

Status of the API key.

One of the following:

"active"

"inactive"

"archived"

"expired"

type: "api\_key"

Object type.

For API Keys, this is always `"api_key"`.

workspace\_id: string

ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.

Get API Key

```
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

# Returns Examples

Response 200

```
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```
