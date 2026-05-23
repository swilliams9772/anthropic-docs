# MCP Tunnels

**Source:** http://platform.claude.com/docs/en/api/admin/mcp_tunnels

Copy page

# MCP Tunnels

# [Get Tunnel](/docs/en/api/admin/mcp_tunnels/retrieve)

GET/v1/organizations/tunnels/{tunnel\_id}

# [List Tunnels](/docs/en/api/admin/mcp_tunnels/list)

GET/v1/organizations/tunnels

# [Reveal Tunnel Token](/docs/en/api/admin/mcp_tunnels/reveal_token)

POST/v1/organizations/tunnels/{tunnel\_id}/reveal\_token

# [Rotate Tunnel Token](/docs/en/api/admin/mcp_tunnels/rotate_token)

POST/v1/organizations/tunnels/{tunnel\_id}/rotate\_token

# [Archive Tunnel](/docs/en/api/admin/mcp_tunnels/archive)

POST/v1/organizations/tunnels/{tunnel\_id}/archive

# ModelsExpand Collapse

MCPTunnelRetrieveResponse object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel.

archived\_at: string

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

display\_name: string

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.

type: "tunnel"

Object type. Always `tunnel` for Tunnels.

workspace\_id: string

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.

MCPTunnelListResponse object { data, next\_page }

data: array of object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel.

archived\_at: string

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

display\_name: string

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.

type: "tunnel"

Object type. Always `tunnel` for Tunnels.

workspace\_id: string

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.

next\_page: string

Opaque cursor for the next page, or `null` if there are no more results.

MCPTunnelRevealTokenResponse object { id, tunnel\_token, type }

id: string

Stable identifier for the current token value. Changes when the token is
rotated.

tunnel\_token: string

The tunnel's connection token.

type: "tunnel\_token"

Object type. Always `tunnel_token` for Tunnel Tokens.

MCPTunnelRotateTokenResponse object { id, tunnel\_token, type }

id: string

Stable identifier for the current token value. Changes when the token is
rotated.

tunnel\_token: string

The tunnel's connection token.

type: "tunnel\_token"

Object type. Always `tunnel_token` for Tunnel Tokens.

MCPTunnelArchiveResponse object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel.

archived\_at: string

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

display\_name: string

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.

type: "tunnel"

Object type. Always `tunnel` for Tunnels.

workspace\_id: string

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.

# MCP TunnelsTunnel Certificates

# [Create Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create)

POST/v1/organizations/tunnels/{tunnel\_id}/certificates

# [Get Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/retrieve)

GET/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}

# [List Tunnel Certificates](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list)

GET/v1/organizations/tunnels/{tunnel\_id}/certificates

# [Archive Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive)

POST/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

# ModelsExpand Collapse

TunnelCertificateCreateResponse object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

TunnelCertificateRetrieveResponse object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

TunnelCertificateListResponse object { data, next\_page }

data: array of object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

next\_page: string

Opaque cursor for the next page, or `null` if there are no more results.

TunnelCertificateArchiveResponse object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.
