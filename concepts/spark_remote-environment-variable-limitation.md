---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 621514f55625d5f310c9bab7ec2c8092a8b0e214f392a6fe15206a92db7611cf
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark_remote-environment-variable-limitation
    - SEVL
    - spark_remote-environment-variable-incompatibility
    - SEVI
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: SPARK_REMOTE Environment Variable Limitation
description: The Databricks SDK for Python does not recognize the SPARK_REMOTE environment variable for authentication, unlike the Databricks Connect client itself
tags:
  - databricks
  - environment-variables
  - limitations
timestamp: "2026-06-18T11:42:36.949Z"
---

# SPARK_REMOTE Environment Variable Limitation

The **SPARK_REMOTE Environment Variable Limitation** refers to the fact that the Databricks SDK for Python — including the `WorkspaceClient` used with [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — does **not** read the `SPARK_REMOTE` environment variable for authentication or connection configuration. Users who rely on `SPARK_REMOTE` to configure Databricks Connect must instead provide credentials through other supported means. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Background

In many Databricks Connect setups, the `SPARK_REMOTE` environment variable is used outside of Python to specify the remote cluster endpoint and authentication token. For example, in the standard Databricks Connect configuration for PySpark, setting `SPARK_REMOTE` with a connection string (e.g., `spark://<workspace-id>@<workspace-url>?token=<token>`) is sufficient. However, the **Databricks SDK for Python**, which provides the `WorkspaceClient` class, does not process `SPARK_REMOTE`. This means that when you use `WorkspaceClient` to access Databricks Utilities (such as `dbutils.fs` or `dbutils.secrets`), you must supply the host and authentication credentials in a different way. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Correct Configuration for the Databricks SDK for Python

The `WorkspaceClient` class recognizes only the following sources for authentication:

- **Explicit parameters** passed to the constructor (`host` and `token`).
- **Configuration profiles** created with the Databricks authentication configuration file.
- **Environment variables** `DATABRICKS_HOST` and `DATABRICKS_TOKEN`.

These options are used instead of `SPARK_REMOTE`. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

The following examples show how to initialise `WorkspaceClient` properly:

```python
# Option 1: Explicit host and token (not recommended due to security concerns)
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(host="https://<workspace-url>", token="<token>")

# Option 2: Using a configuration profile
w = WorkspaceClient(profile="<profile-name>")

# Option 3: Using environment variables (DATABRICKS_HOST and DATABRICKS_TOKEN)
w = WorkspaceClient()
```

^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Impact on Databricks Utilities Usage

This limitation affects only the parts of Databricks Connect that rely on the Databricks SDK for Python, namely the `dbutils.fs` and `dbutils.secrets` utilities exposed via `WorkspaceClient.dbutils`. Plain PySpark operations that use `SparkSession` still respect `SPARK_REMOTE` as usual. For example, reading a DataFrame with `spark.read` does not involve the SDK and therefore works regardless of this limitation. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Recommended Approach

To avoid confusion, use the same authentication environment variables (`DATABRICKS_HOST` and `DATABRICKS_TOKEN`) for both PySpark (via `SPARK_REMOTE`) and the SDK (via the `WorkspaceClient`). This ensures that both the Spark session and the Databricks Utilities work correctly without duplicating credentials. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The overall client that uses both `SparkSession` and `WorkspaceClient`.
- [WorkspaceClient](/concepts/workspaceclient-dbutils.md) — The Databricks SDK class that does not recognise `SPARK_REMOTE`.
- Databricks SDK for Python — The library providing `WorkspaceClient`.
- Authentication Configuration Profiles — An alternative to environment variables for SDK authentication.
- Databricks Utilities — The `dbutils` functions accessed through `WorkspaceClient`.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
