---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1366f04d7924e68b042017c911d30ccdb84108e9d771f1cceceaf6a71c5ebcee
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sdk-authentication-methods
    - DSAM
    - Databricks SDK Authentication
    - Databricks SDK authentication
    - Databricks-supported authentication methods
    - Databricks Utilities authentication
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks SDK Authentication Methods
description: "Multiple ways to authenticate the WorkspaceClient: hard-coded credentials, configuration profiles, or environment variables (DATABRICKS_HOST and DATABRICKS_TOKEN)."
tags:
  - databricks
  - authentication
  - security
timestamp: "2026-06-19T18:15:47.621Z"
---

## Databricks SDK Authentication Methods

**Databricks SDK Authentication Methods** refers to the various techniques the Databricks SDK for Python uses to authenticate with a Databricks workspace when interacting with Databricks REST APIs and Databricks Utilities. The SDK provides multiple authentication pathways, ranging from explicit hard-coded credentials to environment-variable-driven and profile-based configurations.

## Overview

The `WorkspaceClient` class, the primary entry point of the Databricks SDK for Python, requires sufficient authentication information to connect to a target workspace. The SDK does not recognize the `SPARK_REMOTE` environment variable used by [Databricks Connect](/concepts/databricks-connect.md); external authentication configuration must be provided through one of the SDK's own supported methods. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Supported Authentication Methods

### Explicit Host and Token

You can hard-code the workspace host URL and personal access token directly in your code. This method is functional but **not recommended** by Databricks, as it exposes sensitive credentials if the code is stored in version control or shared. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host="https://<workspace-instance-name>",
    token="<your-access-token>"
)
```

### Configuration Profile

You can create or reference a [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) — a configuration file that stores `host` and `token` fields — and pass the profile name to the SDK. This approach separates credentials from code. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile="<profile-name>")
```

### Environment Variables

You can set the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables to configure the SDK without code-level credentials. This method is commonly used with Databricks Connect and other automated workflows. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

# The SDK reads DATABRICKS_HOST and DATABRICKS_TOKEN from the environment
w = WorkspaceClient()
```

### Default (No-Argument) Initialization

If no explicit arguments are provided, the SDK attempts to authenticate using the environment's default configuration, typically falling back to the credentials found in configuration profiles or environment variables. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
```

## Account-Level Authentication

The Databricks SDK for Python also provides an `AccountClient` class for accessing Databricks account-level REST APIs. The same authentication methods — host/token, profile, or environment variables — apply, but the client must be initialized with account-level credentials rather than workspace-level credentials. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Best Practices

- **Prefer configuration profiles or environment variables** over hard-coded credentials to avoid leaking secrets in source control.
- **Use environment variables in CI/CD pipelines** and automated scripts to simplify authentication setup.
- **Validate your authentication method** by checking that the `WorkspaceClient` can successfully call a simple API endpoint (e.g., listing clusters) before building more complex workflows.

## Related Concepts

- Databricks SDK for Python — The software development kit that wraps Databricks REST APIs
- Databricks Utilities — Helper functions (`dbutils`) that require authenticated SDK access
- [Databricks Configuration Profile](/concepts/databricks-configuration-profiles.md) — A file-based credential store for `host` and `token`
- [Databricks Connect](/concepts/databricks-connect.md) — A related tool that uses the `SPARK_REMOTE` environment variable (not recognized by the SDK)
- [WorkspaceClient](/concepts/workspaceclient-and-dbutils.md) — The primary class for workspace-level API access
- AccountClient — The class for account-level API access

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
