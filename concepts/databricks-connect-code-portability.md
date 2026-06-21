---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f7b8ddf2ef337211f4388a14e78ba0f5247f2c654480e49142f13f605567500
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-code-portability
    - DCCP
    - code portability
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Databricks Connect Code Portability
description: The principle that all Databricks Connect APIs are available in Databricks notebooks as part of the corresponding Databricks Runtime, enabling seamless transitions from local development to deployment without code changes.
tags:
  - databricks
  - portability
  - deployment
timestamp: "2026-06-19T09:49:45.125Z"
---

# Databricks Connect Code Portability

**Databricks Connect Code Portability** refers to the design principle that enables code written using [Databricks Connect](/concepts/databricks-connect.md) in a local development environment to run unchanged in Databricks notebooks and jobs within the Databricks workspace. This portability is achieved by making the same Databricks Connect APIs available in both environments as part of the corresponding Databricks Runtime. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Why Code Portability Matters

Developers can write, debug, and test code in their preferred IDE (such as PyCharm, IntelliJ IDEA, or VS Code) using Databricks Connect, then deploy that same code directly to a Databricks notebook or job without modifications. This removes the need for environment-specific code branches or manual rewriting during the transition from development to production. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## How Portability Works

All Databricks Connect APIs are included in Databricks Runtime for supported versions (Databricks Runtime 13.3 LTS and above). When the same code runs in a notebook or job, it uses the pre-configured Spark session of the attached compute instance. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Key API: `DatabricksSession`

The `DatabricksSession` API is the primary entry point for interacting with Spark clusters. Its behavior varies slightly between local and workspace environments to maintain portability while accommodating each environment's unique characteristics. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

#### Local Development Environment

- `DatabricksSession.builder.getOrCreate()`: Returns an existing Spark session if one exists for the provided configuration, or creates a new one if none exists. Connection parameters are sourced from code, environment variables, or the `.databrickscfg` configuration file. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- `DatabricksSession.builder.create()`: Always creates a new Spark session. When called twice with no additional configuration, it creates two separate sessions (example: `spark1 = [DatabricksSession](/concepts/databrickssession.md).builder.create()` and `spark2 = [DatabricksSession](/concepts/databrickssession.md).builder.create()`). ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

#### Databricks Workspace (Notebooks and Jobs)

- `DatabricksSession.builder.getOrCreate()`: When used without additional configuration, returns the default Spark session (accessible through the `spark` variable), which is pre-configured to connect to the notebook's or job's attached compute instance. A new session is created only when additional connection parameters are specified (e.g., `DatabricksSession.builder.clusterId(...).getOrCreate()`). ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- `DatabricksSession.builder.create()`: Requires explicit connection parameters in a notebook (e.g., `DatabricksSession.builder.clusterId(...).create()`), or it returns an `[UNSUPPORTED]` error. This ensures the user intentionally specifies which compute to connect to. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Connecting to Remote Compute

To connect to a different compute resource than the one attached to the notebook or job, use the `remote()` method with configuration keyword arguments or individual configuration methods like `host()` or `token()`. This creates a new session for the specified compute, mirroring the behavior outside the Databricks workspace. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Serverless Compute Considerations

For notebooks running on serverless compute, queries default to a 9000-second timeout. This can be customized by setting the Spark configuration property `spark.databricks.execution.timeout`. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The underlying library for connecting local code to Databricks compute.
- Databricks Runtime — The runtime environment that includes Databricks Connect APIs.
- SparkSession — The core Spark API for session management.
- IDE Integration — How Databricks Connect integrates with development environments.

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
