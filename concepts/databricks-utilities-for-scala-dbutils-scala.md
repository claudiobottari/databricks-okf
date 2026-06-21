---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d5ff1fdf68269f7a6d6acc1326bf823d3e7e76239ed38a56c78bba86d4eee93
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-utilities-for-scala-dbutils-scala
    - DUFS(
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Utilities for Scala (dbutils-scala)
description: A Scala library (com.databricks:databricks-dbutils-scala_2.12) that provides access to DBFS and secrets utilities via DBUtils.getDBUtils in Databricks Connect for Scala projects.
tags:
  - databricks
  - scala
  - utilities
timestamp: "2026-06-19T14:54:42.359Z"
---

# Databricks Utilities for Scala (dbutils-scala)

**Databricks Utilities for Scala (dbutils-scala)** is a library that provides access to select Databricks Utilities functionality within Scala projects using [Databricks Connect](/concepts/databricks-connect.md). It enables developers to interact with the Databricks File System (DBFS) and secrets from Scala applications, IDEs, and custom applications connected to Databricks clusters. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

The `dbutils-scala` library is published as the `com.databricks:databricks-dbutils-scala_2.12` artifact on Maven Central. [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on this library, so Scala projects using Databricks Connect do not need to explicitly add it to their build files (such as `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available Functionality

Only a subset of Databricks Utilities functionality is available through the Scala library:

- **DBFS operations**: File system operations on the Databricks File System, including reading, writing, and deleting files.
- **Secrets operations**: Access to secrets stored in Databricks secret scopes.

No other Databricks Utilities (such as `notebook`, `widgets`, or `jobs`) are available for Scala projects through this library. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in your Databricks Connect project for Scala. The library uses the same authentication configuration as the Databricks Connect session. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Usage

To access Databricks Utilities in Scala, use the `DBUtils.getDBUtils()` method from the `com.databricks.sdk.scala.dbutils` package. This returns a `DBUtils` object that provides access to the `fs` (file system) and `secrets` utilities. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

### Example: Create a file in a Unity Catalog volume

The following example demonstrates how to use the Databricks Utilities for Scala library to interact with a [Unity Catalog](/concepts/unity-catalog.md) volume. It creates a file named `zzz_hello.txt` in the volume's path, reads the data from the file, and then deletes the file. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

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

## Compatibility

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above. For the Python version of this functionality, see [Databricks Utilities with Databricks Connect for Python](/concepts/databricks-utilities-with-databricks-connect.md). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables connecting external applications to Databricks clusters.
- Databricks Utilities — The full set of utility commands available in Databricks notebooks.
- Databricks File System (DBFS) — The distributed file system mounted into a Databricks workspace.
- Secrets — Sensitive credentials managed through Databricks secret scopes.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for managing data assets in Databricks.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
