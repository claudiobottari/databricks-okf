---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c79938ad5fdfef15b579dcf1e04caa626572be8a42de6be6fe7d27eea945f22
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scala-databricks-utilities-limitation
    - SDUL
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Scala Databricks Utilities limitation
description: Only DBFS and secrets utilities are available through Databricks Utilities for Scala; no other Databricks Utilities functionality is supported.
tags:
  - databricks-connect
  - scala
  - limitations
timestamp: "2026-06-18T11:43:16.290Z"
---

---
title: Scala Databricks Utilities Limitation
summary: When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), only DBFS and secrets utilities are available through `DBUtils.getDBUtils`; all other Databricks Utilities are unsupported.
sources:
  - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:08:33.206Z"
updatedAt: "2026-06-18T11:08:33.206Z"
tags:
  - databricks
  - databricks-connect
  - scala
  - utilities
  - limitation
aliases:
  - scala-databricks-utilities-limitation
  - SDUL
  - databricks-utilities-limitation-scala
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# Scala Databricks Utilities Limitation

When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), access to Databricks Utilities is limited to only the DBFS and secrets utilities. No other Databricks Utilities functionality — such as `dbutils.widgets`, `dbutils.notebook`, `dbutils.fs` (beyond DBFS operations), or `dbutils.jobs` — is available in Scala projects. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

The Scala Databricks Utilities limitation applies to Databricks Runtime 13.3 LTS and above. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## What Is Available

### DBUtils.getDBUtils

You use `DBUtils.getDBUtils` from the [Databricks Utilities for Scala library](/concepts/databricks-utilities-for-scala-library.md) to access DBFS and secrets through Databricks Utilities. `DBUtils.getDBUtils` provides access to `dbutils.fs` (DBFS file operations) and `dbutils.secrets` (secret management). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

### Dependency Management

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities for Scala library, so you do not need to explicitly declare this dependency in your Scala project's build file (such as `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

### Authentication

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in your Databricks Connect project for Scala. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## What Is Not Available

No Databricks Utilities functionality other than DBFS and secrets is available for Scala projects when using Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

Unsupported utilities include:

- `dbutils.widgets` — Widget creation and retrieval
- `dbutils.notebook` — Notebook workflow control (run, exit, validate)
- `dbutils.jobs` — Job orchestration
- `dbutils.library` — Library management
- `dbutils.credentials` — Credential management
- `dbutils.data` — Data sharing
- `dbutils.fs` utilities beyond basic DBFS read/write operations (such as `mount`, `unmount`, `refreshMounts`)
- `dbutils.meta` — Metadata utilities

## Example: Working Within the Limitation

The following example shows the supported usage of DBFS file operations via `DBUtils.getDBUtils`. This example creates a file named `zzz_hello.txt` in a Unity Catalog volume, reads the data, and then deletes the file: ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

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

Any attempt to use unsupported utilities — such as `dbutils.widgets.text()` — will result in a compilation error, as the Databricks Utilities for Scala library exposes only the `fs` and `secrets` namespaces.

## Workarounds

### Using Python with Databricks Connect

If you need full Databricks Utilities access, consider using [Databricks Connect for Python](/concepts/databricks-connect-for-python.md), which supports all `dbutils` functionality: `dbutils.fs`, `dbutils.secrets`, `dbutils.widgets`, `dbutils.notebook`, `dbutils.jobs`, `dbutils.library`, `dbutils.credentials`, `dbutils.data`, and `dbutils.meta`. See [Databricks Utilities with Databricks Connect for Python](/concepts/databricks-utilities-with-databricks-connect.md).

### Using the Databricks REST API or SDK

For functionality not available through the Scala utilities library, you can use the [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) or [Databricks SDK for Scala](/concepts/databricks-connect-for-scala.md) to perform operations such as:

- **Job management**: Use the Jobs API (`POST /api/2.1/jobs/run-now`) instead of `dbutils.jobs`.
- **Notebook workflow**: Use the Notebooks API (`POST /api/2.0/workspace/import`) or the Databricks SDK's `workspace` client.
- **Widgets**: Use the Databricks REST API for notebook parameter passing.

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The client library that enables this limitation
- Databricks Utilities — The full set of utilities available in Databricks notebooks
- [Databricks Utilities for Scala library](/concepts/databricks-utilities-for-scala-library.md) — The library providing `DBUtils.getDBUtils`
- Databricks File System (DBFS) — The file system accessible through the available `fs` utility
- [Secrets Utility (dbutils.secrets)](/concepts/databricks-utilities-dbutils-via-connect.md) — The secret management utility available in Scala
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The Python counterpart with full utility support

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
