# Enabling and using the desktop extension allowlist

**Source:** https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist

The desktop extension allowlist is available for Owners of Team and Enterprise plans.

This article introduces a desktop extension allowlist that Team and Enterprise plan Owners can use to manage their organization’s access to extensions.

# How to enable the allowlist

**Important:** If you’ve previously configured Enterprise policy controls at the user-machine level, these will override the in-app allowlist. Ensure both `isDesktopExtensionDirectoryEnabled` and `isDesktopExtensionEnabled` are not set to "false" so the allowlist can populate the available registry. Refer to our [desktop enterprise configuration documentation](https://support.claude.com/en/articles/12622667-enterprise-configuration) for more information.

The desktop extension allowlist is disabled by default, so an organization Owner will need to switch it on manually. Note that **users will be able to access all desktop extensions in the registry until you enable the allowlist.** To prevent this, ensure you activate the allowlist to block all desktop extensions by default, then add only the extensions your team needs access to.

**To turn on the allowlist:**

1. Open Claude Desktop
2. Click your initials or name in the lower left corner
3. Navigate to Admin settings > Connectors
4. Switch to the "Desktop" tab:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755172/63c92550571842577ad435860ec5/6f5cc4e1-ff7d-48de-863a-c4e6184d4605?expires=1767998700&signature=81a5291ac9a5862db226d1ada573ba2c45ad02b8f7ba3360f7102f5079d440ce&req=dScvF857mIBYW%2FMW1HO4zQ9pU00D9njc0ugSQm1MFW8tnyCGoVapVx%2Fty4IX%0A3WLG%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755172/63c92550571842577ad435860ec5/6f5cc4e1-ff7d-48de-863a-c4e6184d4605?expires=1767998700&signature=81a5291ac9a5862db226d1ada573ba2c45ad02b8f7ba3360f7102f5079d440ce&req=dScvF857mIBYW%2FMW1HO4zQ9pU00D9njc0ugSQm1MFW8tnyCGoVapVx%2Fty4IX%0A3WLG%0A)
5. Toggle **Allowlist** on:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755578/a6bafff5f084dc86ae463703fd3d/6cf0ee18-4e71-4129-98e8-cc08174e3c3a?expires=1767998700&signature=865bf6f222e490d3ddf720c27db90f25c8a51f96d56c52004aa7dc176b35127c&req=dScvF857mIRYUfMW1HO4zaj0CnYiQK8DTAorLxpdoc8AAM7Xkmg%2Bh55c4MBq%0AtV4n%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755578/a6bafff5f084dc86ae463703fd3d/6cf0ee18-4e71-4129-98e8-cc08174e3c3a?expires=1767998700&signature=865bf6f222e490d3ddf720c27db90f25c8a51f96d56c52004aa7dc176b35127c&req=dScvF857mIRYUfMW1HO4zaj0CnYiQK8DTAorLxpdoc8AAM7Xkmg%2Bh55c4MBq%0AtV4n%0A)

# What happens after enabling the allowlist?

Once the allowlist is enabled:

* Any existing desktop extension installations will be force-deleted from Claude Desktop clients.
* Users will no longer be able to install new desktop extensions that are not included within the allowlist.
* Users can only download extensions from the sanctioned in-app registry; they can no longer drag or click to install MCPBs.

Note that the allowlist does not guard against individuals tampering with local MCP file contents after installation.

Consider completing the allowlist setup during off-hours to minimize disruption to existing users. If a user's installed extension is deleted while the allowlist is being configured, they will need to manually re-install the extension.

**Important:** The allowlist requires Claude Desktop version 0.13.91 or higher, so users should update the desktop app by clicking “Claude”, then either “Check for updates” or “Restart to update to Claude 0.13.91”:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781756960/ad18af50c83d35f2673656c23e00/a7ee450f-0c7d-42d6-a75f-fb1bc088cb52?expires=1767998700&signature=c0065b6c8ff12e537cd564d9ad978cbae22289b6a280a39aec368ec58bc53366&req=dScvF857m4hZWfMW1HO4zYUJp4SjAzrsCEDZ5AdBjIaiddT5S6B529fooyTo%0AeWCkgdMavME2Yv%2FmDpo%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781756960/ad18af50c83d35f2673656c23e00/a7ee450f-0c7d-42d6-a75f-fb1bc088cb52?expires=1767998700&signature=c0065b6c8ff12e537cd564d9ad978cbae22289b6a280a39aec368ec58bc53366&req=dScvF857m4hZWfMW1HO4zYUJp4SjAzrsCEDZ5AdBjIaiddT5S6B529fooyTo%0AeWCkgdMavME2Yv%2FmDpo%3D%0A)

# Managing allowed extensions

After enabling the allowlist, you can choose which extensions to allow:

1. Navigate to Admin settings > Connectors and select the “Desktop” tab.
2. Click “Browse extensions” to view the list of available extensions.
3. Select the extension you want to add.
4. Click the “Add to your team” button.
5. The extension will appear in your allowlist.

If you want to remove an extension from the allowlist, click the “...” button and “Remove from allowlist.”

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781751250/6558c0f59aea7976bd44b0213d76/e750f02b-cd0d-437e-a83f-9ac362cdf456?expires=1767998700&signature=b614a4b0add5f0dea57e8d2c4059bd68a1c6b93db73dd009c2488118327d9662&req=dScvF857nINaWfMW1HO4zTrxC68g9l%2BSqXridZhfx1K78NztDnKmfd9Ji%2B1Q%0AFqF42CnM8d3lBfB55J8%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781751250/6558c0f59aea7976bd44b0213d76/e750f02b-cd0d-437e-a83f-9ac362cdf456?expires=1767998700&signature=b614a4b0add5f0dea57e8d2c4059bd68a1c6b93db73dd009c2488118327d9662&req=dScvF857nINaWfMW1HO4zTrxC68g9l%2BSqXridZhfx1K78NztDnKmfd9Ji%2B1Q%0AFqF42CnM8d3lBfB55J8%3D%0A)

# Uploading custom extensions

You can also upload custom extensions to deploy across your organization via Admin settings > Connectors > Desktop.

**Note:** Ensure the name field in the manifest.json does not overlap with any existing MCPBs. All names for unique MCPBs / desktop extensions must be unique.

1. Click “Add custom extension”
2. This will open a filepicker; select the .mcpb file.
3. The extension will appear under **Custom team extensions**.
4. Click "...” then “Add to team” to add it to your allowlist and enable it for your team.

When you allowlist a custom extension, it's scoped to your specific organization and can't be used across other organizations. For more in-depth information about creating custom extensions with MCP Bundles (.mcpb), please refer to our [desktop extension developer documentation](https://github.com/anthropics/mcpb).

# Updating custom extensions

We’ve also introduced the ability to update previously-installed custom extensions to new versions without having to remove and reinstall them.

You can update a new MCPB version by making changes to manifest.json, ensuring the version field for the update candidate is incremented from the current uploaded version, and that you leave the name value unchanged. Changing the name will create a new custom desktop extension rather than uploading a new version. Then navigate to the custom upload pane, select "Upload new version" via the kebab menu, and upload the new file.

---

Related Articles

[Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)[Deploy Claude Desktop for macOS](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)[Using the 10x Genomics Extension in Claude](https://support.claude.com/en/articles/12614803-using-the-10x-genomics-extension-in-claude)[Deploying enterprise-grade MCP servers with desktop extensions](https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions)[Building Desktop Extensions with MCPB](https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb)
