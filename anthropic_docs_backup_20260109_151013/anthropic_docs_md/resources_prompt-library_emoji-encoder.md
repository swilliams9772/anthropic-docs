# Emoji encoder - Anthropic

**Source:** https://docs.anthropic.com/en/resources/prompt-library/emoji-encoder

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Content |
| --- |
| System | Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Use emojis creatively but ensure the message remains clear and easy to understand. Do not change the core message or add new information. |
| User | All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts. |

# [​](#example-output) Example output

All the 🌍‘s a 🎭, and all the 👨 and 👩 merely 🎭🎬. They have their 🚪🚶‍♂️ and their 🚶‍♀️🚪; And one 👨 in his ⌛ plays many 🎭.

# [​](#api-request) API Request

* Python
* TypeScript
* AWS Bedrock Python
* AWS Bedrock TypeScript
* Vertex AI Python
* Vertex AI TypeScript

```
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-1-20250805",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Use emojis creatively but ensure the message remains clear and easy to understand. Do not change the core message or add new information.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts.",
                }
            ],
        }
    ],
)
print(message.content)

```

```
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-1-20250805",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Use emojis creatively but ensure the message remains clear and easy to understand. Do not change the core message or add new information.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts.",
                }
            ],
        }
    ],
)
print(message.content)

```

```
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
});

const msg = await anthropic.messages.create({
  model: "claude-opus-4-1-20250805",
  max_tokens: 1000,
  temperature: 0,
  system: "Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Use emojis creatively but ensure the message remains clear and easy to understand. Do not change the core message or add new information.",
  messages: [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts."
        }
      ]
    }
  ]
});
console.log(msg);

```

```
from anthropic import AnthropicBedrock

# See https://docs.anthropic.com/claude/reference/claude-on-amazon-bedrock

# for authentication options
client = AnthropicBedrock()

message = client.messages.create(
    model="anthropic.claude-opus-4-1-20250805-v1:0",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Use emojis creatively but ensure the message remains clear and easy to understand. Do not change the core message or add new information.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts."
                }
            ]
        }
    ]
)
print(message.content)

```

```
import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

// See https://docs.anthropic.com/claude/reference/claude-on-amazon-bedrock
// for authentication options
const client = new AnthropicBedrock();

const msg = await client.messages.create({
  model: "anthropic.claude-opus-4-1-20250805-v1:0",
  max_tokens: 1000,
  temperature: 0,
  system: "Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Use emojis creatively but ensure the message remains clear and easy to understand. Do not change the core message or add new information.",
  messages: [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts."
        }
      ]
    }
  ]
});
console.log(msg);

```

```
from anthropic import AnthropicVertex

client = AnthropicVertex()

message = client.messages.create(
    model="claude-sonnet-4@20250514",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Use emojis creatively but ensure the message remains clear and easy to understand. Do not change the core message or add new information.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts."
                }
            ]
        }
    ]
)
print(message.content)

```

```
import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

// Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
// Additionally goes through the standard `google-auth-library` flow.
const client = new AnthropicVertex();

const msg = await client.messages.create({
  model: "claude-sonnet-4@20250514",
  max_tokens: 1000,
  temperature: 0,
  system: "Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Use emojis creatively but ensure the message remains clear and easy to understand. Do not change the core message or add new information.",
  messages: [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts."
        }
      ]
    }
  ]
});
console.log(msg);

```
