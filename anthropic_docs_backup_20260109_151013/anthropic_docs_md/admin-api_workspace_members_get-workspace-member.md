# Get Workspace Member - Anthropic

**Source:** https://docs.anthropic.com/en/api/admin-api/workspace_members/get-workspace-member

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

[​](#parameter-user-id)

user\_id

string

required

ID of the User.

[​](#parameter-workspace-id)

workspace\_id

string

required

ID of the Workspace.

# Response

200

2004XX

application/json

Successful Response

[​](#response-type)

type

enum<string>

default:workspace\_member

required

Object type.

For Workspace Members, this is always `"workspace_member"`.

Available options:

`workspace_member`

[​](#response-user-id)

user\_id

string

required

ID of the User.

Examples:

`"user_01WCz1FkmYMm4gnmykNKUu3Q"`

[​](#response-workspace-id)

workspace\_id

string

required

ID of the Workspace.

Examples:

`"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"`

[​](#response-workspace-role)

workspace\_role

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
