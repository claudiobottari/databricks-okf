---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 870f446448cb4a7bb3812baf06924ccdb3d2c4c573c9929b8f906e65602c9f86
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbutilsgetdbutils
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: DBUtils.getDBUtils
description: The Scala API entry point in the Databricks Utilities for Scala library used to access DBFS and secrets functionality within Databricks Connect projects.
tags:
  - databricks
  - scala
  - api
  - utilities
timestamp: "2026-06-19T09:55:04.959Z"
---

# DBUtils.getDBUtils

`DBUtils.getDBUtils` is a method from the [Databricks Utilities for Scala](/concepts/databricks-utilities-for-scala-library.md) library that returns an instance of the Databricks Utilities object. This object provides access to the Databricks File System (DBFS) and Secrets through Databricks Utilities in a [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) project. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

`DBUtils.getDBUtils` is the primary entry point for using Databricks Utilities in Scala when working with Databricks Connect. It belongs to the `com.databricks.sdk.scala.dbutils.DBUtils` class. The returned object exposes common utility methods, such as `fs` for file system operations and `secrets` for secret management. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities for Scala library, so you do not need to explicitly add this dependency to your build file (e.g., `build.sbt`, `pom.xml`, or `build.gradle`). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Usage

To use `DBUtils.getDBUtils`, you must first initialize a `DatabricksSession` in your Databricks Connect project. The authentication for the Databricks Utilities library is determined through that session initialization. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

```scala
import com.databricks.sdk.scala.dbutils.DBUtils

val dbutils = DBUtils.getDBUtils()
```

After obtaining the instance, you can use its methods, such as `dbutils.fs.put()`, `dbutils.fs.head()`, and `dbutils.fs.rm()`, as well as `dbutils.secrets` for secret access. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available Functionality

In Scala, `DBUtils.getDBUtils` supports only two categories of Databricks Utilities:

- **Databricks File System (DBFS)** – file read/write/delete operations on DBFS and Unity Catalog volumes.
- **Secrets** – retrieval of secret values stored in Databricks-backed secret scopes.

No other Databricks Utilities (e.g., widgets, notebook, or job utilities) are available through this approach. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Create a file in a Unity Catalog volume

The following Scala example uses `DBUtils.getDBUtils` to interact with a Unity Catalog volume. It creates a file named `zzz_hello.txt` in the volume's path, reads its content, and then deletes the file.

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

This code demonstrates the common pattern of obtaining the utilities object and performing file operations against a Unity Catalog volume. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – The SDK that enables connecting remote applications to Databricks clusters.
- [Databricks Utilities for Scala](/concepts/databricks-utilities-for-scala-library.md) – The library that provides `DBUtils.getDBUtils` and related utilities.
- Databricks File System (DBFS) – The distributed file system used by Databricks.
- Secrets – Secure storage for sensitive credentials, accessible via `dbutils.secrets`.
- Unity Catalog volumes – Managed storage volumes that can be accessed through DBFS utility methods.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
