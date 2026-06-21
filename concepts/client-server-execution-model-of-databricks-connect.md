---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 61c4d9050a2130dfbf21acdad8259dea5e0a063fafc79f138f1f1ab7c36c65d4
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - client-server-execution-model-of-databricks-connect
    - CEMODC
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Client-Server Execution Model of Databricks Connect
description: A decoupled architecture where general code runs locally for interactive debugging, DataFrame APIs execute remotely on Databricks compute, and UDFs are serialized and transmitted to the cluster.
tags:
  - architecture
  - execution-model
  - client-server
  - databricks
timestamp: "2026-06-19T14:44:56.209Z"
---

# Client-Server Execution Model of Databricks Connect

The **Client-Server Execution Model of Databricks Connect** describes how code and data processing are split between a local client environment and remote Databricks Compute when using the [Databricks Connect](/concepts/databricks-connect.md) library. This architecture is built on open-source [Spark Connect](/concepts/spark-connect.md), which enables remote connectivity to Spark clusters using the DataFrame API through a decoupled client-server design. ^[databricks-connect-databricks-on-aws.md]

## Architecture Overview

Databricks Connect uses a gRPC-based protocol that communicates unresolved logical plans and Apache Arrow data between the client and server. This thin client API is designed to be embedded in various environments, including application servers, IDEs, notebooks, and programming languages. ^[databricks-connect-databricks-on-aws.md]

The client-server model divides execution across three categories of code, each running in a different location.

## Where Code Runs

### General Code (Local Execution)

Python and Scala code that is not related to Spark DataFrames runs on the client side. This includes standard programming logic, control flow, and data manipulation that does not involve Spark APIs. Running locally enables interactive debugging and rapid development cycles. ^[databricks-connect-databricks-on-aws.md]

### DataFrame APIs (Remote Execution on Databricks Compute)

All data transformations using Spark DataFrame APIs are converted to Spark unresolved logical plans and transmitted to the remote Databricks compute cluster. The Spark session on the cluster executes these plans. Results are materialized back to the local client only when using commands such as `collect()`, `show()`, or `toPandas()`. ^[databricks-connect-databricks-on-aws.md]

### User-Defined Functions (UDFs) (Remote Execution)

User-defined functions (UDFs) defined locally are serialized and transmitted to the Databricks compute cluster, where they execute alongside Spark tasks. This applies to:
- User-Defined Functions (UDFs)
- `foreach` and `foreachBatch` operations
- `transformWithState` operations

^[databricks-connect-databricks-on-aws.md]

## Dependencies Management

The client-server model requires different approaches for managing dependencies:

- **Application dependencies**: Must be installed on the local machine as part of the project, such as within a Python virtual environment. These run locally.
- **UDF dependencies**: Must be installed on the Databricks cluster so that serialized UDFs can execute correctly. See the documentation on managing [UDF Dependencies](/concepts/udf-dependency-sources.md). ^[databricks-connect-databricks-on-aws.md]

## Relationship to Spark Connect

For Databricks Runtime 13.3 LTS and above, Databricks Connect extends [Spark Connect](/concepts/spark-connect.md) with additions and modifications to support Databricks compute modes and [Unity Catalog](/concepts/unity-catalog.md). Spark Connect is the open-source gRPC-based protocol within Apache Spark that enables remote DataFrame API execution. ^[databricks-connect-databricks-on-aws.md]

## Use Cases

This execution model supports two primary use cases:

- **Interactive development and debugging from any IDE**: Developers can write Spark code using native IDE functionality while executing it remotely on Databricks compute. The [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md) uses this model to provide built-in debugging. ^[databricks-connect-databricks-on-aws.md]
- **Building interactive data applications**: Like a JDBC driver, the Databricks Connect library can be embedded in any application to interact with Databricks, providing the full expressiveness of Python through PySpark without SQL impedance mismatch. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md)
- [Databricks Connect](/concepts/databricks-connect.md)
- Databricks Compute
- [Unity Catalog](/concepts/unity-catalog.md)
- User-Defined Functions (UDFs)
- Apache Arrow
- gRPC
- [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
