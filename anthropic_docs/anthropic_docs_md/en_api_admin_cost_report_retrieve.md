# Get Cost Report

**Source:** http://platform.claude.com/docs/en/api/admin/cost_report/retrieve

Copy page

# Get Cost Report

GET/v1/organizations/cost\_report

Get Cost Report

# Query ParametersExpand Collapse

starting\_at: string

Time buckets that start on or after this RFC 3339 timestamp will be returned.
Each time bucket will be snapped to the start of the minute/hour/day in UTC.

bucket\_width: optional "1d"

Time granularity of the response data.

ending\_at: optional string

Time buckets that end before this RFC 3339 timestamp will be returned.

group\_by: optional array of "workspace\_id" or "description"

Group by any subset of the available options.

One of the following:

"workspace\_id"

"description"

limit: optional number

Maximum number of time buckets to return in the response.

page: optional string

Optionally set to the `next_page` token from the previous response.

# Header ParametersExpand Collapse

"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

# ReturnsExpand Collapse

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

Get Cost Report

```
curl https://api.anthropic.com/v1/organizations/cost_report \
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
          "amount": "123.78912",
          "context_window": "0-200k",
          "cost_type": "tokens",
          "currency": "USD",
          "description": "Claude Sonnet 4 Usage - Input Tokens",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "service_tier": "standard",
          "token_type": "uncached_input_tokens",
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
          "amount": "123.78912",
          "context_window": "0-200k",
          "cost_type": "tokens",
          "currency": "USD",
          "description": "Claude Sonnet 4 Usage - Input Tokens",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "service_tier": "standard",
          "token_type": "uncached_input_tokens",
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
