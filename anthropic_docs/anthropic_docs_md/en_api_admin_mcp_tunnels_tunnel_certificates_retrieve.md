# Get Tunnel Certificate

**Source:** http://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/retrieve

Copy page

# Get Tunnel Certificate

GET/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}

Retrieve a single certificate registered on a tunnel by ID.

# Path ParametersExpand Collapse

tunnel\_id: string

ID of the Tunnel.

certificate\_id: string

ID of the Tunnel Certificate.

# Header ParametersExpand Collapse

"anthropic-beta": array of "mcp-tunnels-2026-05-19"

Required for all Tunnel endpoints.

# ReturnsExpand Collapse

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

Get Tunnel Certificate

```
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates/$CERTIFICATE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
```

Response 200

```
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
}
```

# Returns Examples

Response 200

```
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
}
```
