---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 942626065572f805de9e32f7a0b1749ff118fae93c9c60302a27f4d431db5333
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark_remote-environment-variable-authentication
    - SEVA
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
    - file: inferred from source context
title: SPARK_REMOTE environment variable authentication
description: A configuration method for Databricks Connect where the SPARK_REMOTE environment variable provides connection and authentication details without explicit code configuration.
tags:
  - databricks
  - authentication
  - configuration
timestamp: "2026-06-19T14:14:33.939Z"
---

# SPARK_REMOTE Environment Variable Authentication

**SPARK_REMOTE environment variable authentication** is a mechanism used by [Databricks Connect](/concepts/databricks-connect.md) to authenticate and connect to a remote Databricks cluster. When the `SPARK_REMOTE` environment variable is set, applications can create a standard `SparkSession` without requiring the `DatabricksSession` wrapper, and the connection to the remote cluster is configured automatically.

## Overview

Databricks Connect traditionally uses the `DatabricksSession` builder to establish a connection to a Databricks cluster. As an alternative, you can rely on the `SPARK_REMOTE` environment variable. By setting this variable before launching your application, the `SparkSession.builder().getOrCreate()` call can connect directly to the remote cluster, simplifying code that must work in environments where `DatabricksSession` is not available. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Usage

The typical pattern is to set the `SPARK_REMOTE` environment variable with the connection details (e.g., the Databricks cluster URL, token, and other parameters). Then, in your Scala code, you create a standard `SparkSession`:

```scala
import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder().getOrCreate()
val df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

This approach eliminates the need to import `com.databricks.connect.DatabricksSession` and is useful in scenarios where the `DatabricksSession` class is not available (e.g., in certain IDE integrations or legacy codebases). ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## How It Works

The `SPARK_REMOTE` environment variable encodes the connection string for the remote Spark cluster. The Spark session builder reads this variable at initialization time and configures the remote endpoint, authentication token, and any other necessary settings automatically. The exact format of the variable is determined by the Databricks Connect client configuration (see [Databricks Connect Client Setup](/concepts/databricks-connect-client-setup.md)). ^[inferred from source context]

## Benefits

- **Simplifies code** – Removes the dependency on `DatabricksSession` and its builder.
- **Portability** – Allows the same Spark code to run locally or connect to a remote Databricks cluster by toggling the environment variable.
- **Compatibility** – Useful for unit testing or when integrating with frameworks that expect a plain `SparkSession`.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The overall remote connectivity framework.
- [DatabricksSession](/concepts/databrickssession.md) – The recommended entry point for Databricks Connect, which can be replaced by `SPARK_REMOTE`.
- SparkSession – The standard Spark entry point used in both local and remote modes.
- [Databricks Connect Authentication](/concepts/databricks-connect-authentication.md) – Other methods of authenticating to a Databricks cluster (e.g., OAuth, personal access tokens).
- Code examples for Databricks Connect for Scala – The source document that demonstrates this pattern.

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)
2. inferred from source context
