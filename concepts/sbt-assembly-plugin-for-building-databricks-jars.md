---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a7dfe953e219be4c606f86aa129e38c74dc8119b9278588a24062e7faf02515
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sbt-assembly-plugin-for-building-databricks-jars
    - SPFBDJ
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: sbt-assembly Plugin for Building Databricks JARs
description: Using sbt-assembly (version 2.3.1) to build a fat JAR for Databricks serverless compute; configured via project/plugins.sbt and built with sbt commands.
tags:
  - scala
  - build-tools
  - databricks
timestamp: "2026-06-19T14:36:12.134Z"
---

---

title: sbt-assembly Plugin for Building Databricks JARs
summary: Using the sbt-assembly plugin to create a fat JAR for serverless compute jobs on Databricks.
sources:
  - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T19:00:00.000Z"
updatedAt: "2026-06-18T19:00:00.000Z"
tags:
  - databricks
  - scala
  - sbt
  - JAR
  - serverless
aliases:
  - sbt-assembly-databricks
  - SABDJ
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0

---

# sbt-assembly Plugin for Building Databricks JARs

The **sbt-assembly Plugin** is an sbt plugin that creates a fat JAR (also called an uber JAR) by bundling your project's code together with all of its dependencies into a single archive. When building JARs for Databricks serverless compute, sbt-assembly is the recommended tool for Scala projects that must include every dependency in the JAR (unless a library is already provided by the serverless environment). ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Overview

Serverless compute on Databricks requires that your JAR include all the libraries it needs, except for a curated set of provided libraries (such as Databricks Connect, Scala standard library, and common utilities). Using sbt-assembly lets you produce a single deployable artifact that contains both your code and its dependencies, avoiding `NoClassDefFoundError` or `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Configuration

To use sbt-assembly in your project, add the plugin to `project/plugins.sbt`:

```scala
addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.3.1")
```

Then, in your `build.sbt`, declare your dependencies. Libraries that are already provided by the serverless environment (such as `databricks-connect`) should be marked `% "provided"` so that sbt-assembly excludes them from the resulting JAR. Other dependencies should be declared normally and will be included in the fat JAR. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Example `build.sbt` snippet:

```scala
name := "my-spark-app"
scalaVersion := "2.13.16"
javacOptions ++= Seq("--release", "17")
scalacOptions ++= Seq("-release", "17")

libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.2" % "provided"
// Other dependencies (will be included in the fat JAR)
libraryDependencies += "org.example" %% "my-library" % "1.0.0"

fork := true
javaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"
```

## Building

Run the `assembly` task from the command line:

```bash
sbt assembly
```

This command compiles your code, resolves all non-provided dependencies, and merges them into a single fat JAR file. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Resulting JAR

After a successful build, the fat JAR is placed in the `target/` folder with a name based on your project name and version. For the example project `my-spark-app` with version `0.1.0-SNAPSHOT`, the output file is:

```
target/scala-2.13/my-spark-app-assembly-0.1.0-SNAPSHOT.jar
```

You then upload this JAR to your Databricks workspace and attach it to a serverless environment as a library when configuring a JAR task. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Best Practices

- **Match dependency versions exactly.** Serverless compute runs a specific environment version (e.g., environment version 4 uses Scala 2.13.16 and JDK 17). Ensure your project's `scalaVersion`, `javacOptions`, and Databricks Connect version align with the target environment. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Mark provided libraries correctly.** Declare libraries that are already available on serverless compute (such as `databricks-connect`, `scala-library`, `slf4j-api`, etc.) as `% "provided"` to prevent duplication and conflicts. The list of provided libraries changes with each environment version. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Use only public Spark APIs.** Serverless compute uses Spark Connect, so code that imports internal Spark APIs (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, etc.) will fail at runtime. Ensure your code and all included dependencies rely only on the public Spark API. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Exclude native libraries.** Serverless compute does not support native libraries or JNI. If a dependency unpacks `.so` or `.dll` files, it will cause `UnsatisfiedLinkError`. Prefer pure-Java equivalents. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) – The recommended alternative to manually building and deploying JARs.
- JAR tasks on Databricks – How to run a JAR as a job task.
- Serverless compute environment versions – The runtime environment that determines Scala, JDK, and library versions.
- [Databricks Connect](/concepts/databricks-connect.md) – The Spark API surface used by serverless compute.
- Scala JAR projects on Databricks – General guidance for Scala JAR development.

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
