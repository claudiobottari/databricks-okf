---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 275267e79f367a9a136719a42b11a9398e5b901c05198453dbecc0360603a408
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbutilssecrets-via-databricks-connect
    - DVDC
    - DBUtils Secrets Commands
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: dbutils.secrets via Databricks Connect
description: The secrets utility from Databricks Utilities accessible through WorkspaceClient.dbutils.secrets for managing sensitive information.
tags:
  - databricks
  - secrets
  - dbutils
timestamp: "2026-06-19T18:15:39.796Z"
---

# dbutils.secrets via Databricks Connect

**dbutils.secrets via Databricks Connect** refers to the ability to access the Databricks Utilities secrets utility (`dbutils.secrets`) through the Databricks Connect client for Python. This enables you to programmatically retrieve secrets (such as API keys, passwords, and tokens) from your Databricks workspace when running code in a local IDE, notebook server, or custom application that connects to a Databricks cluster via Databricks Connect.

## Overview

When using Databricks Connect for Python (Databricks Runtime 13.3 LTS and above), the `WorkspaceClient` class from the [Databricks SDK for Python](https://pypi.org/project/databricks-sdk) provides a `dbutils` variable. Through this variable, you can access two Databricks Utilities:

- `dbutils.fs` – file system operations
- `dbutils.secrets` – secret management operations

No other Databricks Utilities are available via `dbutils` in Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Initializing `WorkspaceClient`

To use `dbutils.secrets`, you first must create a `WorkspaceClient` and authenticate it with your Databricks workspace. Common authentication methods include:

- Hard-coding the workspace URL and an access token (not recommended; exposes sensitive information)
- Using a [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles) that contains `host` and `token` fields
- Setting environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (the same variables used for Databricks Connect)

The SDK does not recognize the `SPARK_REMOTE` environment variable for authentication. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

Example using environment variables:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
```

After initialization, `w.dbutils.secrets` provides access to the secrets utility. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Using `dbutils.secrets`

Once the `WorkspaceClient` is initialized, you can call the methods of `dbutils.secrets` (e.g., `get`, `list`, `listScopes`) to retrieve secrets from your workspace’s secret scopes. The exact methods available correspond to those documented in the Databricks Utilities [secrets utility](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#secrets-utility-dbutilssecrets). The Databricks SDK for Python’s `dbutils` wrapper translates these calls into the appropriate REST API requests. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

Because `dbutils.secrets` runs remotely on the Databricks workspace, your Databricks Connect client must have network access to the workspace and the authenticated user or service principal must have the necessary permissions on the target secret scopes.

## Limitations

- Only `dbutils.fs` and `dbutils.secrets` are available via `dbutils` in Databricks Connect. Other utilities such as `dbutils.notebook`, `dbutils.widgets`, or `dbutils.jobs` are not accessible through this interface. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]
- For more advanced Databricks REST API operations, use the Databricks SDK for Python directly (also included in Databricks Connect). ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The framework that enables connecting external tools to Databricks clusters.
- Databricks Utilities – The collection of utility commands, including `dbutils.secrets`.
- Secrets utility – The specific Databricks utility for managing and retrieving secrets.
- [WorkspaceClient](/concepts/workspaceclient-dbutils.md) – The main entry point for the Databricks SDK for Python, providing access to workspace-level APIs.
- databricks-sdk – The underlying Python SDK used by Databricks Connect.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
