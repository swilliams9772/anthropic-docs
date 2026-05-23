# Using agent memory

**Source:** http://platform.claude.com/docs/en/managed-agents/memory

Copy page

Each Managed Agents session starts with a fresh context by default. When a session ends, any state the agent built up is gone. Memory stores let the agent carry information across sessions: user preferences, project conventions, prior mistakes, and domain context.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

# Overview

A **memory store** is a workspace-scoped collection of text documents optimized for Claude. When you attach a store to a session, it is mounted as a directory inside the session's container. The agent reads and writes it with the same file tools it uses for the rest of the filesystem, and a note describing each mount is automatically added to the system prompt, telling the agent where to look. The [agent toolset](/docs/en/managed-agents/tools) is required for these interactions; make sure to enable it during [agent creation](/docs/en/managed-agents/agent-setup).

Each **memory** in a store is addressed by a path and can be read and edited directly via the API or Console, allowing for tuning, importing, and exporting.

Every change to a memory creates an immutable **memory version**, giving you an audit trail and point-in-time recovery for everything the agent writes.

# Create a memory store

Give the store a `name` and a `description`. The description is passed to the agent, telling it what the store contains.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
store_id=$(ant beta:memory-stores create \
  --name "User Preferences" \
  --description "Per-user preferences and project context." \
  --transform id --raw-output)
```

The memory store `id` (`memstore_...`) is what you pass when attaching the store to a session.

# Seed it with content (optional)

Pre-load a store with reference material before any agent runs:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:memory-stores:memories create \
  --memory-store-id "$store_id" \
  --path "/formatting_standards.md" \
  --content "All reports use GAAP formatting. Dates are ISO-8601..." \
  > /dev/null
```

Individual memories within the store are capped at 100 kB (~25k tokens). Structure memory as many small focused files, not a few large ones.

# Attach a memory store to a session

Memory stores are attached in the session's `resources[]` array when the session is created. Unlike file and repository resources, memory stores can only be attached at session creation time; adding or removing one from a running session is not supported.

Optionally include `instructions` to provide session-specific guidance for how the agent should use this store. It is shown to the agent alongside the store's `name` and `description`, and is capped at 4,096 characters.

You can configure `access` as well. It defaults to `read_write` (shown explicitly in the following example), but `read_only` is also supported.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:sessions create <<YAML
agent: $agent_id
environment_id: $environment_id
resources:
  - type: memory_store
    memory_store_id: $store_id
    access: read_write
    instructions: User preferences and project context. Check before starting any task.
YAML
```

Memory stores attach with `read_write` access by default. If the agent processes untrusted input (user-supplied prompts, fetched web content, or third-party tool output), a successful prompt injection could write malicious content into the store. Later sessions then read that content as trusted memory. Use `read_only` for reference material, shared lookups, and any store the agent does not need to modify.

A maximum of **8 memory stores** are supported per session. Attach multiple stores when different parts of memory have different owners or access rules. Common reasons:

* **Shared reference material:** one read-only store attached to many sessions (standards, conventions, domain knowledge), kept separate from each session's own read-write store.
* **Mapping to your product's structure:** one store per end user, per team, or per project, while sharing a single agent configuration.
* **Different lifecycles:** a store that outlives any single session, or one you want to archive on its own schedule.

# How the agent accesses memory

Each attached store is mounted inside the session's container as a directory under `/mnt/memory/`, and the agent reads and writes it with the standard [agent toolset](/docs/en/managed-agents/tools). Writes are persisted back to the store and stay in sync across sessions that share it. A short description of each mount (path, access mode, store `description`, and any `instructions`) is automatically added to the system prompt.

`access` is enforced at the filesystem level: a `read_only` mount rejects writes, while writes to a `read_write` mount produce [memory versions](#audit-memory-changes) attributed to the session.

The agent's reads and writes appear in the [event stream](/docs/en/managed-agents/events-and-streaming) as ordinary `agent.tool_use` and `agent.tool_result` events for whichever tool touched the mount.

# View and edit memories

Memory stores can be managed directly via the API. Use this for building review workflows, correcting bad memories, or seeding stores before any session runs.

# List memories

List the memories in a store, optionally filtered by `path_prefix` to browse a path like a directory:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:memory-stores:memories list \
  --memory-store-id "$store_id" \
  --path-prefix "/" --order-by path --depth 2
```

See the [List memories reference](/docs/en/api/beta/memory_stores/memories/list) for full parameters and response schema.

# Read a memory

Fetching an individual memory returns the full content.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:memory-stores:memories retrieve \
  --memory-store-id "$store_id" \
  --memory-id "$mem_id"
```

See the [Retrieve a memory reference](/docs/en/api/beta/memory_stores/memories/retrieve) for full parameters and response schema.

# Create a memory

`memories.create` creates a memory at a given `path`. Create does not overwrite; to change an existing memory, use [`memories.update`](#update-a-memory).

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
mem=$(ant beta:memory-stores:memories create \
  --memory-store-id "$store_id" \
  --path "/preferences/formatting.md" \
  --content "Always use tabs, not spaces." \
  --format json)
mem_id=$(jq -r '.id' <<< "$mem")
mem_sha=$(jq -r '.content_sha256' <<< "$mem")
```

See the [Create a memory reference](/docs/en/api/beta/memory_stores/memories/create) for full parameters and response schema.

# Update a memory

`memories.update` modifies an existing memory by ID. You can change `content`, `path` (a rename), or both. The example renames a memory to an archive path:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:memory-stores:memories update \
  --memory-store-id "$store_id" \
  --memory-id "$mem_id" \
  --path "/archive/2026_q1_formatting.md" \
  > /dev/null
```

See the [Update a memory reference](/docs/en/api/beta/memory_stores/memories/update) for full parameters and response schema.

# Safe content edits (optimistic concurrency)

To avoid clobbering a concurrent write, pass a `content_sha256` precondition. The update only applies if the stored content hash still matches the one you read; on mismatch, re-read the memory and retry against the fresh state.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:memory-stores:memories update \
  --memory-store-id "$store_id" \
  --memory-id "$mem_id" \
  --content "CORRECTED: Always use 2-space indentation." \
  --precondition "{type: content_sha256, content_sha256: $mem_sha}" \
  > /dev/null
```

# Delete a memory

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:memory-stores:memories delete \
  --memory-store-id "$store_id" \
  --memory-id "$mem_id" \
  > /dev/null
```

See the [Delete a memory reference](/docs/en/api/beta/memory_stores/memories/delete) for full parameters and response schema.

# Audit memory changes

Every mutation to a memory creates an immutable **memory version** (`memver_...`). Use the version endpoints to audit who changed what and when, to inspect or restore a prior snapshot, and to scrub sensitive content out of history with redact.

Versions belong to the store (not the individual memory) and survive even after the memory itself is deleted, so the audit trail stays complete. Versions are retained for 30 days; however, the recent versions are always kept regardless of age, so memories that change infrequently might retain history beyond 30 days. The live `memories.retrieve` call always returns the latest version; the version endpoints give you the retained history.

There is no dedicated restore endpoint; to roll back, retrieve the version you want and write its `content` back with `memories.update` (or `memories.create` if the parent memory has been deleted, because versions outlive their parent).

Past memory versions might be deleted after 30 days. To preserve memory history for longer, export versions via the API.

# List versions

List version history for a store, newest first. The example filters to a single memory's history:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
versions=$(ant beta:memory-stores:memory-versions list \
  --memory-store-id "$store_id" \
  --memory-id "$mem_id" \
  --format json)
jq -r '.data[] | "\(.id): \(.operation)"' <<< "$versions"
version_id=$(jq -r '.data[1].id' <<< "$versions")
```

See the [List memory versions reference](/docs/en/api/beta/memory_stores/memory_versions/list) for full parameters and response schema.

# Retrieve a version

Fetching an individual version returns the same fields as the list response plus the full `content` body.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:memory-stores:memory-versions retrieve \
  --memory-store-id "$store_id" \
  --memory-version-id "$version_id"
```

See the [Retrieve a memory version reference](/docs/en/api/beta/memory_stores/memory_versions/retrieve) for full parameters and response schema.

# Redact a version

Redact scrubs content out of a historical version while preserving the audit trail (who did what, when). Use it for compliance workflows such as removing leaked secrets, PII, or user deletion requests.

A version that is the current head of a live memory cannot be redacted. Write a new version first (or delete the memory), then redact the old one.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:memory-stores:memory-versions redact \
  --memory-store-id "$store_id" \
  --memory-version-id "$version_id"
```

See the [Redact a memory version reference](/docs/en/api/beta/memory_stores/memory_versions/redact) for full parameters and response schema.

# Manage memory stores

In addition to [`create`](/docs/en/api/beta/memory_stores/create), memory stores support [`retrieve`](/docs/en/api/beta/memory_stores/retrieve), [`update`](/docs/en/api/beta/memory_stores/update), [`list`](/docs/en/api/beta/memory_stores/list), [`archive`](/docs/en/api/beta/memory_stores/archive), and [`delete`](/docs/en/api/beta/memory_stores/delete).

# List stores

List stores in the workspace. Archived stores are excluded by default; pass `include_archived: true` to include them.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:memory-stores list --include-archived
```

See the [List memory stores reference](/docs/en/api/beta/memory_stores/list) for full parameters and response schema.

# Archive a store

Archiving makes a store read-only and prevents it from being attached to new sessions. Archiving is one-way; there is no unarchive.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```
ant beta:memory-stores archive --memory-store-id "$store_id"
```

See the [Archive a memory store reference](/docs/en/api/beta/memory_stores/archive) for full parameters and response schema.

To permanently remove a store along with all of its memories and versions, use [`memory_stores.delete`](/docs/en/api/beta/memory_stores/delete).

# Limits

Default capacity and rate limits apply to memory stores while this feature is in beta. [Contact support](https://support.claude.com) if you need higher limits.

Was this page helpful?
