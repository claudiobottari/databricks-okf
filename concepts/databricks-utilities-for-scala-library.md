---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b722520bd64d948eb0848ef2c4537bddde22debe395745248b355a22b3c8584d
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-utilities-for-scala-library
    - DUFSL
    - Databricks Utilities for Scala
    - Databricks Utilities (DBUtils) for Scala
    - Databricks Utilities fs
    - dbutils Utilities
    - dbutils.library
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Utilities for Scala library
description: A published library (com.databricks/databricks-dbutils-scala_2.12) that provides Scala bindings for Databricks Utilities, with a dependency automatically declared by Databricks Connect for Scala.
tags:
  - databricks
  - scala
  - library
  - dependencies
timestamp: "2026-06-19T09:55:15.498Z"
---

```markdown
---
title: Databricks Utilities for Scala Library
summary: A Maven library (com.databricks:databricks-dbutils-scala_2.12) that provides Databricks Utilities functionality for Scala projects via Databricks Connect.
sources:
  - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:42:46.896Z"
updatedAt: "2026-06-18T15:10:31.453Z"
tags:
  - databricks-connect
  - scala
  - library
  - maven
aliases:
  - databricks-utilities-for-scala-library
  - DUFSL
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Utilities for Scala Library

The **Databricks Utilities for Scala library** provides access to Databricks Utilities (`dbutils`) functionality from Scala applications, including those using [[Databricks Connect]]. The library enables you to interact with the Databricks File System (DBFS) and secrets through the familiar dbutils API in Scala projects. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

The Databricks Utilities for Scala library is available as a Maven artifact from the [Sonatype Central Repository](https://central.sonatype.com/artifact/com.databricks/databricks-dbutils-scala_2.12/versions) under the coordinates `com.databricks:databricks-dbutils-scala_2.12`. It is designed to work with [[Databricks Connect for Scala]] for [[Databricks Runtime 13.3 LTS]] and above. The library allows Scala developers to automate file operations and secret management in their Databricks-connected applications. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available Functionality

When using [[databricks-connect-for-scala|Databricks Connect for Scala]], you access Databricks Utilities through the `DBUtils.getDBUtils` method. The library supports the following utilities: ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

- **DBFS utility** (`dbutils.fs`) — File system operations on the Databricks File System, including reading, writing, and deleting files.
- **Secrets utility** (`dbutils.secrets`) — Access to secrets stored in Databricks secret scopes.

No other Databricks Utilities functionality (such as `dbutils.widgets`, `dbutils.notebook`, etc.) is available for Scala projects through this library. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Dependency Management

[[databricks-connect-for-scala|Databricks Connect for Scala]] already declares a dependency on the Databricks Utilities for Scala library. You do **not** need to explicitly add this dependency to your Scala project's build file, whether you use `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle. The dependency is automatically included when you add Databricks Connect to your project. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in your Databricks Connect project for Scala. The library uses the same authentication configuration as your Databricks Connect session (e.g., OAuth, personal access token, or Azure managed identity). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Working with Unity Catalog Volumes

The following example demonstrates how to use the Databricks Utilities for Scala library to automate operations on a Unity Catalog volume. The example creates a file named `zzz_hello.txt` in the volume's path, reads the data from the file, and then deletes the file: ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

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

- [[Databricks Connect]] — The client library that enables connecting IDEs and custom applications to Databricks clusters.
- Databricks Utilities — The full set of dbutils utilities available in Databricks notebooks.
- Databricks File System (DBFS) — The distributed file system mounted into a Databricks workspace.
- Secrets — Sensitive credentials managed through Databricks secret scopes.
- Unity Catalog Volumes — Storage volumes managed by Unity Catalog for file-based data.
- [[Databricks Utilities with Databricks Connect|Databricks Utilities with Databricks Connect for Python]] — The Python equivalent of this library.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
```

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
