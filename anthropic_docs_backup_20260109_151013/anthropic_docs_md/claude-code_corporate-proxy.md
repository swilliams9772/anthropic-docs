# Corporate proxy configuration - Anthropic

**Source:** https://docs.anthropic.com/en/docs/claude-code/corporate-proxy

Claude Code supports standard HTTP/HTTPS proxy configurations through environment variables. This allows you to route all Claude Code traffic through your organization’s proxy servers for security, compliance, and monitoring purposes.

# [​](#basic-proxy-configuration) Basic proxy configuration

# [​](#environment-variables) Environment variables

Claude Code respects standard proxy environment variables:

```
# HTTPS proxy (recommended)

export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)

export HTTP_PROXY=http://proxy.example.com:8080

```

Claude Code currently does not support the `NO_PROXY` environment variable. All traffic will be routed through the configured proxy.

Claude Code does not support SOCKS proxies.

# [​](#authentication) Authentication

# [​](#basic-authentication) Basic authentication

If your proxy requires basic authentication, include credentials in the proxy URL:

```
export HTTPS_PROXY=http://username:password@proxy.example.com:8080

```

Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.

For proxies requiring advanced authentication (NTLM, Kerberos, etc.), consider using an LLM Gateway service that supports your authentication method.

# [​](#ssl-certificate-issues) SSL certificate issues

If your proxy uses custom SSL certificates, you may encounter certificate errors.

Ensure that you set the correct certificate bundle path:

```
export SSL_CERT_FILE=/path/to/certificate-bundle.crt
export NODE_EXTRA_CA_CERTS=/path/to/certificate-bundle.crt

```

# [​](#network-access-requirements) Network access requirements

Claude Code requires access to the following URLs:

* `api.anthropic.com` - Claude API endpoints
* `statsig.anthropic.com` - Telemetry and metrics
* `sentry.io` - Error reporting

Ensure these URLs are allowlisted in your proxy configuration and firewall rules. This is especially important when using Claude Code in containerized or restricted network environments.

# [​](#additional-resources) Additional resources

* [Claude Code settings](/en/docs/claude-code/settings)
* [Environment variables reference](/en/docs/claude-code/settings#environment-variables)
* [Troubleshooting guide](/en/docs/claude-code/troubleshooting)
