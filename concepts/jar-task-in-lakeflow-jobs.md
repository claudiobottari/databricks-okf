---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03dce91089c55d63370180703fcc1e457eee6de1c613e9e2f3c821ebaf093213
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - jar-task-in-lakeflow-jobs
    - JTILJ
    - JAR Tasks for Jobs
    - JAR task for jobs
    - JAR tasks for jobs
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: JAR Task in Lakeflow Jobs
description: A Databricks workflow task type that runs a compiled Java/Scala JAR on serverless or classic compute, configured with main class, parameters, and serverless environment.
tags:
  - databricks
  - workflows
  - jobs
timestamp: "2026-06-18T14:53:16.091Z"
---

# JAR Task in [Lakeflow Jobs](/concepts/lakeflow-jobs.md)

A **JAR Task** is a job type in [Lakeflow Jobs](/concepts/lakeflow-jobs.md) that runs a packaged Java or Scala application (a `.jar` file) containing Spark code on Serverless Compute. The task executes the application’s main class, taking parameters defined in the job configuration, and uses Spark Connect to interact with the Spark engine running server-side. Databricks recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of building and deploying JARs manually. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Requirements

To build a JAR compatible with serverless compute, the local development environment must have:

- **sbt** 1.11.7 or higher (for Scala JARs) or **Maven** 3.9.0 or higher (for Java JARs).
- JDK, Scala, and [Databricks Connect](/concepts/databricks-connect.md) versions that exactly match the target serverless environment version. For example, serverless environment version 4 requires Scala 2.13, JDK 17, and Databricks Connect 17.3. The JAR must be compiled against the same Scala version (`_2.13` suffix for dependencies) and must use only public Spark APIs. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Limitations

Because serverless compute is built on [Spark Connect](/concepts/spark-connect.md), the JAR runs against a thin client library. The following are **not available**:

- **RDD API** (`org.apache.spark.rdd.*`), `SparkContext`, or `JavaSparkContext`. Use `SparkSession` and DataFrame/Dataset operations instead.
- **Spark internal APIs** (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, etc.). Code importing these will fail with `NoClassDefFoundError`.
- **Native libraries** (`.so`, `.dll`, JNI). Serverless compute does not allow writing native binaries to the filesystem. Libraries that unpack native binaries at startup will fail with `UnsatisfiedLinkError`.

If the workload requires any of these capabilities, it must run on standard or dedicated compute clusters. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Dependency Management

Libraries can be made available to the JAR on serverless compute in three ways:

- **Provided libraries** – Serverless compute includes a set of required dependencies (such as `databricks-connect`, Scala standard library, logging frameworks, Jackson, Google Guava, etc.). These must be declared `provided` in the build; bundling custom versions will trigger `NoSuchMethodError`. The provided library list varies by environment version.
- **Attached environment libraries** – Additional runtime libraries can be attached to the [serverless environment](/concepts/serverless-gpu-environment.md) without including them in the JAR.
- **External database connections** – For JDBC sources, use a JDBC connection (Unity Catalog-managed) instead of bundling a driver. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Building a JAR

The build process differs for Scala and Java projects. For a Scala JAR, typical steps include:

1. Create a project with sbt.
2. Set `scalaVersion` to match the serverless environment (e.g., `2.13.16`), `javacOptions/scalacOptions` with `--release 17`, and add the `databricks-connect` dependency with `% "provided"`.
3. Add the `sbt-assembly` plugin and configure `fork := true` with `--add-opens` JVM arguments.
4. Write a main class that uses `SparkSession.builder().getOrCreate()`.
5. Run `sbt assembly` to produce a fat JAR (e.g., `target/my-spark-app-assembly-0.1.0-SNAPSHOT.jar`). ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Creating a Job with a JAR Task

In the Databricks workspace Jobs UI:

1. Click **Jobs & Pipelines** in the sidebar, then **Create** > **Job**.
2. Click the **JAR** tile to add a JAR task. Set the **Type** to **JAR** if not selected.
3. Enter the fully qualified **Main class** (e.g., `com.examples.SparkJar`).
4. Under **Compute**, choose **Serverless** and configure the [serverless environment](/concepts/serverless-gpu-environment.md):
   - Select an **Environment version** (e.g., 4 or higher) compatible with the JAR.
   - Upload the JAR file or select it from a Unity Catalog volume or workspace location.
5. Provide **Parameters** as a JSON array (e.g., `["Hello", "World!"]`).
6. Click **Create task**. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Running the Job

Click **Run now** to execute the job. The run output appears in the **Output** pane, including the main class’s stdout (e.g., printed arguments and Spark version). The job run details can be viewed by clicking the run link from the trigger pop-up or the job runs list. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Troubleshooting

The source documentation includes a troubleshooting table for common exceptions encountered when running JAR tasks on serverless compute. For the most up-to-date information, refer to the official Databricks documentation. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- Serverless Compute
- [Spark Connect](/concepts/spark-connect.md)
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)
- [Databricks Connect](/concepts/databricks-connect.md)
- [JAR task for jobs](/concepts/jar-task-in-lakeflow-jobs.md) (Databricks documentation)
- Create a Databricks compatible JAR

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
