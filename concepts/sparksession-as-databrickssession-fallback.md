---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 055d3337cc6d6439cee00dd0d8ecc0399c01fe37d60124d8dc8eef69c8b56411
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparksession-as-databrickssession-fallback
    - SADF
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: SparkSession as DatabricksSession Fallback
description: A pattern for using org.apache.spark.sql.SparkSession directly (instead of DatabricksSession) when the DatabricksSession class is unavailable, relying on SPARK_REMOTE for authentication.
tags:
  - databricks
  - scala
  - fallback
timestamp: "2026-06-19T09:15:47.417Z"
---

---
title: SparkSession as [DatabricksSession](/concepts/databrickssession.md) Fallback
summary: Using SparkSession as a fallback when [DatabricksSession](/concepts/databrickssession.md) is unavailable in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), typically leveraging the SPARK_REMOTE environment variable for authentication.
sources:
  - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:40:00.000Z"
updatedAt: "2026-06-18T11:40:00.000Z"
tags:
  - databricks-connect
  - scala
  - spark-session
  - fallback
aliases:
  - sparksession-as-databrickssession-fallback
  - SASDF
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# SparkSession as [DatabricksSession](/concepts/databrickssession.md) Fallback

**SparkSession as [DatabricksSession](/concepts/databrickssession.md) Fallback** refers to the pattern of using the standard Apache Spark `SparkSession` class in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) when the Databricks-specific `DatabricksSession` class is unavailable. This fallback enables existing code or environments that cannot use `DatabricksSession` to still connect to a Databricks cluster.

## Overview

In Databricks Connect, the preferred entry point is `DatabricksSession` (provided by the `com.databricks.connect` package). However, some applications, IDEs, or custom integrations may not have access to `DatabricksSession`, or they may rely on a generic `SparkSession` pattern. The fallback approach uses `SparkSession.builder().getOrCreate()` instead of `DatabricksSession.builder().getOrCreate()`. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## How It Works

When using `SparkSession` as a fallback, the connection to the Databricks cluster is typically configured via the `SPARK_REMOTE` environment variable. This variable contains the connection string that the [Spark Connect](/concepts/spark-connect.md) client uses to reach the remote Databricks cluster. The example in the Databricks documentation shows the following pattern: ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
import org.apache.spark.sql.{DataFrame, SparkSession}

object Main {
  def main(args: Array[String]): Unit = {
    getTaxis(getSpark()).show(5)
  }

  private def getSpark(): SparkSession = {
    SparkSession.builder().getOrCreate()
  }

  private def getTaxis(spark: SparkSession): DataFrame = {
    spark.read.table("samples.nyctaxi.trips")
  }
}
```

In this example:
- `getSpark()` returns a `SparkSession` using the default builder.
- The `SPARK_REMOTE` environment variable must be set beforehand (e.g., through [Databricks Connect Client Setup](/concepts/databricks-connect-client-setup.md)).
- The returned `SparkSession` behaves like a remote session, reading tables directly from the Databricks cluster.

## When to Use the Fallback

The fallback is useful when:

- The `DatabricksSession` class is not available in the project dependencies or runtime environment.
- Code is written generically to work with any `SparkSession` and should be reused across local Spark and Databricks Connect without modification.
- Authentication is handled externally via `SPARK_REMOTE` or other Spark Connect configuration mechanisms.

## Limitations

Using `SparkSession` directly means you cannot use methods or properties that are only available on `DatabricksSession`, such as built-in integration with Databricks Unity Catalog metadata or Databricks-specific optimizations. For full functionality, `DatabricksSession` is recommended. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [DatabricksSession](/concepts/databrickssession.md) – The preferred entry point for Databricks Connect.
- [Spark Connect](/concepts/spark-connect.md) – The protocol underlying remote Spark sessions.
- [Databricks Connect Client Setup](/concepts/databricks-connect-client-setup.md) – Configuration steps, including setting `SPARK_REMOTE`.
- Code examples for Databricks Connect for Scala – The source article containing this pattern.

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)
