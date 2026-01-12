# Update API Keys - Anthropic

**Source:** https://docs.anthropic.com/en/api/admin-api/apikeys/update-api-key

# Headers

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the [Console](https://console.anthropic.com/settings/admin-keys).

[​](#parameter-anthropic-version)

anthropic-version

string

required

The version of the Anthropic API you want to use.

Read more about versioning and our version history [here](https://docs.anthropic.com/en/api/versioning).

# Body

application/json

# Response

200

2004XX

application/json

Successful Response

[​](#response-workspace-id)

workspace\_id

string | null

required

ID of the Workspace associated with the API key, or null if the API key belongs to the default Workspace.

Examples:

`"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"`

[​](#response-created-at)

created\_at

string

required

Examples:

`"2024-10-30T23:58:27.427722Z"`

[​](#response-created-by)

created\_by

object

required

Show child attributes

[​](#response-created-by-id)

created\_by.id

string

required

ID of the actor that created the object.

Examples:

`"user_01WCz1FkmYMm4gnmykNKUu3Q"`

[​](#response-created-by-type)

created\_by.type

string

required

Type of the actor that created the object.

Examples:

`"user"`

Examples:

```
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user"
}

```

[​](#response-partial-key-hint)

partial\_key\_hint

string | null

required

[​](#response-status)

status

enum<string>

required
