---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 72284b4cadce329b92ae9727f14701e5000eef25f28781ec2c90fabc11e3d72b
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-environment-versioning
    - SEV
    - Serverless Environment Version
    - Serverless Environment Versions
    - Serverless GPU Environment Versions
    - Serverless GPU environment versions
    - Serverless environment version
    - Serverless environment version 2
    - Serverless environment version notes
    - Serverless environment versions
    - serverless environment version
    - serverless environment version notes
    - Serverless environment versions|serverless environment version
    - serverless environment configuration
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Serverless Environment Versioning
description: Serverless compute uses versioned environments (e.g., version 4) that define exact Scala, JDK, and Databricks Connect versions your JAR must match to run without failures.
tags:
  - serverless
  - environment-version
  - versioning
timestamp: "2026-06-19T09:35:24.912Z"
---

---
title: Serverless Environment Versioning
summary: Serverless compute environments are versioned to provide stable sets of runtime dependencies (Scala, JDK, Spark, and libraries) that jobs must match to run correctly.
sources:
  - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
kind: concept
createdAt: 2026-06-18T08:07:54.120Z
updatedAt: 2026-06-18T08:07:54.120Z
tags:
  - serverless
  - environments
  - versioning
  - databricks
aliases:
  - serverless-environment-versioning
  - serverless-runtime-version
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Serverless Environment Versioning

**Serverless environment versioning** refers to the mechanism by which Databricks’ [serverless compute](/concepts/serverless-gpu-compute.md) provides a curated, versioned set of runtime components — including Scala, JDK, Databricks Connect, and common libraries — that all jobs on that environment must be compatible with to execute successfully. Each environment version pins exact library versions, ensuring reproducibility and avoiding dependency conflicts. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## How Version Selection Works

When configuring a JAR task or any job that uses serverless compute, you must select a serverless environment version. For JAR workloads, Databricks recommends using environment version 4 or higher. The version is chosen in the job’s compute configuration, either through the UI (clicking the edit pencil next to the environment) or programmatically via the API. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Compatibility Requirements

To run a JAR on a given serverless environment version, the following must exactly match the versions declared for that environment:

- **Scala version** (for Scala JARs)
- **JDK version** (class file version)
- **Databricks Connect version** (the Spark API surface)

Mismatches cause runtime errors (e.g., `NoSuchMethodError` or `NoClassDefFoundError`). For example, environment version 4 requires Scala 2.13.16, JDK 17, and Databricks Connect 17.3.2. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Provided Libraries

Each serverless environment version ships a set of preinstalled libraries that are **always available**. These include Spark dependencies, logging, HTTP clients, JSON libraries, and Databricks SDKs. When building a JAR, you must declare these libraries as `provided` in your build tool (e.g., sbt, Maven) — bundling your own versions will override the provided ones and cause `NoSuchMethodError` at runtime. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

For a complete list of libraries for version 4, see the source documentation; for other versions, refer to the [serverless environment version notes](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/). ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Attaching Additional Libraries

If your JAR requires libraries that are not in the provided set, you can attach them as **environment libraries** to the serverless environment. Alternatively, you may bundle them directly inside the JAR — provided they do not conflict with provided libraries. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Version Notes and Updates

Databricks publishes release notes for each serverless environment version, documenting the exact versions of all bundled components. These notes are the authoritative source for determining which Scala, JDK, and library versions apply to a given environment version. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Serverless Compute
- JAR Tasks
- [Databricks Connect](/concepts/databricks-connect.md)
- [Scala JARs on Serverless](/concepts/building-scala-jars-with-sbt-assembly-for-serverless.md)
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)
- [Spark Connect](/concepts/spark-connect.md)

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
