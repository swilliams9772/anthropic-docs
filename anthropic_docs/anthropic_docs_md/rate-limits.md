---
title: 
source_url: https://docs.anthropic.com/en/api/rate-limits/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Using the API

Rate limits

[Welcome](/en/home)[User Guides](/en/docs/welcome)[API Reference](/en/api/getting-started)[Prompt Library](/en/prompt-library/library)[Release Notes](/en/release-notes/overview)

- [Developer Console](https://console.anthropic.com/)
- [Developer Discord](https://www.anthropic.com/discord)
- [Support](https://support.anthropic.com/)

##### Using the API

* [Getting started](/en/api/getting-started)
* [IP addresses](/en/api/ip-addresses)
* [Versions](/en/api/versioning)
* [Errors](/en/api/errors)
* [Rate limits](/en/api/rate-limits)
* [Client SDKs](/en/api/client-sdks)
* [Supported regions](/en/api/supported-regions)
* [Getting help](/en/api/getting-help)

##### Anthropic APIs

* Messages
* Models
* Message Batches
* Text Completions (Legacy)
* Admin API

##### OpenAI SDK compatibility

* [OpenAI SDK compatibility (beta)](/en/api/openai-sdk)

##### Experimental APIs

* Prompt tools

##### Amazon Bedrock API

* [Amazon Bedrock API](/en/api/claude-on-amazon-bedrock)

##### Vertex AI

* [Vertex AI API](/en/api/claude-on-vertex-ai)

We have two types of limits:

1. **Spend limits** set a maximum monthly cost an organization can incur for API usage.
2. **Rate limits** set the maximum number of API requests an organization can make over a defined period of time.

We enforce service-configured limits at the organization level, but you may also set user-configurable limits for your organization’s workspaces.

[​](#about-our-limits) About our limits
---------------------------------------

* Limits are designed to prevent API abuse, while minimizing impact on common customer usage patterns.
* Limits are defined by usage tier, where each tier is associated with a different set of spend and rate limits.
* Your organization will increase tiers automatically as you reach certain thresholds while using the API.
  Limits are set at the organization level. You can see your organization’s limits in the [Limits page](https://console.anthropic.com/settings/limits) in the [Anthropic Console](https://console.anthropic.com/).
* You may hit rate limits over shorter time intervals. For instance, a rate of 60 requests per minute (RPM) may be enforced as 1 request per second. Short bursts of requests at a high volume can surpass the rate limit and result in rate limit errors.
* The limits outlined below are our standard limits. If you’re seeking higher, custom limits, contact sales through the [Anthropic Console](https://console.anthropic.com/settings/limits).
* We use the [token bucket algorithm](https://en.wikipedia.org/wiki/Token_bucket) to do rate limiting. This means that your capacity is continuously replenished up to your maximum limit, rather than being reset at fixed intervals.
* All limits described here represent maximum allowed usage, not guaranteed minimums. These limits are intended to reduce unintentional overspend and ensure fair distribution of resources among users.

[​](#spend-limits) Spend limits
-------------------------------

Each usage tier has a limit on how much you can spend on the API each calendar month. Once you reach the spend limit of your tier, until you qualify for the next tier, you will have to wait until the next month to be able to use the API again.

To qualify for the next tier, you must meet a deposit requirement. To minimize the risk of overfunding your account, you cannot deposit more than your monthly spend limit.

### [​](#requirements-to-advance-tier) Requirements to advance tier

| Usage Tier | Credit Purchase | Max Usage per Month |
| --- | --- | --- |
| Tier 1 | $5 | $100 |
| Tier 2 | $40 | $500 |
| Tier 3 | $200 | $1,000 |
| Tier 4 | $400 | $5,000 |
| Monthly Invoicing | N/A | N/A |

[​](#rate-limits) Rate limits
-----------------------------

Our rate limits for the Messages API are measured in requests per minute (RPM), input tokens per minute (ITPM), and output tokens per minute (OTPM) for each model class.
If you exceed any of the rate limits you will get a [429 error](/en/api/errors) describing which rate limit was exceeded, along with a `retry-after` header indicating how long to wait.

ITPM rate limits are estimated at the beginning of each request, and the estimate is adjusted during the request to reflect the actual number of input tokens used.
The final adjustment counts [`input_tokens`](/en/api/messages#response-usage-input-tokens) and [`cache_creation_input_tokens`](/en/api/messages#response-usage-cache-creation-input-tokens) towards ITPM rate limits, while [`cache_read_input_tokens`](/en/api/messages#response-usage-cache-read-input-tokens) are not (though they are still billed).
In some instances, [`cache_read_input_tokens`](/en/api/messages#response-usage-cache-read-input-tokens) are counted towards ITPM rate limits.

OTPM rate limits are estimated based on `max_tokens` at the beginning of each request, and the estimate is adjusted at the end of the request to reflect the actual number of output tokens used.
If you’re hitting OTPM limits earlier than expected, try reducing `max_tokens` to better approximate the size of your completions.

Rate limits are applied separately for each model; therefore you can use different models up to their respective limits simultaneously.
You can check your current rate limits and behavior in the [Anthropic Console](https://console.anthropic.com/settings/limits).

* Tier 1
* Tier 2
* Tier 3
* Tier 4
* Custom

| Model | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
| --- | --- | --- | --- |
| Claude 3.7 Sonnet | 50 | 20,000 | 8,000 |
| Claude 3.5 Sonnet 2024-10-22 | 50 | 40,000\* | 8,000 |
| Claude 3.5 Sonnet 2024-06-20 | 50 | 40,000\* | 8,000 |
| Claude 3.5 Haiku | 50 | 50,000\* | 10,000 |
| Claude 3 Opus | 50 | 20,000\* | 4,000 |
| Claude 3 Sonnet | 50 | 40,000\* | 8,000 |
| Claude 3 Haiku | 50 | 50,000\* | 10,000 |

Limits marked with asterisks (\*) count [`cache_read_input_tokens`](/en/api/messages#response-usage-cache-read-input-tokens) towards ITPM usage.

### [​](#message-batches-api) Message Batches API

The Message Batches API has its own set of rate limits which are shared across all models. These include a requests per minute (RPM) limit to all API endpoints and a limit on the number of batch requests that can be in the processing queue at the same time. A “batch request” here refers to part of a Message Batch. You may create a Message Batch containing thousands of batch requests, each of which count towards this limit. A batch request is considered part of the processing queue when it has yet to be successfully processed by the model.

* Tier 1
* Tier 2
* Tier 3
* Tier 4
* Custom

| Maximum requests per minute (RPM) | Maximum batch requests in processing queue | Maximum batch requests per batch |
| --- | --- | --- |
| 50 | 100,000 | 100,000 |

[​](#setting-lower-limits-for-workspaces) Setting lower limits for Workspaces
-----------------------------------------------------------------------------

In order to protect Workspaces in your Organization from potential overuse, you can set custom spend and rate limits per Workspace.

Example: If your Organization’s limit is 40,000 input tokens per minute and 8,000 output tokens per minute, you might limit one Workspace to 30,000 total tokens per minute. This protects other Workspaces from potential overuse and ensures a more equitable distribution of resources across your Organization. The remaining unused tokens per minute (or more, if that Workspace doesn’t use the limit) are then available for other Workspaces to use.

Note:

* You can’t set limits on the default Workspace.
* If not set, Workspace limits match the Organization’s limit.
* Organization-wide limits always apply, even if Workspace limits add up to more.
* Support for input and output token limits will be added to Workspaces in the future.

[​](#response-headers) Response headers
---------------------------------------

The API response includes headers that show you the rate limit enforced, current usage, and when the limit will be reset.

The following headers are returned:

| Header | Description |
| --- | --- |
| `retry-after` | The number of seconds to wait until you can retry the request. Earlier retries will fail. |
| `anthropic-ratelimit-requests-limit` | The maximum number of requests allowed within any rate limit period. |
| `anthropic-ratelimit-requests-remaining` | The number of requests remaining before being rate limited. |
| `anthropic-ratelimit-requests-reset` | The time when the request rate limit will be fully replenished, provided in RFC 3339 format. |
| `anthropic-ratelimit-tokens-limit` | The maximum number of tokens allowed within any rate limit period. |
| `anthropic-ratelimit-tokens-remaining` | The number of tokens remaining (rounded to the nearest thousand) before being rate limited. |
| `anthropic-ratelimit-tokens-reset` | The time when the token rate limit will be fully replenished, provided in RFC 3339 format. |
| `anthropic-ratelimit-input-tokens-limit` | The maximum number of input tokens allowed within any rate limit period. |
| `anthropic-ratelimit-input-tokens-remaining` | The number of input tokens remaining (rounded to the nearest thousand) before being rate limited. |
| `anthropic-ratelimit-input-tokens-reset` | The time when the input token rate limit will be fully replenished, provided in RFC 3339 format. |
| `anthropic-ratelimit-output-tokens-limit` | The maximum number of output tokens allowed within any rate limit period. |
| `anthropic-ratelimit-output-tokens-remaining` | The number of output tokens remaining (rounded to the nearest thousand) before being rate limited. |
| `anthropic-ratelimit-output-tokens-reset` | The time when the output token rate limit will be fully replenished, provided in RFC 3339 format. |

The `anthropic-ratelimit-tokens-*` headers display the values for the most restrictive limit currently in effect. For instance, if you have exceeded the Workspace per-minute token limit, the headers will contain the Workspace per-minute token rate limit values. If Workspace limits do not apply, the headers will return the total tokens remaining, where total is the sum of input and output tokens. This approach ensures that you have visibility into the most relevant constraint on your current API usage.

Was this page helpful?

YesNo

[Errors](/en/api/errors)[Client SDKs](/en/api/client-sdks)

On this page

* [About our limits](#about-our-limits)
* [Spend limits](#spend-limits)
* [Requirements to advance tier](#requirements-to-advance-tier)
* [Rate limits](#rate-limits)
* [Message Batches API](#message-batches-api)
* [Setting lower limits for Workspaces](#setting-lower-limits-for-workspaces)
* [Response headers](#response-headers)