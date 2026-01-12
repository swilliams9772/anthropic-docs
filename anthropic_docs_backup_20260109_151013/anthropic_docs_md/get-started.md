# Get started with Claude - Anthropic

**Source:** https://docs.anthropic.com/en/docs/get-started

# [​](#prerequisites) Prerequisites

# [​](#call-the-api) Call the API

* cURL
* Python
* TypeScript
* Java

1

Set your API key

Get your API key from the [Anthropic Console](https://console.anthropic.com/settings/keys) and set it as an environment variable:

2

Make your first API call

Run this command to create a simple web search assistant:

```
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-4-20250514",
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
  "model": "claude-sonnet-4-20250514",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 21,
    "output_tokens": 305
  }
}

```

1

Set your API key

Get your API key from the [Anthropic Console](https://console.anthropic.com/settings/keys) and set it as an environment variable:

2

Make your first API call

Run this command to create a simple web search assistant:

```
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-4-20250514",
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
  "model": "claude-sonnet-4-20250514",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 21,
    "output_tokens": 305
  }
}

```

1

Set your API key

Get your API key from the [Anthropic Console](https://console.anthropic.com/settings/keys) and set it as an environment variable:

2

Install the SDK

Install the Anthropic Python SDK:

```
pip install anthropic

```

3

Create your code

Save this as `quickstart.py`:

```
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?"
        }
    ]
)
print(message.content)

```

4

Run your code

```
python quickstart.py

```

**Example output:**

```
[TextBlock(text='Here are some effective search strategies for finding the latest renewable energy developments:\n\n**Search Terms to Use:**\n- "renewable energy news 2024"\n- "clean energy breakthroughs"\n- "solar/wind/battery technology advances"\n- "energy storage innovations"\n- "green hydrogen developments"\n- "renewable energy policy updates"\n\n**Reliable Sources to Check:**\n- **News & Analysis:** Reuters Energy, Bloomberg New Energy Finance, Greentech Media, Energy Storage News\n- **Industry Publications:** Renewable Energy World, PV Magazine, Wind Power Engineering\n- **Research Organizations:** International Energy Agency (IEA), National Renewable Energy Laboratory (NREL)\n- **Government Sources:** Department of Energy websites, EPA clean energy updates\n\n**Specific Topics to Explore:**\n- Perovskite and next-gen solar cells\n- Offshore wind expansion\n- Grid-scale battery storage\n- Green hydrogen production\n- Carbon capture technologies\n- Smart grid innovations\n- Energy policy changes and incentives...', type='text')]

```

1

Set your API key

Get your API key from the [Anthropic Console](https://console.anthropic.com/settings/keys) and set it as an environment variable:

2

Install the SDK

Install the Anthropic TypeScript SDK:

```
npm install @anthropic-ai/sdk

```

3

Create your code

Save this as `quickstart.ts`:

```
import Anthropic from "@anthropic-ai/sdk";

async function main() {
  const anthropic = new Anthropic();

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1000,
    messages: [
      {
        role: "user",
        content: "What should I search for to find the latest developments in renewable energy?"
      }
    ]
  });
  console.log(msg);
}

main().catch(console.error);

```

4

Run your code

```
npx tsx quickstart.ts

```

**Example output:**

```
{
  id: 'msg_01ThFHzad6Bh4TpQ6cHux9t8',
  type: 'message',
  role: 'assistant',
  model: 'claude-sonnet-4-20250514',
  content: [
    {
      type: 'text',
      text: 'Here are some effective search strategies to find the latest renewable energy developments:\n\n' +
        '## Search Terms to Use:\n' +
        '- "renewable energy news 2024"\n' +
        '- "clean energy breakthroughs"\n' +
        '- "solar wind technology advances"\n' +
        '- "energy storage innovations"\n' +
        '- "green hydrogen developments"\n' +
        '- "offshore wind projects"\n' +
        '- "battery technology renewable"\n\n' +
        '## Best Sources to Check:\n\n' +
        '**News & Industry Sites:**\n' +
        '- Renewable Energy World\n' +
        '- CleanTechnica\n' +
        '- GreenTech Media (now Wood Mackenzie)\n' +
        '- Energy Storage News\n' +
        '- PV Magazine (for solar)...'
    }
  ],
  stop_reason: 'end_turn',
  usage: {
    input_tokens: 21,
    output_tokens: 302
  }
}

```

1

Set your API key

Get your API key from the [Anthropic Console](https://console.anthropic.com/settings/keys) and set it as an environment variable:

2

Install the SDK

Add the Anthropic Java SDK to your project. First find the current version on [Maven Central](https://central.sonatype.com/artifact/com.anthropic/anthropic-java).

**Gradle:**

```
implementation("com.anthropic:anthropic-java:1.0.0")

```

**Maven:**

```
<dependency>
  <groupId>com.anthropic</groupId>
  <artifactId>anthropic-java</artifactId>
  <version>1.0.0</version>
</dependency>

```

3

Create your code

Save this as `QuickStart.java`:

```
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;

public class QuickStart {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
                .model("claude-sonnet-4-20250514")
                .maxTokens(1000)
                .addUserMessage("What should I search for to find the latest developments in renewable energy?")
                .build();

        Message message = client.messages().create(params);
        System.out.println(message.content());
    }
}

```

4

Run your code

```
javac QuickStart.java
java QuickStart

```

**Example output:**

```
[ContentBlock{text=TextBlock{text=Here are some effective search strategies to find the latest renewable energy developments:

# Search Terms to Use:

- "renewable energy news 2024"
- "clean energy breakthroughs"
- "solar/wind/battery technology advances"
- "energy storage innovations"
- "green hydrogen developments"
- "renewable energy policy updates"

# Best Sources to Check:

- **News & Analysis:** Reuters Energy, Bloomberg New Energy Finance, Greentech Media
- **Industry Publications:** Renewable Energy World, PV Magazine, Wind Power Engineering
- **Research Organizations:** International Energy Agency (IEA), National Renewable Energy Laboratory (NREL)
- **Government Sources:** Department of Energy websites, EPA clean energy updates

# Specific Topics to Explore:

- Perovskite and next-gen solar cells
- Offshore wind expansion
- Grid-scale battery storage
- Green hydrogen production..., type=text}}]

```

# [​](#next-steps) Next steps

Now that you have made your first Anthropic API request, it’s time to explore what else is possible:

## Features Overview

Explore Claude’s advanced features and capabilities.## Client SDKs

Discover Anthropic client libraries.[## Anthropic Cookbook

Learn with interactive Jupyter notebooks.](https://github.com/anthropics/anthropic-cookbook)
