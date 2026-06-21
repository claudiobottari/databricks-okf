---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a1ff404319806001ec1196cdccb7878f2bba3bf78996bcc4ef3980d3f537fa22
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-connect-architecture-for-jar-execution
    - SCAFJE
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Spark Connect Architecture for JAR Execution
description: Serverless compute uses Spark Connect; JARs run against a thin client library exposing public Spark APIs while the Spark engine runs server-side; code bypassing public API cannot use Catalyst or Photon optimization.
tags:
  - databricks
  - spark
  - architecture
timestamp: "2026-06-19T14:35:45.022Z"
---

# Spark Connect Architecture for JAR Execution

**Spark Connect Architecture for JAR Execution** refers to the architectural design by which JAR tasks running on [serverless compute](/concepts/serverless-gpu-compute.md) in Databricks interact with the Spark engine through the [Spark Connect](/concepts/spark-connect.md) protocol. Unlike classic compute where JAR code runs inside the same JVM as the Spark driver, serverless compute decouples the client-side JAR process from the server-side engine using a thin client library.

## Architecture Overview

On serverless compute, JAR tasks execute against a thin client library that exposes the public Apache Spark APIs, while the Spark engine itself runs server-side. This architecture means the JAR does not run in the same JVM as the Spark driver. Instead, all DataFrame/Dataset operations are sent from the client to the server via the Spark Connect protocol, where the engine applies Catalyst optimizer transformations and Photon acceleration before execution. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Client-Side Execution Model

The client library used by JAR tasks on serverless compute is [Databricks Connect](/concepts/databricks-connect.md), which provides the public Spark API surface. The JAR code uses standard `SparkSession.builder().getOrCreate()` to establish a connection to the server-side engine. All DataFrame/Dataset operations are compiled and optimized on the server, not on the client. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Advantages of the Spark Connect Architecture

The decoupled architecture provides several benefits for JAR execution:

- **Catalyst optimization**: Code that uses the public DataFrame/Dataset API benefits from Catalyst query optimization and Photon acceleration, even though it runs on the client side. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Isolation**: The client and server can be maintained and versioned independently.
- **Security**: The server-side engine does not run arbitrary JAR code directly, providing a stronger security boundary.

## Limitations and Constraints

Because of the Spark Connect architecture, certain APIs and patterns are unavailable for JAR tasks on serverless compute:

| Unavailable API | Reason | Alternative |
|-----------------|--------|-------------|
| RDD API (`org.apache.spark.rdd.*`) | RDDs are not exposed through Spark Connect | Use DataFrame/Dataset operations instead |
| Spark internal APIs (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) | Internal APIs bypass the public Spark Connect interface | Refactor to use public Spark APIs |
| `SparkContext` / `JavaSparkContext` | Direct context access not available | Use `SparkSession.builder().getOrCreate()` |
| Native libraries (`.so`, `.dll`, JNI) | Serverless compute does not allow writing native libraries to the file system | Use a pure Java equivalent if available |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Code that imports internal APIs fails with `NoClassDefFoundError`. Native libraries that unpack binaries at startup fail with `UnsatisfiedLinkError`. Init scripts are not a workaround for these limitations. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Version Compatibility Requirements

To run on serverless compute without failures, the JAR's Scala and JDK versions must exactly match the runtime versions of the target [serverless environment](/concepts/serverless-gpu-environment.md). For example, for serverless environment version 4:

- Scala 2.13 (all dependencies use the `_2.13` suffix)
- JDK 17 (class file version 61)
- Databricks Connect 17.3

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Dependency Management

Dependencies must be compatible with the Spark Connect architecture:

- **Provided libraries**: Databricks Connect and a curated set of common libraries are available by default on serverless compute. Declare them as `provided` in the build to avoid bundling duplicates. Bundling your own versions of these libraries triggers `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Third-party libraries**: If a third-party library uses Spark internals or RDDs, check whether it publishes a Spark Connect-compatible release. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **JDBC drivers**: Use JDBC connections managed by Unity Catalog instead of including JDBC driver JARs. Credentials, lineage, and governance are handled for you. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Connection Initialization

A JAR task establishes a Spark Connect connection as follows:

```scala
package com.examples

import org.apache.spark.sql.SparkSession

object SparkJar {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder().getOrCreate()
    // All operations use the public DataFrame API
    println(spark.version)
    println(spark.range(10).limit(3).collect().mkString(" "))
  }
}
```

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Relationship to Other Architectures

- Classic Compute JAR Execution: JAR code runs inside the same JVM as the Spark driver, allowing direct access to RDDs and internal APIs. No Spark Connect protocol is used.
- Standard and Dedicated Compute: If a workload requires RDDs, internal APIs, or native libraries, it must run on standard or dedicated compute instead of serverless. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md): Databricks recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of building JARs manually, as bundles automatically configure the correct Scala, JDK, and Databricks Connect versions for serverless. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md) — The wire protocol that enables the decoupled client-server architecture
- Serverless Compute — The compute infrastructure that runs JAR tasks via Spark Connect
- [Databricks Connect](/concepts/databricks-connect.md) — The client library used by JAR tasks on serverless compute
- Catalyst Optimizer — Server-side query optimization available through the public API
- Photon — Vectorized query engine acceleration available through the public API
- [Serverless Environment Versions](/concepts/serverless-environment-versioning.md) — Version mapping for Scala, JDK, and Databricks Connect compatibility
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The job framework for running JAR tasks

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
