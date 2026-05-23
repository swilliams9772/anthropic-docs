# List Workspace Rate Limits

**Source:** http://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list

Copy page

# List Workspace Rate Limits

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

# Path ParametersExpand Collapse

workspace\_id: string

The ID of the workspace.

# Query ParametersExpand Collapse

group\_type: optional "model\_group" or "batch" or "token\_count" or 3 more

Filter by group type.

One of the following:

"model\_group"

"batch"

"token\_count"

"files"

"skills"

"web\_search"

page: optional string

Opaque cursor from a previous response's `next_page`.

# ReturnsExpand Collapse

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

List Workspace Rate Limits

```
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```
{
  "data": [
    {
      "group_type": "model_group",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "workspace_rate_limit"
    }
  ],
  "next_page": "next_page"
}
```

# Returns Examples

Response 200

```
{
  "data": [
    {
      "group_type": "model_group",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "workspace_rate_limit"
    }
  ],
  "next_page": "next_page"
}
```
