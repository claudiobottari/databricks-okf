---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 75ecd73e36315da29741fa73f2c208568c5a7e4213bc1fa0ed65d25687884048
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-client-server-architecture
    - DCCA
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect Client-Server Architecture
description: Architecture where the local client sends logical command representations (e.g., DataFrames) to a Spark server on the remote Databricks cluster for execution, decoupling the client from the cluster.
tags:
  - architecture
  - spark
  - remote-execution
timestamp: "2026-06-18T15:03:10.390Z"
---

# Databricks Connect Client-Server Architecture

**Databricks Connect Client-Server Architecture** refers to the remote execution model in which a lightweight client library runs on a local development machine and communicates with a Spark server process running inside a Databricks cluster. This design decouples the user's application from the cluster lifecycle, enabling interactive development, debugging, and iteration without running Spark locally. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Overview

Databricks Connect is a client library for the Databricks Runtime. It allows developers to write jobs using Spark APIs—Python, Scala, Java, or R—and have those jobs executed remotely on a Databricks cluster rather than in a local Spark session. The client sends a logical representation of each Spark command (for example, a DataFrame operation) to the remote cluster’s Spark server, which performs the actual computation. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

This architecture is fundamentally different from running Spark locally: the client does not instantiate its own SparkContext or execute any Spark transformations or actions. All heavy lifting is delegated to the cluster, while the client remains a thin connector. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Key Components

| Component | Description |
|-----------|-------------|
| **Client Library** | The `databricks-connect` Python package (or equivalent JARs for Scala/Java) installed on the local machine. It replaces the standard PySpark distribution and provides a virtual `SparkSession` that proxies commands to the remote cluster. |
| **Spark Server on Cluster** | A service (`SparkServiceRPCServer`) that runs inside the cluster’s driver JVM, listening on a configurable port (default `15001`). It receives client requests, plans and executes them, and returns results. |
| **Configuration** | The client must be configured with the Databricks workspace URL, a [personal access token](/concepts/databricks-personal-access-token-pat-authentication.md), the cluster ID, and the server port. Configuration can be set via CLI, SQL configs, or environment variables. |

The server logs confirm its start with messages such as: `Loading Spark Service RPC Server` and `Starting Spark Service RPC Server`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## How It Works

When a user runs a command such as `spark.read.table("...").show(5)`, the client:

1. Captures the logical plan (the sequence of operations) without executing anything locally.
2. Serializes the plan into an RPC message and sends it to the cluster’s Spark server.
3. The server receives the request, regenerates the DataFrame plan, executes it on the cluster’s compute resources, and streams the results back to the client.

The client never runs Spark tasks itself; it only acts as a terminal for submitting commands and receiving output. This enables features like stepping through code in an IDE while the actual data processing occurs remotely. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Isolation and Decoupling

A key benefit of the client-server architecture is the separation between the client application and the cluster:

- **Client session isolation**: Each Databricks Connect session is isolated from others on the same cluster. Changing Python or Java library dependencies in the client does not require restarting the cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Cluster restarts**: Because the client is decoupled from the cluster, a cluster restart or upgrade does not cause the client to lose work. The client can reconnect to a new cluster after a restart. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **No local Spark context**: The client does not maintain its own SparkContext; all state (variables, RDDs, DataFrames) resides only on the cluster, which avoids local resource consumption. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Requirements and Compatibility

The client-server architecture imposes specific version alignment:

| Requirement | Details |
|-------------|---------|
| Databricks Runtime version | Supported versions: 7.3 LTS, 9.1 LTS, 10.4 LTS, 11.3 LTS, 12.2 LTS (including ML editions). |
| Python version | Minor version must match between client and cluster (e.g., both Python 3.9). |
| Client package version | `databricks-connect==X.Y.*` must match the cluster’s Runtime version. |
| Java | JRE 8 required; Java 11 not supported. |
| Server config | The cluster must have `spark.databricks.service.server.enabled true`. |

Databricks strongly recommends using a Python virtual environment to prevent conflicts. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Debugging and IDE Integration

The remote execution model allows developers to use familiar IDEs (Visual Studio Code, PyCharm, IntelliJ, Eclipse, RStudio) and set breakpoints in their local code. When a breakpoint is hit, the client pauses, but the remote server continues running network threads—this requires setting IntelliJ’s breakpoint option to **Thread** (not **All**) to avoid network timeouts. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Limitations

The client-server architecture cannot support features that require direct access to the cluster’s internal state or that bypass the Spark session:

- [Unity Catalog](/concepts/unity-catalog.md) is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- Running arbitrary code (non-Spark) on the remote cluster is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- Native Scala/Python/R APIs for Delta table operations (e.g., `DeltaTable.forPath`) are not supported; only SQL and Spark API on Delta tables work. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- Table access control and process isolation clusters are incompatible. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- SparkSession
- Databricks Utilities (dbutils)
- [Personal Access Token Authentication](/concepts/databricks-personal-access-token-pat-authentication.md)
- Databricks SQL Connector for Python
- Cluster Configuration

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
