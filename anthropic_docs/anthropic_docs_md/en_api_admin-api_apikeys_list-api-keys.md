# List Api Keys

**Source:** https://platform.claude.com/docs/en/api/admin-api/apikeys/list-api-keys

Copy page

# List Api Keys

get/v1/organizations/api\_keys

List Api Keys

# Query ParametersExpand Collapse

after\_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before\_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

created\_by\_user\_id: optional string

Filter by the ID of the User who created the object.

limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

status: optional "active" or "inactive" or "archived"

Filter by API key status.

Accepts one of the following:

"active"

"inactive"

"archived"

workspace\_id: optional string

Filter by Workspace ID.

# ReturnsExpand Collapse

data: array of [APIKey](/docs/en/api/$shared#apiKey) { id, created\_at, created\_by, 5 more }

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

first\_id: string

First ID in the `data` list. Can be used as the `before_id` for the previous page.

has\_more: boolean

Indicates if there are more results in the requested page direction.

last\_id: string

Last ID in the `data` list. Can be used as the `after_id` for the next page.

List Api Keys

```
curl https://api.anthropic.com/v1/organizations/api_keys \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```
{
  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

# Returns Examples

Response 200

```
{
  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```
