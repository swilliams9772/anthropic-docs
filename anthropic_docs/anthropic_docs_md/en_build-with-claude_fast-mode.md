# Fast mode (beta: research preview)

**Source:** http://platform.claude.com/docs/en/build-with-claude/fast-mode

Copy page

Fast mode provides significantly faster output token generation for Claude Opus 4.6 and Claude Opus 4.7. By setting `speed: "fast"` in your API request, you get up to 2.5x higher output tokens per second from the same model at premium pricing.

Fast mode is in beta (research preview). [Join the waitlist](https://claude.com/fast-mode) to request access. Availability is limited while Anthropic gathers feedback.

This feature is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

# Supported models

Fast mode is supported on the following models:

* Claude Opus 4.7 (`claude-opus-4-7`)
* Claude Opus 4.6 (`claude-opus-4-6`)

# How fast mode works

Fast mode runs the same model with a faster inference configuration. There is no change to intelligence or capabilities.

* Up to 2.5x higher output tokens per second compared to standard speed
* Speed benefits are focused on output tokens per second (OTPS), not time to first token (TTFT)
* Same model weights and behavior (not a different model)

# Basic usage

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[
        {"role": "user", "content": "Refactor this module to use dependency injection"}
    ],
)

print(response.content[0].text)
```

# Pricing

Fast mode is priced at 6x standard Opus rates across the full context window, including requests over 200k input tokens. The following table shows pricing for Claude Opus 4.6 and Claude Opus 4.7 with fast mode:

| Input | Output |
| --- | --- |
| $30 / MTok | $150 / MTok |

Fast mode pricing stacks with other pricing modifiers:

* [Prompt caching multipliers](/docs/en/about-claude/pricing#prompt-caching) apply on top of fast mode pricing
* [Data residency](/docs/en/manage-claude/data-residency) multipliers apply on top of fast mode pricing

For complete pricing details, see the [pricing page](/docs/en/about-claude/pricing#fast-mode-pricing).

# Rate limits

Fast mode has a dedicated rate limit that is separate from standard Opus rate limits. When your fast mode rate limit is exceeded, the API returns a `429` error with a `retry-after` header indicating when capacity will be available.

The response includes headers that indicate your fast mode rate limit status:

| Header | Description |
| --- | --- |
| `anthropic-fast-input-tokens-limit` | Maximum fast mode input tokens per minute |
| `anthropic-fast-input-tokens-remaining` | Remaining fast mode input tokens |
| `anthropic-fast-input-tokens-reset` | Time when the fast mode input token limit resets |
| `anthropic-fast-output-tokens-limit` | Maximum fast mode output tokens per minute |
| `anthropic-fast-output-tokens-remaining` | Remaining fast mode output tokens |
| `anthropic-fast-output-tokens-reset` | Time when the fast mode output token limit resets |

For tier-specific rate limits, see the [rate limits page](/docs/en/api/rate-limits).

# Checking which speed was used

The response `usage` object includes a `speed` field that indicates which speed was used, either `"fast"` or `"standard"`:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.usage.speed)  # "fast" or "standard"
```

Output

```
{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
// ...
  "usage": {
    "input_tokens": 8,
    "output_tokens": 12,
    "speed": "fast"
  }
}
```

To track fast mode usage and costs across your organization, see the [Usage and Cost API](/docs/en/manage-claude/usage-cost-api).

# Retries and fallback

# Automatic retries

When fast mode rate limits are exceeded, the API returns a `429` error with a `retry-after` header. The Anthropic SDKs automatically retry these requests up to 2 times by default (configurable via `max_retries`), waiting for the server-specified delay before each retry. Since fast mode uses continuous token replenishment, the `retry-after` delay is typically short and requests succeed once capacity is available.

# Falling back to standard speed

If you'd prefer to fall back to standard speed rather than wait for fast mode capacity, catch the rate limit error and retry without `speed: "fast"`. Set `max_retries` to `0` on the initial fast request to skip automatic retries and fail immediately on rate limit errors.

Falling back from fast to standard speed will result in a [prompt cache](/docs/en/build-with-claude/prompt-caching) miss. Requests at different speeds do not share cached prefixes.

Since setting `max_retries` to `0` also disables retries for other transient errors (overloaded, internal server errors), the examples below re-issue the original request with default retries for those cases.

CLIPythonTypeScriptC#GoJavaPHPRuby

```
client = anthropic.Anthropic()

def create_message_with_fast_fallback(max_retries=None, max_attempts=3, **params):
    try:
        return client.beta.messages.create(**params, max_retries=max_retries)
    except anthropic.RateLimitError:
        if params.get("speed") == "fast":
            del params["speed"]
            return create_message_with_fast_fallback(**params)
        raise
    except (
        anthropic.APIStatusError,
        anthropic.APIConnectionError,
    ) as error:
        if isinstance(error, anthropic.APIStatusError) and error.status_code < 500:
            raise
        if max_attempts > 1:
            return create_message_with_fast_fallback(
                max_attempts=max_attempts - 1, **params
            )
        raise

message = create_message_with_fast_fallback(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    betas=["fast-mode-2026-02-01"],
    speed="fast",
    max_retries=0,
)
```

# Considerations

* **Prompt caching:** Switching between fast and standard speed invalidates the prompt cache. Requests at different speeds do not share cached prefixes.
* **Supported models:** Fast mode is supported on Claude Opus 4.6 and Claude Opus 4.7. Sending `speed: "fast"` with an unsupported model returns an error.
* **TTFT:** Fast mode's benefits are focused on output tokens per second (OTPS), not time to first token (TTFT).
* **Batch API:** Fast mode is not available with the [Batch API](/docs/en/build-with-claude/batch-processing).
* **Priority Tier:** Fast mode is not available with [Priority Tier](/docs/en/api/service-tiers).
* **Claude Platform on AWS:** Fast mode is not currently available on [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws).

# Next steps

[Pricing

View detailed fast mode pricing information.](/docs/en/about-claude/pricing#fast-mode-pricing)[Rate limits

Check rate limit tiers for fast mode.](/docs/en/api/rate-limits)[Effort parameter

Control token usage with the effort parameter.](/docs/en/build-with-claude/effort)

Was this page helpful?
