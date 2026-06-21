---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c1f64b416edf867f352b4abb39baf5144a682d847e6a36ac3e51baa9b39ce41
  pageDirectory: concepts
  sources:
    - pyspark-shell-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - local-vs-remote-execution-model-in-databricks-connect
    - LVREMIDC
  citations:
    - file: pyspark-shell-databricks-on-aws.md
title: Local vs Remote Execution Model in Databricks Connect
description: The execution model where all Python code runs locally while PySpark DataFrame operations run on the remote Databricks cluster, with responses sent back to the local caller.
tags:
  - databricks
  - pyspark
  - execution-model
  - distributed-computing
timestamp: "2026-06-19T20:00:28.060Z"
---

##Local vs Remote Execution Model in Databricks Connect

The **local vs remote execution model** describes how [Databricks Connect](/concepts/databricks-connect.md) splits computation between the client environment (local machine) and the remote Databricks cluster. This architecture allows developers to use familiar local tools while executing Apache Spark operations at scale on the cluster.

### Overview

Databricks Connect uses a client‑server architecture based on [Spark Connect](/concepts/spark-connect.md). The client is the local Python environment where the user writes and runs scripts or a PySpark shell. The server is a running Databricks cluster in the remote workspace. When the client connects, a `SparkSession` object (`spark`) becomes available that acts as a proxy to the remote cluster. ^[pyspark-shell-databricks-on-aws.md]

### Execution Boundaries

- **Local execution:** All Python code that does not involve DataFrame operations runs on the client machine. This includes variable assignments, control flow, printing output, and calls to pure-Python libraries. For example, a simple `print()` statement or a Python loop executes locally. ^[pyspark-shell-databricks-on-aws.md]

- **Remote execution:** Every PySpark operation that works with DataFrames (such as `spark.read.table()`, `.select()`, `.filter()`, `.show()`) is sent to the remote cluster via the Spark Connect protocol. The cluster performs the actual distributed computation, and the results (e.g., rows, schema, metrics) are transmitted back to the local client. ^[pyspark-shell-databricks-on-aws.md]

This split means that while the local client sees a Python REPL or script, all heavy lifting happens on the cluster’s workers.

### How the Shell Works

When the PySpark shell starts with `pyspark` (from a Databricks Connect virtual environment), it automatically connects to the configured cluster. After connection, the `spark` object is immediately available. A command such as `spark.range(1,10).show()` triggers a remote job; the shell waits for the result and displays it locally. ^[pyspark-shell-databricks-on-aws.md]

```python
# This runs locally
print("Starting analysis")

# This runs on the remote cluster
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)  # Results are returned locally
```

### Implications for Development

Because pure Python code runs locally, developers can use debugging tools, print statements, and third‑party libraries on the client side without impacting cluster performance. However, any code that depends on DataFrame data (e.g., iterating over rows) must be expressed as Spark transformations or actions; attempting to collect large datasets into local memory can overwhelm the client.

This model also means that UDFs (User Defined Functions) and pandas UDFs are executed on the cluster, not locally, because they are part of the DataFrame operation. The client only orchestrates the execution plan.

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The overall framework for remote Spark execution.
- PySpark shell – The interactive REPL that uses this execution model.
- [Spark Connect](/concepts/spark-connect.md) – The protocol enabling the client‑server split.
- [DataFrame operations](/concepts/remote-dataframe-operations.md) – The operations that are executed remotely.
- Cluster configuration – Requirements for setting up the remote compute.

### Sources

- pyspark-shell-databricks-on-aws.md

# Citations

1. [pyspark-shell-databricks-on-aws.md](/references/pyspark-shell-databricks-on-aws-b2b40482.md)
