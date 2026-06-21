---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7994d4619c621d96ef9d1e4ac24448bb8255fd95159510c06c79114000d4e412
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limited-utility-availability-in-databricks-connect-for-scala
    - LUAIDCFS
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Limited Utility Availability in Databricks Connect for Scala
description: Only DBFS filesystem and secrets utilities are available through Databricks Utilities for Scala; no other utilities are supported
tags:
  - databricks
  - scala
  - limitations
timestamp: "2026-06-19T18:15:54.414Z"
---

# Limited Utility Availability in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)

**Limited Utility Availability in Databricks Connect for Scala** describes the subset of Databricks Utilities that can be used when writing Scala applications with [Databricks Connect](/concepts/databricks-connect.md). When developing with [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) (Databricks Runtime 13.3 LTS and above), only DBFS and Secrets utilities are accessible via `DBUtils.getDBUtils()`; all other Databricks Utilities functionality is unavailable. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

Databricks Utilities provide a set of convenience commands (`dbutils`) commonly used in notebooks for file operations, secrets management, and cluster interaction. When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), the `DBUtils.getDBUtils()` method (from the [Databricks Utilities for Scala](https://central.sonatype.com/artifact/com.databricks/databricks-dbutils-scala_2.12/versions) library) grants access only to the **DBFS** and **secrets** subsets of the full Databricks Utilities API. No other utility categories — such as widgets, notebook workflows, or filesystem mounts — are supported in Scala projects. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available Utilities

- **DBFS (Databricks File System)** — Read, write, delete, and list files on DBFS paths (including Unity Catalog volumes).
- **Secrets** — Access secrets stored in Databricks secret scopes.

These two utilities are accessed via the `dbutils` object returned by `DBUtils.getDBUtils()`. The library dependency is already declared by [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), so no additional build configuration (e.g., `build.sbt`, `pom.xml`, `build.gradle`) is required. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Unavailable Features

All other Databricks Utilities functionality—including but not limited to widgets (`dbutils.widgets`), notebook workflows (`dbutils.notebook`), and filesystem mounting (`dbutils.fs.mount`)—are **not** available when using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). For the Python version of this article, see [Databricks Utilities with Databricks Connect for Python](/concepts/databricks-utilities-with-databricks-connect.md). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication

Authentication for the Databricks Utilities for Scala library is determined through the initialization of the `DatabricksSession` class in your Databricks Connect project. This session must be set up before calling `DBUtils.getDBUtils()`. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Create, read, and delete a file in a volume

The following example demonstrates using the DBFS utility to interact with a Unity Catalog volume:

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

This code writes a string to a file in a volume, reads and prints its contents, then deletes the file. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- Databricks Utilities
- DBFS
- Secrets
- [DatabricksSession](/concepts/databrickssession.md)
- Unity Catalog volumes
- [Databricks Utilities with Databricks Connect for Python](/concepts/databricks-utilities-with-databricks-connect.md)
- Scala SDK for Databricks

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
