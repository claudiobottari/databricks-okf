---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b47e26d21445198cbd924465535b721ed33c001c2bf549349b6342c202042428
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbutilsgetdbutils-method
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: DBUtils.getDBUtils() method
description: The entry point method in the dbutils-scala library that returns a DBUtils instance for accessing Databricks File System (DBFS) and secrets utilities within a Databricks Connect for Scala project.
tags:
  - databricks
  - scala
  - api
timestamp: "2026-06-19T14:54:56.336Z"
---

## DBUtils.getDBUtils() method

The **`DBUtils.getDBUtils()` method** is a static factory method within the Databricks Utilities for Scala library (`com.databricks.sdk.scala.dbutils.DBUtils`). It returns a `DBUtils` instance that provides access to Databricks File System (DBFS) and Secrets functionality within a [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) project. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

`DBUtils.getDBUtils()` is the primary entry point for using Databricks Utilities in Scala when working with [Databricks Connect](/concepts/databricks-connect.md). It is part of the `com.databricks.databricks-dbutils-scala_2.12` library. [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) projects automatically include this dependency, so developers do not need to add it manually in build files like `build.sbt` (sbt), `pom.xml` (Maven), or `build.gradle` (Gradle). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

The method is designed to work exclusively with DBFS file operations and secrets management. No other Databricks Utilities features (such as notebook workflow, widgets, or job scheduling) are available through this method in Scala projects. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

Authentication for the returned `DBUtils` instance is inherited from the `DatabricksSession` that the developer initializes before calling `getDBUtils()`. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Usage

A typical Scala program using Databricks Connect will import `com.databricks.sdk.scala.dbutils.DBUtils` and then call `DBUtils.getDBUtils()` to obtain a helper object. The returned `DBUtils` object provides the methods available in the standard Databricks Utilities for Scala, such as:

- `dbutils.fs.put(path, contents, overwrite)` – write content to a file
- `dbutils.fs.head(path)` – read the first bytes of a file
- `dbutils.fs.rm(path)` – delete a file or directory
- Secrets access via `dbutils.secrets` (e.g., `dbutils.secrets.get(scope, key)`)

The `dbutils.fs.put` method can be used to create files in [Unity Catalog](/concepts/unity-catalog.md) volumes as well as classic DBFS paths. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example

The following Scala example demonstrates creating a file in a Unity Catalog volume, reading its content, and then deleting the file:

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

- Databricks Utilities – Complete suite of utility methods (only FS and Secrets are available in Scala).
- Databricks File System (DBFS) – Distributed file system mounted to Databricks workspaces.
- Secrets – Secure storage for sensitive credentials.
- [Databricks Connect](/concepts/databricks-connect.md) – Client library that lets you run Spark code remotely on a Databricks cluster.
- [Unity Catalog](/concepts/unity-catalog.md) – Fine-grained data governance solution for managing data assets.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Runtime that includes GPU support and common deep learning libraries.
- Supported GPU Types on Databricks – Full list of GPU instances available across clouds.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
