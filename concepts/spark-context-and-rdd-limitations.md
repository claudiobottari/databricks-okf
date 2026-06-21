---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b861ac04aadfa42b378dacfb97a56be274f9c81cdff76340df3ed46bf84101c
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-context-and-rdd-limitations
    - RDD Limitations and Spark Context
    - SCARL
  citations:
    - file: limitations-with-databricks-connect-for-scala-databricks-on-aws.md
title: Spark Context and RDD Limitations
description: Spark Context and RDDs are not available when using Databricks Connect for Scala; users must use higher-level DataFrame APIs.
tags:
  - databricks-connect
  - spark-context
  - rdd
  - limitations
  - scala
timestamp: "2026-06-19T19:12:49.913Z"
---

# Spark Context and RDD Limitations

**Spark Context and RDD Limitations** refer to the set of restrictions placed on SparkContext and Resilient Distributed Datasets (RDDs) when using [Databricks Connect](/concepts/databricks-connect.md) for Scala. These limitations affect how users can interact with Spark's core low-level APIs from a remote client environment.

## Overview

Databricks Connect enables developers to connect popular IDEs, notebook servers, and custom applications to Databricks compute resources. However, when using this connection method, certain fundamental Spark APIs are not available for use. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

The most significant restriction is that **Spark Context** and **RDDs** are **not available** when working through Databricks Connect. This means users cannot directly create or manipulate RDDs, nor can they use the SparkContext API to configure or interact with the Spark cluster at the lowest level. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Specific Limitations

### Unavailable APIs

The following capabilities are **not available** when using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md):

- SparkContext — cannot be directly accessed or used
- RDDs (Resilient Distributed Datasets) — cannot be created or manipulated
- Changing the log4j log level through `SparkContext`
- Distributed ML training
- Synchronizing the local development environment with the remote compute resource

^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

### Additional Restrictions

Beyond the Spark Context and RDD limitations, [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) also restricts:

- **Streaming `foreachBatch`** — Not available on Databricks Runtime 13.3 LTS and below
- **Large unresolved logical plans** — Creating DataFrames with an unresolved logical plan larger than 128 MB is not supported. This limit applies to the plan size, not the data itself.
- **Long queries** — Queries over 3600 seconds are not supported
- **Scalar UDFs** — Not available on compute resources using dedicated access mode (formerly single user)
- **`CREATE TABLE <table-name> AS SELECT`** — Not available (use `spark.sql("SELECT ...").write.saveAsTable("table")` instead)

^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Workarounds

Since RDDs and SparkContext are unavailable, users must rely on higher-level Spark APIs when using Databricks Connect. These include:

- DataFrames and Datasets — Use the SparkSession API instead of SparkContext
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — Use streaming APIs that work with DataFrames
- `spark.sql()` — For executing SQL queries and saving results with `.write.saveAsTable()`

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)
- [Spark Session](/concepts/databrickssession.md)
- DataFrame API
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)
- Log4j Configuration
- Databricks Runtime

## Sources

- limitations-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-scala-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-scala-databricks-on-aws-8e97ac24.md)
