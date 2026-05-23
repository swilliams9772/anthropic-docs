# Vision

**Source:** http://platform.claude.com/docs/en/build-with-claude/vision

Copy page

This guide describes how to work with images in Claude, including best practices, code examples, and limitations to keep in mind.

---

# How to use vision

Use Claude's vision capabilities through:

* [claude.ai](https://claude.ai/). Upload an image like you would a file, or drag and drop an image directly into the chat window.
* The [Console Workbench](/workbench). A button to add images appears at the top right of every User message block.
* API request. See the examples in this guide.

Multiple images can be included in a single request, which Claude will analyze jointly when formulating its response. This can be helpful for comparing or contrasting images.

---

# Before you upload

# General limits

The maximal number of images per message or request is:

* 20 per message on [claude.ai](https://claude.ai/).
* 100 per request on the API, for models with a 200k-token context window.
* 600 per request on the API, for all other models.

The maximal dimensions per image are 8000x8000 px. If you submit more than 20 images in one API request, this limit is reduced to 2000x2000 px.

While the API supports up to 600 images per request, [request size limits](/docs/en/api/overview#request-size-limits) (32 MB for standard endpoints; lower on some partner-operated platforms, for example, Amazon Bedrock and Vertex AI) can be reached first. For many images, consider uploading with the [Files API](#files-api-image-example) and referencing by `file_id` to keep request payloads small.

Even when using the Files API, requests with many large images can fail before reaching the 600-image count. Reduce image dimensions or file sizes (for example, by downsampling) before uploading (see [Evaluate image size](#evaluate-image-size)).

# Evaluate image size

An image uses approximately `width * height / 750` tokens, where the width and height are expressed in pixels.

The maximal native image resolution is:

* For Claude Opus 4.7: 4784 tokens, and at most 2576 pixels on the long edge.
* For other models: 1568 tokens, and at most 1568 pixels on the long edge.

If your input image is larger than this native resolution, it will first be resized to the largest possible size while preserving the aspect ratio. Moreover, images are padded on the bottom and right corners to a multiple of 28 pixels.

When asking Claude to output coordinates (points, bounding boxes, etc.), they will be expressed with respect to the resized/padded image and will need to be rescaled/translated accordingly client-side based on the original and resized dimensions.

To minimize latency and to simplify coordinate-based workflows, you should prefer resizing images before uploading them.

# Calculate image costs

Each image you include in a request to Claude counts toward your token usage. To calculate the approximate cost, multiply the approximate number of image tokens computed as above by the [per-token price of the model](https://claude.com/pricing) you're using.

Here are examples of approximate tokenization and costs for different image sizes within the API's size constraints based on Claude Sonnet 4.6 per-token price of $3 per million input tokens:

| Image size | # of Tokens | Cost / image | Cost / 1k images |
| --- | --- | --- | --- |
| 200x200 px(0.04 megapixels) | ~54 | ~$0.00016 | ~$0.16 |
| 1000x1000 px(1 megapixel) | ~1334 | ~$0.004 | ~$4.00 |
| 1092x1092 px(1.19 megapixels) | ~1568 | ~$0.0047 | ~$4.70 |
| 1920x1080 px(2.07 megapixels) | ~1568 | ~$0.0047 | ~$4.70 |
| 2000x1500 px(3 megapixels) | ~1568 | ~$0.0047 | ~$4.70 |

Note that the last three images are downscaled before processing.

# High-resolution image support on Claude Opus 4.7

Claude Opus 4.7 is the first Claude model with high-resolution image support. The maximum image resolution is 2576 pixels on the long edge, up from 1568 px on prior models. This unlocks performance gains on vision-heavy workloads and is particularly valuable for computer use, screenshot understanding, and document analysis.

High-resolution support is automatic on Claude Opus 4.7 and requires no beta header or client-side opt-in.

High-resolution images on Claude Opus 4.7 can use up to approximately 3x more image tokens than on prior models (4784 versus 1568 tokens per image). If you don't need the additional fidelity, downsample images before sending to control token costs.

Here are the same image sizes tokenized for Claude Opus 4.7, based on its per-token price of $5 per million input tokens:

| Image size | # of Tokens | Cost / image | Cost / 1k images |
| --- | --- | --- | --- |
| 200x200 px(0.04 megapixels) | ~54 | ~$0.00027 | ~$0.27 |
| 1000x1000 px(1 megapixel) | ~1334 | ~$0.0067 | ~$6.70 |
| 1092x1092 px(1.19 megapixels) | ~1590 | ~$0.0080 | ~$8.00 |
| 1920x1080 px(2.07 megapixels) | ~2765 | ~$0.014 | ~$14.00 |
| 2000x1500 px(3 megapixels) | ~4000 | ~$0.020 | ~$20.00 |

# Ensure image quality

When providing images to Claude, keep the following in mind for best results:

* **Image format**: Use a supported image format: JPEG, PNG, GIF, or WebP.
  Animations are unsupported, and only the first frame will be used.
* **Image clarity**: Ensure images are clear and not too blurry or pixelated.
* **Text**: If the image contains important text, make sure it's legible and not too small. Avoid cropping out key visual context just to enlarge the text.
* **Resizing**: Take into account that your image might be resized if it is too large (see above); this might for example make text less legible. Consider pre-resizing your images, cropping them, or both.
* **Image compression**: Compressing images before sending them, using a lossy format such as JPEG or WebP (lossy mode), can reduce latency by reducing the size of requests. However, this can introduce artifacts that are detrimental to model performance, especially when multiple compression passes are applied. For example, heavy JPEG compression can make text difficult to read. Confirm your compression settings are appropriate for the task by inspecting the actual images sent to the API.

---

# Prompt examples

Many of the [prompting techniques](/docs/en/build-with-claude/prompt-engineering/overview) that work well for text-based interactions with Claude can also be applied to image-based prompts.

These examples demonstrate best practice prompt structures involving images.

Just as [placing long documents before your query](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#long-context-prompting) improves results in text prompts, Claude works best when images come before text. Images placed after text or interpolated with text still perform well, but if your use case allows it, prefer an image-then-text structure.

# About the prompt examples

The following examples demonstrate how to use Claude's vision capabilities using various programming languages and approaches. You can provide images to Claude in three ways:

1. As a base64-encoded image in `image` content blocks
2. As a URL reference to an image hosted online
3. Using the Files API (upload once, use multiple times)

On Amazon Bedrock and Vertex AI, only base64-encoded sources are currently available.

The base64 example prompts use these variables:

cURLPythonTypeScriptC#GoJavaPHPRuby

```
import base64
import httpx

# For base64-encoded images
image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image1_media_type = "image/jpeg"
image1_data = base64.standard_b64encode(httpx.get(image1_url).content).decode("utf-8")

image2_url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg"
image2_media_type = "image/jpeg"
image2_data = base64.standard_b64encode(httpx.get(image2_url).content).decode("utf-8")

# For URL-based images, you can use the URLs directly in your requests
```

Below are examples of how to include images in a Messages API request using base64-encoded images and URL references:

# Base64-encoded image example

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
image1_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"
image1_media_type = "image/png"

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ],
)
print(message)
```

# URL-based image example

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

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
                    "type": "image",
                    "source": {
                        "type": "url",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                    },
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ],
)
print(message)
```

# Files API image example

For images you'll use repeatedly or when you want to avoid encoding overhead, use the [Files API](/docs/en/build-with-claude/files). Upload the image once, then reference the returned `file_id` in subsequent messages instead of resending base64 data.

In multi-turn conversations and agentic workflows, each request resends the
full conversation history. If images are base64-encoded, the full image bytes
are included in the payload on every turn, which can significantly increase
request size and latency as the conversation grows. Uploading images to the
Files API and referencing them by `file_id` keeps request payloads small
regardless of how many images accumulate in the conversation history.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
client = anthropic.Anthropic()

# Upload the image file
with open("image.jpg", "rb") as f:
    file_upload = client.beta.files.upload(file=("image.jpg", f, "image/jpeg"))

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
                    "type": "image",
                    "source": {"type": "file", "file_id": file_upload.id},
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ],
)

print(message.content)
```

See [Messages API examples](/docs/en/api/messages/create) for more example code and parameter details.

# Example: One image

# Example: Multiple images

# Example: Multiple images with a system prompt

# Example: Four images across two conversation turns

---

# Limitations

While Claude's image understanding capabilities are cutting-edge, there are some limitations to be aware of:

* **People identification**: Claude [cannot be used](https://www.anthropic.com/legal/aup) to name people in images and refuses to do so.
* **Accuracy**: Claude may hallucinate or make mistakes when interpreting low-quality, rotated, or very small images under 200 pixels.
* **Spatial reasoning**: Claude's spatial reasoning abilities are limited. It may struggle with tasks requiring precise localization or layouts, like reading an analog clock face or describing exact positions of chess pieces.
* **Counting**: Claude can give approximate counts of objects in an image but may not always be precisely accurate, especially with large numbers of small objects.
* **AI generated images**: Claude does not know if an image is AI-generated and may be incorrect if asked. Do not rely on it to detect fake or synthetic images.
* **Inappropriate content**: Claude does not process inappropriate or explicit images that violate the [Acceptable Use Policy](https://www.anthropic.com/legal/aup).
* **Healthcare applications**: While Claude can analyze general medical images, it is not designed to interpret complex diagnostic scans such as CTs or MRIs. Claude's outputs should not be considered a substitute for professional medical advice or diagnosis.

Always carefully review and verify Claude's image interpretations, especially for high-stakes use cases. Do not use Claude for tasks requiring perfect precision or sensitive image analysis without human oversight.

---

# FAQ

# What image file types does Claude support?

# Can Claude read image URLs?

# Is there a limit to the image file size I can upload?

# How many images can I include in one request?

# Does Claude read image metadata?

# Can I delete images I've uploaded?

# Where can I find details on data privacy for image uploads?

# What if Claude's image interpretation seems wrong?

# Can Claude generate or edit images?

---

# Dive deeper into vision

Ready to start building with images using Claude? Here are a few helpful resources:

* [Multimodal cookbook](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision): This cookbook has tips on [getting started with images](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision) and [best practice techniques](https://platform.claude.com/cookbook/multimodal-best-practices-for-vision) to ensure the highest quality performance with images. See how you can effectively prompt Claude with images to carry out tasks such as [interpreting and analyzing charts](https://platform.claude.com/cookbook/multimodal-reading-charts-graphs-powerpoints) or [extracting content from forms](https://platform.claude.com/cookbook/multimodal-how-to-transcribe-text).
* [API reference](/docs/en/api/messages/create): Documentation for the Messages API, including example [API calls involving images](/docs/en/build-with-claude/working-with-messages#vision).

If you have any other questions, reach out to the [support team](https://support.claude.com/). You can also join the [developer community](https://www.anthropic.com/discord) to connect with other creators and get help from Anthropic experts.

Was this page helpful?
