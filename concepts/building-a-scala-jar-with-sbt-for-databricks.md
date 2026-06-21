---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f343b898ba705a84aaf7fe9b71d2eb71ef1f59bda40f23c52d6e04c412b8b5a
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - building-a-scala-jar-with-sbt-for-databricks
    - BASJWSFD
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Building a Scala JAR with sbt for Databricks
description: Step-by-step process to create a Scala project with sbt, configure build.sbt with correct versions, add sbt-assembly plugin, and produce a fat JAR for Databricks serverless compute.
tags:
  - databricks
  - scala
  - build-tools
  - sbt
timestamp: "2026-06-18T14:53:49.168Z"
---

# Building a Scala JAR with sbt for Databricks

**Building a Scala JAR with sbt for Databricks** refers to the process of compiling Scala code into a Java Archive (JAR) file and deploying it as a task on [serverless compute](/concepts/serverless-gpu-compute.md) in a [Lakeflow Job](/concepts/lakeflow-jobs.md). A JAR packages Java or Scala code and its dependencies into a single file that can be executed by the Databricks runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of building and deploying JARs manually, as bundles provide templates with correct Scala, JDK, and Databricks Connect versions pre-configured for serverless compute and simplify deployment to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Requirements

Your local development environment must have the following installed to build a JAR:

- [sbt](https://www.scala-sbt.org/download/) 1.11.7 or higher for Scala JARs
- JDK, Scala, and Databricks Connect versions that match the [serverless environment](/concepts/serverless-gpu-environment.md) version you plan to use. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Dependency Versions

To run on serverless compute without failures, your JAR’s Scala and JDK versions must exactly match the runtime versions of the serverless environment. The example in the source uses serverless environment version 4, which requires:

- Scala 2.13 (all dependencies using the `_2.13` suffix)
- JDK 17 (class file version 61)
- Databricks Connect 17.3 (the Spark API surface for serverless compute)

Only public Spark APIs should be used; the JAR must avoid RDDs and Spark internals. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Limitations

Serverless compute relies on [Spark Connect](/concepts/spark-connect.md). Code that bypasses public Spark APIs cannot benefit from Catalyst optimization or Photon acceleration. The following are unavailable:

- RDD API (`org.apache.spark.rdd.*`) and `SparkContext`/`JavaSparkContext`. Use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead.
- Spark internal APIs (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`). Code that imports these fails with `NoClassDefFoundError`.
- Native libraries (`.so`, `.dll`, JNI). Serverless compute does not permit writing native binaries to the filesystem; libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`.

If your workload requires any of the above, run it on standard or dedicated compute instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 1: Build a JAR with sbt

1. Create a Scala project using the seed template:
   ```
   sbt new scala/scala-seed.g8
   ```
   When prompted, enter a project name (e.g., `my-spark-app`).

2. Delete the seed’s stub files and create the source directory:
   ```
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

   fork := true
   javaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"
   ```

4. Create (or edit) `project/plugins.sbt` and add:
   ```scala
   addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.3.1")
   ```

5. Create your main class `src/main/scala/com/examples/SparkJar.scala`:
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

6. Build the JAR by running `sbt assembly`. The compiled JAR is created in `target/` as `my-spark-app-assembly-0.1.0-SNAPSHOT.jar`. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing Dependencies

To make a library available to your JAR on serverless compute, use one of the following approaches:

- **Use a provided library**: Declare libraries already available on serverless compute as `provided` in your build (see list below).
- **Attach as an environment library**: Add a library to your serverless environment if it is not already provided. Use this for runtime-only libraries you do not want to bundle.
- **Connect to an external database**: Use a JDBC connection instead of including a JDBC driver in your JAR. JDBC connections are Unity Catalog-managed and handle credentials, lineage, and governance. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Provided Libraries (Serverless Environment Version 4)

The following libraries are required dependencies and are available by default. Bundling your own versions causes `NoSuchMethodError` at runtime.

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
- `com.databricks:databricks-dbutils-scala_2.13`, version 0.1.4 ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 2: Create a Job to Run the JAR

1. In your workspace, click **Jobs & Pipelines** in the sidebar.
2. Click **Create** → **Job**.
3. Click the **JAR** tile to configure the first task. If not available, click **Add another task type** and search for JAR.
4. (Optional) Rename the job.
5. Enter a task name (e.g., `JAR_example`).
6. For **Main class**, enter the package and class of your JAR (e.g., `com.examples.SparkJar`).
7. For **Compute**, select **Serverless**.
8. Configure the serverless environment:
   - Select an environment, then click **Edit**.
   - Select **4** or higher for **Environment version**.
   - Add your JAR file by dragging and dropping, or browse to select from a Unity Catalog volume or workspace location.
9. For **Parameters**, enter `["Hello", "World!"]` for the example.
10. Click **Create task**. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 3: Run the Job and View Output

Click **Run Now** to start the workflow. To view run details, click **View run** in the pop-up or the link in the **Start time** column in the job runs view. When the run completes, the output (including arguments passed to the task) appears in the **Output** pane. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Troubleshooting

The source provides a table for common exceptions (not reproduced here). Refer to the Databricks documentation for troubleshooting information. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Next Steps

- Learn more about JAR task for jobs.
- Learn about Create a Databricks compatible JAR.
- Explore [Lakeflow Jobs](/concepts/lakeflow-jobs.md) for creating and running jobs. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- sbt
- Scala
- JDK
- [Databricks Connect](/concepts/databricks-connect.md)
- [Serverless compute](/concepts/serverless-gpu-compute.md)
- [Spark Connect](/concepts/spark-connect.md)
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)
- Photon

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
