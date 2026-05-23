# Start a session

**Source:** http://platform.claude.com/docs/en/managed-agents/sessions

Copy page

A session is an agent instance within an environment. Each session references an [agent](/docs/en/managed-agents/agent-setup) and an [environment](/docs/en/managed-agents/environments) (both created separately), and maintains conversation history across multiple interactions. Sessions follow a two-step lifecycle: first [create the session](#creating-a-session) to provision its container, then [send a user event](#starting-the-session) to start work.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

# Creating a session

A session requires an `agent` ID and an `environment` ID. Agents are versioned resources; passing in the `agent` ID as a string starts the session with the latest agent version.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID"
```

To pin a session to a specific agent version, pass an object. This lets you control exactly which version runs and stage rollouts of new versions independently.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:sessions create <<YAML
agent:
  type: agent
  id: $AGENT_ID
  version: 1
environment_id: $ENVIRONMENT_ID
YAML
```

The agent defines how Claude behaves within the session, including the model, system prompt, tools, and MCP servers. See [Define your agent](/docs/en/managed-agents/agent-setup) for details.

# MCP authentication through vaults

If your agent uses MCP tools that require authentication, pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials. Anthropic manages token refresh on your behalf. See [Authenticate with vaults](/docs/en/managed-agents/vaults) for how to create vaults and register credentials.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:sessions create <<YAML
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
vault_ids:
  - $VAULT_ID
YAML
```

# Starting the session

Creating a session provisions the environment's container but does not start any work. To delegate a task, send events to the session using a [user event](/docs/en/managed-agents/events-and-streaming#event-types). The session acts as a state machine that tracks progress while events drive the actual execution.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:sessions:events send \
  --session-id "$SESSION_ID" <<'YAML'
events:
  - type: user.message
    content:
      - type: text
        text: List the files in the working directory.
YAML
```

See [Session event stream](/docs/en/managed-agents/events-and-streaming) for how to stream the agent's responses and handle tool confirmations.

# Session statuses

Sessions progress through these statuses:

| Status | Description |
| --- | --- |
| `idle` | Agent is waiting for input, including user messages or tool confirmations. Sessions start in `idle`. |
| `running` | Agent is actively executing. |
| `rescheduling` | Transient error occurred, retrying automatically. |
| `terminated` | Session has ended due to an unrecoverable error. |

# Other session operations

# Updating the agent configuration

You can update a session's `agent.tools` and `agent.mcp_servers`, including permission policies, mid-session without creating a new agent version. Updates are session-local and do not propagate back to the underlying agent.

The semantics of an update are full replacement: the provided array is the new value. To preserve existing entries, `GET` the session, modify the array, and `POST` it back.

The session must be `idle` to update the agent. [Interrupt](/docs/en/managed-agents/events-and-streaming#integrating-events) the session if you need to update the agent while it's running.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:sessions update --session-id "$SESSION_ID" <<'YAML'
agent:
  tools:
    - type: agent_toolset_20260401
    - type: mcp_toolset
      mcp_server_name: linear
  mcp_servers:
    - type: url
      name: linear
      url: https://mcp.linear.app/sse
YAML
```

# Retrieving a session

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:sessions retrieve --session-id "$SESSION_ID"
```

# Listing sessions

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:sessions list --agent-id "$AGENT_ID"
```

# Archiving a session

Archive a session to prevent new events from being sent while preserving its history:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:sessions archive \
  --session-id "$SESSION_ID"
```

# Deleting a session

Delete a session to permanently remove its record, events, and associated container. A `running` session cannot be deleted; send an [interrupt event](/docs/en/managed-agents/events-and-streaming#event-types) if you need to delete it immediately.

Files, memory stores, vaults, skills, environments, and agents are independent resources and are not affected by session deletion.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:sessions delete \
  --session-id "$SESSION_ID"
```

Was this page helpful?
