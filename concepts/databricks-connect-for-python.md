---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 449261181e2cec56605a94b3da77969463fe14a9d20856f2ed2c22beddd6f8e5
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
    - databricks-connect-for-python-databricks-on-aws.md
    - databricks-connect-for-scala-databricks-on-aws.md
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
    - install-databricks-connect-for-python-databricks-on-aws.md
    - migrate-to-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-connect-for-python
    - DCFP
    - Databricks Connect for Python Utilities
    - Databricks Connect for Python tutorial
    - Databricks SQL Connector for Python
    - Install Databricks Connect for Python
    - Migrate to Databricks Connect for Python
    - Code examples for Databricks Connect for Python
    - Databricks Connect Python tutorial
    - installation guide for Databricks Connect for Python
  citations:
    - file: databricks-connect-for-python-databricks-on-aws.md
    - file: install-databricks-connect-for-python-databricks-on-aws.md
    - file: tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md
    - file: tutorial-run-code-from-pycharm-on-classic-compute-databricks-on-aws.md
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
    - file: migrate-to-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect for Python
description: A Databricks SDK feature enabling IDEs, notebook servers, and custom applications to connect to Databricks clusters using PySpark.
tags:
  - databricks
  - python
  - spark
  - development-tools
timestamp: "2026-06-19T17:45:36.587Z"
---

# Databricks Connect for Python

**Databricks Connect for Python** is a client library that enables you to connect popular IDEs such as PyCharm and Visual Studio Code, notebook servers, and other custom applications to Databricks compute. It allows you to write PySpark code locally and have it executed on a remote Databricks cluster or serverless compute, combining local development flexibility with the power of the Databricks Runtime. ^[databricks-connect-for-python-databricks-on-aws.md]

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above. For earlier versions, see the migration guide. ^[databricks-connect-for-python-databricks-on-aws.md]

## Requirements

Before installing Databricks Connect, confirm that your workspace and local environment meet the documented requirements, including Python version compatibility with the Databricks Connect package version. ^[install-databricks-connect-for-python-databricks-on-aws.md]

The version of the `databricks-connect` Python package must match the Databricks Runtime version of the target cluster. For serverless compute, Databricks Connect 15.4 LTS and above is required. ^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

## Installation

### Activate a Python virtual environment

Databricks strongly recommends using a Python virtual environment (such as `venv` or Poetry) to help ensure correct version compatibility and avoid conflicts. ^[install-databricks-connect-for-python-databricks-on-aws.md]

### Install with venv

1. Create and activate a virtual environment.
2. Uninstall PySpark if it is already installed, because the `databricks-connect` package conflicts with PySpark. ^[install-databricks-connect-for-python-databricks-on-aws.md]
3. Install the Databricks Connect client:

```bash
pip3 install --upgrade "databricks-connect==17.3.*"
```

Replace `17.3` with the version matching your cluster's Databricks Runtime. Using the `.*` suffix ensures the latest compatible package is installed. ^[install-databricks-connect-for-python-databricks-on-aws.md]

### Install with Poetry

```bash
poetry add databricks-connect@~17.3
```

The `~` notation pins the major.minor version while allowing patch updates. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Authentication

Databricks Connect supports several authentication methods. Databricks recommends using a [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) for interactive development. ^[tutorial-run-code-from-pycharm-on-classic-compute-databricks-on-aws.md, tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

### Using a configuration profile

Create a profile in your `~/.databrickscfg` file. For OAuth U2M authentication, use the Databricks CLI to log in:

```bash
databricks auth login --host <workspace-url>
```

After logging in via the browser, the CLI saves a profile (default name `DEFAULT`) that stores the host and refresh token. ^[tutorial-run-code-from-pycharm-on-classic-compute-databricks-on-aws.md, tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

### Using environment variables

Set the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables. Note that the Databricks SDK does not read the `SPARK_REMOTE` environment variable. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Hard-coding credentials (not recommended)

You can pass `host` and `token` directly to the builder, but Databricks does not recommend this option, as it can expose sensitive information in code. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Connecting to compute

### Classic (cluster) compute

Use `DatabricksSession.builder` with a cluster ID. The cluster must be running. You can specify the cluster ID via a profile (adding `cluster_id = <id>`) or by calling `.cluster_id(...)` on the builder. ^[tutorial-run-code-from-pycharm-on-classic-compute-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.profile("my-profile").getOrCreate()
```

Alternatively, set the `DATABRICKS_CLUSTER_ID` environment variable. ^[tutorial-run-code-from-pycharm-on-classic-compute-databricks-on-aws.md]

### Serverless compute

Use `.serverless()` on the builder:

```python
spark = [[databrickssession|DatabricksSession]].builder.serverless().profile("DEFAULT").getOrCreate()
```

Or configure `serverless_compute_id = auto` in the profile and omit `.serverless()`, making the code portable between environments. ^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

### Production-ready sessions

Write code that works both locally with Databricks Connect and directly on a Databricks cluster by using `DatabricksSession.builder.getOrCreate()` without parameters and configuring connection through environment variables or profiles. ^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

## Using Databricks Utilities

Databricks Connect exposes a subset of Databricks Utilities through the `WorkspaceClient` class from the Databricks SDK for Python. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
fs = w.dbutils.fs
secrets = w.dbutils.secrets
```

Available utilities include `fs` (file system) and `secrets`. For example, to create, read, and delete a file in a [Unity Catalog](/concepts/unity-catalog.md) volume:

```python
file_path = "/Volumes/main/default/my-volume/zzz_hello.txt"
fs.put(file=file_path, contents="Hello, Databricks!", overwrite=True)
print(fs.head(file_path))
fs.rm(file_path)
```

^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Code examples

### Read a table

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Create a DataFrame and save as table

```python
from pyspark.sql.types import *
from datetime import date

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()

schema = StructType([
  StructField('AirportCode', StringType(), False),
  StructField('Date', DateType(), False),
  StructField('TempHighF', IntegerType(), False),
  StructField('TempLowF', IntegerType(), False)
])
data = [
  ['BLI', date(2021,4,3), 52, 43],
  # ... more rows ...
]
temps = spark.createDataFrame(data, schema)
spark.sql('USE default')
temps.write.saveAsTable('zzz_demo_temps_table')
df_temps = spark.sql("SELECT * FROM zzz_demo_temps_table ...")
df_temps.show()
spark.sql('DROP TABLE zzz_demo_temps_table')
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Portable fallback code

This example works both with and without Databricks Connect:

```python
from pyspark.sql import SparkSession

def get_spark() -> SparkSession:
    try:
        from databricks.connect import [[databrickssession|DatabricksSession]]
        return [[databrickssession|DatabricksSession]].builder.getOrCreate()
    except ImportError:
        return SparkSession.builder.getOrCreate()

get_spark().read.table("samples.nyctaxi.trips").show(5)
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Development workflow with IDEs

### PyCharm (classic compute)

1. Create a Pure Python project with a virtual environment.
2. Install `databricks-connect` via the **Python Packages** tool window, matching the cluster's Databricks Runtime.
3. Write code using `DatabricksSession.builder.profile("<name>").getOrCreate()`.
4. Run or debug the script. Breakpoints work; remote execution happens transparently. ^[tutorial-run-code-from-pycharm-on-classic-compute-databricks-on-aws.md]

### Visual Studio Code (serverless compute)

1. Create a project folder and a virtual environment (`python -m venv .venv`).
2. Install `databricks-connect`.
3. Write code using `DatabricksSession.builder.serverless().profile("DEFAULT").getOrCreate()`.
4. Run with Python or the debugger. Results stream back to the local console. ^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

## Migration from older versions

To migrate from Databricks Connect for Databricks Runtime 12.2 LTS and below to 13.3 LTS and above:

1. Upgrade your Python version to match the new cluster requirements.
2. Uninstall PySpark and the old `databricks-connect` package.
3. Install the new package: `pip3 install --upgrade "databricks-connect==14.0.*"`
4. Update your code to use `DatabricksSession` instead of `SparkSession` for connecting.
5. Migrate RDD APIs to DataFrame APIs. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

## Additional resources

- [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements)
- [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config)
- [Example applications on GitHub](https://github.com/databricks-demos/dbconnect-examples)
- [Troubleshooting](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/troubleshooting) and [limitations](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/limitations)

## Related concepts

- [DatabricksSession](/concepts/databrickssession.md) — Main entry point for creating a Spark session in Databricks Connect
- [WorkspaceClient](/concepts/workspaceclient-dbutils.md) — Databricks SDK class for accessing utilities and REST APIs
- [OAuth U2M Authentication](/concepts/user-to-machine-u2m-authentication.md) — Recommended authentication flow
- Serverless Compute — Compute type supported in Databricks Connect 15.4+
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for data
- PyCharm — Supported IDE for local development
- Visual Studio Code — Supported IDE
- Databricks Utilities — File system and secrets utilities accessible through Databricks Connect
- Databricks SDK for Python — SDK included with Databricks Connect

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md
- databricks-connect-for-python-databricks-on-aws.md
- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
- install-databricks-connect-for-python-databricks-on-aws.md
- migrate-to-databricks-connect-for-python-databricks-on-aws.md
- tutorial-run-code-from-pycharm-on-classic-compute-databricks-on-aws.md
- tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md

# Citations

1. [databricks-connect-for-python-databricks-on-aws.md](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
2. [install-databricks-connect-for-python-databricks-on-aws.md](/references/install-databricks-connect-for-python-databricks-on-aws-fe510d11.md)
3. [tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md](/references/tutorial-run-python-code-on-serverless-compute-databricks-on-aws-39a4e270.md)
4. [tutorial-run-code-from-pycharm-on-classic-compute-databricks-on-aws.md](/references/tutorial-run-code-from-pycharm-on-classic-compute-databricks-on-aws-50f6add6.md)
5. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
6. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)
7. [migrate-to-databricks-connect-for-python-databricks-on-aws.md](/references/migrate-to-databricks-connect-for-python-databricks-on-aws-5b63ea6f.md)
