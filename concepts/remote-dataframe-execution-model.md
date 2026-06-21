---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a1fb8c634345e70708dc88b110c70e4fa429f992039c765aaa27d39d11161d82
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-dataframe-execution-model
    - RDEM
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Remote DataFrame Execution Model
description: The execution model where DataFrame transformations run on remote Databricks compute while general Python/Scala code runs locally, with results materialized via commands like collect(), show(), and toPandas().
tags:
  - execution-model
  - dataframe
  - databricks
  - spark
timestamp: "2026-06-19T18:08:41.453Z"
---

# Remote DataFrame Execution Model

The **Remote DataFrame Execution Model** describes the architectural pattern used by [Databricks Connect](/concepts/databricks-connect.md), in which DataFrame operations are executed remotely on a Databricks compute cluster while general‑purpose code (e.g., control flow, local variables) remains on the client machine. This model is built on the open‑source [Spark Connect](/concepts/spark-connect.md) protocol, which provides a decoupled client‑server architecture for Apache Spark that enables remote connectivity using the DataFrame API. ^[databricks-connect-databricks-on-aws.md]

## Overview

In this model, the client and the server are separated: the client runs in an IDE, notebook, or custom application, and the server runs as a Spark cluster on Databricks. The underlying protocol uses Spark unresolved logical plans and Apache Arrow on top of gRPC. The client API is intentionally thin so that it can be embedded in a wide variety of environments. ^[databricks-connect-databricks-on-aws.md]

Databricks Connect is an extension of Spark Connect for Databricks Runtime 13.3 LTS and above. It adds modifications to support working with Databricks compute modes and [Unity Catalog](/concepts/unity-catalog.md). ^[databricks-connect-databricks-on-aws.md]

## How It Works

The Remote DataFrame Execution Model splits code into three categories, each executed in a different location:

| Code type | Execution location | Notes |
|-----------|-------------------|-------|
| General Python/Scala code (control flow, local logic) | **Client side** (local machine) | Runs in the local process, enabling interactive debugging. All non‑Spark logic executes locally. |
| DataFrame APIs (transformations, actions) | **Server side** (Databricks compute) | All data transformations are converted to Spark plans and executed on the remote Spark session. Results are materialized on the client only when actions such as `collect()`, `show()`, or `toPandas()` are called. |
| User‑defined functions (UDFs) | **Server side** (Databricks compute) | UDFs defined locally are serialized and transmitted to the cluster, where they run on the remote executors. |

^[databricks-connect-databricks-on-aws.md]

This design allows developers to write standard PySpark or Scala code in their local environment while leveraging the full scalability of Databricks compute for data processing.

## UDF Execution and Dependencies

User‑defined functions defined in the client are serialized and sent to the cluster for execution. APIs that run user code on Databricks include UDFs, `foreach`, `foreachBatch`, and `transformWithState`. ^[databricks-connect-databricks-on-aws.md]

Because general code runs locally, application dependencies must be installed on the local machine (e.g., in a Python virtual environment). UDF dependencies, on the other hand, must be installed on the Databricks cluster. This separation ensures that the client environment does not need to mirror the cluster’s environment exactly. ^[databricks-connect-databricks-on-aws.md]

## Interaction Flow

1. A client application (e.g., a PySpark script in Visual Studio Code) uses the Databricks Connect library to establish a remote connection.
2. DataFrame operations written in the client are converted to Spark unresolved logical plans and sent over gRPC to the Databricks cluster.
3. The cluster executes the plan, and results are streamed back to the client only when an action is called.
4. The client can intermix local debugging (breakpoints, print statements) with remote Spark execution.

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md) — The open‑source protocol underlying this model.
- [Databricks Connect](/concepts/databricks-connect.md) — The client library that implements the remote DataFrame execution model for Databricks.
- gRPC — The transport layer used by Spark Connect.
- Apache Arrow — Columnar format used for data transfer.
- [Unity Catalog](/concepts/unity-catalog.md) — Metadata and governance that Databricks Connect supports.
- [Managed UDF Dependencies](/concepts/udf-dependency-sources.md) — How to install UDF dependencies on the cluster.

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
