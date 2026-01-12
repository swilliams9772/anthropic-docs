# Get Invite - Anthropic

**Source:** https://docs.anthropic.com/en/api/admin-api/invites/get-invite

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

[​](#parameter-invite-id)

invite\_id

string

required

ID of the Invite.

# Response

200

2004XX

application/json

Successful Response

[​](#response-id)

id

string

required

ID of the Invite.

Examples:

`"invite_015gWxCN9Hfg2QhZwTK7Mdeu"`

[​](#response-type)

type

enum<string>

default:invite

required

Object type.

For Invites, this is always `"invite"`.

Available options:

`invite`

[​](#response-email)

email

string

required

Email of the User being invited.

Examples:

`"user@emaildomain.com"`

[​](#response-role)

role

enum<string>

required

Organization role of the User.

Available options:

`user`,

`developer`,

`billing`,

`admin`

Examples:

`"user"`

`"developer"`

`"billing"`

`"admin"`

[​](#response-invited-at)

invited\_at

string

required

RFC 3339 datetime string indicating when the Invite was created.

Examples:

`"2024-10-30T23:58:27.427722Z"`

[​](#response-expires-at)

expires\_at

string

required

RFC 3339 datetime string indicating when the Invite expires.

Examples:

`"2024-11-20T23:58:27.427722Z"`

[​](#response-status)

status

enum<string>

required

Status of the Invite.

Available options:

`accepted`,

`expired`,

`deleted`,

`pending`

Examples:

`"pending"`
