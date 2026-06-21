---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e85359d4ad8047b57145c53229ad2d2afc648293257445522f12ac7c7567b8c6
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - client-server-architecture-for-spark-jobs
    - CAFSJ
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Client-Server Architecture for Spark Jobs
description: The architectural pattern where Databricks Connect sends logical representations of Spark DataFrame commands to a remote Spark server running in Databricks for execution, rather than running locally.
tags:
  - architecture
  - spark
  - remote-execution
timestamp: "2026-06-19T18:08:54.776Z"
---

# Client-Server Architecture for Spark Jobs

**Client-Server Architecture for Spark Jobs** describes the design pattern used by tools such as [Databricks Connect](/concepts/databricks-connect.md), where a local client application sends Spark commands to a remote Spark server for execution. This architecture decouples the development environment from the compute cluster, enabling iterative development, debugging, and resource management without being tied to a notebook or cluster session.

## Overview

In a client-server model for Spark, the client runs on a local machine (e.g., an IDE like Visual Studio Code or PyCharm) and connects to a **Spark server** running on a remote Databricks cluster. When a user executes a Spark command, the logical representation of the command (e.g., a DataFrame plan) is sent over the network to the server, which performs the actual computation on the cluster. Results are returned to the client. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

This approach contrasts with traditional local Spark sessions, where all parsing, planning, and execution happens on the same machine. With the client-server architecture, the client is responsible for parsing and planning the job, while the remote server handles execution. This can make it more difficult to debug runtime errors because the error may originate on the server. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## How It Works

When a Spark API call is made on the client (e.g., `spark.read.format(...).load(...).groupBy(...).agg(...).show()`), Databricks Connect sends the logical plan to the Spark server running on the Databricks cluster. The server executes the plan on the cluster’s distributed resources and streams the results back to the client. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The client can be written in **Python**, **R**, **Scala**, or **Java**. The client library (Databricks Connect) must match the Databricks Runtime version of the cluster, and the Python minor version on the client must match that of the cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Key benefits of this decoupled design include:

- **Iterative development**: Library changes can be tested without restarting the cluster, because each client session is isolated. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Idle cluster management**: Clients can shut down idle clusters without losing work, because the client state is independent of the cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Remote debugging**: Users can step through code and set breakpoints in their local IDE while the job runs on the remote cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Configuration

To establish a client-server connection, the client must be configured with:
- The **Databricks workspace URL** and a **personal access token**.
- The **cluster ID** of the target cluster.
- The **port** (default `15001`) on which the Spark server listens. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The Spark server must have `spark.databricks.service.server.enabled` set to `true`. This is enabled by default on Databricks clusters that support Databricks Connect. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Compatibility requirements:
- The client’s **Databricks Connect package version** (e.g., `databricks-connect==12.2.*`) must match the cluster’s Databricks Runtime version.
- The client’s **Python minor version** must match the cluster’s Python version (e.g., both 3.9). Use a virtual environment if necessary. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- Java Runtime Environment 8 is required on the client. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Limitations

The client-server architecture introduces several constraints:
- [Unity Catalog](/concepts/unity-catalog.md) is not supported.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) jobs cannot be run via this model.
- Native Scala, Python, and R APIs for [Delta Lake](/concepts/delta-lake.md) table operations (e.g., `DeltaTable.forPath`) are unsupported; only SQL and Spark APIs work for Delta operations.
- Copy Into commands and global temporary views are not supported.
- Connecting to clusters with [table access control](/concepts/table-access-control-tacl.md) or process isolation enabled is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- Databricks Runtime
- Remote Debugging
- [Distributed Data Processing](/concepts/distributed-data-parallelism-training.md)

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
