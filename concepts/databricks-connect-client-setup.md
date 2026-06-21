---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 084206e91bdfdd961991d6c7b2b06e7ff899869dc3baafccdc7d1f89fb86f98a
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-client-setup
    - DCCS
    - Databricks Connect Setup
    - Set up the Databricks Connect client
    - set up the Databricks Connect client
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect Client Setup
description: Step-by-step process to install the databricks-connect package, uninstall conflicting PySpark, configure connection properties (workspace URL, personal access token, cluster ID, port), and test connectivity.
tags:
  - installation
  - configuration
  - troubleshooting
timestamp: "2026-06-19T09:47:32.979Z"
---

# Databricks Connect Client Setup

**Databricks Connect** is a client library that allows you to connect popular IDEs (such as Visual Studio Code, PyCharm, and IntelliJ), notebook servers (such as JupyterLab), and other custom applications to Databricks clusters. It enables you to write jobs using Spark APIs and run them remotely on a Databricks cluster instead of in a local Spark session. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

When you run a DataFrame command using Databricks Connect, the logical representation of the command is sent to the Spark server running in Databricks for execution on the remote cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Overview

Databricks Connect lets you run large-scale Spark jobs from any Python, R, Scala, or Java application without needing IDE plugins or Spark submission scripts. You can step through and debug code in your IDE even when working with a remote cluster, and iterate quickly when developing libraries — each client session is isolated in the cluster, so you do not need to restart the cluster after changing Python or Java library dependencies. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Additionally, you can shut down idle clusters without losing work, because the client application is decoupled from the cluster and is unaffected by cluster restarts or upgrades. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

> **Note:** For Python development with SQL queries, Databricks recommends using the Databricks SQL Connector for Python instead of Databricks Connect, as it is easier to set up and submits SQL queries directly to remote compute resources. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Requirements

Databricks Connect for Databricks Runtime 12.2 LTS and below has the following requirements: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **Supported Databricks Runtime versions**:
  - Databricks Runtime 12.2 LTS ML, Databricks Runtime 12.2 LTS
  - Databricks Runtime 11.3 LTS ML, Databricks Runtime 11.3 LTS
  - Databricks Runtime 10.4 LTS ML, Databricks Runtime 10.4 LTS
  - Databricks Runtime 9.1 LTS ML, Databricks Runtime 9.1 LTS
  - Databricks Runtime 7.3 LTS

- **Python version**: You must install Python 3 on your development machine, and the minor version of your client Python installation must match the minor Python version of your Databricks cluster. The following table shows the Python version installed with each Databricks Runtime version.

- **Virtual environment**: Databricks strongly recommends using a Python virtual environment (such as `venv` or Conda) activated for each Python version you use with Databricks Connect.

- **Package version matching**: The Databricks Connect major and minor package version must always match your Databricks Runtime version. For example, when using a Databricks Runtime 12.2 LTS cluster, you must use the `databricks-connect==12.2.*` package.

- **Java Runtime Environment**: JRE 8 is required. The client does not support Java 11.

## Setup Steps

### Step 1: Install the Databricks Connect Client

With your virtual environment activated: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

1. Uninstall PySpark if it is already installed, as the `databricks-connect` package conflicts with PySpark.
2. Install the Databricks Connect client using the matching version for your cluster:

```bash
pip3 install --upgrade "databricks-connect==12.2.*"  # Or X.Y.* to match your cluster version.
```

Databricks recommends using the "dot-asterisk" notation (e.g., `12.2.*`) instead of an exact version to ensure the most recent package is installed. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Step 2: Configure Connection Properties

Collect the following configuration properties: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- Your Databricks workspace URL
- Your Databricks [personal access token](/concepts/databricks-personal-access-token-pat-authentication.md)
- The ID of your cluster (obtainable from the cluster URL)
- The port for connection (default is `15001`)

You can configure the connection using the CLI, SQL configs, or environment variables. The precedence (highest to lowest) is: SQL config keys, CLI, environment variables. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

**Using the CLI:**

```bash
databricks-connect configure
```

Enter the configuration values when prompted. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Step 3: Test Connectivity

With your virtual environment activated, test connectivity: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```bash
databricks-connect test
```

If the cluster is not running, the test starts the cluster. A successful connection shows Spark and Scala session output without connection-related errors (WARN messages are acceptable). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## IDE and Notebook Configuration

Databricks Connect can be configured with the following environments: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **JupyterLab / Classic Jupyter Notebook**: Install JupyterLab in your virtual environment, create a notebook, and instantiate `SparkSession.builder.getOrCreate()`.
- **Visual Studio Code**: With the Python extension installed, add the Databricks Connect JAR directory (obtained from `databricks-connect get-jar-dir`) to your Python settings and select the matching Python interpreter.
- **PyCharm**: Create a project using the Conda environment matching your cluster Python version, and set the `PYSPARK_PYTHON=python3` environment variable for Python 3 clusters.
- **SparkR / sparklyr with RStudio Desktop**: Download the matching open-source Spark distribution, set `SPARK_HOME` to the Databricks Connect directory, and initiate a Spark session.
- **IntelliJ (Scala or Java)**: Add the JARs from the directory returned by `databricks-connect get-jar-dir` as project dependencies.
- **Eclipse**: Similarly add the Databricks Connect JARs as external JARs.
- **SBT**: Configure `unmanagedBase` in `build.sbt` to point to the Databricks Connect JAR directory.
- **Spark shell**: Run `pyspark` (Python) or `spark-shell` (Scala) after a successful `databricks-connect test`.

## Code Examples

A simple Python example: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```python
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

## Working with Dependencies

You can add dependency JARs and Python files using `sparkContext.addJar()` or `sparkContext.addPyFile()`. These are installed on the cluster each time you run your code. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Accessing Databricks Utilities

You can use `dbutils.fs` and `dbutils.secrets` utilities. Supported commands include `cp`, `head`, `ls`, `mkdirs`, `mv`, `put`, `rm`, `get`, `getBytes`, `list`, and `listScopes`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

You can copy files between local and remote filesystems using the `file:/` scheme for the local filesystem:

```python
dbutils.fs.cp('file:/home/user/data.csv', 'dbfs:/uploads')
```

The maximum file size for transfer is 250 MB. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Troubleshooting

Common issues and resolutions: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **Python version mismatch**: Ensure your local Python minor version matches the cluster version.
- **Server not enabled**: Verify that `spark.databricks.service.server.enabled true` is set on the cluster.
- **Conflicting PySpark installations**: Uninstall PySpark and reinstall Databricks Connect.
- **Conflicting `SPARK_HOME`**: Unset the `SPARK_HOME` environment variable if it points to a different Spark version.
- **Windows issues**: For `winutils.exe` errors, configure the Hadoop path on Windows.

## Limitations

Databricks Connect for these runtime versions does not support: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- [Unity Catalog](/concepts/unity-catalog.md)
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)
- Running arbitrary non-Spark code on the remote cluster
- Native Scala, Python, and R APIs for Delta table operations (SQL API is supported)
- Copy into operations
- Server-side catalog SQL functions or UDFs
- Connecting to clusters with [table access control](/concepts/table-access-control-tacl.md)
- Connecting to clusters with process isolation enabled
- Delta `CLONE` SQL command
- Global temporary views
- Certain `dbutils` utilities (credentials, library, notebook workflow, widgets)

## Related Concepts

- Databricks SQL Connector for Python
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Personal Access Tokens](/concepts/databricks-personal-access-token-pat-authentication.md)
- Databricks Utilities (dbutils)
- Cluster Configuration

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
