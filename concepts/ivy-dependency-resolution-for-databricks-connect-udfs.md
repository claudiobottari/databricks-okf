---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0f0e7249dbfc7746924c3d2457152d8632d3f543136b92bee61e7aa5191aa92f
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ivy-dependency-resolution-for-databricks-connect-udfs
    - IDRFDCU
    - Ivy dependency resolution
  citations:
    - file: user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
title: Ivy Dependency Resolution for Databricks Connect UDFs
description: Using spark.addArtifact() with ivy:// URIs to download third-party Maven dependencies at runtime for UDFs that depend on libraries not present on the Databricks cluster.
tags:
  - databricks-connect
  - scala
  - udf
  - dependencies
timestamp: "2026-06-19T23:23:42.404Z"
---

# Ivy Dependency Resolution for [Databricks Connect](/concepts/databricks-connect.md) UDFs

**Ivy Dependency Resolution for [Databricks Connect](/concepts/databricks-connect.md) UDFs** refers to the mechanism by which [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) downloads third‑party Maven artifacts to a remote cluster when executing user‑defined functions (UDFs) that depend on libraries not already present on the cluster. This is done using the `ivy://` URI scheme with the `spark.addArtifact()` API. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

When developing UDFs locally with [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), the compiled classes and JARs of the local project must be uploaded to the Databricks cluster. If a UDF uses a third‑party library that is not available on the cluster, a `ClassNotFoundException` occurs at runtime. To resolve such dependencies, [Databricks Connect](/concepts/databricks-connect.md) provides an Ivy‑based resolution mechanism that downloads artifacts from Maven repositories. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Mechanism

The `spark.addArtifact()` method accepts an `ivy://` URI that encodes standard Maven coordinates in the format `ivy://groupId:artifactId:version`. For example, the Apache Commons Text library version 1.10.0 is specified as `ivy://org.apache.commons:commons-text:1.10.0`. When the session is created, the artifact and its transitive dependencies are downloaded from the configured Maven repository and made available on the cluster. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

The `ivy://` resolution is performed only when a Spark session is already initialized. It is typically called after `DatabricksSession.builder().getOrCreate()`. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Usage Example

Consider a UDF that uses `StringEscapeUtils.escapeHtml4()` from the Apache Commons Text library. The library is declared in `build.sbt` as a `Provided` dependency because it does not need to be bundled locally — it will be fetched by [Databricks Connect](/concepts/databricks-connect.md) at runtime.

```scala
// build.sbt
libraryDependencies ++= Seq(
  "org.apache.commons" % "commons-text" % "1.10.0" % Provided,
  "oro" % "oro" % "2.0.8"  // Required for ivy:// to work
)
```

In the application code, after creating the Spark session, the artifact is resolved:

```scala
def getSession(): SparkSession = {
  if (sys.env.contains("DATABRICKS_RUNTIME_VERSION")) {
    SparkSession.active
  } else {
    val spark = [[databrickssession|DatabricksSession]].builder()
      .addCompiledArtifacts(
        Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI)
      .getOrCreate()
    spark.addArtifact("ivy://org.apache.commons:commons-text:1.10.0")
    spark
  }
}
```

^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Requirements

For the `ivy://` resolution to function correctly, the `oro` library must be included as a dependency in the project’s build file. The source material states that `oro` version 2.0.8 is required for `ivy://` to work. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

When uploading JARs via `addCompiledArtifacts()`, all transitive dependency JARs must be included because the APIs do not automatically detect transitive dependencies. This note applies generally to JAR uploads, but the `ivy://` mechanism itself handles transitive resolution from Maven repositories. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Limitations

- The `ivy://` scheme relies on Maven repository infrastructure; it is not applicable for dependencies that are not published to a Maven repository. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]
- Support for UDFs on [serverless compute](/concepts/serverless-gpu-compute.md) follows the initial minor release of [Databricks Connect](/concepts/databricks-connect.md). See the version compatibility table for supported versions. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- User-defined functions in Databricks Connect for Scala
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)
- Maven – The dependency repository used by the `ivy://` scheme
- Apache Ivy – The resolution engine underlying the `ivy://` URI
- [addCompiledArtifacts](/concepts/addcompiledartifacts-api.md) – Uploads local classes and JARs to the cluster

## Sources

- user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws-38ccefae.md)
