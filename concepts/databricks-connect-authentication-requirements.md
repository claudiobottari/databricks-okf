---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e59a82fcb1b07beeab8c33ed58cb5f46d7c42350b49d0ada1ddc3f38a7816bf0
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-authentication-requirements
    - DCAR
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Authentication Requirements
description: Databricks Connect supports OAuth U2M and M2M authentication; U2M requires prior authentication via Databricks CLI, and both are supported on Databricks SDK for Python 0.19.0+.
tags:
  - databricks
  - authentication
  - oauth
timestamp: "2026-06-19T09:49:22.116Z"
---

# Databricks Connect Authentication Requirements

**Databricks Connect Authentication Requirements** define the specific authentication methods and configurations needed to connect your local development environment to a Databricks workspace using [Databricks Connect](/concepts/databricks-connect.md). These requirements vary based on the authentication method you choose and the version of the Databricks SDK for Python installed in your project.

## Authentication Types

Databricks Connect supports multiple authentication types. The available options depend on your Databricks SDK for Python version and your chosen authentication workflow.

### OAuth User-to-Machine (U2M) Authentication

For [OAuth U2M authentication](/concepts/user-to-machine-u2m-authentication.md), you must use the Databricks CLI to authenticate before running your code. This requires installing and configuring the Databricks CLI. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### OAuth Machine-to-Machine (M2M) Authentication

[OAuth M2M authentication](/concepts/machine-to-machine-m2m-authentication.md) is supported for automated workflows and service principals. This method does not require user interaction for authentication. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### SDK Version Requirements

Both OAuth U2M and OAuth M2M authentication are supported on Databricks SDK for Python version 0.19.0 and above. To use these authentication methods, ensure your project's installed Databricks SDK for Python meets this minimum version requirement. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Local Environment Authentication Prerequisites

Your local development environment must have authentication configured before you can use Databricks Connect. The specific prerequisites depend on your chosen authentication type:

- **OAuth U2M**: Requires the Databricks CLI to be installed and configured for authentication before running code.
- **OAuth M2M**: Suitable for automated workflows without user interaction requirements.
- Other authentication types: See the full list of [Databricks authentication types](/concepts/databricks-authentication-type.md).

^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Authentication Configuration Steps

### For OAuth U2M

1. Install the Databricks CLI: `pip install databricks-cli`
2. Configure authentication using the CLI: `databricks configure --token` (or the appropriate authentication method)
3. Run your Databricks Connect code after authentication is configured

### For OAuth M2M

1. Set up a service principal with appropriate permissions
2. Configure authentication credentials (typically via environment variables or configuration files)
3. Ensure the Databricks SDK for Python is updated to at least version 0.19.0

## Related Concepts

- Databricks SDK for Python – Required for OAuth authentication support
- Databricks CLI – Required for U2M authentication setup
- [OAuth authentication](/concepts/user-to-machine-u2m-authentication.md) – The underlying protocol for Databricks Connect authentication
- Service principal authentication – Used for automated M2M workflows

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
