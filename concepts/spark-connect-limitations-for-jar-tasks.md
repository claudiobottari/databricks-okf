---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 17671164ec7cb19f4845fc1f81dbbfe32eb86d54c2b5ae865fc854369f8251b8
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-connect-limitations-for-jar-tasks
    - SCLFJT
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Spark Connect Limitations for JAR Tasks
description: Serverless compute uses Spark Connect; RDD APIs, Spark internal APIs, and native libraries (.so, .dll, JNI) are unavailable. Code must use DataFrame/Dataset APIs via SparkSession.
tags:
  - databricks
  - spark-connect
  - limitations
timestamp: "2026-06-18T14:53:10.511Z"
---

---
title: Spark Connect Limitations for JAR Tasks
summary: Restrictions on RDD APIs, Spark internal APIs, and native libraries when running JAR tasks on serverless compute using Spark Connect.
sources:
  - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T13:00:00.000Z"
tags:
  - spark-connect
  - jars
  - serverless
  - limitations
aliases:
  - spark-connect-limitations-for-jar-tasks
  - SCLJT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Spark Connect Limitations for JAR Tasks

**Spark Connect Limitations for JAR Tasks** describes the restrictions on code and libraries when a JAR task is executed on Serverless Compute, which relies on [Spark Connect](/concepts/spark-connect.md). Because serverless compute uses Spark Connect’s thin client architecture, the JAR code runs against a client library that exposes only public Spark APIs, while the Spark engine itself runs server-side. Code that bypasses the public API cannot benefit from the Catalyst Optimizer or Photon acceleration, even on classic compute.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Restrictions

The following APIs and library types are **not available** on serverless compute for JAR tasks. If a workload requires any of these, run it on [standard compute](/concepts/standard-access-mode-compute.md) or [dedicated compute](/concepts/dedicated-access-mode-for-ml-compute.md) instead.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### RDD API

The RDD API (`org.apache.spark.rdd.*`) and `SparkContext` / `JavaSparkContext` are not supported. Instead, use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Spark Internal APIs

Spark internal APIs (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`) cannot be used. Code that imports these APIs fails with `NoClassDefFoundError`. Refactor such code to use the public Spark API. If a third-party library uses internals, check whether it publishes a Spark Connect‑compatible release.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

### Native Libraries

Native libraries (`.so`, `.dll`, JNI) are not permitted because serverless compute does not allow writing native binaries to the file system. Libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`. Init scripts are not a workaround. If a Java equivalent is available, use it instead.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Workarounds and Recommendations

- For workloads that require RDDs, Spark internals, or native libraries, use [standard compute](/concepts/standard-access-mode-compute.md) or [dedicated compute](/concepts/dedicated-access-mode-for-ml-compute.md) rather than serverless.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- When developing new JARs for serverless, ensure that all dependencies are compatible with Spark Connect. The [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) approach (now strongly recommended by Databricks) automatically configures the correct Scala, JDK, and Databricks Connect versions.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- Test your JAR on serverless early; the most common failures are `NoClassDefFoundError` from internal API usage and `UnsatisfiedLinkError` from native libraries.^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md)
- Serverless Compute
- JAR Task
- Photon
- Catalyst Optimizer
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)
- Standard Compute
- [Dedicated Compute](/concepts/dedicated-access-mode-for-ml-compute.md)

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
