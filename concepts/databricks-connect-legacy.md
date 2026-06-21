---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b5142c42bee7fb952cd34596087950e3110e2a238be99aa4e0609a49da2bf68
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-legacy
    - DC(
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect (Legacy)
description: A client library that allows users to connect local IDEs and applications to Databricks clusters, running Spark jobs remotely instead of locally.
tags:
  - databricks
  - connectivity
  - spark
timestamp: "2026-06-19T09:48:48.968Z"
---

# Databricks Connect (Legacy)

**Databricks Connect (Legacy)** is a client library that allows you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters to run Spark jobs remotely. Instead of executing code in a local Spark session, Databricks Connect sends the logical representation of commands — such as DataFrame operations — to a Spark server running on a Databricks cluster for execution.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Overview

Databricks Connect enables you to write jobs using Spark APIs and run them remotely on a Databricks cluster. When you run a command like `spark.read.format(...).load(...).groupBy(...).agg(...).show()`, the logical plan is sent to the Spark server on the remote cluster for execution.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Key capabilities include:

- **Run large-scale Spark jobs** from any Python, R, Scala, or Java application without installing IDE plugins or using Spark submission scripts.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Step through and debug code** in your IDE while working with a remote cluster.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Iterate quickly when developing libraries** — you do not need to restart the cluster after changing Python or Java library dependencies, because each client session is isolated.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Shut down idle clusters without losing work** — the client application is decoupled from the cluster and unaffected by cluster restarts or upgrades.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

> **Note:** For Python development with SQL queries, Databricks recommends using the Databricks SQL Connector for Python instead of Databricks Connect, as it is easier to set up and submits SQL queries directly to remote compute resources.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Requirements

Databricks Connect (Legacy) has specific version and environment requirements:

- **Supported Databricks Runtime versions:** Databricks Runtime 12.2 LTS ML, 12.2 LTS; 11.3 LTS ML, 11.3 LTS; 10.4 LTS ML, 10.4 LTS; 9.1 LTS ML, 9.1 LTS; and 7.3 LTS.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Python version:** Python 3 must be installed on your development machine. The minor version of your client Python installation must match the minor Python version of your Databricks cluster. Databricks strongly recommends using a Python virtual environment.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Package version:** The Databricks Connect major and minor package version must always match your Databricks Runtime version. For example, use `databricks-connect==12.2.*` with a Databricks Runtime 12.2 LTS cluster.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Java Runtime Environment:** JRE 8 is required; Java 11 is not supported.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Setup

### Step 1: Install the client

With your virtual environment activated, uninstall PySpark if present (as it conflicts with Databricks Connect), then install the client:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```bash
pip3 uninstall pyspark
pip3 install --upgrade "databricks-connect==12.2.*"
```

### Step 2: Configure connection properties

Collect the following:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- Databricks workspace URL
- Databricks personal access token
- Cluster ID (from the cluster URL)
- Port (default: `15001`)

Configure using the CLI:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```bash
databricks-connect configure
```

You can also use SQL configs or environment variables. Configuration precedence (highest to lowest) is: SQL config keys, CLI, environment variables.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Step 3: Test connectivity

Run `databricks-connect test` to verify the connection. If successful, you'll see a Spark session greeting without connection-related errors.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Supported IDEs and Environments

Databricks Connect supports a wide range of development environments:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **JupyterLab** and **Classic Jupyter Notebook**
- **Visual Studio Code** — requires the Python extension and proper Python interpreter selection
- **PyCharm** — requires selecting the correct Conda or virtual environment and setting `PYSPARK_PYTHON=python3`
- **SparkR and RStudio Desktop** — requires downloading the open-source Spark distribution and configuring `SPARK_HOME`
- **sparklyr and RStudio Desktop** — requires sparklyr 1.2 or above
- **IntelliJ (Scala or Java)** — requires pointing dependencies to the Databricks Connect JAR directory
- **PyDev with Eclipse**
- **Eclipse** — requires adding Databricks Connect JARs to the build path
- **SBT** — requires setting `unmanagedBase` to the Databricks Connect JAR directory
- **Spark shell** — for both Python (`pyspark`) and Scala (`spark-shell`)

## Accessing Databricks Utilities

You can use `dbutils.fs` and `dbutils.secrets` utilities with Databricks Connect. Supported commands include `dbutils.fs.cp`, `dbutils.fs.ls`, `dbutils.fs.mkdirs`, `dbutils.fs.mv`, `dbutils.fs.rm`, `dbutils.secrets.get`, and others.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

To access the DBUtils module in a version-compatible way:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```python
from pyspark.dbutils import DBUtils
dbutils = DBUtils(spark)
```

For Databricks Runtime 7.3 LTS+, use the direct import; otherwise, check for the `spark.databricks.service.client.enabled` config first.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Limitations

Databricks Connect (Legacy) has several limitations:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- Does not support Unity Catalog
- Does not support Structured Streaming
- Cannot run arbitrary non-Spark code on the remote cluster
- Native Scala, Python, and R APIs for Delta table operations (e.g., `DeltaTable.forPath`) are not supported (SQL API and Spark API on Delta tables are supported)
- Does not support Copy into
- SQL functions, Python or Scala UDFs from the server's catalog are not supported (locally introduced UDFs work)
- Does not support Apache Zeppelin 0.7.x and below
- Cannot connect to clusters with table access control or process isolation enabled
- Does not support Delta `CLONE` SQL command
- Does not support global temporary views
- Does not support Koalas and `pyspark.pandas`
- `CREATE TABLE table AS SELECT ...` SQL commands do not always work (use `spark.sql("SELECT ...").write.saveAsTable("table")` instead)
- Several dbutils utilities are unsupported: credentials, library, notebook workflow, and widgets

## Troubleshooting

Common issues and resolutions:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **Python version mismatch:** Ensure your local Python minor version matches the cluster's Python version
- **Server not enabled:** Verify `spark.databricks.service.server.enabled true` is set in cluster configuration
- **Conflicting PySpark installations:** Uninstall PySpark before installing Databricks Connect
- **Conflicting `SPARK_HOWME`:** Unset `SPARK_HOME` if it points to a different Spark installation
- **Conflicting serialization settings:** Remove incompatible cluster serialization configs like `spark.io.compression.codec`
- **Windows issues:** Install `winutils.exe` and avoid directory paths with spaces

## Related Concepts

- Databricks SQL Connector for Python — Recommended alternative for Python SQL development
- Databricks Runtime — The runtime environment used by clusters
- Databricks Utilities (dbutils) — File system and secrets utilities
- PySpark — The Python API for Apache Spark
- SparkSession — The entry point for Spark functionality

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
