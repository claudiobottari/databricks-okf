---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3023c35c3f1a782481895a74567177589fca31d931f9f3960195a0e6a89d6bdf
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-spark-session-in-databricks-workspace
    - DSSIDW
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Default Spark Session in Databricks Workspace
description: In Databricks notebooks and jobs, the `spark` variable provides a pre-configured default Spark session that connects to the attached compute, accessible via DatabricksSession.builder.getOrCreate() without extra configuration.
tags:
  - databricks
  - spark
  - notebooks
timestamp: "2026-06-18T11:35:23.847Z"
---

# Default Spark Session in Databricks Workspace

The **default Spark session** in a Databricks workspace is the pre-configured Spark session available as the `spark` variable in notebooks and jobs. It is automatically created when a notebook or job is attached to a compute instance, providing immediate access to Spark functionality without requiring any explicit session creation code.

## Behavior in Notebooks and Jobs

When running code in a Databricks notebook or job, the `spark` variable is pre-configured to connect to the compute instance to which the notebook or job is attached. This means you can start using Spark operations immediately without any setup. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Using [DatabricksSession](/concepts/databrickssession.md)

The `DatabricksSession.builder.getOrCreate()` method returns the default Spark session when used without any additional configuration in a workspace notebook or job. This is different from local development environments where `getOrCreate()` may create a new session if one doesn't already exist. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

If you call `DatabricksSession.builder.getOrCreate()` with additional connection parameters — for example, `DatabricksSession.builder.clusterId(...).getOrCreate()` or `DatabricksSession.builder.serverless().getOrCreate()` — a new Spark session is created rather than returning the default session. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Using create() in Workspace

`DatabricksSession.builder.create()` requires explicit connection parameters when called in a notebook. Without parameters such as `DatabricksSession.builder.clusterId(...).create()`, it returns an `[UNSUPPORTED]` error. This contrasts with local development where `create()` always creates a new Spark session without requiring explicit parameters. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Connecting to Remote Compute

You can use [Databricks Connect](/concepts/databricks-connect.md) to connect to Databricks compute that is not attached to the current notebook or job by using the `remote()` method. The `remote()` method accepts configuration keyword arguments or individual configuration methods such as `host()` or `token()`. When connecting to remote compute, a new session is created for the referenced compute, similar to behavior outside of a Databricks notebook or job. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Serverless Compute Timeout

For notebooks running on serverless compute, the default query timeout is 9000 seconds. You can customize this by setting the Spark configuration property `spark.databricks.execution.timeout`. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Portability

All Databricks Connect APIs are available in Databricks notebooks as part of the corresponding Databricks Runtime. This ensures that code runs seamlessly in a Databricks notebook without any changes when transitioning from local development to deployment. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related Concepts

- [DatabricksSession](/concepts/databrickssession.md) — The API for creating and managing Spark sessions
- [Databricks Connect](/concepts/databricks-connect.md) — The tool for connecting to Databricks compute from local development environments
- Databricks Runtime — The runtime environment that includes all Databricks Connect APIs
- Serverless Compute — A compute option with default query timeout settings
- Spark Configuration — Properties that control Spark behavior, including query timeouts

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
