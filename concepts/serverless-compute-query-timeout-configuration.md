---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44cce4a6089bf3b9551a5ef449ab61729ac186b4ceebb193bcd2de67aa31adf3
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-query-timeout-configuration
    - SCQTC
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Serverless compute query timeout configuration
description: For notebooks on serverless compute, queries default to 9000 second timeout, configurable via spark.databricks.execution.timeout
tags:
  - serverless
  - timeout
  - configuration
  - databricks
timestamp: "2026-06-19T18:10:50.657Z"
---

Here is the updated wiki page for "Serverless compute query timeout configuration".

---

## Serverless compute query timeout configuration

**Serverless compute query timeout configuration** refers to the ability to customize the default query timeout for notebooks running on Databricks serverless compute.

### Default behavior

For notebooks running on serverless compute, queries time out after 9000 seconds by default. This is the default timeout period for serverless compute sessions. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Customization

You can customize this default timeout by setting the Spark configuration property `spark.databricks.execution.timeout`. This property controls the query timeout for serverless compute. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Setting the property

To set a custom timeout value, specify the duration in seconds. For example, to set a timeout of 5000 seconds, configure `spark.databricks.execution.timeout=5000`. For more information, see Set Spark configuration properties on Databricks. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Related concepts

- Spark configuration properties — Properties that control various aspects of Spark behavior
- [Serverless compute](/concepts/serverless-gpu-compute.md) — Compute that does not require a running cluster
- [Databricks Connect](/concepts/databricks-connect.md) — A tool for connecting to Databricks from a local environment
- DatabricksSession behavior — Differences in session behavior when using Databricks Connect

### Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
