---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d26341ddc0208d911ef69ebc49cf511e3d3d7569e09a1ce03fdcc6ef2066c85b
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-udf-serialization
    - DCUS
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Databricks Connect UDF Serialization
description: The mechanism by which locally-defined user-defined functions (UDFs) are serialized and transmitted to the remote Databricks cluster for execution, along with related APIs like foreach, foreachBatch, and transformWithState.
tags:
  - databricks
  - udf
  - serialization
  - remote-execution
timestamp: "2026-06-19T09:46:33.908Z"
---

# Databricks Connect UDF Serialization

**Databricks Connect UDF Serialization** refers to the mechanism by which user-defined functions (UDFs) written in Python or Scala are automatically serialized on the client side and transmitted to the remote Databricks cluster for execution. This enables developers to define UDFs locally in an IDE or notebook and run them against distributed data on Databricks compute.

## How UDF Serialization Works

Databricks Connect is built on [Spark Connect](/concepts/spark-connect.md), which uses a decoupled client-server architecture based on gRPC. When a UDF is defined in local code, Databricks Connect serializes the function (its bytecode or source) and sends it as part of the unresolved logical plan to the remote Spark session. The UDF is then deserialized and executed on the Databricks cluster, not on the client machine.^[databricks-connect-databricks-on-aws.md]

This design allows general Python or Scala code to run locally (enabling interactive debugging) while all DataFrame transformations and UDF executions happen remotely. The serialization is transparent to the developer — standard UDF registration APIs work identically to a local Spark session.^[databricks-connect-databricks-on-aws.md]

## APIs That Run User Code on Databricks

The following APIs trigger the serialization and remote execution of user-defined code:^[databricks-connect-databricks-on-aws.md]

- **UDFs** – Functions registered via `pyspark.sql.functions.udf` or `udf` decorator.
- **`foreach`** – Applies a function to each row of a DataFrame.
- **`foreachBatch`** – Applies a function to each micro-batch in a streaming query.
- **`transformWithState`** – Applies a stateful transformation on streaming data.

All these APIs serialize the provided function and send it to the Databricks cluster for execution.

## Dependency Management for UDFs

While application dependencies (e.g., libraries used in local code) must be installed in the local Python environment, **UDF dependencies** — libraries that the serialized UDF code relies on — must be pre-installed on the Databricks cluster. Databricks recommends configuring these dependencies through cluster libraries or by using the Databricks Runtime’s package management. For details, refer to the official documentation on Manage UDF Dependencies.^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library enabling remote execution.
- [Spark Connect](/concepts/spark-connect.md) – The open-source gRPC protocol underlying Databricks Connect.
- User-Defined Functions (UDFs) – Functions applied to DataFrame rows.
- Databricks Compute – The remote Spark cluster that executes UDFs.
- Manage UDF Dependencies – Guidance on installing libraries needed by UDFs.

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
