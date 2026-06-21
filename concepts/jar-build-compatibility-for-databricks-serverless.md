---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f9fbf95c444007f546566bb7c283077317b156efa5aa55240aeaf766371334d
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - jar-build-compatibility-for-databricks-serverless
    - JBCFDS
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: JAR Build Compatibility for Databricks Serverless
description: Specific version requirements (Scala 2.13, JDK 17, Databricks Connect 17.3 for environment version 4) that JARs must match exactly to run on serverless compute.
tags:
  - databricks
  - compatibility
  - versions
  - JAR
timestamp: "2026-06-19T18:01:34.463Z"
---

# JAR Build Compatibility for Databricks Serverless

**JAR Build Compatibility for Databricks Serverless** refers to the specific version requirements and build constraints that Java and Scala JARs must satisfy to run successfully on Databricks Serverless compute. Because Serverless compute uses [Spark Connect](/concepts/spark-connect.md), JARs must be compiled against exact versions of Scala, JDK, and [Databricks Connect](/concepts/databricks-connect.md) that match the serverless environment version.

## Requirements

To build a JAR for Serverless compute, the local development environment must have:
- [sbt](https://www.scala-sbt.org/download/) 1.11.7 or higher for Scala JARs
- [Maven](https://maven.apache.org/install.html) 3.9.0 or higher for Java JARs
- JDK, Scala, and Databricks Connect versions that match the target Serverless Environment Version ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Dependency Versions

The JAR's Scala and JDK versions must exactly match the runtime versions. For example, a JAR targeting serverless environment version 4 must:
- Be compiled against Scala 2.13 (every dependency uses the `_2.13` suffix)
- Be compiled against JDK 17, class file version 61
- Be compiled against Databricks Connect 17.3, the Spark API surface for serverless compute
- Use only public Spark APIs ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Limitations

Serverless compute uses [Spark Connect](/concepts/spark-connect.md). The JAR runs against a thin client library that exposes public Spark APIs, while the Spark engine runs server-side. The following are **not available** on Serverless compute:
- **RDD API** (`org.apache.spark.rdd.*`), `SparkContext`, or `JavaSparkContext`. Use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead.
- **Spark internal APIs** (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`). Code importing these fails with `NoClassDefFoundError`. Refactor to the public Spark API.
- **Native libraries** (`.so`, `.dll`, JNI). Serverless compute does not permit writing native libraries to the file system. Libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`. Init scripts are not a workaround.

If the workload requires any of the above, run it on standard or dedicated compute instead. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Provided Libraries

Serverless compute includes a curated set of libraries by default. These must be declared `provided` in the build; bundling custom versions triggers `NoSuchMethodError` at runtime. For serverless environment version 4, the provided libraries include:

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

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Managing Dependencies

To make a library available to a JAR on serverless compute:
- **Use a provided library**: Declare it `provided` in the build and don't include it in the JAR.
- **Attach as an environment library**: Add a library to the Serverless Environment if it isn't already provided.
- **Connect to an external database**: For JDBC sources, use a JDBC Connection (Unity Catalog-managed) instead of including a driver. Credentials, lineage, and governance are handled automatically.

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Building and Running a JAR

Databricks recommends using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) instead of manual JAR building. Bundles make it easy to create a project from a template with correct Scala, JDK, and Databricks Connect versions, and enable simple deployment of the JAR to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

To run a JAR as a task:
1. In the workspace, go to **Jobs & Pipelines** and create a new job.
2. Add a **JAR** task.
3. Configure the **Main class** (e.g., `com.examples.SparkJar`).
4. Select **Serverless** for **Compute**.
5. Configure the serverless environment version (4 or higher).
6. Add the JAR file via drag-and-drop or browse to a Unity Catalog Volume or workspace location.
7. Optionally, add parameters as a JSON array (e.g., `["Hello", "World!"]`).

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Troubleshooting

Common exceptions and their causes:

| Exception | Cause | Resolution |
|-----------|-------|------------|
| `NoClassDefFoundError` | JAR uses Spark internal APIs | Refactor to public Spark API; check if a Spark Connect-compatible library release exists |
| `UnsatisfiedLinkError` | JAR includes native libraries (`.so`, `.dll`, JNI) | Use a Java equivalent if available |
| `NoSuchMethodError` | JAR bundles its own version of a provided library | Declare the library as `provided` |

^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Serverless Environment Version — The runtime environment specifying Scala, JDK, and Spark versions
- [Spark Connect](/concepts/spark-connect.md) — The architecture powering serverless compute
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — The recommended method for building and deploying JARs
- JAR Task for Jobs — How to configure JAR tasks in Databricks workflows
- Photon Acceleration — Performance optimization compatible with JAR-based workloads
- Unity Catalog Volume — Storage location for JAR file deployment

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
