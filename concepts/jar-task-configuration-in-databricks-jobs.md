---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9dd82d3f1854fb7a2273b3cd9cd493b03dd77cb4292a65589d50bf05cf3213d6
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - jar-task-configuration-in-databricks-jobs
    - JTCIDJ
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: JAR Task Configuration in Databricks Jobs
description: "Step-by-step process for creating a Databricks job that runs a JAR on serverless compute: setting main class, selecting compute type, configuring serverless environment version, attaching JAR file, and passing parameters."
tags:
  - databricks
  - jobs
  - configuration
timestamp: "2026-06-19T14:35:57.730Z"
---

# JAR Task Configuration in Databricks Jobs

A **JAR task** runs a compiled Java archive (JAR) – packaged from Java or Scala code with Spark logic – as a step in a Databricks [Lakeflow Jobs](/concepts/lakeflow-jobs.md) workflow. JAR tasks are supported on Serverless Compute, where the JAR executes against a thin Spark Connect client while the engine runs server-side. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

> Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of manually building and deploying JARs. Bundles simplify project creation, ensure correct dependency versions, and enable one‑click deployment to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Requirements

Your local development environment must have:

- **sbt** 1.11.7 or higher (for Scala JARs) or **Maven** 3.9.0 or higher (for Java JARs)
- JDK, Scala, and [Databricks Connect](/concepts/databricks-connect.md) versions that exactly match the target [serverless environment](/concepts/serverless-gpu-environment.md) version (see [Dependency versions](#dependency-versions))

To run on serverless compute without failures, the JAR’s Scala and JDK versions must exactly match the runtime versions. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Dependency versions

The example on the source page uses **serverless environment version 4**. For that version the JAR must be:

- Compiled against **Scala 2.13** (all dependencies use the `_2.13` suffix)
- Compiled against **JDK 17** (class file version 61)
- Compiled against **Databricks Connect 17.3** (the Spark API surface for serverless compute)
- Using only public Spark APIs; no RDDs or Spark internals
- Including every dependency in the JAR or attached as a serverless environment library

For other environment versions, see the [serverless environment version notes](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/). ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Limitations

Serverless compute uses Spark Connect. Code that bypasses the public API cannot benefit from Catalyst optimization or Photon acceleration. The following are **not available**:

- **RDD API** (`org.apache.spark.rdd.*`) and `SparkContext`/`JavaSparkContext` – use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead.
- **Spark internal APIs** (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) – importing these causes `NoClassDefFoundError`.
- **Native libraries** (`.so`, `.dll`, JNI) – serverless compute does not permit writing native libraries to the filesystem. Libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`.

If your workload requires any of the above, run it on standard or dedicated compute instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 1: Build a JAR

The source provides a Scala example. To create a compatible JAR:

1. Generate a project with `sbt new scala/scala-seed.g8`.
2. Delete seed stubs and create `src/main/scala/com/examples/SparkJar.scala`.
3. Configure `build.sbt` with the correct versions:

```scala
name := "my-spark-app"
scalaVersion := "2.13.16"
javacOptions ++= Seq("--release", "17")
scalacOptions ++= Seq("-release", "17")
libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.2" % "provided"
// Other dependencies go here – use %% for Scala libraries
fork := true
javaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"
```

4. Add `sbt-assembly` plugin (`project/plugins.sbt`):

```scala
addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.3.1")
```

5. Write the main class:

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

6. Run `sbt assembly`. The compiled JAR is created in `target/` as `my-spark-app-assembly-0.1.0-SNAPSHOT.jar`. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing dependencies

To make a library available to your JAR on serverless compute, use one of these methods:

- **Provided library**: Serverless compute includes Databricks Connect and a curated set of common libraries (see list below). If your version matches, declare it `provided` in your build and do **not** bundle it.
- **Environment library**: Attach a library to the [serverless environment](/concepts/serverless-gpu-environment.md) if it is not already provided.
- **JDBC connection**: For JDBC sources, use a JDBC connection managed by Unity Catalog instead of bundling a driver. Credentials, lineage, and governance are handled automatically. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Provided libraries (serverless environment version 4)

The following libraries are available by default and must be declared `provided`. Bundling your own versions triggers `NoSuchMethodError` at runtime.

- `com.databricks:databricks-connect_2.13` 17.3.2
- `org.scala-lang:scala-library_2.13` 2.13.16
- `org.scala-lang:scala-reflect_2.13` 2.13.16
- `org.slf4j:slf4j-api` 2.0.10
- `org.apache.logging.log4j:log4j-api` 2.20.0
- `org.apache.logging.log4j:log4j-core` 2.20.0
- `org.apache.httpcomponents:httpclient` 4.5.14
- `org.apache.httpcomponents:httpcore` 4.4.16
- `com.fasterxml.jackson.core:jackson-databind` 2.15.2
- `com.fasterxml.jackson.core:jackson-core` 2.15.2
- `com.fasterxml.jackson.core:jackson-annotations` 2.15.2
- `com.fasterxml.jackson.datatype:jackson-datatype-jsr310` 2.15.2
- `com.google.guava:guava` 32.0.1-jre
- `commons-io:commons-io` 2.14.0
- `org.json4s:json4s-jackson_2.13` 4.0.7
- `org.apache.commons:commons-lang3` 3.14.0
- `org.apache.commons:commons-configuration2` 2.11.0
- `org.apache.commons:commons-text` 1.12.0
- `com.databricks:databricks-sdk-java` 0.52.0
- `com.databricks:databricks-dbutils-scala_2.13` 0.1.4

For other environment versions, see the [serverless environment version notes](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/). ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 2: Create the job to run the JAR

1. In your workspace, click **Jobs & Pipelines** in the sidebar.
2. Click **Create** → **Job**.
3. Click the **JAR** tile (or click **Add another task type** and search for **JAR**).
4. Optionally rename the job.
5. Enter a **Task name** (e.g., `JAR_example`).
6. Ensure **Type** is set to **JAR**.
7. For **Main class**, enter the fully qualified class name (e.g., `com.examples.SparkJar`).
8. For **Compute**, select **Serverless**.
9. Configure the serverless environment:
   - Select an environment version (4 or higher for this example).
   - Click the pencil icon to edit.
   - Add your JAR file by dragging and dropping or browsing to a Unity Catalog volume or workspace location.
10. For **Parameters**, enter a JSON array of strings (e.g., `["Hello", "World!"]`).
11. Click **Create task**. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 3: Run the job and view output

Click **Run Now** to start the workflow. Once the run completes, the output appears in the **Output** pane, including the arguments passed to the task. To view detailed run information, click **View run** in the triggered run pop-up. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Troubleshooting

The source document includes a table of common exceptions (not reproduced here). Consult the [original troubleshooting section](https://docs.databricks.com/aws/en/jobs/how-to/use-jars-in-workflows#troubleshooting) for solutions to `NoClassDefFoundError`, `UnsatisfiedLinkError`, and other issues. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related concepts

- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) – recommended alternative for building and deploying JARs
- Serverless Compute – execution environment for JAR tasks
- [Databricks Connect](/concepts/databricks-connect.md) – client library used to interact with serverless Spark
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – workflow orchestration platform for Databricks
- JDBC Connection – managed connection for external databases
- [Unity Catalog](/concepts/unity-catalog.md) – governance and metadata layer (used for JDBC connections and volume storage)

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
