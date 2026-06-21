---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8312dbad1f45657ca9fbb2281e056f51a7ea14d447cf6b1d6f8cb9ce560b7078
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-connections-from-databricks-notebooks
    - RCFDN
    - Get connection details for a Databricks compute resource
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Remote Connections from Databricks Notebooks
description: Databricks Connect's remote() function allows notebooks to connect to Databricks compute not attached to the notebook or job, using configuration kwargs or methods like host() and token() to create a new session.
tags:
  - databricks
  - remote-connectivity
  - notebooks
timestamp: "2026-06-18T11:35:31.833Z"
---

# Remote Connections from Databricks Notebooks

**Remote Connections from Databricks Notebooks** refers to the ability to connect from a Databricks notebook or job to separate Databricks compute resources—such as a different cluster or serverless compute—using [Databricks Connect](/concepts/databricks-connect.md) APIs. This capability allows notebooks to access multiple compute environments simultaneously, enabling scenarios where different workloads require different compute configurations or isolation. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Overview

Databricks Connect pipelines are available within Databricks notebooks as part of the corresponding Databricks Runtime, starting from Databricks Runtime 13.3 LTS and above. This means that all APIs available in the local development environment are also available in notebooks, ensuring seamless portability between local development and production deployment. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

The key difference between local and workspace environments is how session creation behaves. In a notebook, the `spark` variable is pre-configured to connect to the compute instance to which the notebook or job is attached. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Using `remote()` for Remote Connections

To connect to Databricks compute that is **not** the compute attached to the current notebook or job, use the `remote()` method on `DatabricksSession.builder`. This method accepts configuration keyword arguments or individual configuration methods such as `host()` or `token()`. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

remote_session = [[databrickssession|DatabricksSession]].builder.remote(
    host="https://your-workspace.cloud.databricks.com",
    token="your-personal-access-token",
    cluster_id="your-cluster-id"
).getOrCreate()
```

## Session Behavior

The behavior of `DatabricksSession.builder` differs from the local development environment when used inside a Databricks notebook: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

| Method | In Local IDE | In Databricks Notebook |
|--------|--------------|------------------------|
| `builder.getOrCreate()` | Returns existing session or creates new one using configured parameters | Returns the default Spark session (`spark` variable) when used without additional configuration. Creates a new session if additional connection parameters are specified (e.g., `builder.clusterId(...).getOrCreate()` or `builder.serverless().getOrCreate()`) |
| `builder.create()` | Always creates a new Spark session | Requires explicit connection parameters (e.g., `builder.clusterId(...).create()`). Returns an `[UNSUPPORTED]` error otherwise |

When `remote()` is used, a new session is always created for the referenced compute, matching the behavior of Databricks Connect outside of a notebook. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Use Cases

Remote connections from notebooks enable several practical scenarios:

- **Cross-cluster data access**: Query data from a cluster optimized for a specific workload while running code on a different compute resource.
- **Isolation of workloads**: Run development or testing workloads against a separate compute environment without affecting the primary attached cluster.
- **Serverless compute access**: Use `builder.serverless()` to route specific operations to [serverless compute](/concepts/serverless-gpu-compute.md) while keeping the main session on a classic cluster.
- **Multi-environment workflows**: Connect to different environments (dev, staging, production) from a single notebook for comparison or migration tasks.

## Considerations

- Authentication for remote connections requires valid credentials—typically a personal access token or service principal credentials.
- Data transfer between the notebook's compute and the remote compute incurs network overhead, which may affect performance for large datasets.
- Remote connections follow the same security and governance rules as direct connections, including [Unity Catalog](/concepts/unity-catalog.md) permissions and ABAC policies.
- For notebooks running on serverless compute, queries time out after 9000 seconds by default. This timeout can be customized by setting the Spark configuration property `spark.databricks.execution.timeout`. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Portability

One of the key benefits of using Databricks Connect APIs in notebooks is [code portability](/concepts/databricks-connect-code-portability.md). Code written for remote connections in a local IDE can be moved to a Databricks notebook without changes. The same APIs work in both environments, with the session behavior adapting to the runtime context. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables remote connections to Databricks compute
- [DatabricksSession](/concepts/databrickssession.md) — The main entry point for creating and managing remote connections
- [Serverless compute](/concepts/serverless-gpu-compute.md) — Compute type that can be targeted via remote connections
- [Personal access tokens](/concepts/databricks-personal-access-token-pat-authentication.md) — Authentication mechanism for remote connections
- Cluster configuration — Parameters needed to establish a remote connection

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
