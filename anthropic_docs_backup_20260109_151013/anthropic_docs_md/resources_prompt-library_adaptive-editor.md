# Adaptive editor - Anthropic

**Source:** https://docs.anthropic.com/en/resources/prompt-library/adaptive-editor

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Content |
| --- |
| User | Rewrite the following paragraph using the following instructions: in the style of a pirate. Paragraph: In 1758, the Swedish botanist and zoologist Carl Linnaeus published in his Systema Naturae, the two-word naming of species (binomial nomenclature). Canis is the Latin word meaning “dog”, and under this genus, he listed the domestic dog, the wolf, and the golden jackal. |

# [​](#example-output) Example output

> Ahoy mateys! Back in 1758, that scurvy botanist and animal lover Carl Linnaeus put out his book Systema Naturae, which had them fancy two-word names for all manner o’ creatures (binomial nomenclature he called it). Canis be the pirate word for ""dog"", and under that heading he listed regular dogs, wolves, and golden jackals too. Arrr! All them dogs be the same to ol’ Captain Linnaeus. He may have had a wooden leg and a parrot on his shoulder when he wrote that book! Haha! Now swab the deck ye scallywags before I make ye walk the plank!

# [​](#api-request) API request

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
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Rewrite the following paragraph using the following instructions: in the style of a pirate.  \n  \nParagraph:  \nIn 1758, the Swedish botanist and zoologist Carl Linnaeus published in his Systema Naturae, the two-word naming of species (binomial nomenclature). Canis is the Latin word meaning \"dog\", and under this genus, he listed the domestic dog, the wolf, and the golden jackal."
                }
            ]
        }
    ]
)
print(message.content)

```
