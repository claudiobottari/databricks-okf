---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d6598bc94e0a49e54000eef64a29ce55d6a0d573420aadc321361a8533efc103
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-jar-compatibility-requirements
    - SCJCR
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Serverless Compute JAR Compatibility Requirements
description: JARs targeting Databricks serverless compute must exactly match the runtime Scala and JDK versions, use Databricks Connect, and only use public Spark APIs.
tags:
  - databricks
  - compatibility
  - serverless
timestamp: "2026-06-18T14:53:16.689Z"
---



# Serverless Compute JAR Compatibility Requirements

**Serverless Compute JAR Compatibility Requirements** define the specific software dependency and API constraints that a JAR (Java Archive) must satisfy to run successfully on [serverless compute](/concepts/serverless-gpu-compute.md) within a [Lakeflow Job](/concepts/lakeflow-jobs.md) on Databricks. These requirements ensure that compiled Java or Scala code can properly interact with the serverless Spark engine through [Spark Connect](/concepts/spark-connect.md).

## Overview

A JAR packages Java or Scala code into a single file for deployment as a task on serverless compute. Due to the architecture of serverless compute, which uses [Spark Connect](/concepts/spark-connect.md) and a thin client library that exposes only public Spark APIs, JARs must be compiled against specific versions of dependencies and must avoid internal Spark APIs or native code. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Dependency Versions

To run on serverless compute without failures, your JAR's Scala and JDK versions must exactly match the runtime versions provided by the serverless environment. For example, serverless environment version 4 requires:

- **Scala**: 2.13.16
- **JDK**: 17 (class file version 61)
- **Databricks Connect**: 17.3.2

Every dependency must use the correct cross-version suffix (e.g., `_2.13` for Scala libraries). ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Build Tool Requirements

- **sbt** 1.11.7 or higher for Scala JARs
- **Maven** 3.9.0 or higher for Java JARs

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## API and Code Restrictions

Serverless compute does not support the following APIs and code patterns:

- **RDD API** (`org.apache.spark.rdd.*`) and `SparkContext`/`JavaSparkContext` — use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead
- **Spark internal APIs** (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) — code that imports these APIs fails with `NoClassDefFoundError`
- **Native libraries** (`.so`, `.dll`, JNI) — serverless compute does not permit writing native libraries to the filesystem; libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`

If your workload requires any of these, run it on standard or dedicated compute instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Provided Libraries

The following libraries are required dependencies and are available by default on serverless compute (versions listed are for serverless environment version 4). Declare them `provided` in your build; bundling your own versions triggers `NoSuchMethodError` at runtime:

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

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing Dependencies

To make a library available to your JAR on serverless compute, you have three options:

- **Use a provided library**: If your version matches one of the provided libraries, declare it `provided` and exclude it from your JAR
- **Attach as an environment library**: Add a library to your [serverless environment](/concepts/serverless-gpu-environment.md) if it is not already provided
- **Connect to an external database**: For JDBC sources, use a JDBC connection (Unity Catalog-managed) instead of including a driver

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Recommended Approach

Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of building and deploying JARs manually. Declarative Automation Bundles makes it easy to create a project from a template that has the correct Scala, JDK, and Databricks Connect versions already configured for serverless. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Serverless Compute
- [Spark Connect](/concepts/spark-connect.md)
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)
- [Databricks Connect](/concepts/databricks-connect.md)
- JDBC Connection

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
