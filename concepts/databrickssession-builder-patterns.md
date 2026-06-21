---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fea891129d84749a71a1b73503c8728d08fd54fdba78cf511c9d37a3318c151e
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-builder-patterns
    - DBP
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: DatabricksSession Builder Patterns
description: The getOrCreate() and create() methods on DatabricksSession.builder behave differently depending on whether code runs in a local IDE (Databricks Connect) or in the Databricks workspace (notebooks/jobs).
tags:
  - databricks
  - session-management
  - api
timestamp: "2026-06-18T11:35:32.969Z"
---

# [DatabricksSession](/concepts/databrickssession.md) Builder Patterns

**DatabricksSession Builder Patterns** describe the different behaviors and best practices for creating `DatabricksSession` instances depending on whether code runs in a local development environment or within a Databricks workspace notebook or job. Understanding these patterns ensures smooth transitions between local development and deployment. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Overview

`DatabricksSession` is the entry point for [Databricks Connect](/concepts/databricks-connect.md), allowing you to connect to Databricks compute from local development environments or from within Databricks notebooks and jobs. The builder provides two primary creation methods with different semantics depending on the runtime context. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Builder Methods

### `getOrCreate()`

Returns an existing Spark session for the provided configuration if one exists, or creates a new one if it doesn't. The default behavior differs between local and workspace environments.

### `create()`

Always creates a new Spark session. This method requires explicit connection parameters when called from within a Databricks notebook or job.

## Local Development Environment Patterns

When using Databricks Connect from an IDE or other local development environment: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

- `DatabricksSession.builder.getOrCreate()` gets the existing Spark session for the provided configuration if it exists, or creates a new session if it doesn't.
- `DatabricksSession.builder.create()` always creates a new Spark session.
- Connection parameters (`host`, `token`, `cluster_id`, etc.) are populated from source code, environment variables, or the `.databrickscfg` configuration profiles file.

### Example: Creating Multiple Sessions

The following code creates two separate sessions when run using Databricks Connect locally: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

```python
spark1 = [[databrickssession|DatabricksSession]].builder.create()
spark2 = [[databrickssession|DatabricksSession]].builder.create()
```

## Databricks Workspace Patterns

When running code in a Databricks notebook or job, the behavior changes significantly: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Default Session

`DatabricksSession.builder.getOrCreate()` returns the default Spark session (also accessible through the `spark` variable) when used without any additional configuration. The `spark` variable is pre-configured to connect to the compute instance to which the notebook or job is attached. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Creating Alternative Sessions

A new Spark session is created if additional connection parameters are set: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

```python
# Connect to a different cluster
spark2 = [[databrickssession|DatabricksSession]].builder.clusterId("your-cluster-id").getOrCreate()

# Connect to serverless compute
spark3 = [[databrickssession|DatabricksSession]].builder.serverless().getOrCreate()
```

### Using `create()` in Notebooks

`DatabricksSession.builder.create()` requires explicit connection parameters in a notebook: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

```python
# This works
spark = [[databrickssession|DatabricksSession]].builder.clusterId("your-cluster-id").create()

# This returns an UNSUPPORTED error
spark = [[databrickssession|DatabricksSession]].builder.create()
```

### Remote Connections

Use `remote()` to connect to Databricks compute that is not attached to the notebook or job: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

```python
spark = [[databrickssession|DatabricksSession]].builder.remote(
    host="your-workspace-url",
    token="your-token",
    cluster_id="your-cluster-id"
).getOrCreate()
```

The `remote()` method accepts configuration keyword arguments or individual configuration methods such as `host()` or `token()`. In these cases, a new session is created for the referenced compute, similar to behavior outside of a Databricks notebook or job. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Portability

All Databricks Connect APIs are available in Databricks notebooks as part of the corresponding Databricks Runtime. This allows you to run code developed locally in a Databricks notebook without any changes, provided you follow the appropriate builder patterns for each environment. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Best Practices

- Use `getOrCreate()` in production code for idempotent session creation.
- Use `create()` explicitly only when you need multiple independent sessions.
- In notebooks, rely on the default `spark` variable for the attached compute instance.
- When connecting to external compute from a notebook, always use `remote()` or explicit connection parameters.

## Serverless Compute Considerations

For notebooks running on serverless compute, queries time out after 9000 seconds by default. Customize this by setting the Spark configuration property `spark.databricks.execution.timeout`. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework for connecting local IDEs to Databricks compute
- SparkSession — The underlying Spark session managed by [DatabricksSession](/concepts/databrickssession.md)
- [Serverless compute](/concepts/serverless-gpu-compute.md) — Compute mode with different timeout characteristics
- .databrickscfg — Configuration profiles file for connection parameters

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
