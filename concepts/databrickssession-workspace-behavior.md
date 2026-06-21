---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b2d022fab086e82411902b500d296f3e4d98e29d818b3b2711955279cd32519
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-workspace-behavior
    - DWB
    - DatabricksSession behavior
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: DatabricksSession workspace behavior
description: In Databricks notebooks/jobs, getOrCreate() returns the default pre-configured Spark session, while create() requires explicit connection parameters
tags:
  - workspace
  - session
  - databricks
timestamp: "2026-06-19T18:10:46.826Z"
---

---
title: [DatabricksSession](/concepts/databrickssession.md) workspace behavior
summary: Behavior of [DatabricksSession](/concepts/databrickssession.md) when used inside Databricks notebooks or jobs, including getOrCreate, create, and remote connection.
sources:
  - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19TT00:00:00Z"
updatedAt: "2026-06-19T00:00:00Z"
tags:
  - databricks
  - databricks-connect
  - apis
  - notebooks
aliases:
  - databrickssession-workspace-behavior
  - DSWB
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 0
---

# [DatabricksSession](/concepts/databrickssession.md) workspace behavior

`DatabricksSession` is the entry point for using [Databricks Connect](/concepts/databricks-connect.md) APIs. Its behavior differs when code is executed inside a Databricks notebook or job compared to a local development environment. This page describes the workspace-specific behavior.

## Overview

[Databricks Connect](/concepts/databricks-connect.md) allows you to develop code locally and then deploy it to Databricks without changes. All Databricks Connect APIs are available in Databricks notebooks as part of the corresponding Databricks Runtime. This portability means that `DatabricksSession` behaves consistently in most cases, but with important differences in how sessions are created and configured in the workspace. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Workspace behavior

### `getOrCreate()`

When running code in a notebook or job in the Databricks workspace, `DatabricksSession.builder.getOrCreate()` returns the default Spark session (also accessible through the `spark` variable) when used without any additional configuration. The `spark` variable is pre-configured to connect to the compute instance to which the notebook or job is attached. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

If additional connection parameters are set — for example, by using `DatabricksSession.builder.clusterId(...).getOrCreate()` or `DatabricksSession.builder.serverless().getOrCreate()` — a **new** Spark session is created, separate from the default `spark` session. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### `create()`

`DatabricksSession.builder.create()` requires explicit connection parameters in a notebook. For example, you must write `DatabricksSession.builder.clusterId(...).create()`. Without explicit parameters, the method returns an `[UNSUPPORTED]` error. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Remote connections

It is possible to use Databricks Connect to connect to Databricks compute that is **not** attached to the notebook or job. This is done using the `remote()` method, which accepts configuration `**kwargs` or individual configuration methods such as `host()` or `token()`. In these cases, a new session is created for the referenced compute, behaving the same as when Databricks Connect is used outside of a Databricks notebook or job. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Serverless compute timeout

For notebooks running on [serverless compute](/concepts/serverless-gpu-compute.md), by default queries time out after 9000 seconds. You can customize this by setting the Spark configuration property `spark.databricks.execution.timeout`. See Set Spark configuration properties on Databricks. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Comparison with local development

In a local development environment (e.g., an IDE outside Databricks), `DatabricksSession.builder.getOrCreate()` behaves like a typical singleton: it returns the existing Spark session for the provided configuration if one exists, or creates a new one if it does not. In contrast, `DatabricksSession.builder.create()` always creates a new Spark session. Connection parameters such as `host`, `token`, and `cluster_id` are populated from source code, environment variables, or the `.databrickscfg` configuration profiles file. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework that enables local development with Databricks compute.
- SparkSession — The underlying Spark API that `DatabricksSession` wraps.
- Databricks Runtime — The runtime environment that includes Databricks Connect APIs.
- [Serverless compute](/concepts/serverless-gpu-compute.md) — Compute option with a default query timeout.

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
