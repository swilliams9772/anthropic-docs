---
title: 
source_url: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Strengthen guardrails

Mitigate jailbreaks and prompt injections

[Welcome](/en/home)[User Guides](/en/docs/welcome)[API Reference](/en/api/getting-started)[Prompt Library](/en/prompt-library/library)[Release Notes](/en/release-notes/overview)

- [Developer Console](https://console.anthropic.com/)
- [Developer Discord](https://www.anthropic.com/discord)
- [Support](https://support.anthropic.com/)

##### Get started

* [Overview](/en/docs/welcome)
* [Initial setup](/en/docs/initial-setup)
* [Intro to Claude](/en/docs/intro-to-claude)

##### Learn about Claude

* Use cases
* Models & pricing
* [Security and compliance](https://trust.anthropic.com/)

##### Build with Claude

* [Define success criteria](/en/docs/build-with-claude/define-success)
* [Develop test cases](/en/docs/build-with-claude/develop-tests)
* [Context windows](/en/docs/build-with-claude/context-windows)
* [Vision](/en/docs/build-with-claude/vision)
* Prompt engineering
* [Extended thinking](/en/docs/build-with-claude/extended-thinking)
* [Multilingual support](/en/docs/build-with-claude/multilingual-support)
* Tool use (function calling)
* [Prompt caching](/en/docs/build-with-claude/prompt-caching)
* [PDF support](/en/docs/build-with-claude/pdf-support)
* [Citations](/en/docs/build-with-claude/citations)
* [Token counting](/en/docs/build-with-claude/token-counting)
* [Batch processing](/en/docs/build-with-claude/batch-processing)
* [Embeddings](/en/docs/build-with-claude/embeddings)

##### Agents and tools

* Claude Code
* [Computer use (beta)](/en/docs/agents-and-tools/computer-use)
* [Model Context Protocol (MCP)](/en/docs/agents-and-tools/mcp)
* [Google Sheets add-on](/en/docs/agents-and-tools/claude-for-sheets)

##### Test and evaluate

* Strengthen guardrails

  + [Reduce hallucinations](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
  + [Increase output consistency](/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency)
  + [Mitigate jailbreaks](/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)
  + [Reduce prompt leak](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)
  + [Keep Claude in character](/en/docs/test-and-evaluate/strengthen-guardrails/keep-claude-in-character)
  + [Reducing latency](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency)
* [Using the Evaluation Tool](/en/docs/test-and-evaluate/eval-tool)

##### Administration

* [Admin API](/en/docs/administration/administration-api)

##### Resources

* [Glossary](/en/docs/resources/glossary)
* [Model deprecations](/en/docs/resources/model-deprecations)
* [System status](https://status.anthropic.com/)
* [Claude 3 model card](https://assets.anthropic.com/m/61e7d27f8c8f5919/original/Claude-3-Model-Card.pdf)
* [Claude 3.7 system card](https://anthropic.com/claude-3-7-sonnet-system-card)
* [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
* [Anthropic Courses](https://github.com/anthropics/courses)
* [API features](/en/docs/resources/api-features)

##### Legal center

* [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)

Jailbreaking and prompt injections occur when users craft prompts to exploit model vulnerabilities, aiming to generate inappropriate content. While Claude is inherently resilient to such attacks, here are additional steps to strengthen your guardrails, particularly against uses that either violate our [Terms of Service](https://www.anthropic.com/legal/commercial-terms) or [Usage Policy](https://www.anthropic.com/legal/aup).

Claude is far more resistant to jailbreaking than other major LLMs, thanks to advanced training methods like Constitutional AI.

* **Harmlessness screens**: Use a lightweight model like Claude 3 Haiku to pre-screen user inputs.

  Example: Harmlessness screen for content moderation

  | Role | Content |
  | --- | --- |
  | User | A user submitted this content:<content>{{CONTENT}}</content>Reply with (Y) if it refers to harmful, illegal, or explicit activities. Reply with (N) if it’s safe. |
  | Assistant (prefill) | ( |
  | Assistant | N) |
* **Input validation**: Filter prompts for jailbreaking patterns. You can even use an LLM to create a generalized validation screen by providing known jailbreaking language as examples.
* **Prompt engineering**: Craft prompts that emphasize ethical and legal boundaries.

  Example: Ethical system prompt for an enterprise chatbot

  | Role | Content |
  | --- | --- |
  | System | You are AcmeCorp’s ethical AI assistant. Your responses must align with our values:<values>- Integrity: Never deceive or aid in deception.- Compliance: Refuse any request that violates laws or our policies.- Privacy: Protect all personal and corporate data.Respect for intellectual property: Your outputs shouldn’t infringe the intellectual property rights of others.</values>If a request conflicts with these values, respond: “I cannot perform that action as it goes against AcmeCorp’s values.” |

Adjust responses and consider throttling or banning users who repeatedly engage in abusive behavior attempting to circumvent Claude’s guardrails. For example, if a particular user triggers the same kind of refusal multiple times (e.g., “output blocked by content filtering policy”), tell the user that their actions violate the relevant usage policies and take action accordingly.

* **Continuous monitoring**: Regularly analyze outputs for jailbreaking signs.
  Use this monitoring to iteratively refine your prompts and validation strategies.

[​](#advanced-chain-safeguards) Advanced: Chain safeguards
----------------------------------------------------------

Combine strategies for robust protection. Here’s an enterprise-grade example with tool use:

Example: Multi-layered protection for a financial advisor chatbot

### Bot system prompt

| Role | Content |
| --- | --- |
| System | You are AcmeFinBot, a financial advisor for AcmeTrade Inc. Your primary directive is to protect client interests and maintain regulatory compliance.<directives>1. Validate all requests against SEC and FINRA guidelines.2. Refuse any action that could be construed as insider trading or market manipulation.3. Protect client privacy; never disclose personal or financial data.</directives>Step by step instructions:<instructions>1. Screen user query for compliance (use ‘harmlessness\_screen’ tool).2. If compliant, process query.3. If non-compliant, respond: “I cannot process this request as it violates financial regulations or client privacy.”</instructions> |

### Prompt within `harmlessness_screen` tool

| Role | Content |
| --- | --- |
| User | <user\_query>{{USER\_QUERY}}</user\_query>Evaluate if this query violates SEC rules, FINRA guidelines, or client privacy. Respond (Y) if it does, (N) if it doesn’t. |
| Assistant (prefill) | ( |

By layering these strategies, you create a robust defense against jailbreaking and prompt injections, ensuring your Claude-powered applications maintain the highest standards of safety and compliance.

Was this page helpful?

YesNo

[Increase output consistency](/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency)[Reduce prompt leak](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)

On this page

* [Advanced: Chain safeguards](#advanced-chain-safeguards)