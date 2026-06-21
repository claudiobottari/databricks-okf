---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 176695a1b80574fa761dd489050856b66d0cd5d71830cdb395596b0567916994
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - building-scala-jars-with-sbt-assembly-for-serverless
    - BSJWSFS
    - Scala JARs on Serverless
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Building Scala JARs with sbt-assembly for Serverless
description: Step-by-step process to build a serverless-compatible Scala JAR using sbt and sbt-assembly plugin
tags:
  - scala
  - sbt
  - build
  - jars
timestamp: "2026-06-18T11:21:20.244Z"
---

---
title: Building Scala JARs with sbt-assembly for Serverless
summary: A guide to building and deploying Scala JARs using sbt-assembly for Databricks serverless compute, including dependency management, environment version matching, and limitations.
sources:
  - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:00:00.000Z"
tags:
  - databricks
  - scala
  - jar
  - serverless
  - sbt-assembly
aliases:
  - building-scala-jars-with-sbt-assembly-for-serverless
  - serverless-scala-jar-build
confidence: 0.98
provenanceState: extracted
---

# Building Scala JARs with sbt-assembly for Serverless

**Building Scala JARs with sbt-assembly for Serverless** describes the process of creating a fat JAR (also known as an assembly JAR) using the [sbt-assembly](https://github.com/sbt/sbt-assembly) plugin and deploying it as a [ Lakeflow Job](/concepts/lakeflow-jobs.md) task on [serverless compute](/concepts/serverless-gpu-compute.md) in Databricks. This page focuses on Scala projects; for Java projects, use Maven instead.

## Overview

A Java archive (JAR) packages Java or Scala code into a single file. To run Spark code as a JAR task on serverless compute, you must build a JAR that is compatible with the serverless environment – matching Scala, JDK, and Databricks Connect versions exactly, and using only public Spark APIs. Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of manual builds, as bundles automatically configure the correct versions and simplify deployment.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Requirements

To build a Scala JAR for serverless, your local development environment must have:

- [sbt](https://www.scala-sbt.org/download/) 1.11.7 or higher
- JDK version matching the serverless environment (see #Dependency versions)
- Scala version matching the serverless environment
- [sbt-assembly](https://github.com/sbt/sbt-assembly) plugin (version 2.3.1 or later)

Additionally, the JAR must:

- Be compiled against Scala 2.13 (every dependency should use the `_2.13` suffix)
- Be compiled against JDK 17 (class file version 61)
- Be compiled against Databricks Connect 17.3 (for serverless environment version 4)
- Use only public Spark APIs – no RDDs, no Spark internals
- Include all dependencies either in the JAR (via sbt-assembly) or attached as a [serverless environment library](/concepts/serverless-gpu-environment.md)^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Dependency versions

The Scala, JDK, and Databricks Connect versions in your JAR must exactly match the runtime versions on serverless compute. The example in the source material uses **serverless environment version 4**, which requires:

- Scala 2.13.16
- JDK 17
- Databricks Connect 17.3.2

If you use a different environment version, consult the [serverless environment version notes](/concepts/serverless-environment-versioning.md) for the correct dependency versions.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Limitations

Serverless compute runs on [Spark Connect](/concepts/spark-connect.md). Your JAR runs against a thin client library that exposes only the public Spark APIs; the Spark engine itself runs server-side. Code that bypasses the public API cannot benefit from Catalyst optimization or Photon acceleration. The following are **not available** on serverless compute:^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **RDD API** (`org.apache.spark.rdd.*`) – use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead.
- **Spark internal APIs** (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) – code that imports these will fail with `NoClassDefFoundError`. Refactor to the public Spark API.
- **Native libraries** (`.so`, `.dll`, JNI) – serverless compute does not permit writing native libraries to the file system. Libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`. Init scripts are not a workaround.

If your workload requires any of the above, run it on standard or dedicated compute instead.

## Step 1: Build the JAR with sbt-assembly

1. Create a Scala project using the seed template:
   ```bash
   sbt new scala/scala-seed.g8
   ```
   When prompted, enter a project name (e.g., `my-spark-app`).

2. Delete the seed's stub files and create the source directory:
   ```bash
   cd my-spark-app
   rm src/main/scala/example/Hello.scala
   rm src/test/scala/example/HelloSpec.scala
   rm project/Dependencies.scala
   mkdir -p src/main/scala/com/examples
   ```

3. Replace the contents of `build.sbt` with the following:
   ```scala
   name := "my-spark-app"

   scalaVersion := "2.13.16"
   javacOptions ++= Seq("--release", "17")
   scalacOptions ++= Seq("-release", "17")

   libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.2" % "provided"

   // Your other dependencies go here. Use %% for Scala libraries so sbt picks the _2.13 artifact.

   fork := true
   javaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"
   ```

4. Edit or create `project/plugins.sbt` and add the sbt-assembly plugin:
   ```scala
   addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.3.1")
   ```

5. Create your main class in `src/main/scala/com/examples/SparkJar.scala`:
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
   The compiled JAR appears in the `target/` folder as `my-spark-app-assembly-0.1.0-SNAPSHOT.jar`.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing dependencies

To make a library available to your JAR on serverless compute, you have three options:^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **Use a provided library**: Serverless compute includes Databricks Connect and a curated set of common libraries. Declare them as `provided` in your build and do not bundle them. The list of provided libraries for environment version 4 includes `com.databricks:databricks-connect_2.13`, `org.scala-lang:scala-library_2.13`, `org.slf4j:slf4j-api`, `com.fasterxml.jackson.core:jackson-databind`, and many others. Bundling your own versions will cause `NoSuchMethodError` at runtime.
- **Attach as an environment library**: Add a library to your [serverless environment](/concepts/serverless-gpu-environment.md) if it is not already provided.
- **Connect to an external database**: For JDBC sources, use a JDBC connection instead of including a driver. JDBC connections are Unity Catalog-managed, handling credentials, lineage, and governance.

## Step 2: Create a job to run the JAR

1. In your Databricks workspace, go to **Jobs & Pipelines** and click **Create** > **Job**.
2. Click the **JAR** tile to configure the first task (if not visible, click **Add another task type** and search for **JAR**).
3. Set **Task name** (e.g., `JAR_example`), **Type** to **JAR**, and **Main class** to the fully qualified class name (e.g., `com.examples.SparkJar`).
4. For **Compute**, select **Serverless**.
5. Configure the serverless environment:
   - Click **Edit** and select environment version **4** or higher.
   - Add your assembly JAR by dragging and dropping it, or browse to a Unity Catalog volume or workspace location.
6. For **Parameters**, enter `["Hello", "World!"]` (JSON array of strings).
7. Click **Create task**.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 3: Run the job and view output

Click **Run Now** to execute the job. View run details by clicking **View run** in the pop‑up or by clicking the start time link in the job runs list. When the run completes, the **Output** pane shows the arguments and Spark version, confirming the JAR executed successfully on serverless compute.

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `NoClassDefFoundError` | Bundled versions of provided libraries conflict with serverless runtime | Declare those dependencies as `provided` and rebuild |
| `NoSuchMethodError` | Scala or JDK version mismatch | Match exact versions of Scala, JDK, and Databricks Connect as per the environment version |
| `UnsatisfiedLinkError` | Native library used (`.so`, `.dll`) | Remove native dependencies or switch to a Java equivalent |
| `NoClassDefFoundError` for Spark internal API | Code imports `org.apache.spark.catalyst.*` etc. | Refactor to use public DataFrame/Dataset API |

For further details, see [JAR task for jobs](https://docs.databricks.com/aws/en/jobs/jar) and [Create a Databricks compatible JAR](https://docs.databricks.com/aws/en/jobs/jar-create).

## Related Concepts

- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) – Recommended alternative to manual JAR builds
- [Databricks Connect](/concepts/databricks-connect.md) – The client library used for serverless Spark access
- [Serverless compute](/concepts/serverless-gpu-compute.md) – Compute type for JAR tasks
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – Job orchestration platform
- sbt-assembly – The plugin used to create fat JARs
- Photon – Accelerated engine not available for non-DataFrame APIs
- [Unity Catalog](/concepts/unity-catalog.md) – Governance for JDBC connections and volumes

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
