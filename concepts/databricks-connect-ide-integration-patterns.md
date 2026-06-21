---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3223965146099c5209e67a24e916448485acc89b2badcc195926d23459bc2fee
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-ide-integration-patterns
    - DCIIP
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect IDE Integration Patterns
description: The various methods for integrating Databricks Connect with popular development environments including JupyterLab, PyCharm, VS Code, IntelliJ, Eclipse, RStudio, and Spark shells.
tags:
  - ide
  - development
  - integration
timestamp: "2026-06-19T14:46:24.747Z"
---

# Databricks Connect IDE Integration Patterns

**Databricks Connect IDE Integration Patterns** refers to the established methods for configuring popular IDEs, notebook servers, and custom applications to work with [Databricks Connect](/concepts/databricks-connect.md), the client library that allows users to write Spark jobs locally and execute them remotely on a Databricks cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Overview

Databricks Connect enables developers to run large-scale Spark jobs from any Python, R, Scala, or Java application without needing IDE plugins or Spark submission scripts. It supports step-through debugging in the local IDE while using a remote cluster, isolates client sessions from each other, and decouples the client from the cluster so that cluster restarts do not destroy in-memory state. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Supported IDEs and Integration Patterns

### JupyterLab

To use Databricks Connect with JupyterLab:

1. Install JupyterLab with the Python virtual environment activated.
2. Start JupyterLab in the browser.
3. Create a new notebook (File > New > Notebook) with the **Python 3 (ipykernel)** kernel.
4. Enter code that instantiates `SparkSession.builder.getOrCreate()`.
5. Run cells via **Run > Run All Cells**.
6. Enable the debugger via the bug icon in the toolbar to set breakpoints.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Classic Jupyter Notebook

The configuration script for Databricks Connect automatically adds the package to the project configuration. To enable the `%sql` magic for running and visualizing SQL queries, use the `DatabricksConnectMagics` class defined in the notebook. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Visual Studio Code

1. Verify the Python extension is installed.
2. Open the Command Palette (**Cmd+Shift+P** on macOS, **Ctrl+Shift+P** on Windows/Linux).
3. Select a Python interpreter that matches the cluster's Python version.
4. Run `databricks-connect get-jar-dir` and add the returned directory to the User Settings JSON under `python.venvPath`.
5. Disable the linter.
6. If using a virtual environment, select the correct Python interpreter in the Command Palette.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### PyCharm

1. When creating a project, select **Existing Interpreter** and choose the Conda environment matching the cluster Python version.
2. Go to **Run > Edit Configurations**.
3. Add `PYSPARK_PYTHON=python3` as an environment variable.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### SparkR and RStudio Desktop

1. Download and unpack the open-source Spark distribution matching the cluster version (Hadoop 2.7).
2. Run `databricks-connect get-jar-dir` and set `SPARK_HOME` to the directory one level above the JAR directory.
3. Configure the library path in the R script.
4. Initiate `sparkR.session()`.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### sparklyr and RStudio Desktop

1. Install sparklyr 1.2+ from CRAN or GitHub.
2. Activate the Python environment with Databricks Connect installed.
3. Run `databricks-connect get-spark-home` to get the Spark home path.
4. In RStudio, run `spark_connect(method = "databricks", spark_home = "<path>")`.

Unsupported features in sparklyr include streaming APIs, ML APIs, broom APIs, csv_file serialization mode, and spark submit. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### IntelliJ (Scala or Java)

1. Run `databricks-connect get-jar-dir`.
2. Point dependencies to the returned directory via **File > Project Structure > Modules > Dependencies > + > JARs or Directories**.
3. Remove any other Spark installations from the classpath to avoid conflicts.
4. In the debugger, set the breakpoint option to **Thread** (not **All**) to avoid network timeouts.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### PyDev with Eclipse

1. Create a **PyDev Project** in Eclipse.
2. Configure the interpreter to point to the Python executable from the virtual environment.
3. Add a Python file with `SparkSession.builder.getOrCreate()`.
4. Set breakpoints and run via **Run > Run** or **Run > Debug**.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Eclipse

1. Run `databricks-connect get-jar-dir`.
2. Point external JARs to the returned directory via **Project > Properties > Java Build Path > Libraries > Add External Jars**.
3. Remove other Spark installations from the classpath.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### SBT

Configure `build.sbt` with the `unmanagedBase` directive set to the directory returned by `databricks-connect get-jar-dir`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Spark Shell (Python and Scala)

After `databricks-connect test` succeeds, run `pyspark` (for Python) or `spark-shell` (for Scala). Use the built-in `spark` variable to represent the `SparkSession` on the running cluster. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Common Configuration Steps Across IDEs

All integrations share a common setup workflow:

1. Meet the requirements: Python 3 (minor version must match the cluster), Java 8 JRE, and matching Databricks Connect package version (e.g., `databricks-connect==12.2.*`).
2. Install the client: `pip3 install --upgrade "databricks-connect==12.2.*"`.
3. Configure connection properties: workspace URL, personal access token, cluster ID, and port (default `15001`).
4. Test connectivity with `databricks-connect test`.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library used for remote Spark execution.
- Databricks Runtime – The runtime environment on the cluster that must match the client version.
- SparkSession – The entry point for Spark operations in Databricks Connect.
- Databricks Utilities (dbutils) – Accessible utilities for filesystem and secrets operations.
- Databricks SQL Connector for Python – Alternative for Python SQL development without the complexity of Databricks Connect.
- [Personal Access Token (PAT)](/concepts/databricks-personal-access-token-pat-authentication.md) – Authentication mechanism for connecting to the workspace.

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
