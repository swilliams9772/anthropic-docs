# Tweet tone detector

**Source:** https://platform.claude.com/docs/en/resources/prompt-library/tweet-tone-detector

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
| --- | --- |
| System | Your task is to analyze the provided tweet and identify the primary tone and sentiment expressed by the author. The tone should be classified as one of the following: Positive, Negative, Neutral, Humorous, Sarcastic, Enthusiastic, Angry, or Informative. The sentiment should be classified as Positive, Negative, or Neutral. Provide a brief explanation for your classifications, highlighting the key words, phrases, emoticons, or other elements that influenced your decision. |
| User | Wow, I'm so impressed by the company's handling of this crisis. 🙄 They really have their priorities straight. #sarcasm #fail |

# Example output

> Tone: Sarcastic
> Sentiment: Negative

# API request

Python

```
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to analyze the provided tweet and identify the primary tone and sentiment expressed by the author. The tone should be classified as one of the following: Positive, Negative, Neutral, Humorous, Sarcastic, Enthusiastic, Angry, or Informative. The sentiment should be classified as Positive, Negative, or Neutral. Provide a brief explanation for your classifications, highlighting the key words, phrases, emoticons, or other elements that influenced your decision.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Wow, I'm so impressed by the company's handling of this crisis. 🙄 They really have their priorities straight. #sarcasm #fail"
                }
            ]
        }
    ]
)
print(message.content)
```
