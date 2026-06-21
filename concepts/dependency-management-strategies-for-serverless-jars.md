---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40b4b19f995db403b60ac8c5497744823fb5e18367b6a95f166bafbcb828ba6d
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dependency-management-strategies-for-serverless-jars
    - DMSFSJ
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Dependency Management Strategies for Serverless JARs
description: "Three strategies to make libraries available on serverless compute: declare as provided, attach as environment libraries, or use JDBC connections for external databases."
tags:
  - databricks
  - dependencies
  - libraries
  - serverless
timestamp: "2026-06-19T18:00:38.361Z"
---

# Dependency Management Strategies for Serverless JARs

**Dependency Management Strategies for Serverless JARs** refers to the three recommended ways to make libraries available to Java or Scala JARs running on Databricks serverless compute. Because serverless compute uses [Spark Connect](/concepts/spark-connect.md) and a fixed set of pre‑installed libraries, dependency versions must be carefully aligned and libraries must be either marked as provided, attached as environment libraries, or accessed via external connections.

## Overview

When a JAR runs on serverless compute, it executes against a thin client library that exposes only public Spark APIs; the engine runs server‑side. All dependencies – Scala, JDK, [Databricks Connect](/concepts/databricks-connect.md), and third‑party libraries – must exactly match the versions of the serverless environment being used. A mismatch causes runtime errors such as `NoSuchMethodError` or `NoClassDefFoundError`. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

Three strategies exist to manage dependencies:

1. **Use a provided library** – rely on the libraries already pre‑installed on serverless compute.
2. **Attach as an environment library** – add a library to the [serverless environment](/concepts/serverless-gpu-environment.md) at runtime.
3. **Connect to an external database** – for JDBC sources, use a JDBC connection managed by Unity Catalog.

The choice depends on whether the library is already available in the environment, whether it should be bundled inside the JAR, or whether a separate connection approach is more appropriate. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Strategy 1: Use a Provided Library

Serverless compute ships with [Databricks Connect](/concepts/databricks-connect.md) and a curated set of common libraries. If your JAR depends on these libraries and the versions are compatible, declare them `provided` in your build tool (sbt or Maven). This prevents them from being bundled into the JAR and avoids class path conflicts. Bundling your own copies of provided libraries triggers a `NoSuchMethodError` at runtime because the class loader encounters them first and they may not match the environment’s versions. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

The following libraries are provided by default on **serverless environment version 4** (the list changes with each environment version; see the [serverless environment version notes](/concepts/serverless-environment-versioning.md) for other versions):

- `com.databricks:databricks-connect_2.13` – version 17.3.2
- `org.scala-lang:scala-library_2.13` – version 2.13.16
- `org.scala-lang:scala-reflect_2.13` – version 2.13.16
- `org.slf4j:slf4j-api` – version 2.0.10
- `org.apache.logging.log4j:log4j-api` – version 2.20.0
- `org.apache.logging.log4j:log4j-core` – version 2.20.0
- `org.apache.httpcomponents:httpclient` – version 4.5.14
- `org.apache.httpcomponents:httpcore` – version 4.4.16
- `com.fasterxml.jackson.core:jackson-databind` – version 2.15.2
- `com.fasterxml.jackson.core:jackson-core` – version 2.15.2
- `com.fasterxml.jackson.core:jackson-annotations` – version 2.15.2
- `com.fasterxml.jackson.datatype:jackson-datatype-jsr310` – version 2.15.2
- `com.google.guava:guava` – version 32.0.1‑jre
- `commons-io:commons-io` – version 2.14.0
- `org.json4s:json4s-jackson_2.13` – version 4.0.7
- `org.apache.commons:commons-lang3` – version 3.14.0
- `org.apache.commons:commons-configuration2` – version 2.11.0
- `org.apache.commons:commons-text` – version 1.12.0
- `com.databricks:databricks-sdk-java` – version 0.52.0
- `com.databricks:databricks-dbutils-scala_2.13` – version 0.1.4

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Strategy 2: Attach as an Environment Library

For libraries that are not in the provided set, you can attach them to the serverless environment when configuring the JAR task in the Databricks UI. This approach is useful for runtime‑only dependencies that you do not want to include inside the JAR itself. The JAR file and any attached libraries are made available to the Spark client at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Strategy 3: Connect to an External Database (JDBC)

Instead of bundling a JDBC driver inside the JAR or attaching it as a library, use a JDBC connection. JDBC connections are Unity Catalog‑managed – they handle credentials, lineage, and governance automatically. This approach avoids driver version conflicts and simplifies security management. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Best Practices

- **Pin dependency versions exactly.** The JAR’s Scala version must match the serverless environment’s Scala version (e.g., Scala 2.13), and the JDK target must match (e.g., JDK 17). Use the `‑‑release` flag for javac and `‑release` for scalac to enforce compilation against the correct class file version. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Use sbt‑assembly or Maven Shade to create a fat JAR** that includes only those dependencies not already provided. For sbt, add the `sbt‑assembly` plugin (version 2.3.1 or higher) and exclude provided dependencies. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Do not bundle provided libraries.** Always mark them `provided` in your build configuration to avoid class path conflicts. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **For third‑party libraries that use Spark internals**, check whether they publish a [Spark Connect](/concepts/spark-connect.md)‑compatible release. Code that imports `org.apache.spark.sql.internal.*` or similar internals will fail with `NoClassDefFoundError`. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Prefer [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)** over manual JAR building. Databricks strongly recommends using bundles, which automatically generate correct versions for Scala, JDK, and Databricks Connect, and simplify deployment to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Troubleshooting Common Issues

| Error | Likely Cause | Resolution |
|-------|--------------|------------|
| `NoSuchMethodError` | Bundled version of a provided library conflicts with the environment’s version. | Remove the conflicting library from your fat JAR and declare it `provided`. |
| `NoClassDefFoundError` | Code imports Spark internal APIs that are not available on serverless. | Refactor code to use public Spark APIs. |
| `UnsatisfiedLinkError` | Native libraries (`.so`, `.dll`, JNI) are not supported. | Use a pure Java equivalent. |
| Version mismatch | Scala or JDK version in JAR differs from serverless environment. | Recompile with the correct Scala version (e.g., 2.13) and JDK version (e.g., 17). |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)
- Serverless Compute
- [Spark Connect](/concepts/spark-connect.md)
- Photon
- JDBC connections
- JAR Tasks
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- [Serverless environment version notes](/concepts/serverless-environment-versioning.md)

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
