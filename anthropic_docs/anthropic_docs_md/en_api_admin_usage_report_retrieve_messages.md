# Get Messages Usage Report

**Source:** http://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages

Copy page

# Get Messages Usage Report

GET/v1/organizations/usage\_report/messages

Get Messages Usage Report

# Query ParametersExpand Collapse

starting\_at: string

Time buckets that start on or after this RFC 3339 timestamp will be returned.
Each time bucket will be snapped to the start of the minute/hour/day in UTC.

account\_ids: optional array of string

Restrict usage returned to the specified user account ID(s).

api\_key\_ids: optional array of string

Restrict usage returned to the specified API key ID(s).

bucket\_width: optional "1d" or "1m" or "1h"

Time granularity of the response data.

One of the following:

"1d"

"1m"

"1h"

context\_window: optional array of "0-200k" or "200k-1M"

Restrict usage returned to the specified context window(s).

One of the following:

"0-200k"

"200k-1M"

ending\_at: optional string

Time buckets that end before this RFC 3339 timestamp will be returned.

group\_by: optional array of "api\_key\_id" or "workspace\_id" or "model" or 6 more

Group by any subset of the available options. Grouping by `speed` requires the `fast-mode-2026-02-01` beta header.

One of the following:

"api\_key\_id"

"workspace\_id"

"model"

"service\_tier"

"context\_window"

"inference\_geo"

"speed"

"account\_id"

"service\_account\_id"

inference\_geos: optional array of "global" or "us" or "not\_available"

Restrict usage returned to the specified inference geo(s). Use `not_available` for models that do not support specifying `inference_geo`.

One of the following:

"global"

"us"

"not\_available"

limit: optional number

Maximum number of time buckets to return in the response.

The default and max limits depend on `bucket_width`:
• `"1d"`: Default of 7 days, maximum of 31 days
• `"1h"`: Default of 24 hours, maximum of 168 hours
• `"1m"`: Default of 60 minutes, maximum of 1440 minutes

models: optional array of string

Restrict usage returned to the specified model(s).

page: optional string

Optionally set to the `next_page` token from the previous response.

service\_account\_ids: optional array of string

Restrict usage returned to the specified service account ID(s).

service\_tiers: optional array of "standard" or "batch" or "priority" or 3 more

Restrict usage returned to the specified service tier(s).

One of the following:

"standard"

"batch"

"priority"

"priority\_on\_demand"

"flex"

"flex\_discount"

speeds: optional array of "standard" or "fast"

Restrict usage returned to the specified speed(s) (Claude Code research preview).
Requires the `fast-mode-2026-02-01` beta header.

One of the following:

"standard"

"fast"

workspace\_ids: optional array of string

Restrict usage returned to the specified workspace ID(s).

# Header ParametersExpand Collapse

"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

# ReturnsExpand Collapse

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

Get Messages Usage Report

```
curl https://api.anthropic.com/v1/organizations/usage_report/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "account_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "service_account_id": "svac_01Hk3R9TWxq7CfQak00OiVw4",
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"
}
```

# Returns Examples

Response 200

```
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "account_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "service_account_id": "svac_01Hk3R9TWxq7CfQak00OiVw4",
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"
}
```
