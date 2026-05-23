# Client SDKs

**Source:** http://platform.claude.com/docs/en/api/client-sdks

Copy page

Anthropic provides official client SDKs in multiple languages to make it easier to work with the Claude API. Each SDK provides idiomatic interfaces, type safety, and built-in support for features like streaming, retries, and error handling.

For the full API specification, see the [API reference](/docs/en/api/overview).

[CLI

Shell scripting, typed flags, response transforms](/docs/en/api/sdks/cli)[Python

Sync and async clients, Pydantic models](/docs/en/api/sdks/python)[TypeScript

Node.js, Deno, Bun, and browser support](/docs/en/api/sdks/typescript)[Java

Builder pattern, CompletableFuture async](/docs/en/api/sdks/java)[Go

Context-based cancellation, functional options](/docs/en/api/sdks/go)[Ruby

Sorbet types, streaming helpers](/docs/en/api/sdks/ruby)[C#

.NET Standard 2.0+, IChatClient integration](/docs/en/api/sdks/csharp)[PHP

Value objects, builder pattern](/docs/en/api/sdks/php)

# Quick installation

CLI

CLI

Python

Python

TypeScript

TypeScript

C#

C#

Go

Go

Java

Java

PHP

PHP

Ruby

Ruby

```
pip install anthropic
```

# Quick start

CLIPythonTypeScriptC#GoJavaPHPRuby

```
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content)
```

# Platform support

SDKs support the following platforms:

| Platform | Description |
| --- | --- |
| Claude API | Connect directly to Claude API endpoints |
| [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws) | Use Anthropic-operated Claude on AWS infrastructure |
| [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry) | Use Anthropic-operated Claude on Microsoft Azure |
| [Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock) | Use partner-operated Claude through the Bedrock API |
| [Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai) | Use partner-operated Claude through Google Cloud |

Platform support varies by language. See individual SDK pages for platform-specific setup instructions and availability.

# Beta features

Access beta features using the `beta` namespace in any SDK:

CLIPythonTypeScriptC#GoJavaPHPRuby

```
message = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    betas=["feature-name"],
)
```

See [Beta headers](/docs/en/api/beta-headers) for available beta features.

# Requirements

| SDK | Minimum version |
| --- | --- |
| Python | 3.9+ |
| TypeScript | 4.9+ (Node.js 20+) |
| Java | 8+ |
| Go | 1.23+ |
| Ruby | 3.2.0+ |
| C# | .NET Standard 2.0+ |
| PHP | 8.1.0+ |

# GitHub repositories

* [anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python)
* [anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript)
* [anthropic-sdk-java](https://github.com/anthropics/anthropic-sdk-java)
* [anthropic-sdk-go](https://github.com/anthropics/anthropic-sdk-go)
* [anthropic-sdk-ruby](https://github.com/anthropics/anthropic-sdk-ruby)
* [anthropic-sdk-csharp](https://github.com/anthropics/anthropic-sdk-csharp)
* [anthropic-sdk-php](https://github.com/anthropics/anthropic-sdk-php)

Was this page helpful?
