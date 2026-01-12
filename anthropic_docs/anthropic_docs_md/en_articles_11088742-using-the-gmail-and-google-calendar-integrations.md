# Using the Gmail and Google Calendar Integrations

**Source:** https://support.claude.com/en/articles/11088742-using-the-gmail-and-google-calendar-integrations

The Gmail and Google Calendar integrations are available for users on all paid Claude plans.

This article explains how to use Claude's Gmail and Google Calendar integrations after you've enabled them. With these integrations, Claude can search your emails and understand your calendar commitments so you can spend less time retrieving information, and more time on strategic work.

For more information on enabling these integrations, review the setup guide [here](https://support.anthropic.com/en/articles/10168395-setting-up-integrations-on-claude-ai).

**Note:** All Claude integrations are currently in beta.

# How to use the integrations

# 1. Ask a question that requires access to your Gmail or Calendar

Simply ask Claude a question that would require checking your emails or calendar. Claude will automatically detect that it needs to access these data sources and use the appropriate tool.

# 2. Review Claude's response

Claude will provide a response based on the information retrieved from your Gmail or Google Calendar. The response will include:

* A clear answer to your question
* Citations indicating which emails or calendar events were used as sources
* Links to the original sources when applicable

# 3. Follow up with clarifying questions

You can ask follow-up questions to get more specific information. For example:

* "Can you show me more details about that email?"
* "When is the next meeting on this topic?"
* "Who else was invited to that event?"

# Understanding citations

When Claude provides information from your Gmail or Calendar, it includes citations to indicate the source of the information. This helps you:

* See which specific emails or calendar events Claude used to answer your question.
* Follow links back to the original sources for more details.

# Privacy and data handling

* In order to use these integrations, you must [authenticate directly to your Google account first](https://support.anthropic.com/en/articles/10168395-setting-up-integrations-on-claude-ai).

  + Before individual users can authenticate to these integrations on Claude for Work (Team and Enterprise) plans, an Owner or Primary Owner must [enable them at the account level](https://support.anthropic.com/en/articles/10168395-setting-up-integrations-on-claude-ai).
* Claude can only access the Gmail and Calendar data for the Google account you've connected.
* Claude only accesses your Gmail and Calendar data when you explicitly ask a question requiring this information.
* Claude will only retrieve the minimum information needed to answer your question.
* Claude mirrors your existing permissions - you cannot access information you don't already have access to in Gmail or Calendar.
* Data retrieved while using integrations is stored in Anthropic servers, which is protected by Anthropic's security infrastructure (see more details in our [Trust Center](https://trust.anthropic.com/controls#organizational-security)). This data is retained with its associated chat, so you can delete any retrieved data by deleting the chat.
* We do not train our models on your Gmail or Calendar integration data, ensuring your private information remains private.

  + **Note**:If you are using our consumer products (e.g. Claude Free, Pro, and Max ( when using Claude Code with those accounts)) and you have chosen to allow us to use your chats and coding sessions for model training, then any content you copy/paste from your Gmail or Calendar or Claude's responses which include specific information from these integrations may be used to improve our models. [Learn more](https://privacy.anthropic.com/en/articles/10023580-is-my-data-used-for-model-training).

# Additional considerations

* These integrations currently do not support creating or modifying emails and calendar events.
* Claude cannot see images embedded in emails.

For more information on leveraging your Google Workspace with Claude, see our guide on [Using the Google Drive Integration](https://support.anthropic.com/en/articles/10166901-using-the-google-docs-integration).

---

Related Articles

[Using the Google Drive Integration](https://support.claude.com/en/articles/10166901-using-the-google-drive-integration)[Setting Up Claude Integrations](https://support.claude.com/en/articles/10168395-setting-up-claude-integrations)[Using Google Drive Cataloging on the Enterprise Plan](https://support.claude.com/en/articles/11088779-using-google-drive-cataloging-on-the-enterprise-plan)[Using Research on Claude](https://support.claude.com/en/articles/11088861-using-research-on-claude)[Using Research and Google Workspace](https://support.claude.com/en/articles/11101545-using-research-and-google-workspace)
