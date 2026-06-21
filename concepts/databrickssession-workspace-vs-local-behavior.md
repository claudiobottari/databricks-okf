---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dc49479bf48d5045066f76226b522ceb09607066523ff899eaeae77298fe15f6
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-workspace-vs-local-behavior
    - DWVLB
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: DatabricksSession Workspace vs Local Behavior
description: Key behavioral differences of DatabricksSession.getOrCreate() and create() when run in a local IDE versus a Databricks notebook or job, including default session handling and connection parameter requirements.
tags:
  - databricks
  - behavioral-differences
  - development-environments
timestamp: "2026-06-19T09:49:12.762Z"
---

# [DatabricksSession](/concepts/databrickssession.md) Workspace vs Local Behavior

**DatabricksSession** is the entry point for interacting with [Databricks Connect](/concepts/databricks-connect.md) from local development environments (IDEs) and also from Databricks notebooks and jobs. Although the same API is used in all contexts, the behavior of `DatabricksSession.builder.getOrCreate()` and `DatabricksSession.builder.create()` differs between local environments and the Databricks workspace. Understanding these differences helps avoid unexpected session reuse or creation failures. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Local Development Environment Behavior

When running code locally via Databricks Connect (for example, in PyCharm or VS Code), the following rules apply:

- `DatabricksSession.builder.getOrCreate()` returns an existing Spark session matching the provided configuration if one exists, or creates a new one if none is found. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- `DatabricksSession.builder.create()` **always** creates a new Spark session, regardless of any existing sessions. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

Connection parameters such as `host`, `token`, and `cluster_id` are resolved from the source code, environment variables, or the `.databrickscfg` configuration profiles file. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

For example, the following code creates two separate sessions:

```python
spark1 = [[databrickssession|DatabricksSession]].builder.create()
spark2 = [[databrickssession|DatabricksSession]].builder.create()
```

^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Databricks Workspace Behavior

When running code inside a notebook or job attached to a Databricks cluster, the `spark` variable is already pre-configured to connect to that compute resource. The behavior changes as follows:

- `DatabricksSession.builder.getOrCreate()` without any additional configuration returns the default Spark session (the one accessible through the `spark` variable). If **additional** connection parameters are set (e.g., `.clusterId(...).getOrCreate()` or `.serverless().getOrCreate()`), a new Spark session is created to the specified target. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- `DatabricksSession.builder.create()` **requires** explicit connection parameters (e.g., `.clusterId(...).create()`); otherwise it raises an `[UNSUPPORTED]` error. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

To connect to a different Databricks compute resource than the one the notebook or job is attached to, use the `remote()` method (or individual setters like `host()` and `token()`). This always creates a new Spark session, replicating the local development behavior. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Serverless Compute Timeout Note

For notebooks running on serverless compute, queries time out after 9,000 seconds by default. This can be customized by setting the Spark configuration property `spark.databricks.execution.timeout`. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Key Differences at a Glance

| Aspect | Local (Databricks Connect) | Workspace (Notebooks/Jobs) |
|--------|----------------------------|----------------------------|
| `getOrCreate()` without extra config | Returns existing session or creates new | Returns the default `spark` session |
| `getOrCreate()` with extra config | Returns existing or creates new (same as without) | Creates a new session to the specified target |
| `create()` without explicit params | Creates a new session | Raises `[UNSUPPORTED]` error |
| `create()` with explicit params | Always creates a new session | Works and creates a new session |
| Connection to a different compute | Uses parameters from code/env/.databrickscfg | Use `remote()` or individual setters |

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that enables local development.
- SparkSession – The underlying PySpark session that `DatabricksSession` wraps.
- Databricks Runtime – The runtime environment where notebooks execute.
- Serverless Compute on Databricks – Compute type with custom timeout configuration.

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
