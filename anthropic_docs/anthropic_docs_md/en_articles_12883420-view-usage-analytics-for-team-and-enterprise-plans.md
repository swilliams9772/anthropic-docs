# View usage analytics for Team and Enterprise plans

**Source:** https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans

This article explains how to view and export usage analytics for your organization.

Usage analytics are available to Team plan Owners and Primary Owners, and Enterprise plan Owners, Primary Owners, and Admins. Enterprise Admins can view all analytics except Spend.

Usage analytics help you track team activity, feature adoption, and spend directly from your admin dashboard. You can monitor how your organization uses Claude and export detailed reports for your own analysis.

Primary Owners and Owners can access analytics via dedicated Analytics settings by clicking your initials in the lower left corner and selecting **[Analytics](https://claude.ai/analytics/activity)** from the menu. Additionally, the Claude.ai, Claude Code, and Cowork options offer product-specific analytics.

---

# All activity

This page includes the following analytics:

# Usage

* Weekly active users (WAU)
* Utilization rates (WAU / total seats)
* Pending invites
* Daily, weekly, and monthly active users, with filters for Claude (chat), Claude Code, and Claude Cowork
* Top connectors

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2153394909/693f3ae0ec2ea158a1f1e233c024/CleanShot+2026-03-11+at+14_52_44%402x.png?expires=1779557400&signature=b499b2f3c0000ab076bdde55f69d980f8118de04f14ef7ca5a301706a0d33b11&req=diEiFcp3mYhfUPMW1HO4zbQxH8o0CiVmSPAYazQ9kuI%2BzGCnEqs5Oy2XMzu0%0A%2B49Z1uePB4Y4OkNPQnc%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2153394909/693f3ae0ec2ea158a1f1e233c024/CleanShot+2026-03-11+at+14_52_44%402x.png?expires=1779557400&signature=b499b2f3c0000ab076bdde55f69d980f8118de04f14ef7ca5a301706a0d33b11&req=diEiFcp3mYhfUPMW1HO4zbQxH8o0CiVmSPAYazQ9kuI%2BzGCnEqs5Oy2XMzu0%0A%2B49Z1uePB4Y4OkNPQnc%3D%0A)

# Spend

**Note:** If you're on a **[seat-based Enterprise plan](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans#h_6a78e30e26)**, spend reports only appear if your organization has **[enabled usage credits](https://support.claude.com/en/articles/12005970-)**. The spend data covers overage spend only—usage within seat-based allotments isn't included.

This section includes the following analytics:

* Total spend (month-to-date, quarter-to-date, year-to-date)
* Spend by model (1 month, 3 months, 1 year)
* Top 10 users by spend leaderboard

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2153417518/03accc4372c7fd4582e6c3978d9d/CleanShot%2B2026-03-11%2Bat%2B15_02_52-402x.png?expires=1779557400&signature=620ec5987b10ee6b3a7230ecac2d1139418367d93b6e40bf13f413fdda6c8089&req=diEiFc1%2FmoReUfMW1HO4zdUtwHUCPSpKuwPrchh43Ep1VHKDUaCC%2Frm8dZPo%0ARNRv9E%2Bf%2BQY04GtM0t0%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2153417518/03accc4372c7fd4582e6c3978d9d/CleanShot%2B2026-03-11%2Bat%2B15_02_52-402x.png?expires=1779557400&signature=620ec5987b10ee6b3a7230ecac2d1139418367d93b6e40bf13f413fdda6c8089&req=diEiFc1%2FmoReUfMW1HO4zdUtwHUCPSpKuwPrchh43Ep1VHKDUaCC%2Frm8dZPo%0ARNRv9E%2Bf%2BQY04GtM0t0%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2153419527/18cba69667e2af1a6f4f2e5ca2c5/CleanShot+2026-03-11+at+15_03_28%402x.png?expires=1779557400&signature=78ec8eaa2cf9605c2e31103cf36e3bf21d929f6cfa774ec0c107bb808d1a1b27&req=diEiFc1%2FlIRdXvMW1HO4zdGt9S2tDvhtP9LVpsbj5NdPGdSujcXJjteRd6WN%0Arg80h%2BoK2KfEF%2BmefOI%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2153419527/18cba69667e2af1a6f4f2e5ca2c5/CleanShot+2026-03-11+at+15_03_28%402x.png?expires=1779557400&signature=78ec8eaa2cf9605c2e31103cf36e3bf21d929f6cfa774ec0c107bb808d1a1b27&req=diEiFc1%2FlIRdXvMW1HO4zdGt9S2tDvhtP9LVpsbj5NdPGdSujcXJjteRd6WN%0Arg80h%2BoK2KfEF%2BmefOI%3D%0A)

**Note:** The spend leaderboard can be delayed by one to two days. For more current month-to-date spend per user, refer to spend limits by person in **[Organization settings > Usage](https://claude.ai/admin-settings/usage)**.

# Export a spend report

You can export a detailed cost and usage report as a CSV file. The report provides per-user, per-model visibility into token usage and estimated spend within a selected time period, updated daily.

To export spend data:

1. Navigate to **[Settings > Analytics](https://claude.ai/analytics/activity)**.
2. Scroll down to the **Spend** section.
3. Click the "Export Spend Report" button.
4. Select a time period: MTD, Last Month, Last 90 Days, or Custom.
5. If you select "Custom," choose your start and end dates. You can go back up to 90 days, and the most recent data available is from yesterday.
6. Click "Download."

# What's included in the report?

Each row in the CSV represents a specific person's usage of a specific model, with spend summed across the entire date range selected for the export. The report includes the following fields:

* User's email
* Account UUID
* Product (such as Chat, Claude Code, Cowork, or Office Agents)

  + Office Agents aggregates usage from the Claude add-ins for Excel, PowerPoint, and Word.
* Model and model family
* Request count (`total_requests`)

  + The count of individual API calls made to Claude. Each time an app or user sends a message and gets a response, that counts as a request.
* Prompt tokens (`total_prompt_tokens`)

  + The number of tokens consumed by the input side of each request. This includes system prompts, conversation history, user messages, tool definitions, etc.
* Completion tokens (`total_completion_tokens`)

  + The number of tokens generated by Claude when it responds*,* including extended thinking tokens.
* Net spend (`total_net_spend_usd`)

  + Your cost (in USD) after any discounts, credits, or negotiated rates are applied. This is what you actually spent.
* Gross spend (`total_gross_spend_usd`)

  + Your cost (in USD) before any discounts or credits.

**Important:** Spend data refreshes daily and has a one-day delay. For usage-based Enterprise plans, the export captures your organization's full usage. For seat-based Enterprise plans with usage credits enabled, **the export only reflects spend that exceeds your seat allotment.**

---

# Claude.ai

Navigate to **[Analytics > Claude.ai](https://claude.ai/analytics/usage)** to view usage and activity metrics for your organization. This page includes the following analytics:

# Chats

* Chats per day
* Percentage of users with 1 or more chat
* Total number of chats (1 week, 1 month, 3 months, 1 year)

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916169034/e3e557f223fcd6976fa5b6353095/CleanShot+2026-01-05+at+15_32_41.png?expires=1779557400&signature=604d94599cb6dc2ef800ce02562e136f3059ee2b78985b26c1371b6658b71fc2&req=dSkmEMh4lIFcXfMW1HO4zZyh%2Bjqb%2B45%2FRyyyIe2wZ0V6%2BI2lfAapXRUs%2BDNE%0AN08ndtRxXxQlf6UfOGo%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916169034/e3e557f223fcd6976fa5b6353095/CleanShot+2026-01-05+at+15_32_41.png?expires=1779557400&signature=604d94599cb6dc2ef800ce02562e136f3059ee2b78985b26c1371b6658b71fc2&req=dSkmEMh4lIFcXfMW1HO4zZyh%2Bjqb%2B45%2FRyyyIe2wZ0V6%2BI2lfAapXRUs%2BDNE%0AN08ndtRxXxQlf6UfOGo%3D%0A)

# Projects

* Projects created per day
* Percentage of users with 1 or more project
* Top 10 users by projects used (month-to-date, quarter-to-date, year-to-date, 1 year)

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916170133/666961061f9a044385e0ea1debdd/CleanShot+2026-01-05+at+15_36_27.png?expires=1779557400&signature=fde47b3a4b373c34672a7f26934f23b39486b6c2fa88c82e278665bc6aeadb6a&req=dSkmEMh5nYBcWvMW1HO4zed15S3r2B9eqVPXIl8sPearD%2FhrOEu22rVL7evo%0AlEd8eu3%2FdgXXGpDdbE0%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916170133/666961061f9a044385e0ea1debdd/CleanShot+2026-01-05+at+15_36_27.png?expires=1779557400&signature=fde47b3a4b373c34672a7f26934f23b39486b6c2fa88c82e278665bc6aeadb6a&req=dSkmEMh5nYBcWvMW1HO4zed15S3r2B9eqVPXIl8sPearD%2FhrOEu22rVL7evo%0AlEd8eu3%2FdgXXGpDdbE0%3D%0A)

# Artifacts

* Artifacts created per day
* Percentage of users with 1 or more artifact
* Top 10 users by artifacts generated (month-to-date, quarter-to-date, year-to-date, 1 year)

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916171160/cd17d2abba34659b9d8f6231df5a/CleanShot+2026-01-05+at+15_37_20.png?expires=1779557400&signature=e67627d3c82861e54ceb64fc63c3352ca8153e693ff8fe825f475376c9900913&req=dSkmEMh5nIBZWfMW1HO4zXYF3lDnuAf94Jgm1Axxim25dW4hlTJVmkcbcVJO%0A7lcmN9UdqIt9LOTqEl8%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916171160/cd17d2abba34659b9d8f6231df5a/CleanShot+2026-01-05+at+15_37_20.png?expires=1779557400&signature=e67627d3c82861e54ceb64fc63c3352ca8153e693ff8fe825f475376c9900913&req=dSkmEMh5nIBZWfMW1HO4zXYF3lDnuAf94Jgm1Axxim25dW4hlTJVmkcbcVJO%0A7lcmN9UdqIt9LOTqEl8%3D%0A)

---

# Claude Code analytics

Navigate to **[Analytics > Claude Code](https://claude.ai/analytics/claude-code)** to view usage and activity metrics for your organization. For more specific details, refer to **[Claude Code usage analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)**.

---

# Claude Cowork analytics

Navigate to **[Analytics > Cowork](https://claude.ai/analytics/cowork)** to view usage and activity metrics for Claude Cowork across your organization. This page includes:

* Cowork sessions per day
* Percentage of users with one or more Cowork sessions
* Daily, weekly, and monthly active Cowork users

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2253604219/0d21918d55e10b3e5d2a92e65c90/42a47632-08c2-4557-a087-fc080c4dda80?expires=1779557400&signature=a297e5d6f7c46891601561f37987c5c7017cdbdbd8aa9644d89dc25d669d640c&req=diIiFc9%2BmYNeUPMW1HO4zSCqqK0CEXga8zs2pRdG0k6Td4Q32tAPUzdpzH%2Bu%0AyoYZc9DujBMnDapZVeE%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2253604219/0d21918d55e10b3e5d2a92e65c90/42a47632-08c2-4557-a087-fc080c4dda80?expires=1779557400&signature=a297e5d6f7c46891601561f37987c5c7017cdbdbd8aa9644d89dc25d669d640c&req=diIiFc9%2BmYNeUPMW1HO4zSCqqK0CEXga8zs2pRdG0k6Td4Q32tAPUzdpzH%2Bu%0AyoYZc9DujBMnDapZVeE%3D%0A)

**Note:** Cowork analytics are available alongside Chat and Claude Code data in the **[Analytics API](https://support.claude.com/en/articles/13694757-access-engagement-and-adoption-data-with-the-analytics-api)**.

---

# Access your analytics data programmatically

If you’re on an Enterprise plan and want to pull analytics data into your own dashboards or reporting tools, the Analytics API gives you programmatic access to the same usage and engagement metrics available in the analytics dashboard. To get started, refer to **[Access usage data with the Analytics API](https://support.claude.com/en/articles/13694757-access-usage-data-with-the-analytics-api)**.

---

Related Articles

[What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)[Manage usage credits for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans)[Get started with the Claude Enterprise Analytics API](https://support.claude.com/en/articles/13694757-get-started-with-the-claude-enterprise-analytics-api)[Use analytics chat to ask Claude about usage](https://support.claude.com/en/articles/14729354-use-analytics-chat-to-ask-claude-about-usage)
