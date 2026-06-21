---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d4f9690b070cdf5372db9f20817817fdae6cf225264127c55f28a05087075ec8
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-client-setup-and-configuration
    - Configuration and Databricks Connect Client Setup
    - DCCSAC
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect Client Setup and Configuration
description: The step-by-step process of installing the Databricks Connect client package, configuring connection properties (workspace URL, token, cluster ID, port), and testing connectivity to a Databricks cluster.
tags:
  - setup
  - configuration
  - installation
timestamp: "2026-06-19T14:45:53.697Z"
---

---
title: Databricks Connect Client Setup and Configuration
summary: A client library that lets you connect IDEs and custom applications to Databricks clusters to run Spark jobs remotely.
sources:
  - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:06:57.586Z"
updatedAt: "2026-06-18T08:06:57.586Z"
tags:
  - databricks
  - databricks-connect
  - ide-integration
  - development-tools
aliases:
  - databricks-connect-client-setup-and-configuration
  - DCCSC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Connect Client Setup and Configuration

**Databricks Connect** is a client library that allows you to connect popular IDEs — including Visual Studio Code, PyCharm, and IntelliJ — notebook servers, and custom applications to Databricks clusters. Instead of running Spark jobs in a local Spark session, the logical representation of commands (such as `spark.read.format(...).load(...).show()`) is sent to the Spark server running on the remote cluster for execution. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Overview

With Databricks Connect, you can run large-scale Spark jobs from any Python, R, Scala, or Java application without needing IDE plugins or Spark submission scripts. The client enables stepping through and debugging code in your IDE even when working with a remote cluster. It also supports rapid iteration on libraries — you do not need to restart the cluster after changing Python or Java library dependencies, because each client session is isolated. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Because the client application is decoupled from the cluster, it is unaffected by cluster restarts or upgrades that would normally cause loss of variables, RDDs, and DataFrames defined in a notebook. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

For Python development with SQL queries, Databricks recommends using the Databricks SQL Connector for Python instead of Databricks Connect, as it is easier to set up. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Requirements

Databricks Connect supports only specific Databricks Runtime versions: Databricks Runtime 12.2 LTS (ML), 11.3 LTS (ML), 10.4 LTS (ML), 9.1 LTS (ML), and 7.3 LTS. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The minor version of Python installed on the development machine must match the minor Python version on the cluster. Databricks recommends using a Python virtual environment (such as `venv` or Conda) for each Python version used with Databricks Connect. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The Databricks Connect major and minor package version must match the Databricks Runtime version. Databricks recommends using the most recent package that matches the runtime, for example, `databricks-connect==12.2.*` for Databricks Runtime 12.2 LTS. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

A Java Runtime Environment (JRE) 8 is required. The client has been tested with OpenJDK 8 JRE. Java 11 is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Client Setup

### Step 1: Install the Databricks Connect client

With the virtual environment activated, uninstall PySpark if it is already installed (the `databricks-connect` package conflicts with PySpark). Then install the client:

```bash
pip3 uninstall pyspark
pip3 install --upgrade "databricks-connect==12.2.*"
```

Databricks recommends using the `*` wildcard (e.g., `databricks-connect==X.Y.*`) to ensure the most recent package is installed. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Step 2: Configure connection properties

Collect the following configuration properties:
- The Databricks workspace URL.
- A [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md).
- The cluster ID (obtained from the cluster URL).
- The port (default is `15001`).

Configure the connection using the CLI (`databricks-connect configure`), SQL configs, or environment variables. The precedence of configuration methods from highest to lowest is: SQL config keys, CLI, environment variables. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Step 3: Test connectivity

Run `databricks-connect test` to verify connectivity. If the cluster is not running, the test will start it. Successful connectivity output shows no connection-related errors (`WARN` messages are acceptable). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Using Databricks Connect

Once configured, you can use Databricks Connect from various environments including JupyterLab, classic Jupyter Notebook, PyCharm, RStudio Desktop (with SparkR or sparklyr), IntelliJ (Scala or Java), PyDev with Eclipse, Eclipse, SBT, and the Spark shell (PySpark or `spark-shell`). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Basic usage involves instantiating a SparkSession:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
```

The `spark` variable represents the SparkSession on the running cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Accessing Databricks Utilities

Supported Databricks Utilities commands include `dbutils.fs` (cp, head, ls, mkdirs, mv, put, rm) and `dbutils.secrets` (get, getBytes, list, listScopes). For Databricks Runtime 7.3 LTS and above, use the `DBUtils` module from `pyspark.dbutils`. The `dbutils.fs` copy command can transfer files between local and remote filesystems (using `file:/` for the local filesystem on the client), with a maximum file size of 250 MB. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Troubleshooting

Common issues include:
- **Python version mismatch**: Ensure the local Python minor version matches the cluster version. Set `PYSPARK_PYTHON` environment variable if needed.
- **Server not enabled**: Verify `spark.databricks.service.server.enabled true` is set in the cluster configuration.
- **Conflicting PySpark installations**: Uninstall PySpark before installing databricks-connect.
- **Conflicting `SPARK_HOME`**: Unset `SPARK_HOME` if it points to a different Spark version.
- **Conflicting or missing `PATH` entries**: Ensure Databricks Connect binaries take precedence in `PATH`.
- **Conflicting serialization settings**: Remove incompatible cluster serialization configs such as `spark.io.compression.codec`.
- **Windows issues**: On Windows, configure the Hadoop path if `winutils.exe` is not found, and avoid installing Java or Databricks Connect in directory paths with spaces. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Limitations

Databricks Connect does not support: Unity Catalog, Structured Streaming, running arbitrary non-Spark code on the remote cluster, native Scala/Python/R APIs for Delta table operations (SQL API works), Copy Into, SQL functions or UDFs from the server's catalog (locally introduced UDFs work), Apache Zeppelin 0.7.x and below, clusters with table access control, clusters with process isolation enabled, Delta `CLONE` SQL command, global temporary views, Koalas and `pyspark.pandas`, and certain Databricks Utilities (credentials, library, notebook workflow, widgets). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md)
- Databricks Runtime
- Databricks SQL Connector for Python
- Visual Studio Code
- PyCharm IDE Setup for Databricks
- PySpark

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
