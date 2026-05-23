# Streaming refusals

**Source:** http://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals

Copy page

Starting with Claude 4 models, streaming responses from Claude's API return **`stop_reason`: `"refusal"`** when streaming classifiers intervene to handle potential policy violations. This new safety feature helps maintain content compliance during real-time streaming.

To learn more about refusals triggered by API safety filters for Claude Sonnet 4.5, see [Understanding Sonnet 4.5's API Safety Filters](https://support.claude.com/en/articles/12449294-understanding-sonnet-4-5-s-api-safety-filters).

# API response format

When streaming classifiers detect content that violates Anthropic's policies, the API returns this response:

```
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello.."
    }
  ],
  "stop_reason": "refusal"
}
```

No additional refusal message is included. You must handle the response and provide appropriate user-facing messaging.

# Reset context after refusal

When you receive **`stop_reason`: `refusal`**, you must reset the conversation context before continuing. You can remove or rephrase the turn that triggered the refusal, or clear the conversation history entirely. Attempting to continue without resetting will result in continued refusals.

Usage metrics are still provided in the response for billing purposes, even when the response is refused.

You will be billed for output tokens up until the refusal.

If you encounter `refusal` stop reasons frequently while using Claude Sonnet 4.5 or Opus 4.1, you can try updating your API calls to use Haiku 4.5 (`claude-haiku-4-5-20251001`), which has different usage restrictions. Learn more about [understanding Sonnet 4.5's API safety filters](https://support.claude.com/en/articles/12449294-understanding-sonnet-4-5-s-api-safety-filters).

# Implementation guide

Here's how to detect and handle streaming refusals in your application:

cURLPythonTypeScriptC#GoJavaPHPRuby

```
client = anthropic.Anthropic()
messages = []

def reset_conversation():
    """Reset conversation context after refusal"""
    global messages
    messages = []
    print("Conversation reset due to refusal")

try:
    with client.messages.stream(
        max_tokens=1024,
        messages=messages + [{"role": "user", "content": "Hello"}],
        model="claude-opus-4-7",
    ) as stream:
        for event in stream:
            # Check for refusal in message delta
            if event.type == "message_delta":
                if event.delta.stop_reason == "refusal":
                    reset_conversation()
                    break
except Exception as e:
    print(f"Error: {e}")
```

# Current refusal types

The API currently handles refusals in three different ways:

| Refusal Type | Response Format | When It Occurs |
| --- | --- | --- |
| Streaming classifier refusals | **`stop_reason`: `refusal`** | During streaming when content violates policies |
| API input and copyright validation | 400 error codes | When input fails validation checks |
| Model-generated refusals | Standard text responses | When the model itself decides to refuse |

Future API versions will expand the **`stop_reason`: `refusal`** pattern to unify refusal handling across all types.

# Best practices

* **Monitor for refusals**: Include **`stop_reason`: `refusal`** checks in your error handling
* **Reset automatically**: Implement automatic context reset when refusals are detected
* **Provide custom messaging**: Create user-friendly messages for better UX when refusals occur
* **Track refusal patterns**: Monitor refusal frequency to identify potential issues with your prompts

# Migration notes

* Future models will expand this pattern to other refusal types
* Plan your error handling to accommodate future unification of refusal responses

Was this page helpful?
