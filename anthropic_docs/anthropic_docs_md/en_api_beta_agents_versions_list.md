# List Agent Versions

**Source:** http://platform.claude.com/docs/en/api/beta/agents/versions/list

Copy page

cURL

# List Agent Versions

GET/v1/agents/{agent\_id}/versions

List Agent Versions

# Path ParametersExpand Collapse

agent\_id: string

# Query ParametersExpand Collapse

limit: optional number

Maximum results per page. Default 20, maximum 100.

page: optional string

Opaque pagination cursor.

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

data: optional array of [BetaManagedAgentsAgent](/docs/en/api/beta#beta_managed_agents_agent) { id, archived\_at, created\_at, 12 more }

Agent versions.

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

next\_page: optional string

Opaque cursor for the next page. Null when no more results.

List Agent Versions

cURL

```
curl https://api.anthropic.com/v1/agents/$AGENT_ID/versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200

```
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```
