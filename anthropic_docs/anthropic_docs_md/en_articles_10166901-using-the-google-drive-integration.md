# Using the Google Drive Integration

**Source:** https://support.claude.com/en/articles/10166901-using-the-google-drive-integration

The Google Drive integration is currently available to users on paid Claude.ai plans. For more information on enabling Google Drive within your account, read [Setting Up Integrations on Claude.ai](https://intercom.help/anthropic-6f71807d7c3e/en/articles/10168395-setting-up-integrations-on-claude-ai).

Connect your Google Docs directly to Claude using the Google Drive integration. Easily add Google Docs by pasting URLs or selecting from your recent documents, helping Claude better understand and assist with your tasks.

# How to add Google Docs

# Chats

1. Click the plus sign in the chat interface.
2. Select the "Add from Google Drive" option.

   1. *Note: If this is your first time using the integration, you will be redirected to Google to authenticate.*
3. Search through your recently accessed documents or paste the document’s URL.
4. When you send your message, Claude will access and process the document to inform its response:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1608125708/5bf70727b4bae6f021630a1ade3a/image+%286%29.png?expires=1767997800&signature=1ca71d0d781021da332f9cee611c40cc0d5ebd281bdb59a45dc90acb9afc52db&req=dSYnHsh8mIZfUfMW1HO4zexw%2BurewlDkHtWhqjkZhkt6I8HLC5vVbuIFSsU2%0AD0YCJcsR0BMW80XBs%2BY%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1608125708/5bf70727b4bae6f021630a1ade3a/image+%286%29.png?expires=1767997800&signature=1ca71d0d781021da332f9cee611c40cc0d5ebd281bdb59a45dc90acb9afc52db&req=dSYnHsh8mIZfUfMW1HO4zexw%2BurewlDkHtWhqjkZhkt6I8HLC5vVbuIFSsU2%0AD0YCJcsR0BMW80XBs%2BY%3D%0A)

# Projects

The Google Drive integration is only available in private projects.

1. Click on “Add Content” in your project knowledge.
2. Select “Google Drive.”

   * *Note: If this is your first time using the integration, you will be redirected to Google to authenticate.*
3. Search through your recently accessed documents or paste the document’s URL.
4. Your document will be added to your project knowledge for Claude to access and process when chatting in that project:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1259913573/0929010908a4f8ff0ebfe5255834/AD_4nXcpDfDzY3xbFJoAMCRWW_nA4wvZ9ohhe-oafptd44TOdxUqUL9JOhWZdq-1SVKbCzmDyayn6-fiQhmqFxVbjV0888oC6u8gIwPLRzkHPhEd3XmCaB68d_WBFgOta9hwYksrPjpMVA?expires=1767997800&signature=962708f82b18ba17ddd99f539217c7f2bbf2d72ca1dd084f777e41b6177ed831&req=dSIiH8B%2FnoRYWvMW1HO4zddl7ZXjJYYin%2B2RKjzEHtnuCdht9zeoM98wx3xX%0AI4LoSya35fwAHTM0dJI%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1259913573/0929010908a4f8ff0ebfe5255834/AD_4nXcpDfDzY3xbFJoAMCRWW_nA4wvZ9ohhe-oafptd44TOdxUqUL9JOhWZdq-1SVKbCzmDyayn6-fiQhmqFxVbjV0888oC6u8gIwPLRzkHPhEd3XmCaB68d_WBFgOta9hwYksrPjpMVA?expires=1767997800&signature=962708f82b18ba17ddd99f539217c7f2bbf2d72ca1dd084f777e41b6177ed831&req=dSIiH8B%2FnoRYWvMW1HO4zddl7ZXjJYYin%2B2RKjzEHtnuCdht9zeoM98wx3xX%0AI4LoSya35fwAHTM0dJI%3D%0A)

# Important Notes

* Supported file types: Google Docs (up to 10MB, text extraction only - Claude cannot interpret images in synced Google Docs).

  + *Tip: .docx files are not currently supported with this integration, but you can convert them to Google Docs by opening them in Docs, clicking "File", and selecting "Save as Google Docs."*
* You can only sync documents that you have permission to view in Google Drive.
* Google Docs added to chats and Project knowledge are synced directly from Google Drive, ensuring you're always working with the latest version.

# Frequently Asked Questions

**Q: What happens if I update my Google Doc after adding it to a chat?**

A: Once a document is added to a chat, it will continue to sync with the most up to date version in Google Drive.

**Q: Can I add multiple Google Docs to a single chat?**

A: Yes, you can add multiple Google Docs to provide Claude with comprehensive context for your discussion. The documents must fit within the conversation’s context window.

**Q: What happens if I lose access to a document?**

A: If you lose access to a document, you won't be able to view its contents in conversations where it was previously added. The document preview will be removed, though the conversation history will be maintained.

**Q: Does Claude have access to images, comments or suggestions on a Google Doc?**

A: No, when documents are uploaded, Claude only extracts the main text content and cannot see additional features like images, comments, or suggestions.

**Q: Can I add Google Sheets or Slides with the Google Drive integration?**

A: At the moment, we only support connecting to Google Docs via the Google Drive integration.

# Troubleshooting Steps

For the error, "Please try again. You may need to reconnect with your Google Drive account", try the following steps:

1. Navigate to [Settings > Integrations](https://claude.ai/settings/integrations).
2. In the “Integrations” section, find “Google Drive.”
3. Click the more button (...) next to Google Drive, then “Disconnect.”
4. After disconnecting, the next time you click the Google Drive icon in your chat menu, you will be redirected to Google to authenticate.

If you're still having trouble, you may need to disconnect from your Google Drive settings (<https://myaccount.google.com/connections>). Search for "Claude for Google Drive", click into the settings and choose "Delete all connections you have with Claude for Google Drive."

Please note that all Claude.ai integrations are currently in beta.

---

Related Articles

[Using the GitHub Integration](https://support.claude.com/en/articles/10167454-using-the-github-integration)[Setting Up Claude Integrations](https://support.claude.com/en/articles/10168395-setting-up-claude-integrations)[Using the Google Docs integration](https://support.claude.com/en/articles/10389539-using-the-google-docs-integration)[Using Google Drive Cataloging on the Enterprise Plan](https://support.claude.com/en/articles/11088779-using-google-drive-cataloging-on-the-enterprise-plan)[FAQs on Using Claude for Education at Your University](https://support.claude.com/en/articles/11139144-faqs-on-using-claude-for-education-at-your-university)
