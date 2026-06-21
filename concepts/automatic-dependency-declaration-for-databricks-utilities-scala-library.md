---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8314602139f8834928f14e2a0d6126ca36673330d18fd51fa484b61bd939e306
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-dependency-declaration-for-databricks-utilities-scala-library
    - ADDFDUSL
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Automatic Dependency Declaration for Databricks Utilities Scala Library
description: Databricks Connect for Scala automatically declares a dependency on the Databricks Utilities for Scala library, so no explicit build file configuration is needed
tags:
  - databricks
  - scala
  - dependency-management
timestamp: "2026-06-19T18:15:52.152Z"
---

## Automatic Dependency Declaration for Databricks Utilities Scala Library

**Automatic Dependency Declaration for Databricks Utilities Scala Library** refers to the built-in behavior of [Databricks Connect](/concepts/databricks-connect.md) for Scala that eliminates the need for users to explicitly add the Databricks Utilities for Scala library as a dependency in their project build files. This simplifies project setup and ensures compatibility between the client and the remote Databricks cluster.

## Background

Databricks Utilities (`dbutils`) is a set of utilities for interacting with Databricks workspaces, including the Databricks File System (DBFS) and secrets. When using [Databricks Connect](/concepts/databricks-connect.md) for Scala, the client library already declares a dependency on the Databricks Utilities for Scala library. As a result, developers do **not** need to add that dependency manually in their build files—such as `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Scope of Available Utilities

Only a subset of Databricks Utilities is accessible through this automatic declaration. Specifically, `DBUtils.getDBUtils` provides access to DBFS file operations and the Secrets Utility (`dbutils.secrets`). No other Databricks Utilities (e.g., widgets, notebook-scoped libraries) are available for Scala projects via Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication

Authentication for the Databricks Utilities for Scala library is handled through the initialization of the `DatabricksSession` class in the Databricks Connect project. Once the session is established, the utilities can be used without additional authentication steps. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example Usage

The following example demonstrates using the automatically available `DBUtils` to create, read, and delete a file in a [Unity Catalog](/concepts/unity-catalog.md) volume:

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

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that automatically declares the dependency.
- Databricks Utilities — The suite of utilities for Databricks workspaces.
- DBFS — The distributed file system accessible through the utilities.
- Secrets Utility — The utility for managing secrets.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance platform for data and AI assets, used for the volume example.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
