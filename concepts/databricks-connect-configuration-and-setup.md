---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9676eca9f6ae7df6fb4aa4fc812aeb9908e3f262df0745959a944ec337e5d7b9
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-configuration-and-setup
    - Setup and Databricks Connect Configuration
    - DCCAS
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect Configuration and Setup
description: Step-by-step process for installing the Databricks Connect client, configuring connection properties (workspace URL, personal access token, cluster ID, port), and testing connectivity.
tags:
  - databricks
  - setup
  - configuration
  - authentication
timestamp: "2026-06-18T11:33:52.166Z"
---

# Databricks Connect Configuration and Setup

**Databricks Connect** is a client library for the Databricks Runtime that enables you to run Spark jobs from popular IDEs (such as Visual Studio Code and PyCharm), notebook servers, or custom applications by executing the commands remotely on a Databricks cluster instead of in a local Spark session. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

This page covers the prerequisites, installation, configuration, and connectivity testing for Databricks Connect on Databricks Runtime 12.2 LTS and below.

## Prerequisites

Before setting up Databricks Connect, ensure your development environment meets the following requirements.

### Databricks Runtime Version

Only the following Databricks Runtime versions are supported:

- Databricks Runtime 12.2 LTS / 12.2 LTS ML
- Databricks Runtime 11.3 LTS / 11.3 LTS ML
- Databricks Runtime 10.4 LTS / 10.4 LTS ML
- Databricks Runtime 9.1 LTS / 9.1 LTS ML
- Databricks Runtime 7.3 LTS

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Python Version

Python 3 must be installed on your development machine, and the **minor version** of your client Python installation must match the minor Python version of your Databricks cluster. For example, if the cluster runs Python 3.9, you must use Python 3.9 locally. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Databricks strongly recommends using a Python virtual environment (such as `venv` or Conda) to manage the correct Python version and avoid version conflicts. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Databricks Connect Package Version

The major and minor version of the `databricks-connect` package must always match your cluster’s Databricks Runtime version. For example, use `databricks-connect==12.2.*` when connecting to a Databricks Runtime 12.2 LTS cluster. Always use the most recent patch release within that minor version. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Java Runtime Environment

Java Runtime Environment (JRE) 8 is required. The client has been tested with OpenJDK 8. Java 11 is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Setup Steps

### Step 1: Install the Databricks Connect Client

1. With your virtual environment activated, uninstall any existing PySpark installation. The `databricks-connect` package conflicts with PySpark and having both installed causes errors. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

   ```bash
   pip3 show pyspark          # Check if PySpark is installed
   pip3 uninstall pyspark     # Uninstall if present
   ```

2. Install the Databricks Connect client using the version that matches your cluster. Use the `--upgrade` flag to ensure the latest patch is installed. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

   ```bash
   pip3 install --upgrade "databricks-connect==12.2.*"
   ```

   Replace `12.2.*` with the appropriate version string for your cluster.

### Step 2: Configure Connection Properties

Collect the following information from your Databricks workspace:

- **Workspace URL** – for example, `https://dbc-xxxxxx.cloud.databricks.com`
- **Personal access token** – create one in your workspace settings
- **Cluster ID** – obtain from the cluster URL in the browser (the part after `#/setting/clusters/`)
- **Port** – the default is `15001`

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

#### Configuration Methods

You can configure the connection using any of the following methods. Precedence (highest to lowest): SQL config keys, CLI, environment variables. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **CLI (Recommended):** Run `databricks-connect configure`. Accept the license and provide the values when prompted. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

  ```bash
  databricks-connect configure
  ```

- **SQL Config Keys:** Use `spark.sql("set key=value")` in your Spark session. For example: `spark.sql("set spark.databricks.service.clusterId=0304-201045-abcdefgh")`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **Environment Variables:** Set corresponding environment variables such as `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, etc. (see source for variable names). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The following table maps the configuration properties to SQL config keys and environment variables:

| Property       | SQL Config Key                      | Environment Variable     |
|----------------|-------------------------------------|--------------------------|
| Host           | `spark.databricks.service.address`  | `DATABRICKS_HOST`        |
| Token          | `spark.databricks.service.token`    | `DATABRICKS_TOKEN`       |
| Cluster ID     | `spark.databricks.service.clusterId`| `DATABRICKS_CLUSTER_ID`  |
| Port           | `spark.databricks.service.port`     | `DATABRICKS_PORT`        |

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Step 3: Test Connectivity

With your virtual environment activated, run the following command to verify the connection:

```bash
databricks-connect test
```

If the cluster is not running, the test will start it (the cluster remains active until its autotermination time). A successful test produces output similar to the following, including a Spark shell session and a successful `spark.range(100).reduce(_ + _)` result. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```
* PySpark is installed at /.../pyspark
* Checking java version ...
* Testing scala command ...
...
scala> spark.range(100).reduce(_ + _)
res0: Long = 4950
scala> :quit
* Testing python command ...
...
```

If no connection-related errors appear (WARN messages are acceptable), the setup is complete.

## Troubleshooting Common Setup Issues

### Python Version Mismatch

Ensure the local Python minor version matches the cluster’s Python version. Use the `PYSPARK_PYTHON` environment variable to explicitly point to the correct Python interpreter if multiple versions are installed. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Conflicting PySpark Installation

If you have both `pyspark` and `databricks-connect` installed, uninstall PySpark first, then reinstall `databricks-connect`:

```bash
pip3 uninstall pyspark databricks-connect
pip3 install --upgrade "databricks-connect==12.2.*"
```

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Conflicting `SPARK_HOME` Environment Variable

If `SPARK_HOME` points to a different Spark installation, unset it. Check your `.bashrc`, `.zshrc`, or IDE environment settings. You do not need to set `SPARK_HOME` for Databricks Connect. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Server Not Enabled

If the Spark server is not enabled on the cluster, ensure the cluster configuration includes `spark.databricks.service.server.enabled true`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Windows-Specific Issues

- **Missing `winutils.exe`:** Follow the [Hadoop on Windows guide](https://cwiki.apache.org/confluence/display/HADOOP2/Hadoop2OnWindows) to install Hadoop binaries. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Spaces in installation path:** If you encounter “The filename, directory name, or volume label syntax is incorrect”, install Java or Databricks Connect into a path without spaces, or use short name forms (e.g., `C:\PROGRA~1`). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Using Databricks Connect After Setup

After successful configuration, you can use Databricks Connect with various IDEs and tools. The client library automatically provides a `SparkSession` that communicates with the remote cluster. For example, in a Python script:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

For IDE-specific instructions (JupyterLab, PyCharm, Visual Studio Code, IntelliJ, Eclipse, RStudio, etc.), see the full [Databricks Connect for Runtime 12.2 LTS and Below](/concepts/migration-of-databricks-connect-from-runtime-122-lts-to-133-lts-and-above.md) documentation.

## Limitations During Setup

- [Unity Catalog](/concepts/unity-catalog.md) is not supported with Databricks Connect for these runtime versions.
- Delta table operations via native APIs (`DeltaTable.forPath`) are not supported; use SQL or DataFrame APIs instead.
- Structured Streaming is not supported.
- The following Databricks Utilities are not available: credentials, library, notebook workflow, and widgets.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- Databricks Connect for Databricks Runtime 13.0 and Above
- Databricks Personal Access Token
- Cluster Configuration
- [PySpark vs Databricks Connect](/concepts/pyspark-and-databricks-connect-conflict.md)
- Databricks SQL Connector for Python – recommended alternative for SQL-only workloads

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
