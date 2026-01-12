# List Invites - Anthropic

**Source:** https://docs.anthropic.com/en/api/admin-api/invites/list-invites

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

[​](#response-data-id)

data.id

string

required

ID of the Invite.

Examples:

`"invite_015gWxCN9Hfg2QhZwTK7Mdeu"`

[​](#response-data-type)

data.type

enum<string>

default:invite

required

Object type.

For Invites, this is always `"invite"`.

Available options:

`invite`

[​](#response-data-email)

data.email

string

required

Email of the User being invited.

Examples:

`"user@emaildomain.com"`

[​](#response-data-role)

data.role

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

[​](#response-data-invited-at)

data.invited\_at

string

required

RFC 3339 datetime string indicating when the Invite was created.

Examples:

`"2024-10-30T23:58:27.427722Z"`

[​](#response-data-expires-at)

data.expires\_at

string

required

RFC 3339 datetime string indicating when the Invite expires.

Examples:

`"2024-11-20T23:58:27.427722Z"`

[​](#response-data-status)

data.status

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
