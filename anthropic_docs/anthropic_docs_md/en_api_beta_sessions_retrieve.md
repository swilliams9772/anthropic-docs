# Get Session

**Source:** http://platform.claude.com/docs/en/api/beta/sessions/retrieve

Copy page

cURL

# Get Session

GET/v1/sessions/{session\_id}

Get Session

# Path ParametersExpand Collapse

session\_id: string

# Header ParametersExpand Collapse

"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)

Optional header to specify the beta version(s) you want to use.

One of the following:

string

"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 22 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

# ReturnsExpand Collapse

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

Get Session

cURL

```
curl https://api.anthropic.com/v1/sessions/$SESSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200

```
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  }
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

# Returns Examples

Response 200

```
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  }
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```
