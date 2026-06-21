---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3a00279cf464302bb840d7dd3bd065c63047b3faac8d9c94d80e5cff7c63ac1
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-api-portability
    - DAP
    - databricks-connect-api-portability
    - DCAP
    - databricks-connect-code-portability
    - DCCP
    - code portability
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: DatabricksSession API Portability
description: Databricks Connect APIs are available in Databricks notebooks as part of the runtime, enabling seamless code transitions
tags:
  - api
  - portability
  - databricks
timestamp: "2026-06-19T18:10:38.736Z"
---

## [DatabricksSession](/concepts/databrickssession.md) API Portability

**DatabricksSession API Portability** refers to the property that all APIs provided by [Databricks Connect](/concepts/databricks-connect.md) are also available in Databricks Notebooks as part of the corresponding Databricks Runtime. This design makes it possible to develop and debug code locally in an IDE and then run the same code in a notebook or job without any modifications. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### [DatabricksSession](/concepts/databrickssession.md) Behavior

The `DatabricksSession` class is the entry point for connecting to Databricks compute. Its behavior differs depending on whether the code is executed in a local development environment or inside a Databricks workspace.

#### Local Development Environment

When running code locally outside of Databricks (for example, in an IDE):

- `DatabricksSession.builder.getOrCreate()` returns the existing Spark session for the provided configuration if one exists, or creates a new one if none exists.
- `DatabricksSession.builder.create()` always creates a new Spark session.
- Connection parameters such as `host`, `token`, and `cluster_id` are populated from source code, environment variables, or the `.databrickscfg` configuration profiles file.

For example, the following code creates two separate sessions when run with Databricks Connect:
```python
spark1 = [[databrickssession|DatabricksSession]].builder.create()
spark2 = [[databrickssession|DatabricksSession]].builder.create()
```
^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

#### Databricks Workspace

When running code in a notebook or job inside the Databricks workspace:

- `DatabricksSession.builder.getOrCreate()` with no additional configuration returns the default Spark session—the same as the `spark` variable that is pre-configured to connect to the compute the notebook or job is attached to.
- If additional connection parameters are supplied (e.g., `DatabricksSession.builder.clusterId(...).getOrCreate()` or `DatabricksSession.builder.serverless().getOrCreate()`), a **new** Spark session is created.
- `DatabricksSession.builder.create()` requires explicit connection parameters, such as `DatabricksSession.builder.clusterId(...).create()`. Without them, it returns an `[UNSUPPORTED]` error.

It is also possible to connect to a different Databricks compute instance—one that is not attached to the notebook or job—by using the `remote()` method with configuration keyword arguments or individual methods like `host()` and `token()`. In such cases, a new session is created for the referenced compute, mirroring the behavior outside of a notebook. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Portability in Practice

Because the same APIs work both locally and in the workspace, developers can write and test their code against Databricks compute from their preferred IDE and then deploy it to a Databricks notebook or job without changes. The only adjustment needed is awareness of how `DatabricksSession` behaves in each context—especially whether `getOrCreate()` returns the default session or requires additional parameters to create a new one. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- [DatabricksSession](/concepts/databrickssession.md)
- Local Development Environment
- Databricks Notebooks
- SparkSession
- [.databrickscfg configuration profiles](/concepts/databricks-configuration-profiles.md)

### Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
