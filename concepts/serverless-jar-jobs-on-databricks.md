---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37546cb23c7df1912af7452e3ad8744d8ff486f0cb0fd878896a3a8333b1c500
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-jar-jobs-on-databricks
    - SJJOD
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Serverless JAR Jobs on Databricks
description: Creating and running JAR tasks (Java/Scala Spark code) on serverless compute within Databricks Lakeflow Jobs.
tags:
  - databricks
  - serverless
  - jobs
  - jar
timestamp: "2026-06-19T09:35:30.135Z"
---

# Serverless JAR Jobs on Databricks

**Serverless JAR Jobs on Databricks** allow you to run Java or Scala Spark code packaged as a Java archive (JAR) file on [serverless compute](/concepts/serverless-gpu-compute.md). This enables you to execute Spark workloads without managing cluster infrastructure, while leveraging Databricks' serverless architecture for automatic scaling and resource management. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Overview

A JAR file packages Java or Scala code into a single file that can be deployed as a task in a [Lakeflow Job](/concepts/lakeflow-jobs.md). Serverless compute provides a fully managed execution environment where Databricks handles infrastructure provisioning, scaling, and management. To run JARs on serverless compute, your code must comply with the serverless environment's requirements and limitations. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of building and deploying JARs manually. Bundles simplify project creation with correct dependency versions pre-configured for serverless and enable straightforward deployment to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Requirements

### Development Environment

To build a JAR for serverless compute, your local development environment requires: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- sbt 1.11.7 or higher for Scala JARs
- Maven 3.9.0 or higher for Java JARs
- JDK, Scala, and Databricks Connect versions matching your serverless environment version

### Dependency Versions

Your JAR's Scala and JDK versions must exactly match the runtime versions on serverless compute. For example, serverless environment version 4 requires: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- Scala 2.13
- JDK 17 (class file version 61)
- Databricks Connect 17.3

## Limitations

Serverless compute uses [Spark Connect](/concepts/spark-connect.md), meaning your JAR runs against a thin client library that exposes public Spark APIs while the Spark engine runs server-side. The following are not available on serverless compute: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **RDD API** (`org.apache.spark.rdd.*`) and `SparkContext`/`JavaSparkContext` — use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead
- **Spark internal APIs** (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) — code importing these fails with `NoClassDefFoundError`
- **Native libraries** (`.so`, `.dll`, JNI) — serverless compute does not permit writing native libraries to the file system

Code that bypasses the public API cannot benefit from Catalyst optimization or Photon acceleration. If your workload requires any of the above, run it on standard or dedicated compute instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing Dependencies

To make a library available to your JAR on serverless compute, you have three options: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Provided Libraries

Serverless compute includes Databricks Connect and a curated set of common libraries by default. Declare these as `provided` in your build — bundling your own versions triggers `NoSuchMethodError` at runtime. For environment version 4, provided libraries include: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- `com.databricks:databricks-connect_2.13`, version 17.3.2
- `org.scala-lang:scala-library_2.13`, version 2.13.16
- `org.scala-lang:scala-reflect_2.13`, version 2.13.16
- Various Apache, Jackson, Google, and Commons libraries

### Attached Environment Libraries

Add libraries to your [serverless environment](/concepts/serverless-gpu-environment.md) if they are not already provided. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### External Database Connections

For JDBC sources, use a JDBC connection managed by [Unity Catalog](/concepts/unity-catalog.md) instead of including a driver. This handles credentials, lineage, and governance automatically. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Building a JAR

### Scala Example

Create a Scala project using sbt, configure `build.sbt` with the correct dependency versions and the `sbt-assembly` plugin for building fat JARs. Your main class initializes a `SparkSession` using `SparkSession.builder().getOrCreate()`. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

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

## Creating and Running a Job

1. In your workspace, navigate to **Jobs & Pipelines** and click **Create** > **Job**.
2. Select the **JAR** task type.
3. Configure the task with your main class name (e.g., `com.examples.SparkJar`).
4. Set **Compute** to **Serverless**.
5. Configure the serverless environment with version 4 or higher and attach your JAR file.
6. Add parameters and create the task. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

After running the job, view the output in the **Output** pane, which includes the arguments passed to the task. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — Recommended alternative to manual JAR building
- Serverless Compute — The execution environment for serverless JAR jobs
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The job orchestration framework
- [Spark Connect](/concepts/spark-connect.md) — The underlying connectivity layer for serverless compute
- Photon — Vectorized query engine for Spark workloads
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance and lineage management
- JAR Task for Jobs — Detailed task configuration documentation
- Create a Databricks Compatible JAR — Guidance for building compatible JARs

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
