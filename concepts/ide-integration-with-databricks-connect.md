---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ba0f2df21b75f969968d19846556a1aa3957785a8a99b0aa78ac379b50db042
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ide-integration-with-databricks-connect
    - IIWDC
    - IDE Integration with Databricks Connect (modern)
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: IDE Integration with Databricks Connect
description: How to configure and use Databricks Connect with various development environments including JupyterLab, Classic Jupyter Notebook, Visual Studio Code, PyCharm, RStudio Desktop, IntelliJ, Eclipse, and PyDev.
tags:
  - ide
  - integration
  - development
timestamp: "2026-06-19T18:09:57.086Z"
---

# IDE Integration with Databricks Connect

**IDE Integration with Databricks Connect** refers to the ability to use local development tools such as JupyterLab, PyCharm, IntelliJ IDEA, Visual Studio Code, Eclipse, and RStudio Desktop to write Spark jobs that run remotely on a Databricks cluster. Instead of executing Spark code in a local Spark session, Databricks Connect sends commands to a Spark server on a Databricks cluster, enabling large-scale data processing and debugging directly from the IDE.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

This page covers the legacy version of Databricks Connect for Databricks Runtime 12.2 LTS and below. For the current version (Databricks Runtime 13.3 LTS and above), see [IDE Integration with Databricks Connect (modern)](/concepts/ide-integration-with-databricks-connect.md).

---

## Overview

With Databricks Connect, you can:

- Run large-scale Spark jobs from any Python, R, Scala, or Java application by importing standard Spark libraries (e.g., `import pyspark`, `require(SparkR)`, or `import org.apache.spark`).
- Step through code and debug in your IDE while the computation executes on a remote cluster.
- Iterate quickly during library development; after changing Python or Java dependencies, you do not need to restart the cluster because each client session is isolated.
- Shut down idle clusters without losing work. The client application is decoupled from the cluster, so variables, RDDs, and DataFrames are not lost during cluster restarts or upgrades.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

---

## Supported IDEs

The following IDEs and environments are documented for use with Databricks Connect (legacy):^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- JupyterLab
- Jupyter Notebook (classic)
- Visual Studio Code (with Python extension)
- PyCharm
- RStudio Desktop (for SparkR and sparklyr)
- IntelliJ IDEA (Scala/Java)
- PyDev with Eclipse
- Eclipse (Java)
- SBT (Scala build tool)
- Spark shell (Python, Scala)

Any IDE that can run a JVM‑based application and reference the Databricks Connect JARs should work, though only the above are explicitly covered in the documentation.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

---

## Getting Started

### Requirements

Before using any IDE with Databricks Connect, ensure your environment meets the following:^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **Databricks Runtime**: Only 12.2 LTS, 11.3 LTS, 10.4 LTS, 9.1 LTS, or 7.3 LTS (and their ML editions).
- **Python version**: The minor Python version on your development machine must match the cluster's Python version. Databricks strongly recommends using a Python virtual environment (e.g., `venv` or Conda).
- **Databricks Connect package version**: Must match the Databricks Runtime major.minor version (e.g., `databricks-connect==12.2.*`).
- **Java**: JRE 8 (OpenJDK 8 tested). Java 11 is not supported.
- **Windows**: If using Windows, `winutils.exe` must be accessible; see troubleshooting.

### Install Databricks Connect

With your virtual environment activated:

1. Uninstall any existing PySpark installation (it conflicts with Databricks Connect).
2. Install the matching Databricks Connect package:
   ```bash
   pip3 install --upgrade "databricks-connect==12.2.*"
   ```
   Replace `12.2` with your cluster's runtime version.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Configure Connection Properties

Collect the following values:

- Databricks workspace URL (must start with `https://`)
- [Personal access token](/concepts/databricks-personal-access-token-pat-authentication.md)
- Cluster ID (visible in the cluster’s URL)
- Port (default `15001`)

Configure them using one of these methods (precedence: SQL configs > CLI > environment variables):^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **CLI**: Run `databricks-connect configure` and supply the values.
- **Environment variables**: Set `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLUSTER_ID`, `DATABRICKS_PORT`.
- **SQL configs**: Use `spark.sql("set spark.databricks.service.clusterId=...")`.

Test connectivity with `databricks-connect test`. A successful test will start the cluster (if not already running) and run sample Scala and Python commands.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

---

## IDE-Specific Setup Instructions

### JupyterLab

1. Install JupyterLab in the activated Python environment: `pip3 install jupyterlab`.
2. Launch JupyterLab: `jupyter lab`. Create a new notebook with the Python 3 kernel.
3. In a cell, create a SparkSession:
   ```python
   from pyspark.sql import SparkSession
   spark = SparkSession.builder.getOrCreate()
   ```
4. Run cells normally. The debugger can be enabled via the bug icon.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Classic Jupyter Notebook

The same Python code as above works. To enable the `%sql` magic for SQL queries and visualisation, use the `DatabricksConnectMagics` class provided in the documentation.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Visual Studio Code

1. Install the Python extension.
2. Open Command Palette and select the correct Python interpreter (must match the cluster’s Python version).
3. Run `databricks-connect get-jar-dir` and add the returned path to `python.venvPath` in User Settings JSON.
4. Disable the linter to avoid conflicts.
5. For virtual environments, select the correct interpreter from the Command Palette.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### PyCharm

1. Create a new project and select **Existing Interpreter** pointing to the Conda/venv environment that has Databricks Connect installed.
2. Go to **Run > Edit Configurations** and add the environment variable `PYSPARK_PYTHON=python3` (for Python 3 clusters).^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### RStudio Desktop (SparkR and sparklyr)

For **SparkR**:
- Download and unpack the matching open‑source Spark distribution.
- Run `databricks-connect get-jar-dir` to find the `SPARK_HOME` path (one directory above the JAR directory).
- In an R script, set `SPARK_HOME` and load the SparkR library from the OSS package path.
- Call `sparkR.session()` and then use SparkR commands.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

For **sparklyr** (version 1.2+):
- Install sparklyr from CRAN or GitHub.
- Activate the Python environment, run `databricks-connect get-spark-home`.
- In R, use `spark_connect(method = "databricks", spark_home = "<path>")`.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

**Limitations**: sparklyr streaming APIs, ML APIs, broom APIs, CSV file serialization, and Spark submit are not supported.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### IntelliJ IDEA (Scala/Java)

1. Run `databricks-connect get-jar-dir` to get the JAR directory.
2. In IntelliJ, go to **File > Project Structure > Modules > Dependencies > '+' > JARs or Directories** and add the JAR directory.
3. Remove any other Spark installations from the classpath to avoid conflicts.
4. Set the breakpoint option to **Thread** instead of **All** to prevent network timeouts during debugging.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### PyDev with Eclipse

1. Install PyDev plugin.
2. Create a PyDev project and manually configure the interpreter to point to the Python executable from your virtual environment.
3. Add a Python file containing the SparkSession code, set breakpoints, and run/debug.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Eclipse (Java)

1. Run `databricks-connect get-jar-dir`.
2. In Eclipse, go to **Project > Properties > Java Build Path > Libraries > Add External Jars** and select the JAR directory.
3. Remove other Spark installations from the classpath.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### SBT

In `build.sbt`, set `unmanagedBase` to the path from `databricks-connect get-jar-dir`. This replaces the usual Spark library dependency. Example:
```scala
unmanagedBase := new java.io.File("/usr/local/lib/python2.7/dist-packages/pyspark/jars")
```^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Spark Shell

After successful `databricks-connect test`, start `pyspark` (Python) or `spark-shell` (Scala) from the activated environment. Use the built-in `spark` variable to run commands.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

---

## Code Examples

### Simple query example
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Full example (creating tables, querying, cleanup) is available in the source documentation.^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

---

## Troubleshooting Common Issues

| Issue | Cause / Solution |
|-------|------------------|
| **Python version mismatch** | Local Python minor version must match cluster’s. Set `PYSPARK_PYTHON` environment variable. |
| **Server not enabled** | Ensure `spark.databricks.service.server.enabled true` is set on the cluster. |
| **Conflicting PySpark installation** | Uninstall PySpark before installing Databricks Connect. |
| **Conflicting `SPARK_HOME`** | Unset `SPARK_HOME` environment variable; do not point to another Spark distribution. |
| **Conflicting or missing `PATH`** | Ensure Databricks Connect binaries are first in `PATH`, or add the `bin` directory. |
| **Conflicting serialization** | Remove incompatible cluster configs like `spark.io.compression.codec`. |
| **Cannot find `winutils.exe`** (Windows) | Configure Hadoop path as per Apache Hadoop on Windows guide. |
| **Path with spaces** (Windows) | Install Java or Databricks Connect in a path without spaces. |

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

---

## Limitations

- [Unity Catalog](/concepts/unity-catalog.md) is not supported.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) is not supported.
- Running arbitrary code (non‑Spark jobs) on the remote cluster is not supported.
- Delta table native APIs (`DeltaTable.forPath`) are not supported; use SQL or Spark API instead.
- `COPY INTO`, global temporary views, Koalas, `pyspark.pandas` are not supported.
- Several Databricks Utilities (`dbutils`) are not accessible: credentials, library, notebook workflow, widgets.
- AWS Glue catalog is not supported.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

---

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
