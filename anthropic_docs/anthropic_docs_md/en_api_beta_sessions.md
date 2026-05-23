# Sessions

**Source:** https://platform.claude.com/docs/en/api/beta/sessions

Copy page

cURL

# Sessions

# [Create Session](/docs/en/api/beta/sessions/create)

POST/v1/sessions

# [List Sessions](/docs/en/api/beta/sessions/list)

GET/v1/sessions

# [Get Session](/docs/en/api/beta/sessions/retrieve)

GET/v1/sessions/{session\_id}

# [Update Session](/docs/en/api/beta/sessions/update)

POST/v1/sessions/{session\_id}

# [Delete Session](/docs/en/api/beta/sessions/delete)

DELETE/v1/sessions/{session\_id}

# [Archive Session](/docs/en/api/beta/sessions/archive)

POST/v1/sessions/{session\_id}/archive

# ModelsExpand Collapse

BetaManagedAgentsAgentParams object { id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.

type: "agent"

version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

BetaManagedAgentsBranchCheckout object { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCacheCreationUsage object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

BetaManagedAgentsCommitCheckout object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsDeletedSession object { id, type }

Confirmation that a `session` has been permanently deleted.

id: string

type: "session\_deleted"

BetaManagedAgentsFileResourceParams object { file\_id, type, mount\_path }

Mount a file uploaded via the Files API into the session.

file\_id: string

ID of a previously uploaded file.

type: "file"

mount\_path: optional string

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

BetaManagedAgentsGitHubRepositoryResourceParams object { authorization\_token, type, url, 2 more }

Mount a GitHub repository into the session's container.

authorization\_token: string

GitHub authorization token used to clone the repository.

type: "github\_repository"

url: string

Github URL of the repository

checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type }

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:

BetaManagedAgentsBranchCheckout object { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

mount\_path: optional string

Mount path in the container. Defaults to `/workspace/<repo-name>`.

BetaManagedAgentsMemoryStoreResourceParam object { memory\_store\_id, type, access, instructions }

Parameters for attaching a memory store to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"

access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

BetaManagedAgentsMultiagent object { agents, type }

Resolved coordinator topology with a concrete agent roster.

agents: array of [BetaManagedAgentsAgentReference](/docs/en/api/beta#beta_managed_agents_agent_reference) { id, type, version }

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: string

type: "agent"

version: number

type: "coordinator"

BetaManagedAgentsMultiagentParams object { agents, type }

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

agents: array of [BetaManagedAgentsMultiagentRosterEntryParams](/docs/en/api/beta#beta_managed_agents_multiagent_roster_entry_params)

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

One of the following:

string

BetaManagedAgentsAgentParams object { id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.

type: "agent"

version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

BetaManagedAgentsMultiagentSelfParams object { type }

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: "self"

type: "coordinator"

BetaManagedAgentsMultiagentRosterEntryParams = string or [BetaManagedAgentsAgentParams](/docs/en/api/beta#beta_managed_agents_agent_params) { id, type, version }  or [BetaManagedAgentsMultiagentSelfParams](/docs/en/api/beta#beta_managed_agents_multiagent_self_params) { type }

An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

One of the following:

string

BetaManagedAgentsAgentParams object { id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.

type: "agent"

version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

BetaManagedAgentsMultiagentSelfParams object { type }

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: "self"

BetaManagedAgentsOutcomeEvaluationResource object { completed\_at, description, explanation, 4 more }

Evaluation state for a single outcome defined via a define\_outcome event.

completed\_at: string

A timestamp in RFC 3339 format

description: string

What the agent should produce.

explanation: string

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

iteration: number

0-indexed revision cycle the outcome is currently on.

outcome\_id: string

Server-generated outc\_ ID for this outcome.

result: string

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

type: "outcome\_evaluation"

BetaManagedAgentsSession object { id, agent, archived\_at, 12 more }

A Managed Agents `session`.

id: string

agent: [BetaManagedAgentsSessionAgent](/docs/en/api/beta#beta_managed_agents_session_agent) { id, description, mcp\_servers, 8 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](/docs/en/api/beta#beta_managed_agents_session_multiagent_coordinator) { agents, type }

Resolved coordinator topology with full agent definitions for each roster member.

agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp\_servers, 7 more }

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

environment\_id: string

metadata: map[string]

outcome\_evaluations: array of [BetaManagedAgentsOutcomeEvaluationResource](/docs/en/api/beta#beta_managed_agents_outcome_evaluation_resource) { completed\_at, description, explanation, 4 more }

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

completed\_at: string

A timestamp in RFC 3339 format

description: string

What the agent should produce.

explanation: string

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

iteration: number

0-indexed revision cycle the outcome is currently on.

outcome\_id: string

Server-generated outc\_ ID for this outcome.

result: string

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

type: "outcome\_evaluation"

resources: array of [BetaManagedAgentsSessionResource](/docs/en/api/beta#beta_managed_agents_session_resource)

One of the following:

BetaManagedAgentsGitHubRepositoryResource object { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type }

One of the following:

BetaManagedAgentsBranchCheckout object { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource object { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

BetaManagedAgentsMemoryStoreResource object { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"

access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

description: optional string

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: optional string

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: optional string

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

stats: [BetaManagedAgentsSessionStats](/docs/en/api/beta#beta_managed_agents_session_stats) { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds: optional number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: optional number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

status: "rescheduling" or "running" or "idle" or "terminated"

SessionStatus enum

One of the following:

"rescheduling"

"running"

"idle"

"terminated"

title: string

type: "session"

updated\_at: string

A timestamp in RFC 3339 format

usage: [BetaManagedAgentsSessionUsage](/docs/en/api/beta#beta_managed_agents_session_usage) { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation: optional [BetaManagedAgentsCacheCreationUsage](/docs/en/api/beta#beta_managed_agents_cache_creation_usage) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: optional number

Total tokens read from prompt cache.

input\_tokens: optional number

Total input tokens consumed across all turns.

output\_tokens: optional number

Total output tokens generated across all turns.

vault\_ids: array of string

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

BetaManagedAgentsSessionAgent object { id, description, mcp\_servers, 8 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](/docs/en/api/beta#beta_managed_agents_session_multiagent_coordinator) { agents, type }

Resolved coordinator topology with full agent definitions for each roster member.

agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp\_servers, 7 more }

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

BetaManagedAgentsSessionAgentUpdate object { mcp\_servers, tools }

Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

mcp\_servers: optional array of [BetaManagedAgentsURLMCPServerParams](/docs/en/api/beta#beta_managed_agents_url_mcp_server_params) { name, type, url }

Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

name: string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: "url"

url: string

Endpoint URL for the MCP server.

tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401_params) { type, configs, default\_config }  or [BetaManagedAgentsMCPToolsetParams](/docs/en/api/beta#beta_managed_agents_mcp_toolset_params) { mcp\_server\_name, type, configs, default\_config }  or [BetaManagedAgentsCustomToolParams](/docs/en/api/beta#beta_managed_agents_custom_tool_params) { description, input\_schema, name, type }

Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

One of the following:

BetaManagedAgentsAgentToolset20260401Params object { type, configs, default\_config }

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: "agent\_toolset\_20260401"

configs: optional array of [BetaManagedAgentsAgentToolConfigParams](/docs/en/api/beta#beta_managed_agents_agent_tool_config_params) { name, enabled, permission\_policy }

Per-tool configuration overrides.

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

enabled: optional boolean

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: optional [BetaManagedAgentsAgentToolsetDefaultConfigParams](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config_params) { enabled, permission\_policy }

Default configuration for all tools in a toolset.

enabled: optional boolean

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

BetaManagedAgentsMCPToolsetParams object { mcp\_server\_name, type, configs, default\_config }

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: string

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: "mcp\_toolset"

configs: optional array of [BetaManagedAgentsMCPToolConfigParams](/docs/en/api/beta#beta_managed_agents_mcp_tool_config_params) { name, enabled, permission\_policy }

Per-tool configuration overrides.

name: string

Name of the MCP tool to configure. 1-128 characters.

enabled: optional boolean

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: optional [BetaManagedAgentsMCPToolsetDefaultConfigParams](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config_params) { enabled, permission\_policy }

Default configuration for all tools from an MCP server.

enabled: optional boolean

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

BetaManagedAgentsCustomToolParams object { description, input\_schema, name, type }

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: string

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: "custom"

BetaManagedAgentsSessionMultiagentCoordinator object { agents, type }

Resolved coordinator topology with full agent definitions for each roster member.

agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp\_servers, 7 more }

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"

BetaManagedAgentsSessionStats object { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds: optional number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: optional number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

BetaManagedAgentsSessionUpdatedEvent object { id, processed\_at, type, 3 more }

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.updated"

agent: optional [BetaManagedAgentsSessionAgent](/docs/en/api/beta#beta_managed_agents_session_agent) { id, description, mcp\_servers, 8 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](/docs/en/api/beta#beta_managed_agents_session_multiagent_coordinator) { agents, type }

Resolved coordinator topology with full agent definitions for each roster member.

agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp\_servers, 7 more }

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

metadata: optional map[string]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: optional string

The session's new title. Present only when the update changed it.

BetaManagedAgentsSessionUsage object { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation: optional [BetaManagedAgentsCacheCreationUsage](/docs/en/api/beta#beta_managed_agents_cache_creation_usage) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: optional number

Total tokens read from prompt cache.

input\_tokens: optional number

Total input tokens consumed across all turns.

output\_tokens: optional number

Total output tokens generated across all turns.

BetaManagedAgentsUserToolResultEvent object { id, tool\_use\_id, type, 4 more }

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string

Unique identifier for this event.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

# SessionsEvents

# [List Events](/docs/en/api/beta/sessions/events/list)

GET/v1/sessions/{session\_id}/events

# [Send Events](/docs/en/api/beta/sessions/events/send)

POST/v1/sessions/{session\_id}/events

# [Stream Events](/docs/en/api/beta/sessions/events/stream)

GET/v1/sessions/{session\_id}/events/stream

# ModelsExpand Collapse

BetaManagedAgentsAgentCustomToolUseEvent object { id, input, name, 3 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

BetaManagedAgentsAgentMCPToolResultEvent object { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentMCPToolUseEvent object { id, input, mcp\_server\_name, 5 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

BetaManagedAgentsAgentMessageEvent object { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

BetaManagedAgentsAgentThinkingEvent object { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

BetaManagedAgentsAgentThreadContextCompactedEvent object { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

BetaManagedAgentsAgentThreadMessageReceivedEvent object { id, content, from\_session\_thread\_id, 3 more }

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Message content blocks.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

from\_session\_thread\_id: string

Public `sthr_` ID of the thread that sent the message.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_message\_received"

from\_agent\_name: optional string

Name of the callable agent this message came from. Absent when received from the primary agent.

BetaManagedAgentsAgentThreadMessageSentEvent object { id, content, processed\_at, 3 more }

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Message content blocks.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

processed\_at: string

A timestamp in RFC 3339 format

to\_session\_thread\_id: string

Public `sthr_` ID of the thread the message was sent to.

type: "agent.thread\_message\_sent"

to\_agent\_name: optional string

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

BetaManagedAgentsAgentToolResultEvent object { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentToolUseEvent object { id, input, name, 4 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsBillingError object { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "billing\_error"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsEventParams = [BetaManagedAgentsUserMessageEventParams](/docs/en/api/beta#beta_managed_agents_user_message_event_params) { content, type }  or [BetaManagedAgentsUserInterruptEventParams](/docs/en/api/beta#beta_managed_agents_user_interrupt_event_params) { type, session\_thread\_id }  or [BetaManagedAgentsUserToolConfirmationEventParams](/docs/en/api/beta#beta_managed_agents_user_tool_confirmation_event_params) { result, tool\_use\_id, type, deny\_message }  or 3 more

Union type for event parameters that can be sent to a session.

One of the following:

BetaManagedAgentsUserMessageEventParams object { content, type }

Parameters for sending a user message to the session.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Array of content blocks for the user message.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

BetaManagedAgentsUserInterruptEventParams object { type, session\_thread\_id }

Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"

session\_thread\_id: optional string

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

BetaManagedAgentsUserToolConfirmationEventParams object { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: "allow" or "deny"

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

BetaManagedAgentsUserCustomToolResultEventParams object { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsUserDefineOutcomeEventParams object { description, rubric, type, max\_iterations }

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

description: string

What the agent should produce. This is the task specification.

rubric: [BetaManagedAgentsFileRubricParams](/docs/en/api/beta#beta_managed_agents_file_rubric_params) { file\_id, type }  or [BetaManagedAgentsTextRubricParams](/docs/en/api/beta#beta_managed_agents_text_rubric_params) { content, type }

Rubric for grading the quality of an outcome.

One of the following:

BetaManagedAgentsFileRubricParams object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

BetaManagedAgentsTextRubricParams object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

type: "text"

type: "user.define\_outcome"

max\_iterations: optional number

Eval→revision cycles before giving up. Default 3, max 20.

BetaManagedAgentsUserToolResultEventParams object { tool\_use\_id, type, content, is\_error }

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

BetaManagedAgentsFileRubric object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

BetaManagedAgentsFileRubricParams object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsMCPAuthenticationFailedError object { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_authentication\_failed\_error"

BetaManagedAgentsMCPConnectionFailedError object { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_connection\_failed\_error"

BetaManagedAgentsModelOverloadedError object { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_overloaded\_error"

BetaManagedAgentsModelRateLimitedError object { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_rate\_limited\_error"

BetaManagedAgentsModelRequestFailedError object { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_request\_failed\_error"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

BetaManagedAgentsSearchResultCitations object { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

BetaManagedAgentsSearchResultContent object { text, type }

Text content within a search result.

text: string

The text content.

type: "text"

BetaManagedAgentsSendSessionEvents object { data }

Events that were successfully sent to the session.

data: optional array of [BetaManagedAgentsUserMessageEvent](/docs/en/api/beta#beta_managed_agents_user_message_event) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](/docs/en/api/beta#beta_managed_agents_user_interrupt_event) { id, type, processed\_at, session\_thread\_id }  or [BetaManagedAgentsUserToolConfirmationEvent](/docs/en/api/beta#beta_managed_agents_user_tool_confirmation_event) { id, result, tool\_use\_id, 4 more }  or 3 more

Sent events

One of the following:

BetaManagedAgentsUserMessageEvent object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Array of content blocks comprising the user message.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

BetaManagedAgentsUserInterruptEvent object { id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

BetaManagedAgentsUserCustomToolResultEvent object { id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: string

Unique identifier for this event.

description: string

What the agent should produce. Copied from the input event.

max\_iterations: number

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: string

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: string

A timestamp in RFC 3339 format

rubric: [BetaManagedAgentsFileRubric](/docs/en/api/beta#beta_managed_agents_file_rubric) { file\_id, type }  or [BetaManagedAgentsTextRubric](/docs/en/api/beta#beta_managed_agents_text_rubric) { content, type }

Rubric for grading the quality of an outcome.

One of the following:

BetaManagedAgentsFileRubric object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

BetaManagedAgentsTextRubric object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: "text"

type: "user.define\_outcome"

BetaManagedAgentsUserToolResultEvent object { id, tool\_use\_id, type, 4 more }

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string

Unique identifier for this event.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

BetaManagedAgentsSessionDeletedEvent object { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

BetaManagedAgentsSessionEndTurn object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionErrorEvent object { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](/docs/en/api/beta#beta_managed_agents_unknown_error) { message, retry\_status, type }  or [BetaManagedAgentsModelOverloadedError](/docs/en/api/beta#beta_managed_agents_model_overloaded_error) { message, retry\_status, type }  or [BetaManagedAgentsModelRateLimitedError](/docs/en/api/beta#beta_managed_agents_model_rate_limited_error) { message, retry\_status, type }  or 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:

BetaManagedAgentsUnknownError object { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "unknown\_error"

BetaManagedAgentsModelOverloadedError object { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_overloaded\_error"

BetaManagedAgentsModelRateLimitedError object { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_rate\_limited\_error"

BetaManagedAgentsModelRequestFailedError object { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_request\_failed\_error"

BetaManagedAgentsMCPConnectionFailedError object { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_connection\_failed\_error"

BetaManagedAgentsMCPAuthenticationFailedError object { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_authentication\_failed\_error"

BetaManagedAgentsBillingError object { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

BetaManagedAgentsSessionEvent = [BetaManagedAgentsUserMessageEvent](/docs/en/api/beta#beta_managed_agents_user_message_event) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](/docs/en/api/beta#beta_managed_agents_user_interrupt_event) { id, type, processed\_at, session\_thread\_id }  or [BetaManagedAgentsUserToolConfirmationEvent](/docs/en/api/beta#beta_managed_agents_user_tool_confirmation_event) { id, result, tool\_use\_id, 4 more }  or 30 more

Union type for all event types in a session.

One of the following:

BetaManagedAgentsUserMessageEvent object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Array of content blocks comprising the user message.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

BetaManagedAgentsUserInterruptEvent object { id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

BetaManagedAgentsUserCustomToolResultEvent object { id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

BetaManagedAgentsAgentCustomToolUseEvent object { id, input, name, 3 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

BetaManagedAgentsAgentMessageEvent object { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

BetaManagedAgentsAgentThinkingEvent object { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

BetaManagedAgentsAgentMCPToolUseEvent object { id, input, mcp\_server\_name, 5 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

BetaManagedAgentsAgentMCPToolResultEvent object { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentToolUseEvent object { id, input, name, 4 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

BetaManagedAgentsAgentToolResultEvent object { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentThreadMessageReceivedEvent object { id, content, from\_session\_thread\_id, 3 more }

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Message content blocks.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

from\_session\_thread\_id: string

Public `sthr_` ID of the thread that sent the message.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_message\_received"

from\_agent\_name: optional string

Name of the callable agent this message came from. Absent when received from the primary agent.

BetaManagedAgentsAgentThreadMessageSentEvent object { id, content, processed\_at, 3 more }

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Message content blocks.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

processed\_at: string

A timestamp in RFC 3339 format

to\_session\_thread\_id: string

Public `sthr_` ID of the thread the message was sent to.

type: "agent.thread\_message\_sent"

to\_agent\_name: optional string

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

BetaManagedAgentsAgentThreadContextCompactedEvent object { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

BetaManagedAgentsSessionErrorEvent object { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](/docs/en/api/beta#beta_managed_agents_unknown_error) { message, retry\_status, type }  or [BetaManagedAgentsModelOverloadedError](/docs/en/api/beta#beta_managed_agents_model_overloaded_error) { message, retry\_status, type }  or [BetaManagedAgentsModelRateLimitedError](/docs/en/api/beta#beta_managed_agents_model_rate_limited_error) { message, retry\_status, type }  or 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:

BetaManagedAgentsUnknownError object { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "unknown\_error"

BetaManagedAgentsModelOverloadedError object { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_overloaded\_error"

BetaManagedAgentsModelRateLimitedError object { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_rate\_limited\_error"

BetaManagedAgentsModelRequestFailedError object { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_request\_failed\_error"

BetaManagedAgentsMCPConnectionFailedError object { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_connection\_failed\_error"

BetaManagedAgentsMCPAuthenticationFailedError object { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_authentication\_failed\_error"

BetaManagedAgentsBillingError object { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

BetaManagedAgentsSessionStatusRescheduledEvent object { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

BetaManagedAgentsSessionStatusRunningEvent object { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

BetaManagedAgentsSessionStatusIdleEvent object { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](/docs/en/api/beta#beta_managed_agents_session_end_turn) { type }  or [BetaManagedAgentsSessionRequiresAction](/docs/en/api/beta#beta_managed_agents_session_requires_action) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](/docs/en/api/beta#beta_managed_agents_session_retries_exhausted) { type }

The agent completed its turn naturally and is ready for the next user message.

One of the following:

BetaManagedAgentsSessionEndTurn object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.status\_idle"

BetaManagedAgentsSessionStatusTerminatedEvent object { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

BetaManagedAgentsSessionThreadCreatedEvent object { id, agent\_name, processed\_at, 2 more }

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: string

Unique identifier for this event.

agent\_name: string

Name of the callable agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public `sthr_` ID of the newly created thread.

type: "session.thread\_created"

BetaManagedAgentsSpanOutcomeEvaluationStartEvent object { id, iteration, outcome\_id, 2 more }

Emitted when an outcome evaluation cycle begins.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.outcome\_evaluation\_start"

BetaManagedAgentsSpanOutcomeEvaluationEndEvent object { id, explanation, iteration, 6 more }

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: string

Unique identifier for this event.

explanation: string

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: string

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

result: string

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: "span.outcome\_evaluation\_end"

usage: [BetaManagedAgentsSpanModelUsage](/docs/en/api/beta#beta_managed_agents_span_model_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

BetaManagedAgentsSpanModelRequestStartEvent object { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

BetaManagedAgentsSpanModelRequestEndEvent object { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](/docs/en/api/beta#beta_managed_agents_span_model_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object { id, iteration, outcome\_id, 2 more }

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.outcome\_evaluation\_ongoing"

BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: string

Unique identifier for this event.

description: string

What the agent should produce. Copied from the input event.

max\_iterations: number

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: string

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: string

A timestamp in RFC 3339 format

rubric: [BetaManagedAgentsFileRubric](/docs/en/api/beta#beta_managed_agents_file_rubric) { file\_id, type }  or [BetaManagedAgentsTextRubric](/docs/en/api/beta#beta_managed_agents_text_rubric) { content, type }

Rubric for grading the quality of an outcome.

One of the following:

BetaManagedAgentsFileRubric object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

BetaManagedAgentsTextRubric object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: "text"

type: "user.define\_outcome"

BetaManagedAgentsSessionDeletedEvent object { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

BetaManagedAgentsSessionThreadStatusRunningEvent object { id, agent\_name, processed\_at, 2 more }

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that started running.

type: "session.thread\_status\_running"

BetaManagedAgentsSessionThreadStatusIdleEvent object { id, agent\_name, processed\_at, 3 more }

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that went idle.

stop\_reason: [BetaManagedAgentsSessionEndTurn](/docs/en/api/beta#beta_managed_agents_session_end_turn) { type }  or [BetaManagedAgentsSessionRequiresAction](/docs/en/api/beta#beta_managed_agents_session_requires_action) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](/docs/en/api/beta#beta_managed_agents_session_retries_exhausted) { type }

The agent completed its turn naturally and is ready for the next user message.

One of the following:

BetaManagedAgentsSessionEndTurn object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.thread\_status\_idle"

BetaManagedAgentsSessionThreadStatusTerminatedEvent object { id, agent\_name, processed\_at, 2 more }

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that terminated.

type: "session.thread\_status\_terminated"

BetaManagedAgentsUserToolResultEvent object { id, tool\_use\_id, type, 4 more }

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string

Unique identifier for this event.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

BetaManagedAgentsSessionThreadStatusRescheduledEvent object { id, agent\_name, processed\_at, 2 more }

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that is retrying.

type: "session.thread\_status\_rescheduled"

BetaManagedAgentsSessionUpdatedEvent object { id, processed\_at, type, 3 more }

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.updated"

agent: optional [BetaManagedAgentsSessionAgent](/docs/en/api/beta#beta_managed_agents_session_agent) { id, description, mcp\_servers, 8 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](/docs/en/api/beta#beta_managed_agents_session_multiagent_coordinator) { agents, type }

Resolved coordinator topology with full agent definitions for each roster member.

agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp\_servers, 7 more }

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

metadata: optional map[string]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: optional string

The session's new title. Present only when the update changed it.

BetaManagedAgentsSessionRequiresAction object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

BetaManagedAgentsSessionStatusIdleEvent object { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](/docs/en/api/beta#beta_managed_agents_session_end_turn) { type }  or [BetaManagedAgentsSessionRequiresAction](/docs/en/api/beta#beta_managed_agents_session_requires_action) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](/docs/en/api/beta#beta_managed_agents_session_retries_exhausted) { type }

The agent completed its turn naturally and is ready for the next user message.

One of the following:

BetaManagedAgentsSessionEndTurn object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.status\_idle"

BetaManagedAgentsSessionStatusRescheduledEvent object { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

BetaManagedAgentsSessionStatusRunningEvent object { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

BetaManagedAgentsSessionStatusTerminatedEvent object { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

BetaManagedAgentsSessionThreadCreatedEvent object { id, agent\_name, processed\_at, 2 more }

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: string

Unique identifier for this event.

agent\_name: string

Name of the callable agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public `sthr_` ID of the newly created thread.

type: "session.thread\_created"

BetaManagedAgentsSessionThreadStatusIdleEvent object { id, agent\_name, processed\_at, 3 more }

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that went idle.

stop\_reason: [BetaManagedAgentsSessionEndTurn](/docs/en/api/beta#beta_managed_agents_session_end_turn) { type }  or [BetaManagedAgentsSessionRequiresAction](/docs/en/api/beta#beta_managed_agents_session_requires_action) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](/docs/en/api/beta#beta_managed_agents_session_retries_exhausted) { type }

The agent completed its turn naturally and is ready for the next user message.

One of the following:

BetaManagedAgentsSessionEndTurn object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.thread\_status\_idle"

BetaManagedAgentsSessionThreadStatusRescheduledEvent object { id, agent\_name, processed\_at, 2 more }

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that is retrying.

type: "session.thread\_status\_rescheduled"

BetaManagedAgentsSessionThreadStatusRunningEvent object { id, agent\_name, processed\_at, 2 more }

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that started running.

type: "session.thread\_status\_running"

BetaManagedAgentsSessionThreadStatusTerminatedEvent object { id, agent\_name, processed\_at, 2 more }

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that terminated.

type: "session.thread\_status\_terminated"

BetaManagedAgentsSpanModelRequestEndEvent object { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](/docs/en/api/beta#beta_managed_agents_span_model_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

BetaManagedAgentsSpanModelRequestStartEvent object { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

BetaManagedAgentsSpanModelUsage object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

BetaManagedAgentsSpanOutcomeEvaluationEndEvent object { id, explanation, iteration, 6 more }

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: string

Unique identifier for this event.

explanation: string

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: string

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

result: string

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: "span.outcome\_evaluation\_end"

usage: [BetaManagedAgentsSpanModelUsage](/docs/en/api/beta#beta_managed_agents_span_model_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object { id, iteration, outcome\_id, 2 more }

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.outcome\_evaluation\_ongoing"

BetaManagedAgentsSpanOutcomeEvaluationStartEvent object { id, iteration, outcome\_id, 2 more }

Emitted when an outcome evaluation cycle begins.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.outcome\_evaluation\_start"

BetaManagedAgentsStreamSessionEvents = [BetaManagedAgentsUserMessageEvent](/docs/en/api/beta#beta_managed_agents_user_message_event) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](/docs/en/api/beta#beta_managed_agents_user_interrupt_event) { id, type, processed\_at, session\_thread\_id }  or [BetaManagedAgentsUserToolConfirmationEvent](/docs/en/api/beta#beta_managed_agents_user_tool_confirmation_event) { id, result, tool\_use\_id, 4 more }  or 30 more

Server-sent event in the session stream.

One of the following:

BetaManagedAgentsUserMessageEvent object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Array of content blocks comprising the user message.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

BetaManagedAgentsUserInterruptEvent object { id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

BetaManagedAgentsUserCustomToolResultEvent object { id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

BetaManagedAgentsAgentCustomToolUseEvent object { id, input, name, 3 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

BetaManagedAgentsAgentMessageEvent object { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

BetaManagedAgentsAgentThinkingEvent object { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

BetaManagedAgentsAgentMCPToolUseEvent object { id, input, mcp\_server\_name, 5 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

BetaManagedAgentsAgentMCPToolResultEvent object { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentToolUseEvent object { id, input, name, 4 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

BetaManagedAgentsAgentToolResultEvent object { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentThreadMessageReceivedEvent object { id, content, from\_session\_thread\_id, 3 more }

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Message content blocks.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

from\_session\_thread\_id: string

Public `sthr_` ID of the thread that sent the message.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_message\_received"

from\_agent\_name: optional string

Name of the callable agent this message came from. Absent when received from the primary agent.

BetaManagedAgentsAgentThreadMessageSentEvent object { id, content, processed\_at, 3 more }

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Message content blocks.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

processed\_at: string

A timestamp in RFC 3339 format

to\_session\_thread\_id: string

Public `sthr_` ID of the thread the message was sent to.

type: "agent.thread\_message\_sent"

to\_agent\_name: optional string

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

BetaManagedAgentsAgentThreadContextCompactedEvent object { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

BetaManagedAgentsSessionErrorEvent object { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](/docs/en/api/beta#beta_managed_agents_unknown_error) { message, retry\_status, type }  or [BetaManagedAgentsModelOverloadedError](/docs/en/api/beta#beta_managed_agents_model_overloaded_error) { message, retry\_status, type }  or [BetaManagedAgentsModelRateLimitedError](/docs/en/api/beta#beta_managed_agents_model_rate_limited_error) { message, retry\_status, type }  or 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:

BetaManagedAgentsUnknownError object { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "unknown\_error"

BetaManagedAgentsModelOverloadedError object { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_overloaded\_error"

BetaManagedAgentsModelRateLimitedError object { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_rate\_limited\_error"

BetaManagedAgentsModelRequestFailedError object { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_request\_failed\_error"

BetaManagedAgentsMCPConnectionFailedError object { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_connection\_failed\_error"

BetaManagedAgentsMCPAuthenticationFailedError object { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_authentication\_failed\_error"

BetaManagedAgentsBillingError object { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

BetaManagedAgentsSessionStatusRescheduledEvent object { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

BetaManagedAgentsSessionStatusRunningEvent object { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

BetaManagedAgentsSessionStatusIdleEvent object { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](/docs/en/api/beta#beta_managed_agents_session_end_turn) { type }  or [BetaManagedAgentsSessionRequiresAction](/docs/en/api/beta#beta_managed_agents_session_requires_action) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](/docs/en/api/beta#beta_managed_agents_session_retries_exhausted) { type }

The agent completed its turn naturally and is ready for the next user message.

One of the following:

BetaManagedAgentsSessionEndTurn object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.status\_idle"

BetaManagedAgentsSessionStatusTerminatedEvent object { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

BetaManagedAgentsSessionThreadCreatedEvent object { id, agent\_name, processed\_at, 2 more }

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: string

Unique identifier for this event.

agent\_name: string

Name of the callable agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public `sthr_` ID of the newly created thread.

type: "session.thread\_created"

BetaManagedAgentsSpanOutcomeEvaluationStartEvent object { id, iteration, outcome\_id, 2 more }

Emitted when an outcome evaluation cycle begins.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.outcome\_evaluation\_start"

BetaManagedAgentsSpanOutcomeEvaluationEndEvent object { id, explanation, iteration, 6 more }

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: string

Unique identifier for this event.

explanation: string

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: string

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

result: string

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: "span.outcome\_evaluation\_end"

usage: [BetaManagedAgentsSpanModelUsage](/docs/en/api/beta#beta_managed_agents_span_model_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

BetaManagedAgentsSpanModelRequestStartEvent object { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

BetaManagedAgentsSpanModelRequestEndEvent object { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](/docs/en/api/beta#beta_managed_agents_span_model_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object { id, iteration, outcome\_id, 2 more }

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.outcome\_evaluation\_ongoing"

BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: string

Unique identifier for this event.

description: string

What the agent should produce. Copied from the input event.

max\_iterations: number

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: string

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: string

A timestamp in RFC 3339 format

rubric: [BetaManagedAgentsFileRubric](/docs/en/api/beta#beta_managed_agents_file_rubric) { file\_id, type }  or [BetaManagedAgentsTextRubric](/docs/en/api/beta#beta_managed_agents_text_rubric) { content, type }

Rubric for grading the quality of an outcome.

One of the following:

BetaManagedAgentsFileRubric object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

BetaManagedAgentsTextRubric object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: "text"

type: "user.define\_outcome"

BetaManagedAgentsSessionDeletedEvent object { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

BetaManagedAgentsSessionThreadStatusRunningEvent object { id, agent\_name, processed\_at, 2 more }

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that started running.

type: "session.thread\_status\_running"

BetaManagedAgentsSessionThreadStatusIdleEvent object { id, agent\_name, processed\_at, 3 more }

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that went idle.

stop\_reason: [BetaManagedAgentsSessionEndTurn](/docs/en/api/beta#beta_managed_agents_session_end_turn) { type }  or [BetaManagedAgentsSessionRequiresAction](/docs/en/api/beta#beta_managed_agents_session_requires_action) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](/docs/en/api/beta#beta_managed_agents_session_retries_exhausted) { type }

The agent completed its turn naturally and is ready for the next user message.

One of the following:

BetaManagedAgentsSessionEndTurn object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.thread\_status\_idle"

BetaManagedAgentsSessionThreadStatusTerminatedEvent object { id, agent\_name, processed\_at, 2 more }

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that terminated.

type: "session.thread\_status\_terminated"

BetaManagedAgentsUserToolResultEvent object { id, tool\_use\_id, type, 4 more }

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string

Unique identifier for this event.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

BetaManagedAgentsSessionThreadStatusRescheduledEvent object { id, agent\_name, processed\_at, 2 more }

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that is retrying.

type: "session.thread\_status\_rescheduled"

BetaManagedAgentsSessionUpdatedEvent object { id, processed\_at, type, 3 more }

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.updated"

agent: optional [BetaManagedAgentsSessionAgent](/docs/en/api/beta#beta_managed_agents_session_agent) { id, description, mcp\_servers, 8 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](/docs/en/api/beta#beta_managed_agents_session_multiagent_coordinator) { agents, type }

Resolved coordinator topology with full agent definitions for each roster member.

agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp\_servers, 7 more }

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

metadata: optional map[string]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: optional string

The session's new title. Present only when the update changed it.

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsTextRubric object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: "text"

BetaManagedAgentsTextRubricParams object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

type: "text"

BetaManagedAgentsUnknownError object { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "unknown\_error"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsUserCustomToolResultEvent object { id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

BetaManagedAgentsUserCustomToolResultEventParams object { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: string

Unique identifier for this event.

description: string

What the agent should produce. Copied from the input event.

max\_iterations: number

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: string

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: string

A timestamp in RFC 3339 format

rubric: [BetaManagedAgentsFileRubric](/docs/en/api/beta#beta_managed_agents_file_rubric) { file\_id, type }  or [BetaManagedAgentsTextRubric](/docs/en/api/beta#beta_managed_agents_text_rubric) { content, type }

Rubric for grading the quality of an outcome.

One of the following:

BetaManagedAgentsFileRubric object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

BetaManagedAgentsTextRubric object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: "text"

type: "user.define\_outcome"

BetaManagedAgentsUserDefineOutcomeEventParams object { description, rubric, type, max\_iterations }

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

description: string

What the agent should produce. This is the task specification.

rubric: [BetaManagedAgentsFileRubricParams](/docs/en/api/beta#beta_managed_agents_file_rubric_params) { file\_id, type }  or [BetaManagedAgentsTextRubricParams](/docs/en/api/beta#beta_managed_agents_text_rubric_params) { content, type }

Rubric for grading the quality of an outcome.

One of the following:

BetaManagedAgentsFileRubricParams object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

BetaManagedAgentsTextRubricParams object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

type: "text"

type: "user.define\_outcome"

max\_iterations: optional number

Eval→revision cycles before giving up. Default 3, max 20.

BetaManagedAgentsUserInterruptEvent object { id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

BetaManagedAgentsUserInterruptEventParams object { type, session\_thread\_id }

Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"

session\_thread\_id: optional string

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

BetaManagedAgentsUserMessageEvent object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Array of content blocks comprising the user message.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

BetaManagedAgentsUserMessageEventParams object { content, type }

Parameters for sending a user message to the session.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Array of content blocks for the user message.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

BetaManagedAgentsUserToolConfirmationEventParams object { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: "allow" or "deny"

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

BetaManagedAgentsUserToolResultEventParams object { tool\_use\_id, type, content, is\_error }

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

# SessionsResources

# [Add Session Resource](/docs/en/api/beta/sessions/resources/add)

POST/v1/sessions/{session\_id}/resources

# [List Session Resources](/docs/en/api/beta/sessions/resources/list)

GET/v1/sessions/{session\_id}/resources

# [Get Session Resource](/docs/en/api/beta/sessions/resources/retrieve)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

# [Update Session Resource](/docs/en/api/beta/sessions/resources/update)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

# [Delete Session Resource](/docs/en/api/beta/sessions/resources/delete)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

# ModelsExpand Collapse

BetaManagedAgentsDeleteSessionResource object { id, type }

Confirmation of resource deletion.

id: string

type: "session\_resource\_deleted"

BetaManagedAgentsFileResource object { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

BetaManagedAgentsGitHubRepositoryResource object { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type }

One of the following:

BetaManagedAgentsBranchCheckout object { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsMemoryStoreResource object { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"

access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

description: optional string

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: optional string

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: optional string

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](/docs/en/api/beta#beta_managed_agents_github_repository_resource) { id, created\_at, mount\_path, 4 more }  or [BetaManagedAgentsFileResource](/docs/en/api/beta#beta_managed_agents_file_resource) { id, created\_at, file\_id, 3 more }  or [BetaManagedAgentsMemoryStoreResource](/docs/en/api/beta#beta_managed_agents_memory_store_resource) { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

One of the following:

BetaManagedAgentsGitHubRepositoryResource object { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type }

One of the following:

BetaManagedAgentsBranchCheckout object { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource object { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

BetaManagedAgentsMemoryStoreResource object { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"

access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

description: optional string

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: optional string

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: optional string

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](/docs/en/api/beta#beta_managed_agents_github_repository_resource) { id, created\_at, mount\_path, 4 more }  or [BetaManagedAgentsFileResource](/docs/en/api/beta#beta_managed_agents_file_resource) { id, created\_at, file\_id, 3 more }  or [BetaManagedAgentsMemoryStoreResource](/docs/en/api/beta#beta_managed_agents_memory_store_resource) { memory\_store\_id, type, access, 4 more }

The requested session resource.

One of the following:

BetaManagedAgentsGitHubRepositoryResource object { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type }

One of the following:

BetaManagedAgentsBranchCheckout object { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource object { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

BetaManagedAgentsMemoryStoreResource object { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"

access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

description: optional string

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: optional string

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: optional string

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](/docs/en/api/beta#beta_managed_agents_github_repository_resource) { id, created\_at, mount\_path, 4 more }  or [BetaManagedAgentsFileResource](/docs/en/api/beta#beta_managed_agents_file_resource) { id, created\_at, file\_id, 3 more }  or [BetaManagedAgentsMemoryStoreResource](/docs/en/api/beta#beta_managed_agents_memory_store_resource) { memory\_store\_id, type, access, 4 more }

The updated session resource.

One of the following:

BetaManagedAgentsGitHubRepositoryResource object { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type }

One of the following:

BetaManagedAgentsBranchCheckout object { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource object { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

BetaManagedAgentsMemoryStoreResource object { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"

access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

description: optional string

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: optional string

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: optional string

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

# SessionsThreads

# [List Session Threads](/docs/en/api/beta/sessions/threads/list)

GET/v1/sessions/{session\_id}/threads

# [Get Session Thread](/docs/en/api/beta/sessions/threads/retrieve)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

# [Archive Session Thread](/docs/en/api/beta/sessions/threads/archive)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

# ModelsExpand Collapse

BetaManagedAgentsSessionThread object { id, agent, archived\_at, 8 more }

An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

id: string

Unique identifier for this thread.

agent: [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

parent\_thread\_id: string

Parent thread that spawned this thread. Null for the primary thread.

session\_id: string

The session this thread belongs to.

stats: [BetaManagedAgentsSessionThreadStats](/docs/en/api/beta#beta_managed_agents_session_thread_stats) { active\_seconds, duration\_seconds, startup\_seconds }

Timing statistics for a session thread.

active\_seconds: optional number

Cumulative time in seconds the thread spent actively running. Excludes idle time.

duration\_seconds: optional number

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

startup\_seconds: optional number

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

status: [BetaManagedAgentsSessionThreadStatus](/docs/en/api/beta#beta_managed_agents_session_thread_status)

SessionThreadStatus enum

One of the following:

"running"

"idle"

"rescheduling"

"terminated"

type: "session\_thread"

updated\_at: string

A timestamp in RFC 3339 format

usage: [BetaManagedAgentsSessionThreadUsage](/docs/en/api/beta#beta_managed_agents_session_thread_usage) { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session thread across all turns.

cache\_creation: optional [BetaManagedAgentsCacheCreationUsage](/docs/en/api/beta#beta_managed_agents_cache_creation_usage) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: optional number

Total tokens read from prompt cache.

input\_tokens: optional number

Total input tokens consumed across all turns.

output\_tokens: optional number

Total output tokens generated across all turns.

BetaManagedAgentsSessionThreadStats object { active\_seconds, duration\_seconds, startup\_seconds }

Timing statistics for a session thread.

active\_seconds: optional number

Cumulative time in seconds the thread spent actively running. Excludes idle time.

duration\_seconds: optional number

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

startup\_seconds: optional number

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

BetaManagedAgentsSessionThreadStatus = "running" or "idle" or "rescheduling" or "terminated"

SessionThreadStatus enum

One of the following:

"running"

"idle"

"rescheduling"

"terminated"

BetaManagedAgentsSessionThreadUsage object { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session thread across all turns.

cache\_creation: optional [BetaManagedAgentsCacheCreationUsage](/docs/en/api/beta#beta_managed_agents_cache_creation_usage) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: optional number

Total tokens read from prompt cache.

input\_tokens: optional number

Total input tokens consumed across all turns.

output\_tokens: optional number

Total output tokens generated across all turns.

BetaManagedAgentsStreamSessionThreadEvents = [BetaManagedAgentsUserMessageEvent](/docs/en/api/beta#beta_managed_agents_user_message_event) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](/docs/en/api/beta#beta_managed_agents_user_interrupt_event) { id, type, processed\_at, session\_thread\_id }  or [BetaManagedAgentsUserToolConfirmationEvent](/docs/en/api/beta#beta_managed_agents_user_tool_confirmation_event) { id, result, tool\_use\_id, 4 more }  or 30 more

Server-sent event in a single thread's stream.

One of the following:

BetaManagedAgentsUserMessageEvent object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Array of content blocks comprising the user message.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

BetaManagedAgentsUserInterruptEvent object { id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

BetaManagedAgentsUserCustomToolResultEvent object { id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

BetaManagedAgentsAgentCustomToolUseEvent object { id, input, name, 3 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

BetaManagedAgentsAgentMessageEvent object { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

BetaManagedAgentsAgentThinkingEvent object { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

BetaManagedAgentsAgentMCPToolUseEvent object { id, input, mcp\_server\_name, 5 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

BetaManagedAgentsAgentMCPToolResultEvent object { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentToolUseEvent object { id, input, name, 4 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: optional string

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

BetaManagedAgentsAgentToolResultEvent object { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentThreadMessageReceivedEvent object { id, content, from\_session\_thread\_id, 3 more }

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Message content blocks.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

from\_session\_thread\_id: string

Public `sthr_` ID of the thread that sent the message.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_message\_received"

from\_agent\_name: optional string

Name of the callable agent this message came from. Absent when received from the primary agent.

BetaManagedAgentsAgentThreadMessageSentEvent object { id, content, processed\_at, 3 more }

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }

Message content blocks.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

processed\_at: string

A timestamp in RFC 3339 format

to\_session\_thread\_id: string

Public `sthr_` ID of the thread the message was sent to.

type: "agent.thread\_message\_sent"

to\_agent\_name: optional string

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

BetaManagedAgentsAgentThreadContextCompactedEvent object { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

BetaManagedAgentsSessionErrorEvent object { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](/docs/en/api/beta#beta_managed_agents_unknown_error) { message, retry\_status, type }  or [BetaManagedAgentsModelOverloadedError](/docs/en/api/beta#beta_managed_agents_model_overloaded_error) { message, retry\_status, type }  or [BetaManagedAgentsModelRateLimitedError](/docs/en/api/beta#beta_managed_agents_model_rate_limited_error) { message, retry\_status, type }  or 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:

BetaManagedAgentsUnknownError object { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "unknown\_error"

BetaManagedAgentsModelOverloadedError object { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_overloaded\_error"

BetaManagedAgentsModelRateLimitedError object { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_rate\_limited\_error"

BetaManagedAgentsModelRequestFailedError object { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_request\_failed\_error"

BetaManagedAgentsMCPConnectionFailedError object { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_connection\_failed\_error"

BetaManagedAgentsMCPAuthenticationFailedError object { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_authentication\_failed\_error"

BetaManagedAgentsBillingError object { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type }

What the client should do next in response to this error.

One of the following:

BetaManagedAgentsRetryStatusRetrying object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

BetaManagedAgentsSessionStatusRescheduledEvent object { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

BetaManagedAgentsSessionStatusRunningEvent object { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

BetaManagedAgentsSessionStatusIdleEvent object { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](/docs/en/api/beta#beta_managed_agents_session_end_turn) { type }  or [BetaManagedAgentsSessionRequiresAction](/docs/en/api/beta#beta_managed_agents_session_requires_action) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](/docs/en/api/beta#beta_managed_agents_session_retries_exhausted) { type }

The agent completed its turn naturally and is ready for the next user message.

One of the following:

BetaManagedAgentsSessionEndTurn object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.status\_idle"

BetaManagedAgentsSessionStatusTerminatedEvent object { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

BetaManagedAgentsSessionThreadCreatedEvent object { id, agent\_name, processed\_at, 2 more }

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: string

Unique identifier for this event.

agent\_name: string

Name of the callable agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public `sthr_` ID of the newly created thread.

type: "session.thread\_created"

BetaManagedAgentsSpanOutcomeEvaluationStartEvent object { id, iteration, outcome\_id, 2 more }

Emitted when an outcome evaluation cycle begins.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.outcome\_evaluation\_start"

BetaManagedAgentsSpanOutcomeEvaluationEndEvent object { id, explanation, iteration, 6 more }

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: string

Unique identifier for this event.

explanation: string

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: string

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

result: string

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: "span.outcome\_evaluation\_end"

usage: [BetaManagedAgentsSpanModelUsage](/docs/en/api/beta#beta_managed_agents_span_model_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

BetaManagedAgentsSpanModelRequestStartEvent object { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

BetaManagedAgentsSpanModelRequestEndEvent object { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](/docs/en/api/beta#beta_managed_agents_span_model_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object { id, iteration, outcome\_id, 2 more }

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: string

Unique identifier for this event.

iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: string

The `outc_` ID of the outcome being evaluated.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.outcome\_evaluation\_ongoing"

BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: string

Unique identifier for this event.

description: string

What the agent should produce. Copied from the input event.

max\_iterations: number

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: string

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: string

A timestamp in RFC 3339 format

rubric: [BetaManagedAgentsFileRubric](/docs/en/api/beta#beta_managed_agents_file_rubric) { file\_id, type }  or [BetaManagedAgentsTextRubric](/docs/en/api/beta#beta_managed_agents_text_rubric) { content, type }

Rubric for grading the quality of an outcome.

One of the following:

BetaManagedAgentsFileRubric object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

BetaManagedAgentsTextRubric object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: "text"

type: "user.define\_outcome"

BetaManagedAgentsSessionDeletedEvent object { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

BetaManagedAgentsSessionThreadStatusRunningEvent object { id, agent\_name, processed\_at, 2 more }

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that started running.

type: "session.thread\_status\_running"

BetaManagedAgentsSessionThreadStatusIdleEvent object { id, agent\_name, processed\_at, 3 more }

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that went idle.

stop\_reason: [BetaManagedAgentsSessionEndTurn](/docs/en/api/beta#beta_managed_agents_session_end_turn) { type }  or [BetaManagedAgentsSessionRequiresAction](/docs/en/api/beta#beta_managed_agents_session_requires_action) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](/docs/en/api/beta#beta_managed_agents_session_retries_exhausted) { type }

The agent completed its turn naturally and is ready for the next user message.

One of the following:

BetaManagedAgentsSessionEndTurn object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.thread\_status\_idle"

BetaManagedAgentsSessionThreadStatusTerminatedEvent object { id, agent\_name, processed\_at, 2 more }

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that terminated.

type: "session.thread\_status\_terminated"

BetaManagedAgentsUserToolResultEvent object { id, tool\_use\_id, type, 4 more }

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string

Unique identifier for this event.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

type: "user.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more }

The result content returned by the tool.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](/docs/en/api/beta#beta_managed_agents_file_image_source) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta#beta_managed_agents_file_document_source) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }

A block containing a web search result.

citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.

content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type }

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

BetaManagedAgentsSessionThreadStatusRescheduledEvent object { id, agent\_name, processed\_at, 2 more }

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.

processed\_at: string

A timestamp in RFC 3339 format

session\_thread\_id: string

Public sthr\_ ID of the thread that is retrying.

type: "session.thread\_status\_rescheduled"

BetaManagedAgentsSessionUpdatedEvent object { id, processed\_at, type, 3 more }

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.updated"

agent: optional [BetaManagedAgentsSessionAgent](/docs/en/api/beta#beta_managed_agents_session_agent) { id, description, mcp\_servers, 8 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](/docs/en/api/beta#beta_managed_agents_session_multiagent_coordinator) { agents, type }

Resolved coordinator topology with full agent definitions for each roster member.

agents: array of [BetaManagedAgentsSessionThreadAgent](/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp\_servers, 7 more }

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](/docs/en/api/beta#beta_managed_agents_model_config) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](/docs/en/api/beta#beta_managed_agents_custom_skill) { skill\_id, type, version }

One of the following:

BetaManagedAgentsAnthropicSkill object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input\_schema, name, type }

One of the following:

BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type }

Permission policy for tool execution.

One of the following:

BetaManagedAgentsAlwaysAllowPolicy object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

metadata: optional map[string]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: optional string

The session's new title. Present only when the update changed it.

# SessionsThreadsEvents

# [List Session Thread Events](/docs/en/api/beta/sessions/threads/events/list)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

# [Stream Session Thread Events](/docs/en/api/beta/sessions/threads/events/stream)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream
