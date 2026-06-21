---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51296cbbb8192dc7708832ebf7654d71540c7a80c76497d94632b7c7ac15095a
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-connect-api-limitations-on-serverless
    - SCALOS
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Spark Connect API Limitations on Serverless
description: Serverless compute uses Spark Connect, which prohibits RDD APIs, Spark internal APIs, and native libraries; code must use only public Spark APIs (DataFrame/Dataset/SQL).
tags:
  - spark-connect
  - limitations
  - serverless
  - API
timestamp: "2026-06-19T18:00:18.405Z"
---

# Spark Connect API Limitations on Serverless

**Spark Connect API Limitations on Serverless** describes the restrictions placed on user code when running on Serverless Compute in Databricks. Because serverless compute uses [Spark Connect](/concepts/spark-connect.md) as its communication protocol, only a subset of the Apache Spark API is available. Code that relies on internal or legacy APIs fails at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Overview

Serverless compute runs the Spark engine server-side while a thin client library exposes only the public Spark API. User-written JARs or notebooks must comply with the Spark Connect surface; otherwise, the job may throw exceptions such as `NoClassDefFoundError` or `UnsatisfiedLinkError`. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Unavailable APIs and Features

The following Spark components are **not available** on serverless compute:

- **RDD API** (`org.apache.spark.rdd.*`) and direct use of `SparkContext` / `JavaSparkContext`. Use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Spark internal APIs** (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`). Code that imports these packages fails with `NoClassDefFoundError`. Refactor to the public Spark API. If a third-party library uses internals, check whether it publishes a Spark Connect‑compatible release. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Native libraries** (`.so`, `.dll`, JNI). Serverless compute does not permit writing native libraries to the file system. Libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`. Init scripts are not a workaround. Use a Java equivalent if one is available. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Performance Considerations

Code that bypasses the public API cannot benefit from Catalyst optimizer or Photon acceleration, even on classic compute. RDD-based and internals-dependent code is generally slower than the equivalent DataFrame or SQL code. Therefore, using only public APIs not only ensures compatibility but also enables better performance. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## When to Use Standard/Dedicated Compute

If your workload requires any of the unavailable APIs or features, run it on standard or dedicated compute instead. Serverless compute is designed for workloads that can be expressed entirely through the Spark Connect API. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md)
- Serverless Compute
- Photon
- Catalyst Optimizer
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- [Databricks Connect](/concepts/databricks-connect.md)

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
