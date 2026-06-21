---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30494bdc6aaf1be6d2d8e971b558d2cf4719ec038df878710fd01c3f911a051c
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - client-server-architecture-for-spark
    - CAFS
    - Client-Server Architecture in Spark
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Client-Server Architecture for Spark
description: A decoupled architecture for Apache Spark using Spark Connect that allows remote connectivity to Spark clusters via unresolved logical plans and Apache Arrow over gRPC, enabling thin embedded clients.
tags:
  - architecture
  - apache-spark
  - remote-connectivity
timestamp: "2026-06-19T09:46:14.912Z"
---

# Client-Server Architecture for Spark

**Client-Server Architecture for Spark** refers to the decoupled architecture introduced by [Spark Connect](/concepts/spark-connect.md) that enables remote connectivity to Spark clusters using the DataFrame API. This architecture separates the client and server components, allowing Spark workloads to be executed remotely from various environments including IDEs, notebooks, and custom applications.

## Overview

Traditional Spark architectures require the driver program to run within the same process as the Spark session. The client-server architecture, built on Spark Connect, decouples these components. The client API is designed to be thin so it can be embedded in application servers, IDEs, notebooks, and programming languages. The underlying protocol uses Spark unresolved logical plans and Apache Arrow on top of gRPC. ^[databricks-connect-databricks-on-aws.md]

## How It Works

In the client-server architecture for Spark, code execution is distributed between the client and server:

- **General code runs locally**: Python and Scala code executes on the client side, enabling interactive debugging. All non-Spark code runs locally while Spark code runs on the remote cluster. ^[databricks-connect-databricks-on-aws.md]
- **DataFrame APIs execute on Databricks compute**: All data transformations are converted to Spark plans and run on the remote Spark session. Results are materialized on the local client when using commands such as `collect()`, `show()`, or `toPandas()`. ^[databricks-connect-databricks-on-aws.md]
- **UDF code runs on Databricks compute**: User-defined functions (UDFs) defined locally are serialized and transmitted to the cluster where they execute. APIs that run user code on Databricks include UDFs, `foreach`, `foreachBatch`, and `transformWithState`. ^[databricks-connect-databricks-on-aws.md]

## Databricks Connect

[Databricks Connect](/concepts/databricks-connect.md) is a client library for the Databricks Runtime that implements this client-server architecture. It is built on open-source Spark Connect with additions and modifications to support working with Databricks compute modes and [Unity Catalog](/concepts/unity-catalog.md). Databricks Connect is available for Python, R, and Scala. ^[databricks-connect-databricks-on-aws.md]

### Capabilities

Using Databricks Connect, developers can write code using Spark APIs and run them remotely on Databricks compute instead of in a local Spark session. This enables:

- **Interactive development and debugging from any IDE**: Developers can develop and debug code on Databricks compute using any IDE's native running and debugging functionality. The [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md) uses Databricks Connect to provide built-in debugging of user code on Databricks. ^[databricks-connect-databricks-on-aws.md]
- **Interactive data applications**: Like a JDBC driver, the Databricks Connect library can be embedded in any application to interact with Databricks. It provides the full expressiveness of Python through PySpark, eliminating SQL programming language impedance mismatch. ^[databricks-connect-databricks-on-aws.md]

## Dependencies Management

The client-server architecture requires different dependency management strategies for client-side and server-side code:

- **Application dependencies** must be installed on the local machine, as they run locally as part of the project environment (such as a Python virtual environment). ^[databricks-connect-databricks-on-aws.md]
- **UDF dependencies** must be installed on Databricks compute, as UDFs are serialized and transmitted to the cluster for execution. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md) — The open-source gRPC-based protocol enabling remote Spark execution
- [Databricks Connect](/concepts/databricks-connect.md) — The Databricks implementation of Spark Connect
- Apache Spark DataFrame API — The primary API used in the client-server architecture
- gRPC — The transport protocol for Spark Connect
- Apache Arrow — The data serialization format used in the protocol
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks metadata layer supported by Databricks Connect

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
