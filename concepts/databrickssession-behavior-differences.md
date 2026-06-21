---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37f2b236e2524d6f5a81e4f38573e78bbcb9b25a4eed1a941795ced0905f78c7
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-behavior-differences
    - DBD
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: DatabricksSession behavior differences
description: The behavior of DatabricksSession.builder.getOrCreate() and create() differs between local development environments and Databricks workspace notebooks/jobs, particularly regarding default session handling and error behavior.
tags:
  - databricks
  - api
  - session-management
timestamp: "2026-06-18T15:04:52.373Z"
---

# [DatabricksSession](/concepts/databrickssession.md) Behavior Differences

**DatabricksSession Behavior Differences** describes how the `DatabricksSession` API behaves differently when used in a local development environment (via [Databricks Connect](/concepts/databricks-connect.md)) versus when used inside a Databricks notebook or job. Understanding these differences is important for writing code that can transition smoothly between local development and Databricks deployment.^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Local Development Environment Behavior

When running code locally in an IDE outside of Databricks using Databricks Connect:

- `DatabricksSession.builder.getOrCreate()` returns the existing Spark session for the provided configuration if one exists, otherwise it creates a new one.^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- `DatabricksSession.builder.create()` always creates a new Spark session, even if one already exists.^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- Connection parameters such as `host`, `token`, and `cluster_id` are populated from source code, environment variables, or the `.databrickscfg` configuration profiles file.^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

For example, the following code creates two separate sessions when run locally:^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

```python
spark1 = [[databrickssession|DatabricksSession]].builder.create()
spark2 = [[databrickssession|DatabricksSession]].builder.create()
```

## Databricks Workspace Behavior

When running code in a Databricks notebook or job (i.e., inside the Databricks workspace):

- `DatabricksSession.builder.getOrCreate()` used without any additional configuration returns the default Spark session, which is also accessible via the built-in `spark` variable. This default session is pre-configured to connect to the compute instance the notebook or job is attached to.^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- If additional connection parameters are set — for example, `DatabricksSession.builder.clusterId(...).getOrCreate()` or `DatabricksSession.builder.serverless().getOrCreate()` — a new Spark session is created, distinct from the default one.^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- `DatabricksSession.builder.create()` requires explicit connection parameters in a notebook, such as `DatabricksSession.builder.clusterId(...).create()`. Without explicit parameters, it returns an `[UNSUPPORTED]` error.^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Using `remote()` to Connect to Other Compute

It is possible to use Databricks Connect from within a notebook or job to connect to Databricks compute that is not the one the notebook or job is attached to, using the `remote()` method. `remote()` takes configuration key-word arguments or individual configuration methods like `host()` or `token()`. In these cases, a new session is created for the referenced compute, similar to the behavior when used outside a Databricks notebook or job.^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Additional Notes

For notebooks running on serverless compute, queries time out after 9000 seconds by default. This timeout can be customized by setting the Spark configuration property `spark.databricks.execution.timeout`. Refer to the documentation on Spark configuration properties.^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that connects local environments to Databricks compute.
- [DatabricksSession](/concepts/databrickssession.md) — The API entry point for Databricks-specific Spark sessions.
- [Spark Session](/concepts/databrickssession.md) — The unified entry point for Spark functionality.
- [Portability of Databricks Connect Code](/concepts/portability-of-databricks-connect-apis.md) — How code written with Databricks Connect can run unchanged in notebooks.

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
