---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef32123272a13e0b9fd65501db3d903d79f7dc3899ed905f06ccf1d7612de163
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-limitations-and-unsupported-features
    - Unsupported Features and Databricks Connect Limitations
    - DCLAUF
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect Limitations and Unsupported Features
description: The documented set of features and APIs that are not supported when using Databricks Connect, including Unity Catalog, Structured Streaming, Delta table native APIs, dbutils subsets, and table access control.
tags:
  - limitations
  - compatibility
timestamp: "2026-06-19T14:46:12.227Z"
---

# Databricks Connect Limitations and Unsupported Features

**Databricks Connect** is a client library that allows you to write Spark jobs locally and run them remotely on a Databricks cluster using Databricks Runtime 12.2 LTS and below. While it provides a powerful development workflow, certain features are not supported or have known limitations.

## Supported Databricks Runtime Versions

Databricks Connect is supported only on the following Databricks Runtime versions:

- Databricks Runtime 12.2 LTS / 12.2 LTS ML
- Databricks Runtime 11.3 LTS / 11.3 LTS ML
- Databricks Runtime 10.4 LTS / 10.4 LTS ML
- Databricks Runtime 9.1 LTS / 9.1 LTS ML
- Databricks Runtime 7.3 LTS

Any cluster running an unsupported runtime version cannot be used with Databricks Connect. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## General Limitations

- **Python version mismatch**: The minor Python version on the development machine must match the Python version on the cluster (e.g., both 3.9). Mismatches cause connectivity errors. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Conflicting PySpark installations**: The `databricks-connect` package conflicts with PySpark. PySpark must be uninstalled before installing `databricks-connect`. Failure to do so leads to “stream corrupted” or “class not found” errors. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Cluster configuration**: The cluster must have the Spark server enabled (`spark.databricks.service.server.enabled true`). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **File copy size limit**: When copying files between local and remote filesystems using `dbutils.fs.cp`, the maximum file size is 250 MB. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **`dbutils.secrets.get` disabled by default**: For security reasons, `dbutils.secrets.get` is disabled. To enable it, you must contact Databricks support. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Unsupported Features

The following features are **not supported** when using Databricks Connect:

- **[Unity Catalog](/concepts/unity-catalog.md)** – Connecting to a cluster that uses Unity Catalog is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **[Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)** – Running streaming queries is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Arbitrary non-Spark code execution on the remote cluster** – Only Spark jobs (jobs that go through the Spark API) are supported. General Python/Scala code is not executed remotely. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Native Delta table APIs (Python, Scala, R)** – Operations like `DeltaTable.forPath` are not supported. However, the SQL API (`spark.sql(...)`) with Delta Lake commands and the Spark API (`spark.read.load`) on Delta tables do work. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **`COPY INTO`** – The `COPY INTO` SQL command is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Server-side catalog UDFs** – SQL functions, Python UDFs, or Scala UDFs that are registered in the cluster’s permanent catalog are not supported. Locally defined UDFs (defined in the client session) work. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Apache Zeppelin 0.7.x and below** – Not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Clusters with [table access control](/concepts/table-access-control-tacl.md)** – Connecting to clusters with table access control enabled is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Clusters with process isolation enabled** – When `spark.databricks.pyspark.enableProcessIsolation` is set to `true`, Databricks Connect cannot connect. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Delta `CLONE` SQL command** – Not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Global temporary views** – Not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Koalas and `pyspark.pandas`** – The Koalas library and `pyspark.pandas` module are not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **`CREATE TABLE ... AS SELECT ...`** – This SQL command does not always work. The recommended alternative is `spark.sql("SELECT ...").write.saveAsTable("table")`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Specific Databricks Utilities** – The following dbutils modules are not supported:
  - `credentials`
  - `library`
  - `notebook workflow`
  - `widgets`
  - 
  ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **AWS Glue catalog** – Connecting to clusters that use the AWS Glue [Metastore](/concepts/metastore.md) is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **SparkR and sparklyr streaming/ML APIs** – When using SparkR or sparklyr via Databricks Connect, the following are unsupported: sparklyr streaming APIs, sparklyr ML APIs, broom APIs, `csv_file` serialization mode, and `spark submit`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- Databricks Connect for Databricks Runtime 12.2 LTS and below – Full setup guide and troubleshooting.
- Databricks Utilities – Supported commands for `dbutils.fs` and `dbutils.secrets`.
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md) – Alternative for GPU workloads.
- Databricks SQL Connector for Python – Recommended for SQL-only Python development.

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
