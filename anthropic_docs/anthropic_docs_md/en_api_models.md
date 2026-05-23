# Models

**Source:** http://platform.claude.com/docs/en/api/models

Copy page

cURL

# Models

# [List Models](/docs/en/api/models/list)

GET/v1/models

# [Get a Model](/docs/en/api/models/retrieve)

GET/v1/models/{model\_id}

# ModelsExpand Collapse

CapabilitySupport object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

ContextManagementCapability object { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management capability details.

clear\_thinking\_20251015: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact\_20260112: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

EffortCapability object { high, low, max, 3 more }

Effort (reasoning\_effort) capability details.

high: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

xhigh: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

ModelCapabilities object { batch, citations, code\_execution, 6 more }

Model capability information.

batch: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.

citations: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.

code\_execution: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.

context\_management: [ContextManagementCapability](/docs/en/api/models#context_management_capability) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management support and available strategies.

clear\_thinking\_20251015: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact\_20260112: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort: [EffortCapability](/docs/en/api/models#effort_capability) { high, low, max, 3 more }

Effort (reasoning\_effort) support and available levels.

high: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

xhigh: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

image\_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.

pdf\_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.

structured\_outputs: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.

thinking: [ThinkingCapability](/docs/en/api/models#thinking_capability) { supported, types }

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.

types: [ThinkingTypes](/docs/en/api/models#thinking_types) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

ModelInfo object { id, capabilities, created\_at, 4 more }

id: string

Unique model identifier.

capabilities: [ModelCapabilities](/docs/en/api/models#model_capabilities) { batch, citations, code\_execution, 6 more }

Model capability information.

batch: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.

citations: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.

code\_execution: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.

context\_management: [ContextManagementCapability](/docs/en/api/models#context_management_capability) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management support and available strategies.

clear\_thinking\_20251015: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact\_20260112: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort: [EffortCapability](/docs/en/api/models#effort_capability) { high, low, max, 3 more }

Effort (reasoning\_effort) support and available levels.

high: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

xhigh: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

image\_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.

pdf\_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.

structured\_outputs: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.

thinking: [ThinkingCapability](/docs/en/api/models#thinking_capability) { supported, types }

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.

types: [ThinkingTypes](/docs/en/api/models#thinking_types) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

created\_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: string

A human-readable name for the model.

max\_input\_tokens: number

Maximum input context window size in tokens for this model.

max\_tokens: number

Maximum value for the `max_tokens` parameter when using this model.

type: "model"

Object type.

For Models, this is always `"model"`.

ThinkingCapability object { supported, types }

Thinking capability details.

supported: boolean

Whether this capability is supported by the model.

types: [ThinkingTypes](/docs/en/api/models#thinking_types) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

ThinkingTypes object { adaptive, enabled }

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.
