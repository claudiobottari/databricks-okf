---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a55ff7875b185d7e577acec89a197ae54644fc8bf0c93711ba5f898125fcafd5
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - creating-and-running-jar-tasks-in-databricks-jobs
    - Running JAR Tasks in Databricks Jobs and Creating
    - CARJTIDJ
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Creating and Running JAR Tasks in Databricks Jobs
description: How to configure a Databricks job to run a JAR as a serverless task, including main class, parameters, and environment setup
tags:
  - databricks
  - jobs
  - workflows
  - jars
timestamp: "2026-06-18T11:21:50.827Z"
---

# Creating and Running JAR Tasks in Databricks Jobs

A **Java archive (JAR)** packages Java or Scala code into a single file. You can build a JAR containing Spark code and deploy it as a JAR task on [serverless compute](/concepts/serverless-gpu-compute.md) in a [Lakeflow Job](/concepts/lakeflow-jobs.md). Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of manually building and deploying JARs, as bundles automatically configure the correct Scala, JDK, and [Databricks Connect](/concepts/databricks-connect.md) versions for serverless and simplify deployment to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Requirements

To build a JAR, your local development environment must have:

- **sbt** 1.11.7 or higher for Scala JARs
- **Maven** 3.9.0 or higher for Java JARs
- JDK, Scala, and Databricks Connect versions that match your target serverless environment version

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Dependency Versions

To run on serverless compute without failures, your JAR's Scala and JDK versions must exactly match the runtime versions provided by the serverless environment. The example in this page uses **serverless environment version 4**, which requires:

- Scala 2.13 (every dependency must use the `_2.13` suffix)
- JDK 17 (class file version 61)
- Databricks Connect 17.3 (the Spark API surface for serverless compute)

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Limitations

Serverless compute uses [Spark Connect](/concepts/spark-connect.md). Your JAR runs against a thin client library that exposes public Spark APIs, while the Spark engine itself runs server-side. The following are **not available** on serverless compute:

- **RDD API** (`org.apache.spark.rdd.*`) and `SparkContext`/`JavaSparkContext`. Use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead.
- **Spark internal APIs** (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, etc.). Code importing these fails with `NoClassDefFoundError`.
- **Native libraries** (`.so`, `.dll`, JNI). Serverless compute does not allow writing native libraries to the file system. Libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`. Init scripts are not a workaround.

If your workload requires any of the above, run it on standard or dedicated compute instead.

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 1: Build a JAR

The following example builds a Scala JAR using sbt.

1. Create a new project:
   ```bash
   sbt new scala/scala-seed.g8
   ```
   Enter a project name, e.g., `my-spark-app`.

2. Remove seed files and create your source directory:
   ```bash
   cd my-spark-app
   rm src/main/scala/example/Hello.scala
   rm src/test/scala/example/HelloSpec.scala
   rm project/Dependencies.scala
   mkdir -p src/main/scala/com/examples
   ```

3. Replace `build.sbt` with the following:
   ```scala
   name := "my-spark-app"

   scalaVersion := "2.13.16"
   javacOptions ++= Seq("--release", "17")
   scalacOptions ++= Seq("-release", "17")

   libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.2" % "provided"

   fork := true
   javaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"
   ```

4. Create or edit `project/plugins.sbt` and add:
   ```scala
   addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.3.1")
   ```

5. Create your main class at `src/main/scala/com/examples/SparkJar.scala`:
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

6. Build the JAR:
   ```bash
   sbt assembly
   ```
   The compiled JAR is created in `target/` as `my-spark-app-assembly-0.1.0-SNAPSHOT.jar`.

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Managing Dependencies

To make a library available to your JAR on serverless compute, use one of these approaches:

- **Provided library**: Serverless compute includes Databricks Connect and a curated set of common libraries. If your version is compatible, declare it `provided` in your build and do not include it in the JAR.
- **Attach as an environment library**: Add a library to your [serverless environment](/concepts/serverless-gpu-environment.md) if it is not already provided.
- **Connect to an external database**: For JDBC sources, use a JDBC connection (Unity Catalog–managed) instead of including a JDBC driver. Credentials, lineage, and governance are handled for you.

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

#### Provided Libraries (Serverless Environment Version 4)

The following libraries are available by default. Declare them `provided` in your build; bundling your own versions triggers `NoSuchMethodError` at runtime.

| GroupId | ArtifactId | Version |
|---------|------------|---------|
| `com.databricks` | `databricks-connect_2.13` | 17.3.2 |
| `org.scala-lang` | `scala-library_2.13` | 2.13.16 |
| `org.scala-lang` | `scala-reflect_2.13` | 2.13.16 |
| `org.slf4j` | `slf4j-api` | 2.0.10 |
| `org.apache.logging.log4j` | `log4j-api` | 2.20.0 |
| `org.apache.logging.log4j` | `log4j-core` | 2.20.0 |
| `org.apache.httpcomponents` | `httpclient` | 4.5.14 |
| `org.apache.httpcomponents` | `httpcore` | 4.4.16 |
| `com.fasterxml.jackson.core` | `jackson-databind` | 2.15.2 |
| `com.fasterxml.jackson.core` | `jackson-core` | 2.15.2 |
| `com.fasterxml.jackson.core` | `jackson-annotations` | 2.15.2 |
| `com.fasterxml.jackson.datatype` | `jackson-datatype-jsr310` | 2.15.2 |
| `com.google.guava` | `guava` | 32.0.1-jre |
| `commons-io` | `commons-io` | 2.14.0 |
| `org.json4s` | `json4s-jackson_2.13` | 4.0.7 |
| `org.apache.commons` | `commons-lang3` | 3.14.0 |
| `org.apache.commons` | `commons-configuration2` | 2.11.0 |
| `org.apache.commons` | `commons-text` | 1.12.0 |
| `com.databricks` | `databricks-sdk-java` | 0.52.0 |
| `com.databricks` | `databricks-dbutils-scala_2.13` | 0.1.4 |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 2: Create a Job to Run the JAR

1. In your workspace, click **Workflows** icon (Jobs & Pipelines) in the sidebar.
2. Click **Create**, then **Job**.
3. Click the **JAR** tile to configure the first task. If the tile is not visible, click **Add another task type** and search for **JAR**.
4. Optionally rename the job.
5. In **Task name**, enter a name (e.g., `JAR_example`).
6. Ensure **Type** is set to **JAR**.
7. For **Main class**, enter the fully qualified class name (e.g., `com.examples.SparkJar`).
8. For **Compute**, select **Serverless**.
9. Configure the serverless environment:
   - Select an environment and click **Edit**.
   - Set **Environment version** to **4** or higher.
   - Add your JAR file by dragging and dropping it or browsing from a Unity Catalog volume or workspace location.
10. For **Parameters**, enter `["Hello", "World!"]`.
11. Click **Create task**.

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 3: Run the Job and View Output

Click **Run Now** to execute the workflow. To view job run details, click **View run** in the **Triggered run** pop-up or click the run's start time link in the job runs view. When the run completes, the output appears in the **Output** pane, including the arguments you passed to the task. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Troubleshooting

Common exceptions when running JAR tasks on serverless compute include:

| Exception | Likely Cause | Resolution |
|-----------|--------------|------------|
| `NoClassDefFoundError` | Code uses Spark internal APIs (e.g., `catalyst.*`, `util.*`, `sql.internal.*`) | Refactor to use public Spark API (DataFrame/Dataset). |
| `UnsatisfiedLinkError` | A library unpacks native binaries (`.so`, `.dll`) at startup | Use a Java equivalent if available, or switch to standard/dedicated compute. |
| `NoSuchMethodError` | Bundled version of a provided library conflicts with the serverless runtime | Declare provided libraries as `provided` in your build. |

If your workload requires RDD APIs, Spark internals, or native libraries, run it on standard or dedicated compute instead of serverless. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Serverless compute](/concepts/serverless-gpu-compute.md) – The compute type used for JAR tasks in this guide
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – The job orchestration service
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) – Recommended alternative for deploying JARs
- [Databricks Connect](/concepts/databricks-connect.md) – The Spark API surface for serverless
- [Spark Connect](/concepts/spark-connect.md) – The underlying protocol for serverless compute
- Photon – Acceleration technology (unavailable for internal API code)
- JAR task – The task type for running custom Java/Scala code

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
