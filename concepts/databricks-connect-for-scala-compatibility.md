---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b52cc5b070017ae764750c51e22e311961161458a50d6f5c78fc26499d5af306
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-for-scala-compatibility
    - DCFSC
    - databricks-connect-for-scala-runtime-compatibility
    - DCFSRC
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect for Scala Compatibility
description: This version of Databricks Connect for Scala requires Databricks Runtime 13.3 LTS and above
tags:
  - databricks
  - scala
  - versioning
  - compatibility
timestamp: "2026-06-19T18:16:26.566Z"
---

# [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) Compatibility

**Databricks Connect for Scala Compatibility** refers to the supported functionality and available Databricks Utilities when using Databricks Connect with Scala for Databricks Runtime 13.3 LTS and above. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available Databricks Utilities

When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), you access Databricks Utilities through `DBUtils.getDBUtils`, which belongs to the [Databricks Utilities for Scala](https://central.sonatype.com/artifact/com.databricks/databricks-dbutils-scala_2.12/versions) library. This provides access to the Databricks File System (DBFS) and secrets functionality. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Limitations

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) does not support the full set of Databricks Utilities. Only the DBFS and secrets utilities are available — no other Databricks Utilities functionality is accessible for Scala projects. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Dependency Management

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities for Scala library. You do not need to explicitly declare this dependency in your Scala project's build file, such as `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in your Databricks Connect project for Scala. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Creating a File in a Volume

The following example demonstrates using the Databricks Utilities for Scala library to automate a Unity Catalog volume. It creates a file named `zzz_hello.txt` in the volume's path within the workspace, reads the data from the file, and then deletes the file: ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

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

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The general framework for connecting IDEs and custom applications to Databricks clusters
- Databricks Utilities — The complete set of utilities available on Databricks
- Databricks File System (DBFS) — The distributed file system for Databricks
- Secrets — Secure credential management in Databricks
- Unity Catalog Volumes — Storage volumes managed by Unity Catalog
- Databricks Connect for Python Utilities — The Python equivalent of this functionality

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
