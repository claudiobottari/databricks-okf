---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dbaacc63548082e043fb92dd3f2571ee80a452d5ce1e35d0bb37412d39e2467d
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-shell-and-sbt-with-databricks-connect
    - SBT with Databricks Connect and Spark Shell
    - SSASWDC
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Spark Shell and SBT with Databricks Connect
description: Instructions for using Databricks Connect with the Spark shell (pyspark and spark-shell) and configuring SBT build files to link against Databricks Connect JARs.
tags:
  - spark-shell
  - sbt
  - scala
timestamp: "2026-06-19T09:47:31.682Z"
---

# Spark Shell and SBT with Databricks Connect

Databricks Connect allows you to use the local Spark shell (Python or Scala) and SBT build tool to run Spark jobs on a remote Databricks cluster, rather than in a local Spark session. This enables interactive exploration, debugging, and iterative development without needing IDE plugins or manual JAR submission.

## Overview

With Databricks Connect, you can start a `pyspark` (Python) or `spark-shell` (Scala) session on your development machine that forwards all Spark operations to a configured Databricks cluster. Similarly, SBT projects can use Databricks Connect by linking against the client JARs instead of the usual Spark library dependency. Both approaches require that the Databricks Connect client is installed and configured on the local machine. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Prerequisites

Before using the Spark shell or SBT with Databricks Connect, you must meet the general Databricks Connect requirements:

- A supported Databricks Runtime version (e.g., 12.2 LTS, 11.3 LTS, etc.).
- Python 3 installed on the development machine, with the minor version matching that of the cluster (e.g., Python 3.9 for a cluster running Python 3.9). A Python virtual environment is strongly recommended.
- The `databricks-connect` package installed (e.g., `pip3 install --upgrade "databricks-connect==12.2.*"`) and configured using `databricks-connect configure`, which sets the workspace URL, personal access token, cluster ID, and port (default 15001).
- The connection must be testable with `databricks-connect test`.

For full setup details, see [Databricks Connect Setup](/concepts/databricks-connect-client-setup.md). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Using the Spark Shell

### Python (pyspark)

1. Activate the Python virtual environment where Databricks Connect is installed.
2. Run the `pyspark` command from the terminal. The shell starts, displaying a `>>>` prompt.
3. Use the built-in `spark` variable (a SparkSession) to run commands on the remote cluster. For example:

```python
>>> df = spark.read.table("samples.nyctaxi.trips")
>>> df.show(5)
```

4. To stop the shell, press `Ctrl+D` (or `Ctrl+Z` on Windows) or run `quit()` or `exit()`.

### Scala (spark-shell)

1. With the virtual environment activated, run the `spark-shell` command from the terminal.
2. The shell starts with a `scala>` prompt, providing `sc` as the SparkContext and `spark` as the SparkSession.
3. Use `spark` to interact with the cluster. Example:

```scala
scala> val df = spark.read.table("samples.nyctaxi.trips")
scala> df.show(5)
```

4. Exit with `:q` or `:quit`.

The Spark shell listens on a local HTTP port for the Spark UI, which can be accessed via the URL printed at startup. Job details are also viewable in the Databricks cluster’s Spark UI. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Using SBT

To use Databricks Connect with an SBT project, you must modify `build.sbt` to use the Databricks Connect JARs instead of the standard Spark library dependency. The key directive is `unmanagedBase`, which should point to the directory returned by `databricks-connect get-jar-dir`.

Example `build.sbt` for a Scala application:

```scala
name := "hello-world"
version := "1.0"
scalaVersion := "2.11.6"

// Use the path from ``databricks-connect get-jar-dir``
unmanagedBase := new java.io.File("/usr/local/lib/python2.7/dist-packages/pyspark/jars")

mainClass := Some("com.example.Test")
```

After configuring `build.sbt`, SBT will resolve Spark classes from the Databricks Connect client JARs, and any code that uses `SparkSession.builder.getOrCreate()` will connect to the configured remote cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Troubleshooting

Common issues when using the Spark shell or SBT with Databricks Connect include:

- **Python version mismatch**: Ensure the local Python minor version matches the cluster’s Python version. Set `PYSPARK_PYTHON` if multiple Python installations exist.
- **Conflicting PySpark installations**: The `databricks-connect` package conflicts with PySpark. Uninstall PySpark before installing `databricks-connect` and reinstall the latter.
- **Conflicting `SPARK_HOME`**: If `SPARK_HOME` points to a different Spark installation, unset it. Check IDE settings, `.bashrc`, etc.
- **Conflicting serialization settings**: Remove incompatible cluster configs (e.g., `spark.io.compression.codec`) from cluster settings or set them in the client.
- **Windows `winutils.exe`**: On Windows, if an error about missing `winutils.exe` appears, follow the Hadoop-on-Windows configuration guide.

These issues can prevent the shell from starting or cause “stream corrupted” errors. Running `databricks-connect test` helps diagnose connectivity problems. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Limitations

The Spark shell and SBT sessions share the same limitations as Databricks Connect generally. Notably:

- [Unity Catalog](/concepts/unity-catalog.md) is not supported.
- Structured Streaming, Delta operation native APIs (except SQL), and global temporary views are not supported.
- Some `dbutils` utilities (credentials, notebook workflow, widgets) are not available.
- The `CREATE TABLE ... AS SELECT` SQL command may not work; use `spark.sql(...).write.saveAsTable(...)` instead.

These limitations apply regardless of whether you use the shell or SBT. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect Setup](/concepts/databricks-connect-client-setup.md) – Full client installation and configuration instructions.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – GPU-enabled runtime for deep learning tasks.
- SparkSession – The entry point for Spark functionality in Databricks Connect.
- [Personal Access Token (PAT)](/concepts/databricks-personal-access-token-pat-authentication.md) – Authentication method for Databricks Connect.
- [PySpark vs Databricks Connect](/concepts/pyspark-and-databricks-connect-conflict.md) – Comparison of local vs remote execution.

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
