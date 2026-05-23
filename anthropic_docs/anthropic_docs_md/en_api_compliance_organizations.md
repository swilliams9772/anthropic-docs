# Organizations

**Source:** http://platform.claude.com/docs/en/api/compliance/organizations

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Organizations

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

# OrganizationsUsers

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

# OrganizationsRoles

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

# OrganizationsRolesPermissions

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
