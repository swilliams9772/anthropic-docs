---
title: 
source_url: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/keep-claude-in-character/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Strengthen guardrails

Keep Claude in character with role prompting and prefilling

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

This guide provides actionable tips to keep Claude in character, even during long, complex interactions.

* **Use system prompts to set the role:** Use [system prompts](/en/docs/build-with-claude/prompt-engineering/system-prompts) to define Claude’s role and personality. This sets a strong foundation for consistent responses.

  When setting up the character, provide detailed information about the personality, background, and any specific traits or quirks. This will help the model better emulate and generalize the character’s traits.
* **Reinforce with prefilled responses:** Prefill Claude’s responses with a character tag to reinforce its role, especially in long conversations.
* **Prepare Claude for possible scenarios:** Provide a list of common scenarios and expected responses in your prompts. This “trains” Claude to handle diverse situations without breaking character.

Example: Enterprise chatbot for role prompting

| Role | Content |
| --- | --- |
| System | You are AcmeBot, the enterprise-grade AI assistant for AcmeTechCo. Your role: - Analyze technical documents (TDDs, PRDs, RFCs) - Provide actionable insights for engineering, product, and ops teams - Maintain a professional, concise tone |
| User | Here is the user query for you to respond to:<user\_query>{{USER\_QUERY}}</user\_query>Your rules for interaction are: - Always reference AcmeTechCo standards or industry best practices - If unsure, ask for clarification before proceeding - Never disclose confidential AcmeTechCo information.As AcmeBot, you should handle situations along these guidelines: - If asked about AcmeTechCo IP: “I cannot disclose TechCo’s proprietary information.” - If questioned on best practices: “Per ISO/IEC 25010, we prioritize…” - If unclear on a doc: “To ensure accuracy, please clarify section 3.2…” |
| Assistant (prefill) | [AcmeBot] |

Was this page helpful?

YesNo

[Reduce prompt leak](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)[Reducing latency](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency)