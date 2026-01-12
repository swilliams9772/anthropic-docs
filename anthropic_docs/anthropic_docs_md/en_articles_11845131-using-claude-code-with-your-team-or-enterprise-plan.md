# Using Claude Code with your Team or Enterprise plan

**Source:** https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan

Claude Code is only available to members of Team and Enterprise organizations assigned to premium seats.

# What is Claude Code?

Claude Code is a command line tool that gives you access to Claude models directly in your terminal, allowing you to delegate complex coding tasks while maintaining transparency and control. With premium seats on Team and Enterprise plans, you can access Claude on the web, desktop, and mobile apps, plus Claude Code in your terminal with one unified subscription.

# Why use Claude and Claude Code?

Combine two powerful AI products in one unified subscription:

* Use Claude for writing, research, analysis, and collaboration across teams.
* Use Claude Code for terminal-based coding workflows and development tasks.

# How to connect Claude Code to your Team or Enterprise plan

# Step 1: Purchase premium seats

Team or Enterprise plan Owners can [purchase premium seats](https://support.claude.com/en/articles/12004354-how-to-purchase-and-manage-premium-seats) that include Claude Code access and manage seat allocation in [Admin settings > Organization](https://claude.ai/admin-settings/organization).

# Step 2: Download and install Claude Code

**Note:** If you already have Claude Code installed on your computer, proceed to Step 3.

1. Once you have Claude Code access via a premium seat, visit the [Claude Code page](https://claude.com/product/claude-code).
2. Click the link to install [Node.js 18+](https://nodejs.org/en/download).
3. Open your terminal, then run: `npm install -g @anthropic-ai/claude-code`

# Step 3: Authenticate with the Team or Enterprise account tied to the premium seat

1. Type `claude` within your Terminal window to start a Claude Code session.
2. When prompted during setup or first use, select a login method.

   1. If you're already logged in to Claude Code via a different account, run /login to select a different login method.
3. Select “Claude account with subscription” to be routed to an OAuth prompt.
4. Select your Team or Enterprise plan and click “Authorize.”
5. Your premium seat subscription will be linked to Claude Code.

# Having trouble using your Team or Enterprise account to access Claude Code?

If you're not seeing the option to authenticate with your preferred account, follow these steps to update Claude Code:

1. Log out of your active session completely using the `/logout` command.
2. Run `claude update`.
3. Restart your terminal completely for the change to take effect.
4. Run `claude` and select the correct account to use Claude Code.

# How do usage limits work?

**Team plan members with premium seats:**

Opus 4.5 is now your default model.

**Enterprise plan members with premium seats:**

Opus 4.5 is now available. Opus 4.5 consumes your weekly limit faster than Sonnet, so we recommend Sonnet 4.5 for everyday use.

Premium seats include enhanced usage limits compared to standard seats. Note that usage is tracked across both Claude Code and Claude (on the web, desktop, and mobile).

# For Team plans

Average users can send approximately 225 messages with Claude every five hours, and have weekly usage limits of 50-95 hours of Sonnet 4 usage and 3-7 hours of Opus 4 usage. This will vary based on factors such as codebase size and user settings like auto-accept mode. Heavy Opus users with large codebases or those running multiple Claude Code instances in parallel will hit their limits sooner.

# For Enterprise plans

If you’re on an Enterprise plan and looking for more specific information about usage limits, please reach out to your Account Manager or [our Sales team](https://www.claude.com/contact-sales).

# What happens when you hit usage limits

Your Team or Enterprise organization can enable extra usage to allow team members on all seat types to continue working with Claude and Claude Code after reaching their included usage limits. See this article for more information: [Extra Usage for Claude for Work (Team and Enterprise) Plans](https://support.claude.com/en/articles/12005970-extra-usage-for-claude-for-work-team-and-enterprise-plans).

---

Related Articles

[About Team and Enterprise Plan Usage](https://support.claude.com/en/articles/9267304-about-team-and-enterprise-plan-usage)[What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)[Using Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)[Claude Code Model Configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)[Extra Usage for Team and Enterprise Plans](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-enterprise-plans)
