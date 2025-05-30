# Citations - Anthropic

**Source:** https://docs.anthropic.com/en/docs/build-with-claude/citations

- [Documentation](/en/home)
- [Developer Console](https://console.anthropic.com/)
- [Developer Discord](https://www.anthropic.com/discord)
- [Support](https://support.anthropic.com/)

# First steps

* [Intro to Claude](/en/docs/welcome)
* [Get started](/en/docs/get-started)

# Models & pricing

* [Models overview](/en/docs/about-claude/models/overview)
* [Choosing a model](/en/docs/about-claude/models/choosing-a-model)
* [Migrating to Claude 4](/en/docs/about-claude/models/migrating-to-claude-4)
* [Model deprecations](/en/docs/about-claude/model-deprecations)
* [Pricing](/en/docs/about-claude/pricing)

# Learn about Claude

* [Building with Claude](/en/docs/overview)
* Use cases
* [Context windows](/en/docs/build-with-claude/context-windows)
* [Glossary](/en/docs/about-claude/glossary)
* Prompt engineering

# Explore features

* [Features overview](/en/docs/build-with-claude/overview)
* [Prompt caching](/en/docs/build-with-claude/prompt-caching)
* [Extended thinking](/en/docs/build-with-claude/extended-thinking)
* [Streaming Messages](/en/docs/build-with-claude/streaming)
* [Batch processing](/en/docs/build-with-claude/batch-processing)
* [Citations](/en/docs/build-with-claude/citations)
* [Multilingual support](/en/docs/build-with-claude/multilingual-support)
* [Token counting](/en/docs/build-with-claude/token-counting)
* [Embeddings](/en/docs/build-with-claude/embeddings)
* [Vision](/en/docs/build-with-claude/vision)
* [PDF support](/en/docs/build-with-claude/pdf-support)

# Agent components

* Tools
* Model Context Protocol (MCP)
* [Computer use (beta)](/en/docs/agents-and-tools/computer-use)
* [Google Sheets add-on](/en/docs/agents-and-tools/claude-for-sheets)

# Test & evaluate

* [Define success criteria](/en/docs/test-and-evaluate/define-success)
* [Develop test cases](/en/docs/test-and-evaluate/develop-tests)
* Strengthen guardrails
* [Using the Evaluation Tool](/en/docs/test-and-evaluate/eval-tool)

# Legal center

* [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)
* [Security and compliance](https://trust.anthropic.com/)

Claude is capable of providing detailed citations when answering questions about documents, helping you track and verify information sources in responses.

The citations feature is currently available on Claude Opus 4, Claude Sonnet 4, Claude Sonnet 3.7, Claude Sonnet 3.5 (new) and Haiku 3.5.

*Citations with Claude Sonnet 3.7*

Claude Sonnet 3.7 may be less likely to make citations compared to other Claude models without more explicit instructions from the user. When using citations with Claude Sonnet 3.7, we recommend including additional instructions in the `user` turn, like `"Use citations to back up your answer."` for example.

We’ve also observed that when the model is asked to structure its response, it is unlikely to use citations unless explicitly told to use citations within that format. For example, if the model is asked to use tags in its response, you should add something like “Always use citations in your answer, even within .”

Please share your feedback and suggestions about the citations feature using this [form](https://forms.gle/9n9hSrKnKe3rpowH9).

Here’s an example of how to use citations with the Messages API:

Shell

Python

Java

```
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-20250514",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "document",
            "source": {
              "type": "text",
              "media_type": "text/plain",
              "data": "The grass is green. The sky is blue."
            },
            "title": "My Document",
            "context": "This is a trustworthy document.",
            "citations": {"enabled": true}
          },
          {
            "type": "text",
            "text": "What color is the grass and sky?"
          }
        ]
      }
    ]
  }'

```

**Comparison with prompt-based approaches**

In comparison with prompt-based citations solutions, the citations feature has the following advantages:

* **Cost savings:** If your prompt-based approach asks Claude to output direct quotes, you may see cost savings due to the fact that `cited_text` does not count towards your output tokens.
* **Better citation reliability:** Because we parse citations into the respective response formats mentioned above and extract `cited_text`, citations are guaranteed to contain valid pointers to the provided documents.
* **Improved citation quality:** In our evals, we found the citations feature to be significantly more likely to cite the most relevant quotes from documents as compared to purely prompt-based approaches.

# [​](#how-citations-work) How citations work

Integrate citations with Claude in these steps:

1

Provide document(s) and enable citations

* Include documents in any of the supported formats: [PDFs](/_sites/docs.anthropic.com/en/docs/build-with-claude/citations#pdf-documents), [plain text](/_sites/docs.anthropic.com/en/docs/build-with-claude/citations#plain-text-documents), or [custom content](/_sites/docs.anthropic.com/en/docs/build-with-claude/citations#custom-content-documents) documents
* Set `citations.enabled=true` on each of your documents. Currently, citations must be enabled on all or none of the documents within a request.
* Note that only text citations are currently supported and image citations are not yet possible.

2

Documents get processed

* Document contents are “chunked” in order to define the minimum granularity of possible citations. For example, sentence chunking would allow Claude to cite a single sentence or chain together multiple consecutive sentences to cite a paragraph (or longer)!
  + **For PDFs:** Text is extracted as described in [PDF Support](/en/docs/build-with-claude/pdf-support) and content is chunked into sentences. Citing images from PDFs is not currently supported.
  + **For plain text documents:** Content is chunked into sentences that can be cited from.
  + **For custom content documents:** Your provided content blocks are used as-is and no further chunking is done.

3

Claude provides cited response

* Responses may now include multiple text blocks where each text block can contain a claim that Claude is making and a list of citations that support the claim.
* Citations reference specific locations in source documents. The format of these citations are dependent on the type of document being cited from.
  + **For PDFs:** citations will include the page number range (1-indexed).
  + **For plain text documents:** Citations will include the character index range (0-indexed).
  + **For custom content documents:** Citations will include the content block index range (0-indexed) corresponding to the original content list provided.
* Document indices are provided to indicate the reference source and are 0-indexed according to the list of all documents in your original request.

**Automatic chunking vs custom content**

By default, plain text and PDF documents are automatically chunked into sentences. If you need more control over citation granularity (e.g., for bullet points or transcripts), use custom content documents instead. See [Document Types](/_sites/docs.anthropic.com/en/docs/build-with-claude/citations#document-types) for more details.

For example, if you want Claude to be able to cite specific sentences from your RAG chunks, you should put each RAG chunk into a plain text document. Otherwise, if you do not want any further chunking to be done, or if you want to customize any additional chunking, you can put RAG chunks into custom content document(s).

# [​](#citable-vs-non-citable-content) Citable vs non-citable content

* Text found within a document’s `source` content can be cited from.
* `title` and `context` are optional fields that will be passed to the model but not used towards cited content.
* `title` is limited in length so you may find the `context` field to be useful in storing any document metadata as text or stringified json.

# [​](#citation-indices) Citation indices

* Document indices are 0-indexed from the list of all document content blocks in the request (spanning across all messages).
* Character indices are 0-indexed with exclusive end indices.
* Page numbers are 1-indexed with exclusive end page numbers.
* Content block indices are 0-indexed with exclusive end indices from the `content` list provided in the custom content document.

# [​](#token-costs) Token costs

* Enabling citations incurs a slight increase in input tokens due to system prompt additions and document chunking.
* However, the citations feature is very efficient with output tokens. Under the hood, the model is outputting citations in a standardized format that are then parsed into cited text and document location indices. The `cited_text` field is provided for convenience and does not count towards output tokens.
* When passed back in subsequent conversation turns, `cited_text` is also not counted towards input tokens.

# [​](#feature-compatibility) Feature compatibility

Citations works in conjunction with other API features including [prompt caching](/en/docs/build-with-claude/prompt-caching), [token counting](/en/docs/build-with-claude/token-counting) and [batch processing](/en/docs/build-with-claude/batch-processing).

# [​](#using-prompt-caching-with-citations) Using Prompt Caching with Citations

Citations and prompt caching can be used together effectively.

The citation blocks generated in responses cannot be cached directly, but the source documents they reference can be cached. To optimize performance, apply `cache_control` to your top-level document content blocks.

Python

TypeScript

Shell

```
import anthropic

client = anthropic.Anthropic()

# Long document content (e.g., technical documentation)

long_document = "This is a very long document with thousands of words..." + " ... " * 1000  # Minimum cacheable length

response = client.messages.create(
    model="claude-opus-4-20250514",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "text",
                        "media_type": "text/plain",
                        "data": long_document
                    },
                    "citations": {"enabled": True},
                    "cache_control": {"type": "ephemeral"}  # Cache the document content
                },
                {
                    "type": "text",
                    "text": "What does this document say about API features?"
                }
            ]
        }
    ]
)

```

In this example:

* The document content is cached using `cache_control` on the document block
* Citations are enabled on the document
* Claude can generate responses with citations while benefiting from cached document content
* Subsequent requests using the same document will benefit from the cached content

# [​](#document-types) Document Types

# [​](#choosing-a-document-type) Choosing a document type

We support three document types for citations. Documents can be provided directly in the message (base64, text, or URL) or uploaded via the [Files API](/en/docs/build-with-claude/files) and referenced by `file_id`:

| Type | Best for | Chunking | Citation format |
| --- | --- | --- | --- |
| Plain text | Simple text documents, prose | Sentence | Character indices (0-indexed) |
| PDF | PDF files with text content | Sentence | Page numbers (1-indexed) |
| Custom content | Lists, transcripts, special formatting, more granular citations | No additional chunking | Block indices (0-indexed) |

# [​](#plain-text-documents) Plain text documents

Plain text documents are automatically chunked into sentences. You can provide them inline or by reference with their `file_id`:

```
{
    "type": "document",
    "source": {
        "type": "text",
        "media_type": "text/plain",
        "data": "Plain text content..."
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}

```

```
{
    "type": "document",
    "source": {
        "type": "text",
        "media_type": "text/plain",
        "data": "Plain text content..."
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}

```

```
{
    "type": "document",
    "source": {
        "type": "file",
        "file_id": "file_011CNvxoj286tYUAZFiZMf1U"
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}

```

Example plain text citation

```
{
    "type": "char_location",
    "cited_text": "The exact text being cited", # not counted towards output tokens
    "document_index": 0,
    "document_title": "Document Title",
    "start_char_index": 0,    # 0-indexed
    "end_char_index": 50      # exclusive
}

```

# [​](#pdf-documents) PDF documents

PDF documents can be provided as base64-encoded data or by `file_id`. PDF text is extracted and chunked into sentences. As image citations are not yet supported, PDFs that are scans of documents and do not contain extractable text will not be citable.

```
{
    "type": "document",
    "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": base64_encoded_pdf_data
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}

```

```
{
    "type": "document",
    "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": base64_encoded_pdf_data
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}

```

```
{
    "type": "document",
    "source": {
        "type": "file",
        "file_id": "file_011CNvxoj286tYUAZFiZMf1U"
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}

```

Example PDF citation

```
{
    "type": "page_location",
    "cited_text": "The exact text being cited", # not counted towards output tokens
    "document_index": 0,
    "document_title": "Document Title",
    "start_page_number": 1,  # 1-indexed
    "end_page_number": 2     # exclusive
}

```

# [​](#custom-content-documents) Custom content documents

Custom content documents give you control over citation granularity. No additional chunking is done and chunks are provided to the model according to the content blocks provided.

```
{
    "type": "document",
    "source": {
        "type": "content",
        "content": [
            {"type": "text", "text": "First chunk"},
            {"type": "text", "text": "Second chunk"}
        ]
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}

```

Example citation

```
{
    "type": "content_block_location",
    "cited_text": "The exact text being cited", # not counted towards output tokens
    "document_index": 0,
    "document_title": "Document Title",
    "start_block_index": 0,   # 0-indexed
    "end_block_index": 1      # exclusive
}

```

# [​](#response-structure) Response Structure

When citations are enabled, responses include multiple text blocks with citations:

```
{
    "content": [
        {
            "type": "text",
            "text": "According to the document, "
        },
        {
            "type": "text",
            "text": "the grass is green",
            "citations": [{
                "type": "char_location",
                "cited_text": "The grass is green.",
                "document_index": 0,
                "document_title": "Example Document",
                "start_char_index": 0,
                "end_char_index": 20
            }]
        },
        {
            "type": "text",
            "text": " and "
        },
        {
            "type": "text",
            "text": "the sky is blue",
            "citations": [{
                "type": "char_location",
                "cited_text": "The sky is blue.",
                "document_index": 0,
                "document_title": "Example Document",
                "start_char_index": 20,
                "end_char_index": 36
            }]
        }
    ]
}

```

# [​](#streaming-support) Streaming Support

For streaming responses, we’ve added a `citations_delta` type that contains a single citation to be added to the `citations` list on the current `text` content block.

Example streaming events

```
event: message_start
data: {"type": "message_start", ...}

event: content_block_start
data: {"type": "content_block_start", "index": 0, ...}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0,
       "delta": {"type": "text_delta", "text": "According to..."}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0,
       "delta": {"type": "citations_delta",
                 "citation": {
                     "type": "char_location",
                     "cited_text": "...",
                     "document_index": 0,
                     ...
                 }}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: message_stop
data: {"type": "message_stop"}

```

Was this page helpful?

YesNo

Batch processing[Multilingual support](/en/docs/build-with-claude/multilingual-support)

On this page
