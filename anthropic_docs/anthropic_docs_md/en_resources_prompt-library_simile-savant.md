# Simile savant

**Source:** https://platform.claude.com/docs/en/resources/prompt-library/simile-savant

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

| Role | Content |
| --- | --- |
| User | Help me create some similes to describe a person's laughter that is joyful and contagious? |

# Example Output

1. His laughter bubbled up like a freshly opened bottle of champagne, effervescent and full of life.
2. Their laughter was as warm and inviting as a cozy fireplace on a chilly evening, drawing people in to share in the merriment.

---

# API Request

Python

Python

TypeScript

TypeScript

AWS Bedrock Python

AWS Bedrock Python

AWS Bedrock TypeScript

AWS Bedrock TypeScript

Vertex AI Python

Vertex AI Python

Vertex AI TypeScript

Vertex AI TypeScript

```
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=1,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Help me create some similes to describe a person's laughter that is joyful and contagious?"
        }
      ]
    }
  ]
)
print(message.content)
```
