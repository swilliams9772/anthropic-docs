# List Session Thread Events

**Source:** http://platform.claude.com/docs/en/api/beta/sessions/threads/events/list

Copy page

cURL

# List Session Thread Events

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

List Session Thread Events

# Path ParametersExpand Collapse

session\_id: string

thread\_id: string

# Query ParametersExpand Collapse

limit: optional number

Query parameter for limit

page: optional string

Query parameter for page

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

data: optional array of [BetaManagedAgentsSessionEvent](/docs/en/api/beta#beta_managed_agents_session_event)

Events for the thread, ordered by `created_at`.

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

next\_page: optional string

Opaque cursor for the next page. Null when no more results.

List Session Thread Events

cURL

```
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/events \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200

```
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
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
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "next_page"
}
```
