# Compliance API

**Source:** http://platform.claude.com/docs/en/api/compliance

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Compliance API

# Compliance APIActivities

# [Query compliance activities](/docs/en/api/compliance/activities/list)

GET/v1/compliance/activities

# ModelsExpand Collapse

ActivityListResponse = object { actor, id, created\_at, 3 more }  or object { actor, admin\_api\_key\_id, scopes, 5 more }  or object { actor, admin\_api\_key\_id, id, 4 more }  or 302 more

User-initiated self-service account deletion.

One of the following:

AccountDeleted object { actor, id, created\_at, 3 more }

User-initiated self-service account deletion.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "account\_deleted"

AdminAPIKeyCreated object { actor, admin\_api\_key\_id, scopes, 5 more }

An admin API key was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

admin\_api\_key\_id: string

Tagged ID of the created admin API key

scopes: array of string

Scopes granted to the key (empty for legacy non-scoped admin keys)

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "admin\_api\_key\_created"

AdminAPIKeyDeleted object { actor, admin\_api\_key\_id, id, 4 more }

An admin API key was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

admin\_api\_key\_id: string

Tagged ID of the deleted admin API key

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "admin\_api\_key\_deleted"

AdminAPIKeyUpdated object { actor, admin\_api\_key\_id, updates, 5 more }

An admin API key was updated (renamed or activated/deactivated).

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

admin\_api\_key\_id: string

Tagged ID of the updated admin API key

updates: array of object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: "name" or "status"

One of the following:

"name"

"status"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "admin\_api\_key\_updated"

AdminConnectorRequestResolved object { actor, decision, mcp\_server\_id, 6 more }

Admin approved or dismissed pending member requests to enable an MCP connector.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

decision: "approved" or "dismissed"

One of the following:

"approved"

"dismissed"

mcp\_server\_id: string

resolved\_count: number

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "admin\_connector\_request\_resolved"

AdminRequestCreated object { actor, request\_type, id, 4 more }

Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

request\_type: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "admin\_request\_created"

AgeVerified object { actor, id, created\_at, 3 more }

User age was verified.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "age\_verified"

AnonymousMobileLoginAttempted object { actor, id, created\_at, 3 more }

Anonymous mobile login was attempted.

actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "anonymous\_mobile\_login\_attempted"

APIKeyCreated object { actor, api\_key\_id, scopes, 5 more }

Activity logged when a new API key is created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

api\_key\_id: string

The tagged ID of the created API key

scopes: array of string

The scopes for this API key

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "api\_key\_created"

ClaudeArtifactAccessFailed object { actor, claude\_artifact\_id, claude\_artifact\_version\_id, 5 more }

An attempt to access an artifact failed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_artifact\_id: string

claude\_artifact\_version\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_artifact\_access\_failed"

ClaudeArtifactCreated object { actor, claude\_artifact\_id, id, 4 more }

An artifact was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_artifact\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_artifact\_created"

ClaudePublishedArtifactDeleted object { actor, claude\_published\_artifact\_id, id, 4 more }

A published artifact was unpublished/deleted by its creator.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_published\_artifact\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_published\_artifact\_deleted"

ClaudeArtifactPublished object { actor, artifact\_type, claude\_published\_artifact\_id, 6 more }

An artifact was published and made publicly accessible.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

artifact\_type: string

Artifact type (code, html, react, etc.)

claude\_published\_artifact\_id: string

title: string

Title of the published artifact

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_artifact\_published"

ClaudeArtifactSharingUpdated object { actor, audience, claude\_artifact\_id, 6 more }

An artifact's sharing settings were updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

audience: array of object { type }

Sharing audience for the project. If empty, this it's only visible to the creating user.

type: optional "organization"

claude\_artifact\_id: string

claude\_artifact\_version\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_artifact\_sharing\_updated"

ClaudeArtifactViewed object { actor, claude\_artifact\_id, id, 4 more }

An artifact was viewed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_artifact\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_artifact\_viewed"

AuditLogExportAccessed object { actor, id, created\_at, 3 more }

Audit log export file was accessed/downloaded via signed URL.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "audit\_log\_export\_accessed"

AuditLogExportStarted object { actor, id, created\_at, 5 more }

Audit log export was initiated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

from\_date: optional string

Start date of the export range

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

to\_date: optional string

End date of the export range

type: optional "audit\_log\_export\_started"

BillingEmailsUpdated object { actor, id, cc\_email\_count, 6 more }

The organization's billing email recipients were updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

cc\_email\_count: optional number

Number of 'cc' email recipients.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

primary\_email\_set: optional boolean

Whether a primary billing email is configured.

to\_email\_count: optional number

Number of 'to' email recipients.

type: optional "billing\_emails\_updated"

ClaudeChatAccessFailed object { actor, claude\_chat\_id, id, 4 more }

An attempt to access a chat failed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_chat\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_chat\_access\_failed"

ClaudeChatCreated object { actor, claude\_chat\_id, id, 5 more }

User created a chat.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_chat\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_project\_id: optional string

Project ID this chat belongs to, if any

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_chat\_created"

ClaudeChatDeleted object { actor, claude\_chat\_id, id, 5 more }

User deleted a chat.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_chat\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_project\_id: optional string

Project ID this chat belongs to, if any

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_chat\_deleted"

ClaudeChatDeletionFailed object { actor, claude\_chat\_id, id, 4 more }

A request to delete a chat failed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_chat\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_chat\_deletion\_failed"

ClaudeChatSettingsUpdated object { actor, claude\_chat\_id, id, 5 more }

User updated the settings for a conversation.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_chat\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_project\_id: optional string

Project ID this chat belongs to, if any

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_chat\_settings\_updated"

ClaudeChatSnapshotCreated object { actor, claude\_chat\_id, claude\_chat\_snapshot\_id, 5 more }

User created/shared a chat snapshot.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_chat\_id: string

claude\_chat\_snapshot\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_chat\_snapshot\_created"

ClaudeChatSnapshotViewed object { actor, claude\_chat\_snapshot\_id, id, 5 more }

User viewed a chat snapshot (authenticated or public/unauthenticated).

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_chat\_snapshot\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_chat\_id: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_chat\_snapshot\_viewed"

ClaudeChatUpdated object { actor, claude\_chat\_id, id, 5 more }

User updated the chat metadata (e.g name, model).

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_chat\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_project\_id: optional string

Project ID this chat belongs to, if any

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_chat\_updated"

ClaudeChatViewed object { actor, claude\_chat\_id, id, 5 more }

User viewed a chat.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_chat\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_project\_id: optional string

Project ID this chat belongs to, if any

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_chat\_viewed"

ClaudeCodeReviewConfigUpdated object { actor, enabled, id, 7 more }

Claude Code Review configuration was enabled/disabled for an org.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

enabled: boolean

Whether code review is now enabled

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

environment\_id: optional string

Environment used for code review

model: optional string

Model configured for code review

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

per\_review\_limit\_usd: optional string

Per-review spend limit in USD

type: optional "claude\_code\_review\_config\_updated"

ClaudeCodeReviewRepositoryAdded object { actor, config\_id, repo\_name, 7 more }

A repository was added to org-level Claude Code Review configuration.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

config\_id: string

ID of the repository configuration

repo\_name: string

Repository name

repo\_owner: string

Repository owner (GitHub org/user)

trigger\_mode: string

When code review is triggered

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_review\_repository\_added"

ClaudeCodeReviewRepositoryRemoved object { actor, config\_id, repo\_name, 6 more }

A repository was removed from org-level Claude Code Review configuration.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

config\_id: string

ID of the deleted repository configuration

repo\_name: string

Repository name at deletion time

repo\_owner: string

Repository owner at deletion time

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_review\_repository\_removed"

ClaudeCodeReviewRepositoryUpdated object { actor, config\_id, repo\_name, 8 more }

A Claude Code Review repository configuration was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

config\_id: string

ID of the repository configuration

repo\_name: string

Repository name

repo\_owner: string

Repository owner

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

status: optional string

Updated status (ACTIVE/INACTIVE)

trigger\_mode: optional string

Updated trigger mode

type: optional "claude\_code\_review\_repository\_updated"

ClaudeCodeSecurityCenterConfigUpdated object { actor, enabled, id, 5 more }

Claude Code Security Center scanning was enabled/disabled for an org.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

enabled: boolean

Whether Security Center is now enabled

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

environment\_id: optional string

Environment used for security scanning

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_security\_center\_config\_updated"

ClaudeCodeSecurityScanCancelled object { actor, scan\_project\_id, scans\_cancelled, 5 more }

In-flight Claude Code Security scans were cancelled for a project.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

scan\_project\_id: string

Tagged ID of the scan project

scans\_cancelled: number

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_security\_scan\_cancelled"

ClaudeCodeSecurityScanProjectUpdated object { action, actor, scan\_project\_id, 5 more }

A Claude Code Security scan project was archived or unarchived.

action: "archived" or "unarchived"

One of the following:

"archived"

"unarchived"

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

scan\_project\_id: string

Tagged ID of the scan project

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_security\_scan\_project\_updated"

ClaudeCodeSecurityScanScheduleDeleted object { actor, scan\_project\_id, id, 4 more }

A recurring scan schedule was deleted for a Claude Code Security project.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

scan\_project\_id: string

Tagged ID of the scan project

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_security\_scan\_schedule\_deleted"

ClaudeCodeSecurityScanScheduleUpdated object { actor, cadence, scan\_project\_id, 5 more }

A recurring scan schedule was set or replaced for a Claude Code Security project.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

cadence: string

scan\_project\_id: string

Tagged ID of the scan project

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_security\_scan\_schedule\_updated"

ClaudeCodeSecurityWebhookCreated object { actor, scan\_project\_id, url, 6 more }

An outbound webhook was created for a Claude Code Security scan project.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

scan\_project\_id: string

Tagged ID of the scan project

url: string

webhook\_id: string

Tagged ID of the webhook

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_security\_webhook\_created"

ClaudeCodeSecurityWebhookDeleted object { actor, scan\_project\_id, webhook\_id, 5 more }

An outbound webhook for a Claude Code Security scan project was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

scan\_project\_id: string

Tagged ID of the scan project

webhook\_id: string

Tagged ID of the webhook

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_security\_webhook\_deleted"

ClaudeCodeSecurityWebhookSecretUpdated object { actor, scan\_project\_id, webhook\_id, 5 more }

The HMAC signing secret for a Claude Code Security webhook was rotated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

scan\_project\_id: string

Tagged ID of the scan project

webhook\_id: string

Tagged ID of the webhook

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_security\_webhook\_secret\_updated"

ClaudeCodeSecurityWebhookUpdated object { actor, scan\_project\_id, webhook\_id, 5 more }

An outbound webhook for a Claude Code Security scan project was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

scan\_project\_id: string

Tagged ID of the scan project

webhook\_id: string

Tagged ID of the webhook

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_security\_webhook\_updated"

ClaudeCodeTeamMemoryACLUpdated object { action, actor, group\_id, 6 more }

An RBAC group was added to or removed from the Claude Code team-memory ACL.

action: "removed" or "set"

Whether the group was set (added/updated) or removed

One of the following:

"removed"

"set"

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

group\_id: string

Tagged ID of the RBAC group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

access\_level: optional string

Access level granted (when action=set)

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_code\_team\_memory\_acl\_updated"

CliPluginExecPolicyUpdated object { actor, cli\_name, marketplace\_id, 9 more }

Admin set or cleared the per-op permission ceiling for a plugin CLI.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

cli\_name: string

CLI name as declared by the plugin manifest

marketplace\_id: string

Marketplace ID owning the plugin

max\_permission: string

New max\_permission value ('allow' | 'ask' | 'blocked'), or null when cleared

op\_name: string

Op name (or '\*' for the per-CLI default)

plugin\_id: string

Plugin ID resolved from the URL

plugin\_name: string

Plugin name within its marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "cli\_plugin\_exec\_policy\_updated"

ClaudeCommandCreated object { actor, id, command\_id, 5 more }

Command was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

command\_id: optional string

command\_name: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_command\_created"

ClaudeCommandDeleted object { actor, id, command\_id, 5 more }

Command was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

command\_id: optional string

command\_name: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_command\_deleted"

ClaudeCommandReplaced object { actor, id, command\_id, 5 more }

Command was replaced.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

command\_id: optional string

command\_name: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_command\_replaced"

ComplianceAPIAccessed object { actor, request\_id, request\_method, 8 more }

Logging event auto-generated for each compliance API request.

actor: object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

request\_id: string

request\_method: "DELETE" or "GET" or "POST" or "PUT"

One of the following:

"DELETE"

"GET"

"POST"

"PUT"

status\_code: number

HTTP status code

url: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

request\_body: optional string

Serialized JSON request body

type: optional "compliance\_api\_accessed"

DesktopExtensionAllowlisted object { actor, extension\_id, id, 4 more }

A desktop extension was added to an org's allowlist.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

extension\_id: string

Allowlisted DXT extension ID

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "desktop\_extension\_allowlisted"

DesktopExtensionBlocklisted object { actor, extension\_id, id, 4 more }

A desktop extension was added to the global blocklist.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

extension\_id: string

Blocklisted DXT extension ID

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "desktop\_extension\_blocklisted"

DesktopExtensionDeleted object { actor, extension\_id, id, 5 more }

A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

extension\_id: string

DXT extension ID

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "desktop\_extension\_deleted"

version: optional string

Specific version deleted (null if all versions)

DesktopExtensionRemovedFromAllowlist object { actor, extension\_id, id, 4 more }

A desktop extension was removed from an org's allowlist.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

extension\_id: string

DXT extension ID removed from allowlist

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "desktop\_extension\_removed\_from\_allowlist"

DesktopExtensionUnblocked object { actor, extension\_id, id, 4 more }

A desktop extension was removed from the global blocklist.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

extension\_id: string

Unblocked DXT extension ID

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "desktop\_extension\_unblocked"

DesktopExtensionUploaded object { actor, extension\_id, version, 5 more }

A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

extension\_id: string

DXT extension ID

version: string

Version string from the manifest

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "desktop\_extension\_uploaded"

DesktopExtensionVersionUploaded object { actor, extension\_id, version, 5 more }

A new version of an existing org-owned desktop extension was uploaded.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

extension\_id: string

DXT extension ID

version: string

Version string from the manifest

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "desktop\_extension\_version\_uploaded"

DomainClaimInitiated object { actor, id, created\_at, 3 more }

Domain capture claim initiated over personal accounts on verified domains.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "domain\_claim\_initiated"

EndUserInviteRequested object { actor, invitee\_email, id, 4 more }

Non-admin member submitted an invite request for a new org member.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

invitee\_email: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "end\_user\_invite\_requested"

ExtraUsageBillingEnabled object { actor, id, created\_at, 3 more }

Usage credit billing was enabled for an organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "extra\_usage\_billing\_enabled"

ExtraUsageCreditGranted object { actor, id, created\_at, 3 more }

A promotional usage credit grant was claimed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "extra\_usage\_credit\_granted"

ExtraUsageSpendLimitCreated object { actor, id, amount, 8 more }

Usage credit spend limit was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

amount: optional number

The monthly credit limit amount in minor units (e.g. cents).

created\_at: optional string

When this activity occurred.

is\_enabled: optional boolean

Whether the spend limit is enabled.

limit\_type: optional string

The type of spend limit created (e.g. organization, seat\_tier, member, service, group).

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

spend\_limit\_id: optional string

Tagged ID of the spend limit.

type: optional "extra\_usage\_spend\_limit\_created"

user\_id: optional string

Tagged ID of the user who performed the action.

ExtraUsageSpendLimitDeleted object { actor, id, created\_at, 5 more }

Usage credit spend limit was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

spend\_limit\_id: optional string

Tagged ID of the spend limit.

type: optional "extra\_usage\_spend\_limit\_deleted"

user\_id: optional string

Tagged ID of the user who performed the action.

ExtraUsageSpendLimitIncreaseRequestApproved object { actor, id, amount, 7 more }

A usage credit spend limit increase request was approved.

actor: object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

amount: optional number

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

requester\_user\_id: optional string

spend\_limit\_id: optional string

spend\_limit\_increase\_request\_id: optional string

type: optional "extra\_usage\_spend\_limit\_increase\_request\_approved"

ExtraUsageSpendLimitIncreaseRequestDenied object { actor, id, created\_at, 5 more }

A usage credit spend limit increase request was denied.

actor: object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

requester\_user\_id: optional string

spend\_limit\_increase\_request\_id: optional string

type: optional "extra\_usage\_spend\_limit\_increase\_request\_denied"

ExtraUsageSpendLimitUpdated object { actor, id, amount, 8 more }

Usage credit spend limit was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

amount: optional number

The new monthly credit limit amount in minor units (e.g. cents).

created\_at: optional string

When this activity occurred.

is\_enabled: optional boolean

Whether the spend limit is enabled.

limit\_type: optional string

The type of spend limit updated (e.g. organization, seat\_tier, member, service, group).

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

spend\_limit\_id: optional string

Tagged ID of the spend limit.

type: optional "extra\_usage\_spend\_limit\_updated"

user\_id: optional string

Tagged ID of the user who performed the action.

ClaudeFileAccessFailed object { actor, claude\_file\_id, filename, 7 more }

An attempt to access a file failed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_file\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_artifact\_id: optional string

Artifact ID if file was accessed via an artifact

claude\_project\_id: optional string

Project ID if file was accessed via a project

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_file\_access\_failed"

ClaudeFileDeleted object { actor, claude\_file\_id, filename, 5 more }

A file was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_file\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_file\_deleted"

ClaudeFileUploaded object { actor, claude\_file\_id, filename, 7 more }

A file was uploaded.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_file\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_chat\_id: optional string

Chat ID if file was uploaded to a chat

claude\_project\_id: optional string

Project ID if file was uploaded to a project

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_file\_uploaded"

ClaudeFileViewed object { actor, claude\_file\_id, filename, 7 more }

A file was viewed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_file\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_artifact\_id: optional string

Artifact ID if file was accessed via an artifact

claude\_project\_id: optional string

Project ID if file was accessed via a project

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_file\_viewed"

GheConfigurationCreated object { actor, ghe\_configuration\_id, id, 4 more }

Admin created a GHE configuration.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

ghe\_configuration\_id: string

ID of the GHE configuration

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "ghe\_configuration\_created"

GheConfigurationDeleted object { actor, ghe\_configuration\_id, id, 4 more }

Admin deleted a GHE configuration.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

ghe\_configuration\_id: string

ID of the GHE configuration

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "ghe\_configuration\_deleted"

GheConfigurationUpdated object { actor, ghe\_configuration\_id, id, 4 more }

Admin updated a GHE configuration.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

ghe\_configuration\_id: string

ID of the GHE configuration

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "ghe\_configuration\_updated"

GheUserConnected object { actor, id, created\_at, 4 more }

User connected to a GHE instance.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

ghe\_configuration\_id: optional string

ID of the GHE configuration

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "ghe\_user\_connected"

GheUserDisconnected object { actor, id, created\_at, 4 more }

User disconnected from a GHE instance.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

ghe\_configuration\_id: optional string

ID of the GHE configuration

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "ghe\_user\_disconnected"

GheWebhookSignatureInvalid object { actor, ghe\_configuration\_id, id, 4 more }

Webhook signature validation failed.

actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

ghe\_configuration\_id: string

ID of the GHE configuration

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "ghe\_webhook\_signature\_invalid"

ClaudeGitHubIntegrationCreated object { actor, integration\_id, id, 6 more }

A GitHub integration was enabled for the organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_name: optional string

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

repository\_name: optional string

type: optional "claude\_github\_integration\_created"

ClaudeGitHubIntegrationDeleted object { actor, integration\_id, id, 6 more }

A GitHub integration was disabled for the organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_name: optional string

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

repository\_name: optional string

type: optional "claude\_github\_integration\_deleted"

ClaudeGitHubIntegrationUpdated object { actor, integration\_id, id, 6 more }

A GitHub integration's configuration was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_name: optional string

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

repository\_name: optional string

type: optional "claude\_github\_integration\_updated"

ClaudeGdriveIntegrationCreated object { actor, integration\_id, id, 5 more }

A Google Drive integration was enabled for the organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

folder\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_gdrive\_integration\_created"

ClaudeGdriveIntegrationDeleted object { actor, integration\_id, id, 5 more }

A Google Drive integration was disabled for the organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

folder\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_gdrive\_integration\_deleted"

ClaudeGdriveIntegrationUpdated object { actor, integration\_id, id, 5 more }

A Google Drive integration's configuration was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

folder\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_gdrive\_integration\_updated"

GroupCreated object { actor, group\_id, group\_name, 5 more }

A group was created (RBAC admin or SCIM provisioning).

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

group\_id: string

Tagged ID of the created group

group\_name: string

Name of the created group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "group\_created"

GroupDeleted object { actor, group\_id, id, 4 more }

A group was deleted (RBAC admin or SCIM provisioning).

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

group\_id: string

Tagged ID of the deleted group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "group\_deleted"

GroupListViewed object { actor, id, created\_at, 3 more }

Admin viewed the list of RBAC groups.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "group\_list\_viewed"

GroupMemberAdded object { actor, group\_id, member\_ids, 5 more }

One or more members were added to a group.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

group\_id: string

Tagged ID of the group

member\_ids: array of string

Tagged IDs of the members added

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "group\_member\_added"

GroupMemberListViewed object { actor, group\_id, id, 4 more }

Admin viewed the members of an RBAC group.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

group\_id: string

Tagged ID of the group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "group\_member\_list\_viewed"

GroupMemberRemoved object { actor, group\_id, member\_ids, 5 more }

One or more members were removed from a group.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

group\_id: string

Tagged ID of the group

member\_ids: array of string

Tagged IDs of the members removed

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "group\_member\_removed"

GroupUpdated object { actor, group\_id, id, 4 more }

A group was updated (RBAC admin or SCIM provisioning).

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

group\_id: string

Tagged ID of the updated group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "group\_updated"

GroupViewed object { actor, group\_id, id, 4 more }

A group was viewed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

group\_id: string

Tagged ID of the viewed group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "group\_viewed"

IntegrationUserConnected object { actor, id, created\_at, 4 more }

User connected to an integration.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

integration\_type: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "integration\_user\_connected"

IntegrationUserDisconnected object { actor, id, created\_at, 4 more }

User disconnected from an integration.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

integration\_type: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "integration\_user\_disconnected"

InvoiceCollectionMethodUpdated object { actor, id, created\_at, 4 more }

Invoice collection method was changed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

new\_collection\_method: optional string

New collection method (e.g. charge\_automatically, send\_invoice).

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "invoice\_collection\_method\_updated"

UserLoggedOut object { actor, id, created\_at, 3 more }

A user signed out of one or all sessions.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "user\_logged\_out"

LtiLaunchInitiated object { actor, id, created\_at, 3 more }

LTI launch was initiated.

actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "lti\_launch\_initiated"

LtiLaunchSuccess object { actor, id, created\_at, 3 more }

LTI launch completed successfully.

actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "lti\_launch\_success"

LtiPlatformCreated object { actor, lti\_platform\_id, lti\_platform\_issuer, 5 more }

Admin created an LTI platform integration.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

lti\_platform\_id: string

UUID of the LTI platform

lti\_platform\_issuer: string

Platform issuer URL

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "lti\_platform\_created"

LtiPlatformUpdated object { actor, lti\_platform\_id, id, 5 more }

Admin updated an LTI platform integration.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

lti\_platform\_id: string

UUID of the LTI platform

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

lti\_platform\_issuer: optional string

Platform issuer URL

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "lti\_platform\_updated"

MagicLinkLoginFailed object { actor, id, created\_at, 3 more }

A magic link sign-in attempt failed.

actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "magic\_link\_login\_failed"

MagicLinkLoginInitiated object { actor, id, created\_at, 3 more }

A user requested a magic link sign-in email.

actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "magic\_link\_login\_initiated"

MagicLinkLoginSucceeded object { actor, id, auth\_method, 5 more }

A user successfully signed in with a magic link email.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

auth\_method: optional "magic\_link"

The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

created\_at: optional string

When this activity occurred.

mfa\_method: optional "not\_used"

The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "magic\_link\_login\_succeeded"

ManagedOrganizationSetupCompleted object { actor, id, created\_at, 3 more }

Managed (AWS Marketplace) organization setup was completed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "managed\_organization\_setup\_completed"

MarketplaceCreated object { actor, marketplace\_id, id, 4 more }

Admin created an organization marketplace.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

marketplace\_id: string

Tagged ID of the marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "marketplace\_created"

MarketplaceDeleted object { actor, marketplace\_id, id, 4 more }

Admin deleted an organization marketplace.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

marketplace\_id: string

Tagged ID of the marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "marketplace\_deleted"

MarketplaceUpdated object { actor, marketplace\_id, id, 4 more }

Admin updated an organization marketplace.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

marketplace\_id: string

Tagged ID of the marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "marketplace\_updated"

MarketplaceWebhookDeleted object { actor, marketplace\_id, id, 4 more }

Admin removed the GitHub push webhook for a marketplace.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

marketplace\_id: string

Tagged ID of the marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "marketplace\_webhook\_deleted"

MarketplaceWebhookProvisioned object { actor, marketplace\_id, id, 5 more }

Admin provisioned a GitHub push webhook for a marketplace.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

marketplace\_id: string

Tagged ID of the marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

github\_webhook\_id: optional number

GitHub-assigned webhook ID returned by the hooks API

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "marketplace\_webhook\_provisioned"

McpServerCreated object { actor, mcp\_server\_id, mcp\_server\_name, 5 more }

An MCP server was added to the organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

mcp\_server\_id: string

Tagged ID of the MCP server

mcp\_server\_name: string

Display name of the MCP server

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "mcp\_server\_created"

McpServerDeleted object { actor, mcp\_server\_id, mcp\_server\_name, 5 more }

An MCP server was removed from the organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

mcp\_server\_id: string

Tagged ID of the MCP server

mcp\_server\_name: string

Display name of the MCP server

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "mcp\_server\_deleted"

McpServerUpdated object { actor, mcp\_server\_id, mcp\_server\_name, 5 more }

An MCP server's configuration was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

mcp\_server\_id: string

Tagged ID of the MCP server

mcp\_server\_name: string

Display name of the MCP server

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "mcp\_server\_updated"

McpToolPolicyUpdated object { actor, max\_permission, mcp\_server\_id, 7 more }

The permission restriction for an MCP tool was set or cleared.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

max\_permission: string

New max\_permission value ('allow' | 'ask' | 'blocked'), or null when cleared

mcp\_server\_id: string

Tagged ID of the MCP server

mcp\_server\_name: string

Display name of the MCP server

tool\_name: string

Tool name (or '\*' for the MCP-server-wide default)

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "mcp\_tool\_policy\_updated"

OrgAnalyticsAPICapabilityUpdated object { actor, id, created\_at, 3 more }

Organization analytics\_api capability was enabled or disabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_analytics\_api\_capability\_updated"

OrgBulkDeleteInitiated object { actor, id, created\_at, 3 more }

Organization bulk deletion was initiated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_bulk\_delete\_initiated"

OrgClaudeCodeDataSharingDisabled object { actor, id, created\_at, 3 more }

Organization Claude Code data sharing was disabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_claude\_code\_data\_sharing\_disabled"

OrgClaudeCodeDataSharingEnabled object { actor, id, created\_at, 3 more }

Organization Claude Code data sharing was enabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_claude\_code\_data\_sharing\_enabled"

OrgClaudeCodeDesktopDisabled object { actor, id, created\_at, 3 more }

Organization Claude Code Desktop was disabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_claude\_code\_desktop\_disabled"

OrgClaudeCodeDesktopEnabled object { actor, id, created\_at, 3 more }

Organization Claude Code Desktop was enabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_claude\_code\_desktop\_enabled"

OrgComplianceAPISettingsUpdated object { actor, id, compliance\_api\_enabled, 5 more }

Organization compliance API settings were updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

compliance\_api\_enabled: optional boolean

compliance\_api\_logging\_enabled: optional boolean

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_compliance\_api\_settings\_updated"

OrgCoworkAgentDisabled object { actor, id, created\_at, 3 more }

Organization Cowork Agent was disabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_cowork\_agent\_disabled"

OrgCoworkAgentEnabled object { actor, id, created\_at, 3 more }

Organization Cowork Agent was enabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_cowork\_agent\_enabled"

OrgCoworkDisabled object { actor, id, created\_at, 3 more }

Organization cowork was disabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_cowork\_disabled"

OrgCoworkEnabled object { actor, id, created\_at, 3 more }

Organization cowork was enabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_cowork\_enabled"

OrgCreationBlocked object { actor, id, created\_at, 4 more }

Organization creation was blocked.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

reason: optional string

type: optional "org\_creation\_blocked"

OrgDataExportAccessed object { actor, id, created\_at, 3 more }

Organization data export file was accessed/downloaded via signed URL.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_data\_export\_accessed"

OrgDataExportCompleted object { actor, id, created\_at, 3 more }

Organization data export was completed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_data\_export\_completed"

OrgDataExportStarted object { actor, id, created\_at, 3 more }

Organization data export was started.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_data\_export\_started"

OrgDeletedViaBulk object { actor, id, created\_at, 3 more }

Organization was deleted via bulk operation.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_deleted\_via\_bulk"

OrgDeletionRequested object { actor, id, created\_at, 3 more }

Organization deletion was requested.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_deletion\_requested"

OrgDirectoryResyncCompleted object { actor, resync\_uuid, id, 4 more }

Organization directory resync completed successfully.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

resync\_uuid: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_directory\_resync\_completed"

OrgDirectoryResyncFailed object { actor, resync\_uuid, id, 4 more }

Organization directory resync failed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

resync\_uuid: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_directory\_resync\_failed"

OrgDirectoryResyncStarted object { actor, resync\_uuid, sync\_destinations, 5 more }

Organization directory resync was started asynchronously.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

resync\_uuid: string

sync\_destinations: array of string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_directory\_resync\_started"

OrgDirectorySyncActivated object { actor, id, created\_at, 3 more }

Organization directory sync was activated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_directory\_sync\_activated"

OrgDirectorySyncAddInitiated object { actor, id, created\_at, 3 more }

Organization directory sync setup was initiated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_directory\_sync\_add\_initiated"

OrgDirectorySyncDeleted object { actor, id, created\_at, 3 more }

Organization directory sync was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_directory\_sync\_deleted"

OrgDiscoverabilityDisabled object { actor, id, created\_at, 3 more }

Admin disabled organization discoverability.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_discoverability\_disabled"

OrgDiscoverabilityEnabled object { actor, id, created\_at, 3 more }

Admin enabled organization discoverability.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_discoverability\_enabled"

OrgDiscoverabilitySettingsUpdated object { actor, id, created\_at, 3 more }

Admin updated organization discoverability settings.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_discoverability\_settings\_updated"

OrgDomainAddInitiated object { actor, id, created\_at, 3 more }

Organization domain verification was initiated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_domain\_add\_initiated"

OrgDomainRemoved object { actor, id, created\_at, 4 more }

Organization domain was removed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

domain: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_domain\_removed"

OrgDomainVerified object { actor, id, created\_at, 4 more }

Organization domain was verified.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

domain: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_domain\_verified"

OrgHipaaSelfServeEnabled object { actor, baa\_content\_hash, baa\_version\_label, 6 more }

A primary owner click-accepted the BAA and enabled HIPAA protections
for the organization via the self-serve flow.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

baa\_content\_hash: string

baa\_version\_label: string

setup\_guide\_content\_hash: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_hipaa\_self\_serve\_enabled"

OrgIPRestrictionCreated object { actor, id, created\_at, 3 more }

Organization IP restriction was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_ip\_restriction\_created"

OrgIPRestrictionDeleted object { actor, id, created\_at, 3 more }

Organization IP restriction was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_ip\_restriction\_deleted"

OrgIPRestrictionUpdated object { actor, id, created\_at, 3 more }

Organization IP restriction was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_ip\_restriction\_updated"

OrgInviteLinkDisabled object { actor, id, created\_at, 3 more }

Organization invite link was disabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_invite\_link\_disabled"

OrgInviteLinkGenerated object { actor, id, created\_at, 3 more }

Organization invite link was generated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_invite\_link\_generated"

OrgInviteLinkRegenerated object { actor, id, created\_at, 3 more }

Organization invite link was regenerated (previous link invalidated).

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_invite\_link\_regenerated"

OrgInviteViewed object { actor, invite\_id, id, 4 more }

An organization invite was viewed.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

invite\_id: string

Tagged ID of the viewed invite

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_invite\_viewed"

OrgInvitesListed object { actor, id, created\_at, 3 more }

Organization invites were listed.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_invites\_listed"

OrgJoinProposalDecided object { actor, approved, id, 4 more }

Approve or reject decision on a parent-org join proposal.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

approved: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_join\_proposal\_decided"

OrgJoinRequestApproved object { actor, id, created\_at, 3 more }

Admin approved a join request.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_join\_request\_approved"

OrgJoinRequestCreated object { actor, id, created\_at, 3 more }

User requested to join an organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_join\_request\_created"

OrgJoinRequestDismissed object { actor, id, created\_at, 3 more }

Admin dismissed a join request.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_join\_request\_dismissed"

OrgJoinRequestInstantApproved object { actor, id, created\_at, 3 more }

Join request was instantly approved.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_join\_request\_instant\_approved"

OrgJoinRequestsBulkDismissed object { actor, id, created\_at, 3 more }

Admin bulk-dismissed join requests.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_join\_requests\_bulk\_dismissed"

OrgMagicLinkSecondFactorToggled object { actor, enabled, id, 4 more }

Organization magic link second factor was toggled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

enabled: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_magic\_link\_second\_factor\_toggled"

OrgMemberInvitesDisabled object { actor, id, created\_at, 3 more }

Admin disabled member invites for the organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_member\_invites\_disabled"

OrgMemberInvitesEnabled object { actor, id, created\_at, 3 more }

Admin enabled member invites for the organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_member\_invites\_enabled"

OrgMembersExported object { actor, id, created\_at, 3 more }

Organization members list was exported as CSV.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_members\_exported"

OrgParentJoinProposalCreated object { actor, id, created\_at, 3 more }

Organization parent join proposal was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_parent\_join\_proposal\_created"

OrgParentSearchPerformed object { actor, id, created\_at, 3 more }

Organization parent search was performed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_parent\_search\_performed"

OrgSSOAddInitiated object { actor, id, created\_at, 3 more }

Organization SSO setup was initiated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_sso\_add\_initiated"

OrgSSOConnectionActivated object { actor, id, connection\_id, 5 more }

Organization SSO connection was activated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

connection\_id: optional string

connection\_type: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_sso\_connection\_activated"

OrgSSOConnectionDeactivated object { actor, id, connection\_id, 4 more }

Organization SSO connection was deactivated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

connection\_id: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_sso\_connection\_deactivated"

OrgSSOConnectionDeleted object { actor, id, connection\_id, 4 more }

Organization SSO connection was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

connection\_id: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_sso\_connection\_deleted"

OrgSSOGroupRoleMappingsUpdated object { actor, id, created\_at, 3 more }

Organization SSO group role mappings were updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_sso\_group\_role\_mappings\_updated"

OrgSSOProvisioningModeChanged object { actor, id, created\_at, 5 more }

Organization SSO provisioning mode was changed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

new\_mode: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

previous\_mode: optional string

type: optional "org\_sso\_provisioning\_mode\_changed"

OrgSSOSeatTierAssignmentToggled object { actor, enabled, id, 4 more }

Organization SSO seat tier assignment was toggled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

enabled: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_sso\_seat\_tier\_assignment\_toggled"

OrgSSOSeatTierMappingsUpdated object { actor, id, created\_at, 3 more }

Organization SSO seat tier mappings were updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_sso\_seat\_tier\_mappings\_updated"

OrgSSOToggled object { actor, enabled, id, 4 more }

Organization SSO was toggled on or off.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

enabled: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_sso\_toggled"

OrgSyncDeletingSynchronizedFilesStarted object { actor, id, created\_at, 3 more }

Organization started deleting synchronized files.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_sync\_deleting\_synchronized\_files\_started"

OrgSyncSynchronizedFilesDeleted object { actor, id, created\_at, 3 more }

Organization synchronized files were deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_sync\_synchronized\_files\_deleted"

OrgTaintAdded object { actor, id, created\_at, 4 more }

A taint was added to an organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

taint: optional string

type: optional "org\_taint\_added"

OrgTaintRemoved object { actor, id, created\_at, 4 more }

A taint was removed from an organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

taint: optional string

type: optional "org\_taint\_removed"

OrgUserDeleted object { actor, id, created\_at, 5 more }

User was removed from organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

deleted\_user\_email: optional string

deleted\_user\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_user\_deleted"

OrgUserInviteAccepted object { actor, id, created\_at, 4 more }

Organization user invite was accepted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

invite\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_user\_invite\_accepted"

OrgUserInviteDeleted object { actor, id, created\_at, 4 more }

Organization user invite was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

invite\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_user\_invite\_deleted"

OrgUserInviteReSent object { actor, id, created\_at, 4 more }

Organization user invite was re-sent.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

invited\_email: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_user\_invite\_re\_sent"

OrgUserInviteRejected object { actor, id, created\_at, 4 more }

Organization user invite was rejected.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

invite\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_user\_invite\_rejected"

OrgUserInviteSent object { actor, id, created\_at, 5 more }

Organization user invite was sent.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

invited\_email: optional string

invited\_role: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_user\_invite\_sent"

OrgUserLeft object { actor, id, created\_at, 4 more }

User removed themselves from organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

previous\_role: optional string

type: optional "org\_user\_left"

OrgUserViewed object { actor, user\_id, id, 4 more }

An organization user was viewed.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

user\_id: string

Tagged ID of the viewed user

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_user\_viewed"

OrgUsersListed object { actor, id, created\_at, 3 more }

Organization users were listed.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_users\_listed"

OrgWorkAcrossAppsDisabled object { actor, id, created\_at, 3 more }

Organization Work Across Apps was disabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_work\_across\_apps\_disabled"

OrgWorkAcrossAppsEnabled object { actor, id, created\_at, 3 more }

Organization Work Across Apps was enabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "org\_work\_across\_apps\_enabled"

OrganizationAddressUpdated object { actor, id, billing\_address\_updated, 7 more }

The organization's billing or shipping address was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

billing\_address\_updated: optional boolean

billing\_name\_updated: optional boolean

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

shipping\_address\_updated: optional boolean

shipping\_name\_updated: optional boolean

type: optional "organization\_address\_updated"

OrganizationIconDeleted object { actor, id, created\_at, 3 more }

Organization's custom icon deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "organization\_icon\_deleted"

OrganizationIconUpdated object { actor, id, created\_at, 3 more }

Organization's custom icon uploaded or replaced.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "organization\_icon\_updated"

ClaudeOrganizationSettingsUpdated object { actor, updates, id, 4 more }

Organization settings were updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

updates: array of object { current\_value, previous\_value, type }  or object { current\_value, previous\_value, type }  or object { current\_value, previous\_value, type }  or 38 more

One of the following:

OrganizationName object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: optional "name"

OrganizationCapabilities object { current\_value, previous\_value, type }

current\_value: array of string

previous\_value: array of string

type: optional "capabilities"

OrganizationRedactContent object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "redact\_content"

PublicProjectsEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "public\_projects\_enabled"

WebSearchEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "web\_search\_enabled"

GeolocationEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "geolocation\_enabled"

OrgMemoryEnabledSetting object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "enabled\_saffron"

DataRetentionPeriods object { current\_value, previous\_value, type }

current\_value: array of object { data\_type, duration, timescale }

data\_type: "all" or "chat" or "project"

One of the following:

"all"

"chat"

"project"

duration: number

timescale: "day" or "indefinite" or "month"

One of the following:

"day"

"indefinite"

"month"

previous\_value: array of object { data\_type, duration, timescale }

data\_type: "all" or "chat" or "project"

One of the following:

"all"

"chat"

"project"

duration: number

timescale: "day" or "indefinite" or "month"

One of the following:

"day"

"indefinite"

"month"

type: optional "data\_retention\_periods"

MembersLimit object { current\_value, previous\_value, type }

current\_value: number

previous\_value: number

type: optional "members\_limit"

ClaudeAPIInArtifactsEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_api\_in\_artifacts\_enabled"

WorkbenchCompletionFeedbackEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "workbench\_completion\_feedback\_enabled"

ClaudeAICompletionFeedbackEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_ai\_completion\_feedback\_enabled"

ClaudeAIIntegrationSharingEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_ai\_integration\_sharing\_enabled"

ClaudeAIChatSharingEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_ai\_chat\_sharing\_enabled"

ClaudeAiccrSharingEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_ai\_ccr\_sharing\_enabled"

BatchesDownloadUiVisibility object { current\_value, previous\_value, type }

current\_value: "all" or "none" or "selected"

One of the following:

"all"

"none"

"selected"

previous\_value: "all" or "none" or "selected"

One of the following:

"all"

"none"

"selected"

type: optional "batches\_download\_ui\_visibility"

AllowedInviteDomains object { current\_value, previous\_value, type }

current\_value: array of string

previous\_value: array of string

type: optional "allowed\_invite\_domains"

WebSearchAPISettingsChanged object { current\_value, previous\_value, type }

current\_value: object { domain\_filters, is\_enabled }

domain\_filters: object { allowed\_domains, blocked\_domains }

Allowed/blocked domain filters shared by web\_search and web\_fetch tools.

allowed\_domains: optional array of string

blocked\_domains: optional array of string

is\_enabled: boolean

previous\_value: object { domain\_filters, is\_enabled }

domain\_filters: object { allowed\_domains, blocked\_domains }

Allowed/blocked domain filters shared by web\_search and web\_fetch tools.

allowed\_domains: optional array of string

blocked\_domains: optional array of string

is\_enabled: boolean

type: optional "web\_search\_api\_settings"

WebFetchAPISettingsChanged object { current\_value, previous\_value, type }

current\_value: object { domain\_filters, is\_enabled }

domain\_filters: object { allowed\_domains, blocked\_domains }

Allowed/blocked domain filters shared by web\_search and web\_fetch tools.

allowed\_domains: optional array of string

blocked\_domains: optional array of string

is\_enabled: boolean

previous\_value: object { domain\_filters, is\_enabled }

domain\_filters: object { allowed\_domains, blocked\_domains }

Allowed/blocked domain filters shared by web\_search and web\_fetch tools.

allowed\_domains: optional array of string

blocked\_domains: optional array of string

is\_enabled: boolean

type: optional "web\_fetch\_api\_settings"

DefaultWorkspaceSettings object { current\_value, previous\_value, type }

current\_value: object { enable\_api\_keys }

enable\_api\_keys: optional boolean

previous\_value: object { enable\_api\_keys }

enable\_api\_keys: optional boolean

type: optional "default\_workspace\_settings"

BatchesDownloadUiEnabledWorkspaceIDs object { current\_value, previous\_value, type }

current\_value: array of string

previous\_value: array of string

type: optional "batches\_download\_ui\_enabled\_workspace\_ids"

ClaudeCodeManagedSettings object { current\_value, current\_version, previous\_value, 3 more }

The organization's Claude Code managed settings were changed.

The full previous and current settings content is provided in the
`previous_value` and `current_value` fields.

current\_value: optional map[unknown]

current\_version: optional number

previous\_value: optional map[unknown]

previous\_version: optional number

settings\_uuid: optional string

type: optional "claude\_code\_managed\_settings"

AccountSessionDurationSeconds object { current\_value, previous\_value, type }

Tracks changes to the enterprise account session duration setting (in seconds).

current\_value: number

previous\_value: number

type: optional "account\_session\_duration\_seconds"

VcsConnections object { current\_value, previous\_value, type }

Tracks changes to VCS (GitHub, etc.) organization connections.

current\_value: array of object { org\_name, type, metadata, org\_id }

org\_name: string

type: "github"

Supported Version Control System providers.

metadata: optional map[string]

org\_id: optional string

previous\_value: array of object { org\_name, type, metadata, org\_id }

org\_name: string

type: "github"

Supported Version Control System providers.

metadata: optional map[string]

org\_id: optional string

type: optional "vcs\_connections"

DisabledAdminRequestTypes object { current\_value, previous\_value, type }

Tracks changes to which admin request types are disabled.

current\_value: array of string

previous\_value: array of string

type: optional "disabled\_admin\_request\_types"

CodeExecutionNetworkEgressEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "code\_execution\_network\_egress\_enabled"

CodeExecutionDomainAllowlistChanged object { current\_value, previous\_value, type }

current\_value: array of string

previous\_value: array of string

type: optional "code\_execution\_domain\_allowlist\_changed"

CodeExecutionDomainAllowlistTemplateChanged object { current\_value, previous\_value, type }

current\_value: "custom" or "full\_egress" or "package\_managers"

One of the following:

"custom"

"full\_egress"

"package\_managers"

previous\_value: "custom" or "full\_egress" or "package\_managers"

One of the following:

"custom"

"full\_egress"

"package\_managers"

type: optional "code\_execution\_domain\_allowlist\_template\_changed"

ChatEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "chat\_enabled"

ClaudeCodeQuickWebSetupEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_code\_quick\_web\_setup\_enabled"

ClaudeCodeTeamMemoryMode object { current\_value, previous\_value, type }

current\_value: "all\_org\_members" or "github\_repo" or "off" or "specific\_groups"

One of the following:

"all\_org\_members"

"github\_repo"

"off"

"specific\_groups"

previous\_value: "all\_org\_members" or "github\_repo" or "off" or "specific\_groups"

One of the following:

"all\_org\_members"

"github\_repo"

"off"

"specific\_groups"

type: optional "claude\_code\_team\_memory\_mode"

BrowserExtensionSettingsUpdated object { current\_value, previous\_value, type }

current\_value: map[unknown]

previous\_value: map[unknown]

type: optional "browser\_extension\_settings"

DesktopExtensionAllowlistEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "is\_desktop\_extension\_allowlist\_enabled"

ClaudeDesignEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_ai\_design\_enabled"

ClaudeAISkillSharingEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_ai\_skill\_sharing\_enabled"

ClaudeAISkillSharingOrgEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_ai\_skill\_sharing\_org\_enabled"

ClaudeCodeRemoteControlEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_code\_remote\_control\_enabled"

ClaudeCodeRoutinesEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_code\_routines\_enabled"

FrontierServicesDataUseEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "frontier\_services\_data\_use\_enabled"

LtiCourseProjectsEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "lti\_course\_projects\_enabled"

ManagedAgentsEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "managed\_agents\_enabled"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_organization\_settings\_updated"

OwnedProjectsAccessRestored object { actor, id, created\_at, 4 more }

Access to owned projects was restored.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "owned\_projects\_access\_restored"

user\_id: optional string

PaymentMethodUpdated object { actor, id, created\_at, 3 more }

The organization's default payment method was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "payment\_method\_updated"

PhoneCodeSent object { actor, id, created\_at, 3 more }

User requested a phone verification code.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "phone\_code\_sent"

PhoneCodeVerified object { actor, id, created\_at, 3 more }

User successfully verified their phone code.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "phone\_code\_verified"

PlatformAPIKeyCreated object { actor, api\_key\_id, id, 4 more }

An API key was created.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

api\_key\_id: string

Tagged ID of the created API key

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_api\_key\_created"

PlatformAPIKeyUpdated object { actor, api\_key\_id, updates, 5 more }

An API key was updated.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

api\_key\_id: string

Tagged ID of the updated API key

updates: array of object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: "name" or "status" or "workspace"

One of the following:

"name"

"status"

"workspace"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_api\_key\_updated"

PlatformCostReportViewed object { actor, id, created\_at, 3 more }

The cost report was viewed.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_cost\_report\_viewed"

PlatformFederationIssuerArchived object { actor, federation\_issuer\_id, id, 4 more }

An OIDC federation issuer was archived.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

federation\_issuer\_id: string

Tagged ID of the archived issuer

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_federation\_issuer\_archived"

PlatformFederationIssuerUpdated object { actor, federation\_issuer\_id, updates, 5 more }

An OIDC federation issuer was updated.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

federation\_issuer\_id: string

Tagged ID of the updated issuer

updates: array of object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: "ca\_cert\_pem\_sha256" or "check\_jti" or "discovery\_base" or 7 more

One of the following:

"ca\_cert\_pem\_sha256"

"check\_jti"

"discovery\_base"

"issuer\_url"

"jwks\_keys\_sha256"

"jwks\_polling\_disabled\_at"

"jwks\_source"

"jwks\_url"

"max\_jwt\_lifetime\_seconds"

"name"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_federation\_issuer\_updated"

PlatformFederationRuleArchived object { actor, federation\_rule\_id, id, 4 more }

An OIDC federation rule was archived.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

federation\_rule\_id: string

Tagged ID of the archived rule

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_federation\_rule\_archived"

PlatformFederationRuleUpdated object { actor, federation\_rule\_id, updates, 5 more }

An OIDC federation rule was updated.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

federation\_rule\_id: string

Tagged ID of the updated rule

updates: array of object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: "applies\_to\_all\_workspaces" or "attributes" or "description" or 11 more

One of the following:

"applies\_to\_all\_workspaces"

"attributes"

"description"

"match\_audience"

"match\_claims"

"match\_condition"

"match\_subject\_prefix"

"name"

"oauth\_scope"

"target\_id"

"target\_lookup\_attr"

"target\_type"

"token\_lifetime\_seconds"

"workspace\_id"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_federation\_rule\_updated"

PlatformFederationRuleWorkspaceAdded object { actor, federation\_rule\_id, workspace\_id, 5 more }

A federation rule was enabled for a workspace.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

federation\_rule\_id: string

Tagged ID of the federation rule

workspace\_id: string

Tagged ID of the workspace the rule was enabled for

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_federation\_rule\_workspace\_added"

PlatformFederationRuleWorkspaceRemoved object { actor, federation\_rule\_id, workspace\_id, 5 more }

A federation rule was disabled for a workspace.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

federation\_rule\_id: string

Tagged ID of the federation rule

workspace\_id: string

Tagged ID of the workspace the rule was disabled for

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_federation\_rule\_workspace\_removed"

PlatformFileContentDownloaded object { actor, file\_id, id, 4 more }

Activity logged when file content is downloaded via GET /v1/files/{file\_id}/content.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

file\_id: string

The tagged ID of the downloaded file

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_file\_content\_downloaded"

PlatformFileDeleted object { actor, file\_id, id, 4 more }

Activity logged when a file is deleted via DELETE /v1/files/{file\_id}.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

file\_id: string

The tagged ID of the deleted file

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_file\_deleted"

PlatformFileUploaded object { actor, file\_id, id, 5 more }

Activity logged when a file is uploaded via POST /v1/files.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

file\_id: string

The tagged ID of the uploaded file

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

session\_id: optional string

The tagged session ID (agent-api only)

type: optional "platform\_file\_uploaded"

PlatformServiceAccountArchived object { actor, service\_account\_id, id, 4 more }

A service account was archived.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

service\_account\_id: string

Tagged ID of the archived service account

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_service\_account\_archived"

PlatformServiceAccountUpdated object { actor, service\_account\_id, updates, 5 more }

A service account was updated.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

service\_account\_id: string

Tagged ID of the updated service account

updates: array of object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: "description"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_service\_account\_updated"

PlatformServiceAccountWorkspaceMemberAdded object { actor, service\_account\_id, workspace\_id, 5 more }

A service account was added as a member of a workspace.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

service\_account\_id: string

Tagged ID of the service account

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_service\_account\_workspace\_member\_added"

PlatformServiceAccountWorkspaceMemberRemoved object { actor, service\_account\_id, workspace\_id, 5 more }

A service account was removed from a workspace.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

service\_account\_id: string

Tagged ID of the service account

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_service\_account\_workspace\_member\_removed"

PlatformServiceAccountWorkspaceMemberUpdated object { actor, service\_account\_id, updates, 6 more }

A service account's workspace membership role was updated.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

service\_account\_id: string

Tagged ID of the service account

updates: array of object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: "workspace\_role"

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_service\_account\_workspace\_member\_updated"

PlatformSigningKeyCreated object { actor, algorithm, key\_backing\_type, 7 more }

Activity logged when a new request-signing key is registered for the org.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

algorithm: string

The signing algorithm (e.g. ecdsa-p256-sha256)

key\_backing\_type: string

The backing type of the key (IN\_MEMORY or CLOUD\_KMS)

signing\_key\_id: string

The tagged ID of the created signing key

status: string

The initial status of the key (ACTIVE or PENDING)

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_signing\_key\_created"

PlatformSigningKeyDeleted object { actor, algorithm, key\_backing\_type, 7 more }

Activity logged when a signing key is permanently deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

algorithm: string

The algorithm of the deleted key

key\_backing\_type: string

The backing type of the deleted key (IN\_MEMORY or CLOUD\_KMS)

key\_name: string

The name of the deleted key

signing\_key\_id: string

The tagged ID of the deleted signing key

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_signing\_key\_deleted"

PlatformSigningKeyRotated object { actor, algorithm, key\_group\_identifier, 7 more }

Activity logged when an in-memory signing key is rotated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

algorithm: string

The algorithm of the new key

key\_group\_identifier: string

The key group identifier linking old and new keys

new\_signing\_key\_id: string

The tagged ID of the newly created key

old\_signing\_key\_id: string

The tagged ID of the expired old key

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_signing\_key\_rotated"

PlatformSkillVersionCreated object { actor, skill\_id, version, 5 more }

Activity logged when a skill version is created via POST /v1/skills/{skill\_id}/versions.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

skill\_id: string

The tagged ID of the skill

version: string

The version number of the created version

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_skill\_version\_created"

PlatformSkillVersionDeleted object { actor, skill\_id, version, 5 more }

Activity logged when a skill version is deleted via DELETE /v1/skills/{skill\_id}/versions/{version}.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

skill\_id: string

The tagged ID of the skill

version: string

The version number of the deleted version

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_skill\_version\_deleted"

PlatformSpendLimitAlertEmailsUpdated object { actor, id, alert\_emails, 5 more }

Spend limit alert email addresses and role targets were updated for an org.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

alert\_emails: optional array of string

Updated list of alert email addresses.

alerted\_roles: optional array of string

Updated list of alerted roles.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_spend\_limit\_alert\_emails\_updated"

PlatformSpendLimitCreated object { actor, id, created\_at, 5 more }

An org-level fixed-dollar spend limit was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

limit\_action: optional string

The action taken when the limit is reached (notify\_only or notify\_and\_pause).

limit\_usd: optional number

The spend limit threshold in USD cents.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_spend\_limit\_created"

PlatformSpendLimitDeleted object { actor, id, created\_at, 4 more }

An org-level spend limit was removed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

spend\_limit\_id: optional string

UUID of the deleted spend limit.

type: optional "platform\_spend\_limit\_deleted"

PlatformSpendLimitUpdated object { actor, id, created\_at, 5 more }

An org-level spend limit snooze/ignore state was changed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

ignore: optional boolean

Whether the limit is being snoozed (ignored).

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

spend\_limit\_id: optional string

UUID of the spend limit.

type: optional "platform\_spend\_limit\_updated"

PlatformUsageReportClaudeCodeViewed object { actor, id, created\_at, 3 more }

The Claude Code usage report was viewed.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_usage\_report\_claude\_code\_viewed"

PlatformUsageReportMessagesViewed object { actor, id, created\_at, 3 more }

The messages usage report was viewed.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_usage\_report\_messages\_viewed"

PlatformWorkspaceArchived object { actor, workspace\_id, id, 4 more }

A workspace was archived.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

workspace\_id: string

Tagged ID of the archived workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_workspace\_archived"

PlatformWorkspaceCreated object { actor, workspace\_id, id, 4 more }

A workspace was created.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

workspace\_id: string

Tagged ID of the created workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_workspace\_created"

PlatformWorkspaceMemberAdded object { actor, user\_id, workspace\_id, 5 more }

A member was added to a workspace.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

user\_id: string

Tagged ID of the added member

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_workspace\_member\_added"

PlatformWorkspaceMemberRemoved object { actor, user\_id, workspace\_id, 5 more }

A member was removed from a workspace.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

user\_id: string

Tagged ID of the removed member

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_workspace\_member\_removed"

PlatformWorkspaceMemberUpdated object { actor, updates, user\_id, 6 more }

A workspace member was updated.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

updates: array of object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: "workspace\_role"

user\_id: string

Tagged ID of the updated member

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_workspace\_member\_updated"

PlatformWorkspaceMemberViewed object { actor, user\_id, workspace\_id, 5 more }

A workspace member was viewed.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

user\_id: string

Tagged ID of the viewed member

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_workspace\_member\_viewed"

PlatformWorkspaceMembersListed object { actor, workspace\_id, id, 4 more }

Workspace members were listed.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_workspace\_members\_listed"

PlatformWorkspaceRateLimitDeleted object { actor, limiter\_type, model\_group, 6 more }

A workspace rate limit was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

limiter\_type: string

Type of rate limiter

model\_group: string

Model group the rate limit applied to

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_workspace\_rate\_limit\_deleted"

PlatformWorkspaceRateLimitUpdated object { actor, limiter\_type, model\_group, 7 more }

A workspace rate limit was created or updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

limiter\_type: string

Type of rate limiter

model\_group: string

Model group the rate limit applies to

value: number

New rate limit value

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_workspace\_rate\_limit\_updated"

PlatformWorkspaceUpdated object { actor, updates, workspace\_id, 5 more }

A workspace was updated.

actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }

One of the following:

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

updates: array of object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: "allowed\_inference\_geos" or "default\_inference\_geo" or "display\_color" or "name"

One of the following:

"allowed\_inference\_geos"

"default\_inference\_geo"

"display\_color"

"name"

workspace\_id: string

Tagged ID of the updated workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "platform\_workspace\_updated"

ClaudePluginCreated object { actor, id, created\_at, 5 more }

Plugin was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

plugin\_id: optional string

plugin\_name: optional string

type: optional "claude\_plugin\_created"

ClaudePluginDeleted object { actor, id, created\_at, 5 more }

Plugin was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

plugin\_id: optional string

plugin\_name: optional string

type: optional "claude\_plugin\_deleted"

PluginInstallationPreferenceUpdated object { actor, marketplace\_id, plugin\_name, 9 more }

An org admin changed the installation preference for a plugin.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

marketplace\_id: string

Marketplace ID

plugin\_name: string

Plugin name

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

action: optional string

Action taken (e.g. 'deleted' for clearing an override)

created\_at: optional string

When this activity occurred.

group\_id: optional string

Tagged group ID for group-level overrides (null for org-level)

group\_name: optional string

Group name for group-level overrides

installation\_preference: optional string

New installation preference value (set only when action is an update; null for delete actions)

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "plugin\_installation\_preference\_updated"

ClaudePluginReplaced object { actor, id, created\_at, 5 more }

Plugin was replaced.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

plugin\_id: optional string

plugin\_name: optional string

type: optional "claude\_plugin\_replaced"

ClaudePluginUpdated object { actor, id, created\_at, 5 more }

Plugin was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

plugin\_id: optional string

plugin\_name: optional string

type: optional "claude\_plugin\_updated"

PrepaidAutoRechargeDisabled object { actor, id, created\_at, 3 more }

Auto-recharge was disabled for API prepaid org.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "prepaid\_auto\_recharge\_disabled"

PrepaidAutoRechargeUpdated object { actor, id, created\_at, 5 more }

Auto-recharge settings were updated for API prepaid org.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

target\_amount: optional number

Target recharge amount in minor units.

threshold\_amount: optional number

Threshold amount to trigger recharge in minor units.

type: optional "prepaid\_auto\_recharge\_updated"

PrepaidExtraUsageAutoReloadDisabled object { actor, id, created\_at, 3 more }

Prepaid usage credit auto-reload was disabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "prepaid\_extra\_usage\_auto\_reload\_disabled"

PrepaidExtraUsageAutoReloadEnabled object { actor, id, created\_at, 3 more }

Prepaid usage credit auto-reload was enabled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "prepaid\_extra\_usage\_auto\_reload\_enabled"

PrepaidExtraUsageAutoReloadSettingsUpdated object { actor, id, created\_at, 3 more }

Prepaid usage credit auto-reload settings were updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "prepaid\_extra\_usage\_auto\_reload\_settings\_updated"

PrimaryOwnerTransferred object { actor, new\_owner\_id, previous\_owner\_id, 5 more }

Primary owner role was transferred to another org member.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

new\_owner\_id: string

previous\_owner\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "primary\_owner\_transferred"

ClaudeProjectArchived object { actor, claude\_project\_id, id, 4 more }

A Claude project was archived.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_archived"

ClaudeProjectCreated object { actor, claude\_project\_id, id, 4 more }

A Claude project was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_created"

ClaudeProjectDeleted object { actor, claude\_project\_id, id, 4 more }

A Claude project was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_deleted"

ClaudeProjectDocumentAccessFailed object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

An attempt to access a document in a Claude project failed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_document\_access\_failed"

ClaudeProjectDocumentDeleted object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

A document was deleted from a Claude project.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_document\_deleted"

ClaudeProjectDocumentDeletionFailed object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

A request to delete a document from a Claude project failed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_document\_deletion\_failed"

ClaudeProjectDocumentUploaded object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

A document was uploaded to a Claude project.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_document\_uploaded"

ClaudeProjectDocumentViewed object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

A document in a Claude project was viewed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_document\_viewed"

ClaudeProjectFileAccessFailed object { actor, claude\_file\_id, claude\_project\_id, 5 more }

An attempt to access a file in a Claude project failed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_file\_id: string

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_file\_access\_failed"

ClaudeProjectFileDeleted object { actor, claude\_file\_id, claude\_project\_id, 5 more }

A file was deleted from a Claude project.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_file\_id: string

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_file\_deleted"

ClaudeProjectFileDeletionFailed object { actor, claude\_file\_id, claude\_project\_id, 5 more }

A request to delete a file from a Claude project failed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_file\_id: string

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_file\_deletion\_failed"

ClaudeProjectFileUploaded object { actor, claude\_file\_id, claude\_project\_id, 6 more }

A file was uploaded to a Claude project.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_file\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_file\_uploaded"

ClaudeProjectReported object { actor, claude\_project\_id, id, 4 more }

A Claude project was reported.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_reported"

ClaudeProjectSharingUpdated object { actor, audience, claude\_project\_id, 5 more }

A Claude project's sharing settings were updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

audience: array of object { type }  or object { type }

Sharing audience for the project. If empty, this it's only visible to the creating user.

One of the following:

ProjectSharingAudiencePublic object { type }

type: optional "public"

ProjectSharingAudienceOrganization object { type }

type: optional "organization"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_project\_sharing\_updated"

ClaudeProjectViewed object { actor, claude\_project\_id, id, 5 more }

A Claude project was viewed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

preview\_only: optional boolean

type: optional "claude\_project\_viewed"

ClaudePubsecIdentityConfigured object { actor, idp\_saml\_config\_updated, magic\_link\_toggled, 6 more }

SAML IdP configuration updated for a public sector organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

idp\_saml\_config\_updated: boolean

magic\_link\_toggled: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

magic\_link\_enabled: optional boolean

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_pubsec\_identity\_configured"

RbacRoleAssigned object { actor, principal\_id, principal\_type, 6 more }

Admin assigned an RBAC custom role to a principal.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

principal\_id: string

Tagged ID of the principal

principal\_type: string

Type of principal: account or group

role\_id: string

Tagged ID of the role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "rbac\_role\_assigned"

RbacRoleCreated object { actor, role\_id, role\_name, 5 more }

Admin created an RBAC custom role.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

role\_id: string

Tagged ID of the created role

role\_name: string

Name of the created role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "rbac\_role\_created"

RbacRoleDeleted object { actor, role\_id, id, 4 more }

Admin deleted an RBAC custom role.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

role\_id: string

Tagged ID of the deleted role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "rbac\_role\_deleted"

RbacRolePermissionAdded object { action, actor, resource\_id, 7 more }

Admin added a permission to an RBAC custom role.

action: string

Action permitted on the resource

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

resource\_id: string

ID of the resource

resource\_type: string

Type of resource the permission applies to

role\_id: string

Tagged ID of the role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "rbac\_role\_permission\_added"

RbacRolePermissionRemoved object { action, actor, resource\_id, 7 more }

Admin removed a permission from an RBAC custom role.

action: string

Action that was permitted on the resource

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

resource\_id: string

ID of the resource

resource\_type: string

Type of resource the permission applied to

role\_id: string

Tagged ID of the role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "rbac\_role\_permission\_removed"

RbacRoleUnassigned object { actor, principal\_id, principal\_type, 6 more }

Admin unassigned an RBAC custom role from a principal.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

principal\_id: string

Tagged ID of the principal

principal\_type: string

Type of principal: account or group

role\_id: string

Tagged ID of the role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "rbac\_role\_unassigned"

RbacRoleUpdated object { actor, role\_id, id, 4 more }

Admin updated an RBAC custom role.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

role\_id: string

Tagged ID of the updated role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "rbac\_role\_updated"

RoleAssignmentGranted object { actor, id, created\_at, 8 more }

Role assignment was granted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

resource\_id: optional string

resource\_type: optional string

role: optional string

target\_id: optional string

target\_type: optional string

type: optional "role\_assignment\_granted"

RoleAssignmentRevoked object { actor, id, created\_at, 8 more }

Role assignment was revoked.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AnthropicActor object { email\_address, type }

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

resource\_id: optional string

resource\_type: optional string

role: optional string

target\_id: optional string

target\_type: optional string

type: optional "role\_assignment\_revoked"

SSOLoginFailed object { actor, id, created\_at, 3 more }

An SSO sign-in attempt failed.

actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "sso\_login\_failed"

SSOLoginInitiated object { actor, id, created\_at, 3 more }

A user started an SSO sign-in flow.

actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "sso\_login\_initiated"

SSOLoginSucceeded object { actor, id, auth\_method, 5 more }

A user successfully signed in with SSO.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

auth\_method: optional "sso"

The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

created\_at: optional string

When this activity occurred.

mfa\_method: optional "not\_used"

The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "sso\_login\_succeeded"

SSOSecondFactorMagicLink object { actor, id, created\_at, 3 more }

SSO second factor magic link was used.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "sso\_second\_factor\_magic\_link"

ScimUserCreated object { actor, user\_id, id, 4 more }

A SCIM user was provisioned.

actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

user\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "scim\_user\_created"

ScimUserDeleted object { actor, user\_id, id, 4 more }

A SCIM user was deleted.

actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

user\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "scim\_user\_deleted"

ScimUserUpdated object { actor, user\_id, id, 4 more }

A SCIM user was updated.

actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

One of the following:

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type }

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

user\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "scim\_user\_updated"

ScopedAPIKeyDeleted object { actor, api\_key\_id, api\_key\_name, 6 more }

A scoped API key was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

api\_key\_id: string

Tagged ID of the deleted scoped API key

api\_key\_name: string

Name of the deleted scoped API key

scopes: array of string

Scopes the deleted key had

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "scoped\_api\_key\_deleted"

ScopedAPIKeyUpdated object { actor, api\_key\_id, updates, 5 more }

A scoped API key was renamed or its activation state changed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

api\_key\_id: string

Tagged ID of the updated scoped API key

updates: array of object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: "activation\_state" or "name"

One of the following:

"activation\_state"

"name"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "scoped\_api\_key\_updated"

SeatTierChangesCancelled object { actor, id, created\_at, 3 more }

Scheduled seat tier downgrades were cancelled.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "seat\_tier\_changes\_cancelled"

SeatTiersPurchased object { actor, id, created\_at, 4 more }

Seat tiers were purchased or upgraded on a subscription.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

item\_allocations: optional map[number]

Desired seat tier allocations (item type to quantity).

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "seat\_tiers\_purchased"

ServiceCreated object { actor, service\_name, id, 4 more }

Activity logged when an org service is explicitly created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

service\_name: string

The org service name (e.g., 'external')

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "service\_created"

ServiceDeleted object { actor, service\_name, id, 4 more }

Activity logged when an org service is deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

service\_name: string

The org service name (e.g., 'external')

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "service\_deleted"

ServiceKeyCreated object { actor, is\_service\_created, key\_name, 8 more }

Activity logged when a new org service key is created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

is\_service\_created: boolean

Whether the org service was implicitly created in this request

key\_name: string

The human-readable name of the key

scopes: array of string

The scopes granted to this service key

service\_key\_id: string

The ID of the created service key

service\_name: string

The service name this key belongs to

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "service\_key\_created"

ServiceKeyRevoked object { actor, service\_key\_id, service\_name, 5 more }

Activity logged when an org service key is revoked.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

service\_key\_id: string

The tagged ID of the revoked service key

service\_name: string

The service name this key belongs to

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "service\_key\_revoked"

SessionRevoked object { actor, id, created\_at, 3 more }

User revoked a specific session.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "session\_revoked"

SessionShareAccessed object { actor, id, created\_at, 4 more }

Session share was accessed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

share\_id: optional string

type: optional "session\_share\_accessed"

SessionShareCreated object { actor, id, created\_at, 4 more }

Session share was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

share\_id: optional string

type: optional "session\_share\_created"

SessionShareRevoked object { actor, id, created\_at, 4 more }

Session share was revoked.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address }

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

share\_id: optional string

type: optional "session\_share\_revoked"

ClaudeSkillCreated object { actor, id, created\_at, 5 more }

Skill was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

skill\_id: optional string

skill\_name: optional string

type: optional "claude\_skill\_created"

ClaudeSkillDeleted object { actor, id, created\_at, 5 more }

Skill was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

skill\_id: optional string

skill\_name: optional string

type: optional "claude\_skill\_deleted"

ClaudeSkillDisabled object { actor, id, created\_at, 5 more }

User disabled a skill for their account.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

skill\_id: optional string

skill\_name: optional string

type: optional "claude\_skill\_disabled"

ClaudeSkillEnabled object { actor, id, created\_at, 5 more }

User enabled a skill for their account.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

skill\_id: optional string

skill\_name: optional string

type: optional "claude\_skill\_enabled"

ClaudeSkillReplaced object { actor, id, created\_at, 5 more }

Skill was replaced.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

APIActor object { api\_key\_id, ip\_address, user\_agent, type }

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

skill\_id: optional string

skill\_name: optional string

type: optional "claude\_skill\_replaced"

SocialLoginSucceeded object { actor, provider, id, 6 more }

A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

provider: "apple" or "google" or "microsoft"

One of the following:

"apple"

"google"

"microsoft"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

auth\_method: optional "social"

The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

created\_at: optional string

When this activity occurred.

mfa\_method: optional "not\_used"

The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "social\_login\_succeeded"

SubscriptionCancellationScheduled object { actor, id, created\_at, 3 more }

Subscription cancellation was scheduled at end of billing period.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "subscription\_cancellation\_scheduled"

SubscriptionQuantityUpdated object { actor, added\_seats, new\_quantity, 6 more }

Contracted subscription seat quantity was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

added\_seats: number

new\_quantity: number

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

previous\_quantity: optional number

type: optional "subscription\_quantity\_updated"

SubscriptionRenewed object { actor, id, billing\_interval, 5 more }

A cancelled subscription was renewed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

billing\_interval: optional string

Billing interval (e.g. monthly, annual).

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

plan\_type: optional string

Plan type being renewed into (e.g. team).

type: optional "subscription\_renewed"

SubscriptionResumed object { actor, id, created\_at, 3 more }

A scheduled subscription cancellation was reversed.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "subscription\_resumed"

SubscriptionStarted object { actor, id, billing\_interval, 6 more }

A new subscription was created (Team or Enterprise).

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

billing\_interval: optional string

Billing interval (e.g. monthly, annual).

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

plan\_type: optional string

Type of subscription started (e.g. team, enterprise).

seat\_count: optional number

Number of seats purchased.

type: optional "subscription\_started"

SubscriptionUpgraded object { actor, id, created\_at, 5 more }

Subscription plan was upgraded (e.g. Team to Enterprise).

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

new\_plan: optional string

New plan type after upgrade.

old\_plan: optional string

Previous plan type.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "subscription\_upgraded"

TunnelTokenMinted object { actor, token\_id, id, 5 more }

An OAuth bearer token for the tunnel management API was minted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

token\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

token\_name: optional string

type: optional "tunnel\_token\_minted"

TunnelTokenRevoked object { actor, token\_id, id, 4 more }

An OAuth bearer token for the tunnel management API was revoked.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

token\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "tunnel\_token\_revoked"

UserConsentRecorded object { actor, consent\_type, entity\_id, 6 more }

User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

consent\_type: string

entity\_id: string

entity\_type: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "user\_consent\_recorded"

UserConsentRevoked object { actor, id, consent\_id, 7 more }

User revoked a previously granted consent for a specific entity.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

consent\_id: optional string

consent\_type: optional string

created\_at: optional string

When this activity occurred.

entity\_id: optional string

entity\_type: optional string

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "user\_consent\_revoked"

ClaudeUserRoleUpdated object { actor, current\_role, previous\_role, 7 more }

A user's role within the organization was changed, or the user was added to or removed from the organization.

actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }

One of the following:

UserActor object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type }

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"

current\_role: string

If null, then user was removed from the Organization

previous\_role: string

If null, then user was added to the Organization

user\_email: string

Email of the user whose role was changed

user\_id: string

ID of the user whose role was changed

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_user\_role\_updated"

ClaudeUserSettingsUpdated object { actor, updates, id, 4 more }

User updated their personal settings.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

updates: array of object { current\_value, previous\_value, type }  or object { current\_value, previous\_value, type }  or object { current\_value, previous\_value, type }  or 19 more

One of the following:

FullName object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: optional "full\_name"

DisplayName object { current\_value, previous\_value, type }

current\_value: string

previous\_value: string

type: optional "display\_name"

ArtifactsEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "artifacts\_enabled"

LatexEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "latex\_enabled"

AnalysisToolEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "analysis\_tool\_enabled"

ChatSuggestionsEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "chat\_suggestions\_enabled"

MultimodalPdfsEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "multimodal\_pdfs\_enabled"

GDriveEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "gdrive\_enabled"

GDriveIndexingEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "gdrive\_indexing\_enabled"

WebSearchEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "web\_search\_enabled"

GeolocationEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "geolocation\_enabled"

UserMemoryEnabledSetting object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "enabled\_saffron"

McpToolsEnabled object { current\_value, previous\_value, type }

current\_value: map[boolean]

previous\_value: map[boolean]

type: optional "mcp\_tools\_enabled"

CliOpPermissionsEnabled object { current\_value, previous\_value, type }

current\_value: map[string]

previous\_value: map[string]

type: optional "cli\_op\_permissions\_enabled"

GoogleDriveSearchEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "google\_drive\_search\_enabled"

GmailIntegrationEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "gmail\_integration\_enabled"

GoogleCalendarIntegrationEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "google\_calendar\_integration\_enabled"

ThinkingModeEnabled object { current\_value, previous\_value, type }

current\_value: "adaptive" or "extended" or "off"

One of the following:

"adaptive"

"extended"

"off"

previous\_value: "adaptive" or "extended" or "off"

One of the following:

"adaptive"

"extended"

"off"

type: optional "thinking\_mode\_enabled"

ResearchModeEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "research\_mode\_enabled"

ComputerUseEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "computer\_use\_enabled"

ClaudeAPIInArtifactsEnabled object { current\_value, previous\_value, type }

current\_value: boolean

previous\_value: boolean

type: optional "claude\_api\_in\_artifacts\_enabled"

ConversationPreferences object { type }

The 'conversation\_preferences' for the user were updated. Values omitted.

type: optional "conversation\_preferences"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "claude\_user\_settings\_updated"

WorkspaceMemberSpendLimitCreated object { actor, id, account\_id, 7 more }

A per-member or workspace-default Claude Code spend limit was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

account\_id: optional string

Tagged ID of the user (null for workspace-wide default).

created\_at: optional string

When this activity occurred.

limit\_action: optional string

The action taken when the limit is reached.

limit\_usd: optional number

The spend limit threshold in USD cents.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "workspace\_member\_spend\_limit\_created"

workspace\_id: optional string

Tagged ID of the workspace.

WorkspaceMemberSpendLimitDeleted object { actor, id, account\_id, 6 more }

A per-member or workspace-default Claude Code spend limit was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

account\_id: optional string

Tagged ID of the user (null for workspace-wide default).

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

spend\_limit\_id: optional string

UUID of the deleted spend limit.

type: optional "workspace\_member\_spend\_limit\_deleted"

workspace\_id: optional string

Tagged ID of the workspace.

WorkspaceMemberSpendLimitUpdated object { actor, id, account\_id, 7 more }

A per-member Claude Code spend limit amount was updated.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

account\_id: optional string

Tagged ID of the user (null for workspace-wide default).

created\_at: optional string

When this activity occurred.

new\_limit\_usd: optional number

The new spend limit threshold in USD cents.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

spend\_limit\_id: optional string

UUID of the spend limit.

type: optional "workspace\_member\_spend\_limit\_updated"

workspace\_id: optional string

Tagged ID of the workspace.

WorkspaceSpendLimitCreated object { actor, id, created\_at, 6 more }

A workspace-level API spend limit was created.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

limit\_action: optional string

The action taken when the limit is reached (notify\_only or notify\_and\_pause).

limit\_usd: optional number

The spend limit threshold in USD cents.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

type: optional "workspace\_spend\_limit\_created"

workspace\_id: optional string

Tagged ID of the workspace.

WorkspaceSpendLimitDeleted object { actor, id, created\_at, 5 more }

A workspace-level API spend limit was deleted.

actor: object { email\_address, ip\_address, user\_agent, 2 more }

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

Deprecatedorganization\_uuid: optional string

Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

spend\_limit\_id: optional string

UUID of the deleted spend limit.

type: optional "workspace\_spend\_limit\_deleted"

workspace\_id: optional string

Tagged ID of the workspace.

# Compliance APIOrganizations

# [List organizations](/docs/en/api/compliance/organizations/list)

GET/v1/compliance/organizations

# ModelsExpand Collapse

OrganizationListResponse object { data }

List of organizations under a parent organization.

data: array of object { created\_at, name, uuid }

List of organizations sorted by creation date, ascending

created\_at: string

Organization creation time (RFC 3339 format)

name: string

Organization name

uuid: string

Unique identifier for the organization (UUID format)

# Compliance APIOrganizationsUsers

# [List organization users](/docs/en/api/compliance/organizations/users/list)

GET/v1/compliance/organizations/{org\_uuid}/users

# ModelsExpand Collapse

UserListResponse object { id, created\_at, email, 2 more }

User member information for compliance responses.

id: string

User identifier (tagged ID)

created\_at: string

User account creation timestamp

email: string

User's current email address

full\_name: string

User's current full name

organization\_role: "admin" or "billing" or "claude\_code\_user" or 6 more

User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

One of the following:

"admin"

"billing"

"claude\_code\_user"

"developer"

"managed"

"membership\_admin"

"owner"

"primary\_owner"

"user"

# Compliance APIOrganizationsRoles

# [List Compliance Roles](/docs/en/api/compliance/organizations/roles/list)

GET/v1/compliance/organizations/{org\_uuid}/roles

# [Get Compliance Role](/docs/en/api/compliance/organizations/roles/retrieve)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

# ModelsExpand Collapse

RoleListResponse object { id, created\_at, description, 2 more }

Role information for compliance responses.

id: string

Role identifier (tagged ID)

created\_at: string

Role creation timestamp (ISO 8601)

description: string

Role description

name: string

Role name

updated\_at: string

Role last-updated timestamp (ISO 8601)

RoleRetrieveResponse object { id, created\_at, description, 2 more }

Role information for compliance responses.

id: string

Role identifier (tagged ID)

created\_at: string

Role creation timestamp (ISO 8601)

description: string

Role description

name: string

Role name

updated\_at: string

Role last-updated timestamp (ISO 8601)

# Compliance APIOrganizationsRolesPermissions

# [List Compliance Role Permissions](/docs/en/api/compliance/organizations/roles/permissions/list)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}/permissions

# ModelsExpand Collapse

PermissionListResponse object { action, resource\_id, resource\_type }

Permission granted by a role.

action: string

Action permitted on the resource

resource\_id: string

Identifier of the resource the permission applies to

resource\_type: string

Type of resource the permission applies to

# Compliance APIGroups

# [List Compliance Groups](/docs/en/api/compliance/groups/list)

GET/v1/compliance/groups

# [Get Compliance Group](/docs/en/api/compliance/groups/retrieve)

GET/v1/compliance/groups/{group\_id}

# ModelsExpand Collapse

GroupListResponse object { id, created\_at, description, 4 more }

Group information for compliance responses.

id: string

Group identifier (tagged ID)

created\_at: string

Group creation timestamp (ISO 8601)

description: string

Group description

name: string

Group name

roles: array of string

Role IDs assigned to this group.

source\_type: string

How the group was created ('direct' or 'scim')

updated\_at: string

Group last-updated timestamp (ISO 8601)

GroupRetrieveResponse object { id, created\_at, description, 4 more }

Group information for compliance responses.

id: string

Group identifier (tagged ID)

created\_at: string

Group creation timestamp (ISO 8601)

description: string

Group description

name: string

Group name

roles: array of string

Role IDs assigned to this group.

source\_type: string

How the group was created ('direct' or 'scim')

updated\_at: string

Group last-updated timestamp (ISO 8601)

# Compliance APIGroupsMembers

# [List Compliance Group Members](/docs/en/api/compliance/groups/members/list)

GET/v1/compliance/groups/{group\_id}/members

# ModelsExpand Collapse

MemberListResponse object { created\_at, email, updated\_at, user\_id }

Group member for compliance responses.

created\_at: string

Membership creation timestamp (ISO 8601)

email: string

Member email address

updated\_at: string

Membership last-updated timestamp (ISO 8601)

user\_id: string

Member user identifier (tagged ID)

# Compliance APIApps

# Compliance APIAppsChats

# [List chats](/docs/en/api/compliance/apps/chats/list)

GET/v1/compliance/apps/chats

# [Delete chat](/docs/en/api/compliance/apps/chats/delete)

DELETE/v1/compliance/apps/chats/{claude\_chat\_id}

# ModelsExpand Collapse

ChatListResponse object { id, created\_at, deleted\_at, 8 more }

Chat metadata for listing chats (without messages).

id: string

Chat ID

created\_at: string

Creation timestamp

deleted\_at: string

Deletion timestamp if deleted

href: string

URL to view this chat in claude.ai

model: string

Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

name: string

Chat name/title

Deprecatedorganization\_id: string

Organization ID this chat belongs to

organization\_uuid: string

Organization UUID this chat belongs to

project\_id: string

Project ID this chat belongs to

updated\_at: string

Last update timestamp

user: object { id, email\_address }

User information for the chat creator

id: string

User identifier

email\_address: string

User's email address

ChatDeleteResponse object { id, type }

Response for deleting a Claude chat.

id: string

The ID of the Claude chat that was deleted

type: optional "claude\_chat\_deleted"

Constant string confirming deletion

# Compliance APIAppsChatsMessages

# [Get chat messages](/docs/en/api/compliance/apps/chats/messages/list)

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

# ModelsExpand Collapse

MessageListResponse object { id, artifacts, content, 4 more }

A single message in a chat conversation.

id: string

Unique identifier for the message e.g. 'claude\_chat\_msg\_abcd1234'

artifacts: array of object { id, artifact\_type, title, version\_id }

Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string

MIME-like artifact type e.g. 'application/vnd.ant.code'

title: string

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'

content: array of object { text, type }

Content blocks within the message

text: string

Text content from human or assistant

type: "text"

created\_at: string

Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

files: array of object { id, filename, mime\_type }

Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

id: string

File ID

filename: string

Display name of the file

mime\_type: string

MIME type of the file when it was uploaded (e.g. 'application/pdf')

generated\_files: array of object { id, filename, mime\_type }

Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'. Treat as an opaque string; the encoding may change without notice.

filename: string

Display name of the generated file

mime\_type: string

MIME type reported by the tool that produced the file

role: "assistant" or "user"

Message sender (user or assistant)

One of the following:

"assistant"

"user"

# Compliance APIAppsChatsFiles

# [Get file metadata](/docs/en/api/compliance/apps/chats/files/retrieve)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

# [Delete file](/docs/en/api/compliance/apps/chats/files/delete)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

# [Download file content](/docs/en/api/compliance/apps/chats/files/download)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

# ModelsExpand Collapse

FileRetrieveResponse object { id, created\_at, filename, 4 more }

File metadata for GET /v1/compliance/apps/chats/files/{claude\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the file bytes.

id: string

File ID

created\_at: string

File creation timestamp

filename: string

Display name of the file, if set

md5: string

Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

message\_ids: array of string

Chat message IDs this file is attached to. A file can be referenced by multiple messages.

mime\_type: string

MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

size\_bytes: number

Size in bytes of the file's preferred downloadable variant, if known

FileDeleteResponse object { id, type }

Response for deleting a compliance file.

id: string

The ID of the file that was deleted

type: optional "claude\_file\_deleted"

Constant string confirming deletion

# Compliance APIAppsChatsGenerated Files

# [Get Claude-generated file metadata](/docs/en/api/compliance/apps/chats/generated_files/retrieve)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}

# [Download a Claude-generated file](/docs/en/api/compliance/apps/chats/generated_files/download)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

# ModelsExpand Collapse

GeneratedFileRetrieveResponse object { id, claude\_chat\_id, created\_at, 4 more }

Metadata for GET /v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the bytes. The owning chat is included since the id is opaque; to find the
specific message that produced the file, fetch
`/v1/compliance/apps/chats/{claude_chat_id}/messages` and match on
`generated_files[].id`.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'.

claude\_chat\_id: string

The chat this generated file belongs to

created\_at: string

File creation timestamp from Filestore

filename: string

Display name of the generated file

md5: string

Lowercase hex MD5 of the stored file, as recorded by Filestore. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

mime\_type: string

MIME type as recorded by Filestore, when available

size\_bytes: number

Size in bytes of the stored file, when available

# Compliance APIAppsProjects

# [List projects](/docs/en/api/compliance/apps/projects/list)

GET/v1/compliance/apps/projects

# [Get project details](/docs/en/api/compliance/apps/projects/retrieve)

GET/v1/compliance/apps/projects/{project\_id}

# [Delete project](/docs/en/api/compliance/apps/projects/delete)

DELETE/v1/compliance/apps/projects/{project\_id}

# ModelsExpand Collapse

ProjectListResponse object { id, created\_at, deleted\_at, 6 more }

Project information for compliance responses.

id: string

Project identifier (tagged ID)

created\_at: string

Project creation timestamp

deleted\_at: string

Timestamp when the project was deleted by an end user, or null otherwise

is\_private: boolean

If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

name: string

Project name

Deprecatedorganization\_id: string

Organization identifier (tagged ID)

organization\_uuid: string

Organization UUID this project belongs to

updated\_at: string

Project last update timestamp

user: object { id, email\_address }

User information for project creator.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

ProjectRetrieveResponse object { id, attachments\_count, chats\_count, 10 more }

Detailed project information for compliance responses.

id: string

Project identifier (tagged ID)

attachments\_count: number

Number of attachments contained within this project

chats\_count: number

Number of chats contained within this project

created\_at: string

Project creation timestamp

deleted\_at: string

Timestamp when the project was deleted by an end user, or null otherwise

description: string

Project description

instructions: string

Project's custom instructions / prompt

is\_private: boolean

If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

name: string

Project name

Deprecatedorganization\_id: string

Organization identifier (tagged ID)

organization\_uuid: string

Organization UUID this project belongs to

updated\_at: string

Project last update timestamp

user: object { id, email\_address }

User information for project creator.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

ProjectDeleteResponse object { id, type }

Response for deleting a Claude project.

id: string

The ID of the Claude project that was deleted

type: optional "claude\_project\_deleted"

Constant string confirming deletion.

# Compliance APIAppsProjectsAttachments

# [List project attachments](/docs/en/api/compliance/apps/projects/attachments/list)

GET/v1/compliance/apps/projects/{project\_id}/attachments

# ModelsExpand Collapse

AttachmentListResponse = object { id, created\_at, filename, 2 more }  or object { id, created\_at, filename, 2 more }

File attachment reference for compliance responses.

One of the following:

ComplianceProjectFileReference object { id, created\_at, filename, 2 more }

File attachment reference for compliance responses.

id: string

File identifier (e.g., 'claude\_file\_abcd')

created\_at: string

Creation timestamp (RFC 3339 format)

filename: string

Display name of the file (e.g., 'document.pdf')

mime\_type: string

MIME type of the file when it was uploaded (e.g., 'application/pdf')

type: "project\_file"

Discriminator marking this as a binary file

ComplianceProjectDocReference object { id, created\_at, filename, 2 more }

Project document attachment reference for compliance responses.

id: string

Project document identifier (e.g., 'claude\_proj\_doc\_abcd')

created\_at: string

Creation timestamp (RFC 3339 format)

filename: string

Display name of the document (e.g., 'document.txt')

mime\_type: "text/plain"

MIME type of the project document, always set to plain text

type: "project\_doc"

Discriminator marking this as a plain text document

# Compliance APIAppsProjectsDocuments

# [Get project document content](/docs/en/api/compliance/apps/projects/documents/retrieve)

GET/v1/compliance/apps/projects/documents/{document\_id}

# [Get project document metadata](/docs/en/api/compliance/apps/projects/documents/metadata)

GET/v1/compliance/apps/projects/documents/{document\_id}/metadata

# [Delete project document](/docs/en/api/compliance/apps/projects/documents/delete)

DELETE/v1/compliance/apps/projects/documents/{document\_id}

# ModelsExpand Collapse

DocumentRetrieveResponse object { id, content, created\_at, 2 more }

Project document information for compliance responses.

id: string

Project document identifier (tagged ID)

content: string

Document text content

created\_at: string

Document creation timestamp

filename: string

Document filename

user: object { id, email\_address }

User information for project creator.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

DocumentMetadataResponse object { id, claude\_project\_id, created\_at, 5 more }

Project document metadata for GET /v1/compliance/apps/projects/documents/{document\_id}/metadata.

Returns metadata only. Use the sibling endpoint (without `/metadata`)
to fetch the document text content.

id: string

Project document identifier (tagged ID)

claude\_project\_id: string

The project this document belongs to

created\_at: string

Document creation timestamp

filename: string

Document filename

md5: string

Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

mime\_type: "text/plain"

MIME type of the document content, always plain text

size\_bytes: number

Size in bytes of the document content (UTF-8 encoded)

user: object { id, email\_address }

User information for project creator.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

DocumentDeleteResponse object { id, type }

Response for deleting a project document.

id: string

The ID of the project document that was deleted

type: "claude\_project\_document\_deleted"

Constant string confirming deletion.

# Compliance APIAppsArtifacts

# [Get artifact metadata](/docs/en/api/compliance/apps/artifacts/retrieve)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}

# [Download artifact content](/docs/en/api/compliance/apps/artifacts/download)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}/content

# ModelsExpand Collapse

ArtifactRetrieveResponse object { id, artifact\_type, claude\_chat\_id, 5 more }

Artifact version metadata for GET /v1/compliance/apps/artifacts/{artifact\_version\_id}.

Returns metadata only. Use the sibling `/content` endpoint to fetch the
artifact body.

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string

MIME-like artifact type e.g. 'application/vnd.ant.code'

claude\_chat\_id: string

The chat this artifact belongs to

created\_at: string

Artifact version creation timestamp

md5: string

Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

size\_bytes: number

Size in bytes of the artifact content (UTF-8 encoded)

title: string

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'
