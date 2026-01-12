# Update Api Key

**Source:** https://platform.claude.com/docs/en/api/admin/api_keys/update

Copy page

# Update Api Key

post/v1/organizations/api\_keys/{api\_key\_id}

Update Api Key

# Path ParametersExpand Collapse

api\_key\_id: string

ID of the API key.

# Body ParametersExpand Collapse

name: optional string

Name of the API key.

maxLength500

minLength1

status: optional "active" or "inactive" or "archived"

Status of the API key.

Accepts one of the following:

"active"

"inactive"

"archived"

# ReturnsExpand Collapse

APIKey = object { id, created\_at, created\_by, 5 more }

id: string

ID of the API key.

created\_at: string

RFC 3339 datetime string indicating when the API Key was created.

formatdate-time

created\_by: object { id, type }

The ID and type of the actor that created the API key.

id: string

ID of the actor that created the object.

type: string

Type of the actor that created the object.

name: string

Name of the API key.

partial\_key\_hint: string

Partially redacted hint for the API key.

status: "active" or "inactive" or "archived"

Status of the API key.

Accepts one of the following:

"active"

"inactive"

"archived"

type: "api\_key"

Object type.

For API Keys, this is always `"api_key"`.

Accepts one of the following:

"api\_key"

workspace\_id: string

ID of the Workspace associated with the API key, or null if the API key belongs to the default Workspace.

Update Api Key

```
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'Content-Type: application/json' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{}'
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
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```
