---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b00c00102492afd209db25e28543dbf08dcd3dedc5dcf3129b7c36f3748599cc
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volume-automation-via-dbutils
    - UCVAVD
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Unity Catalog volume automation via DBUtils
description: Using DBUtils.getDBUtils with Databricks Connect for Scala to automate Unity Catalog volumes — creating, reading, and deleting files within volume paths.
tags:
  - databricks-connect
  - scala
  - unity-catalog
  - volume
timestamp: "2026-06-18T11:42:55.070Z"
---

# Unity Catalog Volume Automation via DBUtils

**Unity Catalog Volume Automation via DBUtils** describes how to use the [DBUtils](/concepts/dbutilsnotebookrun.md) (Databricks Utilities) library within a [Databricks Connect](/concepts/databricks-connect.md) for Scala project to programmatically manage files in a [Unity Catalog](/concepts/unity-catalog.md) volume. The `DBUtils.getDBUtils()` method provides access to the Databricks File System (DBFS) and Secrets utility, enabling tasks such as creating, reading, and deleting files in Unity Catalog volumes. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available Utilities

When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), only a subset of DBUtils functionality is available:

- **DBFS** (`dbutils.fs`): Use `DBUtils.getDBUtils` to interact with the Databricks File System, including Unity Catalog volumes.
- **Secrets** (`dbutils.secrets`): Access secrets through the same `DBUtils.getDBUtils()` call.

No other Databricks Utilities functionality is available for Scala projects. The `DBUtils` class belongs to the [Databricks Utilities for Scala library](https://central.sonatype.com/artifact/com.databricks/databricks-dbutils-scala_2.12/versions). [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on this library, so you do not need to explicitly add it to your build file (`build.sbt`, `pom.xml`, or `build.gradle`). Authentication for DBUtils is determined through initializing the `DatabricksSession` class in your Databricks Connect project. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Create a File in a Volume

The following Scala example demonstrates automating a Unity Catalog volume by creating a file, reading its contents, and deleting it using `dbutils.fs`:

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

The volume path follows the Unity Catalog three-level namespace format: `/Volumes/<catalog>/<schema>/<volume>/<file>`. In this example, the file `zzz_hello.txt` is written, its content is printed via `head`, and then it is removed with `rm`. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites

- A running Databricks cluster with [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) or above.
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) properly [installed and configured](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install).
- The target Unity Catalog volume must exist and the authenticated user must have write permissions on it.

## Related Concepts

- [DBUtils](/concepts/dbutilsnotebookrun.md) — General Databricks Utilities overview
- [Databricks Connect](/concepts/databricks-connect.md) — Remote execution for custom applications
- Unity Catalog Volumes — Storage volumes for non-tabular data
- DBFS — Distributed file system abstraction
- Secrets utility — Secure credential management

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
