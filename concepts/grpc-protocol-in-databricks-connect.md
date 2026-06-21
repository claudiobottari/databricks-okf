---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 249a361643a4da8162369910ec926f20c1d0a2a5b4db423b88424335de260b8e
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grpc-protocol-in-databricks-connect
    - GPIDC
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: gRPC Protocol in Databricks Connect
description: The underlying communication protocol used by Spark Connect that transmits Spark unresolved logical plans and Apache Arrow data over gRPC between the client and the remote Databricks cluster.
tags:
  - protocol
  - grpc
  - arrow
timestamp: "2026-06-18T15:02:52.981Z"
---

# gRPC Protocol in Databricks Connect

**gRPC Protocol in Databricks Connect** refers to the underlying remote procedure call mechanism that enables communication between a client application and a remote Databricks compute cluster. Databricks Connect uses gRPC as the transport layer for executing Spark DataFrame operations remotely.

## Overview

Databricks Connect is a client library for the Databricks Runtime that allows developers to connect to Databricks compute from local IDEs, notebooks, and custom applications. The library is built on open-source [Spark Connect](/concepts/spark-connect.md), which uses a decoupled client-server architecture for Apache Spark. This architecture enables remote connectivity to Spark clusters using the DataFrame API through a gRPC-based protocol. ^[databricks-connect-databricks-on-aws.md]

## Protocol Architecture

The gRPC protocol in Databricks Connect transmits Spark unresolved logical plans from the client to the remote cluster. The communication layer combines gRPC with Apache Arrow for efficient data serialization. This design keeps the client API thin, allowing it to be embedded in diverse environments such as application servers, IDEs, notebooks, and various programming languages. ^[databricks-connect-databricks-on-aws.md]

### Data Flow

1. **Client-side transformation**: When a user writes DataFrame operations locally (e.g., `df.filter(...).select(...)`), the client converts these operations into unresolved logical plans.
2. **gRPC transmission**: These logical plans are serialized and sent over gRPC to the remote Databricks compute cluster.
3. **Remote execution**: The Databricks cluster executes the Spark plans and processes the data.
4. **Result materialization**: Results are materialized locally when the user calls actions such as `collect()`, `show()`, or `toPandas()`. ^[databricks-connect-databricks-on-aws.md]

## Extensions for Databricks

For Databricks Runtime 13.3 LTS and above, Databricks Connect extends Spark Connect with additions and modifications to support working with Databricks compute modes and [Unity Catalog](/concepts/unity-catalog.md). The gRPC protocol implementation incorporates these Databricks-specific features while maintaining compatibility with the open-source Spark Connect standard. ^[databricks-connect-databricks-on-aws.md]

## Code Execution Model

The gRPC protocol determines where different types of code execute:

- **General code** (Python and Scala) runs locally on the client side, enabling interactive debugging.
- **DataFrame APIs** are converted to Spark plans and transmitted via gRPC to execute on the remote cluster.
- **UDF code** defined locally is serialized and transmitted through the gRPC connection to run on Databricks compute, including operations like `foreach`, `foreachBatch`, and `transformWithState`. ^[databricks-connect-databricks-on-aws.md]

## Key Benefits

- **Remote execution**: Developers can leverage Databricks' scalable compute without running a local Spark session.
- **Interactive development**: The gRPC protocol enables real-time debugging from any IDE while Spark operations execute remotely.
- **Language flexibility**: The protocol supports Python, Scala, and R clients through the same gRPC-based communication layer.
- **Thin client**: The gRPC-based architecture allows the client library to be lightweight and embeddable in various applications. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md)
- Apache Arrow
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md)
- DataFrame API
- [Unity Catalog](/concepts/unity-catalog.md)
- gRPC

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
