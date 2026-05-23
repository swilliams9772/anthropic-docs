# Create a Message

**Source:** http://platform.claude.com/docs/en/api/cli/messages/create

Copy page

CLI

# Create a Message

$ ant messages create

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

# ParametersExpand Collapse

--max-tokens: number

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

--message: array of [MessageParam](/docs/en/api/messages#message_param) { content, role }

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

--model: "claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

--cache-control: optional object { type, ttl }

Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

--container: optional string

Container identifier for reuse across requests.

--inference-geo: optional string

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

--metadata: optional object { user\_id }

An object describing metadata about the request.

--output-config: optional object { effort, format }

Configuration options for the model's output, such as the output format.

--service-tier: optional "auto" or "standard\_only"

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

--stop-sequence: optional array of string

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

--system: optional string or array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache\_control, citations }

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Deprecated--temperature: optional number

Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

--thinking: optional [ThinkingConfigEnabled](/docs/en/api/messages#thinking_config_enabled) { budget\_tokens, type, display }  or [ThinkingConfigDisabled](/docs/en/api/messages#thinking_config_disabled) { type }  or [ThinkingConfigAdaptive](/docs/en/api/messages#thinking_config_adaptive) { type, display }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

--tool-choice: optional [ToolChoiceAuto](/docs/en/api/messages#tool_choice_auto) { type, disable\_parallel\_tool\_use }  or [ToolChoiceAny](/docs/en/api/messages#tool_choice_any) { type, disable\_parallel\_tool\_use }  or [ToolChoiceTool](/docs/en/api/messages#tool_choice_tool) { name, type, disable\_parallel\_tool\_use }  or [ToolChoiceNone](/docs/en/api/messages#tool_choice_none) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

--tool: optional array of [ToolUnion](/docs/en/api/messages#tool_union)

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

Deprecated--top-k: optional number

Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

Deprecated--top-p: optional number

Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

# ReturnsExpand Collapse

message: object { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: object { id, expires\_at }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

content: array of [ContentBlock](/docs/en/api/messages#content_block)

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

text\_block: object { citations, text, type }

citations: array of [TextCitation](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

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

citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

citations\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

tool\_use\_block: object { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"

server\_tool\_use\_block: object { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

web\_search\_tool\_result\_block: object { caller, content, tool\_use\_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

content: [WebSearchToolResultError](/docs/en/api/messages#web_search_tool_result_error) { error\_code, type }  or array of [WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

web\_fetch\_tool\_result\_block: object { caller, content, tool\_use\_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error\_code, type }  or [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved\_at, type, url }

web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media\_type, type }  or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media\_type, type }

base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

plain\_text\_source: object { data, media\_type, type }

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

code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [CodeExecutionToolResultError](/docs/en/api/messages#code_execution_tool_result_error) { error\_code, type }  or [CodeExecutionResultBlock](/docs/en/api/messages#code_execution_result_block) { content, return\_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlock](/docs/en/api/messages#encrypted_code_execution_result_block) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error\_code, type }  or [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool\_references, type }

tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

model: "claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 3 more

The reason that we stopped.

This may be one the following values:

* `"end_turn"`: the model reached a natural stopping point
* `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
* `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
* `"tool_use"`: the model invoked one or more tools
* `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
* `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

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

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

raw\_message\_stream\_event: [RawMessageStartEvent](/docs/en/api/messages#raw_message_start_event) { message, type }  or [RawMessageDeltaEvent](/docs/en/api/messages#raw_message_delta_event) { delta, type, usage }  or [RawMessageStopEvent](/docs/en/api/messages#raw_message_stop_event) { type }  or 3 more

raw\_message\_start\_event: object { message, type }

message: object { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: object { id, expires\_at }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

content: array of [ContentBlock](/docs/en/api/messages#content_block)

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

text\_block: object { citations, text, type }

citations: array of [TextCitation](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

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

citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

citations\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

tool\_use\_block: object { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"

server\_tool\_use\_block: object { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

web\_search\_tool\_result\_block: object { caller, content, tool\_use\_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

content: [WebSearchToolResultError](/docs/en/api/messages#web_search_tool_result_error) { error\_code, type }  or array of [WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

web\_fetch\_tool\_result\_block: object { caller, content, tool\_use\_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error\_code, type }  or [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved\_at, type, url }

web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media\_type, type }  or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media\_type, type }

base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

plain\_text\_source: object { data, media\_type, type }

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

code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [CodeExecutionToolResultError](/docs/en/api/messages#code_execution_tool_result_error) { error\_code, type }  or [CodeExecutionResultBlock](/docs/en/api/messages#code_execution_result_block) { content, return\_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlock](/docs/en/api/messages#encrypted_code_execution_result_block) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error\_code, type }  or [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool\_references, type }

tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

model: "claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 3 more

The reason that we stopped.

This may be one the following values:

* `"end_turn"`: the model reached a natural stopping point
* `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
* `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
* `"tool_use"`: the model invoked one or more tools
* `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
* `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

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

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

type: "message\_start"

raw\_message\_delta\_event: object { delta, type, usage }

delta: object { container, stop\_details, stop\_reason, stop\_sequence }

container: object { id, expires\_at }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 3 more

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: string

type: "message\_delta"

usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

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

output\_tokens: number

The cumulative number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

raw\_message\_stop\_event: object { type }

type: "message\_stop"

raw\_content\_block\_start\_event: object { content\_block, index, type }

content\_block: [TextBlock](/docs/en/api/messages#text_block) { citations, text, type }  or [ThinkingBlock](/docs/en/api/messages#thinking_block) { signature, thinking, type }  or [RedactedThinkingBlock](/docs/en/api/messages#redacted_thinking_block) { data, type }  or 9 more

Response model for a file uploaded to the container.

text\_block: object { citations, text, type }

citations: array of [TextCitation](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

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

citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

citations\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

tool\_use\_block: object { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"

server\_tool\_use\_block: object { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

web\_search\_tool\_result\_block: object { caller, content, tool\_use\_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

content: [WebSearchToolResultError](/docs/en/api/messages#web_search_tool_result_error) { error\_code, type }  or array of [WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

web\_fetch\_tool\_result\_block: object { caller, content, tool\_use\_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool\_id, type }  or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error\_code, type }  or [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved\_at, type, url }

web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media\_type, type }  or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media\_type, type }

base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

plain\_text\_source: object { data, media\_type, type }

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

code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [CodeExecutionToolResultError](/docs/en/api/messages#code_execution_tool_result_error) { error\_code, type }  or [CodeExecutionResultBlock](/docs/en/api/messages#code_execution_result_block) { content, return\_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlock](/docs/en/api/messages#encrypted_code_execution_result_block) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error\_code, type }  or [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool\_references, type }

tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

index: number

type: "content\_block\_start"

raw\_content\_block\_delta\_event: object { delta, index, type }

delta: [TextDelta](/docs/en/api/messages#text_delta) { text, type }  or [InputJSONDelta](/docs/en/api/messages#input_json_delta) { partial\_json, type }  or [CitationsDelta](/docs/en/api/messages#citations_delta) { citation, type }  or 2 more

text\_delta: object { text, type }

text: string

type: "text\_delta"

input\_json\_delta: object { partial\_json, type }

partial\_json: string

type: "input\_json\_delta"

citations\_delta: object { citation, type }

citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited\_text, document\_index, document\_title, 4 more }  or [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited\_text, document\_index, document\_title, 4 more }  or [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

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

citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

citations\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "citations\_delta"

thinking\_delta: object { thinking, type }

thinking: string

type: "thinking\_delta"

signature\_delta: object { signature, type }

signature: string

type: "signature\_delta"

index: number

type: "content\_block\_delta"

raw\_content\_block\_stop\_event: object { index, type }

index: number

type: "content\_block\_stop"

Create a Message

CLI

```
ant messages create \
  --api-key my-anthropic-api-key \
  --max-tokens 1024 \
  --message '{content: [{text: x, type: text}], role: user}' \
  --model claude-opus-4-6
```

Response 200

```
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z"
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
    "output_tokens": 503,
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard"
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
    "expires_at": "2019-12-27T18:11:19.117Z"
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
    "output_tokens": 503,
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard"
  }
}
```
