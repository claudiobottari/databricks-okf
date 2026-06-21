---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1aef7de9315f73f1c4df803a42b19b7e5d079cf5310ae53c26a1f13f8aed7da0
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - jar-dependency-management-on-serverless
    - JDMOS
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: JAR Dependency Management on Serverless
description: "Three strategies to make libraries available to JARs on serverless: use provided libraries, attach as environment libraries, or use JDBC connections for external databases."
tags:
  - dependencies
  - serverless
  - jar
  - libraries
timestamp: "2026-06-19T09:35:28.409Z"
---

# JAR Dependency Management on Serverless

**JAR Dependency Management on Serverless** refers to the set of practices and constraints for making external libraries available to Java or Scala JARs running on [serverless compute](/concepts/serverless-gpu-compute.md) in a Databricks Lakeflow Job. Because serverless compute uses [Spark Connect](/concepts/spark-connect.md) and a curated runtime environment, dependency handling differs from classic compute — bundling incompatible or duplicate libraries can cause runtime failures. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Supported Strategies

Databricks recommends three strategies for making a library available to a JAR on serverless compute, depending on the type of dependency:

| Strategy | When to Use |
|----------|-------------|
| **Use a provided library** | The library is already included in the serverless environment. Declare it `provided` in your build tool and do **not** bundle it in the JAR. |
| **Attach as an environment library** | The library is not provided, but you want it available at runtime without bundling it in the JAR. Add it to the serverless environment configuration. |
| **Connect to an external database** | You need a JDBC driver. Use a JDBC connection (Unity Catalog–managed) instead of including the driver in the JAR. Credentials, lineage, and governance are handled automatically. |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Bundling your own versions of libraries that are already provided triggers a `NoSuchMethodError` at runtime. Always check the provided library list for your serverless environment version before building the JAR. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Provided Libraries

The following libraries are required dependencies and are available by default on serverless compute. They must be declared `provided` in your build file. The versions below correspond to **serverless environment version 4**; for other environment versions, see the serverless environment version release notes. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

| GroupId | ArtifactId | Version |
|---------|------------|---------|
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

## Version Compatibility Requirements

To avoid runtime failures, the JAR's Scala, JDK, and Databricks Connect versions must exactly match the serverless runtime's versions. For example, for serverless environment version 4: compile against Scala 2.13, JDK 17 (class file version 61), and Databricks Connect 17.3. Use only public Spark APIs — code using RDDs, Spark internals (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, etc.), or native libraries (`.so`, `.dll`, JNI) will fail on serverless compute. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Recommendations

Databricks strongly recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of manually building and deploying JARs. Bundles simplify creating a project from a template with the correct Scala, JDK, and Databricks Connect versions already configured for serverless, and enable simple deployment of the JAR to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Serverless compute](/concepts/serverless-gpu-compute.md)
- [Databricks Connect](/concepts/databricks-connect.md) — the Spark API surface for serverless compute
- [Spark Connect](/concepts/spark-connect.md) — the underlying protocol for serverless JAR execution
- Photon — acceleration engine (JAR must use public Spark APIs to benefit)
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)
- JDBC connection — Unity Catalog–managed external database connectivity

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
