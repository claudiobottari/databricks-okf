---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac90c7d954d318cd282e7970475da2847be68e198a5dc1c98c0bc45409d6ff17
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-ide-integration
    - DCII
    - databricks-connect-ide-integration-patterns
    - DCIIP
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect IDE Integration
description: Integration of Databricks Connect with popular IDEs and tools including Visual Studio Code, PyCharm, JupyterLab, Classic Jupyter Notebook, RStudio Desktop, IntelliJ, Eclipse, PyDev, SBT, and Spark shell for remote development and debugging.
tags:
  - ide
  - development
  - debugging
  - integration
timestamp: "2026-06-18T15:03:16.080Z"
---

# Databricks Connect IDE Integration

**Databricks Connect IDE Integration** refers to the ability to use the Databricks Connect client library to connect popular integrated development environments (IDEs) and notebook servers to Databricks clusters. This allows developers to write jobs using Apache Spark APIs and run them remotely on a Databricks cluster instead of in a local Spark session. The client library decouples the local application from the cluster, so that cluster restarts or upgrades do not cause loss of variables or DataFrames. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

With Databricks Connect, you can run large-scale Spark jobs from any Python, R, Scala, or Java application without needing IDE plugins or Spark submission scripts, step through and debug code in your IDE while working with a remote cluster, iterate quickly when developing libraries (client sessions are isolated from each other on the cluster, so you do not need to restart the cluster after changing dependencies), and shut down idle clusters without losing work. For Python development with SQL queries, Databricks recommends using the Databricks SQL Connector for Python instead of Databricks Connect, because it is easier to set up and submits SQL queries directly to remote compute resources. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Requirements

Before setting up IDE integration, ensure the following prerequisites are met:

- **Databricks Runtime version**: The client supports Databricks Runtime 12.2 LTS, 11.3 LTS, 10.4 LTS, 9.1 LTS, and 7.3 LTS (both ML and standard editions where applicable). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Python version**: The minor version of Python on your development machine must match the minor Python version of your Databricks cluster. A Python virtual environment (such as `venv` or Conda) is strongly recommended. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Package version**: The `databricks-connect` major and minor version must match the Databricks Runtime version. For a cluster running Databricks Runtime 12.2 LTS, use `pip install "databricks-connect==12.2.*"`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Java Runtime Environment**: JRE 8 (OpenJDK 8) is required. Java 11 is not supported. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
- **Uninstall PySpark**: The `databricks-connect` package conflicts with PySpark. Before installing Databricks Connect, uninstall any existing PySpark installation. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Setting Up the Client

1. With your Python virtual environment activated, uninstall PySpark if present, then install Databricks Connect:
   ```bash
   pip3 uninstall pyspark
   pip3 install --upgrade "databricks-connect==12.2.*"  # Match your cluster version
   ```
2. Configure connection properties using the CLI (`databricks-connect configure`), SQL configs, or environment variables. Required values: workspace URL, personal access token, cluster ID, and port (default `15001`). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]
3. Test connectivity by running `databricks-connect test`. Successful output includes Spark version information and a successful Scala/Python test. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## IDE-Specific Instructions

### JupyterLab

1. Install JupyterLab in the same Python virtual environment that has Databricks Connect installed.
2. Start JupyterLab and create a new notebook with the Python 3 (ipykernel) kernel.
3. In the first cell, instantiate a Spark session and run your code:
   ```python
   from pyspark.sql import SparkSession
   spark = SparkSession.builder.getOrCreate()
   ```
4. Debugging is supported by enabling the debugger icon in the notebook toolbar. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Classic Jupyter Notebook

The configuration script for Databricks Connect automatically adds the package. To use the `%sql` magic for SQL queries, register a custom magic class as shown in the source documentation. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Visual Studio Code (VS Code)

1. Ensure the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) is installed.
2. Open the Command Palette and select a Python interpreter that matches your cluster’s Python version (recommended: use a virtual environment).
3. Run `databricks-connect get-jar-dir` and add that directory to the `python.venvPath` setting in User Settings JSON.
4. Disable the linter (optional but recommended in the source). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### PyCharm

1. When creating a new project, select **Existing Interpreter** and point to the Conda or virtual environment that matches the cluster’s Python version.
2. Go to **Run > Edit Configurations** and add the environment variable `PYSPARK_PYTHON=python3` to ensure the correct Python executable is used. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### IntelliJ IDEA (Scala or Java)

1. Obtain the JAR directory: run `databricks-connect get-jar-dir`.
2. In IntelliJ, go to **File > Project Structure > Modules > Dependencies > + > JARs or Directories** and add that directory.
3. Remove any other Spark installations from the classpath to avoid conflicts.
4. For debugging, set the breakpoint option to **Thread** (not **All**) to avoid network timeouts. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### PyDev with Eclipse

1. Create a new PyDev project in Eclipse and set the project contents to your Python virtual environment.
2. Configure the interpreter by browsing to the Python executable inside the virtual environment.
3. Add Python code that instantiates a Spark session. Breakpoints and debugging work normally. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Eclipse (Java)

1. Run `databricks-connect get-jar-dir` to get the JAR directory.
2. In Eclipse, go to **Project > Properties > Java Build Path > Libraries > Add External Jars** and select all JARs from that directory.
3. Remove any other Spark JARs from the classpath to prevent conflicts. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### SBT (Scala)

Configure `build.sbt` to use the Databricks Connect JARs as unmanaged dependencies:
```scala
unmanagedBase := new java.io.File("/path/from/databricks-connect get-jar-dir")
```
Set `mainClass` to your application’s entry point. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Spark Shell (Python / Scala)

After running `databricks-connect test` successfully, start the shell with `pyspark` (Python) or `spark-shell` (Scala). The built-in `spark` variable provides access to the remote `SparkSession`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### RStudio Desktop (SparkR and sparklyr)

For **SparkR**, download and unpack the open-source Spark distribution matching your cluster version, then set the `SPARK_HOME` environment variable to the path returned by `databricks-connect get-jar-dir` (one directory above the JAR directory). Load the SparkR library from the OSS Spark package. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

For **sparklyr**, install sparklyr 1.2 or above, then call:
```r
sc <- spark_connect(method = "databricks", spark_home = "<spark-home-path>")
```
where `<spark-home-path>` is the value from `databricks-connect get-spark-home`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Working with Dependencies

You can add dependency JARs and Python files at runtime using `SparkContext.addJar("path-to-jar")` or `SparkContext.addPyFile("path-to-file")`. These are installed on the cluster each time your code runs. Egg files and zip files are also supported with `addPyFile()`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Accessing Databricks Utilities

Databricks Connect supports `dbutils.fs` and `dbutils.secrets` utilities. Use `DBUtils(spark)` to instantiate them. For `dbutils.secrets.get`, you must contact Databricks support to enable the feature in your workspace. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Troubleshooting Common Issues

- **Python version mismatch**: Ensure local Python minor version matches the cluster’s. Set `PYSPARK_PYTHON=python3` if needed.
- **Server not enabled**: Confirm the cluster has `spark.databricks.service.server.enabled true`.
- **Conflicting PySpark installations**: Completely uninstall PySpark before installing Databricks Connect.
- **Conflicting SPARK_HOME**: Unset `SPARK_HOME` if it points to a different Spark installation.
- **Conflicting serialization configurations**: Remove incompatible cluster configs like `spark.io.compression.codec`.
- **winutils.exe on Windows**: Follow instructions to configure Hadoop binaries.
- **Spaces in path on Windows**: Install into a path without spaces or use short name form. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Limitations

Databricks Connect does not support:
- Unity Catalog (except as noted in the source)
- Structured Streaming
- Native Scala/Python/R APIs for Delta table operations (SQL API and Spark API on Delta tables work)
- Copy into
- Server-side registered SQL functions, Python, or Scala UDFs (local UDFs work)
- Table access control and process isolation enabled clusters
- Delta `CLONE` SQL command
- Global temporary views
- Koalas / `pyspark.pandas`
- Some `dbutils` components (credentials, library, notebook workflow, widgets)
- AWS Glue catalog
- Apache Zeppelin 0.7.x and below

Additionally, `CREATE TABLE AS SELECT` SQL commands do not always work; use `spark.sql("SELECT ...").write.saveAsTable("table")` instead. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect Setup](/concepts/databricks-connect-client-setup.md)
- Databricks Runtime
- SparkSession
- Databricks SQL Connector for Python
- Databricks Utilities (dbutils)
- Managing Dependencies with Databricks Connect

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
