# Create Tunnel Certificate

**Source:** http://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create

Copy page

# Create Tunnel Certificate

POST/v1/organizations/tunnels/{tunnel\_id}/certificates

Register a public CA certificate for the tunnel.

Anthropic verifies the gateway's server certificate against this CA
when it terminates the inner TLS session. The PEM body must contain
exactly one X.509 certificate and no private-key material. A tunnel
holds at most two non-archived certificates.

# Path ParametersExpand Collapse

tunnel\_id: string

ID of the Tunnel.

# Header ParametersExpand Collapse

"anthropic-beta": array of "mcp-tunnels-2026-05-19"

Required for all Tunnel endpoints.

# Body ParametersJSONExpand Collapse

ca\_certificate\_pem: string

PEM-encoded X.509 CA certificate. Must contain exactly one certificate and
no private-key material.

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

Create Tunnel Certificate

```
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN" \
    -d '{
          "ca_certificate_pem": "-----BEGIN CERTIFICATE-----\\nMIIBexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexa\\n...illustrative placeholder, not a real certificate...\\n-----END CERTIFICATE-----\\n"
        }'
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
