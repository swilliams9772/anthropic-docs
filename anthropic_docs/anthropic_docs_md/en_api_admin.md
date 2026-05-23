# Admin

**Source:** http://platform.claude.com/docs/en/api/admin

Copy page

# Admin

# AdminOrganizations

# [Get Current Organization](/docs/en/api/admin/organizations/me)

GET/v1/organizations/me

# ModelsExpand Collapse

Organization object { id, name, type }

id: string

ID of the Organization.

name: string

Name of the Organization.

type: "organization"

Object type.

For Organizations, this is always `"organization"`.

# AdminInvites

# [Create Invite](/docs/en/api/admin/invites/create)

POST/v1/organizations/invites

# [Get Invite](/docs/en/api/admin/invites/retrieve)

GET/v1/organizations/invites/{invite\_id}

# [List Invites](/docs/en/api/admin/invites/list)

GET/v1/organizations/invites

# [Delete Invite](/docs/en/api/admin/invites/delete)

DELETE/v1/organizations/invites/{invite\_id}

# ModelsExpand Collapse

Invite object { id, email, expires\_at, 4 more }

id: string

ID of the Invite.

email: string

Email of the User being invited.

expires\_at: string

RFC 3339 datetime string indicating when the Invite expires.

invited\_at: string

RFC 3339 datetime string indicating when the Invite was created.

role: "user" or "developer" or "billing" or 2 more

Organization role of the User.

One of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"

status: "accepted" or "expired" or "deleted" or "pending"

Status of the Invite.

One of the following:

"accepted"

"expired"

"deleted"

"pending"

type: "invite"

Object type.

For Invites, this is always `"invite"`.

InviteDeleteResponse object { id, type }

id: string

ID of the Invite.

type: "invite\_deleted"

Deleted object type.

For Invites, this is always `"invite_deleted"`.

# AdminUsers

# [Get User](/docs/en/api/admin/users/retrieve)

GET/v1/organizations/users/{user\_id}

# [List Users](/docs/en/api/admin/users/list)

GET/v1/organizations/users

# [Update User](/docs/en/api/admin/users/update)

POST/v1/organizations/users/{user\_id}

# [Remove User](/docs/en/api/admin/users/delete)

DELETE/v1/organizations/users/{user\_id}

# ModelsExpand Collapse

User object { id, added\_at, email, 3 more }

id: string

ID of the User.

added\_at: string

RFC 3339 datetime string indicating when the User joined the Organization.

email: string

Email of the User.

name: string

Name of the User.

role: "user" or "developer" or "billing" or 2 more

Organization role of the User.

One of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"

type: "user"

Object type.

For Users, this is always `"user"`.

UserDeleteResponse object { id, type }

id: string

ID of the User.

type: "user\_deleted"

Deleted object type.

For Users, this is always `"user_deleted"`.

# AdminWorkspaces

# [Create Workspace](/docs/en/api/admin/workspaces/create)

POST/v1/organizations/workspaces

# [Get Workspace](/docs/en/api/admin/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace\_id}

# [List Workspaces](/docs/en/api/admin/workspaces/list)

GET/v1/organizations/workspaces

# [Update Workspace](/docs/en/api/admin/workspaces/update)

POST/v1/organizations/workspaces/{workspace\_id}

# [Archive Workspace](/docs/en/api/admin/workspaces/archive)

POST/v1/organizations/workspaces/{workspace\_id}/archive

# AdminWorkspacesMembers

# [Create Workspace Member](/docs/en/api/admin/workspaces/members/create)

POST/v1/organizations/workspaces/{workspace\_id}/members

# [Get Workspace Member](/docs/en/api/admin/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

# [List Workspace Members](/docs/en/api/admin/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace\_id}/members

# [Update Workspace Member](/docs/en/api/admin/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

# [Delete Workspace Member](/docs/en/api/admin/workspaces/members/delete)

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

# ModelsExpand Collapse

WorkspaceMember object { type, user\_id, workspace\_id, workspace\_role }

type: "workspace\_member"

Object type.

For Workspace Members, this is always `"workspace_member"`.

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the Workspace Member.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"

MemberDeleteResponse object { type, user\_id, workspace\_id }

type: "workspace\_member\_deleted"

Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

# AdminWorkspacesRate Limits

# [List Workspace Rate Limits](/docs/en/api/admin/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

# ModelsExpand Collapse

RateLimitListResponse object { data, next\_page }

data: array of object { group\_type, limits, models, type }

Rate-limit entries for the workspace, one per group that has at least one override.

group\_type: "model\_group" or "batch" or "token\_count" or 3 more

The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

One of the following:

"model\_group"

"batch"

"token\_count"

"files"

"skills"

"web\_search"

limits: array of object { org\_limit, type, value }

The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

org\_limit: number

The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

type: string

The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number

The workspace-level override value for this limiter type.

models: array of string

Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

type: "workspace\_rate\_limit"

Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

# AdminAPI Keys

# [Get API Key](/docs/en/api/admin/api_keys/retrieve)

GET/v1/organizations/api\_keys/{api\_key\_id}

# [List API Keys](/docs/en/api/admin/api_keys/list)

GET/v1/organizations/api\_keys

# [Update API Key](/docs/en/api/admin/api_keys/update)

POST/v1/organizations/api\_keys/{api\_key\_id}

# AdminUsage Report

# [Get Messages Usage Report](/docs/en/api/admin/usage_report/retrieve_messages)

GET/v1/organizations/usage\_report/messages

# [Get Claude Code Usage Report](/docs/en/api/admin/usage_report/retrieve_claude_code)

GET/v1/organizations/usage\_report/claude\_code

# ModelsExpand Collapse

ClaudeCodeUsageReport object { data, has\_more, next\_page }

data: array of object { actor, core\_metrics, customer\_type, 6 more }

List of Claude Code usage records for the requested date.

actor: object { email\_address, type }  or object { api\_key\_name, type }

The user or API key that performed the Claude Code actions.

One of the following:

UserActor object { email\_address, type }

email\_address: string

Email address of the user who performed Claude Code actions.

type: "user\_actor"

APIActor object { api\_key\_name, type }

api\_key\_name: string

Name of the API key used to perform Claude Code actions.

type: "api\_actor"

core\_metrics: object { commits\_by\_claude\_code, lines\_of\_code, num\_sessions, pull\_requests\_by\_claude\_code }

Core productivity metrics measuring Claude Code usage and impact.

commits\_by\_claude\_code: number

Number of git commits created through Claude Code's commit functionality.

lines\_of\_code: object { added, removed }

Statistics on code changes made through Claude Code.

added: number

Total number of lines of code added across all files by Claude Code.

removed: number

Total number of lines of code removed across all files by Claude Code.

num\_sessions: number

Number of distinct Claude Code sessions initiated by this actor.

pull\_requests\_by\_claude\_code: number

Number of pull requests created through Claude Code's PR functionality.

customer\_type: "api" or "subscription"

Type of customer account (api for API customers, subscription for Pro/Team customers).

One of the following:

"api"

"subscription"

date: string

UTC date for the usage metrics in YYYY-MM-DD format.

model\_breakdown: array of object { estimated\_cost, model, tokens }

Token usage and cost breakdown by AI model used.

estimated\_cost: object { amount, currency }

Estimated cost for using this model

amount: number

Estimated cost amount in minor currency units (e.g., cents for USD).

currency: string

Currency code for the estimated cost (e.g., 'USD').

model: string

Name of the AI model used for Claude Code interactions.

tokens: object { cache\_creation, cache\_read, input, output }

Token usage breakdown for this model

cache\_creation: number

Number of cache creation tokens consumed by this model.

cache\_read: number

Number of cache read tokens consumed by this model.

input: number

Number of input tokens consumed by this model.

output: number

Number of output tokens generated by this model.

organization\_id: string

ID of the organization that owns the Claude Code usage.

terminal\_type: string

Type of terminal or environment where Claude Code was used.

tool\_actions: map[object { accepted, rejected } ]

Breakdown of tool action acceptance and rejection rates by tool type.

accepted: number

Number of tool action proposals that the user accepted.

rejected: number

Number of tool action proposals that the user rejected.

subscription\_type: optional "enterprise" or "team"

Subscription tier for subscription customers. `null` for API customers.

One of the following:

"enterprise"

"team"

has\_more: boolean

True if there are more records available beyond the current page.

next\_page: string

Opaque cursor token for fetching the next page of results, or null if no more pages are available.

MessagesUsageReport object { data, has\_more, next\_page }

data: array of object { ending\_at, results, starting\_at }

ending\_at: string

End of the time bucket (exclusive) in RFC 3339 format.

results: array of object { account\_id, api\_key\_id, cache\_creation, 10 more }

List of usage items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

account\_id: string

ID of the user account that made the request. `null` if not grouping by account or for non-OAuth requests.

api\_key\_id: string

ID of the API key used. `null` if not grouping by API key or for usage in the Anthropic Console.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

The number of input tokens for cache creation.

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

context\_window: "0-200k" or "200k-1M"

Context window used. `null` if not grouping by context window.

One of the following:

"0-200k"

"200k-1M"

inference\_geo: string

Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

model: string

Model used. `null` if not grouping by model.

output\_tokens: number

The number of output tokens generated.

server\_tool\_use: object { web\_search\_requests }

Server-side tool usage metrics.

web\_search\_requests: number

The number of web search requests made.

service\_account\_id: string

ID of the service account that made the request. `null` if not grouping by service account or for non-OIDC-federation requests.

service\_tier: "standard" or "batch" or "priority" or 3 more

Service tier used. `null` if not grouping by service tier.

One of the following:

"standard"

"batch"

"priority"

"priority\_on\_demand"

"flex"

"flex\_discount"

uncached\_input\_tokens: number

The number of uncached input tokens processed.

workspace\_id: string

ID of the Workspace used. `null` if not grouping by workspace or for the default workspace.

starting\_at: string

Start of the time bucket (inclusive) in RFC 3339 format.

has\_more: boolean

Indicates if there are more results.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

# AdminCost Report

# [Get Cost Report](/docs/en/api/admin/cost_report/retrieve)

GET/v1/organizations/cost\_report

# ModelsExpand Collapse

CostReport object { data, has\_more, next\_page }

data: array of object { ending\_at, results, starting\_at }

ending\_at: string

End of the time bucket (exclusive) in RFC 3339 format.

results: array of object { amount, context\_window, cost\_type, 7 more }

List of cost items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

amount: string

Cost amount in lowest currency units (e.g. cents) as a decimal string. For example, `"123.45"` in `"USD"` represents `$1.23`.

context\_window: "0-200k" or "200k-1M"

Input context window used. `null` if not grouping by description or for non-token costs.

One of the following:

"0-200k"

"200k-1M"

cost\_type: "tokens" or "web\_search" or "code\_execution" or "session\_usage"

Type of cost. `null` if not grouping by description.

One of the following:

"tokens"

"web\_search"

"code\_execution"

"session\_usage"

currency: string

Currency code for the cost amount. Currently always `"USD"`.

description: string

Description of the cost item. `null` if not grouping by description.

inference\_geo: string

Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

model: string

Model name used. `null` if not grouping by description or for non-token costs.

service\_tier: "standard" or "batch"

Service tier used. `null` if not grouping by description or for non-token costs.

One of the following:

"standard"

"batch"

token\_type: "uncached\_input\_tokens" or "output\_tokens" or "cache\_read\_input\_tokens" or 2 more

Type of token. `null` if not grouping by description or for non-token costs.

One of the following:

"uncached\_input\_tokens"

"output\_tokens"

"cache\_read\_input\_tokens"

"cache\_creation.ephemeral\_1h\_input\_tokens"

"cache\_creation.ephemeral\_5m\_input\_tokens"

workspace\_id: string

ID of the Workspace this cost is associated with. `null` if not grouping by workspace or for the default workspace.

starting\_at: string

Start of the time bucket (inclusive) in RFC 3339 format.

has\_more: boolean

Indicates if there are more results.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

# AdminRate Limits

# [List Organization Rate Limits](/docs/en/api/admin/rate_limits/list)

GET/v1/organizations/rate\_limits

# ModelsExpand Collapse

RateLimitListResponse object { data, next\_page }

data: array of object { group\_type, limits, models, type }

Rate-limit entries for the organization, one per group.

group\_type: "model\_group" or "batch" or "token\_count" or 3 more

The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

One of the following:

"model\_group"

"batch"

"token\_count"

"files"

"skills"

"web\_search"

limits: array of object { type, value }

The limiter values that apply to this group.

type: string

The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number

The configured limit value for this limiter type.

models: array of string

Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

type: "rate\_limit"

Object type. Always `rate_limit` for organization rate-limit entries.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

# AdminMCP Tunnels

# [Get Tunnel](/docs/en/api/admin/mcp_tunnels/retrieve)

GET/v1/organizations/tunnels/{tunnel\_id}

# [List Tunnels](/docs/en/api/admin/mcp_tunnels/list)

GET/v1/organizations/tunnels

# [Reveal Tunnel Token](/docs/en/api/admin/mcp_tunnels/reveal_token)

POST/v1/organizations/tunnels/{tunnel\_id}/reveal\_token

# [Rotate Tunnel Token](/docs/en/api/admin/mcp_tunnels/rotate_token)

POST/v1/organizations/tunnels/{tunnel\_id}/rotate\_token

# [Archive Tunnel](/docs/en/api/admin/mcp_tunnels/archive)

POST/v1/organizations/tunnels/{tunnel\_id}/archive

# ModelsExpand Collapse

MCPTunnelRetrieveResponse object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel.

archived\_at: string

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

display\_name: string

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.

type: "tunnel"

Object type. Always `tunnel` for Tunnels.

workspace\_id: string

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.

MCPTunnelListResponse object { data, next\_page }

data: array of object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel.

archived\_at: string

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

display\_name: string

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.

type: "tunnel"

Object type. Always `tunnel` for Tunnels.

workspace\_id: string

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.

next\_page: string

Opaque cursor for the next page, or `null` if there are no more results.

MCPTunnelRevealTokenResponse object { id, tunnel\_token, type }

id: string

Stable identifier for the current token value. Changes when the token is
rotated.

tunnel\_token: string

The tunnel's connection token.

type: "tunnel\_token"

Object type. Always `tunnel_token` for Tunnel Tokens.

MCPTunnelRotateTokenResponse object { id, tunnel\_token, type }

id: string

Stable identifier for the current token value. Changes when the token is
rotated.

tunnel\_token: string

The tunnel's connection token.

type: "tunnel\_token"

Object type. Always `tunnel_token` for Tunnel Tokens.

MCPTunnelArchiveResponse object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel.

archived\_at: string

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

display\_name: string

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.

type: "tunnel"

Object type. Always `tunnel` for Tunnels.

workspace\_id: string

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.

# AdminMCP TunnelsTunnel Certificates

# [Create Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create)

POST/v1/organizations/tunnels/{tunnel\_id}/certificates

# [Get Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/retrieve)

GET/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}

# [List Tunnel Certificates](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list)

GET/v1/organizations/tunnels/{tunnel\_id}/certificates

# [Archive Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive)

POST/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

# ModelsExpand Collapse

TunnelCertificateCreateResponse object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

TunnelCertificateRetrieveResponse object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

TunnelCertificateListResponse object { data, next\_page }

data: array of object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

next\_page: string

Opaque cursor for the next page, or `null` if there are no more results.

TunnelCertificateArchiveResponse object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.
