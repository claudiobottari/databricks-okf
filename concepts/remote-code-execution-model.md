---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f5c0fc9e3ea0fe8b8be6b0dffce955a04c9170e1a54988d39763132f6df2590
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-code-execution-model
    - RCEM
    - Shell Command Execution
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Remote Code Execution Model
description: The execution model in Databricks Connect where general Python/Scala code runs locally on the client, DataFrame APIs execute on remote Databricks compute, and UDFs are serialized and run on the cluster.
tags:
  - execution-model
  - udf
  - dataframe-api
timestamp: "2026-06-18T11:33:19.012Z"
---

# Remote Code Execution Model

The **Remote Code Execution Model** describes the client-server architecture used by [Databricks Connect](/concepts/databricks-connect.md) to distribute computation between a local development environment and a remote Databricks cluster. In this model, general-purpose code runs locally on the client machine, while Spark DataFrame APIs and user-defined functions (UDFs) are executed on the remote Databricks compute, enabling interactive debugging and scalable data processing from any IDE or custom application. ^[databricks-connect-databricks-on-aws.md]

## Architecture

Databricks Connect is built on the open-source [Spark Connect](/concepts/spark-connect.md) protocol, which uses a decoupled client-server design. The underlying communication relies on Spark unresolved logical plans and Apache Arrow transmitted over gRPC. The client API is deliberately thin so that it can be embedded in application servers, IDEs, notebooks, and custom applications. ^[databricks-connect-databricks-on-aws.md]

## Code Execution Roles

The model clearly separates where different types of code run:

| Code Type | Execution Location | Notes |
|-----------|-------------------|-------|
| General Python/Scala code | Local client | Enables interactive debugging; all non-Spark logic runs locally |
| DataFrame APIs (e.g., `collect()`, `show()`, `toPandas()`) | Remote Databricks compute | Data transformations are converted to Spark plans and run remotely; results are materialised back to the client on demand |
| UDFs, `foreach`, `foreachBatch`, `transformWithState` | Remote Databricks compute | Locally defined functions are serialised and transmitted to the cluster for execution ^[databricks-connect-databricks-on-aws.md] |

## Dependency Management

Because code runs in two environments, dependencies must be managed separately:

- **Local dependencies**: Application packages required for client-side code (e.g., those used in a Python virtual environment) are installed on the local machine.
- **UDF dependencies**: Libraries needed by user-defined functions that run on the cluster must be installed on the remote Databricks compute. ^[databricks-connect-databricks-on-aws.md]

## Benefits

The model allows developers to use any IDE’s native debugging and running functionality while still leveraging the full power of the Spark engine on Databricks. It also eliminates SQL language impedance mismatch by providing the full expressiveness of Python (through PySpark) for data transformations, all executed on Databricks serverless or classic compute. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that implements this model
- [Spark Connect](/concepts/spark-connect.md) — The open-source gRPC protocol underlying the architecture
- DataFrame API — The set of operations executed remotely under this model
- User-Defined Functions (UDFs) — Code serialised and run on the remote cluster
- Databricks Runtime — The compute environment that receives remote execution requests
- [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md) — A tool that uses Databricks Connect for debugging

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
