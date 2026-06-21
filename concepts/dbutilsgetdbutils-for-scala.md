---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08b325e26d73ab96916fe53ef2bb2c6fc2f4084e9756770df3d6fb176c799490
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbutilsgetdbutils-for-scala
    - DFS
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: DBUtils.getDBUtils for Scala
description: The method to access Databricks Utilities (DBFS and secrets) in Scala via Databricks Connect
tags:
  - databricks
  - scala
  - api
timestamp: "2026-06-19T18:15:45.431Z"
---

# DBUtils.getDBUtils for Scala

**DBUtils.getDBUtils** is a factory method in the [Databricks Utilities for Scala](/concepts/databricks-utilities-for-scala-library.md) library that provides access to Databricks Utilities functionality within [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) projects. It belongs to the `com.databricks.sdk.scala.dbutils` package and returns a `DBUtils` instance.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

`DBUtils.getDBUtils` enables Scala developers working with Databricks Connect to interact with the Databricks File System (DBFS) and secrets through the Databricks Utilities API. The method instantiates a `DBUtils` object that mirrors the familiar `dbutils` interface available in Databricks notebooks.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

### Availability

`DBUtils.getDBUtils` is available in Databricks Connect for Databricks Runtime 13.3 LTS and above. It belongs to the [Databricks Utilities for Scala](/concepts/databricks-utilities-for-scala-library.md) library (artifact: `com.databricks/databricks-dbutils-scala_2.12`), published on Maven Central.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Features

The `DBUtils.getDBUtils` method provides access to two primary Databricks Utilities sub-utilities:

- **`dbutils.fs`** — File system operations on DBFS, including reading, writing, and deleting files and directories.
- **`dbutils.secrets`** — Secret retrieval for accessing sensitive information stored in Databricks secret scopes.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

### Limitations

No Databricks Utilities functionality other than the file system and secrets utilities is available for Scala projects through this method.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Dependency Management

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities for Scala library. As a result, developers do not need to explicitly declare this dependency in their Scala project's build file (such as `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle).^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in the Databricks Connect project for Scala. The `DBUtils.getDBUtils` method uses the session's authentication configuration to connect to the Databricks workspace.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Usage Example

The following example demonstrates creating a file in a Unity Catalog volume, reading its contents, and then deleting the file:

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

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The client SDK that enables connecting IDEs and custom applications to Databricks clusters.
- Databricks Utilities — The complete set of utilities available in Databricks notebooks.
- DBUtils for Python — The Python equivalent for accessing Databricks Utilities in Databricks Connect.
- Databricks File System (DBFS) — The distributed file system mounted into a Databricks workspace.
- [Secrets Utility (dbutils.secrets)](/concepts/databricks-utilities-dbutils-via-connect.md) — The sub-utility for accessing secret scopes.
- Unity Catalog Volumes — Storage volumes in Unity Catalog where files can be managed.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
