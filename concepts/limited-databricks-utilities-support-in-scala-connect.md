---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9c164463948832d03d264bc34b594092693fbd31e473171f9af99205b98583f
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limited-databricks-utilities-support-in-scala-connect
    - LDUSISC
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Limited Databricks Utilities Support in Scala Connect
description: Only DBFS and secrets utilities are available through Databricks Connect for Scala; no other Databricks Utilities (like widgets, notebook, etc.) are supported for Scala projects.
tags:
  - databricks
  - scala
  - limitations
  - utilities
timestamp: "2026-06-18T15:10:26.778Z"
---

---
title: Limited Databricks Utilities Support in Scala Connect
summary: Only a subset of Databricks Utilities (DBFS and Secrets) are available via the `DBUtils.getDBUtils()` API in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). Other utilities are not supported.
sources:
  - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:06:40.019Z"
updatedAt: "2026-06-18T08:06:40.019Z"
tags:
  - databricks-connect
  - scala
  - databricks-utilities
  - limited-support
aliases:
  - limited-databricks-utilities-support-in-scala-connect
  - LDUSSC
confidence: 1.0
provenanceState: extracted
inferredParagraphs: 0
---

# Limited Databricks Utilities Support in Scala Connect

**Limited Databricks Utilities Support in Scala Connect** refers to the constrained set of Databricks Utilities that are accessible when using [Databricks Connect](/concepts/databricks-connect.md) for Scala. Only two utility categories — DBFS and Secrets — are available through the `DBUtils.getDBUtils()` API. All other Databricks Utilities are not supported in Scala projects built on Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

Databricks Connect for Databricks Runtime 13.3 LTS and above is required to use this limited utility support. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), developers can programmatically interact with the DBFS (Databricks File System) and manage Secrets (e.g., secret scopes and keys) via Databricks Utilities. These capabilities are exposed through the `DBUtils.getDBUtils()` method, which belongs to the [Databricks Utilities for Scala](https://central.sonatype.com/artifact/com.databricks/databricks-dbutils-scala_2.12/versions) library. The library is already declared as a dependency in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) projects, so no additional build configuration (such as `build.sbt`, `pom.xml`, or `build.gradle`) is needed. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in the Databricks Connect project. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Supported Utilities

The following Databricks Utilities are available:

- **DBFS Utility (`dbutils.fs`)** – Allows file operations such as reading, writing, and deleting files on DBFS or Unity Catalog volumes. The `put`, `head`, and `rm` methods are demonstrated in the official example. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- **Secrets Utility (`dbutils.secrets`)** – Allows access to secret scopes and secrets. The source notes this utility is available but does not provide a Scala example. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Unsupported Utilities

No Databricks Utilities functionality other than DBFS and Secrets is available for Scala projects using Databricks Connect. Utilities such as `dbutils.widgets`, `dbutils.notebook`, `dbutils.jobs`, and others are not supported. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Usage

To use the supported utilities in a Scala application:

1. Ensure the Databricks Connect client is set up for Scala. See the [Databricks Connect for Scala installation guide](/concepts/databricks-connect-for-scala-installation.md).
2. Import `com.databricks.sdk.scala.dbutils.DBUtils`.
3. Call `DBUtils.getDBUtils()` to obtain the `dbutils` instance. This method returns a singleton object.
4. Call the desired utility methods (e.g., `dbutils.fs.put(...)`) as shown in the example below.

## Example: Create a file in a Unity Catalog volume

The following example demonstrates using the DBFS utility to create, read, and delete a file in a Unity Catalog volume:

```scala
import com.databricks.sdk.scala.dbutils.DBUtils

object Main {
  def main(args: Array[String]): Unit = {
    val filePath = "/Volumes/main/default/my-volume/zzz_hello.txt"
    val fileData = "Hello, Databricks!"
    val dbutils = DBUtils.getDBUtils()
    dbutils.fs.put(
      file = filePath,
      contents = fileData,
      overwrite = true
    )
    println(dbutils.fs.head(filePath))
    dbutils.fs.rm(filePath)
  }
}
```

^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that enables remote execution against Databricks clusters.
- Databricks Utilities – The full set of CLI-like utilities available in Databricks notebooks.
- DBFS (Databricks File System) – Distributed file system for storing data.
- Secrets – Secure storage for sensitive information.
- Unity Catalog Volumes – Managed storage for non-tabular data.
- [DatabricksSession](/concepts/databrickssession.md) – Entry point for authentication in Databricks Connect.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
