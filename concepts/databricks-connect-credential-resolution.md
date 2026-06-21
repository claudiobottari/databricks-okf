---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04ec9547003a1e65d01bfabc590fd217f3b048732b4f7b26c427019af3f874e0
  pageDirectory: concepts
  sources:
    - pyspark-shell-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-credential-resolution
    - DCCR
  citations:
    - file: pyspark-shell-databricks-on-aws.md
title: Databricks Connect Credential Resolution
description: The mechanism by which the PySpark shell picks up default credentials from environment variables (DATABRICKS_* vars) or a DEFAULT configuration profile when started without additional parameters.
tags:
  - databricks
  - authentication
  - configuration
timestamp: "2026-06-19T20:00:02.283Z"
---

# Databricks Connect Credential Resolution

**Databricks Connect Credential Resolution** refers to the process by which the Databricks Connect client determines which authentication credentials to use when connecting to a remote Databricks cluster. When the PySpark shell or any Databricks Connect client is started without explicit credential parameters, it automatically resolves credentials from the environment.

## Default Credential Resolution

When the PySpark shell is started with no additional parameters, it picks up default credentials from the environment. The resolution order follows a standard hierarchy: environment variables (such as `DATABRICKS_` prefixed variables) are checked first, followed by the `DEFAULT` configuration profile from the Databricks configuration file. ^[pyspark-shell-databricks-on-aws.md]

This automatic resolution applies to all Databricks Connect clients, not just the PySpark shell. The resolved credentials are used to establish a connection to the remote cluster specified in the [Databricks Connect compute configuration](/concepts/databricks-connect-compute-configuration.md). ^[pyspark-shell-databricks-on-aws.md]

## Credential Sources

The credential resolution system checks the following sources in order:

1. **Environment variables**: Variables prefixed with `DATABRICKS_` (e.g., `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLUSTER_ID`) are used if present.
2. **Configuration profiles**: If no environment variables are set, the system falls back to the `DEFAULT` profile in the Databricks configuration file (typically located at `~/.databrickscfg`).

For information about configuring a connection, see [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md). ^[pyspark-shell-databricks-on-aws.md]

## Connection Verification

Once credentials are resolved and the connection is established, the client displays a confirmation message indicating the Spark Connect server URL, including the cluster ID. For example:

```
Client connected to the Spark Connect server at sc://...:.../;token=...;x-databricks-cluster-id=...
```

^[pyspark-shell-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The overall framework for connecting local code to Databricks clusters
- [Databricks Connect compute configuration](/concepts/databricks-connect-compute-configuration.md) — How to configure cluster and connection settings
- [PySpark Shell](/concepts/stopping-the-pyspark-shell.md) — The REPL that uses credential resolution to connect
- Databricks Authentication — Broader authentication mechanisms on the Databricks platform
- [Spark Connect](/concepts/spark-connect.md) — The underlying protocol used by Databricks Connect

## Sources

- pyspark-shell-databricks-on-aws.md

# Citations

1. [pyspark-shell-databricks-on-aws.md](/references/pyspark-shell-databricks-on-aws-b2b40482.md)
