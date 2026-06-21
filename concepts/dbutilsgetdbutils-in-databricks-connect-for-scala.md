---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5fef943aef35a76cd65fa0b6ffdb30063dfcff03e3232f8d90fc3bd44856ab3
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbutilsgetdbutils-in-databricks-connect-for-scala
    - DIDCFS
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: DBUtils.getDBUtils in Databricks Connect for Scala
description: The entry point for accessing Databricks Utilities (DBFS and Secrets) in Scala-based Databricks Connect projects via the DBUtils.getDBUtils() method from the com.databricks.sdk.scala.dbutils package.
tags:
  - databricks
  - scala
  - utilities
  - api
timestamp: "2026-06-18T15:10:24.640Z"
---

# `DBUtils.getDBUtils` in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)

**`DBUtils.getDBUtils`** is the entry point for accessing Databricks Utilities from Scala projects using [Databricks Connect](/concepts/databricks-connect.md). It enables Scala applications to interact with the Databricks File System (DBFS) and secrets through the Databricks Utilities API.

## Overview

`DBUtils.getDBUtils` belongs to the [Databricks Utilities for Scala](/concepts/databricks-utilities-for-scala-library.md) library (`com.databricks:databricks-dbutils-scala_2.12`). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

It provides access to:

- Databricks File System (DBFS) operations
- Secrets utility (`dbutils.secrets`)

## Prerequisites

Before using `DBUtils.getDBUtils`, you must:

1. [Set up the Databricks Connect client](/concepts/databricks-connect-client-setup.md) for installation.
2. Initialize the `DatabricksSession` class in your Databricks Connect project for Scala — this determines authentication for the Utilities library. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Dependency Information

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities for Scala library. You do not need to explicitly add this dependency in your Scala project's build file (such as `build.sbt` for `sbt`, `pom.xml` for Maven, or `build.gradle` for Gradle). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Create a file in a volume

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

This example:

- Creates a file named `zzz_hello.txt` in a Unity Catalog volume.
- Writes the string `"Hello, Databricks!"` to the file.
- Reads the file contents back using `dbutils.fs.head`.
- Deletes the file using `dbutils.fs.rm`.

## Available Utilities

Only the following Databricks Utilities are available for Scala projects through `DBUtils.getDBUtils`:

- `dbutils.fs` — Databricks File System operations (DBFS)
- `dbutils.secrets` — Secrets operations

No other Databricks Utilities functionality is available for Scala projects. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)
- Databricks Utilities
- Databricks File System (DBFS)
- Secrets
- [Unity Catalog](/concepts/unity-catalog.md)
- Unity Catalog volumes
- [DatabricksSession](/concepts/databrickssession.md)

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
