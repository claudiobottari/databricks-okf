---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3741c450fcd14dc24d3b3403bf1e7c4ccec525d872b2575f41838a6111fb52bc
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
    - install-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.98
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-connect-dependency-management
    - DCDM
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Databricks Connect Dependency Management
description: The approach to handling dependencies where application dependencies are installed locally on the client machine and UDF dependencies are installed on the Databricks cluster.
tags:
  - databricks
  - dependencies
  - udf
timestamp: "2026-06-19T09:47:10.249Z"
---

# Databricks Connect Dependency Management

**Databricks Connect Dependency Management** refers to the methods and best practices for handling library dependencies—JARs, Python files, Egg files, and zip files—when using the [Databricks Connect](/concepts/databricks-connect.md) client library to execute Spark jobs on a remote Databricks cluster.

## Overview

When you write Spark code locally using Databricks Connect and run it on a remote cluster, you must ensure that all external libraries your code depends on are available at runtime on the cluster. Databricks Connect provides dynamic mechanisms to add dependencies without requiring a cluster restart, enabling rapid iteration during development. ^[databricks-connect-databricks-on-aws.md]

### Architecture of Dependency Execution

In the Databricks Connect architecture, different types of code run in different locations:

- **General application code** (Python, Scala) runs on the **local client** side, enabling interactive debugging. These dependencies must be installed locally in your project environment, such as a Python virtual environment. ^[databricks-connect-databricks-on-aws.md]
- **Spark DataFrame APIs** are converted to unresolved logical plans and executed remotely on the **Databricks cluster** through the gRPC-based [Spark Connect](/concepts/spark-connect.md) protocol. No local dependencies are needed for these operations. ^[databricks-connect-databricks-on-aws.md]
- **UDF code** (user-defined functions) runs on **Databricks compute** nodes and requires its dependencies to be installed or distributed to the cluster. This is the primary focus of dependency management in Databricks Connect. ^[databricks-connect-databricks-on-aws.md]

## Adding Dependencies to the Cluster

You can add dependency JARs and Python files programmatically using the SparkContext object within your application. The following methods are supported:

- **`sparkContext.addJar("path-to-the-jar")`** – Adds a JAR file that your code or UDFs depend on. The JAR is uploaded to the cluster and made available for all tasks. ^[databricks-connect-databricks-on-aws.md]
- **`sparkContext.addPyFile("path-to-the-file")`** – Adds a Python file (`.py`), Egg file (`.egg`), or zip file (`.zip`) containing Python modules or dependencies. The file is distributed to worker nodes. ^[databricks-connect-databricks-on-aws.md]

These calls can be placed directly in your Python or Scala code. Every time you run the code from your IDE, the specified dependencies are installed on the cluster. ^[databricks-connect-databricks-on-aws.md]

### Example: Python Dependency

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

# Add a Python module from a local file
sc.addPyFile("lib.py")

# Use the imported class in a distributed operation
print(sc.parallelize(range(10)).map(lambda i: Foo(2)).collect())
```

In the example, `lib.py` defines a class `Foo` that is used in a distributed map operation.^[databricks-connect-databricks-on-aws.md]

### Example: Java UDF JAR

For Java or Scala UDFs packaged as a JAR, you can specify the JAR path in the Spark configuration or add it via `sc._jsc.addJar()`:

```python
spark = SparkSession.builder \
  .config("spark.jars", "/path/to/udf.jar") \
  .getOrCreate()

sc = spark.sparkContext
sc._jsc.addJar("/path/to/udf.jar")
```

This makes the UDF classes available for registration and use in Spark SQL.^[databricks-connect-databricks-on-aws.md]

## Benefits of Dynamic Dependency Management

- **No cluster restart required:** Because each client session is isolated, changing library dependencies does not require restarting the cluster. ^[databricks-connect-databricks-on-aws.md]
- **Rapid iteration:** You can modify and re‑run code with updated dependencies without waiting for cluster reconfiguration. ^[databricks-connect-databricks-on-aws.md]
- **Session isolation:** Dependencies added via `addJar` or `addPyFile` affect only the current client session, not other sessions on the same cluster. ^[databricks-connect-databricks-on-aws.md]

## Limitations and Constraints

The following dependency-related limitations apply when using Databricks Connect:

- **Native Delta table APIs** (e.g., `DeltaTable.forPath`) are not supported for Scala, Python, or R. Use the SQL API (`spark.sql(...)`) or Spark DataFrame API (`spark.read.load`) for [Delta Lake](/concepts/delta-lake.md) operations instead. ^[databricks-connect-databricks-on-aws.md]
- **Python/Scala UDFs from the server's catalog** are not accessible. Only locally introduced UDFs work. ^[databricks-connect-databricks-on-aws.md]
- **Conflicting PySpark installations** must be avoided. The `databricks-connect` package conflicts with PySpark; having both installed can cause "stream corrupted" or "class not found" errors. Uninstall PySpark before installing Databricks Connect. ^[databricks-connect-databricks-on-aws.md]

## Best Practices

- Always uninstall any existing PySpark before installing `databricks-connect` to avoid hidden dependency conflicts. ^[databricks-connect-databricks-on-aws.md]
- Use **virtual environments** (e.g., `venv` or Conda) with a Python version matching the cluster's Python minor version to ensure compatibility. ^[databricks-connect-databricks-on-aws.md]
- For SQL‑only workloads, consider using the Databricks SQL Connector for Python, which is simpler to set up and avoids the complexity of Spark job planning on the client side. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – Client library for remote execution
- [Spark Connect](/concepts/spark-connect.md) – The gRPC-based protocol underlying Databricks Connect
- PySpark UDFs – User-defined functions in PySpark
- [Delta Lake on Databricks](/concepts/delta-lake-on-databricks.md) – Working with Delta tables
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-configured environment with dependencies

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
