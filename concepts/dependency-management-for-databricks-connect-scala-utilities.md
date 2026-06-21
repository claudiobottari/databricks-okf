---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 99a0e98faa97a740b54eecd979a48e5938de2c249ae29c6c09b0f1f1c1a4fe97
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dependency-management-for-databricks-connect-scala-utilities
    - DMFDCSU
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Dependency management for Databricks Connect Scala Utilities
description: Databricks Connect for Scala automatically declares a dependency on the databricks-dbutils-scala library, so users do not need to add it explicitly in build.sbt, pom.xml, or build.gradle.
tags:
  - databricks
  - scala
  - dependency-management
timestamp: "2026-06-19T14:55:20.148Z"
---

# Dependency management for Databricks Connect Scala Utilities

**Dependency management for Databricks Connect Scala Utilities** refers to how the [Databricks Utilities for Scala](/concepts/databricks-utilities-for-scala-library.md) library is handled as a dependency in Scala projects that use [Databricks Connect](/concepts/databricks-connect.md). The library provides programmatic access to Databricks‑specific features such as the Databricks File System (DBFS) and Secrets.

## Overview

When you set up a Databricks Connect project for Scala, the Databricks Connect client already declares a dependency on the Databricks Utilities for Scala library. You do **not** need to explicitly declare this dependency in your Scala project’s build file — whether that is `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle. The dependency is inherited automatically from the Databricks Connect client. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available utilities

Only a subset of Databricks Utilities functionality is available for Scala projects through Databricks Connect:

- Use `com.databricks.sdk.scala.dbutils.DBUtils.getDBUtils()` to access the Databricks File System (DBFS) and secrets. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- No other Databricks Utilities (such as widgets, notebook workflows, or the file system metadata operations beyond what `DBUtils` provides) are available for Scala projects via Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in your Databricks Connect Scala project. You must configure the session before calling `DBUtils.getDBUtils()`. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Create a file in a volume

The following example demonstrates using the Databricks Utilities for Scala library to work with a Unity Catalog volume. It creates a file named `zzz_hello.txt` in the volume’s path, reads its contents, and then deletes the file.

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

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client framework that connects IDEs and custom applications to Databricks clusters.
- Databricks Utilities – The full set of Databricks utility commands (`dbutils`) available in notebooks and Python clients.
- Scala – The programming language used in these projects.
- DBFS – The Databricks File System, accessible via `DBUtils`.
- Secrets – Securely stored credentials accessible via `DBUtils`.
- Unity Catalog volumes – Managed storage volumes used in the example.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
