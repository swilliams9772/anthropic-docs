# LLM gateway configuration - Anthropic

**Source:** https://docs.anthropic.com/en/docs/claude-code/llm-gateway

LLM gateways provide a centralized proxy layer between Claude Code and model providers, offering:

* **Centralized authentication** - Single point for API key management
* **Usage tracking** - Monitor usage across teams and projects
* **Cost controls** - Implement budgets and rate limits
* **Audit logging** - Track all model interactions for compliance
* **Model routing** - Switch between providers without code changes

# [​](#litellm-configuration) LiteLLM configuration

LiteLLM is a third-party proxy service. Anthropic doesn’t endorse, maintain, or audit LiteLLM’s security or functionality. This guide is provided for informational purposes and may become outdated. Use at your own discretion.

# [​](#prerequisites) Prerequisites

* Claude Code updated to the latest version
* LiteLLM Proxy Server deployed and accessible
* Access to Claude models through your chosen provider

# [​](#basic-litellm-setup) Basic LiteLLM setup

**Configure Claude Code**:

# [​](#authentication-methods) Authentication methods

# Static API key

Simplest method using a fixed API key:

```
# Set in environment

export ANTHROPIC_AUTH_TOKEN=sk-litellm-static-key

# Or in Claude Code settings

{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-litellm-static-key"
  }
}

```

This value will be sent as the `Authorization` header.

# Dynamic API key with helper

For rotating keys or per-user authentication:

```
#!/bin/bash
# ~/bin/get-litellm-key.sh

# Example: Fetch key from vault

vault kv get -field=api_key secret/litellm/claude-code

# Example: Generate JWT token

jwt encode \
  --secret="${JWT_SECRET}" \
  --exp="+1h" \
  '{"user":"'${USER}'","team":"engineering"}'

```

2. Configure Claude Code settings to use the helper:

3. Set token refresh interval:

This value will be sent as `Authorization` and `X-Api-Key` headers. The `apiKeyHelper` has lower precedence than `ANTHROPIC_AUTH_TOKEN` or `ANTHROPIC_API_KEY`.

# [​](#unified-endpoint-recommended) Unified endpoint (recommended)

Using LiteLLM’s [Anthropic format endpoint](https://docs.litellm.ai/docs/anthropic_unified):

```
export ANTHROPIC_BASE_URL=https://litellm-server:4000

```

**Benefits of the unified endpoint over pass-through endpoints:**

* Load balancing
* Fallbacks
* Consistent support for cost tracking and end-user tracking

# [​](#provider-specific-pass-through-endpoints-alternative) Provider-specific pass-through endpoints (alternative)

# Anthropic API through LiteLLM

Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/anthropic_completion):

```
export ANTHROPIC_BASE_URL=https://litellm-server:4000/anthropic

```

# Amazon Bedrock through LiteLLM

Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/bedrock):

```
export ANTHROPIC_BEDROCK_BASE_URL=https://litellm-server:4000/bedrock
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
export CLAUDE_CODE_USE_BEDROCK=1

```

# Google Vertex AI through LiteLLM

Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/vertex_ai):

```
export ANTHROPIC_VERTEX_BASE_URL=https://litellm-server:4000/vertex_ai/v1
export ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5

```

# [​](#model-selection) Model selection

By default, the models will use those specified in [Model configuration](/en/docs/claude-code/bedrock-vertex-proxies#model-configuration).

If you have configured custom model names in LiteLLM, set the aforementioned environment variables to those custom names.

For more detailed information, refer to the [LiteLLM documentation](https://docs.litellm.ai/).

# [​](#additional-resources) Additional resources

* [LiteLLM documentation](https://docs.litellm.ai/)
* [Claude Code settings](/en/docs/claude-code/settings)
* [Corporate proxy setup](/en/docs/claude-code/corporate-proxy)
* [Third-party integrations overview](/en/docs/claude-code/third-party-integrations)
