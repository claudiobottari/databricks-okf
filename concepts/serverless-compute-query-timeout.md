---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7903dc094cb766047a12bf7698cc1c83cd8cfd6137859523ddecfaebe45d0c7
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-query-timeout
    - SCQT
    - serverless-compute-query-timeout-configuration
    - SCQTC
    - serverless-compute-query-timeout-in-databricks-notebooks
    - SCQTIDN
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Serverless Compute Query Timeout
description: A configurable timeout property (spark.databricks.execution.timeout) for Databricks notebooks running on serverless compute, which defaults to 9000 seconds.
tags:
  - databricks
  - serverless
  - configuration
  - timeout
timestamp: "2026-06-19T09:49:23.465Z"
---

# Serverless Compute Query Timeout

The **Serverless Compute Query Timeout** is the maximum duration a query is allowed to run on a Databricks serverless compute resource before it is automatically terminated. For notebooks executing on serverless compute, the default timeout is **9000 seconds** (2.5 hours). ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Customizing the Timeout

You can override the default timeout by setting the Spark configuration property `spark.databricks.execution.timeout`. Changing this property adjusts the timeout for all queries running on the serverless compute instance. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

For instructions on how to set Spark configuration properties, see Set Spark configuration properties on Databricks.

## Related Concepts

- [Serverless compute](/concepts/serverless-gpu-compute.md) – The execution environment subject to this timeout.
- Spark configuration properties – How to configure Spark settings in Databricks.
- Databricks notebooks – The primary interface where notebooks run on serverless compute.

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
