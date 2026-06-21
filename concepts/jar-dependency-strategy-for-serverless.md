---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea9a07cc0e8cd65093a97d827b1299430b9b6651a34857597005e7e1937009a2
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - jar-dependency-strategy-for-serverless
    - JDSFS
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: JAR Dependency Strategy for Serverless
description: "Three approaches to manage library dependencies for JARs on serverless compute: provided libraries, environment libraries, and JDBC connections"
tags:
  - dependencies
  - serverless
  - databricks
  - jars
timestamp: "2026-06-18T11:22:56.818Z"
---

# JAR Dependency Strategy for Serverless

**JAR Dependency Strategy for Serverless** describes how to manage and package Java and Scala dependencies so that a JAR file runs correctly on [serverless compute](/concepts/serverless-gpu-compute.md) in a Databricks Lakeflow Job. Because serverless compute uses a thin Spark Connect client and a fixed runtime environment, dependencies must be handled carefully to avoid runtime failures.

## Overview

Serverless compute runs against a Spark Connect thin client library that exposes the public Spark API, while the Spark engine runs server-side. Your JAR's dependencies must be compatible with this architecture. The key principles are: include every dependency your code needs, but do not bundle dependencies that are already provided by the serverless environment. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Dependency Management Options

To make a library available to your JAR on serverless compute, use one of the following approaches: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **Declare as `provided`**: Serverless compute includes Databricks Connect and a curated set of common libraries. If your library's version matches what the environment provides, declare it `provided` in your build tool and do not include it in your JAR.
- **Attach as an environment library**: Add a library to your [serverless environment](/concepts/serverless-gpu-environment.md) if it isn't already provided. This works well for runtime-only libraries you do not want to bundle.
- **Connect to an external database**: For JDBC sources, use a JDBC connection instead of including a driver. JDBC connections are Unity Catalog-managed — credentials, lineage, and governance are handled for you.

## Provided Libraries

The following libraries are available by default on serverless compute and must be declared `provided` in your build. Bundling your own versions of these libraries triggers a `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

The versions listed below are for **serverless environment version 4**. For other environment versions, see the [serverless environment version notes](/concepts/serverless-environment-versioning.md). ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

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

## Version Compatibility

To run on serverless compute without failures, your JAR's Scala and JDK versions must exactly match the runtime Scala and JDK versions. The example using serverless environment version 4 requires: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- Compiled against Scala 2.13; every dependency uses the `_2.13` suffix.
- Compiled against JDK 17, class file version 61.
- Compiled against Databricks Connect 17.3, the Spark API surface for serverless compute.

## Build Configuration Examples

### Scala (sbt)

When using sbt, configure your `build.sbt` with the correct version constraints: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

```scala
name := "my-spark-app"

scalaVersion := "2.13.16"
javacOptions ++= Seq("--release", "17")
scalacOptions ++= Seq("-release", "17")

libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.2" % "provided"

fork := true
javaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"
```

Use the `%%` notation with sbt so it picks the `_2.13` artifact for Scala libraries. The sbt-assembly plugin (`com.eed3si9n` % `sbt-assembly` % `2.3.1`) is recommended for building fat JARs. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Java (Maven)

For Java JARs, use Maven 3.9.0 or higher. Configure your compiler to target JDK 17 and ensure your dependencies are compatible with the serverless environment. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Limitations

Serverless compute imposes specific limitations on what code and dependencies your JAR can use: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **RDD API not available**: `org.apache.spark.rdd.*`, `SparkContext`, and `JavaSparkContext` are not supported. Use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead.
- **Spark internal APIs not available**: Packages like `org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, and `org.apache.spark.sql.internal.*` are unavailable. Importing them causes `NoClassDefFoundError`.
- **Native libraries not supported**: Serverless compute does not permit writing `.so`, `.dll`, or JNI libraries to the file system. Libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`. Init scripts are not a workaround.

If your workload requires any of the above, run it on standard or dedicated compute instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Best Practices

- **Use only public Spark APIs**: Serverless compute uses Spark Connect. Code that bypasses the public API cannot benefit from Catalyst optimization or Photon acceleration, even on classic compute. RDD-based and internals-dependent code is generally slower than the equivalent DataFrame or SQL code. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Check third-party library compatibility**: If a third-party library uses Spark internals, check whether it publishes a Spark Connect-compatible release. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Consider Declarative Automation Bundles**: Databricks strongly recommends [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of building and deploying JARs manually. Bundles make it easy to create a project from a template with the correct Scala, JDK, and Databricks Connect versions already configured for serverless. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Serverless Compute — The execution environment for serverless jobs
- [Spark Connect](/concepts/spark-connect.md) — The thin client protocol used by serverless compute
- [Databricks Connect](/concepts/databricks-connect.md) — The library that provides the Spark API surface for serverless
- JAR Task for Jobs — How to configure a JAR task in a Lakeflow Job
- Serverless Environment Version — Version-specific dependency information
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — Recommended alternative to manual JAR building

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
