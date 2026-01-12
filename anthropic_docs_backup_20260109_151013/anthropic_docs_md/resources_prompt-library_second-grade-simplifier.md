# Second-grade simplifier - Anthropic

**Source:** https://docs.anthropic.com/en/resources/prompt-library/second-grade-simplifier

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Content |
| --- |
| System | Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner. |
| User | The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur. |

# [​](#example-output) Example Output

Mitochondria are tiny parts inside cells that work like little power stations. They make a special molecule called ATP, which is like the cell’s energy money. ATP helps the cell do important jobs and keeps it running smoothly, just like how money helps people buy things they need. Mitochondria are very important because without them, cells wouldn’t have the energy to function properly.

# [​](#api-request) API Request

* Python
* TypeScript
* AWS Bedrock Python
* AWS Bedrock TypeScript
* Vertex AI Python
* Vertex AI TypeScript

```
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-opus-4-1-20250805",
  max_tokens=1000,
  temperature=0,
  system="Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
        }
      ]
    }
  ]
)
print(message.content)

```

```
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-opus-4-1-20250805",
  max_tokens=1000,
  temperature=0,
  system="Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
        }
      ]
    }
  ]
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
  system: "Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
  messages: [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
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
    system="Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
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
  system: "Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
  messages: [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
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
system="Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
messages=[
{
"role": "user",
"content": [
{
"type": "text",
"text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
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
  system: "Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
  messages: [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
        }
      ]
    }
  ]
});
console.log(msg);

```
