# List API Keys - Anthropic

**Source:** https://docs.anthropic.com/en/api/admin-api/apikeys/list-api-keys

# Headers

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the [Console](https://console.anthropic.com/settings/admin-keys).

[​](#parameter-anthropic-version)

anthropic-version

string

required

The version of the Anthropic API you want to use.

Read more about versioning and our version history [here](https://docs.anthropic.com/en/api/versioning).

# Query Parameters

[​](#parameter-before-id)

before\_id

string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

[​](#parameter-after-id)

after\_id

string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

[​](#parameter-limit)

limit

integer

default:20

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

Required range: `1 <= x <= 1000`

[​](#parameter-workspace-id)

workspace\_id

string | null

Filter by Workspace ID.

[​](#parameter-created-by-user-id)

created\_by\_user\_id

string | null

Filter by the ID of the User who created the object.

# Response

200

2004XX

application/json

Successful Response

[​](#response-data)

data

object[]

required

Show child attributes

[​](#response-data-workspace-id)

data.workspace\_id

string | null

required

ID of the Workspace associated with the API key, or null if the API key belongs to the default Workspace.

Examples:

`"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"`

[​](#response-data-created-at)

data.created\_at

string

required

Examples:

`"2024-10-30T23:58:27.427722Z"`

[​](#response-data-created-by)

data.created\_by

object

required

Show child attributes

[​](#response-data-created-by-id)

data.created\_by.id

string

required

ID of the actor that created the object.

Examples:

`"user_01WCz1FkmYMm4gnmykNKUu3Q"`

[​](#response-data-created-by-type)

data.created\_by.type

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

[​](#response-data-partial-key-hint)

data.partial\_key\_hint

string | null

required

[​](#response-data-status)

data.status

enum<string>

required

[​](#response-has-more)

has\_more

boolean

required

Indicates if there are more results in the requested page direction.

[​](#response-first-id)

first\_id

string | null

required

First ID in the `data` list. Can be used as the `before_id` for the previous page.

[​](#response-last-id)

last\_id

string | null

required

Last ID in the `data` list. Can be used as the `after_id` for the next page.
