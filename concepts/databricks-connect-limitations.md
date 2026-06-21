---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b52a52ebafc85e8bcd5c8d3ffa6dcd8cc25332ca4074414cb310cc9fa9388d6
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-limitations
    - DCL
    - Databricks Connect Validation
    - Databricks Connect for Python limitations
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect Limitations
description: Known limitations of Databricks Connect including lack of support for Unity Catalog, Structured Streaming, certain Delta table operations, Koalas, table access control, and various dbutils modules.
tags:
  - limitations
  - unsupported-features
timestamp: "2026-06-19T18:09:16.973Z"
---

# Databricks Connect Limitations

**Databricks Connect** is a client library for the Databricks Runtime that allows you to write jobs using Spark APIs and run them remotely on a Databricks cluster. While it enables local development with remote execution, several features and configurations are not supported when using Databricks Connect with Databricks Runtime 12.2 LTS and below. This page documents those limitations. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Version and Environment Requirements

Only the following Databricks Runtime versions are supported: Databricks Runtime 12.2 LTS, 11.3 LTS, 10.4 LTS, 9.1 LTS, and 7.3 LTS (including ML editions where applicable). The major and minor version of the `databricks-connect` package must exactly match the version of the cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The client requires Python 3 on the development machine, and the minor Python version must match the minor version on the cluster. Only Java Runtime Environment (JRE) 8 is supported; Java 11 is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The `databricks-connect` package conflicts with PySpark. Having both installed causes errors when initializing the Spark context in Python. PySpark must be uninstalled before installing Databricks Connect. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Feature and API Limitations

The following features and APIs are **not** supported by Databricks Connect:

- [Unity Catalog](/concepts/unity-catalog.md) – any security model or query routed through Unity Catalog.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – streaming workloads cannot be run through Databricks Connect.
- Running arbitrary code that is not part of a Spark job on the remote cluster.
- Native Scala, Python, and R APIs for [Delta Lake](/concepts/delta-lake.md) table operations (for example, `DeltaTable.forPath`). However, the SQL API (`spark.sql(...)`) with Delta Lake operations and the Spark API (for example, `spark.read.load`) on Delta tables are supported.
- `COPY INTO` SQL command.
- Using SQL functions, Python or Scala UDFs that are part of the server’s catalog. Locally introduced Scala and Python UDFs work.
- Apache Zeppelin 0.7.x and below.
- Connecting to clusters with [table access control](/concepts/table-access-control-tacl.md) (legacy ACLs).
- Connecting to clusters with process isolation enabled (where `spark.databricks.pyspark.enableProcessIsolation` is set to `true`).
- Delta `CLONE` SQL command.
- Global temporary views.
- Koalas and `pyspark.pandas`.
- `CREATE TABLE table AS SELECT ...` SQL commands do not always work. Instead, use `spark.sql("SELECT ...").write.saveAsTable("table")`.
- AWS Glue catalog.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Databricks Utilities (dbutils) Limitations

The following dbutils modules are **not** supported: credentials, library, notebook workflow, and widgets. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The `dbutils.secrets.get` capability is disabled by default for security reasons. Contact Databricks support to enable it. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

When copying files between local and remote filesystems using `dbutils.fs.cp`, the maximum file size that can be transferred is 250 MB. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Additional Limitations

A conflicting `SPARK_HOME` environment variable or PATH entries from previous Spark installations can cause errors, including “stream corrupted” or “class not found” errors. `SPARK_HOME` should be unset or pointed to the correct Databricks Connect path. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

On Windows, Hadoop `winutils.exe` must be configured; see the Hadoop on Windows guide for instructions. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)
- [Delta Lake](/concepts/delta-lake.md)
- dbutils
- [Table access control](/concepts/table-access-control-tacl.md)
- Koalas
- Apache Zeppelin

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
