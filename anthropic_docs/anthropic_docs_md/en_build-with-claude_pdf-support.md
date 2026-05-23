# PDF support

**Source:** http://platform.claude.com/docs/en/build-with-claude/pdf-support

Copy page

This feature is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

You can ask Claude about any text, pictures, charts, and tables in PDFs you provide. Some sample use cases:

* Analyzing financial reports and understanding charts/tables
* Extracting key information from legal documents
* Translation assistance for documents
* Converting document information into structured formats

# Before you begin

# Check PDF requirements

Claude works with any standard PDF. Ensure your request size meets these requirements:

| Requirement | Limit |
| --- | --- |
| Maximum request size | 32 MB ([varies by platform](/docs/en/api/overview#request-size-limits)) |
| Maximum pages per request | 600 (100 for models with a 200k-token context window) |
| Format | Standard PDF (no passwords/encryption) |

Both limits are on the entire request payload, including any other content sent alongside PDFs. For large PDFs, consider uploading with the [Files API](#option-3-files-api) and referencing by `file_id` to keep request payloads small.

Dense PDFs (many small-font pages, complex tables, or heavy graphics) can fill the context window before reaching the page limit. Requests with large PDFs can also fail before reaching the page limit, even when using the Files API. Try splitting the document into sections; for large files, since each page is processed as an image, downsampling embedded images can also help.

Since PDF support relies on Claude's vision capabilities, it is subject to the same [limitations and considerations](/docs/en/build-with-claude/vision#limitations) as other vision tasks.

# Supported platforms and models

PDF support is available on the Claude API, [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), [Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock) (see [Amazon Bedrock PDF support](#amazon-bedrock-pdf-support)), [Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai), and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry). All [active models](/docs/en/about-claude/models/overview) support PDF processing.

# Amazon Bedrock PDF support

When using PDF support through Bedrock's Converse API, there are two distinct document processing modes:

**Important:** To access Claude's full visual PDF understanding capabilities in the Converse API, you must enable citations. Without citations enabled, the API falls back to basic text extraction only. Learn more about [working with citations](/docs/en/build-with-claude/citations).

# Document processing modes

1. **Converse Document Chat** (Original mode - Text extraction only)

   * Provides basic text extraction from PDFs
   * Cannot analyze images, charts, or visual layouts within PDFs
   * Uses approximately 1,000 tokens for a 3-page PDF
   * Automatically used when citations are not enabled
2. **Claude PDF Chat** (New mode - Full visual understanding)

   * Provides complete visual analysis of PDFs
   * Can understand and analyze charts, graphs, images, and visual layouts
   * Processes each page as both text and image for comprehensive understanding
   * Uses approximately 7,000 tokens for a 3-page PDF
   * **Requires citations to be enabled** in the Converse API

# Key limitations

* **Converse API**: Visual PDF analysis requires citations to be enabled. There is currently no option to use visual analysis without citations (unlike the InvokeModel API).
* **InvokeModel API**: Provides full control over PDF processing without forced citations.

# Common issues

If Claude isn't seeing images or charts in your PDFs when using the Converse API, you likely need to enable the citations flag. Without it, Converse falls back to basic text extraction only.

This is a known constraint with the Converse API. For applications that require visual PDF analysis without citations, consider using the InvokeModel API instead.

For non-PDF files like .csv, .xlsx, .docx, .md, or .txt files, see [Working with other file formats](/docs/en/build-with-claude/files#working-with-other-file-formats).

---

# Process PDFs with Claude

# Send your first PDF request

Let's start with a simple example using the Messages API. You can provide PDFs to Claude in three ways:

1. As a URL reference to a PDF hosted online
2. As a base64-encoded PDF in `document` content blocks
3. By a `file_id` from the [Files API](/docs/en/build-with-claude/files)

On Amazon Bedrock and Vertex AI, only base64-encoded sources are currently available.

# Option 1: URL-based PDF document

The simplest approach is to reference a PDF directly from a URL:

cURLCLIPythonTypeScriptJava

```
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "url",
                        "url": "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf",
                    },
                },
                {"type": "text", "text": "What are the key findings in this document?"},
            ],
        }
    ],
)

print(message.content)
```

# Option 2: Base64-encoded PDF document

If you need to send PDFs from your local system or when a URL isn't available:

cURLCLIPythonTypeScriptJava

```
import base64
import httpx

# First, load and encode the PDF
pdf_url = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
pdf_data = base64.standard_b64encode(httpx.get(pdf_url).content).decode("utf-8")

# Alternative: Load from a local file
# with open("document.pdf", "rb") as f:
#     pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

# Send to Claude using base64 encoding
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data,
                    },
                },
                {"type": "text", "text": "What are the key findings in this document?"},
            ],
        }
    ],
)

print(message.content)
```

# Option 3: Files API

For PDFs you'll use repeatedly, or when you want to avoid encoding overhead, use the [Files API](/docs/en/build-with-claude/files):

cURLCLIPythonTypeScriptJava

```
client = anthropic.Anthropic()

# Upload the PDF file
with open("document.pdf", "rb") as f:
    file_upload = client.beta.files.upload(file=("document.pdf", f, "application/pdf"))

# Use the uploaded file in a message
message = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    betas=["files-api-2025-04-14"],
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {"type": "file", "file_id": file_upload.id},
                },
                {"type": "text", "text": "What are the key findings in this document?"},
            ],
        }
    ],
)

print(message.content)
```

# How PDF support works

When you send a PDF to Claude, the following steps occur:

1. 1

   The system extracts the contents of the document.

   * The system converts each page of the document into an image.
   * The text from each page is extracted and provided alongside each page's image.
2. 2

   Claude analyzes both the text and images to better understand the document.

   * Documents are provided as a combination of text and images for analysis.
   * This allows users to ask for insights on visual elements of a PDF, such as charts, diagrams, and other non-textual content.
3. 3

   Claude responds, referencing the PDF's contents if relevant.

   Claude can reference both textual and visual content when it responds. You can further improve performance by integrating PDF support with:

   * **Prompt caching**: To improve performance for repeated analysis.
   * **Batch processing**: For high-volume document processing.
   * **Tool use**: To extract specific information from documents for use as tool inputs.

# Estimate your costs

The token count of a PDF file depends on the total text extracted from the document as well as the number of pages:

* Text token costs: Each page typically uses 1,500-3,000 tokens per page depending on content density. Standard API pricing applies with no additional PDF fees.
* Image token costs: Since each page is converted into an image, the same [image-based cost calculations](/docs/en/build-with-claude/vision#evaluate-image-size) are applied.

You can use [token counting](/docs/en/build-with-claude/token-counting) to estimate costs for your specific PDFs.

---

# Optimize PDF processing

# Improve performance

Follow these best practices for optimal results:

* Place PDFs before text in your requests
* Use standard fonts
* Ensure text is clear and legible
* Rotate pages to proper upright orientation
* Use logical page numbers (from PDF viewer) in prompts
* Split large PDFs into chunks when needed
* Enable prompt caching for repeated analysis

# Scale your implementation

For high-volume processing, consider these approaches:

# Use prompt caching

Cache PDFs to improve performance on repeated queries:

cURLCLIPythonTypeScriptJava

```
client = anthropic.Anthropic()
# ...
message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data,
                    },
                    "cache_control": {"type": "ephemeral"},
                },
                {"type": "text", "text": "Analyze this document."},
            ],
        }
    ],
)
```

# Process document batches

Use the Message Batches API for high-volume workflows:

cURLCLIPythonTypeScriptJava

```
client = anthropic.Anthropic()
# ...
message_batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": "doc1",
            "params": {
                "model": "claude-opus-4-7",
                "max_tokens": 1024,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "document",
                                "source": {
                                    "type": "base64",
                                    "media_type": "application/pdf",
                                    "data": pdf_data,
                                },
                            },
                            {"type": "text", "text": "Summarize this document."},
                        ],
                    }
                ],
            },
        }
    ]
)
```

# Next steps

[Try PDF examples

Explore practical examples of PDF processing in the cookbook recipe.](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision)[View API reference

See complete API documentation for PDF support.](/docs/en/api/messages/create)

Was this page helpful?
