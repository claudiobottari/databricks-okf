---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b0ee8fc9f797ae3b22dad43c6bb4ba367334040873f2c49cd1baec62179f5e4
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provided-libraries-on-databricks-serverless
    - PLODS
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Provided Libraries on Databricks Serverless
description: The curated set of libraries automatically available on serverless compute (environment version 4), which should not be bundled in JARs
tags:
  - libraries
  - serverless
  - databricks
  - dependencies
timestamp: "2026-06-18T11:21:38.843Z"
---

# Provided Libraries on Databricks Serverless

**Provided Libraries** are a curated set of common Java and Scala libraries that are pre-installed and available by default on Databricks Serverless Compute. When building JARs for serverless jobs, developers must declare these libraries as `provided` in their build configuration rather than bundling them into the JAR file. Including bundled versions of these libraries can cause `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Purpose

Serverless compute environments include Databricks Connect and a curated set of common libraries to reduce JAR size and avoid version conflicts. By declaring these libraries as `provided`, developers ensure that the JAR uses the versions already present in the serverless environment rather than potentially incompatible bundled versions. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Library Versions by Environment Version

The specific versions of provided libraries depend on the serverless environment version in use. The versions listed below apply to **serverless environment version 4**. For other environment versions, consult the serverless environment version notes. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Core Spark and Scala Libraries

| Library | Version |
|---------|---------|
| `com.databricks:databricks-connect_2.13` | 17.3.2 |
| `org.scala-lang:scala-library_2.13` | 2.13.16 |
| `org.scala-lang:scala-reflect_2.13` | 2.13.16 |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Logging Libraries

| Library | Version |
|---------|---------|
| `org.slf4j:slf4j-api` | 2.0.10 |
| `org.apache.logging.log4j:log4j-api` | 2.20.0 |
| `org.apache.logging.log4j:log4j-core` | 2.20.0 |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### HTTP and Networking Libraries

| Library | Version |
|---------|---------|
| `org.apache.httpcomponents:httpclient` | 4.5.14 |
| `org.apache.httpcomponents:httpcore` | 4.4.16 |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### JSON and Serialization Libraries

| Library | Version |
|---------|---------|
| `com.fasterxml.jackson.core:jackson-databind` | 2.15.2 |
| `com.fasterxml.jackson.core:jackson-core` | 2.15.2 |
| `com.fasterxml.jackson.core:jackson-annotations` | 2.15.2 |
| `com.fasterxml.jackson.datatype:jackson-datatype-jsr310` | 2.15.2 |
| `org.json4s:json4s-jackson_2.13` | 4.0.7 |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Commons and Utility Libraries

| Library | Version |
|---------|---------|
| `com.google.guava:guava` | 32.0.1-jre |
| `commons-io:commons-io` | 2.14.0 |
| `org.apache.commons:commons-lang3` | 3.14.0 |
| `org.apache.commons:commons-configuration2` | 2.11.0 |
| `org.apache.commons:commons-text` | 1.12.0 |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Databricks-Specific Libraries

| Library | Version |
|---------|---------|
| `com.databricks:databricks-sdk-java` | 0.52.0 |
| `com.databricks:databricks-dbutils-scala_2.13` | 0.1.4 |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Declaring Libraries as Provided

When building a JAR for serverless compute, declare provided libraries in your build configuration to exclude them from the packaged JAR. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Scala (sbt)

In your `build.sbt` file, use the `% "provided"` classifier:

```scala
libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.2" % "provided"
```

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Java (Maven)

In your `pom.xml`, use the `<scope>provided</scope>` element:

```xml
<dependency>
    <groupId>com.databricks</groupId>
    <artifactId>databricks-connect_2.13</artifactId>
    <version>17.3.2</version>
    <scope>provided</scope>
</dependency>
```

## Managing Non-Provided Dependencies

For libraries not included in the provided set, developers have two options: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **Bundle in the JAR**: Include the dependency in the assembled JAR file.
- **Attach as an environment library**: Add the library to the [serverless environment](/concepts/serverless-gpu-environment.md) configuration. This is useful for runtime-only libraries that should not be bundled.

For JDBC sources, Databricks recommends using a JDBC connection managed by Unity Catalog instead of including a JDBC driver in the JAR. This approach handles credentials, lineage, and governance automatically. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Best Practices

- **Always declare provided libraries as `provided`** in your build configuration. Bundling your own versions can cause `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Match dependency versions exactly** to the serverless environment version you are targeting. Incompatible versions can cause runtime failures. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Use [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)** instead of building and deploying JARs manually. Bundles make it easy to create a project from a template with the correct Scala, JDK, and Databricks Connect versions already configured for serverless. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Serverless Compute — The execution environment for serverless jobs
- Serverless Environment Version — Version-specific library availability
- JAR Tasks — Running JARs as tasks in [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- [Databricks Connect](/concepts/databricks-connect.md) — The Spark API surface for serverless compute
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — Recommended alternative to manual JAR building
- JDBC Connections — Unity Catalog-managed database connections

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
