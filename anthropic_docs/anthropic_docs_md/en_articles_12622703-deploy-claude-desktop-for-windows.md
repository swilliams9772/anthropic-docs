# Deploy Claude Desktop for Windows

**Source:** https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows

Administrators on Team or Enterprise plans can deploy Claude Desktop automatically across their organization to manage installations and updates centrally. We offer an MSIX package for Windows deployments, enabling secure, scalable distribution.

# Available Formats

- `.msix` - Compatible with Microsoft Intune and Microsoft Store

- `.exe` - Standard installer. Installs to `%LOCALAPPDATA%\Programs\Claude\`. Updates automatically when new versions are released, unless disabled via enterprise policies.

# Download:

* [X64 Claude MSIX Installer](https://claude.ai/api/desktop/win32/x64/msix/latest/redirect)
* [ARM64 Claude MSIX Installer](https://claude.ai/api/desktop/win32/arm64/msix/latest/redirect)

# Installation commands:

For manual installation on individual machines, use the following PowerShell commands:

**Install for single user:**

```
```powershell
Add-AppxPackage -Path "Claude.msix"
```
```

See Microsoft's [Add-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/add-appxpackage?view=windowsserver2022-ps) documentation for more details.

**Install for all users (provisions machine-wide):**

```
```powershell
Add-AppxProvisionedPackage -Online -PackagePath "Claude.msix" -SkipLicense -Regions "all"
```
```

See Microsoft's [Add-AppxProvisionedPackage](https://learn.microsoft.com/en-us/powershell/module/dism/add-appxprovisionedpackage?view=windowsserver2022-ps) documentation for more details.

# Deploy via MDM

Claude Desktop can be deployed through various enterprise software distribution services. Choose the method that aligns with your organization's existing infrastructure:

* [Microsoft Intune](https://docs.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-intune)
* [Microsoft Endpoint Configuration Manager (SCCM)](https://learn.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-mem-adminconsole)
* [Group Policy Software Installation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software)
* [Deployment Image Servicing and Management (DISM.exe)](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/preinstall-apps-using-dism?view=windows-10)
* [PowerShell Scripts](https://learn.microsoft.com/en-us/windows/msix/desktop/powershell-msix-cmdlets)

# Configuration

To configure Claude Desktop settings such as auto-updates, extensions, and MCP servers, see the [Enterprise Configuration article](https://support.claude.com/en/articles/12622667-enterprise-configuration).

# Troubleshooting

# MSIX package not working with AppLocker?

By default, packaged apps may be restricted by AppLocker policies. Ensure your AppLocker rules allow MSIX packages, or add Claude Desktop to your allowed applications list. Consult your organization's security policies before making changes.

---

Related Articles

[Installing Claude Desktop](https://support.claude.com/en/articles/10065433-installing-claude-desktop)[Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)[Deploy Claude Desktop for macOS](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)[Enterprise Configuration](https://support.claude.com/en/articles/12622667-enterprise-configuration)[Deploying enterprise-grade MCP servers with desktop extensions](https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions)
