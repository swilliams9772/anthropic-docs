# Create a Message

**Source:** http://platform.claude.com/docs/en/api/beta/messages/create

Copy page

cURL

# Create a Message

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

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

max\_tokens: number

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum0

messages: array of [BetaMessageParam](/docs/en/api/beta#beta_message_param) { content, role }

Input messages.

Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

Example with a single `user` message:

```
[{"role": "user", "content": "Hello, Claude"}]
```

Example with multiple conversational turns:

```
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]
```

Example with a partially-filled response from Claude:

```
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("},
]
```

Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

```
{"role": "user", "content": "Hello, Claude"}
```

```
{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
```

See [input examples](https://docs.claude.com/en/api/messages-examples).

Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.

content: string or array of [BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)

One of the following:

string

array of [BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)

One of the following:

BetaTextBlockParam object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

One of the following:

BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

BetaImageBlockParam object { source, type, cache\_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type }  or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url }  or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file\_id, type }

One of the following:

BetaBase64ImageSource object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource object { type, url }

type: "url"

url: string

BetaFileImageSource object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

BetaRequestDocumentBlock object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type }  or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }  or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type }  or 2 more

One of the following:

BetaBase64PDFSource object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

One of the following:

string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

One of the following:

BetaTextBlockParam object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

One of the following:

BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

BetaImageBlockParam object { source, type, cache\_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type }  or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url }  or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file\_id, type }

One of the following:

BetaBase64ImageSource object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource object { type, url }

type: "url"

url: string

BetaFileImageSource object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource object { type, url }

type: "url"

url: string

BetaFileDocumentSource object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaSearchResultBlockParam object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

One of the following:

BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaThinkingBlockParam object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlockParam object { data, type }

data: string

type: "redacted\_thinking"

BetaToolUseBlockParam object { id, input, name, 3 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaToolResultBlockParam object { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: string

type: "tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }  or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache\_control }  or [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more }  or 2 more

One of the following:

string

array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }  or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache\_control }  or [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more }  or 2 more

One of the following:

BetaTextBlockParam object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

One of the following:

BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

BetaImageBlockParam object { source, type, cache\_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type }  or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url }  or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file\_id, type }

One of the following:

BetaBase64ImageSource object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource object { type, url }

type: "url"

url: string

BetaFileImageSource object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

BetaSearchResultBlockParam object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

One of the following:

BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaRequestDocumentBlock object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type }  or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }  or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type }  or 2 more

One of the following:

BetaBase64PDFSource object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

One of the following:

string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

One of the following:

BetaTextBlockParam object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

One of the following:

BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

BetaImageBlockParam object { source, type, cache\_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type }  or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url }  or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file\_id, type }

One of the following:

BetaBase64ImageSource object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource object { type, url }

type: "url"

url: string

BetaFileImageSource object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource object { type, url }

type: "url"

url: string

BetaFileDocumentSource object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaToolReferenceBlockParam object { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

is\_error: optional boolean

BetaServerToolUseBlockParam object { id, input, name, 3 more }

id: string

input: map[unknown]

name: "advisor" or "web\_search" or "web\_fetch" or 5 more

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlockParam object { content, tool\_use\_id, type, 2 more }

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

One of the following:

ResultBlock = array of [BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

BetaWebSearchToolRequestError object { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlockParam object { content, tool\_use\_id, type, 2 more }

content: [BetaWebFetchToolResultErrorBlockParam](/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error\_code, type }  or [BetaWebFetchBlockParam](/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved\_at }

One of the following:

BetaWebFetchToolResultErrorBlockParam object { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlockParam object { content, type, url, retrieved\_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type }  or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }  or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type }  or 2 more

One of the following:

BetaBase64PDFSource object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

One of the following:

string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

One of the following:

BetaTextBlockParam object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

One of the following:

BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

BetaImageBlockParam object { source, type, cache\_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type }  or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url }  or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file\_id, type }

One of the following:

BetaBase64ImageSource object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource object { type, url }

type: "url"

url: string

BetaFileImageSource object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource object { type, url }

type: "url"

url: string

BetaFileDocumentSource object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaAdvisorToolResultBlockParam object { content, tool\_use\_id, type, cache\_control }

content: [BetaAdvisorToolResultErrorParam](/docs/en/api/beta#beta_advisor_tool_result_error_param) { error\_code, type }  or [BetaAdvisorResultBlockParam](/docs/en/api/beta#beta_advisor_result_block_param) { text, type }  or [BetaAdvisorRedactedResultBlockParam](/docs/en/api/beta#beta_advisor_redacted_result_block_param) { encrypted\_content, type }

One of the following:

BetaAdvisorToolResultErrorParam object { error\_code, type }

error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 3 more

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

type: "advisor\_tool\_result\_error"

BetaAdvisorResultBlockParam object { text, type }

text: string

type: "advisor\_result"

BetaAdvisorRedactedResultBlockParam object { encrypted\_content, type }

encrypted\_content: string

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

BetaCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:

BetaCodeExecutionToolResultErrorParam object { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlockParam object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control }

content: [BetaBashCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error\_code, type }  or [BetaBashCodeExecutionResultBlockParam](/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return\_code, stderr, 2 more }

One of the following:

BetaBashCodeExecutionToolResultErrorParam object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error\_code, type, error\_message }  or [BetaTextEditorCodeExecutionViewResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file\_type, type, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new\_lines, 3 more }

One of the following:

BetaTextEditorCodeExecutionToolResultErrorParam object { error\_code, type, error\_message }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string

BetaTextEditorCodeExecutionViewResultBlockParam object { content, file\_type, type, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number

BetaTextEditorCodeExecutionCreateResultBlockParam object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new\_lines, 3 more }

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

BetaToolSearchToolResultBlockParam object { content, tool\_use\_id, type, cache\_control }

content: [BetaToolSearchToolResultErrorParam](/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error\_code, type }  or [BetaToolSearchToolSearchResultBlockParam](/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool\_references, type }

One of the following:

BetaToolSearchToolResultErrorParam object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlockParam object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool\_name, type, cache\_control }

tool\_name: string

type: "tool\_reference"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

BetaMCPToolUseBlockParam object { id, input, name, 3 more }

id: string

input: map[unknown]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

BetaRequestMCPToolResultBlockParam object { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: string

type: "mcp\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

One of the following:

string

BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

One of the following:

BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

is\_error: optional boolean

BetaContainerUploadBlockParam object { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

BetaCompactionBlockParam object { content, type, cache\_control, encrypted\_content }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

encrypted\_content: optional string

Opaque metadata from prior compaction, to be round-tripped verbatim

role: "user" or "assistant"

One of the following:

"user"

"assistant"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

container: optional [BetaContainerParams](/docs/en/api/beta#beta_container_params) { id, skills }  or string

Container identifier for reuse across requests.

One of the following:

BetaContainerParams object { id, skills }

Container parameters with skills to be loaded.

id: optional string

Container id

skills: optional array of [BetaSkillParams](/docs/en/api/beta#beta_skill_params) { skill\_id, type, version }

List of skills to load in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: optional string

Skill version or 'latest' for most recent version

string

context\_management: optional [BetaContextManagementConfig](/docs/en/api/beta#beta_context_management_config) { edits }

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

edits: optional array of [BetaClearToolUses20250919Edit](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit) { type, clear\_at\_least, clear\_tool\_inputs, 3 more }  or [BetaClearThinking20251015Edit](/docs/en/api/beta#beta_clear_thinking_20251015_edit) { type, keep }  or [BetaCompact20260112Edit](/docs/en/api/beta#beta_compact_20260112_edit) { type, instructions, pause\_after\_compaction, trigger }

List of context management edits to apply

One of the following:

BetaClearToolUses20250919Edit object { type, clear\_at\_least, clear\_tool\_inputs, 3 more }

type: "clear\_tool\_uses\_20250919"

clear\_at\_least: optional [BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input\_tokens"

value: number

clear\_tool\_inputs: optional boolean or array of string

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

boolean

array of string

exclude\_tools: optional array of string

Tool names whose uses are preserved from clearing

keep: optional [BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep) { type, value }

Number of tool uses to retain in the conversation

type: "tool\_uses"

value: number

trigger: optional [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value }  or [BetaToolUsesTrigger](/docs/en/api/beta#beta_tool_uses_trigger) { type, value }

Condition that triggers the context management strategy

One of the following:

BetaInputTokensTrigger object { type, value }

type: "input\_tokens"

value: number

BetaToolUsesTrigger object { type, value }

type: "tool\_uses"

value: number

BetaClearThinking20251015Edit object { type, keep }

type: "clear\_thinking\_20251015"

keep: optional [BetaThinkingTurns](/docs/en/api/beta#beta_thinking_turns) { type, value }  or [BetaAllThinkingTurns](/docs/en/api/beta#beta_all_thinking_turns) { type }  or "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:

BetaThinkingTurns object { type, value }

type: "thinking\_turns"

value: number

BetaAllThinkingTurns object { type }

type: "all"

"all"

BetaCompact20260112Edit object { type, instructions, pause\_after\_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: "compact\_20260112"

instructions: optional string

Additional instructions for summarization.

pause\_after\_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.

trigger: optional [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: "input\_tokens"

value: number

diagnostics: optional [BetaDiagnosticsParam](/docs/en/api/beta#beta_diagnostics_param) { previous\_message\_id }

Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.

previous\_message\_id: optional string

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

inference\_geo: optional string

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

mcp\_servers: optional array of [BetaRequestMCPServerURLDefinition](/docs/en/api/beta#beta_request_mcp_server_url_definition) { name, type, url, 2 more }

MCP servers to be utilized in this request

name: string

type: "url"

url: string

authorization\_token: optional string

tool\_configuration: optional [BetaRequestMCPServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration) { allowed\_tools, enabled }

allowed\_tools: optional array of string

enabled: optional boolean

metadata: optional [BetaMetadata](/docs/en/api/beta#beta_metadata) { user\_id }

An object describing metadata about the request.

user\_id: optional string

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

output\_config: optional [BetaOutputConfig](/docs/en/api/beta#beta_output_config) { effort, format, task\_budget }

Configuration options for the model's output, such as the output format.

effort: optional "low" or "medium" or "high" or 2 more

All possible effort levels.

One of the following:

"low"

"medium"

"high"

"xhigh"

"max"

format: optional [BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format) { schema, type }

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"

task\_budget: optional [BetaTokenTaskBudget](/docs/en/api/beta#beta_token_task_budget) { total, type, remaining }

User-configurable total token budget across contexts.

total: number

Total token budget across all contexts in the session.

type: "tokens"

The budget type. Currently only 'tokens' is supported.

remaining: optional number

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

Deprecatedoutput\_format: optional [BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format) { schema, type }

Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"

service\_tier: optional "auto" or "standard\_only"

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

One of the following:

"auto"

"standard\_only"

speed: optional "standard" or "fast"

The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

One of the following:

"standard"

"fast"

stop\_sequences: optional array of string

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

stream: optional boolean

Whether to incrementally stream the response using server-sent events.

See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

system: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

One of the following:

string

array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

One of the following:

BetaCitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

Deprecatedtemperature: optional number

Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

thinking: optional [BetaThinkingConfigParam](/docs/en/api/beta#beta_thinking_config_param)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

One of the following:

BetaThinkingConfigEnabled object { budget\_tokens, type, display }

budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"

BetaThinkingConfigDisabled object { type }

type: "disabled"

BetaThinkingConfigAdaptive object { type, display }

type: "adaptive"

display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"

tool\_choice: optional [BetaToolChoice](/docs/en/api/beta#beta_tool_choice)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:

BetaToolChoiceAuto object { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: "auto"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

BetaToolChoiceAny object { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: "any"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceTool object { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceNone object { type }

The model will not be allowed to use tools.

type: "none"

tools: optional array of [BetaToolUnion](/docs/en/api/beta#beta_tool_union)

Definitions of tools that the model may use.

If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

Each tool definition includes:

* `name`: Name of the tool.
* `description`: Optional, but strongly-recommended description of the tool.
* `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

For example, if you defined `tools` as:

```
[
  {
    "name": "get_stock_price",
    "description": "Get the current stock price for a given ticker symbol.",
    "input_schema": {
      "type": "object",
      "properties": {
        "ticker": {
          "type": "string",
          "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
        }
      },
      "required": ["ticker"]
    }
  }
]
```

And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

```
[
  {
    "type": "tool_use",
    "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "name": "get_stock_price",
    "input": { "ticker": "^GSPC" }
  }
]
```

You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

```
[
  {
    "type": "tool_result",
    "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "content": "259.75 USD"
  }
]
```

Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

One of the following:

BetaTool object { input\_schema, name, allowed\_callers, 7 more }

input\_schema: object { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

type: optional "custom"

BetaToolBash20241022 object { name, type, allowed\_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20241022"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolBash20250124 object { name, type, allowed\_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250522 object { name, type, allowed\_callers, 3 more }

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250825 object { name, type, allowed\_callers, 3 more }

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20260120 object { name, type, allowed\_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20241022 object { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20241022"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaMemoryTool20250818 object { name, type, allowed\_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20250124 object { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20250124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20241022 object { name, type, allowed\_callers, 4 more }

name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20241022"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20251124 object { display\_height\_px, display\_width\_px, name, 8 more }

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20251124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250124 object { name, type, allowed\_callers, 4 more }

name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250429 object { name, type, allowed\_callers, 4 more }

name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250728 object { name, type, allowed\_callers, 5 more }

name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

max\_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebSearchTool20250305 object { name, type, allowed\_callers, 7 more }

name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user\_location: optional [BetaUserLocation](/docs/en/api/beta#beta_user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebFetchTool20250910 object { name, type, allowed\_callers, 8 more }

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebSearchTool20260209 object { name, type, allowed\_callers, 7 more }

name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user\_location: optional [BetaUserLocation](/docs/en/api/beta#beta_user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebFetchTool20260209 object { name, type, allowed\_callers, 8 more }

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebFetchTool20260309 object { name, type, allowed\_callers, 9 more }

Web fetch tool with use\_cache parameter for bypassing cached content.

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260309"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

use\_cache: optional boolean

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

BetaAdvisorTool20260301 object { model, name, type, 6 more }

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string

name: "advisor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "advisor\_20260301"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

caching: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolBm25\_20251119 object { name, type, allowed\_callers, 3 more }

name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool\_search\_tool\_bm25\_20251119" or "tool\_search\_tool\_bm25"

One of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolRegex20251119 object { name, type, allowed\_callers, 3 more }

name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool\_search\_tool\_regex\_20251119" or "tool\_search\_tool\_regex"

One of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaMCPToolset object { mcp\_server\_name, type, cache\_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: string

Name of the MCP server to configure tools for

type: "mcp\_toolset"

cache\_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

* `5m`: 5 minutes
* `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

configs: optional map[[BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config) { defer\_loading, enabled } ]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: optional boolean

enabled: optional boolean

default\_config: optional [BetaMCPToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config) { defer\_loading, enabled }

Default configuration applied to all tools from this server

defer\_loading: optional boolean

enabled: optional boolean

Deprecatedtop\_k: optional number

Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0

Deprecatedtop\_p: optional number

Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

user\_profile\_id: optional string

The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization.

# ReturnsExpand Collapse

BetaMessage object { id, container, content, 9 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

```
[{"type": "text", "text": "B)"}]
```

One of the following:

BetaTextBlock object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:

BetaCitationCharLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock object { data, type }

data: string

type: "redacted\_thinking"

BetaToolUseBlock object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "advisor" or "web\_search" or "web\_fetch" or 5 more

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

One of the following:

BetaWebSearchToolResultError object { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type }  or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

One of the following:

BetaWebFetchToolResultErrorBlock object { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock object { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type }  or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

One of the following:

BetaBase64PDFSource object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaAdvisorToolResultBlock object { content, tool\_use\_id, type }

content: [BetaAdvisorToolResultError](/docs/en/api/beta#beta_advisor_tool_result_error) { error\_code, type }  or [BetaAdvisorResultBlock](/docs/en/api/beta#beta_advisor_result_block) { text, type }  or [BetaAdvisorRedactedResultBlock](/docs/en/api/beta#beta_advisor_redacted_result_block) { encrypted\_content, type }

One of the following:

BetaAdvisorToolResultError object { error\_code, type }

error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 3 more

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

type: "advisor\_tool\_result\_error"

BetaAdvisorResultBlock object { text, type }

text: string

type: "advisor\_result"

BetaAdvisorRedactedResultBlock object { encrypted\_content, type }

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"

BetaCodeExecutionToolResultBlock object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:

BetaCodeExecutionToolResultError object { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

One of the following:

BetaBashCodeExecutionToolResultError object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

One of the following:

BetaTextEditorCodeExecutionToolResultError object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

One of the following:

BetaToolSearchToolResultError object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

One of the following:

string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:

BetaCitationCharLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock object { content, encrypted\_content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"

context\_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

One of the following:

BetaClearToolUses20250919EditResponse object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

diagnostics: [BetaDiagnostics](/docs/en/api/beta#beta_diagnostics) { cache\_miss\_reason }

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.

cache\_miss\_reason: [BetaCacheMissModelChanged](/docs/en/api/beta#beta_cache_miss_model_changed) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissSystemChanged](/docs/en/api/beta#beta_cache_miss_system_changed) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissToolsChanged](/docs/en/api/beta#beta_cache_miss_tools_changed) { cache\_missed\_input\_tokens, type }  or 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:

BetaCacheMissModelChanged object { cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"

BetaCacheMissSystemChanged object { cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"

BetaCacheMissToolsChanged object { cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"

BetaCacheMissMessagesChanged object { cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"

BetaCacheMissPreviousMessageNotFound object { type }

type: "previous\_message\_not\_found"

BetaCacheMissUnavailable object { type }

type: "unavailable"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: [BetaRefusalStopDetails](/docs/en/api/beta#beta_refusal_stop_details) { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

* `"end_turn"`: the model reached a natural stopping point
* `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
* `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
* `"tool_use"`: the model invoked one or more tools
* `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
* `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

* Determine which iterations exceeded long context thresholds (>=200k tokens)
* Calculate the true context window size from the last iteration
* Understand token accumulation across server-side tool use loops

One of the following:

BetaMessageIterationUsage object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

BetaAdvisorMessageIterationUsage object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Token usage for an advisor sub-inference iteration.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

One of the following:

"standard"

"fast"

BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](/docs/en/api/beta#beta_raw_message_start_event) { message, type }  or [BetaRawMessageDeltaEvent](/docs/en/api/beta#beta_raw_message_delta_event) { context\_management, delta, type, usage }  or [BetaRawMessageStopEvent](/docs/en/api/beta#beta_raw_message_stop_event) { type }  or 3 more

One of the following:

BetaRawMessageStartEvent object { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 9 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

```
[{"type": "text", "text": "B)"}]
```

One of the following:

BetaTextBlock object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:

BetaCitationCharLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock object { data, type }

data: string

type: "redacted\_thinking"

BetaToolUseBlock object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "advisor" or "web\_search" or "web\_fetch" or 5 more

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

One of the following:

BetaWebSearchToolResultError object { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type }  or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

One of the following:

BetaWebFetchToolResultErrorBlock object { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock object { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type }  or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

One of the following:

BetaBase64PDFSource object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaAdvisorToolResultBlock object { content, tool\_use\_id, type }

content: [BetaAdvisorToolResultError](/docs/en/api/beta#beta_advisor_tool_result_error) { error\_code, type }  or [BetaAdvisorResultBlock](/docs/en/api/beta#beta_advisor_result_block) { text, type }  or [BetaAdvisorRedactedResultBlock](/docs/en/api/beta#beta_advisor_redacted_result_block) { encrypted\_content, type }

One of the following:

BetaAdvisorToolResultError object { error\_code, type }

error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 3 more

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

type: "advisor\_tool\_result\_error"

BetaAdvisorResultBlock object { text, type }

text: string

type: "advisor\_result"

BetaAdvisorRedactedResultBlock object { encrypted\_content, type }

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"

BetaCodeExecutionToolResultBlock object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:

BetaCodeExecutionToolResultError object { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

One of the following:

BetaBashCodeExecutionToolResultError object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

One of the following:

BetaTextEditorCodeExecutionToolResultError object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

One of the following:

BetaToolSearchToolResultError object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

One of the following:

string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:

BetaCitationCharLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock object { content, encrypted\_content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"

context\_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

One of the following:

BetaClearToolUses20250919EditResponse object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

diagnostics: [BetaDiagnostics](/docs/en/api/beta#beta_diagnostics) { cache\_miss\_reason }

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.

cache\_miss\_reason: [BetaCacheMissModelChanged](/docs/en/api/beta#beta_cache_miss_model_changed) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissSystemChanged](/docs/en/api/beta#beta_cache_miss_system_changed) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissToolsChanged](/docs/en/api/beta#beta_cache_miss_tools_changed) { cache\_missed\_input\_tokens, type }  or 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:

BetaCacheMissModelChanged object { cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"

BetaCacheMissSystemChanged object { cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"

BetaCacheMissToolsChanged object { cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"

BetaCacheMissMessagesChanged object { cache\_missed\_input\_tokens, type }

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"

BetaCacheMissPreviousMessageNotFound object { type }

type: "previous\_message\_not\_found"

BetaCacheMissUnavailable object { type }

type: "unavailable"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: [BetaRefusalStopDetails](/docs/en/api/beta#beta_refusal_stop_details) { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

* `"end_turn"`: the model reached a natural stopping point
* `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
* `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
* `"tool_use"`: the model invoked one or more tools
* `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
* `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

* Determine which iterations exceeded long context thresholds (>=200k tokens)
* Calculate the true context window size from the last iteration
* Understand token accumulation across server-side tool use loops

One of the following:

BetaMessageIterationUsage object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

BetaAdvisorMessageIterationUsage object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Token usage for an advisor sub-inference iteration.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

One of the following:

"standard"

"fast"

type: "message\_start"

BetaRawMessageDeltaEvent object { context\_management, delta, type, usage }

context\_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Information about context management strategies applied during the request

applied\_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

One of the following:

BetaClearToolUses20250919EditResponse object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

delta: object { container, stop\_details, stop\_reason, stop\_sequence }

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

stop\_details: [BetaRefusalStopDetails](/docs/en/api/beta#beta_refusal_stop_details) { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

type: "message\_delta"

usage: [BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

* Determine which iterations exceeded long context thresholds (>=200k tokens)
* Calculate the true context window size from the last iteration
* Understand token accumulation across server-side tool use loops

One of the following:

BetaMessageIterationUsage object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

BetaAdvisorMessageIterationUsage object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Token usage for an advisor sub-inference iteration.

cache\_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration

output\_tokens: number

The cumulative number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

BetaRawMessageStopEvent object { type }

type: "message\_stop"

BetaRawContentBlockStartEvent object { content\_block, index, type }

content\_block: [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }  or [BetaThinkingBlock](/docs/en/api/beta#beta_thinking_block) { signature, thinking, type }  or [BetaRedactedThinkingBlock](/docs/en/api/beta#beta_redacted_thinking_block) { data, type }  or 13 more

Response model for a file uploaded to the container.

One of the following:

BetaTextBlock object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:

BetaCitationCharLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock object { data, type }

data: string

type: "redacted\_thinking"

BetaToolUseBlock object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "advisor" or "web\_search" or "web\_fetch" or 5 more

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

One of the following:

BetaWebSearchToolResultError object { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type }  or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

One of the following:

BetaWebFetchToolResultErrorBlock object { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock object { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type }  or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

One of the following:

BetaBase64PDFSource object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type }  or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

One of the following:

BetaDirectCaller object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

BetaAdvisorToolResultBlock object { content, tool\_use\_id, type }

content: [BetaAdvisorToolResultError](/docs/en/api/beta#beta_advisor_tool_result_error) { error\_code, type }  or [BetaAdvisorResultBlock](/docs/en/api/beta#beta_advisor_result_block) { text, type }  or [BetaAdvisorRedactedResultBlock](/docs/en/api/beta#beta_advisor_redacted_result_block) { encrypted\_content, type }

One of the following:

BetaAdvisorToolResultError object { error\_code, type }

error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 3 more

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

type: "advisor\_tool\_result\_error"

BetaAdvisorResultBlock object { text, type }

text: string

type: "advisor\_result"

BetaAdvisorRedactedResultBlock object { encrypted\_content, type }

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"

BetaCodeExecutionToolResultBlock object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:

BetaCodeExecutionToolResultError object { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

One of the following:

BetaBashCodeExecutionToolResultError object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

One of the following:

BetaTextEditorCodeExecutionToolResultError object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

One of the following:

BetaToolSearchToolResultError object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

One of the following:

string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:

BetaCitationCharLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock object { content, encrypted\_content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"

index: number

type: "content\_block\_start"

BetaRawContentBlockDeltaEvent object { delta, index, type }

delta: [BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta)

One of the following:

BetaTextDelta object { text, type }

text: string

type: "text\_delta"

BetaInputJSONDelta object { partial\_json, type }

partial\_json: string

type: "input\_json\_delta"

BetaCitationsDelta object { citation, type }

citation: [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

One of the following:

BetaCitationCharLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "citations\_delta"

BetaThinkingDelta object { thinking, type }

thinking: string

type: "thinking\_delta"

BetaSignatureDelta object { signature, type }

signature: string

type: "signature\_delta"

BetaCompactionContentBlockDelta object { content, encrypted\_content, type }

content: string

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction\_delta"

index: number

type: "content\_block\_delta"

BetaRawContentBlockStopEvent object { index, type }

index: number

type: "content\_block\_stop"

Create a Message

cURL

```
curl https://api.anthropic.com/v1/messages \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    --max-time 600 \
    -d "{
          \"max_tokens\": 1024,
          \"messages\": [
            {
              \"content\": \"Hello, world\",
              \"role\": \"user\"
            }
          ],
          \"model\": \"claude-opus-4-6\",
          \"system\": [
            {
              \"text\": \"Today's date is 2024-06-01.\",
              \"type\": \"text\"
            }
          ],
          \"temperature\": 1,
          \"thinking\": {
            \"type\": \"adaptive\"
          },
          \"tools\": [
            {
              \"input_schema\": {
                \"type\": \"object\",
                \"properties\": {
                  \"location\": \"bar\",
                  \"unit\": \"bar\"
                },
                \"required\": [
                  \"location\"
                ]
              },
              \"name\": \"name\"
            }
          ],
          \"top_k\": 5,
          \"top_p\": 0.7
        }"
```

Response 200

```
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "pdf",
        "type": "anthropic",
        "version": "latest"
      }
    ]
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "cited_text",
          "document_index": 0,
          "document_title": "document_title",
          "end_char_index": 0,
          "file_id": "file_id",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "explanation",
    "type": "refusal"
  },
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "inference_geo",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard",
    "speed": "standard"
  }
}
```

# Returns Examples

Response 200

```
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "pdf",
        "type": "anthropic",
        "version": "latest"
      }
    ]
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "cited_text",
          "document_index": 0,
          "document_title": "document_title",
          "end_char_index": 0,
          "file_id": "file_id",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "explanation",
    "type": "refusal"
  },
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "inference_geo",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard",
    "speed": "standard"
  }
}
```
