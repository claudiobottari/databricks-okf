---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 990a7e1eb7a8888671afdfd930922260cc6c0375b8bfe7904a437dd3d9cf146e
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - building-jars-with-sbt-for-databricks-serverless
    - BJWSFDS
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Building JARs with sbt for Databricks Serverless
description: Step-by-step process to create a Scala JAR compatible with Databricks serverless using sbt, with sbt-assembly plugin, matching JDK 17, Scala 2.13, and Databricks Connect versions.
tags:
  - sbt
  - jar
  - scala
  - build
timestamp: "2026-06-19T09:36:00.634Z"
---

# Building JARs with sbt for Databricks Serverless

**Building JARs with sbt for Databricks Serverless** refers to the process of compiling a Scala project into a Java archive (JAR) file that is compatible with [serverless compute](/concepts/serverless-gpu-compute.md) in [Lakeflow Jobs](/concepts/lakeflow-jobs.md). Serverless compute requires specific dependency versions and build configuration to avoid runtime failures. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of building and deploying JARs manually. Declarative Automation Bundles provide templates with the correct versions of Scala, JDK, and [Databricks Connect](/concepts/databricks-connect.md) already configured for serverless compute, and enable simple deployment of the JAR to the Databricks workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Requirements

To build a JAR for serverless compute, your local development environment must have sbt 1.11.7 or higher installed. You also need JDK, Scala, and Databricks Connect versions that match your target serverless environment. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Dependency Versions

Your JAR's Scala and JDK versions must exactly match the runtime Scala and JDK versions of the target serverless environment. For serverless environment version 4, this means: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- Scala 2.13 — all dependencies must use the `_2.13` suffix
- JDK 17, class file version 61
- [Databricks Connect](/concepts/databricks-connect.md) 17.3, which is the Spark API surface for serverless compute
- Only public Spark APIs — no RDDs, no Spark internals

## Limitations

Serverless compute uses [Spark Connect](/concepts/spark-connect.md) under the hood. Your JAR runs against a thin client library that exposes only the public Spark APIs, while the Spark engine runs server-side. Code that bypasses the public API cannot benefit from Catalyst optimization or Photon acceleration. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

The following are not available on serverless compute: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- RDD API (`org.apache.spark.rdd.*`) and `SparkContext` / `JavaSparkContext` — use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead
- Spark internal APIs (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) — code that imports these APIs fails with `NoClassDefFoundError`
- Native libraries (`.so`, `.dll`, JNI) — serverless compute does not permit writing native libraries to the file system; Init scripts are not a workaround

If your workload requires any of the above, run it on standard or dedicated compute instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Step 1: Create the sbt Project

1. Run the following command to create a Scala project:

```
sbt new scala/scala-seed.g8
```

When prompted, enter a project name (e.g., `my-spark-app`). ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

2. Delete the seed's stub files and create the source directory:

```
cd my-spark-app
rm src/main/scala/example/Hello.scala
rm src/test/scala/example/HelloSpec.scala
rm project/Dependencies.scala
mkdir -p src/main/scala/com/examples
```

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

3. Replace the contents of your `build.sbt` file with the following:

```scala
name := "my-spark-app"

// Set the dependency versions
scalaVersion := "2.13.16"
javacOptions ++= Seq("--release", "17")
scalacOptions ++= Seq("-release", "17")

libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.2" % "provided"

// Your other dependencies go here. Use %% for Scala libraries so sbt picks the _2.13 artifact.

// Fork a new JVM on run so our javaOptions are applied.
fork := true
javaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"
```

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

4. Edit or create a `project/plugins.sbt` file and add the sbt-assembly plugin:

```scala
addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.3.1")
```

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

5. Create your main class in `src/main/scala/com/examples/SparkJar.scala`:

```scala
package com.examples

import org.apache.spark.sql.SparkSession

object SparkJar {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder().getOrCreate()
    // Prints the arguments to the class, which
    // are job parameters when run as a job:
    println(args.mkString(", "))
    // Shows using spark:
    println(spark.version)
    println(spark.range(10).limit(3).collect().mkString(" "))
  }
}
```

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

6. Build your JAR file:

```
sbt assembly
```

The compiled JAR is created in the `target/` folder as `my-spark-app-assembly-0.1.0-SNAPSHOT.jar`. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing Dependencies

To make a library available to your JAR on serverless compute, you have three options: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **Use a provided library**: Serverless compute includes Databricks Connect and a curated set of common libraries. If your version matches, declare it `provided` in your build and do not include it in your JAR.
- **Attach as an environment library**: Add a library to your serverless environment if it is not already provided. Use this for runtime-only libraries you do not want to include.
- **Connect to an external database**: For JDBC sources, use a JDBC connection instead of including a driver. JDBC connections are Unity Catalog-managed.

### Provided Libraries

The following libraries are available by default on serverless compute (environment version 4). Declare them `provided` in your build. Bundling your own versions triggers a `NoSuchMethodError` at runtime: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

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

## Step 2: Deploy the JAR as a Job Task

After building your JAR, create a Lakeflow Job to run it on serverless compute. In the Databricks workspace, create a new job and configure a JAR task with the following settings: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **Main class**: Enter the package and class (e.g., `com.examples.SparkJar`).
- **Compute**: Select **Serverless**.
- **Environment version**: Select **4** or higher.
- **JAR file**: Drag and drop your JAR into the file selector, or browse to select it from a Unity Catalog volume or workspace location.
- **Parameters**: Enter any command-line arguments your JAR expects (e.g., `["Hello", "World!"]`).

## Related Concepts

- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — Recommended alternative for building and deploying JARs
- [Databricks Connect](/concepts/databricks-connect.md) — Spark API surface for serverless compute
- [Spark Connect](/concepts/spark-connect.md) — Underlying technology for serverless compute
- Serverless Compute — Compute type that runs JAR tasks without managing clusters
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — Workflow platform for running JAR tasks
- JAR Task for Jobs — Detailed reference for JAR task configuration

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
