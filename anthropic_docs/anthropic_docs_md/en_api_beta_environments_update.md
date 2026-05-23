# Update Environment

**Source:** http://platform.claude.com/docs/en/api/beta/environments/update

Copy page

cURL

# Update Environment

POST/v1/environments/{environment\_id}

Update an existing environment's configuration.

# Path ParametersExpand Collapse

environment\_id: string

# Header ParametersExpand Collapse

"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)

Optional header to specify the beta version(s) you want to use.

One of the following:

string

"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 22 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

# Body ParametersJSONExpand Collapse

config: optional [BetaCloudConfigParams](/docs/en/api/beta#beta_cloud_config_params) { type, networking, packages }  or [BetaSelfHostedConfigParams](/docs/en/api/beta#beta_self_hosted_config_params) { type }

Updated environment configuration

One of the following:

BetaCloudConfigParams object { type, networking, packages }

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "cloud"

Environment type

networking: optional [BetaUnrestrictedNetwork](/docs/en/api/beta#beta_unrestricted_network) { type }  or [BetaLimitedNetworkParams](/docs/en/api/beta#beta_limited_network_params) { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Network configuration policy. Omit on update to preserve the existing value.

One of the following:

BetaUnrestrictedNetwork object { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

BetaLimitedNetworkParams object { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "limited"

Network policy type

allow\_mcp\_servers: optional boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: optional boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: optional array of string

Specifies domains the container can reach.

packages: optional [BetaPackagesParams](/docs/en/api/beta#beta_packages_params) { apt, cargo, gem, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: optional array of string

Ubuntu/Debian packages to install

cargo: optional array of string

Rust packages to install

gem: optional array of string

Ruby packages to install

go: optional array of string

Go packages to install

npm: optional array of string

Node.js packages to install

pip: optional array of string

Python packages to install

type: optional "packages"

Package configuration type

BetaSelfHostedConfigParams object { type }

Request params for `self_hosted` environment configuration.

type: "self\_hosted"

Environment type

description: optional string

Updated description of the environment

metadata: optional map[string]

User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

name: optional string

Updated name for the environment

scope: optional "organization" or "account"

The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

One of the following:

"organization"

"account"

# ReturnsExpand Collapse

BetaEnvironment object { id, archived\_at, config, 7 more }

Unified Environment resource for both cloud and self-hosted environments.

id: string

Environment identifier (e.g., 'env\_...')

archived\_at: string

RFC 3339 timestamp when environment was archived, or null if not archived

config: [BetaCloudConfig](/docs/en/api/beta#beta_cloud_config) { networking, packages, type }  or [BetaSelfHostedConfig](/docs/en/api/beta#beta_self_hosted_config) { type }

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:

BetaCloudConfig object { networking, packages, type }

`cloud` environment configuration.

networking: [BetaUnrestrictedNetwork](/docs/en/api/beta#beta_unrestricted_network) { type }  or [BetaLimitedNetwork](/docs/en/api/beta#beta_limited_network) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Network configuration policy.

One of the following:

BetaUnrestrictedNetwork object { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

BetaLimitedNetwork object { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: array of string

Specifies domains the container can reach.

type: "limited"

Network policy type

packages: [BetaPackages](/docs/en/api/beta#beta_packages) { apt, cargo, gem, 4 more }

Package manager configuration.

apt: array of string

Ubuntu/Debian packages to install

cargo: array of string

Rust packages to install

gem: array of string

Ruby packages to install

go: array of string

Go packages to install

npm: array of string

Node.js packages to install

pip: array of string

Python packages to install

type: optional "packages"

Package configuration type

type: "cloud"

Environment type

BetaSelfHostedConfig object { type }

Configuration for self-hosted environments.

type: "self\_hosted"

Environment type

created\_at: string

RFC 3339 timestamp when environment was created

description: string

User-provided description for the environment

metadata: map[string]

User-provided metadata key-value pairs

name: string

Human-readable name for the environment

type: "environment"

The type of object (always 'environment')

updated\_at: string

RFC 3339 timestamp when environment was last updated

scope: optional "organization" or "account"

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

"organization"

"account"

Update Environment

cURL

```
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "description": "Python environment with data-analysis packages."
        }'
```

Response 200

```
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

# Returns Examples

Response 200

```
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```
