# List Workspace Members - Anthropic

**Source:** https://docs.anthropic.com/en/api/admin-api/workspace_members/list-workspace-members

**The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.

# Headers

Your unique Admin API key for authentication.

This key is required in the header of all Admin API requests, to authenticate your account and access Anthropic's services. Get your Admin API key through the [Console](https://console.anthropic.com/settings/admin-keys).

[​](#parameter-anthropic-version)

anthropic-version

string

required

The version of the Anthropic API you want to use.

Read more about versioning and our version history [here](https://docs.anthropic.com/en/api/versioning).

# Path Parameters

[​](#parameter-workspace-id)

workspace\_id

string

required

ID of the Workspace.

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

[​](#response-data-type)

data.type

enum<string>

default:workspace\_member

required

Object type.

For Workspace Members, this is always `"workspace_member"`.

Available options:

`workspace_member`

[​](#response-data-user-id)

data.user\_id

string

required

ID of the User.

Examples:

`"user_01WCz1FkmYMm4gnmykNKUu3Q"`

[​](#response-data-workspace-id)

data.workspace\_id

string

required

ID of the Workspace.

Examples:

`"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"`

[​](#response-data-workspace-role)

data.workspace\_role

enum<string>

required

Role of the Workspace Member.

Available options:

`workspace_user`,

`workspace_developer`,

`workspace_admin`,

`workspace_billing`

Examples:

`"workspace_user"`

`"workspace_developer"`

`"workspace_admin"`

`"workspace_billing"`

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
