# Polyglot superpowers - Anthropic

**Source:** https://docs.anthropic.com/en/resources/prompt-library/polyglot-superpowers

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Content |
| --- |
| System | You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version. |
| User | Das Wetter heute ist wunderschön, lass uns spazieren gehen. —> Italienisch |

# [​](#example-output) Example output

> Il tempo oggi è bellissimo, andiamo a fare una passeggiata

# [​](#api-request) API request

Python

TypeScript

AWS Bedrock Python

AWS Bedrock TypeScript

Vertex AI Python

Vertex AI

```
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-1-20250805",
    max_tokens=2000,
    temperature=0.2,
    system="You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Das Wetter heute ist wunderschön, lass uns spazieren gehen. --> Italienisch"
                }
            ]
        }
    ]
)
print(message.content)

```
