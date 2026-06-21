---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82e0200696b4fd2e26333eba6976cfba11bda8d2aed4391fd81ca00cd0b74555
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-authentication
    - DCA
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Authentication
description: Supported authentication methods for Databricks Connect including OAuth user-to-machine (U2M) and OAuth machine-to-machine (M2M), with specific configuration requirements.
tags:
  - databricks
  - authentication
  - security
timestamp: "2026-06-19T14:47:32.597Z"
---

# Databricks Connect Authentication

**Databricks Connect Authentication** refers to the configuration and authentication methods used to establish a secure connection between a local development environment and a Databricks workspace when using [Databricks Connect](/concepts/databricks-connect.md). The authentication method must be properly configured before any Databricks Connect client code can communicate with the remote compute resources. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Supported Authentication Types

Databricks Connect supports multiple authentication types, each with specific requirements for the local environment and the Databricks workspace. The available authentication methods depend on the [DATABRICKS Authentication Type](/concepts/databricks-authentication-type.md) configured in your local environment. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### OAuth User-to-Machine (U2M) Authentication

[OAuth user-to-machine (U2M) authentication](/concepts/user-to-machine-u2m-authentication.md) requires the Databricks CLI to be installed and configured before running Databricks Connect code. To set up U2M authentication: ^[databricks-connect-usage-requirements-databricks-on-aws.md]

1. Install and configure the Databricks CLI by following the instructions to [Install or update the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install).
2. Use the Databricks CLI to authenticate before running your code. See the [Databricks Connect for Python tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-cluster) for a step-by-step example.

### OAuth Machine-to-Machine (M2M) Authentication

[OAuth machine-to-machine (M2M) authentication](/concepts/machine-to-machine-m2m-authentication.md) is supported for service principal-based authentication scenarios. Both U2M and M2M authentication are supported on Databricks SDK for Python version 0.19.0 and above. To update your project's installed version of the Databricks SDK for Python, see [Get started with the Databricks SDK for Python](https://docs.databricks.com/aws/en/dev-tools/sdk-python#get-started). ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Prerequisites

### Databricks SDK for Python Version

OAuth U2M and OAuth M2M authentication require the Databricks SDK for Python version 0.19.0 or later. If your project uses an older version, upgrade to meet this requirement. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Databricks CLI (for U2M)

For OAuth U2M authentication, the Databricks CLI must be installed and configured on the local development machine. The CLI handles the OAuth token exchange and refresh cycle. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Python Environment

The local Python environment must meet the [Databricks Connect](/concepts/databricks-connect.md) version requirements. Python 3 is required, and the minor Python version must be compatible with the target Databricks Runtime version. See the [version compatibility table](#versions) for details. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Configuration Steps

1. **Install the Databricks SDK for Python** (version 0.19.0 or later for OAuth support).
2. **Configure authentication** using one of the supported methods:
   - For U2M: Run `databricks auth login` via the Databricks CLI.
   - For M2M: Configure OAuth credentials for a service principal.
3. **Set up environment variables** or a Databricks configuration profile (typically at `~/.databrickscfg`) with the required authentication parameters.
4. **Verify the connection** by running a validation test as described in [Validate the connection to Databricks](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config#validate).

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables connecting local code to Databricks compute
- [Databricks authentication types](/concepts/databricks-authentication-type.md) — The complete list of supported authentication methods
- [OAuth user-to-machine (U2M) authentication](/concepts/user-to-machine-u2m-authentication.md) — Authentication using user credentials via OAuth
- [OAuth machine-to-machine (M2M) authentication](/concepts/machine-to-machine-m2m-authentication.md) — Authentication for service principals via OAuth
- Databricks CLI — The command-line tool used for U2M authentication setup
- Databricks SDK for Python — The SDK that provides the authentication implementation

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
