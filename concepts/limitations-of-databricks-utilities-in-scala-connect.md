---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08da35f11cb4aaab1d6189fbf75e6b5d294212adce3e877b74e69e0e622e95c9
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-databricks-utilities-in-scala-connect
    - LODUISC
    - limited-databricks-utilities-support-in-scala-connect
    - LDUSISC
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Limitations of Databricks Utilities in Scala Connect
description: When using Databricks Connect for Scala, only DBFS and secrets utilities are available through DBUtils.getDBUtils; no other Databricks Utilities functionality is accessible.
tags:
  - databricks
  - scala
  - limitations
timestamp: "2026-06-19T14:55:11.723Z"
---

# Limitations of Databricks Utilities in Scala Connect

**Limitations of Databricks Utilities in Scala Connect** refers to the restricted subset of Databricks Utilities functionality available when using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). Unlike the Python counterpart, which offers full access to all Databricks Utilities, the Scala implementation has significant constraints that developers must consider when designing their workflows.

## Available Functionality

When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), you can access Databricks Utilities through the `DBUtils.getDBUtils` method, which belongs to the [Databricks Utilities for Scala library](https://central.sonatype.com/artifact/com.databricks/databricks-dbutils-scala_2.12/versions). This provides access to two specific utilities:

- **Databricks File System (DBFS)** – File operations such as creating, reading, and deleting files in volumes and other DBFS paths.
- **Secrets** – Accessing stored secrets through the `dbutils.secrets` utility.

^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Unavailable Functionality

**No Databricks Utilities functionality other than DBFS and secrets is available for Scala projects.** This means the following commonly used utilities are **not supported** in Scala Connect:

- Widgets (`dbutils.widgets`)
- Notebook workflow utilities (`dbutils.notebook`)
- Job task utilities
- Any other Databricks Utilities not explicitly listed as available

^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Key Limitations Summary

| Aspect | Limitation |
|--------|-----------|
| **Available utilities** | Only DBFS and secrets |
| **Unavailable utilities** | Widgets, notebook workflow, job tasks, and all others |
| **Python vs. Scala parity** | Python Connect offers full Databricks Utilities; Scala Connect is restricted |
| **Library dependency** | Declared automatically — no explicit build file changes needed |

## Important Considerations

### Implicit Dependency Declaration

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities for Scala library. You **do not need** to explicitly declare this dependency in your Scala project's build file (such as `build.sbt` for `sbt`, `pom.xml` for Maven, or `build.gradle` for Gradle). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

### Authentication

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in your Databricks Connect project for Scala. This means you must properly set up your [Databricks Connect client configuration](/concepts/databricks-connect-configuration.md) before using `DBUtils.getDBUtils`. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

### Comparison with Python

For the Python version of Databricks Connect, see [Databricks Utilities with Databricks Connect for Python](/concepts/databricks-utilities-with-databricks-connect.md), which offers full access to all Databricks Utilities without the limitations described here. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Working Within the Limitations

The following example demonstrates using the available DBFS functionality to create, read, and delete a file in a Unity Catalog volume:

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

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – The client library that enables connecting IDEs to Databricks clusters.
- Databricks Utilities – The full suite of notebook utilities available on Databricks.
- [Databricks Utilities with Databricks Connect for Python](/concepts/databricks-utilities-with-databricks-connect.md) – The Python equivalent with full utility support.
- DBFS (Databricks File System) – The distributed file system accessible through the available utilities.
- [Secrets Utility (dbutils.secrets)](/concepts/databricks-utilities-dbutils-via-connect.md) – The secrets management utility available in Scala Connect.
- Unity Catalog Volumes – Non-tabular data storage accessible via DBFS utilities.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
