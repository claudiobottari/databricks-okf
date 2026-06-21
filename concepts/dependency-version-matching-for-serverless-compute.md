---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8ca3f538ff10edbb76e3bb5e6d01effb947e7a0937ae005c8a7df4c0ea7ff710
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dependency-version-matching-for-serverless-compute
    - DVMFSC
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Dependency Version Matching for Serverless Compute
description: JAR Scala and JDK versions must exactly match the serverless runtime versions; mismatches cause failures. Example uses Scala 2.13, JDK 17, Databricks Connect 17.3.
tags:
  - databricks
  - dependencies
  - versioning
timestamp: "2026-06-19T14:36:27.829Z"
---

# Dependency Version Matching for Serverless Compute

**Dependency Version Matching for Serverless Compute** refers to the requirement that the Scala, JDK, and Databricks Connect versions used in a JAR (Java archive) must exactly match the corresponding versions provided by the serverless runtime environment. Failure to match these versions causes runtime failures.

## Why Version Matching Matters

Serverless compute on Databricks runs on a predefined runtime environment with specific versions of Scala, the JDK, Databricks Connect, and other core libraries. When a JAR is submitted as a serverless task, the code runs against the serverless environment's versions, not the versions used during compilation. If any version mismatch exists, the JAR may fail with exceptions such as `NoSuchMethodError` or `NoClassDefFoundError`.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Versions That Must Match

The following dependency versions must exactly match the serverless environment:

- **Scala version**: The JAR must be compiled against the exact Scala version used by the serverless runtime. For serverless environment version 4, this is Scala 2.13. Every Scala dependency must use the `_2.13` suffix.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **JDK version**: The JAR must be compiled against the exact JDK version used by the serverless runtime. For serverless environment version 4, this is JDK 17 (class file version 61).^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Databricks Connect version**: The JAR must be compiled against the Databricks Connect version that matches the serverless environment. For serverless environment version 4, this is Databricks Connect 17.3.2.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Provided Libraries

Serverless compute includes a curated set of core libraries that are available by default. These libraries must be declared as `provided` in the build configuration. Bundling your own versions of these libraries results in `NoSuchMethodError` at runtime.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

For serverless environment version 4, the provided libraries include:

| Library | Version |
|---------|---------|
| `com.databricks:databricks-connect_2.13` | 17.3.2 |
| `org.scala-lang:scala-library_2.13` | 2.13.16 |
| `org.scala-lang:scala-reflect_2.13` | 2.13.16 |
| `org.slf4j:slf4j-api` | 2.0.10 |
| `org.apache.logging.log4j:log4j-api` | 2.20.0 |
| `org.apache.logging.log4j:log4j-core` | 2.20.0 |
| `org.apache.httpcomponents:httpclient` | 4.5.14 |
| `org.apache.httpcomponents:httpcore` | 4.4.16 |
| `com.fasterxml.jackson.core:jackson-databind` | 2.15.2 |
| `com.fasterxml.jackson.core:jackson-core` | 2.15.2 |
| `com.fasterxml.jackson.core:jackson-annotations` | 2.15.2 |
| `com.fasterxml.jackson.datatype:jackson-datatype-jsr310` | 2.15.2 |
| `com.google.guava:guava` | 32.0.1-jre |
| `commons-io:commons-io` | 2.14.0 |
| `org.json4s:json4s-jackson_2.13` | 4.0.7 |
| `org.apache.commons:commons-lang3` | 3.14.0 |
| `org.apache.commons:commons-configuration2` | 2.11.0 |
| `org.apache.commons:commons-text` | 1.12.0 |
| `com.databricks:databricks-sdk-java` | 0.52.0 |
| `com.databricks:databricks-dbutils-scala_2.13` | 0.1.4 |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing Dependencies

To make a library available to a JAR on serverless compute, use one of the following approaches:^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **Use a provided library**: If the library is in the provided set and the version is compatible, declare it as `provided` in the build and do not bundle it in the JAR.
- **Attach as an environment library**: Add the library to a [serverless environment](/concepts/serverless-gpu-environment.md) configuration. This is useful for runtime-only libraries that should not be bundled in the JAR.
- **Bundle in the JAR**: Include the library in the JAR using a tool like `sbt-assembly` (for sbt projects) or Maven Shade Plugin (for Maven projects). This is appropriate for libraries not in the provided set.

## Using Declarative Automation Bundles

Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of manually building and deploying JARs. Bundles automatically configure the correct Scala, JDK, and Databricks Connect versions for the target serverless environment, eliminating version matching errors.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Checking Environment Versions

The exact list of provided libraries and their versions depends on the serverless environment version. For the current version's dependency list, see the [serverless environment version notes](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/) reference.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Serverless compute on Databricks](/concepts/serverless-gpu-compute-on-databricks.md)
- [JAR tasks for jobs](/concepts/jar-task-in-lakeflow-jobs.md)
- [Databricks Connect](/concepts/databricks-connect.md)
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)
- [Spark Connect](/concepts/spark-connect.md)

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
