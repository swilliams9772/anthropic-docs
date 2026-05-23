# Update Credential

**Source:** http://platform.claude.com/docs/en/api/beta/vaults/credentials/update

Copy page

cURL

# Update Credential

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

Update Credential

# Path ParametersExpand Collapse

vault\_id: string

credential\_id: string

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

auth: optional [BetaManagedAgentsMCPOAuthUpdateParams](/docs/en/api/beta#beta_managed_agents_mcp_oauth_update_params) { type, access\_token, expires\_at, refresh }  or [BetaManagedAgentsStaticBearerUpdateParams](/docs/en/api/beta#beta_managed_agents_static_bearer_update_params) { type, token }

Updated authentication details for a credential.

One of the following:

BetaManagedAgentsMCPOAuthUpdateParams object { type, access\_token, expires\_at, refresh }

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: "mcp\_oauth"

access\_token: optional string

Updated OAuth access token.

expires\_at: optional string

A timestamp in RFC 3339 format

refresh: optional [BetaManagedAgentsMCPOAuthRefreshUpdateParams](/docs/en/api/beta#beta_managed_agents_mcp_oauth_refresh_update_params) { refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.

refresh\_token: optional string

Updated OAuth refresh token.

scope: optional string

Updated OAuth scope for the refresh request.

token\_endpoint\_auth: optional [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](/docs/en/api/beta#beta_managed_agents_token_endpoint_auth_basic_update_param) { type, client\_secret }  or [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](/docs/en/api/beta#beta_managed_agents_token_endpoint_auth_post_update_param) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:

BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

client\_secret: optional string

Updated OAuth client secret.

BetaManagedAgentsTokenEndpointAuthPostUpdateParam object { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

client\_secret: optional string

Updated OAuth client secret.

BetaManagedAgentsStaticBearerUpdateParams object { type, token }

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: "static\_bearer"

token: optional string

Updated static bearer token value.

display\_name: optional string

Updated human-readable name for the credential. 1-255 characters.

metadata: optional map[string]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

# ReturnsExpand Collapse

BetaManagedAgentsCredential object { id, archived\_at, auth, 6 more }

A credential stored in a vault. Sensitive fields are never returned in responses.

id: string

Unique identifier for the credential.

archived\_at: string

A timestamp in RFC 3339 format

auth: [BetaManagedAgentsMCPOAuthAuthResponse](/docs/en/api/beta#beta_managed_agents_mcp_oauth_auth_response) { mcp\_server\_url, type, expires\_at, refresh }  or [BetaManagedAgentsStaticBearerAuthResponse](/docs/en/api/beta#beta_managed_agents_static_bearer_auth_response) { mcp\_server\_url, type }

Authentication details for a credential.

One of the following:

BetaManagedAgentsMCPOAuthAuthResponse object { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format

refresh: optional [BetaManagedAgentsMCPOAuthRefreshResponse](/docs/en/api/beta#beta_managed_agents_mcp_oauth_refresh_response) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](/docs/en/api/beta#beta_managed_agents_token_endpoint_auth_none_response) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](/docs/en/api/beta#beta_managed_agents_token_endpoint_auth_basic_response) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](/docs/en/api/beta#beta_managed_agents_token_endpoint_auth_post_response) { type }

Token endpoint requires no client authentication.

One of the following:

BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostResponse object { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

BetaManagedAgentsStaticBearerAuthResponse object { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

Arbitrary key-value metadata attached to the credential.

type: "vault\_credential"

updated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault this credential belongs to.

display\_name: optional string

Human-readable name for the credential.

Update Credential

cURL

```
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_name": "Example credential",
          "metadata": {
            "environment": "production"
          }
        }'
```

Response 200

```
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

# Returns Examples

Response 200

```
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```
