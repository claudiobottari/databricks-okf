---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b00299be87ff5aa0d57a488283b7ac10ae72f0a7cd3aeb1fda38425cf47db8e
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - decoupled-client-server-architecture
    - DCA
    - Decoupled Architecture
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Decoupled Client-Server Architecture
description: The architectural pattern underlying Databricks Connect where the client runs general code locally while Spark DataFrame operations are executed remotely on Databricks compute via Spark Connect.
tags:
  - architecture
  - client-server
  - distributed-computing
timestamp: "2026-06-18T11:33:07.599Z"
---

# Decoupled Client-Server Architecture

**Decoupled Client-Server Architecture** is a software design pattern in which the client and server components of a system operate as independent processes that communicate over a network protocol, rather than being tightly integrated in a single process space. In the context of Apache Spark and Databricks, this architecture enables remote connectivity to Spark clusters using the DataFrame API through the open-source [Spark Connect](/concepts/spark-connect.md) protocol. ^[databricks-connect-databricks-on-aws.md]

## Overview

In a decoupled client-server architecture, the client runs a thin API layer that translates API calls into network requests, while the server executes the actual computational work. This separation allows the client to be embedded in a wide variety of environments — including application servers, IDEs, notebooks, and different programming languages — without requiring a local Spark installation. ^[databricks-connect-databricks-on-aws.md]

## How It Works

The decoupled client-server architecture in [Databricks Connect](/concepts/databricks-connect.md) is built on Spark Connect, which uses a gRPC-based protocol for communication. The key design principles are: ^[databricks-connect-databricks-on-aws.md]

- **General code runs locally**: Python and Scala code executes on the client side, enabling interactive debugging with native IDE tools. ^[databricks-connect-databricks-on-aws.md]
- **DataFrame APIs execute remotely**: All data transformations are converted to Spark unresolved logical plans and transmitted over the protocol to the remote cluster. Results are materialized on the client only when commands such as `collect()`, `show()`, or `toPandas()` are called. ^[databricks-connect-databricks-on-aws.md]
- **UDF code runs on the server**: User-defined functions (UDFs) defined on the client are serialized and transmitted to the cluster where they execute. This applies to APIs such as UDFs, `foreach`, `foreachBatch`, and `transformWithState`. ^[databricks-connect-databricks-on-aws.md]

### Communication Protocol

The underlying protocol uses Spark unresolved logical plans and Apache Arrow on top of gRPC. This design keeps the client API thin so it can be embedded in diverse environments. ^[databricks-connect-databricks-on-aws.md]

## Benefits

- **IDE-native development**: Developers can write and debug Spark code from IDEs such as Visual Studio Code, PyCharm, and IntelliJ IDEA while running workloads on remote Databricks compute. ^[databricks-connect-databricks-on-aws.md]
- **Interactive data applications**: Like a JDBC driver, the client library can be embedded in any application to interact with Databricks, providing the full expressiveness of Python through PySpark and enabling all data transformations with Spark on serverless scalable compute. ^[databricks-connect-databricks-on-aws.md]
- **Separation of dependencies**: Application dependencies are installed locally for client-side code, while UDF dependencies are managed on the Databricks cluster. ^[databricks-connect-databricks-on-aws.md]

## Relationship to Spark Connect

For Databricks Runtime 13.3 LTS and above, Databricks Connect is an extension of the open-source [Spark Connect](/concepts/spark-connect.md) protocol with additions and modifications to support working with Databricks compute modes and [Unity Catalog](/concepts/unity-catalog.md). Spark Connect itself is an open-source gRPC-based protocol within Apache Spark that enables remote execution of Spark workloads using the DataFrame API. ^[databricks-connect-databricks-on-aws.md]

## Comparison with Traditional Architecture

| Aspect | Traditional Spark | Decoupled Client-Server |
|--------|------------------|------------------------|
| Client relationship | Tightly coupled to Spark session | Independent, network-connected |
| Code execution | All code runs in Spark process | General code runs locally, Spark code runs remotely |
| UDFs | Run in-process | Serialized and transmitted to server |
| Environment requirement | Requires local Spark installation | Thin client library only |

## Use Cases

- **Interactively develop and debug from any IDE**: Developers can use any IDE's native running and debugging functionality while executing code on Databricks compute. ^[databricks-connect-databricks-on-aws.md]
- **Build interactive data apps**: The client library can power custom applications that need to interact with Databricks, eliminating SQL programming language impedance mismatch by providing full PySpark expressiveness. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The Databricks implementation of this architecture
- [Spark Connect](/concepts/spark-connect.md) — The open-source protocol underlying decoupled client-server for Spark
- gRPC — The remote procedure call framework used for communication
- Apache Arrow — The columnar data format used in the protocol
- [Decoupled Architecture](/concepts/decoupled-client-server-architecture.md) — The general software pattern
- [Client-Server Model](/concepts/client-server-decoupled-architecture.md) — The foundational distributed computing model

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
