---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef2d39afb1becf20be3836862c34b68a2227b8a80199c0de7ca581965a28f65b
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volume-file-operations-via-databricks-utilities-scala
    - UCVFOVDUS
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Unity Catalog Volume file operations via Databricks Utilities Scala
description: Example pattern showing how to use dbutils.fs.put, dbutils.fs.head, and dbutils.fs.rm on Unity Catalog volume paths (e.g., /Volumes/main/default/my-volume/) in Databricks Connect for Scala.
tags:
  - databricks
  - unity-catalog
  - scala
  - file-operations
timestamp: "2026-06-19T14:55:14.600Z"
---

# Unity Catalog Volume File Operations via Databricks Utilities Scala

**Unity Catalog Volume file operations via Databricks Utilities Scala** refers to the capability of using Databricks Utilities (DBUtils) from a Scala application, running through [Databricks Connect](/concepts/databricks-connect.md), to create, read, and delete files inside a [Unity Catalog](/concepts/unity-catalog.md) volume. This allows automated, programmatic file management within governed data assets without requiring a notebook or cluster-attached session.

## Overview

Databricks Utilities provide a set of convenience functions for working with the Databricks environment. When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) (Databricks Runtime 13.3 LTS and above), you can access a subset of these utilities—specifically the DBFS file system commands and Secrets management—through the `DBUtils` object. This enables Scala applications to perform file operations directly on Unity Catalog volumes, which are a type of managed storage location within the Unity Catalog data governance model. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites

Before using DBUtils for volume operations:

- You must set up the [Databricks Connect](/concepts/databricks-connect.md) client for Scala. See the [installation guide](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) automatically declares a dependency on the `databricks-dbutils-scala` library; no explicit dependency declaration is needed in your build file (`build.sbt`, `pom.xml`, or `build.gradle`). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- Authentication is determined by initializing the `DatabricksSession` class in your Databricks Connect project. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available Utilities

In a Scala project, only the following two Databricks Utilities are accessible via `DBUtils.getDBUtils()`:

- **DBFS File System** (`dbutils.fs`) – supports commands such as `put`, `head`, `rm`, `ls`, `cp`, `mv`, and `mkdirs`.
- **Secrets** (`dbutils.secrets`) – for retrieving secrets stored in Databricks secret scopes.

No other Databricks Utilities are available for Scala projects. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Using DBUtils for Unity Catalog Volume File Operations

Unity Catalog volumes are mounted under the `/Volumes` path in the DBFS namespace. You can interact with them using the standard `dbutils.fs` methods, exactly as you would with any other DBFS path. The typical operations for managing files within a volume are:

- **`dbutils.fs.put(file, contents, overwrite)`** – Creates or overwrites a file with the given string contents.
- **`dbutils.fs.head(file)`** – Reads and returns the first portion of a file (default 65535 bytes).
- **`dbutils.fs.rm(file)`** – Deletes a file (or directory with recursive option).

All these methods operate on volume paths such as `/Volumes/main/default/my-volume/zzz_hello.txt`. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Create, Read, and Delete a File in a Volume

The following Scala example demonstrates using `DBUtils.getDBUtils()` to create a file in a Unity Catalog volume, read its contents, and then delete it.

```scala
import com.databricks.sdk.scala.dbutils.DBUtils

object Main {
  def main(args: Array[String]): Unit = {
    val filePath = "/Volumes/main/default/my-volume/zzz_hello.txt"
    val fileData = "Hello, Databricks!"

    val dbutils = DBUtils.getDBUtils()

    // Create the file (overwrite if exists)
    dbutils.fs.put(
      file = filePath,
      contents = fileData,
      overwrite = true
    )

    // Read and print the file contents
    println(dbutils.fs.head(filePath))

    // Delete the file
    dbutils.fs.rm(filePath)
  }
}
```

- `DBUtils.getDBUtils()` returns the singleton instance of the utilities object. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- The path must be the full volume path under `/Volumes`. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- After running, the file is removed from the volume, leaving no trace.

## Important Notes

- The volume file operations shown here work only when your Databricks Connect client is properly authenticated and connected to a Databricks cluster. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- This approach is supported for Databricks Runtime 13.3 LTS and above. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- If you need to work with volumes via the [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) or Python DBUtils, refer to the corresponding documentation.

## Related Concepts

- Databricks Utilities – Overview of all available utilities.
- [DBUtils](/concepts/dbutilsnotebookrun.md) – The Scala API for Databricks Utilities.
- [Databricks Connect](/concepts/databricks-connect.md) – How to connect external applications to Databricks clusters.
- Unity Catalog Volumes – Managed storage areas governed by Unity Catalog.
- [Data Governance with Unity Catalog](/concepts/ai-governance-unity-catalog.md) – Policies and permissions for volume access.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
