# Mitigate jailbreaks and prompt injections

**Source:** http://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks

Copy page

Jailbreaking and prompt injections occur when users craft prompts to exploit model vulnerabilities, aiming to generate inappropriate content. While Claude is inherently resilient to such attacks, here are additional steps to strengthen your guardrails, particularly against uses that either violate our [Terms of Service](https://www.anthropic.com/legal/commercial-terms) or [Usage Policy](https://www.anthropic.com/legal/aup).

* **Harmlessness screens**: Use a lightweight model like Claude Haiku 4.5 to pre-screen user inputs. Use [structured outputs](/docs/en/build-with-claude/structured-outputs) to constrain the response to a simple classification.

  ### Example: Harmlessness screen for content moderation
* **Input validation**: Filter prompts for jailbreaking patterns. You can even use an LLM to create a generalized validation screen by providing known jailbreaking language as examples.
* **Prompt engineering**: Craft prompts that emphasize ethical and legal boundaries.

  ### Example: Ethical system prompt for an enterprise chatbot

Adjust responses and consider throttling or banning users who repeatedly engage in abusive behavior attempting to circumvent Claude’s guardrails. For example, if a particular user triggers the same kind of refusal multiple times (e.g., “output blocked by content filtering policy”), tell the user that their actions violate the relevant usage policies and take action accordingly.

* **Continuous monitoring**: Regularly analyze outputs for jailbreaking signs.
  Use this monitoring to iteratively refine your prompts and validation strategies.

# Advanced: Chain safeguards

Combine strategies for robust protection. Here's an enterprise-grade example with tool use:

# Example: Multi-layered protection for a financial advisor chatbot

By layering these strategies, you create a robust defense against jailbreaking and prompt injections, ensuring your Claude-powered applications maintain the highest standards of safety and compliance.

Was this page helpful?
