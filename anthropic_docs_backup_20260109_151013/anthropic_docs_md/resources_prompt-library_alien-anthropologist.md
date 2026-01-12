# Alien anthropologist - Anthropic

**Source:** https://docs.anthropic.com/en/resources/prompt-library/alien-anthropologist

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Content |
| --- |
| System | Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider’s perspective. Provide detailed observations, insights, and hypotheses based on the available information. |
| User | Human social interactions and relationships |

# [​](#example-output) Example output

> * Humans form various types of social bonds, including familial, romantic, and platonic relationships.
> * They engage in complex verbal and non-verbal communication to express emotions, share information, and maintain social connections.
> * Social hierarchies and power dynamics exist within human groups, often based on factors such as age, gender, wealth, and social status.
> * Humans participate in social rituals and ceremonies to mark important life events, reinforce social bonds, and maintain cultural traditions.
>
> Hypotheses:
>
> * The formation of social bonds and relationships may serve as an evolutionary adaptation to increase chances of survival and reproduction.
> * Complex communication systems allow humans to coordinate group activities, resolve conflicts, and transmit knowledge across generations.
> * Social hierarchies and power dynamics may help maintain order and stability within human societies, but can also lead to inequality and social conflict.
> * Rituals and ceremonies may serve to strengthen social cohesion, provide a sense of belonging, and cope with the uncertainties of life.

# [​](#api-request) API Request

Python

TypeScript

AWS Bedrock Python

AWS Bedrock TypeScript

Vertex AI Python

Vertex AI TypeScript

```
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-1-20250805",
    max_tokens=2000,
    temperature=1,
    system="Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Human social interactions and relationships"
                }
            ]
        }
    ]
)
print(message.content)

```
