# Using Google Drive Cataloging on the Enterprise Plan

**Source:** https://support.claude.com/en/articles/11088779-using-google-drive-cataloging-on-the-enterprise-plan

Google Drive Cataloging is available to users on the Claude Enterprise plan.

Enterprise users can catalog their Google Drive content\* with RAG (Retrieval Augmented Generation) Search. This system works by first indexing the content of your Google Drive, and then using that index to match queries to results. With this setting enabled, Claude will provide accurate contextual responses based on your indexed documents, and will provide direct citations to the relevant sources.

*\*Supported file types:* Google Docs (text extraction only, up to 10MB).

# Enabling Google Drive Cataloging

Before individual users can start using indexed content from their Drive, an Owner or Primary Owner must enable the feature at the account level. To enable:

1. Navigate to [Settings > Integrations](https://claude.ai/settings/integrations)
2. Toggle to “Organization integrations” at the top of the page
3. Locate “Google Drive cataloging”
4. Click Enable and follow the instructions to authenticate

**For Individual Users:**

Once the global setting has been turned on, individual users can toggle Google Drive search on from the chat interface:

1. Click on the slider icon in the chat interface
2. Toggle “Drive search” on

   * *Note:* If this is your first time using the integration, you will be redirected to Google to authenticate

# After Enabling

Once enabled, Claude will index your Google Docs and leverage that index during your conversations to provide relevant context and citations in his responses.

Periodically Claude will re-index documents that have changed and de-index documents that have been deleted. It may take several hours for Claude to recognize that a document has been updated or deleted.

# Privacy & Security

This infrastructure builds upon and augments the Claude for Work security infrastructure:

* Data retrieved while using integrations is stored in Anthropic servers, which is protected by Anthropic's security infrastructure (see more details in our [Trust Center](https://trust.anthropic.com/controls#organizational-security)). This data is retained with its associated chat, so you can delete any retrieved data by deleting the chat.
* Data is encrypted at rest and in transit using Google’s managed encryption services
* Each user has access to their protected index:

  + This index fully respects access controls and underlying user level permissions
  + Each user can only access their own index
* All document edits, deletions, and access changes are propagated promptly

---

Related Articles

[Can you delete data that I sent via Team and Enterprise plans?](https://support.claude.com/en/articles/9796617-can-you-delete-data-that-i-sent-via-team-and-enterprise-plans)[Using the Google Drive Integration](https://support.claude.com/en/articles/10166901-using-the-google-drive-integration)[Using the Gmail and Google Calendar Integrations](https://support.claude.com/en/articles/11088742-using-the-gmail-and-google-calendar-integrations)[Getting Started with Claude for Education at Your University (for Owners/Admins)](https://support.claude.com/en/articles/11139094-getting-started-with-claude-for-education-at-your-university-for-owners-admins)[Using Enterprise Search](https://support.claude.com/en/articles/12489464-using-enterprise-search)
