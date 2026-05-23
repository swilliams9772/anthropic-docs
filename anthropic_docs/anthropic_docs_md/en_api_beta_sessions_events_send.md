# Send Events

**Source:** http://platform.claude.com/docs/en/api/beta/sessions/events/send

Copy page

cURL

# Send Events

POST/v1/sessions/{session\_id}/events

Send Events

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

# Body ParametersJSONExpand Collapse

events: array of [BetaManagedAgentsEventParams](/docs/en/api/beta#beta_managed_agents_event_params)

Events to send to the `session`.

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

# ReturnsExpand Collapse

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

Send Events

cURL

```
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "events": [
            {
              "content": [
                {
                  "text": "Where is my order #1234?",
                  "type": "text"
                }
              ],
              "type": "user.message"
            }
          ]
        }'
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
  ]
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
  ]
}
```
