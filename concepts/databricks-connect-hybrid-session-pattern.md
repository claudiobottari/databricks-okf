---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5907bb922ba9313cbbc37c8819e480932a576cf37569c833cb9b3411f93ec327
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-hybrid-session-pattern
    - DCHSP
  citations:
    - file: user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect Hybrid Session Pattern
description: A design pattern where code checks for the DATABRICKS_RUNTIME_VERSION environment variable to decide whether to reuse an existing SparkSession (on-cluster) or create a new DatabricksSession with artifact uploads (local development).
tags:
  - databricks-connect
  - scala
  - session-management
  - pattern
timestamp: "2026-06-19T23:23:28.160Z"
---

## [Databricks Connect](/concepts/databricks-connect.md) Hybrid Session Pattern

The **Databricks Connect Hybrid Session Pattern** is a coding practice that lets a single SparkSession initialization routine work both in a local development environment (using [Databricks Connect](/concepts/databricks-connect.md)) and on a Databricks cluster. The pattern detects where the code is running and creates the session accordingly, avoiding manual switching between configurations.

### Overview

When developing Spark applications locally with [Databricks Connect](/concepts/databricks-connect.md), the session must be created to connect to a remote cluster. When the same code is deployed directly on a Databricks cluster, the session already exists and must be reused. The hybrid session pattern uses the `DATABRICKS_RUNTIME_VERSION` environment variable – which is set only on Databricks clusters – to decide which session creation path to take.^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

This pattern is critical for User-Defined Functions (UDFs) and Typed Dataset APIs because those workloads require compiled classes and JARs to be uploaded to the remote cluster only when running locally. On a cluster, the artifacts are already available.^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

### Implementation

The core of the pattern is a `getSession()` method that branches on the environment variable:

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]
import org.apache.spark.sql.SparkSession

def getSession(): SparkSession = {
  if (sys.env.contains("DATABRICKS_RUNTIME_VERSION")) {
    // On a Databricks cluster — reuse the active session
    SparkSession.active
  } else {
    // Locally with [[databricks-connect|Databricks Connect]] — upload local JARs and classes
    [[databrickssession|DatabricksSession]]
      .builder()
      .addCompiledArtifacts(
        Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI
      )
      .getOrCreate()
  }
}
```^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

The `addCompiledArtifacts()` call uploads all compiled classes in the project's output directory to the remote cluster, enabling UDFs and typed transformations to resolve correctly on the server side.^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

### When to Use

Use the hybrid session pattern whenever you write code that must run both locally (via [Databricks Connect](/concepts/databricks-connect.md)) and directly on a Databricks cluster. This includes:

- Applications that define and register UDFs.
- Code that uses Dataset typed APIs such as `map()`, `filter()`, or `mapPartitions()`.
- Multi-module projects where classes from different modules must be uploaded.^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

For multi-module builds, obtain the code source location from a class in each module and call `addCompiledArtifacts()` multiple times:

```scala
val moduleALocation = Main.getClass
  .getProtectionDomain.getCodeSource.getLocation.toURI
val moduleBLocation = DataProcessor.getClass
  .getProtectionDomain.getCodeSource.getLocation.toURI

[[databrickssession|DatabricksSession]].builder()
  .addCompiledArtifacts(moduleALocation)
  .addCompiledArtifacts(moduleBLocation)
  .getOrCreate()
```^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library enabling local development against a Databricks cluster.
- User-defined functions in Databricks Connect for Scala – Details on UDF execution with artifact upload.
- Typed Dataset APIs – Transformations that require compiled classes on the cluster.
- SparkSession – The entry point for Spark functionality, reused or created per environment.
- UDF artifact upload – The mechanism of uploading JARs and classes for remote execution.

### Sources

- user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws-38ccefae.md)
