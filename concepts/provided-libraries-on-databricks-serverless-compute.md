---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb366fcd0044fa4232b94fb67afa54b0e667c82e433a3bd1cce7db1581041dda
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provided-libraries-on-databricks-serverless-compute
    - PLODSC
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Provided Libraries on Databricks Serverless Compute
description: A curated set of libraries (Databricks Connect, Scala, logging, HTTP, Jackson, Guava, etc.) are pre-installed on serverless compute; bundling duplicate versions causes NoSuchMethodError.
tags:
  - databricks
  - provided-libraries
  - dependencies
  - serverless
timestamp: "2026-06-19T18:00:59.551Z"
---

# Provided Libraries on Databricks Serverless Compute

**Provided Libraries on Databricks Serverless Compute** refers to the set of libraries that are pre-installed and available by default on serverless compute environments in Databricks. These libraries are required dependencies for JAR-based workloads and must be declared as `provided` in the build configuration to avoid runtime conflicts.

## Overview

Serverless compute includes a curated set of common libraries that are available without additional configuration. When building JARs for serverless compute, developers must declare these libraries as `provided` in their build tool (such as sbt or Maven). Bundling custom versions of these libraries in the JAR triggers a `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Library Versions by Environment Version

The specific library versions depend on the serverless environment version being used. The versions listed below apply to **serverless environment version 4**. For other environment versions, consult the serverless environment version notes. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Core Spark and Scala Libraries

- `com.databricks:databricks-connect_2.13`, version 17.3.2
- `org.scala-lang:scala-library_2.13`, version 2.13.16
- `org.scala-lang:scala-reflect_2.13`, version 2.13.16 ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Logging Libraries

- `org.slf4j:slf4j-api`, version 2.0.10
- `org.apache.logging.log4j:log4j-api`, version 2.20.0
- `org.apache.logging.log4j:log4j-core`, version 2.20.0 ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### HTTP Libraries

- `org.apache.httpcomponents:httpclient`, version 4.5.14
- `org.apache.httpcomponents:httpcore`, version 4.4.16 ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### JSON Libraries

- `com.fasterxml.jackson.core:jackson-databind`, version 2.15.2
- `com.fasterxml.jackson.core:jackson-core`, version 2.15.2
- `com.fasterxml.jackson.core:jackson-annotations`, version 2.15.2
- `com.fasterxml.jackson.datatype:jackson-datatype-jsr310`, version 2.15.2
- `org.json4s:json4s-jackson_2.13`, version 4.0.7 ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Apache Commons Libraries

- `org.apache.commons:commons-lang3`, version 3.14.0
- `org.apache.commons:commons-configuration2`, version 2.11.0
- `org.apache.commons:commons-text`, version 1.12.0 ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Other Common Libraries

- `com.google.guava:guava`, version 32.0.1-jre
- `commons-io:commons-io`, version 2.14.0
- `com.databricks:databricks-sdk-java`, version 0.52.0
- `com.databricks:databricks-dbutils-scala_2.13`, version 0.1.4 ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing Dependencies

When building JARs for serverless compute, developers have three options for making libraries available: ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

1. **Use provided libraries**: Declare compatible versions as `provided` in the build configuration and do not include them in the JAR.
2. **Attach as an environment library**: Add a library to the [serverless environment](/concepts/serverless-gpu-environment.md) if it is not already provided. This is useful for runtime-only libraries that should not be bundled.
3. **Connect to an external database**: For JDBC sources, use a JDBC connection instead of including a driver. JDBC connections are Unity Catalog-managed, with credentials, lineage, and governance handled automatically.

## Best Practices

- Always check the library versions for your specific serverless environment version before building JARs.
- Declare provided libraries with the `provided` scope in sbt or the equivalent scope in Maven to avoid bundling duplicates.
- If a third-party library conflicts with a provided library, check whether the library publishes a version compatible with the serverless environment.

## Related Concepts

- Serverless Environment Version — The runtime version that determines which library versions are available
- Create and Run JARs on Serverless Compute — Guide for building and deploying JARs
- [Databricks Connect](/concepts/databricks-connect.md) — The Spark API surface for serverless compute
- [Spark Connect](/concepts/spark-connect.md) — The underlying architecture for serverless Spark workloads
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The job execution framework for serverless compute

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
