# Delete a memory

**Source:** http://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete

Copy page

cURL

# Delete a memory

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

Delete a memory

# Path ParametersExpand Collapse

memory\_store\_id: string

memory\_id: string

# Query ParametersExpand Collapse

expected\_content\_sha256: optional string

Query parameter for expected\_content\_sha256

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

BetaManagedAgentsDeletedMemory object { id, type }

Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

id: string

ID of the deleted memory (a `mem_...` value).

type: "memory\_deleted"

Delete a memory

cURL

```
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200

```
{
  "id": "id",
  "type": "memory_deleted"
}
```

# Returns Examples

Response 200

```
{
  "id": "id",
  "type": "memory_deleted"
}
```
