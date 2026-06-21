---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb858bc9dc34f0d2fb46ba22db0effb23bfbb979b9a74636264f6e638d625e8a
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-api-portability
    - DCAP
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Databricks Connect API Portability
description: Databricks Connect APIs are available in Databricks notebooks as part of the corresponding Databricks Runtime, allowing code to run in notebooks without any changes after local development.
tags:
  - databricks
  - portability
  - api
timestamp: "2026-06-18T11:35:25.833Z"
---

# Databricks Connect API Portability

**Databricks Connect API Portability** refers to the property that all APIs available through [Databricks Connect](/concepts/databricks-connect.md) in a local development environment (IDE) are also available in Databricks Runtime when running inside a notebook or job within the Databricks workspace. This enables seamless code migration from local development to deployment without requiring any code changes. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Overview

Databricks Connect allows you to connect to Databricks compute from a local development environment outside of Databricks. You can develop, debug, and test your code directly from your IDE before moving it to a notebook or job. To make this transition seamless, **all Databricks Connect APIs are available in Databricks notebooks** as part of the corresponding Databricks Runtime version. This means that code written using Databricks Connect locally will run in a Databricks notebook without any modifications, as long as the runtime in the notebook is compatible with the API version used. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## [DatabricksSession](/concepts/databrickssession.md) Behavior Differences

While the APIs are portable, the behavior of `DatabricksSession` differs slightly depending on whether the code runs locally or inside the Databricks workspace. Understanding these differences helps avoid unexpected errors when moving code between environments.

### Local Development Environment Behavior

When running code locally within an IDE outside of Databricks: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

- `DatabricksSession.builder.getOrCreate()` gets the existing Spark session for the provided configuration if it exists, or creates a new Spark session if it does not exist.
- `DatabricksSession.builder.create()` always creates a new Spark session.
- Connection parameters such as `host`, `token`, and `cluster_id` are populated either from source code, environment variables, or the `.databrickscfg` configuration profiles file.

For example, the following code creates two separate sessions when run locally:

```python
spark1 = [[databrickssession|DatabricksSession]].builder.create()
spark2 = [[databrickssession|DatabricksSession]].builder.create()
```

### Databricks Workspace Behavior

When running code in a notebook or job inside the Databricks workspace: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

- `DatabricksSession.builder.getOrCreate()` **without any additional configuration** returns the default Spark session (also accessible through the pre-configured `spark` variable). This default session is automatically connected to the compute instance to which the notebook or job is attached.
- A **new** Spark session is created only if additional connection parameters are set — for example, using `DatabricksSession.builder.clusterId(...).getOrCreate()` or `DatabricksSession.builder.serverless().getOrCreate()`.
- `DatabricksSession.builder.create()` **requires explicit connection parameters** in a notebook (such as `.clusterId(...)`), otherwise it returns an `[UNSUPPORTED]` error.
- It is possible to connect to *different* Databricks compute (not attached to the notebook or job) using the `remote()` method, which takes configuration keyword arguments or individual methods like `host()` or `token()`. In that case, a new session is created for the referenced compute, similar to local usage.

### Serverless Compute Timeout Note

For notebooks running on [serverless compute](/concepts/serverless-gpu-compute.md), by default queries time out after 9000 seconds. You can customize this by setting the Spark configuration property `spark.databricks.execution.timeout`. See Set Spark Configuration Properties. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Best Practices for Portability

- Write code that uses `DatabricksSession.builder.getOrCreate()` without explicit connection parameters when possible — it will work transparently in both local and workspace environments (using the local config or the workspace’s default session).
- If you need to create additional sessions in a notebook (e.g., to connect to another cluster), always provide `clusterId` or equivalent parameters to avoid `[UNSUPPORTED]` errors.
- Use the same Databricks Runtime version in your notebook that your local Databricks Connect client targets, to ensure full API compatibility.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The tool for local development against Databricks compute
- [DatabricksSession](/concepts/databrickssession.md) — The entry point for creating Spark sessions via Databricks Connect
- Databricks Runtime — The runtime environment that includes the notebook-side APIs
- [IDE Development with Databricks](/concepts/interactive-ide-development-with-databricks-connect.md) — Local debugging workflows
- Notebooks on Databricks — Running code in the workspace
- Serverless Compute — Compute model with default query timeout

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
