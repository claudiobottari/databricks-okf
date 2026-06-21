---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f87f40678d3f8ef95f0ac910db025d952c1293da4717f49c7ea87f759f29d626
  pageDirectory: concepts
  sources:
    - pyspark-shell-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - spark-connect-protocol
    - SCP
  citations:
    - file: pyspark-shell-databricks-on-aws.md
title: Spark Connect Protocol
description: The communication protocol used by Databricks Connect to connect a local PySpark shell to a remote Spark server on a Databricks cluster, as seen in the connection URI scheme.
tags:
  - databricks
  - spark
  - networking
  - protocol
timestamp: "2026-06-19T20:00:08.340Z"
---

## Spark Connect Protocol

The **Spark Connect Protocol** is the client-server communication protocol used by [Databricks Connect](/concepts/databricks-connect.md) to enable remote execution of PySpark DataFrame operations on a Databricks cluster. It separates the local Python environment from the remote Spark runtime, allowing code to run locally while Spark operations execute on the cluster. ^[pyspark-shell-databricks-on-aws.md]

### How It Works

When a [PySpark Shell](/concepts/stopping-the-pyspark-shell.md) (REPL) is started via Databricks Connect, the local client establishes a connection to a **Spark Connect server** running on the Databricks cluster. All Python code that does not involve DataFrame operations executes locally; any PySpark DataFrame operation (e.g., `spark.read.table`, `df.show()`) is sent over the Spark Connect Protocol to the remote cluster for execution, and the results are returned to the local caller. ^[pyspark-shell-databricks-on-aws.md]

### Connection Details

The client connects to the Spark Connect server using a URI with the scheme `sc://`. The URI includes the server endpoint, port, and authentication tokens, as demonstrated in the connection log:

```
Client connected to the Spark Connect server at sc://...:.../;token=...;x-databricks-cluster-id=...
```

The protocol handles authentication via tokens and identifies the target cluster with a cluster ID. ^[pyspark-shell-databricks-on-aws.md]

### Usage in Databricks Connect

The `pyspark` binary shipped with [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) automatically configures the Spark Connect protocol to connect to a running cluster. When the shell starts, a `SparkSession` object (`spark`) is made available, and users interact with it as if they were running locally. All DataFrame operations are transparently forwarded to the remote cluster via the Spark Connect Protocol. ^[pyspark-shell-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- [PySpark Shell](/concepts/stopping-the-pyspark-shell.md)
- SparkSession
- Remote Execution in Databricks
- [Client-Server Architecture in Spark](/concepts/client-server-architecture-for-spark.md)

### Sources

- pyspark-shell-databricks-on-aws.md

# Citations

1. [pyspark-shell-databricks-on-aws.md](/references/pyspark-shell-databricks-on-aws-b2b40482.md)
