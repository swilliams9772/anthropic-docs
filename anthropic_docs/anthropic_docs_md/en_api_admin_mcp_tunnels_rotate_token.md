# Rotate Tunnel Token

**Source:** http://platform.claude.com/docs/en/api/admin/mcp_tunnels/rotate_token

Copy page

# Rotate Tunnel Token

POST/v1/organizations/tunnels/{tunnel\_id}/rotate\_token

Invalidate the tunnel's current token for new connections and return a fresh value.

Established connections are not severed by rotation; a connector
restarted after rotation must use the new value. An optional
`reason` is captured for operational context.

# Path ParametersExpand Collapse

tunnel\_id: string

ID of the Tunnel.

# Header ParametersExpand Collapse

"anthropic-beta": array of "mcp-tunnels-2026-05-19"

Required for all Tunnel endpoints.

# Body ParametersJSONExpand Collapse

reason: optional string

Optional free-text reason for the rotation, recorded for audit.

# ReturnsExpand Collapse

id: string

Stable identifier for the current token value. Changes when the token is
rotated.

tunnel\_token: string

The tunnel's connection token.

type: "tunnel\_token"

Object type. Always `tunnel_token` for Tunnel Tokens.

Rotate Tunnel Token

```
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/rotate_token \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
```

Response 200

```
{
  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"
}
```

# Returns Examples

Response 200

```
{
  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"
}
```
