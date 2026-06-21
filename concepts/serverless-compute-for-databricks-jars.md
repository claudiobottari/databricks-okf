---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43795a91a598986f0508d96366c43e744e2e64a36eee935dd9fcbb3b18dfe73a
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-for-databricks-jars
    - SCFDJ
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Serverless Compute for Databricks JARs
description: How to build, configure, and run Java/Scala JARs as tasks on Databricks serverless compute using Lakeflow Jobs, including version requirements and limitations.
tags:
  - databricks
  - serverless
  - JAR
  - workflows
timestamp: "2026-06-19T18:00:32.278Z"
---

# Serverless Compute for Databricks JARs

**Serverless Compute for Databricks JARs** enables deploying and running Java archive (JAR) files containing Spark code as tasks on serverless compute in a Databricks workflow, without managing cluster infrastructure. JARs package Java or Scala code into a single file and run on serverless compute using a thin client library based on [Spark Connect](/concepts/spark-connect.md).

## Overview

When running a JAR on serverless compute, your code executes against a thin client that exposes the public Spark APIs, while the Spark engine runs server-side. This architecture enables serverless scaling but imposes specific requirements on your code and dependencies. The platform recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of manually building and deploying JARs, as bundles automatically configure the correct Scala, JDK, and Databricks Connect versions for serverless compatibility. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Requirements

To build a JAR compatible with serverless compute, your local development environment must have:
- **sbt** 1.11.7 or higher for Scala JARs
- **Maven** 3.9.0 or higher for Java JARs
- JDK, Scala, and Databricks Connect versions matching your [serverless environment](/concepts/serverless-gpu-environment.md) ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Dependency Versions

Your JAR's Scala and JDK versions must exactly match the runtime versions of the serverless environment. For example, serverless environment version 4 requires:
- Scala 2.13
- JDK 17 (class file version 61)
- Databricks Connect 17.3 ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

All dependencies should use the `_2.13` suffix to match the Scala version. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Limitations

Serverless compute uses [Spark Connect](/concepts/spark-connect.md), which means certain APIs are unavailable and code that bypasses the public Spark API will fail: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **RDD API** (`org.apache.spark.rdd.*`) and `SparkContext` / `JavaSparkContext` are not available. Use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Spark internal APIs** (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) cause `NoClassDefFoundError`. Refactor to the public Spark API. If a third-party library uses internals, check for a [Spark Connect](/concepts/spark-connect.md)-compatible release. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Native libraries** (`.so`, `.dll`, JNI) are not permitted. Serverless compute does not allow writing native libraries to the file system, and init scripts are not a workaround. Libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Code that bypasses the public API cannot benefit from Catalyst optimization or Photon acceleration, even on classic compute. RDD-based and internals-dependent code is generally slower than the equivalent DataFrame or SQL code. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

If your workload requires any of the above, run it on standard or dedicated compute instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing Dependencies

To make a library available to your JAR on serverless compute, use one of three approaches: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **Provided libraries**: Serverless compute includes [Databricks Connect](/concepts/databricks-connect.md) and a curated set of common libraries. Declare them `provided` in your build to avoid bundling duplicates, which would cause `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Attach as an environment library**: Add a library to your serverless environment if it isn't already provided. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **JDBC connections**: For database sources, use a Unity Catalog-managed JDBC connection instead of including a driver. Credentials, lineage, and governance are handled automatically. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Provided Libraries in Environment Version 4

The following libraries are available by default and must be declared `provided`:
- `com.databricks:databricks-connect_2.13` (17.3.2)
- `org.scala-lang:scala-library_2.13` (2.13.16)
- `org.scala-lang:scala-reflect_2.13` (2.13.16)
- Various Apache Commons, Jackson, Log4j, and other common libraries ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Creating a JAR Task

To run a JAR on serverless compute in a Databricks workflow:

1. In your workspace, navigate to **Jobs & Pipelines** and create a new job.
2. Select the **JAR** task type.
3. Enter the **Main class** (e.g., `com.examples.SparkJar`).
4. For **Compute**, select **Serverless**.
5. Configure the serverless environment, selecting environment version 4 or higher, and add your JAR file.
6. Set optional **Parameters** as a JSON array (e.g., `["Hello", "World!"]`). ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Example

A minimal main class for a serverless-compatible JAR: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

```scala
package com.examples

import org.apache.spark.sql.SparkSession

object SparkJar {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder().getOrCreate()
    println(args.mkString(", "))
    println(spark.version)
    println(spark.range(10).limit(3).collect().mkString(" "))
  }
}
```

## Related Concepts

- [Serverless compute](/concepts/serverless-gpu-compute.md) — Infrastructure that provisions compute on demand without cluster management
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The workflow system for running tasks including JAR tasks
- [Spark Connect](/concepts/spark-connect.md) — The communication protocol underlying serverless compute
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — Recommended alternative to manual JAR building
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — GPU-enabled runtime for ML workloads
- Photon — Vectorized query engine for accelerated SQL and DataFrame operations

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
