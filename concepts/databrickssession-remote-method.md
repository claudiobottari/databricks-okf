---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 01d06717af8c577b8adb9658f5dc4f8559e40efafa12f4acef9f4a4ea2c35bc2
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-remote-method
    - DRM
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: DatabricksSession remote() Method
description: A method that allows DatabricksSession to connect to Databricks compute not attached to the current notebook or job by specifying configuration kwargs or individual configuration methods like host() or token().
tags:
  - databricks
  - api
  - remote-connection
timestamp: "2026-06-19T09:49:16.271Z"
---

# [DatabricksSession](/concepts/databrickssession.md) remote() Method

The **`DatabricksSession.remote()` method** is a configuration builder on `DatabricksSession` that allows connecting to a Databricks compute resource that is different from the one the current notebook or job is attached to. This enables multi-cluster or cross-workspace access patterns within a single session.

## Overview

The `remote()` method is typically used within a Databricks notebook or job to establish a connection to a separate Databricks compute cluster. It accepts configuration keyword arguments or can be chained with individual configuration methods such as `host()` or `token()`. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Behavior in Different Environments

### Databricks Workspace (Notebooks and Jobs)

When running code in a Databricks notebook or job, the default `spark` variable is pre-configured to connect to the attached compute instance. The `remote()` method creates a new session for a different compute resource, overriding the default attachment. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

```python
# Connect to a different cluster from a notebook
from databricks.connect import [[databrickssession|DatabricksSession]]

remote_spark = [[databrickssession|DatabricksSession]].builder.remote(
    host="https://<workspace-url>",
    token="<personal-access-token>",
    cluster_id="<cluster-id>"
).getOrCreate()
```

When `remote()` is used, a new session is created for the referenced compute, similar to how Databricks Connect behaves outside of a Databricks notebook or job. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Local Development Environment

In a local development environment (outside Databricks), the `remote()` method is not typically needed because `DatabricksSession.builder.getOrCreate()` and `DatabricksSession.builder.create()` already handle connection parameters from source code, environment variables, or `.databrickscfg` configuration profiles. However, `remote()` can still be used for clarity or to override default connection parameters. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Usage Patterns

### Chaining with Other Configuration Methods

The `remote()` method can be combined with other builder methods for fine-grained control:

```python
spark = [[databrickssession|DatabricksSession]].builder \
    .remote(host="https://<workspace-url>") \
    .token("<personal-access-token>") \
    .clusterId("<cluster-id>") \
    .getOrCreate()
```

### Creating a New Session

When paired with `create()`, the `remote()` method ensures a new session is established rather than reusing an existing one:

```python
new_session = [[databrickssession|DatabricksSession]].builder \
    .remote(host="https://<workspace-url>") \
    .getOrCreate()
```

## Key Differences from Default Behavior

| Aspect | Default `spark` variable | With `remote()` |
|--------|------------------------|-----------------|
| Target compute | Attached cluster/job compute | Specified remote compute |
| Session reuse | Reuses default session | Creates new session |
| Configuration | Pre-configured | Must be explicitly provided |

## Related Concepts

- [DatabricksSession builder](/concepts/databrickssession-builder-api.md) — The builder pattern for creating [DatabricksSession](/concepts/databrickssession.md) instances
- [Databricks Connect](/concepts/databricks-connect.md) — The framework for connecting to Databricks compute from local environments
- DatabricksSession getOrCreate() — Method that returns existing or creates new session
- [DatabricksSession create()](/concepts/databrickssessiongetorcreate-vs-create.md) — Method that always creates a new session
- [Personal Access Tokens](/concepts/databricks-personal-access-token-pat-authentication.md) — Authentication mechanism for remote connections

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
