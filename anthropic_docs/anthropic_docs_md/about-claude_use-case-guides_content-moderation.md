# Content moderation - Anthropic

**Source:** https://docs.anthropic.com/en/docs/about-claude/use-case-guides/content-moderation

- [Documentation](/en/home)
- [Developer Console](https://console.anthropic.com/)
- [Developer Discord](https://www.anthropic.com/discord)
- [Support](https://support.anthropic.com/)

# First steps

* [Intro to Claude](/en/docs/welcome)
* [Get started](/en/docs/get-started)

# Models & pricing

* [Models overview](/en/docs/about-claude/models/overview)
* [Choosing a model](/en/docs/about-claude/models/choosing-a-model)
* [Migrating to Claude 4](/en/docs/about-claude/models/migrating-to-claude-4)
* [Model deprecations](/en/docs/about-claude/model-deprecations)
* [Pricing](/en/docs/about-claude/pricing)

# Learn about Claude

* [Building with Claude](/en/docs/overview)
* Use cases

  + [Overview](/en/docs/about-claude/use-case-guides/overview)
  + [Ticket routing](/en/docs/about-claude/use-case-guides/ticket-routing)
  + [Customer support agent](/en/docs/about-claude/use-case-guides/customer-support-chat)
  + [Content moderation](/en/docs/about-claude/use-case-guides/content-moderation)
  + [Legal summarization](/en/docs/about-claude/use-case-guides/legal-summarization)
* [Context windows](/en/docs/build-with-claude/context-windows)
* [Glossary](/en/docs/about-claude/glossary)
* Prompt engineering

# Explore features

* [Features overview](/en/docs/build-with-claude/overview)
* [Prompt caching](/en/docs/build-with-claude/prompt-caching)
* [Extended thinking](/en/docs/build-with-claude/extended-thinking)
* [Streaming Messages](/en/docs/build-with-claude/streaming)
* [Batch processing](/en/docs/build-with-claude/batch-processing)
* [Citations](/en/docs/build-with-claude/citations)
* [Multilingual support](/en/docs/build-with-claude/multilingual-support)
* [Token counting](/en/docs/build-with-claude/token-counting)
* [Embeddings](/en/docs/build-with-claude/embeddings)
* [Vision](/en/docs/build-with-claude/vision)
* [PDF support](/en/docs/build-with-claude/pdf-support)

# Agent components

* Tools
* Model Context Protocol (MCP)
* [Computer use (beta)](/en/docs/agents-and-tools/computer-use)
* [Google Sheets add-on](/en/docs/agents-and-tools/claude-for-sheets)

# Test & evaluate

* [Define success criteria](/en/docs/test-and-evaluate/define-success)
* [Develop test cases](/en/docs/test-and-evaluate/develop-tests)
* Strengthen guardrails
* [Using the Evaluation Tool](/en/docs/test-and-evaluate/eval-tool)

# Legal center

* [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)
* [Security and compliance](https://trust.anthropic.com/)

> Visit our [content moderation cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building%5Fmoderation%5Ffilter.ipynb) to see an example content moderation implementation using Claude.

This guide is focused on moderating user-generated content within your application. If you’re looking for guidance on moderating interactions with Claude, please refer to our [guardrails guide](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations).

# [​](#before-building-with-claude) Before building with Claude

# [​](#decide-whether-to-use-claude-for-content-moderation) Decide whether to use Claude for content moderation

Here are some key indicators that you should use an LLM like Claude instead of a traditional ML or rules-based approach for content moderation:

Traditional ML methods require significant engineering resources, ML expertise, and infrastructure costs. Human moderation systems incur even higher costs. With Claude, you can have a sophisticated moderation system up and running in a fraction of the time for a fraction of the price.

You desire both semantic understanding and quick decisions

Traditional ML approaches, such as bag-of-words models or simple pattern matching, often struggle to understand the tone, intent, and context of the content. While human moderation systems excel at understanding semantic meaning, they require time for content to be reviewed. Claude bridges the gap by combining semantic understanding with the ability to deliver moderation decisions quickly.

You need consistent policy decisions

By leveraging its advanced reasoning capabilities, Claude can interpret and apply complex moderation guidelines uniformly. This consistency helps ensure fair treatment of all content, reducing the risk of inconsistent or biased moderation decisions that can undermine user trust.

Your moderation policies are likely to change or evolve over time

Once a traditional ML approach has been established, changing it is a laborious and data-intensive undertaking. On the other hand, as your product or customer needs evolve, Claude can easily adapt to changes or additions to moderation policies without extensive relabeling of training data.

You require interpretable reasoning for your moderation decisions

If you wish to provide users or regulators with clear explanations behind moderation decisions, Claude can generate detailed and coherent justifications. This transparency is important for building trust and ensuring accountability in content moderation practices.

You need multilingual support without maintaining separate models

Traditional ML approaches typically require separate models or extensive translation processes for each supported language. Human moderation requires hiring a workforce fluent in each supported language. Claude’s multilingual capabilities allow it to classify tickets in various languages without the need for separate models or extensive translation processes, streamlining moderation for global customer bases.

You require multimodal support

Claude’s multimodal capabilities allow it to analyze and interpret content across both text and images. This makes it a versatile tool for comprehensive content moderation in environments where different media types need to be evaluated together.

Anthropic has trained all Claude models to be honest, helpful and harmless. This may result in Claude moderating content deemed particularly dangerous (in line with our [Acceptable Use Policy](https://www.anthropic.com/legal/aup)), regardless of the prompt used. For example, an adult website that wants to allow users to post explicit sexual content may find that Claude still flags explicit content as requiring moderation, even if they specify in their prompt not to moderate explicit sexual content. We recommend reviewing our AUP in advance of building a moderation solution.

# [​](#generate-examples-of-content-to-moderate) Generate examples of content to moderate

Before developing a content moderation solution, first create examples of content that should be flagged and content that should not be flagged. Ensure that you include edge cases and challenging scenarios that may be difficult for a content moderation system to handle effectively. Afterwards, review your examples to create a well-defined list of moderation categories.
For instance, the examples generated by a social media platform might include the following:

```
allowed_user_comments = [
    'This movie was great, I really enjoyed it. The main actor really killed it!',
    'I hate Mondays.',
    'It is a great time to invest in gold!'
]

disallowed_user_comments = [
    'Delete this post now or you better hide. I am coming after you and your family.',
    'Stay away from the 5G cellphones!! They are using 5G to control you.',
    'Congratulations! You have won a $1,000 gift card. Click here to claim your prize!'
]

# Sample user comments to test the content moderation

user_comments = allowed_user_comments + disallowed_user_comments

# List of categories considered unsafe for content moderation

unsafe_categories = [
    'Child Exploitation',
    'Conspiracy Theories',
    'Hate',
    'Indiscriminate Weapons',
    'Intellectual Property',
    'Non-Violent Crimes',
    'Privacy',
    'Self-Harm',
    'Sex Crimes',
    'Sexual Content',
    'Specialized Advice',
    'Violent Crimes'
]

```

Effectively moderating these examples requires a nuanced understanding of language. In the comment, `This movie was great, I really enjoyed it. The main actor really killed it!`, the content moderation system needs to recognize that “killed it” is a metaphor, not an indication of actual violence. Conversely, despite the lack of explicit mentions of violence, the comment `Delete this post now or you better hide. I am coming after you and your family.` should be flagged by the content moderation system.

The `unsafe_categories` list can be customized to fit your specific needs. For example, if you wish to prevent minors from creating content on your website, you could append “Underage Posting” to the list.

# [​](#how-to-moderate-content-using-claude) How to moderate content using Claude

# [​](#select-the-right-claude-model) Select the right Claude model

When selecting a model, it’s important to consider the size of your data. If costs are a concern, a smaller model like Claude Haiku 3 is an excellent choice due to its cost-effectiveness. Below is an estimate of the cost to moderate text for a social media platform that receives one billion posts per month:

* **Content size**

  + Posts per month: 1bn
  + Characters per post: 100
  + Total characters: 100bn
* **Estimated tokens**

  + Input tokens: 28.6bn (assuming 1 token per 3.5 characters)
  + Percentage of messages flagged: 3%
  + Output tokens per flagged message: 50
  + Total output tokens: 1.5bn
* **Claude Haiku 3 estimated cost**

  + Input token cost: 2,860 MTok \* $0.25/MTok = $715
  + Output token cost: 1,500 MTok \* $1.25/MTok = $1,875
  + Monthly cost: $715 + $1,875 = $2,590
* **Claude Sonnet 4 estimated cost**

  + Input token cost: 2,860 MTok \* $3.00/MTok = $8,580
  + Output token cost: 1,500 MTok \* $15.00/MTok = $22,500
  + Monthly cost: $8,580 + $22,500 = $31,080

Actual costs may differ from these estimates. These estimates are based on the prompt highlighted in the section on [batch processing](/_sites/docs.anthropic.com/en/docs/about-claude/use-case-guides/content-moderation#consider-batch-processing). Output tokens can be reduced even further by removing the `explanation` field from the response.

# [​](#build-a-strong-prompt) Build a strong prompt

In order to use Claude for content moderation, Claude must understand the moderation requirements of your application. Let’s start by writing a prompt that allows you to define your moderation needs:

```
import anthropic
import json

# Initialize the Anthropic client

client = anthropic.Anthropic()

def moderate_message(message, unsafe_categories):
    # Convert the list of unsafe categories into a string, with each category on a new line
    unsafe_category_str = '\n'.join(unsafe_categories)

    # Construct the prompt for Claude, including the message and unsafe categories
    assessment_prompt = f"""
    Determine whether the following message warrants moderation,
    based on the unsafe categories outlined below.

    Message:
    <message>{message}</message>

    Unsafe Categories:
    <categories>
    {unsafe_category_str}
    </categories>

    Respond with ONLY a JSON object, using the format below:
    {{
    "violation": <Boolean field denoting whether the message should be moderated>,
    "categories": [Comma-separated list of violated categories],
    "explanation": [Optional. Only include if there is a violation.]
    }}"""

    # Send the request to Claude for content moderation
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # Using the Haiku model for lower costs
        max_tokens=200,
        temperature=0,   # Use 0 temperature for increased consistency
        messages=[
            {"role": "user", "content": assessment_prompt}
        ]
    )

    # Parse the JSON response from Claude
    assessment = json.loads(response.content[0].text)

    # Extract the violation status from the assessment
    contains_violation = assessment['violation']

    # If there's a violation, get the categories and explanation; otherwise, use empty defaults
    violated_categories = assessment.get('categories', []) if contains_violation else []
    explanation = assessment.get('explanation') if contains_violation else None

    return contains_violation, violated_categories, explanation

# Process each comment and print the results

for comment in user_comments:
    print(f"\nComment: {comment}")
    violation, violated_categories, explanation = moderate_message(comment, unsafe_categories)

    if violation:
        print(f"Violated Categories: {', '.join(violated_categories)}")
        print(f"Explanation: {explanation}")
    else:
        print("No issues detected.")

```

In this example, the `moderate_message` function contains an assessment prompt that includes the unsafe content categories and the message we wish to evaluate. The prompt asks Claude to assess whether the message should be moderated, based on the unsafe categories we defined.

The model’s assessment is then parsed to determine if there is a violation. If there is a violation, Claude also returns a list of violated categories, as well as an explanation as to why the message is unsafe.

# [​](#evaluate-your-prompt) Evaluate your prompt

Content moderation is a classification problem. Thus, you can use the same techniques outlined in our [classification cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/classification/guide.ipynb) to determine the accuracy of your content moderation system.

One additional consideration is that instead of treating content moderation as a binary classification problem, you may instead create multiple categories to represent various risk levels. Creating multiple risk levels allows you to adjust the aggressiveness of your moderation. For example, you might want to automatically block user queries that are deemed high risk, while users with many medium risk queries are flagged for human review.

```
import anthropic
import json

# Initialize the Anthropic client

client = anthropic.Anthropic()

def assess_risk_level(message, unsafe_categories):
    # Convert the list of unsafe categories into a string, with each category on a new line
    unsafe_category_str = '\n'.join(unsafe_categories)

    # Construct the prompt for Claude, including the message, unsafe categories, and risk level definitions
    assessment_prompt = f"""
    Assess the risk level of the following message warrants moderation,
    based on the unsafe categories listed below.

Message:
<message>{message}</message>

Unsafe Categories:
<categories>
{unsafe_category_str}
</categories>

Assign a risk level based on your confidence that the user's message should be moderated
based on the defined unsafe categories:

0 - No risk
1 - Low risk
2 - Medium risk
3 - High risk

Respond with ONLY a JSON object, using the format below:
{{
  "risk_level": <Numerical field denoting the risk level>,
  "categories": [Comma-separated list of violated categories],
  "explanation": <Optional. Only include if risk level is greater than 0>
}}"""

    # Send the request to Claude for risk assessment
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # Using the Haiku model for lower costs
        max_tokens=200,
        temperature=0,   # Use 0 temperature for increased consistency
        messages=[
            {"role": "user", "content": assessment_prompt}
        ]
    )

    # Parse the JSON response from Claude
    assessment = json.loads(response.content[0].text)

    # Extract the risk level, violated categories, and explanation from the assessment
    risk_level = assessment["risk_level"]
    violated_categories = assessment["categories"]
    explanation = assessment.get("explanation")

    return risk_level, violated_categories, explanation

# Process each comment and print the results

for comment in user_comments:
    print(f"\nComment: {comment}")
    risk_level, violated_categories, explanation = assess_risk_level(comment, unsafe_categories)

    print(f"Risk Level: {risk_level}")
    if violated_categories:
        print(f"Violated Categories: {', '.join(violated_categories)}")
    if explanation:
        print(f"Explanation: {explanation}")

```

This code implements an `assess_risk_level` function that uses Claude to evaluate the risk level of a message. The function accepts a message and a list of unsafe categories as inputs.

Within the function, a prompt is generated for Claude, including the message to be assessed, the unsafe categories, and specific instructions for evaluating the risk level. The prompt instructs Claude to respond with a JSON object that includes the risk level, the violated categories, and an optional explanation.

This approach enables flexible content moderation by assigning risk levels. It can be seamlessly integrated into a larger system to automate content filtering or flag comments for human review based on their assessed risk level. For instance, when executing this code, the comment `Delete this post now or you better hide. I am coming after you and your family.` is identified as high risk due to its dangerous threat. Conversely, the comment `Stay away from the 5G cellphones!! They are using 5G to control you.` is categorized as medium risk.

# [​](#deploy-your-prompt) Deploy your prompt

Once you are confident in the quality of your solution, it’s time to deploy it to production. Here are some best practices to follow when using content moderation in production:

1. **Provide clear feedback to users:** When user input is blocked or a response is flagged due to content moderation, provide informative and constructive feedback to help users understand why their message was flagged and how they can rephrase it appropriately. In the coding examples above, this is done through the `explanation` tag in the Claude response.
2. **Analyze moderated content:** Keep track of the types of content being flagged by your moderation system to identify trends and potential areas for improvement.
3. **Continuously evaluate and improve:** Regularly assess the performance of your content moderation system using metrics such as precision and recall tracking. Use this data to iteratively refine your moderation prompts, keywords, and assessment criteria.

# [​](#improve-performance) Improve performance

In complex scenarios, it may be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview). Here are some advanced strategies:

# [​](#define-topics-and-provide-examples) Define topics and provide examples

In addition to listing the unsafe categories in the prompt, further improvements can be made by providing definitions and phrases related to each category.

```
import anthropic
import json

# Initialize the Anthropic client

client = anthropic.Anthropic()

# Dictionary of categories considered unsafe for content moderation, with their definitions

unsafe_category_definitions = {
    'Child Exploitation': 'Content that depicts child nudity or that enables, encourages, excuses, or depicts the sexual abuse of children.',
    'Conspiracy Theories': """Content that promotes or endorses unfounded, false, or misleading theories about events, situations, or individuals,
        which can incite harm or undermine public trust in institutions or facts.""",
    'Hate': """Content that is hateful toward people on the basis of their protected characteristics
        (race, color, ethnicity, national origin, disability, religious affiliation, caste, sexual orientation, sex, gender identity and serious disease),
        or content that perpetuates negative stereotypes.""",
    'Indiscriminate Weapons': 'Content that enables the creation of weapons of mass destruction.',
    'Intellectual Property': 'Content that violates the intellectual property rights of third parties.',
    'Non-Violent Crimes': 'Content that enables, encourages, or excuses the commission of non-violent crimes.',
    'Privacy': 'Content that contains sensitive, personal information about private individuals.',
    'Self-Harm': 'Content that enables, encourages, or excuses acts of intentional self-harm.',
    'Sex Crimes': 'Content that enables, encourages, or excuses the commission of sex crimes.',
    'Sexual Content': 'Content that contains erotic descriptions or explicit depictions of sex acts.',
    'Specialized Advice': """Content that contains financial, medical, or legal advice.
        Financial advice includes guidance on investments, stocks, bonds, or any financial planning.""",
    'Violent Crimes': 'Content that enables, encourages, or excuses the commission of violent crimes.',
}

def moderate_message_with_definitions(message, unsafe_category_definitions):
    # Format unsafe categories string, with each category and its definition on a new line
    unsafe_category_str = '\n'.join(f'{category}: {definition}'
        for category, definition in unsafe_category_definitions.items()
    )

    # Construct the prompt for Claude, including the message and unsafe categories
    assessment_prompt = f"""Determine whether the following message warrants moderation, based on the unsafe categories outlined below.

Message:
<message>{message}</message>

Unsafe Categories and Their Definitions:
<categories>
{unsafe_category_str}
</categories>

It's important that you remember all unsafe categories and their definitions.

Respond with ONLY a JSON object, using the format below:
{{
  "violation": <Boolean field denoting whether the message should be moderated>,
  "categories": [Comma-separated list of violated categories],
  "explanation": [Optional. Only include if there is a violation.]
}}"""

    # Send the request to Claude for content moderation
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # Using the Haiku model for lower costs
        max_tokens=200,
        temperature=0,   # Use 0 temperature for increased consistency
        messages=[
            {"role": "user", "content": assessment_prompt}
        ]
    )

    # Parse the JSON response from Claude
    assessment = json.loads(response.content[0].text)

    # Extract the violation status from the assessment
    contains_violation = assessment['violation']

    # If there's a violation, get the categories and explanation; otherwise, use empty defaults
    violated_categories = assessment.get('categories', []) if contains_violation else []
    explanation = assessment.get('explanation') if contains_violation else None

    return contains_violation, violated_categories, explanation

# Process each comment and print the results

for comment in user_comments:
    print(f"\nComment: {comment}")
    violation, violated_categories, explanation = moderate_message_with_definitions(comment, unsafe_category_definitions)

    if violation:
        print(f"Violated Categories: {', '.join(violated_categories)}")
        print(f"Explanation: {explanation}")
    else:
        print("No issues detected.")

```

The `moderate_message_with_definitions` function expands upon the earlier `moderate_message` function by allowing each unsafe category to be paired with a detailed definition. This occurs in the code by replacing the `unsafe_categories` list from the original function with an `unsafe_category_definitions` dictionary. This dictionary maps each unsafe category to its corresponding definition. Both the category names and their definitions are included in the prompt.

Notably, the definition for the `Specialized Advice` category now specifies the types of financial advice that should be prohibited. As a result, the comment `It's a great time to invest in gold!`, which previously passed the `moderate_message` assessment, now triggers a violation.

# [​](#consider-batch-processing) Consider batch processing

To reduce costs in situations where real-time moderation isn’t necessary, consider moderating messages in batches. Include multiple messages within the prompt’s context, and ask Claude to assess which messages should be moderated.

```
import anthropic
import json

# Initialize the Anthropic client

client = anthropic.Anthropic()

def batch_moderate_messages(messages, unsafe_categories):
    # Convert the list of unsafe categories into a string, with each category on a new line
    unsafe_category_str = '\n'.join(unsafe_categories)

    # Format messages string, with each message wrapped in XML-like tags and given an ID
    messages_str = '\n'.join([f'<message id={idx}>{msg}</message>' for idx, msg in enumerate(messages)])

    # Construct the prompt for Claude, including the messages and unsafe categories
    assessment_prompt = f"""Determine the messages to moderate, based on the unsafe categories outlined below.

Messages:
<messages>
{messages_str}
</messages>

Unsafe categories and their definitions:
<categories>
{unsafe_category_str}
</categories>

Respond with ONLY a JSON object, using the format below:
{{
  "violations": [
    {{
      "id": <message id>,
      "categories": [list of violated categories],
      "explanation": <Explanation of why there's a violation>
    }},
    ...
  ]
}}

Important Notes:
- Remember to analyze every message for a violation.
- Select any number of violations that reasonably apply."""

    # Send the request to Claude for content moderation
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # Using the Haiku model for lower costs
        max_tokens=2048,  # Increased max token count to handle batches
        temperature=0,    # Use 0 temperature for increased consistency
        messages=[
            {"role": "user", "content": assessment_prompt}
        ]
    )

    # Parse the JSON response from Claude
    assessment = json.loads(response.content[0].text)
    return assessment

# Process the batch of comments and get the response

response_obj = batch_moderate_messages(user_comments, unsafe_categories)

# Print the results for each detected violation

for violation in response_obj['violations']:
    print(f"""Comment: {user_comments[violation['id']]}
Violated Categories: {', '.join(violation['categories'])}
Explanation: {violation['explanation']}
""")

```

In this example, the `batch_moderate_messages` function handles the moderation of an entire batch of messages with a single Claude API call.
Inside the function, a prompt is created that includes the list of messages to evaluate, the defined unsafe content categories, and their descriptions. The prompt directs Claude to return a JSON object listing all messages that contain violations. Each message in the response is identified by its id, which corresponds to the message’s position in the input list.
Keep in mind that finding the optimal batch size for your specific needs may require some experimentation. While larger batch sizes can lower costs, they might also lead to a slight decrease in quality. Additionally, you may need to increase the `max_tokens` parameter in the Claude API call to accommodate longer responses. For details on the maximum number of tokens your chosen model can output, refer to the [model comparison page](https://docs.anthropic.com/en/docs/about-claude/models#model-comparison).

[## Content moderation cookbook

View a fully implemented code-based example of how to use Claude for content moderation.](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building%5Fmoderation%5Ffilter.ipynb)[## Guardrails guide

Explore our guardrails guide for techniques to moderate interactions with Claude.](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)

Was this page helpful?

YesNo

Customer support agent[Legal summarization](/en/docs/about-claude/use-case-guides/legal-summarization)

On this page
