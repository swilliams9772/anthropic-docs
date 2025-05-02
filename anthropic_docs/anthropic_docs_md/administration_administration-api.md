---
title: 
source_url: https://docs.anthropic.com/en/docs/administration/administration-api/
---

[Anthropic home page](/)

English

Search...

Search...

Navigation

Administration

Admin API

[Welcome](/en/home)[User Guides](/en/docs/welcome)[API Reference](/en/api/getting-started)[Prompt Library](/en/prompt-library/library)[Release Notes](/en/release-notes/overview)

- [Developer Console](https://console.anthropic.com/)
- [Developer Discord](https://www.anthropic.com/discord)
- [Support](https://support.anthropic.com/)

##### Get started

* [Overview](/en/docs/welcome)
* [Initial setup](/en/docs/initial-setup)
* [Intro to Claude](/en/docs/intro-to-claude)

##### Learn about Claude

* Use cases
* Models & pricing
* [Security and compliance](https://trust.anthropic.com/)

##### Build with Claude

* [Define success criteria](/en/docs/build-with-claude/define-success)
* [Develop test cases](/en/docs/build-with-claude/develop-tests)
* [Context windows](/en/docs/build-with-claude/context-windows)
* [Vision](/en/docs/build-with-claude/vision)
* Prompt engineering
* [Extended thinking](/en/docs/build-with-claude/extended-thinking)
* [Multilingual support](/en/docs/build-with-claude/multilingual-support)
* Tool use (function calling)
* [Prompt caching](/en/docs/build-with-claude/prompt-caching)
* [PDF support](/en/docs/build-with-claude/pdf-support)
* [Citations](/en/docs/build-with-claude/citations)
* [Token counting](/en/docs/build-with-claude/token-counting)
* [Batch processing](/en/docs/build-with-claude/batch-processing)
* [Embeddings](/en/docs/build-with-claude/embeddings)

##### Agents and tools

* Claude Code
* [Computer use (beta)](/en/docs/agents-and-tools/computer-use)
* [Model Context Protocol (MCP)](/en/docs/agents-and-tools/mcp)
* [Google Sheets add-on](/en/docs/agents-and-tools/claude-for-sheets)

##### Test and evaluate

* Strengthen guardrails
* [Using the Evaluation Tool](/en/docs/test-and-evaluate/eval-tool)

##### Administration

* [Admin API](/en/docs/administration/administration-api)

##### Resources

* [Glossary](/en/docs/resources/glossary)
* [Model deprecations](/en/docs/resources/model-deprecations)
* [System status](https://status.anthropic.com/)
* [Claude 3 model card](https://assets.anthropic.com/m/61e7d27f8c8f5919/original/Claude-3-Model-Card.pdf)
* [Claude 3.7 system card](https://anthropic.com/claude-3-7-sonnet-system-card)
* [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
* [Anthropic Courses](https://github.com/anthropics/courses)
* [API features](/en/docs/resources/api-features)

##### Legal center

* [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)

**The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.

The [Admin API](/en/api/admin-api) allows you to programmatically manage your organization’s resources, including organization members, workspaces, and API keys. This provides programmatic control over administrative tasks that would otherwise require manual configuration in the [Anthropic Console](https://console.anthropic.com).

**The Admin API requires special access**

The Admin API requires a special Admin API key (starting with `sk-ant-admin...`) that differs from standard API keys. Only organization members with the admin role can provision Admin API keys through the Anthropic Console.

[​](#how-the-admin-api-works) How the Admin API works
-----------------------------------------------------

When you use the Admin API:

1. You make requests using your Admin API key in the `x-api-key` header
2. The API allows you to manage:
  * Organization members and their roles
  * Organization member invites
  * Workspaces and their members
  * API keys

This is useful for:

* Automating user onboarding/offboarding
* Programmatically managing workspace access
* Monitoring and managing API key usage

[​](#organization-roles-and-permissions) Organization roles and permissions
---------------------------------------------------------------------------

There are five organization-level roles.

| Role | Permissions |
| --- | --- |
| user | Can use Workbench |
| claude\_code\_user | Can use Workbench and [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) |
| developer | Can use Workbench and manage API keys |
| billing | Can use Workbench and manage billing details |
| admin | Can do all of the above, plus manage users |

[​](#key-concepts) Key concepts
-------------------------------

### [​](#organization-members) Organization Members

You can list organization members, update member roles, and remove members.

### [​](#organization-invites) Organization Invites

You can invite users to organizations and manage those invites.

### [​](#workspaces) Workspaces

Create and manage [workspaces](https://console.anthropic.com/settings/workspaces) to organize your resources:

### [​](#workspace-members) Workspace Members

Manage user access to specific workspaces:

### [​](#api-keys) API Keys

Monitor and manage API keys:

[​](#best-practices) Best practices
-----------------------------------

To effectively use the Admin API:

* Use meaningful names and descriptions for workspaces and API keys
* Implement proper error handling for failed operations
* Regularly audit member roles and permissions
* Clean up unused workspaces and expired invites
* Monitor API key usage and rotate keys periodically

[​](#faq) FAQ
-------------

What permissions are needed to use the Admin API?

Only organization members with the admin role can use the Admin API. They must also have a special Admin API key (starting with `sk-ant-admin`).

Can I create new API keys through the Admin API?

No, new API keys can only be created through the Anthropic Console for security reasons. The Admin API can only manage existing API keys.

What happens to API keys when removing a user?

API keys persist in their current state as they are scoped to the Organization, not to individual users.

Can organization admins be removed via the API?

No, organization members with the admin role cannot be removed via the API for security reasons.

How long do organization invites last?

Organization invites expire after 21 days. There is currently no way to modify this expiration period.

Are there limits on workspaces?

Yes, you can have a maximum of 100 workspaces per Organization. Archived workspaces do not count towards this limit.

What's the Default Workspace?

Every Organization has a “Default Workspace” that cannot be edited or removed, and has no ID. This Workspace does not appear in workspace list endpoints.

How do organization roles affect Workspace access?

Organization admins automatically get the `workspace_admin` role to all workspaces. Organization billing members automatically get the `workspace_billing` role. Organization users and developers must be manually added to each workspace.

Which roles can be assigned in workspaces?

Organization users and developers can be assigned `workspace_admin`, `workspace_developer`, or `workspace_user` roles. The `workspace_billing` role can’t be manually assigned - it’s inherited from having the organization `billing` role.

Can organization admin or billing members' workspace roles be changed?

Only organization billing members can have their workspace role upgraded to an admin role. Otherwise, organization admins and billing members can’t have their workspace roles changed or be removed from workspaces while they hold those organization roles. Their workspace access must be modified by changing their organization role first.

What happens to workspace access when organization roles change?

If an organization admin or billing member is demoted to user or developer, they lose access to all workspaces except ones where they were manually assigned roles. When users are promoted to admin or billing roles, they gain automatic access to all workspaces.

Was this page helpful?

YesNo

[Using the Evaluation Tool](/en/docs/test-and-evaluate/eval-tool)[Glossary](/en/docs/resources/glossary)

On this page

* [How the Admin API works](#how-the-admin-api-works)
* [Organization roles and permissions](#organization-roles-and-permissions)
* [Key concepts](#key-concepts)
* [Organization Members](#organization-members)
* [Organization Invites](#organization-invites)
* [Workspaces](#workspaces)
* [Workspace Members](#workspace-members)
* [API Keys](#api-keys)
* [Best practices](#best-practices)
* [FAQ](#faq)