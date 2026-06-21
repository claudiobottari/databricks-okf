---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7990ea157a92703f58318869062b1896286f1d294954e50a2c435bf7fa04debe
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provided-libraries-on-serverless-compute
    - PLOSC
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Provided Libraries on Serverless Compute
description: A curated set of required libraries (Databricks Connect, Scala libraries, Jackson, Guava, etc.) that are pre-installed on serverless compute and must be declared 'provided' in your build.
tags:
  - serverless
  - libraries
  - dependencies
  - provided
timestamp: "2026-06-19T09:36:03.230Z"
---

Here is the wiki page for "Provided Libraries on Serverless Compute".

---

## Provided Libraries on Serverless Compute

When building and deploying JAR tasks on Serverless Compute in [Databricks on AWS](/concepts/databricks-on-aws.md), the runtime environment includes a curated set of pre-installed libraries. These are known as "provided libraries" and are available by default, meaning you do not need to bundle them within your JAR file. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### How to Use Provided Libraries

To avoid conflicts and errors at runtime, you must declare these libraries as `provided` in your build configuration (e.g., in your `build.sbt`). If you bundle your own versions of these libraries inside your JAR, it will trigger a `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Provided Library List (Serverless Environment Version 4)

The following table lists the required dependencies and their versions for **serverless environment version 4**. For the installed libraries for other environment versions, refer to the [serverless environment version notes](/concepts/serverless-environment-versioning.md). ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

| Group ID | Artifact ID | Version |
| :--- | :--- | :--- |
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

> **Note:** The library versions listed above are for **serverless environment version 4**. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Alternatives to Bundling Libraries

If a library is required for your JAR but is not listed among the provided libraries, you have two primary options to make it available without bundling it inside the JAR itself: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

- **Attach as an environment library**: You can add a library to your [serverless environment](/concepts/serverless-gpu-environment.md) using its configuration settings. This is suitable for runtime-only libraries that you do not wish to include in your JAR. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Connect to an external database**: For JDBC-based data sources, you should use a JDBC connection instead of including a JDBC driver in your JAR. JDBC connections are managed by [Unity Catalog](/concepts/unity-catalog.md), and credentials, lineage, and governance are handled automatically for you. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Related Concepts

- Serverless Compute
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)
- [Databricks Connect](/concepts/databricks-connect.md)
- [Spark Connect](/concepts/spark-connect.md)
- Environment Library
- [JAR task for jobs](/concepts/jar-task-in-lakeflow-jobs.md)

### Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
