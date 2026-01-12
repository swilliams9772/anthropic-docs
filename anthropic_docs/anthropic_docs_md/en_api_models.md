# Models

**Source:** https://platform.claude.com/docs/en/api/models

Copy page

cURL

# Models

# [List Models](/docs/en/api/models/list)

get/v1/models

# [Get a Model](/docs/en/api/models/retrieve)

get/v1/models/{model\_id}

# ModelsExpand Collapse

ModelInfo = object { id, created\_at, display\_name, type }

id: string

Unique model identifier.

created\_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

display\_name: string

A human-readable name for the model.

type: "model"

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

"model"
