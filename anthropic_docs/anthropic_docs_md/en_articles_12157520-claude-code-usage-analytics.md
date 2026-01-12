# Claude Code Usage Analytics

**Source:** https://support.claude.com/en/articles/12157520-claude-code-usage-analytics

Usage analytics for Claude Code are currently available to Team and Enterprise plan Owners assigned to premium seats, and API Console users (Admin, Billing, and Developer roles). See [Analytics](https://code.claude.com/docs/en/analytics) in our Claude Code docs for more information.

This feature allows Console users and Owners of Team and Enterprise plans to monitor how their organization uses Claude Code, tracking productivity metrics and adoption patterns across teams.

# Accessing Claude Code analytics

# Team and Enterprise Owners

1. Log in to your Owner or Primary Owner account.
2. Click your initials or name in the lower left corner.
3. Navigate to [Admin settings > Claude Code](https://claude.ai/admin-settings/claude-code) to view **Usage**.

# API Console users

1. Log in to your [Claude Console account](https://platform.claude.com).
2. Expand the left side panel.
3. Click “Claude Code” under **Analytics**.
4. View Claude Code usage analytics on [Settings > Claude Code](https://platform.claude.com/claude-code).

# Available metrics

The Claude Code Usage page displays the following metrics for your organization:

# Organization-level metrics

* **Lines of code accepted**: Total lines of code your team has accepted from Claude Code suggestions.
* **Suggestion accept rate**: Percentage of Claude Code suggestions that your team accepts.
* **Activity trends**: Daily view of active users and sessions over time.
* **Lines accepted over time**: Daily breakdown of accepted code lines.

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1717579277/46c512f4b3ed05c359cecd78ed5c/e0ce2c19-39e2-411f-9a1f-cb1d46439a42?expires=1767997800&signature=c5d11044dbce204e69f43d395fdc91c66ba2f89f8c6ad318c19774c0a34d3e0a&req=dScmEcx5lINYXvMW1HO4zfiEMaFZhn7GCX9h5MbdDjN6nmJrjUMaEEh%2Fi3%2B0%0AMsTzLR6zdjqzphG1%2BuE%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1717579277/46c512f4b3ed05c359cecd78ed5c/e0ce2c19-39e2-411f-9a1f-cb1d46439a42?expires=1767997800&signature=c5d11044dbce204e69f43d395fdc91c66ba2f89f8c6ad318c19774c0a34d3e0a&req=dScmEcx5lINYXvMW1HO4zfiEMaFZhn7GCX9h5MbdDjN6nmJrjUMaEEh%2Fi3%2B0%0AMsTzLR6zdjqzphG1%2BuE%3D%0A)

# User-level metrics

**Individual usage**: View each team member's email address and their total lines of code accepted for the current month. You can search for specific users or click the “Export” button to generate a CSV of members’ email addresses and total lines of code.

# Understanding the metrics

**Lines of code accepted** measures the actual code your team incorporates into their work from Claude Code suggestions, helping you understand the tool's practical impact on development productivity.

**Suggestion accept rate** indicates how relevant and useful Claude Code's suggestions are for your team's specific coding needs and practices.

**Activity trends** show adoption patterns and help identify peak usage periods, allowing you to understand how Claude Code fits into your team's workflow.

# Data reset and availability

Usage metrics display data for the current calendar month and reset at the beginning of each month. Historical data visualization shows daily granularity for tracking trends over time.

# Using analytics to optimize Claude Code adoption

Review your organization's code acceptance rate to understand if teams are finding Claude Code's suggestions valuable. If rates are lower than expected, consider providing additional training on effective prompting techniques.

Monitor individual usage patterns to identify power users who can share best practices with the broader team, or to spot team members who might benefit from additional support.

Track activity trends to understand when your team uses Claude Code most effectively and ensure adequate seat allocation during peak periods.

# FAQs

# I'm using an individual paid plan; how can I access usage analytics for Claude Code?

Claude Code usage analytics are not available to individual Pro or Max plans at this time.

# I'm looking for specific user but they're missing from the reports.

If you notice that a specific user isn't showing up in your analytics, you should have them update Claude Code to the most recent version. The first Claude Code version to support this feature is **version 2.0.28**, so users should run `claude update` to manually update Claude Code if needed.

---

Related Articles

[Claude Console Roles and Permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions)[Using Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)[Using Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan)[Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)[Usage Analytics for Enterprise Plans](https://support.claude.com/en/articles/12883420-usage-analytics-for-enterprise-plans)
