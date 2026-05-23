# Create Agent

**Source:** http://platform.claude.com/docs/en/api/beta/agents/create

Copy page

cURL

# Create Agent

POST/v1/agents

Create Agent

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

# Body ParametersJSONExpand Collapse

model: [BetaManagedAgentsModel](/docs/en/api/beta#beta_managed_agents_model) or [BetaManagedAgentsModelConfigParams](/docs/en/api/beta#beta_managed_agents_model_config_params) { id, speed }

Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

One of the following:

BetaManagedAgentsModel = "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more or string

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

BetaManagedAgentsModelConfigParams object { id, speed }

An object that defines additional configuration control over model use

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

Human-readable name for the agent. 1-256 characters.

description: optional string

Description of what the agent does. Up to 2048 characters.

mcp\_servers: optional array of [BetaManagedAgentsURLMCPServerParams](/docs/en/api/beta#beta_managed_agents_url_mcp_server_params) { name, type, url }

MCP servers this agent connects to. Maximum 20. Names must be unique within the array.

name: string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: "url"

url: string

Endpoint URL for the MCP server.

metadata: optional map[string]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

multiagent: optional [BetaManagedAgentsMultiagentParams](/docs/en/api/beta#beta_managed_agents_multiagent_params) { agents, type }

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

skills: optional array of [BetaManagedAgentsSkillParams](/docs/en/api/beta#beta_managed_agents_skill_params)

Skills available to the agent. Maximum 20.

One of the following:

BetaManagedAgentsAnthropicSkillParams object { skill\_id, type, version }

An Anthropic-managed skill.

skill\_id: string

Identifier of the Anthropic skill (e.g., "xlsx").

type: "anthropic"

version: optional string

Version to pin. Defaults to latest if omitted.

BetaManagedAgentsCustomSkillParams object { skill\_id, type, version }

A user-created custom skill.

skill\_id: string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: "custom"

version: optional string

Version to pin. Defaults to latest if omitted.

system: optional string

System prompt for the agent. Up to 100,000 characters.

tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](/docs/en/api/beta#beta_managed_agents_agent_toolset20260401_params) { type, configs, default\_config }  or [BetaManagedAgentsMCPToolsetParams](/docs/en/api/beta#beta_managed_agents_mcp_toolset_params) { mcp\_server\_name, type, configs, default\_config }  or [BetaManagedAgentsCustomToolParams](/docs/en/api/beta#beta_managed_agents_custom_tool_params) { description, input\_schema, name, type }

Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

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

# ReturnsExpand Collapse

BetaManagedAgentsAgent object { id, archived\_at, created\_at, 12 more }

A Managed Agents `agent`.

id: string

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url }

name: string

type: "url"

url: string

metadata: map[string]

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

multiagent: [BetaManagedAgentsMultiagent](/docs/en/api/beta#beta_managed_agents_multiagent) { agents, type }

Resolved coordinator topology with a concrete agent roster.

agents: array of [BetaManagedAgentsAgentReference](/docs/en/api/beta#beta_managed_agents_agent_reference) { id, type, version }

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: string

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

updated\_at: string

A timestamp in RFC 3339 format

version: number

The agent's current version. Starts at 1 and increments when the agent is modified.

Create Agent

cURL

```
curl https://api.anthropic.com/v1/agents \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d "{
          \"model\": \"claude-sonnet-4-6\",
          \"name\": \"My First Agent\",
          \"description\": \"A general-purpose starter agent.\",
          \"metadata\": {
            \"foo\": \"bar\"
          },
          \"system\": \"You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.\",
          \"tools\": [
            {
              \"type\": \"agent_toolset_20260401\"
            }
          ]
        }"
```

Response 200

```
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
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
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

# Returns Examples

Response 200

```
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
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
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```
