---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a78a157a29a6407f9cae7bb9f61c49904f43031f67be5de30e6b8fba31cef39
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - client-server-decoupled-architecture
    - CDA
    - CUDA
    - Client-Server Model
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Client-Server Decoupled Architecture
description: The architectural pattern where Databricks Connect separates local client code execution from remote Spark DataFrame API execution on Databricks compute clusters.
tags:
  - architecture
  - distributed-computing
  - databricks
timestamp: "2026-06-19T18:08:39.193Z"
---

# Client-Server Decoupled Architecture

**Client-Server Decoupled Architecture** refers to a design pattern used by Apache Spark’s [Spark Connect] protocol, which separates the client API from the cluster execution engine. This architecture enables remote connectivity to Spark clusters using the DataFrame API, allowing code to run on the client while data transformations execute on a remote server. ^[databricks-connect-databricks-on-aws.md]

## Overview

In the decoupled client-server model, the client library is intentionally kept thin so that it can be embedded in various environments such as application servers, IDEs, notebooks, and programming languages. The underlying communication protocol uses Spark unresolved logical plans and [Apache Arrow] on top of [gRPC], a high-performance remote procedure call framework. ^[databricks-connect-databricks-on-aws.md]

This pattern is the foundation of [Databricks Connect] (for Databricks Runtime 13.3 LTS and above), which extends Spark Connect with additions to support Databricks compute modes and [Unity Catalog]. ^[databricks-connect-databricks-on-aws.md]

## Execution Model

The decoupled architecture defines specific boundaries for where different types of code run:

- **General code (Python, Scala) runs locally on the client** – This enables interactive debugging, as local logic executes without requiring remote resources. All non-Spark code is processed on the client side. ^[databricks-connect-databricks-on-aws.md]
- **DataFrame APIs execute on the remote server** – All data transformations are converted into Spark plans and sent to the remote Spark session for execution. Results are materialized back to the client only when commands such as `collect()`, `show()`, or `toPandas()` are called. ^[databricks-connect-databricks-on-aws.md]
- **User-defined functions (UDFs) run on the remote server** – UDFs defined locally are serialized and transmitted to the cluster where they execute. Other APIs that run user code remotely include `foreach`, `foreachBatch`, and `transformWithState`. ^[databricks-connect-databricks-on-aws.md]

## Dependency Management

The decoupled architecture splits dependency management between the two environments:

- **Application dependencies** (used by local code) must be installed on the local machine as part of the project, such as in a Python virtual environment. ^[databricks-connect-databricks-on-aws.md]
- **UDF dependencies** must be installed on the Databricks compute cluster. See the official documentation for managing UDF dependencies. ^[databricks-connect-databricks-on-aws.md]

## Use Cases

The client-server decoupled architecture enables two primary use cases:

1. **Interactive development and debugging from any IDE** – Developers can run and debug their code on Databricks compute using native IDE functionality. The Databricks Visual Studio Code extension leverages this architecture for debugging. ^[databricks-connect-databricks-on-aws.md]
2. **Building interactive data applications** – Just like a JDBC driver, the Databricks Connect library can be embedded in any application to interact with Databricks. It provides the full expressiveness of Python through PySpark, eliminating SQL programming language impedance mismatch and enabling data transformations with Spark on serverless scalable compute. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md) – The open-source gRPC-based protocol that implements this architecture
- [Databricks Connect](/concepts/databricks-connect.md) – The Databricks extension of Spark Connect
- DataFrame API – The primary interface for remote query execution
- Apache Arrow – Used for efficient data serialization
- gRPC – The transport protocol for client-server communication
- [Unity Catalog](/concepts/unity-catalog.md) – Supported by Databricks Connect
- [Visual Studio Code Extension for Databricks](/concepts/databricks-visual-studio-code-extension.md) – Uses this architecture for debugging
- Serverless Compute – One of the compute modes accessible through this architecture

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
