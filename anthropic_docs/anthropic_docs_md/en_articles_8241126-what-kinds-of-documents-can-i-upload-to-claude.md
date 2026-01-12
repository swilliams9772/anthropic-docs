# What kinds of documents can I upload to Claude?

**Source:** https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude

Claude can work with various types of documents within chats and [project knowledge bases](https://support.anthropic.com/en/articles/9517075-what-are-projects) to help you analyze and understand their contents.

We currently support the following document types:

* PDF
* DOCX
* CSV
* TXT
* HTML
* ODT
* RTF
* EPUB
* JSON
* XLSX\*

**Note:** You must enable either the [analysis tool](https://support.anthropic.com/en/articles/10008684-enabling-and-using-the-analysis-tool) or [Upgraded file creation and analysis](https://support.anthropic.com/en/articles/12111783-create-and-edit-files-with-claude) in your account to upload XLSX documents.

# File Limits

# Chat uploads

* File size: 30MB per file
* Number of files: Up to 20 files per chat

# Project knowledge bases

* File size: 30MB per file
* Number of files: Unlimited, but total content must fit within Claude's context window.
* Text extraction only, except for multimodal PDFs

**Note:**Additional token limits apply to these limits based on the length of the extracted content.

# PDF Processing

# Visual analysis

Claude 4 models, Claude 3.7 Sonnet, and Claude 3.5 Sonnet can analyze both text and visual elements (like images, charts, and graphics) in PDFs that are under 100 pages and uploaded to chats or projects.

# Text-only analysis

Claude will only process the text (not images) from PDFs when:

* The PDF is over 100 pages
* You aren't using Claude 4 models

# Important Notes

* When referring to specific pages of a PDF, use the PDF page numbers as shown in your PDF viewer, not the page numbers printed on the document itself.
* For non-PDF documents, Claude will only extract text. If these files contain images, Claude won't be able to read or interpret them.
* If you're working with larger documents, we recommend dividing your file into smaller sections to stay within these limits.

---

Related Articles

[Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)[Claude for Financial Services Overview](https://support.claude.com/en/articles/12219959-claude-for-financial-services-overview)[Create professional results across tools with Claude Sonnet 4.5](https://support.claude.com/en/articles/12439380-create-professional-results-across-tools-with-claude-sonnet-4-5)[Claude in Excel](https://support.claude.com/en/articles/12650343-claude-in-excel)[Using Egnyte for data room management with Claude](https://support.claude.com/en/articles/12651659-using-egnyte-for-data-room-management-with-claude)
