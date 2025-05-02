---
title: 
source_url: https://docs.anthropic.com/en/docs/build-with-claude/pdf-support/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Build with Claude

PDF support

[Welcome](/en/home)[User Guides](/en/docs/welcome)[API Reference](/en/api/getting-started)[Prompt Library](/en/prompt-library/library)[Release Notes](/en/release-notes/overview)

- [Developer Console](https://console.anthropic.com/)
- [Developer Discord](https://www.anthropic.com/discord)
- [Support](https://support.anthropic.com/)

##### Get started

* [Overview](/en/docs/welcome)
* [Initial setup](/en/docs/initial-setup)
* [Intro to Claude](/en/docs/intro-to-claude)

##### Learn about Claude

* Use cases
* Models & pricing
* [Security and compliance](https://trust.anthropic.com/)

##### Build with Claude

* [Define success criteria](/en/docs/build-with-claude/define-success)
* [Develop test cases](/en/docs/build-with-claude/develop-tests)
* [Context windows](/en/docs/build-with-claude/context-windows)
* [Vision](/en/docs/build-with-claude/vision)
* Prompt engineering
* [Extended thinking](/en/docs/build-with-claude/extended-thinking)
* [Multilingual support](/en/docs/build-with-claude/multilingual-support)
* Tool use (function calling)
* [Prompt caching](/en/docs/build-with-claude/prompt-caching)
* [PDF support](/en/docs/build-with-claude/pdf-support)
* [Citations](/en/docs/build-with-claude/citations)
* [Token counting](/en/docs/build-with-claude/token-counting)
* [Batch processing](/en/docs/build-with-claude/batch-processing)
* [Embeddings](/en/docs/build-with-claude/embeddings)

##### Agents and tools

* Claude Code
* [Computer use (beta)](/en/docs/agents-and-tools/computer-use)
* [Model Context Protocol (MCP)](/en/docs/agents-and-tools/mcp)
* [Google Sheets add-on](/en/docs/agents-and-tools/claude-for-sheets)

##### Test and evaluate

* Strengthen guardrails
* [Using the Evaluation Tool](/en/docs/test-and-evaluate/eval-tool)

##### Administration

* [Admin API](/en/docs/administration/administration-api)

##### Resources

* [Glossary](/en/docs/resources/glossary)
* [Model deprecations](/en/docs/resources/model-deprecations)
* [System status](https://status.anthropic.com/)
* [Claude 3 model card](https://assets.anthropic.com/m/61e7d27f8c8f5919/original/Claude-3-Model-Card.pdf)
* [Claude 3.7 system card](https://anthropic.com/claude-3-7-sonnet-system-card)
* [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
* [Anthropic Courses](https://github.com/anthropics/courses)
* [API features](/en/docs/resources/api-features)

##### Legal center

* [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)

You can now ask Claude about any text, pictures, charts, and tables in PDFs you provide. Some sample use cases:

* Analyzing financial reports and understanding charts/tables
* Extracting key information from legal documents
* Translation assistance for documents
* Converting document information into structured formats

[​](#before-you-begin) Before you begin
---------------------------------------

### [​](#check-pdf-requirements) Check PDF requirements

Claude works with any standard PDF. However, you should ensure your request size meet these requirements when using PDF support:

| Requirement | Limit |
| --- | --- |
| Maximum request size | 32MB |
| Maximum pages per request | 100 |
| Format | Standard PDF (no passwords/encryption) |

Please note that both limits are on the entire request payload, including any other content sent alongside PDFs.

Since PDF support relies on Claude’s vision capabilities, it is subject to the same [limitations and considerations](/en/docs/build-with-claude/vision#limitations) as other vision tasks.

### [​](#supported-platforms-and-models) Supported platforms and models

PDF support is currently available on Claude 3.7 Sonnet (`claude-3-7-sonnet-20250219`), both Claude 3.5 Sonnet models (`claude-3-5-sonnet-20241022`, `claude-3-5-sonnet-20240620`), and Claude 3.5 Haiku (`claude-3-5-haiku-20241022`) via direct API access and Google Vertex AI. This functionality will be supported on Amazon Bedrock soon.

[​](#process-pdfs-with-claude) Process PDFs with Claude
-------------------------------------------------------

### [​](#send-your-first-pdf-request) Send your first PDF request

Let’s start with a simple example using the Messages API. You can provide PDFs to Claude in two ways:

1. As a base64-encoded PDF in `document` content blocks
2. As a URL reference to a PDF hosted online

#### [​](#option-1-url-based-pdf-document) Option 1: URL-based PDF document

The simplest approach is to reference a PDF directly from a URL:

#### [​](#option-2-base64-encoded-pdf-document) Option 2: Base64-encoded PDF document

If you need to send PDFs from your local system or when a URL isn’t available:

### [​](#how-pdf-support-works) How PDF support works

When you send a PDF to Claude, the following steps occur:

1

The system extracts the contents of the document.

* The system converts each page of the document into an image.
* The text from each page is extracted and provided alongside each page’s image.

2

Claude analyzes both the text and images to better understand the document.

* Documents are provided as a combination of text and images for analysis.
* This allows users to ask for insights on visual elements of a PDF, such as charts, diagrams, and other non-textual content.

3

Claude responds, referencing the PDF's contents if relevant.

Claude can reference both textual and visual content when it responds. You can further improve performance by integrating PDF support with:

* **Prompt caching**: To improve performance for repeated analysis.
* **Batch processing**: For high-volume document processing.
* **Tool use**: To extract specific information from documents for use as tool inputs.

### [​](#estimate-your-costs) Estimate your costs

The token count of a PDF file depends on the total text extracted from the document as well as the number of pages:

* Text token costs: Each page typically uses 1,500-3,000 tokens per page depending on content density. Standard API pricing applies with no additional PDF fees.
* Image token costs: Since each page is converted into an image, the same [image-based cost calculations](/en/docs/build-with-claude/vision#evaluate-image-size) are applied.

You can use [token counting](/en/docs/build-with-claude/token-counting) to estimate costs for your specific PDFs.

[​](#optimize-pdf-processing) Optimize PDF processing
-----------------------------------------------------

### [​](#improve-performance) Improve performance

Follow these best practices for optimal results:

* Place PDFs before text in your requests
* Use standard fonts
* Ensure text is clear and legible
* Rotate pages to proper upright orientation
* Use logical page numbers (from PDF viewer) in prompts
* Split large PDFs into chunks when needed
* Enable prompt caching for repeated analysis

### [​](#scale-your-implementation) Scale your implementation

For high-volume processing, consider these approaches:

#### [​](#use-prompt-caching) Use prompt caching

Cache PDFs to improve performance on repeated queries:

#### [​](#process-document-batches) Process document batches

Use the Message Batches API for high-volume workflows:

[​](#next-steps) Next steps
---------------------------

[Try PDF examples
----------------

Explore practical examples of PDF processing in our cookbook recipe.](https://github.com/anthropics/anthropic-cookbook/tree/main/multimodal)[View API reference
------------------

See complete API documentation for PDF support.](/en/api/messages)

Was this page helpful?

YesNo

[Prompt caching](/en/docs/build-with-claude/prompt-caching)[Citations](/en/docs/build-with-claude/citations)

On this page

* [Before you begin](#before-you-begin)
* [Check PDF requirements](#check-pdf-requirements)
* [Supported platforms and models](#supported-platforms-and-models)
* [Process PDFs with Claude](#process-pdfs-with-claude)
* [Send your first PDF request](#send-your-first-pdf-request)
* [Option 1: URL-based PDF document](#option-1-url-based-pdf-document)
* [Option 2: Base64-encoded PDF document](#option-2-base64-encoded-pdf-document)
* [How PDF support works](#how-pdf-support-works)
* [Estimate your costs](#estimate-your-costs)
* [Optimize PDF processing](#optimize-pdf-processing)
* [Improve performance](#improve-performance)
* [Scale your implementation](#scale-your-implementation)
* [Use prompt caching](#use-prompt-caching)
* [Process document batches](#process-document-batches)
* [Next steps](#next-steps)