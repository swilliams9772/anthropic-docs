# Getting Started with Custom Connectors Using Remote MCP

**Source:** https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp

Custom connectors using remote MCP are available on Claude and Claude Desktop for users on Pro, Max, Team, and Enterprise plans. This feature is currently in beta.

# What are custom connectors?

Custom connectors let you connect Claude directly to the tools and data sources that matter most to your workflows. This enables Claude to operate within your favorite software and draw insights from the complete context of your external tools.

You can:

* Connect Claude to existing remote MCP servers.
* Build your own remote MCP servers to connect with any tool.

**⚠️ Security and Privacy with Custom Connectors (beta)**

Be aware that custom connectors allow you to connect Claude to services that have not been verified by Anthropic, and allow Claude to access and take action in these services. For more guidance, review the [Security and Privacy Considerations](#h_9088ccdf4d) section below.

# What are remote MCP servers?

The Model Context Protocol (MCP) is an open standard, created by Anthropic, for AI applications to connect to tools and data.

Previously, [MCP servers only ran locally](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop) (i.e. on a user's laptop). Now, developers can build and host remote MCP servers that communicate with AI apps over the internet.

Remote MCP servers give models access to internet-hosted tools and data, transforming Claude into an informed teammate that can independently handle complex, multi-step projects tailored to your needs.

# How to add a custom connector

**Note:**While anyone can build and host connectors using remote MCP, only Owners can add them to Team and Enterprise plans. Once a connector has been added to a Team or Enterprise organization, users individually connect to and enable that connector. This ensures that Claude can only access tools and data that the individual user has access to.

# For Team and Enterprise Plans

**Preliminary steps for Owners:**

Before members of Team and Enterprise plans can configure custom connectors, an Owner needs to follow these initial steps to add a custom connector to your organization:

1. Navigate to [Admin settings > Connectors](https://claude.ai/admin-settings/connectors).
2. Click "Add custom connector" at the bottom of the section.
3. Add your connector's remote MCP server URL.
4. Optionally, click “Advanced settings” to specify an OAuth Client ID and OAuth Client Secret for your server.
5. Finish configuring your connector by clicking "Add."

**Steps for members after connector is configured:**

1. Navigate to [Settings > Connectors](https://claude.ai/settings/connectors).
2. Locate the "Connectors" section.
3. Find the custom connector your Owner added in the list (it will have a "Custom" label).
4. Click "Connect" to authenticate and start using the connector with Claude.

# For Pro and Max plans

If you are using an individual Pro or Max plan, follow these steps to add a custom connector:

1. Navigate to [Settings > Connectors](https://claude.ai/settings/connectors).
2. Locate the "Connectors" section.
3. Click "Add custom connector" at the bottom of the section.
4. Add your connector's remote MCP server URL.
5. Optionally, click “Advanced settings” to specify an OAuth Client ID and OAuth Client Secret for your server.
6. Finish configuring your connector by clicking "Add."

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916091157/febc1f1e569df97a2f800c7ea493/8d09370d-1c7a-489c-b62b-b3484aaaef31?expires=1767998700&signature=b23d2b1612360f1582d92a2b74801cf54ed8120285800f01061f27105d10383a&req=dSkmEMl3nIBaXvMW1HO4zWxgPd94pqqNxxBcrakePoN%2BVC3VxPKb6frsC48v%0AQ4QKDAry7u8uuw%2F1EcE%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916091157/febc1f1e569df97a2f800c7ea493/8d09370d-1c7a-489c-b62b-b3484aaaef31?expires=1767998700&signature=b23d2b1612360f1582d92a2b74801cf54ed8120285800f01061f27105d10383a&req=dSkmEMl3nIBaXvMW1HO4zWxgPd94pqqNxxBcrakePoN%2BVC3VxPKb6frsC48v%0AQ4QKDAry7u8uuw%2F1EcE%3D%0A)

# Enabling connectors after configuration

You can enable connectors for individual conversations via the “+” button on the lower left of your chat interface, then "Connectors." You'll see your configured connectors with toggles allowing you to enable/disable them per conversation.

# How to remove or edit connectors

You can remove or edit the configuration of your connector:

1. Navigate to [Settings > Connectors](https://claude.ai/settings/connectors).
2. Locate the "Connectors" section.
3. Click "Remove" or select the three dots next to the connector you'd like to edit.
4. Follow the prompts to edit or remove.

# How to build custom connectors

To learn about building connectors to use with Claude, see [Building Custom Connectors via Remote MCP Servers](https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers).

# Security and Privacy Considerations

Custom connectors allow you to connect Claude to arbitrary services that have not been verified by Anthropic. When you connect Claude to external services, you're granting it the ability to access and potentially modify data within those services based on your permissions. It’s important to make sure you’re only connecting to remote MCP servers that you trust and that you’re aware of Claude’s interactions with web connectors.

# Security and Permissions

When you add a custom connector to Claude, you'll typically go through an OAuth authentication process to securely sign in to the application and grant specific permissions. This allows Claude to interact with the application on your behalf, without Claude ever seeing your actual password. You can revoke these permissions at any time by disconnecting the connector in Claude's settings or the third-party service's security settings.

Remote MCP servers act as intermediaries between Claude and external applications. You should:

* **Only connect to trusted servers:** Only connect Claude to servers built and hosted by organizations and applications you trust.
* **Review requested permissions carefully:** During auth, review what permissions the MCP server is requesting to the application. Limit these scopes when possible and deny access if requested permissions seem unnecessary.
* **Be aware of prompt injections:** Malicious MCP servers may include hidden instructions that try to make Claude perform unintended actions. Claude has built-in protections that attempt to block these attacks, but it's important to pay attention to tool inputs & outputs and connect only to trusted servers.
* **Monitor changes in tool behavior:** Server developers may update tool behavior unexpectedly, leading to unintended or malicious behavior.

# Reporting Malicious MCP Servers

If you become aware of a malicious MCP server, please it to our [vulnerability disclosure program](https://hackerone.com/anthropic-vdp/), and choose [`https://github.com/modelcontextprotocol`](https://github.com/modelcontextprotocol) as the Asset.

# Taking Actions with Tools

Remote MCP servers give Claude tools it can invoke during your conversation. The developer of an MCP server can define what these tools do, including:

* Reading data from connected applications.
* Creating, modifying, or deleting data in connected applications.
* Taking actions on behalf of the user.

Claude can only access resources that you've given the server permission to access, but you should:

* Be aware of any actions Claude is taking and that they have no destructive or unintended effects.
* Review Claude's tool approval requests carefully and only click "Allow always" when using a server and tool that you trust to run unsupervised.
* Using the "Search and tools" menu, disable any tools that aren't relevant to the current conversation or that you don't want Claude to be able to invoke.

# Using Claude with Research

**Note:** [Advanced Research](https://www.anthropic.com/news/integrations) is not currently able to invoke tools from local MCP servers.

Research allows Claude to deeply investigate queries by searching through hundreds of internal and external sources. During the research process, Claude can invoke tools from your connectors automatically without further approval.

When using Research with custom connectors:

* Disable any tools that can take write actions in external applications.
* Review Claude’s approval request carefully and be aware of which tools you’re granting Claude permission to invoke.
* Be mindful of the impact of Claude sending a large number of requests to your connectors.

See [Using Research on Claude](https://support.claude.com/en/articles/11088861-using-research-on-claude) for more information about this feature.

---

Related Articles

[Pre-built Web Connectors Using Remote MCP](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp)[Building Custom Connectors via Remote MCP Servers](https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers)[Anthropic Connectors Directory FAQ](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq)[When to Use Desktop and Web Connectors](https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors)[Remote MCP Server Submission Guide](https://support.claude.com/en/articles/12922490-remote-mcp-server-submission-guide)
