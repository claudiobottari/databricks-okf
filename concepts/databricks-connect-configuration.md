---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5336da9b31a1f57d0f37d734f6464749584c1ddeddeff320ebdc94a814ec821
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-configuration
    - DCC
    - Advanced Databricks Connect Configuration
    - Databricks CLI Configuration
    - Databricks Connect client configuration
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect Configuration
description: The process of configuring Databricks Connect including workspace URL, personal access token, cluster ID, and port settings via CLI, SQL configs, or environment variables.
tags:
  - configuration
  - setup
  - databricks
timestamp: "2026-06-19T18:10:05.481Z"
---

# Databricks Connect Configuration

**Databricks Connect** is a client library that allows you to connect popular IDEs such as Visual Studio Code, PyCharm, and other custom applications to Databricks clusters, enabling you to run Spark jobs remotely on a Databricks cluster instead of in a local Spark session.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Overview

Databricks Connect is a client library for the Databricks Runtime. When you use Databricks Connect, the logical representation of commands (such as `spark.read.format(...).load(...).groupBy(...).agg(...).show()`) is sent to a Spark server running on a remote Databricks cluster for execution, rather than executing locally.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Key Capabilities

- Run large-scale Spark jobs from any Python, R, Scala, or Java application without needing IDE plugins or spark-submit scripts.
- Step through and debug code in your IDE even when working with a remote Databricks cluster.
- Iterate quickly when developing libraries — you do not need to restart the cluster after changing Python or Java library dependencies because each client session is isolated from others on the cluster.
- Shut down idle clusters without losing work — because the client application is decoupled from the cluster, it is unaffected by cluster restarts or upgrades.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Note for Python SQL Development

For Python development with SQL queries, Databricks recommends using the Databricks SQL Connector for Python instead of Databricks Connect. The SQL Connector is easier to set up, and it submits SQL queries directly to remote compute resources rather than parsing and planning jobs on your local machine, which can make runtime errors difficult to debug.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Requirements

Databricks Connect has specific version requirements:

- **Supported Databricks Runtime versions:** Databricks Runtime 12.2 LTS and 12.2 LTS ML, 11.3 LTS and 11.3 LTS ML, 10.4 LTS and 10.4 LTS ML, 9.1 LTS and 9.1 LTS ML, and 7.3 LTS.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Python 3 requirement:** The minor version of your client Python installation must match the minor Python version of your Databricks cluster. Databricks strongly recommends using a Python virtual environment (e.g., `venv` or `Conda`) activated for each Python version you use with Databricks Connect.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Package version match:** The `databricks-connect` major and minor package version must always match your Databricks Runtime version. For example, use `databricks-connect==12.2.*` with a Databricks Runtime 12.2 LTS cluster.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Java Runtime Environment (JRE) 8:** Requires JRE 8 (tested with OpenJDK 8). The client does not support Java 11.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Setup Procedure

### Step 1: Install the Databricks Connect Client

The `databricks-connect` package conflicts with PySpark. If PySpark is already installed, uninstall it first, then install Databricks Connect:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```bash
pip3 uninstall pyspark
pip3 install --upgrade "databricks-connect==12.2.*"
```

### Step 2: Configure Connection Properties

Configuration can be set via CLI, SQL configs, or environment variables (precedence: SQL config keys > CLI > environment variables). The required properties are:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

1. **Databricks Host:** The workspace URL (e.g., `https://<databricks-instance>.cloud.databricks.com`).
2. **Databricks Token:** A [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md).
3. **Cluster ID:** Obtainable from the cluster URL.
4. **Port:** Default is `15001`.

Configure via CLI:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```bash
databricks-connect configure
```

Then accept the license and enter the configuration values.

## Testing Connectivity

Run the following command to test connectivity:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```bash
databricks-connect test
```

A successful test will display a Welcome message with the Spark version, and then test both the Scala and Python commands. If no connection-related errors (other than `WARN` messages) are shown, the connection is established successfully.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Supported IDEs and Workflows

Databricks Connect supports configuration for multiple development environments:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **JupyterLab and Classic Jupyter Notebook:** Use `SparkSession.builder.getOrCreate()` in a Python kernel.
- **Visual Studio Code:** Requires the Python extension; configure the `python.venvPath` to the JAR directory returned by `databricks-connect get-jar-dir`.
- **PyCharm:** Select an existing interpreter matching the cluster's Python version; set `PYSPARK_PYTHON=python3` as an environment variable.
- **RStudio Desktop (SparkR and sparklyr):** Configure `SPARK_HOME` using the path from `databricks-connect get-jar-dir` or `databricks-connect get-spark-home`, and then use the `spark_connect` or `sparkR.session()` API.
- **IntelliJ (Scala/Java):** Point dependencies to the JAR directory from `databricks-connect get-jar-dir`.
- **Eclipse and PyDev:** Add external JARs from the JAR directory.
- **SBT:** Use the `unmanagedBase` directive in `build.sbt` pointed to the JAR directory.
- **Spark Shell:** Start with `pyspark` (Python) or `spark-shell` (Scala) after successful setup.

## Accessing Databricks Utilities

Use the `dbutils.fs` and `dbutils.secrets` modules via the `DBUtils` class from `pyspark.dbutils`:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```python
from pyspark.dbutils import DBUtils
dbutils = DBUtils(spark)
dbutils.fs.ls("dbfs:/")
dbutils.secrets.listScopes()
```

For Databricks Runtime 7.3 LTS or above, use `DBUtils(spark)` directly. File transfer between local (`file:/`) and remote (`dbfs:/`) filesystems is supported with a maximum file size of 250 MB.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Common Issues and Troubleshooting

| Symptom | Cause | Resolution |
|---|---|---|
| "Stream corrupted" or "class not found" errors | Conflicting PySpark installation | Uninstall PySpark before installing databricks-connect |
| "Stream corrupted" errors | Conflicting `SPARK_HOME` environment variable | Unset `SPARK_HOME` |
| `databricks-connect test` fails | Conflicting or missing `PATH` entry for binaries | Ensure Databricks Connect binaries take precedence, or add the installation `bin` directory to `PATH` |
| "stream corrupted" on cluster | Incompatible cluster serialization configs (e.g., `spark.io.compression.codec`) | Remove conflicting configs from cluster settings |
| Cannot find `winutils.exe` on Windows | Missing Hadoop binary path | Configure the Hadoop path on Windows |
| `The filename, directory name, or volume label syntax is incorrect` on Windows | Space in installation path | Install into a path without spaces, or use short name form |

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Limitations

Databricks Connect does not support the following:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- [Unity Catalog](/concepts/unity-catalog.md)
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)
- Running arbitrary code that is not part of a Spark job
- Native Scala, Python, and R APIs for Delta table operations (e.g., `DeltaTable.forPath` — though SQL API and Spark API on Delta tables are supported)
- Copy into
- Apache Zeppelin 0.7.x and below
- Connecting to clusters with [table access control](/concepts/table-access-control-tacl.md) or process isolation enabled
- Global temporary views
- Koalas and `pyspark.pandas`
- `CREATE TABLE table AS SELECT ...` — use `spark.sql("...").write.saveAsTable("table")` instead
- dbutils credentials, library, notebook workflow, and widgets utilities

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
