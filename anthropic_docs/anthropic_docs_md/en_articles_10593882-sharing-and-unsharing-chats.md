# Sharing and Unsharing Chats

**Source:** https://support.claude.com/en/articles/10593882-sharing-and-unsharing-chats

Learn how to create shareable links to your chats with Claude. While chats are always private by default, you can easily create snapshots of your conversations to share via direct link. This guide walks you through the process of sharing and unsharing chats.

# Sharing Chats

To share a chat:

1. Click the "Share" button in the upper right corner of your chat.
2. Click the "Share" button in the pop out to create a shareable link.

Once a chat has been shared, anyone with the link can view the chat snapshot. The chat snapshot includes all messages that were sent prior to sharing the chat, including any artifacts. All messages sent after sharing a chat will remain private by default. However, if you unshare the chat and share it again, the snapshot will be updated to include any new messages.

**Note:** Users on Team and Enterprise plans can only share chats with other members of the same organization, not publicly. Read more here: [Project visibility and sharing](https://support.claude.com/en/articles/9519189-project-visibility-and-sharing).

# Sharing Chats with Files or MCP Integrations

When sharing chats that include uploaded files or MCP (Model Context Protocol) integrations, it's important to understand what information is included in the shared snapshot.

**Attached files:** If you share a chat that contains an attached file, the file itself is not included in the shared snapshot and remains private. Only the conversation and Claude's responses will be visible to anyone with the link.

**MCP tool calls:** When sharing chats that use MCP integrations, the raw data retrieved from MCP tool calls remains hidden in the shared snapshot. Only the final chat output and conversation will be visible to viewers. The underlying tool call data stays private.

This ensures that sensitive information from your files and connected tools is protected, even when you share a chat snapshot.

# Unsharing Chats

To unshare a chat:

1. Navigate to the "Share" menu.
2. Click the visibility dropdown.
3. Change the chat from "Public" to "Private" to disable the direct link.

# Managing Shared Chats

Users on free, Pro, or Max plans can review a log of shared chats by navigating to [Settings > Privacy](https://claude.ai/settings/data-privacy-controls). Find the **Privacy settings** section and click “Manage” next to **Shared chats:**

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1921669913/7cc7be48cfc7a18f9f469d6cd83c/CleanShot+2026-01-08+at+10_20_43%402x.png?expires=1768003200&signature=1ff74efc71e02b0cb1096142eb5023fa0473991f2998fb0ec7e45b5a1b876996&req=dSklF894lIheWvMW3nq%2Bgf%2BHUFYVi9clr1%2FjKjOzfKabdL9CzYgKw6mpmtrW%0A4gs5ethY%2Fxwlwa4wH8W9d3a1mRo%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1921669913/7cc7be48cfc7a18f9f469d6cd83c/CleanShot+2026-01-08+at+10_20_43%402x.png?expires=1768003200&signature=1ff74efc71e02b0cb1096142eb5023fa0473991f2998fb0ec7e45b5a1b876996&req=dSklF894lIheWvMW3nq%2Bgf%2BHUFYVi9clr1%2FjKjOzfKabdL9CzYgKw6mpmtrW%0A4gs5ethY%2Fxwlwa4wH8W9d3a1mRo%3D%0A)

This will open a **Shared chats** modal listing the title, date shared, and link to each chat, allowing you to easily review and access all your previously-shared content. From here, you also have the option to click “Unshare” next to each listed chat to revoke access to the last snapshot you shared:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243810/e6fe1d262597446c7fe21dff9f10/AD_4nXdW-GhByF8uKV7fCq9lTbkVB91FglSL6TSyXAOUk_MLcTV9YsEMBMkm9rgm1oXqv0k3sJh1JhlzZP6tHVkKbDJJ71pDRRtM3aVNG64MDuKDIzgmknh-XDZdNa7biTsTdwGoPr5GRg?expires=1768003200&signature=a9b91f20d2b26975fae2873bb4ab5d7279fccf6b20a1961cb10216cd1b4a12ed&req=dSYlEst6noleWfMW3nq%2BgRse9HKpn%2BddxRXgQ8VJ8zfesFGhtMlYzMsG7MgL%0Ar0eun5hs4ewwcJ2J7XB2oSOcRRs%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243810/e6fe1d262597446c7fe21dff9f10/AD_4nXdW-GhByF8uKV7fCq9lTbkVB91FglSL6TSyXAOUk_MLcTV9YsEMBMkm9rgm1oXqv0k3sJh1JhlzZP6tHVkKbDJJ71pDRRtM3aVNG64MDuKDIzgmknh-XDZdNa7biTsTdwGoPr5GRg?expires=1768003200&signature=a9b91f20d2b26975fae2873bb4ab5d7279fccf6b20a1961cb10216cd1b4a12ed&req=dSYlEst6noleWfMW3nq%2BgRse9HKpn%2BddxRXgQ8VJ8zfesFGhtMlYzMsG7MgL%0Ar0eun5hs4ewwcJ2J7XB2oSOcRRs%3D%0A)

If you don’t have any shared chat snapshots, the **Shared chats** modal will show “No shared content found”:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243808/b025db8e598f0c88fb16d83d48d5/AD_4nXeUwCKnmFzzrjMHhfr5By4zk5pJlkEn3wbJ8-aNfu13Yl99IjBywpqPx9G07QRzpH1EwRY7uG7Q9m9fib98Gql1cIV7XwUCTzEgBNu79Ey8tCOS5CEVmwveIcEOxJ4fonBhe3g9MA?expires=1768003200&signature=31e40834908298a9e189e35b2391e9a9071e04aaa724234c1ecfe65281384b92&req=dSYlEst6nolfUfMW3nq%2BgX8ECo7kypOfI77rJPHbnxr43W9URT02KoyjcurO%0A8DYCN0DInLIwRDSTc8tR22RYRPo%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243808/b025db8e598f0c88fb16d83d48d5/AD_4nXeUwCKnmFzzrjMHhfr5By4zk5pJlkEn3wbJ8-aNfu13Yl99IjBywpqPx9G07QRzpH1EwRY7uG7Q9m9fib98Gql1cIV7XwUCTzEgBNu79Ey8tCOS5CEVmwveIcEOxJ4fonBhe3g9MA?expires=1768003200&signature=31e40834908298a9e189e35b2391e9a9071e04aaa724234c1ecfe65281384b92&req=dSYlEst6nolfUfMW3nq%2BgX8ECo7kypOfI77rJPHbnxr43W9URT02KoyjcurO%0A8DYCN0DInLIwRDSTc8tR22RYRPo%3D%0A)

---

Related Articles

[What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)[Project visibility and sharing](https://support.claude.com/en/articles/9519189-project-visibility-and-sharing)[Discovering, publishing, customizing, and sharing artifacts](https://support.claude.com/en/articles/9547008-discovering-publishing-customizing-and-sharing-artifacts)[Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)[Anthropic Connectors Directory FAQ](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq)
