---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b2b2c1e1d2a1885a2711e01d1ecce3737122f9fa03dc27e6e537b803b013e6cb
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark_remote-environment-variable-incompatibility
    - SEVI
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: SPARK_REMOTE Environment Variable Incompatibility
description: The Databricks SDK for Python does not recognize the SPARK_REMOTE environment variable used by Databricks Connect; authentication must use DATABRICKS_HOST and DATABRICKS_TOKEN instead.
tags:
  - databricks
  - environment-variables
  - compatibility
timestamp: "2026-06-18T15:10:21.761Z"
---

---

title: SPARK_REMOTE Environment Variable Incompatibility
summary: The Databricks SDK for Python does not recognize the `SPARK_REMOTE` environment variable for authentication with Databricks Connect; alternative configuration methods are required.
kind: concept
createdAt: "2026-06-18T08:06:14.810Z"
updatedAt: "2026-06-18T08:06:14.810Z"
tags:
  - databricks-connect
  - python-sdk
  - authentication
  - environment-variables
aliases:
  - spark-remote-env-var-incompatibility
  - SREVI
confidence: 1
provenanceState: extracted
inferredParagraphs: 0

---

# SPARK_REMOTE Environment Variable Incompatibility

**SPARK_REMOTE Environment Variable Incompatibility** describes a limitation of the Databricks SDK for Python: when used with [Databricks Connect](/concepts/databricks-connect.md), the SDK does **not** read or honor the `SPARK_REMOTE` environment variable for authentication. This can cause confusion for users who expect the SDK to pick up cluster connection details from that variable, as other Databricks Connect components do. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Background

`SPARK_REMOTE` is an environment variable commonly used by [Databricks Connect](/concepts/databricks-connect.md) to specify the remote Spark cluster endpoint and authentication token (e.g., `spark://...`). While Databricks Connect (and the underlying Spark Connect protocol) can leverage this variable, the **Databricks SDK for Python** — which provides the `dbutils` wrapper and other workspace-level APIs — does not parse it. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Effect

When initializing `WorkspaceClient` (the main entry point for calling Databricks Utilities and other REST APIs through the SDK), the SDK will fail to authenticate if only `SPARK_REMOTE` is set. This is explicitly documented:

> The Databricks SDK for Python does not recognize the `SPARK_REMOTE` environment variable for Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

As a result, users cannot rely on `SPARK_REMOTE` to configure the SDK; they must use one of the supported authentication mechanisms.

## Supported Alternatives

The Databricks SDK for Python supports the following methods for authentication with Databricks Connect. These are the recommended alternatives to setting `SPARK_REMOTE`:

| Method | Description |
|--------|-------------|
| **`DATABRICKS_HOST` and `DATABRICKS_TOKEN`** | Set these two environment variables, then call `WorkspaceClient()` with no arguments. Works the same way as the standard Databricks Connect setup. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md] |
| **Configuration profile** | Create a [profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles) with `host` and `token` fields, then pass the profile name: `WorkspaceClient(profile="<profile-name>")`. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md] |
| **Explicit credentials in code** | Hard-code the workspace URL and token (not recommended because sensitive values may be exposed). ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md] |

These alternatives ensure that `WorkspaceClient` can successfully authenticate and provide access to Databricks Utilities (`dbutils.fs`, `dbutils.secrets`) and the full Databricks REST API. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example

The following snippet demonstrates the recommended approach using environment variables (after `DATABRICKS_HOST` and `DATABRICKS_TOKEN` are set): ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
# Now w.dbutils.fs, w.dbutils.secrets, etc. are available.
```

If only `SPARK_REMOTE` is set, this code would raise an authentication error.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The connectivity layer that uses `SPARK_REMOTE` for Spark Connect, but not for the SDK.
- Databricks SDK for Python – The library that provides `WorkspaceClient` and other workspace/account APIs.
- Databricks Utilities – The `dbutils` functionality accessible through the SDK.
- Authentication for Databricks SDK – Official documentation on supported credential providers.
- [Configuration profiles](/concepts/databricks-configuration-profiles.md) – A secure way to store host and token information.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
