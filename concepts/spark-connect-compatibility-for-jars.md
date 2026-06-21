---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c42a2f53faffcf69bc39d80806aa88c34e1ceb3b2b557c1f13b7737038864f05
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-connect-compatibility-for-jars
    - SCCFJ
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Spark Connect Compatibility for JARs
description: When running JARs on serverless compute, the JAR must use only public Spark APIs (no RDDs, no Catalyst/Spark internal APIs, no native libraries) because serverless uses Spark Connect under the hood.
tags:
  - spark-connect
  - compatibility
  - serverless
  - limitations
timestamp: "2026-06-19T09:35:20.183Z"
---

# Spark Connect Compatibility for JARs

**Spark Connect Compatibility for JARs** refers to the requirements and limitations that apply when building and running Java or Scala JARs on [serverless compute](/concepts/serverless-gpu-compute.md) in Databricks. Serverless compute uses [Spark Connect](/concepts/spark-connect.md) as its underlying architecture, which means JARs must be compiled against the public Spark API and cannot rely on internal Spark APIs or RDD-based code. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Overview

When you run a JAR task on serverless compute, your code executes against a thin client library that exposes the public Spark APIs, while the Spark engine itself runs server-side. This architecture imposes specific compatibility requirements on the JAR's dependencies, compilation targets, and API usage. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of manually building and deploying JARs. Bundles make it easy to create a project from a template with the correct Scala, JDK, and Databricks Connect versions already configured for serverless, and enable simple deployment of the JAR to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Requirements

### Dependency Versions

To run on serverless compute without failures, your JAR's Scala and JDK versions must exactly match the runtime versions. The example in the source material uses serverless environment version 4, which requires: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **Scala 2.13** — every dependency must use the `_2.13` suffix
- **JDK 17** — class file version 61
- **Databricks Connect 17.3** — the Spark API surface for serverless compute
- **Public Spark APIs only** — no RDDs and no Spark internals

### Build Tools

Your local development environment must have: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **sbt** 1.11.7 or higher for Scala JARs
- **Maven** 3.9.0 or higher for Java JARs

## Limitations

The following are **not available** on serverless compute: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **RDD API** (`org.apache.spark.rdd.*`) and `SparkContext` / `JavaSparkContext` — use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead
- **Spark internal APIs** (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) — code that imports these APIs fails with `NoClassDefFoundError`
- **Native libraries** (`.so`, `.dll`, JNI) — serverless compute does not permit writing native libraries to the file system; libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`

If your workload requires any of the above, run it on standard or dedicated compute instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing Dependencies

To make a library available to your JAR on serverless compute, use one of the following approaches: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **Use a provided library** — serverless compute includes Databricks Connect and a curated set of common libraries. If your version is compatible, declare it `provided` in your build and do not include it in your JAR.
- **Attach as an environment library** — add a library to your [serverless environment](/concepts/serverless-gpu-environment.md) if it is not already provided.
- **Connect to an external database** — for JDBC sources, use a JDBC connection instead of including a driver. JDBC connections are Unity Catalog-managed, and credentials, lineage, and governance are handled for you.

### Provided Libraries

The following libraries are available by default on serverless compute (for environment version 4). Declare them `provided` in your build. Bundling your own versions triggers a `NoSuchMethodError` at runtime: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

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

## Building a Compatible JAR

When building a JAR for serverless compute, your `build.sbt` should configure the correct versions and include the `--add-opens` JVM flag required by Spark Connect: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

```scala
name := "my-spark-app"

scalaVersion := "2.13.16"
javacOptions ++= Seq("--release", "17")
scalacOptions ++= Seq("-release", "17")

libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.2" % "provided"

fork := true
javaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"
```

Use the `sbt-assembly` plugin to create a fat JAR that includes all non-provided dependencies. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md) — The underlying architecture for serverless compute
- Serverless Compute — The compute environment that requires Spark Connect-compatible JARs
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — The recommended alternative to manual JAR building
- [JAR Tasks for Jobs](/concepts/jar-task-in-lakeflow-jobs.md) — How to configure and run JAR tasks in [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- [Databricks Connect](/concepts/databricks-connect.md) — The client library that exposes the Spark API surface
- [Serverless Environment Versions](/concepts/serverless-environment-versioning.md) — Version-specific dependency requirements

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
