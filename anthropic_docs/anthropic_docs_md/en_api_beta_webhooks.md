# Webhooks

**Source:** http://platform.claude.com/docs/en/api/beta/webhooks

Copy page

cURL

# Webhooks

Helpers for receiving and verifying webhook events. Use `unwrap` in your SDK to verify signatures and parse payloads; see the [webhooks guide](/docs/en/managed-agents/webhooks) for handler examples.

Possible `data.type` values:

* `session.archived`
* `session.created`
* `session.deleted`
* `session.idled`
* `session.outcome_evaluation_ended`
* `session.pending`
* `session.requires_action`
* `session.running`
* `session.status_idled`
* `session.status_rescheduled`
* `session.status_run_started`
* `session.status_terminated`
* `session.thread_created`
* `session.thread_idled`
* `session.thread_terminated`
* `vault.archived`
* `vault.created`
* `vault.deleted`
* `vault_credential.archived`
* `vault_credential.created`
* `vault_credential.deleted`
* `vault_credential.refresh_failed`

# ModelsExpand Collapse

BetaWebhookEvent object { id, created\_at, data, type }

id: string

Unique event identifier for idempotency.

created\_at: string

RFC 3339 timestamp when the event occurred.

data: [BetaWebhookEventData](/docs/en/api/beta#beta_webhook_event_data)

One of the following:

BetaWebhookSessionCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string

BetaWebhookSessionPendingEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string

BetaWebhookSessionRunningEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string

BetaWebhookSessionIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string

BetaWebhookSessionRequiresActionEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string

BetaWebhookSessionArchivedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string

BetaWebhookSessionDeletedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string

BetaWebhookSessionStatusRescheduledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_rescheduled"

workspace\_id: string

BetaWebhookSessionStatusRunStartedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string

BetaWebhookSessionStatusIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string

BetaWebhookSessionStatusTerminatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string

BetaWebhookSessionThreadCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_created"

workspace\_id: string

BetaWebhookSessionThreadIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_idled"

workspace\_id: string

BetaWebhookSessionThreadTerminatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_terminated"

workspace\_id: string

BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string

BetaWebhookVaultCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string

BetaWebhookVaultArchivedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string

BetaWebhookVaultDeletedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string

BetaWebhookVaultCredentialCreatedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialArchivedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialDeletedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

type: "event"

Object type. Always `event` for webhook payloads.

BetaWebhookEventData = [BetaWebhookSessionCreatedEventData](/docs/en/api/beta#beta_webhook_session_created_event_data) { id, organization\_id, type, workspace\_id }  or [BetaWebhookSessionPendingEventData](/docs/en/api/beta#beta_webhook_session_pending_event_data) { id, organization\_id, type, workspace\_id }  or [BetaWebhookSessionRunningEventData](/docs/en/api/beta#beta_webhook_session_running_event_data) { id, organization\_id, type, workspace\_id }  or 19 more

One of the following:

BetaWebhookSessionCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string

BetaWebhookSessionPendingEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string

BetaWebhookSessionRunningEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string

BetaWebhookSessionIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string

BetaWebhookSessionRequiresActionEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string

BetaWebhookSessionArchivedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string

BetaWebhookSessionDeletedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string

BetaWebhookSessionStatusRescheduledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_rescheduled"

workspace\_id: string

BetaWebhookSessionStatusRunStartedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string

BetaWebhookSessionStatusIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string

BetaWebhookSessionStatusTerminatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string

BetaWebhookSessionThreadCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_created"

workspace\_id: string

BetaWebhookSessionThreadIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_idled"

workspace\_id: string

BetaWebhookSessionThreadTerminatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_terminated"

workspace\_id: string

BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string

BetaWebhookVaultCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string

BetaWebhookVaultArchivedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string

BetaWebhookVaultDeletedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string

BetaWebhookVaultCredentialCreatedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialArchivedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialDeletedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookSessionArchivedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string

BetaWebhookSessionCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string

BetaWebhookSessionDeletedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string

BetaWebhookSessionIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string

BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string

BetaWebhookSessionPendingEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string

BetaWebhookSessionRequiresActionEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string

BetaWebhookSessionRunningEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string

BetaWebhookSessionStatusIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string

BetaWebhookSessionStatusRescheduledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_rescheduled"

workspace\_id: string

BetaWebhookSessionStatusRunStartedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string

BetaWebhookSessionStatusTerminatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string

BetaWebhookSessionThreadCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_created"

workspace\_id: string

BetaWebhookSessionThreadIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_idled"

workspace\_id: string

BetaWebhookSessionThreadTerminatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_terminated"

workspace\_id: string

BetaWebhookVaultArchivedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string

BetaWebhookVaultCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string

BetaWebhookVaultCredentialArchivedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialCreatedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialDeletedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultDeletedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string

UnwrapWebhookEvent object { id, created\_at, data, type }

id: string

Unique event identifier for idempotency.

created\_at: string

RFC 3339 timestamp when the event occurred.

data: [BetaWebhookEventData](/docs/en/api/beta#beta_webhook_event_data)

One of the following:

BetaWebhookSessionCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string

BetaWebhookSessionPendingEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string

BetaWebhookSessionRunningEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string

BetaWebhookSessionIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string

BetaWebhookSessionRequiresActionEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string

BetaWebhookSessionArchivedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string

BetaWebhookSessionDeletedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string

BetaWebhookSessionStatusRescheduledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_rescheduled"

workspace\_id: string

BetaWebhookSessionStatusRunStartedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string

BetaWebhookSessionStatusIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string

BetaWebhookSessionStatusTerminatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string

BetaWebhookSessionThreadCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_created"

workspace\_id: string

BetaWebhookSessionThreadIdledEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_idled"

workspace\_id: string

BetaWebhookSessionThreadTerminatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_terminated"

workspace\_id: string

BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string

BetaWebhookVaultCreatedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string

BetaWebhookVaultArchivedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string

BetaWebhookVaultDeletedEventData object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string

BetaWebhookVaultCredentialCreatedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialArchivedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialDeletedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

type: "event"

Object type. Always `event` for webhook payloads.
