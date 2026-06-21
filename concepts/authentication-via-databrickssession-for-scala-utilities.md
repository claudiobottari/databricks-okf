---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8809c99ca1a30a051f5d6846ecab5451a71ead9c6e6d55ef7a491d298374cfec
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - authentication-via-databrickssession-for-scala-utilities
    - AVDFSU
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Authentication via DatabricksSession for Scala Utilities
description: Authentication for the Databricks Utilities for Scala library is determined through initializing the DatabricksSession class in a Databricks Connect project
tags:
  - databricks
  - scala
  - authentication
  - security
timestamp: "2026-06-19T18:16:25.481Z"
---

# Authentication via [DatabricksSession](/concepts/databrickssession.md) for Scala Utilities

When using Databricks Utilities with [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), the authentication mechanism for the Databricks Utilities for Scala library (including access to the Databricks File System (DBFS) and Secrets utility (dbutils.secrets)) is determined by initializing the `DatabricksSession` class within your Databricks Connect project. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## How Authentication Works

The `DatabricksSession` is the entry point for a Databricks Connect client in Scala. When you initialize a `DatabricksSession` (typically by providing connection details such as host, token, or cluster ID), the underlying SDK establishes an authenticated connection to the remote Databricks workspace. This session is then used by the Databricks Utilities for Scala library – specifically the `DBUtils.getDBUtils()` method – to authenticate requests to DBFS and secrets. No separate authentication configuration is required for the utilities themselves; they inherit the session's credentials. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Scope of Authentication

The authentication provided by `DatabricksSession` covers only the subset of Databricks Utilities that are accessible via `DBUtils.getDBUtils()` in Scala. According to the documentation, the only available utilities for Scala projects are the DBFS filesystem operations and the secrets utility. All other Databricks Utilities functionality (such as notebook widgets, job parameters, or filesystem mounts) is not exposed in the Scala API and therefore does not require authentication through this mechanism. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Usage Example

The following example shows how a `DatabricksSession` (implicitly used via `DBUtils.getDBUtils()`) authenticates file system operations. The code creates a file in a Unity Catalog volume, reads its contents, and deletes it – all actions that depend on the session's authentication context.

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

In this example, `DBUtils.getDBUtils()` relies on the `DatabricksSession` that was initialized earlier in the Databricks Connect setup. The session’s credentials are used to authenticate the `fs.put`, `fs.head`, and `fs.rm` calls against the remote workspace. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Relationship to Databricks Connect Setup

To use authentication via `DatabricksSession`, you must first set up the Databricks Connect client for Scala. This involves installing the client library, configuring a `DatabricksSession` (or using environment variables), and ensuring the session is initialized before calling any `DBUtils` methods. [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities for Scala library, so you do not need to add that dependency manually. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## See Also

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that enables remote execution against Databricks clusters.
- [Databricks Connect for Scala Setup](/concepts/databricks-connect-for-scala.md) – Steps to configure the client and initialize a session.
- [DBUtils](/concepts/dbutilsnotebookrun.md) – The Scala API wrapper for Databricks Utilities.
- Databricks File System (DBFS) – A distributed filesystem mounted on Databricks workspaces.
- Secrets utility (dbutils.secrets) – Utility for managing sensitive information.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
