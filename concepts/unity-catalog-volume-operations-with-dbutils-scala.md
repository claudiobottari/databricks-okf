---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8cbb32ecf6bdb02fa0c56f1e2dcd50a6e258183c918dccc07580c61db520f089
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volume-operations-with-dbutils-scala
    - UCVOWDS
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Unity Catalog Volume Operations with DBUtils Scala
description: Pattern for creating, reading, and deleting files in Unity Catalog volumes using DBUtils.fs in Scala
tags:
  - databricks
  - scala
  - unity-catalog
  - example
timestamp: "2026-06-19T18:16:22.462Z"
---

# Unity Catalog Volume Operations with DBUtils Scala

**Unity Catalog Volume Operations with DBUtils Scala** refers to the use of the Databricks Utilities for Scala library (DBUtils) to programmatically interact with [Unity Catalog](/concepts/unity-catalog.md) volumes through [Databricks Connect](/concepts/databricks-connect.md) for Scala. This functionality enables creating, reading, and deleting files in Unity Catalog volumes from external Scala applications, IDEs, and custom tools.

## Overview

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) provides access to a subset of Databricks Utilities through the `DBUtils.getDBUtils` method. This method belongs to the Databricks Utilities for Scala library and supports operations on the Databricks File System (DBFS) and secrets management. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

For Unity Catalog volume operations, the DBUtils library provides file system commands (`dbutils.fs`) that work with Unity Catalog volume paths. This allows automation of file management tasks within volumes without requiring a notebook environment. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available Functionality

When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) with DBUtils, the following functionality is available for Unity Catalog volume operations:

- **File creation and writing** — Use `dbutils.fs.put()` to create new files or overwrite existing ones in a volume path.
- **File reading** — Use `dbutils.fs.head()` to read the contents of a file in a volume.
- **File deletion** — Use `dbutils.fs.rm()` to remove files from a volume.

^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

Only DBFS and secrets utilities are available through DBUtils in the Scala Databricks Connect context; other Databricks Utilities are not supported for Scala projects. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Setup and Dependencies

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities for Scala library, so you do not need to explicitly add this dependency to your Scala project's build file (such as `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in your Databricks Connect project for Scala. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: File Operations in a Unity Catalog Volume

The following example demonstrates how to use DBUtils to automate file operations within a Unity Catalog volume. The code creates a file named `zzz_hello.txt` in a specified volume path, reads and prints its contents, then deletes the file. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

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

The example uses three key file system operations:

- `dbutils.fs.put(file, contents, overwrite)` — Creates or overwrites a file at the specified volume path with the given string contents. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- `dbutils.fs.head(filePath)` — Reads and returns the first portion of the file's contents. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- `dbutils.fs.rm(filePath)` — Deletes the file from the volume path. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Volume Path Format

Unity Catalog volume paths follow the format `/Volumes/<catalog>/<schema>/<volume-name>/<path>`, where:

- `<catalog>` is the Unity Catalog name
- `<schema>` is the schema (database) name
- `<volume-name>` is the volume name
- `<path>` is the file path within the volume

^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library enabling external applications to connect to Databricks clusters.
- [Databricks Utilities (DBUtils)](/concepts/databricks-utilities-dbutils-via-connect.md) — The complete set of utility functions available in Databricks environments.
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks' data governance solution for managing data assets.
- Unity Catalog volumes — Managed storage locations within Unity Catalog for file-based data.
- Databricks File System (DBFS) — The distributed file system mounted to Databricks workspaces.
- Secrets utility (dbutils.secrets) — The other utility available through DBUtils in Scala.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
