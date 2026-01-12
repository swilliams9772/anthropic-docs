# Get started with Claude

**Source:** https://platform.claude.com/docs/en/get-started

Copy page

# Prerequisites

* An Anthropic [Console account](/)
* An [API key](/settings/keys)

# Call the API

cURL

cURL

Python

Python

TypeScript

TypeScript

Java

Java

1. 1

   Set your API key

   Get your API key at the [Claude Console](/settings/keys) and set it as an environment variable:

   ```
   export ANTHROPIC_API_KEY='your-api-key-here'
   ```
2. 2

   Make your first API call

   Run this command to create a simple web search assistant:

   ```
   curl https://api.anthropic.com/v1/messages \
     -H "Content-Type: application/json" \
     -H "x-api-key: $ANTHROPIC_API_KEY" \
     -H "anthropic-version: 2023-06-01" \
     -d '{
       "model": "claude-sonnet-4-5",
       "max_tokens": 1000,
       "messages": [
         {
           "role": "user",
           "content": "What should I search for to find the latest developments in renewable energy?"
         }
       ]
     }'
   ```

   **Example output:**

   ```
   {
     "id": "msg_01HCDu5LRGeP2o7s2xGmxyx8",
     "type": "message",
     "role": "assistant",
     "content": [
       {
         "type": "text",
         "text": "Here are some effective search strategies to find the latest renewable energy developments:\n\n## Search Terms to Use:\n- \"renewable energy news 2024\"\n- \"clean energy breakthrough\"\n- \"solar/wind/battery technology advances\"\n- \"green energy innovations\"\n- \"climate tech developments\"\n- \"energy storage solutions\"\n\n## Best Sources to Check:\n\n**News & Industry Sites:**\n- Renewable Energy World\n- GreenTech Media (now Wood Mackenzie)\n- Energy Storage News\n- CleanTechnica\n- PV Magazine (for solar)\n- WindPower Engineering & Development..."
       }
     ],
     "model": "claude-sonnet-4-5",
     "stop_reason": "end_turn",
     "usage": {
       "input_tokens": 21,
       "output_tokens": 305
     }
   }
   ```

# Next steps

Now that you have made your first Claude API request, it's time to explore what else is possible:

[Working with Messages

Learn common patterns for the Messages API.](/docs/en/build-with-claude/working-with-messages)[Features Overview

Explore Claude's advanced features and capabilities.](/docs/en/api/overview)[Client SDKs

Discover Anthropic client libraries.](/docs/en/api/client-sdks)[Claude Cookbook

Learn with interactive Jupyter notebooks.](https://platform.claude.com/cookbooks)
