# Get User - Anthropic

**Source:** https://docs.anthropic.com/en/api/admin-api/users/get-user

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

# Response

200

2004XX

application/json

Successful Response

[​](#response-id)

id

string

required

ID of the User.

Examples:

`"user_01WCz1FkmYMm4gnmykNKUu3Q"`

[​](#response-type)

type

enum<string>

default:user

required

Object type.

For Users, this is always `"user"`.

Available options:

`user`

[​](#response-email)

email

string

required

Email of the User.

Examples:

`"user@emaildomain.com"`

[​](#response-name)

name

string

required

Name of the User.

Examples:

`"Jane Doe"`

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

[​](#response-added-at)

added\_at

string

required

RFC 3339 datetime string indicating when the User joined the Organization.

Examples:

`"2024-10-30T23:58:27.427722Z"`
