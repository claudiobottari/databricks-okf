---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec2897ca2eeedf27211eb0e54696d193347bab3c1f241d7d195f8cd07e36d405
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - udf-execution-in-databricks-connect
    - UEIDC
    - User-defined functions (UDFs) in Databricks Connect
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: UDF Execution in Databricks Connect
description: User-defined functions (UDFs) defined locally are serialized and transmitted to the Databricks cluster for execution, requiring UDF dependencies to be installed on Databricks while application dependencies run locally.
tags:
  - udf
  - execution-model
  - dependencies
timestamp: "2026-06-18T15:02:50.919Z"
---

# UDF Execution in Databricks Connect

**UDF Execution in Databricks Connect** describes how user-defined functions (UDFs) are handled when using the Databricks Connect client library. Unlike general client‑side code or DataFrame API calls, UDFs are serialized on the client, transmitted to the remote Databricks compute, and executed there. This design ensures that UDFs benefit from the full compute power of the cluster while the rest of the application code remains debuggable locally. ^[databricks-connect-databricks-on-aws.md]

## How UDFs Are Executed

When you define a UDF (e.g., a Python `udf` or a Scala `udf`) in a Databricks Connect application, it is packaged and sent over the gRPC‑based [Spark Connect](/concepts/spark-connect.md) protocol to the remote cluster. The UDF code then runs on the Databricks compute nodes, not on the client machine. This is the same mechanism used for other APIs that execute user code on the cluster, including `foreach`, `foreachBatch`, and `transformWithState`. ^[databricks-connect-databricks-on-aws.md]

### Execution Model Overview

| Code type | Where it runs |
|-----------|---------------|
| General Python/Scala logic | Locally (client side) |
| DataFrame APIs (e.g., `select`, `filter`) | Remotely on Databricks compute |
| **UDFs, `foreach`, `foreachBatch`, `transformWithState`** | **Remotely on Databricks compute** |

The diagram from the source document illustrates this split: general code runs locally (enabling interactive debugging), DataFrame APIs are converted to Spark plans and execute remotely, and UDFs are shipped to the cluster for execution. ^[databricks-connect-databricks-on-aws.md]

## UDF Dependencies

Because UDFs run on the remote cluster, any libraries or dependencies that the UDF requires must be installed on the Databricks compute, not just on the local development environment. Databricks provides documentation on how to [manage UDF dependencies](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/udf#dependencies) (e.g., using cluster libraries or [Python Wheel Files](/concepts/python-wheel-files.md)). ^[databricks-connect-databricks-on-aws.md]

### Best Practices

- **Install UDF dependencies on the cluster**, not only locally. The local environment only needs dependencies that run client‑side code.
- **Test UDF serialization**: Ensure that your UDF functions are serializable (e.g., avoid local closures that capture non‑serializable objects).
- **Minimize UDF payload**: Keep the UDF code simple to reduce serialization overhead.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The overall client library for remote Spark execution.
- [Spark Connect](/concepts/spark-connect.md) – The open‑source gRPC protocol underlying Databricks Connect.
- User-Defined Functions (UDFs) – General overview of UDFs in Apache Spark.
- Vectorized UDFs – A more performant UDF variant (Pandas UDFs) that can also be used with Databricks Connect.
- [Dependency Management in Databricks](/concepts/dependency-management-in-databricks-connect.md) – How to install packages on clusters.

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
