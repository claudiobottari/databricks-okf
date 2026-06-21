---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa9270254538ed99533be3be9ed6209844b724b745af150aafc3251e5b4ea20b
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-jar-limitations
    - SCJL
    - Serverless Compute Limitations
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Serverless Compute JAR Limitations
description: "APIs and techniques unavailable on serverless compute: RDD API, Spark internal APIs, and native libraries"
tags:
  - serverless
  - limitations
  - spark
  - databricks
timestamp: "2026-06-18T11:21:41.181Z"
---

# Serverless Compute JAR Limitations

When running JAR tasks on Databricks [serverless compute](/concepts/serverless-gpu-compute.md), there are several important limitations to understand. These constraints arise from the architecture of serverless compute, which uses [Spark Connect](/concepts/spark-connect.md) with a thin client library exposing only public Spark APIs, while the Spark engine itself runs server-side. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Unavailable APIs and Features

### RDD API Restrictions

The RDD API (`org.apache.spark.rdd.*`) and `SparkContext`/`JavaSparkContext` are not available on serverless compute. Instead, use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Spark Internal APIs

Code that imports Spark internal APIs (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) will fail with `NoClassDefFoundError`. Refactor such code to use the public Spark API. If a third-party library uses internals, check whether it publishes a Spark Connect-compatible release. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Native Libraries

Serverless compute does not permit writing native libraries (`.so`, `.dll`, JNI) to the file system. Libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`. Init scripts are not a workaround. If a Java equivalent is available, use that instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Performance Considerations

Code that bypasses the public Spark API cannot benefit from Catalyst optimization or Photon acceleration, even on classic compute. RDD-based and internals-dependent code is generally slower than the equivalent DataFrame or SQL code. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Dependency Version Requirements

To run on serverless compute without failures, your JAR's Scala and JDK versions must exactly match the runtime Scala and JDK versions. For example, serverless environment version 4 requires: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- Compilation against Scala 2.13 (every dependency must use the `_2.13` suffix)
- Compilation against JDK 17, class file version 61
- Compilation against Databricks Connect 17.3 (the Spark API surface for serverless compute)
- Use of only public Spark APIs

## Provided Library Conflicts

The following libraries are provided by default on serverless compute and must be declared as `provided` in your build. Bundling your own versions of these libraries triggers `NoSuchMethodError` at runtime. The list below applies to serverless environment version 4 — see the serverless environment version notes for other versions. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- `com.databricks:databricks-connect_2.13`, version 17.3.2
- `org.scala-lang:scala-library_2.13`, version 2.13.16
- `org.scala-lang:scala-reflect_2.13`, version 2.13.16
- `org.slf4j:slf4j-api`, version 2.0.10
- `org.apache.logging.log4j:log4j-api`, version 2.20.0
- `org.apache.logging.log4j:log4j-core`, version 2.20.0
- `org.apache.httpcomponents:httpclient`, version 4.5.14
- `org.apache.httpcomponents:httpcore`, version 4.4.16
- `com.fasterxml.jackson.core:jackson-databind`, version 2.15.2
- `com.fasterxml.jackson.core:jackson-core`, version 2.15.2
- `com.fasterxml.jackson.core:jackson-annotations`, version 2.15.2
- `com.fasterxml.jackson.datatype:jackson-datatype-jsr310`, version 2.15.2
- `com.google.guava:guava`, version 32.0.1-jre
- `commons-io:commons-io`, version 2.14.0
- `org.json4s:json4s-jackson_2.13`, version 4.0.7
- `org.apache.commons:commons-lang3`, version 3.14.0
- `org.apache.commons:commons-configuration2`, version 2.11.0
- `org.apache.commons:commons-text`, version 1.12.0
- `com.databricks:databricks-sdk-java`, version 0.52.0
- `com.databricks:databricks-dbutils-scala_2.13`, version 0.1.4

## Workloads Requiring Standard Compute

If your workload requires any of the unavailable features listed above (RDD API, Spark internals, native libraries), run it on [standard compute](/concepts/standard-access-mode-compute.md) or [dedicated compute](/concepts/dedicated-access-mode-for-ml-compute.md) instead of serverless compute. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Recommendation

Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of building and deploying JARs manually. Bundles make it easy to create a project from a template with the correct Scala, JDK, and Databricks Connect versions already configured for serverless, and enable simple deployment of the JAR to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Serverless Compute — The compute environment for serverless jobs
- [Spark Connect](/concepts/spark-connect.md) — The protocol used by serverless compute
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The job system for running JAR tasks
- JAR Task for Jobs — Configuring JAR tasks in workflows
- Photon — Vectorized query engine

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
