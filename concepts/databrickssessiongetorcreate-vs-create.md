---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6920061d9e51777ac162a3751f6ec55d1bc480b6df68d695a1af00f09a466bd6
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssessiongetorcreate-vs-create
    - DVC
    - DatabricksSession getOrCreate()
    - DatabricksSession create()
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: DatabricksSession.getOrCreate() vs create()
description: Behavioral differences between getOrCreate() and create() methods when running locally vs in Databricks workspace
tags:
  - api
  - session-management
  - databricks
timestamp: "2026-06-19T18:10:34.938Z"
---

# [DatabricksSession](/concepts/databrickssession.md).getOrCreate() vs create()

The `DatabricksSession.builder.getOrCreate()` and `DatabricksSession.builder.create()` methods are both used to obtain a Spark session within the Databricks ecosystem, but they differ fundamentally in whether they reuse an existing session or create a new one. Their behavior also varies depending on whether the code is running locally via [Databricks Connect](/concepts/databricks-connect.md) or within a Databricks workspace (notebook or job). ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Behavior in Local Development (Databricks Connect)

When running code locally within an IDE outside of Databricks using Databricks Connect:
- `DatabricksSession.builder.getOrCreate()` gets the existing Spark session for the provided configuration if one exists, or creates a new Spark session if it does not exist. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- `DatabricksSession.builder.create()` **always** creates a new Spark session, regardless of whether an existing session already exists. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

Connection parameters such as `host`, `token`, and `cluster_id` are populated either from the source code, environment variables, or the `.databrickscfg` configuration profiles file for both methods. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

For example, when run using Databricks Connect, the following code creates two separate sessions:
```python
spark1 = [[databrickssession|DatabricksSession]].builder.create()
spark2 = [[databrickssession|DatabricksSession]].builder.create()
```

## Behavior in Databricks Workspace (Notebooks and Jobs)

When running code in a notebook or job within the Databricks workspace:
- `DatabricksSession.builder.getOrCreate()` returns the default Spark session (also accessible through the `spark` variable) when used **without any additional configuration**. The `spark` variable is pre-configured to connect to the compute instance to which the notebook or job is attached. However, if additional connection parameters are set — for example, by using `DatabricksSession.builder.clusterId(...).getOrCreate()` or `DatabricksSession.builder.serverless().getOrCreate()` — a new Spark session is created. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- `DatabricksSession.builder.create()` requires explicit connection parameters in a notebook, such as `DatabricksSession.builder.clusterId(...).create()`. Without explicit parameters, it returns an `[UNSUPPORTED]` error. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Using `remote()` for External Connections

Both methods can be used with `remote()` to connect to Databricks compute that is not attached to the notebook or job. `remote()` takes configuration keyword arguments or individual configuration methods such as `host()` or `token()`. In these cases, a new session is created for the referenced compute, similar to behavior outside of a Databricks notebook or job. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Practical Guidance

- Use `getOrCreate()` when you want to reuse an existing session, particularly for portability from local development to notebooks. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- Use `create()` when you explicitly need a new, separate session, understanding that it requires connection parameters in workspace environments. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- The [DatabricksSession API](/concepts/databrickssession.md) is available in both local development and workspace environments, enabling seamless code portability. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- SparkSession (the underlying Apache Spark session interface)
- Databricks Runtime
- Databricks Notebooks
- Serverless Compute on Databricks

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
