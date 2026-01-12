# Pre

**Source:** https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp

Web connectors using remote MCP are available on Claude, Claude Desktop, and Claude Mobile (iOS and Android) for users with paid plans (Pro, Max, Team, or Enterprise).

Connect your favorite tools and data sources to Claude. The list below includes connectors provided by [initial launch partners announced in the Anthropic blog](https://www.anthropic.com/news/integrations). You can also connect Claude to any connectors built by your favorite companies and software providers, or to custom connectors built by yourself or your organization.

|  |  |  |
| --- | --- | --- |
| **Connector** | **Description** | **Connector URL** |
| [Asana](https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server) | Create, search, and assign tasks and deliverables | <https://mcp.asana.com/sse> |
| [Atlassian](http://atlassian.com/platform/remote-mcp-server) | Track issues, manage sprints, create docs, and search knowledge bases | <https://mcp.atlassian.com/v1/sse> |
| [Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare/tree/main) | Build, manage, and debug cloud services | For the exact connector URL, visit: <https://github.com/cloudflare/mcp-server-cloudflare> |
| [Intercom](https://www.intercom.com/blog/introducing-model-context-protocol-fin) | Analyze support trends and triage customer issues | <https://mcp.intercom.com/sse> |
| [Linear](https://linear.app/changelog/2025-05-01-mcp) | Search for and create issues, projects, and comments | <https://mcp.linear.app/sse> |
| [PayPal](https://www.paypal.ai/) | Create and manage invoices, and analyze sales activity | <https://mcp.paypal.com/sse> |
| [Plaid](https://api.dashboard.plaid.com/mcp/sse) | Analyze metrics, usage, and support tickets | <https://api.dashboard.plaid.com/mcp/sse> |
| [Sentry](https://docs.sentry.io/product/sentry-mcp/) | Search, query, and debug errors intelligently | <https://mcp.sentry.dev/sse> |
| \*[Slack](https://docs.slack.dev/ai/mcp-server) | Send messages, create canvasses and fetch Slack content | <https://claude.ai/directory/597f662f-36de-437e-836e-5a81013cbfbe> |
| [Square](https://developer.squareup.com/docs/mcp) | Search and manage transaction, merchant, and payment data | <https://mcp.squareup.com/sse> |
| [Zapier](https://zapier.com/mcp) | Automate workflows across thousands of apps via conversation | For the exact connector URL, visit: <https://mcp.zapier.com/> |

\*The Slack connector is currently available for Team and Enterprise plans only.

# Adding connectors to Claude

Before members of Team and Enterprise plans can use connectors, an Owner needs to enable it for the organization:

1. Navigate to [Admin settings > Connectors](https://claude.ai/admin-settings/connectors).
2. Click the "Browse connectors" button at the bottom of the page.
3. Select the connector from the list and click "Add to your team."
4. Individual users can now authenticate with the connector to start using it with Claude.

Pro and Max users, and individual Team and Enterprise users can add these connectors, or others, to Claude or Claude Desktop by following these steps:

1. Navigate to [Settings > Connectors](https://claude.ai/settings/connectors).
2. Find the connector in the list and click "Connect."
3. Authenticate with the connector to start using it with Claude.

**Note:** Once you've added a connector to your Claude account, you can authenticate with the tool and use it on Claude for iOS or Android.

See [Getting Started with Custom Connectors Using Remote MCP](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) for more details on how to add and use connectors.

---

Related Articles

[Getting Started with Custom Connectors Using Remote MCP](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)[Building Custom Connectors via Remote MCP Servers](https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers)[Anthropic Connectors Directory FAQ](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq)[Enabling and Using the Microsoft 365 Connector](https://support.claude.com/en/articles/12542951-enabling-and-using-the-microsoft-365-connector)[Remote MCP Server Submission Guide](https://support.claude.com/en/articles/12922490-remote-mcp-server-submission-guide)
