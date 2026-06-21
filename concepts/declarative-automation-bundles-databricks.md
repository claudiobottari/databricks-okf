---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a205a7f05e962eb36d46a774646eeaa27ce609263c44f573c93542571b871bb6
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - declarative-automation-bundles-databricks
    - DAB(
    - declarative-automation-bundles-for-scala-jars
    - DABFSJ
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Declarative Automation Bundles (Databricks)
description: Databricks' recommended tool for building and deploying Scala JARs, providing correct Scala, JDK, and Databricks Connect versions pre-configured for serverless compute.
tags:
  - databricks
  - bundles
  - jar
  - deployment
timestamp: "2026-06-19T09:35:59.818Z"
---

# Declarative Automation Bundles (Databricks)

**Declarative Automation Bundles** is a Databricks framework that simplifies building, deploying, and running JAR-based workloads on [serverless compute](/concepts/serverless-gpu-compute.md). It replaces the manual process of constructing JARs and configuring environments with a templated, declarative approach that automatically sets the correct Scala, JDK, and [Databricks Connect](/concepts/databricks-connect.md) versions for the target serverless environment. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Overview

Manually building a JAR for serverless compute requires careful alignment of dependency versions — including Scala, JDK, and Spark Connect API compatibility — or the JAR will fail at runtime with errors like `NoClassDefFoundError` or `NoSuchMethodError`. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Declarative Automation Bundles solve this problem by:

- **Generating a project from a template** that already includes the correct `scalaVersion`, JDK release flags, and the `com.databricks::databricks-connect` dependency at the `provided` scope.
- **Automating deployment** of the compiled JAR to the workspace, so you do not need to manually upload it to the serverless environment.
- **Managing library attachments**: the bundle can attach environment-level libraries (e.g., from the [serverless environment](/concepts/serverless-gpu-environment.md) configuration) so that runtime-only dependencies are available without being bundled inside the JAR.

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Workflow

1. **Create a project** from a Databricks-provided template (using the `databricks bundle init` command or the equivalent IDE wizard).
2. **Write your Spark code** in Scala or Java, using only public Spark API surfaces (DataFrame, Dataset, `SparkSession`). Code that uses RDDs, `SparkContext`, or internal APIs (`catalyst.*`, `util.*`, `sql.internal.*`) will fail on serverless compute.
3. **Declare dependencies** in the build file — mark `databricks-connect` as `provided` and list any other libraries.
4. **Build** the JAR using sbt (for Scala) or Maven (for Java), producing a fat JAR.
5. **Deploy** the bundle to the workspace, which places the JAR in the target serverless environment and creates a [Lakeflow Job](/concepts/lakeflow-jobs.md) that references it.
6. **Run** the job and inspect the output in the job run details pane.

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Dependency Management

Declarative Automation Bundles handle dependencies through three mechanisms: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

| Mechanism | Description |
|-----------|-------------|
| **Provided libraries** | Libraries that the serverless runtime already includes (e.g., `databricks-connect`, `scala-library`, `slf4j-api`) — mark these `provided` in your build. Bundling your own copies will cause `NoSuchMethodError`. |
| **Environment libraries** | Libraries attached to the [serverless environment](/concepts/serverless-gpu-environment.md) via the environment configuration UI — these are available at runtime without being in the JAR. |
| **JDBC connections** | For database sources, use a [Unity Catalog](/concepts/unity-catalog.md)-managed JDBC connection instead of bundling a JDBC driver — this gives you credential, lineage, and governance management. |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Limitations of Serverless Compute

Because serverless compute runs on [Spark Connect](/concepts/spark-connect.md), it imposes constraints that Declarative Automation Bundles must respect: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **No RDD API**: use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations.
- **No Spark internals**: imports of `catalyst.*`, `util.*`, `sql.util.*`, or `sql.internal.*` cause `NoClassDefFoundError`.
- **No native libraries**: `.so`, `.dll`, and JNI are not supported (init scripts are not a workaround).
- **Version locking**: the Scala and JDK versions in the JAR must exactly match the serverless runtime versions — Declarative Automation Bundles enforce this by generating version-aligned templates.

If your workload requires any of these capabilities, run it on standard or dedicated compute instead.

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
