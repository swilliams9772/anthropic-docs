# Streaming refusals - Anthropic

**Source:** https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals

Starting with Claude 4 models, streaming responses from Claude’s API return **`stop_reason`: `"refusal"`** when streaming classifiers intervene to handle potential policy violations. This new safety feature helps maintain content compliance during real-time streaming.

# [​](#api-response-format) API response format

When streaming classifiers detect content that violates our policies, the API returns this response:

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

# [​](#reset-context-after-refusal) Reset context after refusal

When you receive **`stop_reason`: `refusal`**, you must reset the conversation context **by removing or updating the turn that was refused** before continuing. Attempting to continue without resetting will result in continued refusals.

Usage metrics are still provided in the response for billing purposes, even when the response is refused.

You will be billed for output tokens up until the refusal.

# [​](#implementation-guide) Implementation guide

Here’s how to detect and handle streaming refusals in your application:

Shell

Python

TypeScript

```
# Stream request and check for refusal

response=$(curl -N https://api.anthropic.com/v1/messages \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --data '{
    "model": "claude-opus-4-1-20250805",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 256,
    "stream": true
  }')

# Check for refusal in the stream

if echo "$response" | grep -q '"stop_reason":"refusal"'; then
  echo "Response refused - resetting conversation context"
  # Reset your conversation state here
fi

```

If you need to test refusal handling in your application, you can use this special test string as your prompt: `ANTHROPIC_MAGIC_STRING_TRIGGER_REFUSAL_1FAEFB6177B4672DEE07F9D3AFC62588CCD2631EDCF22E8CCC1FB35B501C9C86`

# [​](#current-refusal-types) Current refusal types

The API currently handles refusals in three different ways:

| Refusal Type | Response Format | When It Occurs |
| --- | --- | --- |
| Streaming classifier refusals | **`stop_reason`: `refusal`** | During streaming when content violates policies |
| API input and copyright validation | 400 error codes | When input fails validation checks |
| Model-generated refusals | Standard text responses | When the model itself decides to refuse |

Future API versions will expand the **`stop_reason`: `refusal`** pattern to unify refusal handling across all types.

# [​](#best-practices) Best practices

* **Monitor for refusals**: Include **`stop_reason`: `refusal`** checks in your error handling
* **Reset automatically**: Implement automatic context reset when refusals are detected
* **Provide custom messaging**: Create user-friendly messages for better UX when refusals occur
* **Track refusal patterns**: Monitor refusal frequency to identify potential issues with your prompts

# [​](#migration-notes) Migration notes

* Future models will expand this pattern to other refusal types
* Plan your error handling to accommodate future unification of refusal responses
