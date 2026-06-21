---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a18b215bea77d44e24929b9e728544eb213bbe1596551bd2f2fe5c7030822475
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-authentication-for-dbutils
    - DAFD
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: DatabricksSession Authentication for DBUtils
description: Authentication for the Databricks Utilities for Scala library is determined through initialization of the DatabricksSession class in a Databricks Connect for Scala project.
tags:
  - databricks
  - authentication
  - scala
  - session
timestamp: "2026-06-18T15:10:37.249Z"
---

# [DatabricksSession](/concepts/databrickssession.md) Authentication for DBUtils

**DatabricksSession Authentication for DBUtils** refers to the authentication mechanism used to access Databricks Utilities (DBUtils) Secrets and Databricks File System (DBFS) functionality through the Databricks Utilities for Scala library in a [Databricks Connect](/concepts/databricks-connect.md) project. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

The Databricks Utilities for Scala library, published as `com.databricks:databricks-dbutils-scala_2.12`, provides access to DBFS operations and secrets via the `DBUtils.getDBUtils()` method. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication Mechanism

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in your Databricks Connect project for Scala. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

The session initialization sets up the authentication context that the DBUtils library uses when making API calls to the Databricks workspace. Without a properly configured `DatabricksSession`, calls to `DBUtils.getDBUtils()` will fail due to missing authentication credentials. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Scope

This authentication mechanism specifically governs access to:

- Databricks File System (DBFS) operations, such as `dbutils.fs.put()`, `dbutils.fs.head()`, and `dbutils.fs.rm()`. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]
- Secrets utility operations (`dbutils.secrets`). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

No other Databricks Utilities functionality beyond DBFS and secrets is available for Scala projects through this library. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Code Example

The following example demonstrates basic usage after authentication is established:

```scala
import com.databricks.sdk.scala.dbutils.DBUtils

object Main {
  def main(args: Array[String]): Unit = {
    val dbutils = DBUtils.getDBUtils()
    
    dbutils.fs.put(
      file = "/Volumes/main/default/my-volume/zzz_hello.txt",
      contents = "Hello, Databricks!",
      overwrite = true
    )
    
    println(dbutils.fs.head(filePath))
    dbutils.fs.rm(filePath)
  }
}
```

## Dependency Management

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities for Scala library, so you do not need to explicitly declare this dependency in your Scala project's build file (such as `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The framework for connecting IDEs and applications to Databricks clusters.
- Databricks Utilities – The full set of utility functions available in Databricks notebooks.
- [Databricks Session](/concepts/databrickssession.md) – The authentication session object that configures credentials for SDK clients.
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – The Python equivalent of this authentication mechanism.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
