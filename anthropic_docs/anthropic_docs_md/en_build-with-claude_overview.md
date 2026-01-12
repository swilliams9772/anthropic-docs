# Features overview

**Source:** https://platform.claude.com/docs/en/build-with-claude/overview

Copy page

# Core capabilities

These features enhance Claude's fundamental abilities for processing, analyzing, and generating content across various formats and use cases.

| Feature | Description | Availability |
| --- | --- | --- |
| [1M token context window](/docs/en/build-with-claude/context-windows#1m-token-context-window) | An extended context window that allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Agent Skills](/docs/en/agents-and-tools/agent-skills/overview) | Extend Claude's capabilities with Skills. Use pre-built Skills (PowerPoint, Excel, Word, PDF) or create custom Skills with instructions and scripts. Skills use progressive disclosure to efficiently manage context. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Batch processing](/docs/en/build-with-claude/batch-processing) | Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Batch API calls costs 50% less than standard API calls. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI |
| [Citations](/docs/en/build-with-claude/citations) | Ground Claude's responses in source documents. With Citations, Claude can provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Context editing](/docs/en/build-with-claude/context-editing) | Automatically manage conversation context with configurable strategies. Supports clearing tool results when approaching token limits and managing thinking blocks in extended thinking conversations. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Effort](/docs/en/build-with-claude/effort) | Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Extended thinking](/docs/en/build-with-claude/extended-thinking) | Enhanced reasoning capabilities for complex tasks, providing transparency into Claude's step-by-step thought process before delivering its final answer. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Files API](/docs/en/build-with-claude/files) | Upload and manage files to use with Claude without re-uploading content with each request. Supports PDFs, images, and text files. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [PDF support](/docs/en/build-with-claude/pdf-support) | Process and analyze text and visual content from PDF documents. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Prompt caching (5m)](/docs/en/build-with-claude/prompt-caching) | Provide Claude with more background knowledge and example outputs to reduce costs and latency. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Prompt caching (1hr)](/docs/en/build-with-claude/prompt-caching#1-hour-cache-duration) | Extended 1-hour cache duration for less frequently accessed but important context, complementing the standard 5-minute cache. | Claude API  Microsoft Foundry |
| [Search results](/docs/en/build-with-claude/search-results) | Enable natural citations for RAG applications by providing search results with proper source attribution. Achieve web search-quality citations for custom knowledge bases and tools. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Structured outputs](/docs/en/build-with-claude/structured-outputs) | Guarantee schema conformance with two approaches: JSON outputs for structured data responses, and strict tool use for validated tool inputs. Available on Sonnet 4.5, Opus 4.1, Opus 4.5, and Haiku 4.5. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Token counting](/docs/en/api/messages-count-tokens) | Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Tool use](/docs/en/agents-and-tools/tool-use/overview) | Enable Claude to interact with external tools and APIs to perform a wider variety of tasks. For a list of supported tools, see [the Tools table](#tools). | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |

# Tools

These features enable Claude to interact with external systems, execute code, and perform automated tasks through various tool interfaces.

| Feature | Description | Availability |
| --- | --- | --- |
| [Bash](/docs/en/agents-and-tools/tool-use/bash-tool) | Execute bash commands and scripts to interact with the system shell and perform command-line operations. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Code execution](/docs/en/agents-and-tools/tool-use/code-execution-tool) | Run Python code in a sandboxed environment for advanced data analysis. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) | Enable Claude to call your tools programmatically from within code execution containers, reducing latency and token consumption for multi-tool workflows. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Computer use](/docs/en/agents-and-tools/tool-use/computer-use-tool) | Control computer interfaces by taking screenshots and issuing mouse and keyboard commands. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming) | Stream tool use parameters without buffering/JSON validation, reducing latency for receiving large parameters. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [MCP connector](/docs/en/agents-and-tools/mcp-connector) | Connect to remote [MCP](/docs/en/mcp) servers directly from the Messages API without a separate MCP client. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Memory](/docs/en/agents-and-tools/tool-use/memory-tool) | Enable Claude to store and retrieve information across conversations. Build knowledge bases over time, maintain project context, and learn from past interactions. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Text editor](/docs/en/agents-and-tools/tool-use/text-editor-tool) | Create and edit text files with a built-in text editor interface for file manipulation tasks. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Tool search](/docs/en/agents-and-tools/tool-use/tool-search-tool) | Scale to thousands of tools by dynamically discovering and loading tools on-demand using regex-based search, optimizing context usage and improving tool selection accuracy. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Web fetch](/docs/en/agents-and-tools/tool-use/web-fetch-tool) | Retrieve full content from specified web pages and PDF documents for in-depth analysis. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Web search](/docs/en/agents-and-tools/tool-use/web-search-tool) | Augment Claude's comprehensive knowledge with current, real-world data from across the web. | Claude API  Google Cloud's Vertex AI  Microsoft Foundry |
