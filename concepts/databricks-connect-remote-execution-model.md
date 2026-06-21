---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7f26a2be75185577ee5d86a22d1a70082d12633bd67bb15ca268d06ebb228d4
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-remote-execution-model
    - DCREM
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect Remote Execution Model
description: The architectural pattern where logical representations of Spark commands (DataFrame operations) are sent to a remote Spark server on the Databricks cluster rather than executed locally.
tags:
  - architecture
  - remote-execution
  - spark
timestamp: "2026-06-19T14:45:24.505Z"
---

## Databricks Connect Remote Execution Model

**Databricks Connect Remote Execution Model** refers to the architecture and mechanism by which the Databricks Connect client library enables local applications (IDEs, notebook servers, or custom applications) to run Apache Spark jobs remotely on a Databricks cluster instead of executing them in a local Spark session. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Overview

Databricks Connect is a client library for the Databricks Runtime. When a user runs a DataFrame command such as `spark.read.format(...).load(...).groupBy(...).agg(...).show()`, the logical representation of that command is sent to the Spark server running in the Databricks cluster for execution on the remote cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

This decoupled architecture allows developers to:
- Run large-scale Spark jobs from any Python, R, Scala, or Java application without needing IDE plugins or Spark submission scripts.
- Step through and debug code in an IDE even when working with a remote cluster.
- Iterate quickly on library development because each client session is isolated from others on the cluster, and changing dependencies does not require restarting the cluster.
- Shut down idle clusters without losing work, as the client application is unaffected by cluster restarts or upgrades. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Connection Setup

To use Databricks Connect, the client must meet specific version requirements (matching Python minor version, matching Databricks Connect package version with the cluster runtime, and Java 8) and be configured with connection properties. The configuration includes the workspace URL, a personal access token, the cluster ID, and a port (default `15001`). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Configuration can be done via CLI (`databricks-connect configure`), SQL config keys, or environment variables. Precedence from highest to lowest is: SQL config keys, CLI, environment variables. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The cluster must have the Spark server enabled with `spark.databricks.service.server.enabled true`. The server listens on port `15001` (by default). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Execution Flow

When a client starts a SparkSession using `SparkSession.builder.getOrCreate()`, Databricks Connect initializes a connection to the remote cluster. All subsequent Spark operations (DataFrame transformations/actions, SQL queries, RDD operations) are compiled locally into a logical plan, which is then serialized and sent to the remote Spark server for execution. Results are returned to the client. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Because execution happens remotely, the client does not run any actual data processing locally; it only orchestrates commands. This means the local environment does not need a large cluster configuration, but it also implies that debugging runtime errors can be more difficult because error messages originate from the remote cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md] The source notes that for Python SQL queries, Databricks SQL Connector for Python is easier to set up and runs queries directly on remote compute resources, whereas Databricks Connect parses and plans jobs on the local machine before sending them to the cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Client Session Isolation

Each client session is isolated from others on the cluster. This means multiple users or applications can connect to the same cluster without interfering with each other. It also allows library changes to be picked up without restarting the cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Limitations of the Remote Execution Model

The remote execution model imposes several limitations:

- [Unity Catalog](/concepts/unity-catalog.md) is not supported.
- Structured Streaming is not supported.
- Arbitrary code that is not part of a Spark job cannot be run on the remote cluster.
- Native Scala, Python, and R APIs for Delta table operations (e.g., `DeltaTable.forPath`) are not supported, though SQL API and Spark API on Delta tables work.
- `COPY INTO` is not supported.
- SQL functions, Python or Scala UDFs from the server’s catalog are not supported (locally introduced UDFs work).
- Connecting to clusters with table access control or process isolation is not supported.
- Delta `CLONE` SQL command, global temporary views, and Koalas/pyspark.pandas are not supported.
- `CREATE TABLE table AS SELECT ...` SQL commands may not always work; the recommended alternative is `spark.sql("SELECT ...").write.saveAsTable("table")`.
- Several Databricks Utilities (dbutils) modules (credentials, library, notebook workflow, widgets) are unsupported.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library itself.
- Databricks Runtime – The runtime environment on the cluster.
- SparkSession – Entry point for Spark operations.
- IDE Integration – How Databricks Connect integrates with VS Code, PyCharm, IntelliJ, etc.
- Databricks SQL Connector for Python – Alternative for SQL-heavy workloads.
- Remote Debugging – Using breakpoints and debuggers with Databricks Connect.

### Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
