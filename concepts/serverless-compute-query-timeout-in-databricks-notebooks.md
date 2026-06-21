---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70595be17724ec996e46cf6e417810c676f3f8a6c0829fe7810a8dbda2a461a6
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-query-timeout-in-databricks-notebooks
    - SCQTIDN
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Serverless compute query timeout in Databricks notebooks
description: For notebooks running on serverless compute, queries time out after 9000 seconds by default, configurable via the Spark property spark.databricks.execution.timeout.
tags:
  - databricks
  - serverless
  - configuration
  - timeout
timestamp: "2026-06-18T15:05:10.704Z"
---

# Serverless Compute Query Timeout in Databricks Notebooks

**Serverless Compute Query Timeout** refers to the default maximum execution duration for queries running on Databricks serverless compute within notebooks. When using serverless compute in Databricks notebooks, queries are subject to a configurable timeout that limits how long they can execute before being terminated.

## Default Timeout Behavior

For notebooks running on [serverless compute](/concepts/serverless-gpu-compute.md), queries time out after **9000 seconds** (2.5 hours) by default. This timeout applies to all query executions within the notebook environment, ensuring that long-running or stuck queries do not consume serverless resources indefinitely. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Customizing the Timeout

You can customize the serverless compute query timeout by setting the Spark configuration property `spark.databricks.execution.timeout`. This property allows you to:

- **Increase** the timeout for long-running queries that need more execution time
- **Decrease** the timeout to prevent runaway queries from consuming excessive resources
- **Set** it to any valid duration in seconds

To configure this property, use the method described in Set Spark configuration properties on Databricks. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Configuration Methods

You can set the query timeout property through:

- **Spark configuration UI** in the Databricks workspace
- **Programmatic configuration** using Spark APIs
- **Cluster configuration** when creating or modifying compute resources

The property `spark.databricks.execution.timeout` accepts integer values representing seconds. For example, setting it to `18000` would create a 5-hour timeout window. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Important Considerations

- **Override behavior**: Custom timeout settings apply to all queries running on the notebook, not just specific operations
- **Resource management**: Longer timeouts should be balanced against cluster resource consumption and cost considerations
- **Session context**: The timeout affects queries executed through the default Spark session or any custom sessions created via `DatabricksSession.builder` with serverless configurations

## Related Concepts

- [Serverless compute](/concepts/serverless-gpu-compute.md) - The execution environment for Databricks notebooks
- [DatabricksSession configuration](/concepts/databrickssession-builder-configuration-chain.md) - How Spark sessions are created in serverless environments
- Notebook execution management - Controls for managing notebook behavior
- Spark configuration properties - Available configuration options for Spark workloads

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
