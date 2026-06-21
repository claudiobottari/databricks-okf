---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e62a0327899ffad2315a233d8d40af231ee959b76516b9047ed01835a80cdfc
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-connection-in-databricks-connect
    - RCIDC
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Remote connection in Databricks Connect
description: Using the remote() method to connect to Databricks compute that is not attached to the current notebook or job, allowing connections to separate clusters via configuration kwargs or methods like host() and token().
tags:
  - databricks
  - remote-connection
  - configuration
timestamp: "2026-06-18T15:05:04.114Z"
---

# Remote Connection in Databricks Connect

**Remote connection in Databricks Connect** refers to the ability to connect to Databricks compute from outside the Databricks workspace — typically a local IDE — and to also connect to a different Databricks compute instance from within a Databricks notebook or job. This enables flexible development and testing across environments.

## Overview

Databricks Connect allows you to develop, debug, and test code in a local development environment (such as an IDE) and then seamlessly move that code to a Databricks notebook or job. The Databricks Connect APIs are available in Databricks notebooks as part of the corresponding Databricks Runtime, so code written locally can run in a notebook without modification. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## [DatabricksSession](/concepts/databrickssession.md) Behavior

The `DatabricksSession` object behaves differently depending on whether it is used in a local environment outside Databricks or inside a Databricks notebook or job. Understanding these differences is essential for correctly managing Spark sessions in remote connections.

### Local Development Environment

When running code locally in an IDE:

- `DatabricksSession.builder.getOrCreate()` — Returns the existing Spark session for the provided configuration if it exists, or creates a new one if it does not.
- `DatabricksSession.builder.create()` — Always creates a new Spark session.
- Connection parameters (`host`, `token`, `cluster_id`) are populated from source code, environment variables, or the `.databrickscfg` configuration profiles file.

The following example creates two separate sessions: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

```python
spark1 = [[databrickssession|DatabricksSession]].builder.create()
spark2 = [[databrickssession|DatabricksSession]].builder.create()
```

### Databricks Workspace (Notebooks and Jobs)

When running code in a Databricks notebook or job:

- `DatabricksSession.builder.getOrCreate()` — Returns the default Spark session (also accessible through the `spark` variable) when used without any additional configuration. The `spark` variable is pre‑configured to connect to the compute instance to which the notebook or job is attached. If additional connection parameters are set (e.g., `DatabricksSession.builder.clusterId(...).getOrCreate()`), a new session is created.
- `DatabricksSession.builder.create()` — Requires explicit connection parameters (e.g., `DatabricksSession.builder.clusterId(...).create()`), otherwise it returns an `[UNSUPPORTED]` error.

To connect to a different Databricks compute instance from within a notebook or job, use the `remote()` method. The `remote()` method accepts configuration keyword arguments or individual configuration methods such as `host()` or `token()`. In these cases, a new session is created for the referenced compute, similar to how it works outside a Databricks notebook or job. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Serverless Compute Timeout

For notebooks running on serverless compute, queries time out after 9000 seconds by default. This timeout can be customized by setting the Spark configuration property `spark.databricks.execution.timeout`. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The broader tool for connecting local environments to Databricks.
- [DatabricksSession](/concepts/databrickssession.md) — The session object used for interacting with Databricks compute.
- Spark Session Management — Best practices for managing Spark sessions in distributed environments.
- Serverless Compute — Compute mode that imposes a default query timeout.

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
