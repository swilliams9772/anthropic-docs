# Count tokens in a Message

**Source:** http://platform.claude.com/docs/en/api/beta/messages/count_tokens

Copy page

cURL

# Count tokens in a Message

POST/v1/messages/count\_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

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

mcp\_servers: optional array of [BetaRequestMCPServerURLDefinition](/docs/en/api/beta#beta_request_mcp_server_url_definition) { name, type, url, 2 more }

MCP servers to be utilized in this request

name: string

type: "url"

url: string

authorization\_token: optional string

tool\_configuration: optional [BetaRequestMCPServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration) { allowed\_tools, enabled }

allowed\_tools: optional array of string

enabled: optional boolean

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

speed: optional "standard" or "fast"

The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

One of the following:

"standard"

"fast"

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

tools: optional array of [BetaTool](/docs/en/api/beta#beta_tool) { input\_schema, name, allowed\_callers, 7 more }  or [BetaToolBash20241022](/docs/en/api/beta#beta_tool_bash_20241022) { name, type, allowed\_callers, 4 more }  or [BetaToolBash20250124](/docs/en/api/beta#beta_tool_bash_20250124) { name, type, allowed\_callers, 4 more }  or 20 more

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

# ReturnsExpand Collapse

BetaMessageTokensCount object { context\_management, input\_tokens }

context\_management: [BetaCountTokensContextManagementResponse](/docs/en/api/beta#beta_count_tokens_context_management_response) { original\_input\_tokens }

Information about context management applied to the message.

original\_input\_tokens: number

The original token count before context management was applied

input\_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

cURL

```
curl https://api.anthropic.com/v1/messages/count_tokens \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d "{
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
          ]
        }"
```

Response 200

```
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```

# Returns Examples

Response 200

```
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```
