---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b575a84af3bd9fad74e0d1a811b607969c0764928b51ffb9c33d68f5af349fbf
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-utilities-with-unity-catalog-volumes
    - DUWUCV
    - Databricks Unity Catalog Volume
    - What are Unity Catalog volumes?
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Utilities with Unity Catalog Volumes
description: Using the DBUtils.fs API in Scala to programmatically create, read, and delete files in Unity Catalog volume paths within Databricks Connect projects.
tags:
  - databricks
  - unity-catalog
  - volumes
  - scala
timestamp: "2026-06-19T09:55:13.988Z"
---

# Databricks Utilities with Unity Catalog Volumes

**Databricks Utilities with Unity Catalog Volumes** refers to the usage of Databricks Utilities (also known as `dbutils`) to interact with [Unity Catalog](/concepts/unity-catalog.md) volumes programmatically. This is particularly relevant when working with external environments such as [Databricks Connect](/concepts/databricks-connect.md).

## Overview

Databricks Utilities provides a set of helper functions for common data engineering tasks, including working with the Databricks File System (DBFS), secrets, and file operations. When combined with Unity Catalog volumes, users can automate file creation, reading, and deletion within volume paths using utilities. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available Utilities

When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), only a subset of Databricks Utilities functionality is available:

- **DBFS operations** – Accessible via `DBUtils.getDBUtils()` to perform file system operations such as `put`, `head`, `rm`, and others.
- **Secrets** – Also accessible through the same `dbutils` object.
- **Other utilities** – No other Databricks Utilities (such as widgets, notebook workflow tools, or job management) are available in Scala projects. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication

Authentication for the Databricks Utilities library is determined through the initialization of the `DatabricksSession` class within the Databricks Connect project for Scala. The client must be properly configured before using any utility functions. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Dependency Management

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities for Scala library (`com.databricks:databricks-dbutils-scala_2.12`). Users do **not** need to explicitly declare this dependency in their build file (e.g., `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Creating a File in a Unity Catalog Volume

The following example demonstrates using Databricks Utilities to automate operations on a Unity Catalog volume. It creates a file named `zzz_hello.txt` in a volume path, reads its contents, and then deletes the file. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

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

### Key Notes

- Volume paths in Unity Catalog follow the format `/Volumes/<catalog>/<schema>/<volume>/<path>`.
- The `dbutils.fs.put()` method writes data to a file, with the `overwrite = true` flag allowing replacement of an existing file.
- The `dbutils.fs.head()` method reads and prints the file contents (typically returning the first kilobyte of data).
- The `dbutils.fs.rm()` method deletes the specified file. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – The client library that enables connecting IDEs and custom applications to Databricks clusters
- Unity Catalog Volumes – Catalog-level storage objects that provide governance and access control for non-tabular data
- Databricks File System (DBFS) – The distributed file system interface accessed through Databricks Utilities
- [Secrets Utility (dbutils.secrets)](/concepts/databricks-utilities-dbutils-via-connect.md) – The secrets management component of Databricks Utilities
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – The Python equivalent with its own utility access patterns

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
