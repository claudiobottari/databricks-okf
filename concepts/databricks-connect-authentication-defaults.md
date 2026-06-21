---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b2907a0470589fc7b3e6477fcb8bda775130b35b5be7a272c26704f3220cf7a
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-connect-authentication-defaults
    - DCAD
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect authentication defaults
description: The default authentication mechanism used by Databricks Connect client setup, configurable via environment variables such as SPARK_REMOTE
tags:
  - databricks
  - authentication
  - security
timestamp: "2026-06-19T17:45:38.348Z"
---

# Databricks Connect authentication defaults

**Databricks Connect authentication defaults** refer to the standard authentication method used when connecting a remote client to a Databricks cluster via Databricks Connect. By default, the client uses the authentication configuration set up during the [Databricks Connect client installation](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install). ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Default authentication behavior

The code examples in the [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) documentation assume that you are using the **default authentication** that was configured during client setup. This typically involves using a Databricks personal access token or an OAuth token, combined with the workspace URL and cluster ID, stored in the `~/.databrickscfg` file or in environment variables. The exact mechanism depends on the Databricks Connect client version and the authentication provider configured. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Using `SPARK_REMOTE` environment variable

An alternative to the default authentication is to use the `SPARK_REMOTE` environment variable. When this variable is set, the `SparkSession` (or `DatabricksSession`) reads the connection string from `SPARK_REMOTE`, allowing the client to connect without relying on the default profile. This approach is useful when you need to override the default connection in scripts or CI/CD pipelines. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

The example that uses `SparkSession.builder().getOrCreate()` without explicitly passing a `DatabricksSession` demonstrates this pattern: the session builder picks up the `SPARK_REMOTE` variable if it is set, otherwise it falls back to the default authentication method. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Choosing between `DatabricksSession` and `SparkSession`

When using default authentication, the recommended practice is to use `DatabricksSession.builder().getOrCreate()` as shown in the main examples. However, if you need to use the `SparkSession` class directly (for example, when `DatabricksSession` is unavailable), the authentication is handled via the `SPARK_REMOTE` environment variable or the default Databricks Connect configuration. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The remote client library for connecting IDEs and applications to Databricks clusters.
- [DatabricksSession](/concepts/databrickssession.md) – The recommended entry point for Databricks Connect in Scala.
- SparkSession – The standard Spark entry point, also usable with Databricks Connect.
- SPARK_REMOTE Environment Variable|SPARK_REMOTE environment variable – An alternative authentication mechanism for Databricks Connect.
- Databricks authentication setup – General guidance on configuring authentication for Databricks tools.

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)
