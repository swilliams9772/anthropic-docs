# List Environments

**Source:** http://platform.claude.com/docs/en/api/beta/environments/list

Copy page

cURL

# List Environments

GET/v1/environments

List environments with pagination support.

# Query ParametersExpand Collapse

include\_archived: optional boolean

Include archived environments in the response

limit: optional number

Maximum number of environments to return

page: optional string

Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

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

# ReturnsExpand Collapse

data: array of [BetaEnvironment](/docs/en/api/beta#beta_environment) { id, archived\_at, config, 7 more }

List of environments.

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

next\_page: string

Token for fetching the next page of results. If `null`, there are no more results available. Pass this value to the `page` parameter in the next request.

List Environments

cURL

```
curl https://api.anthropic.com/v1/environments \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200

```
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

# Returns Examples

Response 200

```
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
