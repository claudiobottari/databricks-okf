---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 523b22dcd0e842b14fcab9ae02686e3fd10d865e1ad67abef3822db283fe7ecc
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-limitations-for-jar-tasks
    - SCLFJT
    - Serverless Compute Limitations
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md#limitations
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md#dependency-versions
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md#provided-libraries
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Serverless Compute Limitations for JAR Tasks
description: "Restrictions when running JARs on Databricks serverless compute: no RDD API, no Spark internal APIs, no native libraries; code must use public Spark APIs only."
tags:
  - databricks
  - serverless
  - limitations
timestamp: "2026-06-19T14:35:27.053Z"
---

# Serverless Compute Limitations for JAR Tasks

**Serverless Compute Limitations for JAR Tasks** describes the constraints that apply when running Java or Scala JARs on [serverless compute](/concepts/serverless-gpu-compute.md) in Databricks [Lakeflow Jobs](/concepts/lakeflow-jobs.md). These limitations arise from the architecture of serverless compute, which uses [Spark Connect](/concepts/spark-connect.md) and relies on a thin client library that exposes only public Spark APIs while the engine runs server-side. Code that bypasses the public API cannot benefit from Catalyst optimization or Photon acceleration. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md#limitations]

## Unavailable APIs

### RDD API

The RDD API (`org.apache.spark.rdd.*`) and `SparkContext` / `JavaSparkContext` are not available. Code should use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md#limitations]

### Spark Internal APIs

Spark internal APIs (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) are not available. Code that imports these APIs will fail with `NoClassDefFoundError`. Refactor to the public Spark API. If a third-party library uses internals, check whether it publishes a Spark Connect-compatible release. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md#limitations]

### Native Libraries

Native libraries (`.so`, `.dll`, JNI) are not permitted on serverless compute. Serverless compute does not allow writing native libraries to the file system. Libraries that unpack native binaries at startup will fail with `UnsatisfiedLinkError`. Init scripts are not a workaround. Use a Java equivalent if one is available. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md#limitations]

## Dependency Version Constraints

To run on serverless compute without failures, the JAR's Scala and JDK versions must exactly match the runtime Scala and JDK versions of the [serverless environment](/concepts/serverless-gpu-environment.md). For example, environment version 4 requires compilation against Scala 2.13, JDK 17 (class file version 61), and Databricks Connect 17.3. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md#dependency-versions]

### Provided Libraries

Serverless compute includes a curated set of required libraries that are available by default. These must be declared `provided` in the build tool and must **not** be bundled into the JAR. Bundling your own versions will trigger a `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md#provided-libraries]

The list of provided libraries for environment version 4 includes (but is not limited to):
- `com.databricks:databricks-connect_2.13` v17.3.2
- `org.scala-lang:scala-library_2.13` v2.13.16
- `org.slf4j:slf4j-api` v2.0.10
- `org.apache.logging.log4j:log4j-api` v2.20.0
- `com.fasterxml.jackson.core:jackson-databind` v2.15.2
- `com.google.guava:guava` v32.0.1-jre
- `commons-io:commons-io` v2.14.0
- `com.databricks:databricks-sdk-java` v0.52.0
- `com.databricks:databricks-dbutils-scala_2.13` v0.1.4

(Full list available in the [serverless environment version notes](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/).) ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md#provided-libraries]

## Workload Suitability

If a workload depends on RDDs, Spark internal APIs, or native libraries, Databricks recommends running it on standard or dedicated compute instead of serverless compute. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md#limitations]

## Recommended Alternative

Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of building and deploying JARs manually. Bundles make it easy to create a project from a template with the correct Scala, JDK, and Databricks Connect versions for serverless, and enable simple deployment of the JAR to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Serverless compute](/concepts/serverless-gpu-compute.md) — The execution environment for JAR tasks.
- [Spark Connect](/concepts/spark-connect.md) — The protocol underpinning serverless compute.
- Photon — Vectorized query engine (not available for non-public APIs).
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — Recommended alternative to manual JAR deployment.
- [JAR task for jobs](/concepts/jar-task-in-lakeflow-jobs.md) — How to configure and run JAR tasks.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — Job orchestration on Databricks.

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. create-and-run-jars-on-serverless-compute-databricks-on-aws.md#limitations
2. create-and-run-jars-on-serverless-compute-databricks-on-aws.md#dependency-versions
3. create-and-run-jars-on-serverless-compute-databricks-on-aws.md#provided-libraries
4. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
