---
title: 
source_url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Prompt engineering

Extended thinking tips

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

  + [Overview](/en/docs/build-with-claude/prompt-engineering/overview)
  + [Prompt generator](/en/docs/build-with-claude/prompt-engineering/prompt-generator)
  + [Use prompt templates](/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables)
  + [Prompt improver](/en/docs/build-with-claude/prompt-engineering/prompt-improver)
  + [Be clear and direct](/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct)
  + [Use examples (multishot prompting)](/en/docs/build-with-claude/prompt-engineering/multishot-prompting)
  + [Let Claude think (CoT)](/en/docs/build-with-claude/prompt-engineering/chain-of-thought)
  + [Use XML tags](/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
  + [Give Claude a role (system prompts)](/en/docs/build-with-claude/prompt-engineering/system-prompts)
  + [Prefill Claude's response](/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)
  + [Chain complex prompts](/en/docs/build-with-claude/prompt-engineering/chain-prompts)
  + [Long context tips](/en/docs/build-with-claude/prompt-engineering/long-context-tips)
  + [Extended thinking tips](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips)
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

This guide provides advanced strategies and techniques for getting the most out of Claude’s extended thinking feature. Extended thinking allows Claude to work through complex problems step-by-step, improving performance on difficult tasks. When you enable extended thinking, Claude shows its reasoning process before providing a final answer, giving you transparency into how it arrived at its conclusion.

See [Extended thinking models](/en/docs/about-claude/models/extended-thinking-models) for guidance on deciding when to use extended thinking vs. standard thinking modes.

[​](#before-diving-in) Before diving in
---------------------------------------

This guide presumes that you have already decided to use extended thinking mode over standard mode and have reviewed our basic steps on [how to get started with extended thinking](/en/docs/about-claude/models/extended-thinking-models#getting-started-with-claude-3-7-sonnet) as well as our [extended thinking implementation guide](/en/docs/build-with-claude/extended-thinking).

### [​](#technical-considerations-for-extended-thinking) Technical considerations for extended thinking

* Thinking tokens have a minimum budget of 1024 tokens. We recommend that you start with the minimum thinking budget and incrementally increase to adjust based on your needs and task complexity.
* For workloads where the optimal thinking budget is above 32K, we recommend that you use [batch processing](/en/docs/build-with-claude/batch-processing) to avoid networking issues. Requests pushing the model to think above 32K tokens causes long running requests that might run up against system timeouts and open connection limits.
* Extended thinking performs best in English, though final outputs can be in [any language Claude supports](/en/docs/build-with-claude/multilingual-support).
* If you need thinking below the minimum budget, we recommend using standard mode, with thinking turned off, with traditional chain-of-thought prompting with XML tags (like `<thinking>`). See [chain of thought prompting](/en/docs/build-with-claude/prompt-engineering/chain-of-thought).

[​](#prompting-techniques-for-extended-thinking) Prompting techniques for extended thinking
-------------------------------------------------------------------------------------------

### [​](#use-general-instructions-first-then-troubleshoot-with-more-step-by-step-instructions) Use general instructions first, then troubleshoot with more step-by-step instructions

Claude often performs better with high level instructions to just think deeply about a task rather than step-by-step prescriptive guidance. The model’s creativity in approaching problems may exceed a human’s ability to prescribe the optimal thinking process.

For example, instead of:

Consider:

That said, Claude can still effectively follow complex structured execution steps when needed. The model can handle even longer lists with more complex instructions than previous versions. We recommend that you start with more generalized instructions, then read Claude’s thinking output and iterate to provide more specific instructions to steer its thinking from there.

### [​](#multishot-prompting-with-extended-thinking) Multishot prompting with extended thinking

[Multishot prompting](/en/docs/build-with-claude/prompt-engineering/multishot-prompting) works well with extended thinking. When you provide Claude examples of how to think through problems, it will follow similar reasoning patterns within its extended thinking blocks.

You can include few-shot examples in your prompt in extended thinking scenarios by using XML tags like `<thinking>` or `<scratchpad>` to indicate canonical patterns of extended thinking in those examples.

Claude will generalize the pattern to the formal extended thinking process. However, it’s possible you’ll get better results by giving Claude free rein to think in the way it deems best.

Example:

### [​](#maximizing-instruction-following-with-extended-thinking) Maximizing instruction following with extended thinking

Claude shows significantly improved instruction following when extended thinking is enabled. The model typically:

1. Reasons about instructions inside the extended thinking block
2. Executes those instructions in the response

To maximize instruction following:

* Be clear and specific about what you want
* For complex instructions, consider breaking them into numbered steps that Claude should work through methodically
* Allow Claude enough budget to process the instructions fully in its extended thinking

### [​](#using-extended-thinking-to-debug-and-steer-claudes-behavior) Using extended thinking to debug and steer Claude’s behavior

You can use Claude’s thinking output to debug Claude’s logic, although this method is not always perfectly reliable.

To make the best use of this methodology, we recommend the following tips:

* We don’t recommend passing Claude’s extended thinking back in the user text block, as this doesn’t improve performance and may actually degrade results.
* Prefilling extended thinking is explicitly not allowed, and manually changing the model’s output text that follows its thinking block is likely going to degrade results due to model confusion.

When extended thinking is turned off, standard `assistant` response text [prefill](/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response) is still allowed.

Sometimes Claude may repeat its extended thinking in the assistant output text. If you want a clean response, instruct Claude not to repeat its extended thinking and to only output the answer.

### [​](#making-the-best-of-long-outputs-and-longform-thinking) Making the best of long outputs and longform thinking

Claude with extended thinking enabled and [extended output capabilities (beta)](/en/docs/about-claude/models/extended-thinking-models#extended-output-capabilities-beta) excels at generating large amounts of bulk data and longform text.

For dataset generation use cases, try prompts such as “Please create an extremely detailed table of…” for generating comprehensive datasets.

For use cases such as detailed content generation where you may want to generate longer extended thinking blocks and more detailed responses, try these tips:

* Increase both the maximum extended thinking length AND explicitly ask for longer outputs
* For very long outputs (20,000+ words), request a detailed outline with word counts down to the paragraph level. Then ask Claude to index its paragraphs to the outline and maintain the specified word counts

We do not recommend that you push Claude to output more tokens for outputting tokens’ sake. Rather, we encourage you to start with a small thinking budget and increase as needed to find the optimal settings for your use case.

Here are example use cases where Claude excels due to longer extended thinking:

Complex STEM problems

Complex STEM problems require Claude to build mental models, apply specialized knowledge, and work through sequential logical steps—processes that benefit from longer reasoning time.

* Standard prompt
* Enhanced prompt

This simpler task typically results in only about a few seconds of thinking time.

Constraint optimization problems

Constraint optimization challenges Claude to satisfy multiple competing requirements simultaneously, which is best accomplished when allowing for long extended thinking time so that the model can methodically address each constraint.

* Standard prompt
* Enhanced prompt

This open-ended request typically results in only about a few seconds of thinking time.

Thinking frameworks

Structured thinking frameworks give Claude an explicit methodology to follow, which may work best when Claude is given long extended thinking space to follow each step.

* Standard prompt
* Enhanced prompt

This broad strategic question typically results in only about a few seconds of thinking time.

### [​](#have-claude-reflect-on-and-check-its-work-for-improved-consistency-and-error-handling) Have Claude reflect on and check its work for improved consistency and error handling

You can use simple natural language prompting to improve consistency and reduce errors:

1. Ask Claude to verify its work with a simple test before declaring a task complete
2. Instruct the model to analyze whether its previous step achieved the expected result
3. For coding tasks, ask Claude to run through test cases in its extended thinking

Example:

[​](#next-steps) Next steps
---------------------------

[Extended thinking cookbook
--------------------------

Explore practical examples of extended thinking in our cookbook.](https://github.com/anthropics/anthropic-cookbook/tree/main/extended_thinking)[Extended thinking guide
-----------------------

See complete technical documentation for implementing extended thinking.](/en/docs/build-with-claude/extended-thinking)

Was this page helpful?

YesNo

[Long context tips](/en/docs/build-with-claude/prompt-engineering/long-context-tips)[Extended thinking](/en/docs/build-with-claude/extended-thinking)

On this page

* [Before diving in](#before-diving-in)
* [Technical considerations for extended thinking](#technical-considerations-for-extended-thinking)
* [Prompting techniques for extended thinking](#prompting-techniques-for-extended-thinking)
* [Use general instructions first, then troubleshoot with more step-by-step instructions](#use-general-instructions-first-then-troubleshoot-with-more-step-by-step-instructions)
* [Multishot prompting with extended thinking](#multishot-prompting-with-extended-thinking)
* [Maximizing instruction following with extended thinking](#maximizing-instruction-following-with-extended-thinking)
* [Using extended thinking to debug and steer Claude’s behavior](#using-extended-thinking-to-debug-and-steer-claudes-behavior)
* [Making the best of long outputs and longform thinking](#making-the-best-of-long-outputs-and-longform-thinking)
* [Have Claude reflect on and check its work for improved consistency and error handling](#have-claude-reflect-on-and-check-its-work-for-improved-consistency-and-error-handling)
* [Next steps](#next-steps)