---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9803e6419e5206eab179a6561ae70c574617027a67a785aff38514319feaca3
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-execution-model
    - DCEM
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Databricks Connect Execution Model
description: The architecture where general Python/Scala code runs locally on the client, DataFrame APIs execute on the remote Databricks compute, and UDF code is serialized and transmitted to the cluster for execution.
tags:
  - databricks
  - architecture
  - code-execution
timestamp: "2026-06-19T09:46:12.356Z"
---

# Databricks Connect Execution Model

**Databricks Connect** is a client library for the Databricks Runtime that enables you to write Spark code in local development environments and execute it remotely on Databricks compute, using a decoupled client-server architecture based on the open-source [Spark Connect](https://spark.apache.org/spark-connect/) protocol. ^[databricks-connect-databricks-on-aws.md]

## How It Works

Databricks Connect uses Spark Connect, which has a decoupled client-server architecture for Apache Spark that allows remote connectivity to Spark clusters using the DataFrame API. The underlying protocol uses Spark unresolved logical plans and Apache Arrow on top of gRPC. The client API is designed to be thin so that it can be embedded in application servers, IDEs, notebooks, and programming languages. ^[databricks-connect-databricks-on-aws.md]

### Where Code Runs

The execution model follows a split execution pattern: ^[databricks-connect-databricks-on-aws.md]

- **General code runs locally**: Python and Scala code runs on the client side, enabling interactive debugging. All code is executed locally.
- **DataFrame APIs are executed on Databricks compute**: All data transformations are converted to Spark plans and run on the Databricks compute through the remote Spark session. Results are materialized on your local client when you use commands such as `collect()`, `show()`, or `toPandas()`.
- **UDF code runs on Databricks compute**: User-defined functions (UDFs) defined locally are serialized and transmitted to the cluster where they execute. APIs that run user code on Databricks include UDFs, `foreach`, `foreachBatch`, and `transformWithState`.

## Key Characteristics

### Client-Server Architecture

The architecture decouples the client application from the compute cluster: ^[databricks-connect-databricks-on-aws.md]

- **Client**: The local development environment (IDE, notebook, or custom application) that runs general code and sends DataFrame operations as unresolved logical plans over gRPC.
- **Server**: The Databricks compute that receives Spark plans, performs all data transformations, and returns results to the client.

### Dependency Management

Dependencies are managed separately for local and remote execution: ^[databricks-connect-databricks-on-aws.md]

- **Local dependencies**: Application dependencies that run locally must be installed as part of your project, such as in a Python virtual environment.
- **UDF dependencies**: Dependencies needed for UDF execution must be installed on Databricks.

## Capabilities

Using Databricks Connect, you can: ^[databricks-connect-databricks-on-aws.md]

- **Interactively develop and debug from any IDE**: Develop and debug code on Databricks compute using any IDE's native running and debugging functionality. The [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md) uses Databricks Connect to provide built-in debugging of user code on Databricks.
- **Build interactive data apps**: Like a JDBC driver, the Databricks Connect library can be embedded in any application to interact with Databricks. It provides the full expressiveness of Python through PySpark, eliminating SQL programming language impedance mismatch.

## Comparison with Local Execution

Unlike local Spark execution, Databricks Connect: ^[databricks-connect-databricks-on-aws.md]

| Aspect | Databricks Connect | Local Spark |
|--------|-------------------|-------------|
| Spark execution | Remote Databricks compute | Local machine |
| General code execution | Local client | Local machine |
| UDF execution | Remote cluster (serialized and transmitted) | Local machine |
| Debugging | Interactive debugging from IDE with local code execution | Local debugging only |
| Data transformations | Run on Databricks compute | Run on local hardware |
| Results retrieval | Materialized locally via `collect()`, `show()`, `toPandas()` | Available in local memory |

### Spark Connect Protocol

[Spark Connect](https://spark.apache.org/spark-connect/) is an open-source gRPC-based protocol within Apache Spark that allows remote execution of Spark workloads using the DataFrame API. For Databricks Runtime 13.3 LTS and above, Databricks Connect is an extension of Spark Connect with additions and modifications to support working with Databricks compute modes and [Unity Catalog](/concepts/unity-catalog.md). ^[databricks-connect-databricks-on-aws.md]

## Supported Environments

Databricks Connect supports: ^[databricks-connect-databricks-on-aws.md]

- [Python](/concepts/python-wheel-task.md) via PySpark (Databricks Connect for Python)
- R (Databricks Connect for R)
- Scala ([Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md))

IDEs and tools include:
- Visual Studio Code (with Databricks extension)
- PyCharm
- IntelliJ IDEA
- Jupyter Notebook
- Any custom application

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md) — The open-source protocol underlying Databricks Connect
- [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md) — IDE integration using Databricks Connect
- Databricks Compute — The remote execution environment
- Unresolved Logical Plan — The representation used in the gRPC protocol
- User-Defined Functions (UDFs) — Code that runs on the remote cluster
- gRPC — The transport protocol for Spark Connect

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
