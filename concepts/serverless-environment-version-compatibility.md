---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ae998741e341c9ecdae7bb4d9793b3dd78b72953cce332d9f5ffb842ac071aa
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-environment-version-compatibility
    - SEVC
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Serverless Environment Version Compatibility
description: JARs must match the serverless runtime's exact Scala, JDK, and Databricks Connect versions to avoid runtime failures
tags:
  - versioning
  - compatibility
  - serverless
  - databricks
timestamp: "2026-06-18T11:21:31.299Z"
---

# Serverless Environment Version Compatibility

**Serverless Environment Version Compatibility** refers to the required alignment between the versions of Scala, Java Development Kit (JDK), and Databricks Connect used in your local development environment and the versions supported by a specific [serverless compute](/concepts/serverless-gpu-compute.md) environment version in Databricks. When building and deploying JAR tasks to serverless compute, the dependency versions in your compiled JAR must exactly match the runtime versions available in the target serverless environment to avoid runtime failures. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Version Requirements

To run a JAR task on serverless compute without errors, your JAR must be compiled against the same versions of Scala, JDK, and Databricks Connect that are present in the serverless environment version you are targeting. For example, the documentation for serverless environment version 4 specifies an exact set of dependency versions. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Because the serverless environment provides certain libraries as runtime dependencies, you must not bundle your own versions of these libraries in your JAR. Declare them as `provided` in your build tool. Bundling your own copies triggers a `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

The list of installed libraries and their versions varies by serverless environment version. For the current list for your target version, see the [serverless environment version notes](/concepts/serverless-environment-versioning.md) reference. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Provided Libraries (Environment Version 4 Example)

For serverless environment version 4, the following libraries are provided by the runtime and must be declared `provided` in your build — you must **not** bundle them in your JAR: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

| Group ID | Artifact ID | Version |
|---|---|---|
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

## Development Environment Setup

Your local development environment must have the following tools installed at versions compatible with your target serverless environment: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **sbt** 1.11.7 or higher (for Scala JARs)
- **Maven** 3.9.0 or higher (for Java JARs)
- **JDK**, **Scala**, and **Databricks Connect** versions that match your target serverless environment version

For example, to target serverless environment version 4 using Scala, your `build.sbt` would specify: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

```scala
scalaVersion := "2.13.16"
javacOptions ++= Seq("--release", "17")
scalacOptions ++= Seq("-release", "17")
libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.2" % "provided"
```

## Choosing a Serverless Environment Version

When configuring a [serverless compute](/concepts/serverless-gpu-compute.md) environment for a JAR task, you select the environment version. For the example described in the documentation for building and running JARs, version **4** or higher is used. The environment version determines which library versions are available and the Scala/JDK compatibility requirements. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Best Practices

- **Match versions exactly.** The runtime Scala and JDK versions in your compiled JAR must exactly match the versions installed in the serverless environment. Any deviation can cause failures. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Declare provided libraries as `provided`.** Do not bundle any libraries that are already supplied by the serverless environment. Use the `% "provided"` scope in sbt or the equivalent `<scope>provided</scope>` in Maven. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Use [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) when possible.** Databricks recommends using Declarative Automation Bundles instead of manually building and deploying JARs. Bundles make it easy to create a project from a template that has the correct Scala, JDK, and Databricks Connect versions already configured for serverless, and enable simple deployment of the JAR to the Databricks workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Serverless Compute — The execution environment for serverless jobs
- JAR Tasks — How to configure and run JAR-based tasks in [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- [Databricks Connect](/concepts/databricks-connect.md) — The client library exposing Spark APIs for serverless compute
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — The recommended approach for building and deploying JARs
- [Spark Connect](/concepts/spark-connect.md) — The underlying architecture used by serverless compute
- [Spark API Compatibility](/concepts/apache-spark-compatibility.md) — Limitations when using serverless compute

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
