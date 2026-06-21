---
title: Databricks Connect | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/
ingestedAt: "2026-06-18T08:06:07.370Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

Databricks Connect is a client library for the Databricks Runtime that allows you to connect to Databricks compute from IDEs such as Visual Studio Code, PyCharm, and IntelliJ IDEA, notebooks and any custom application, to enable new interactive user experiences based on your Databricks Lakehouse.

Databricks Connect is available for the following languages:

*   [Databricks Connect for Python](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/)
*   [Databricks Connect for R](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/r/)
*   [Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/)

## What can I do with Databricks Connect?[​](#what-can-i-do-with-databricks-connect "Direct link to What can I do with Databricks Connect?")

Using Databricks Connect, you can write code using Spark APIs and run them remotely on Databricks compute instead of in the local Spark session.

*   **Interactively develop and debug from any IDE**. Databricks Connect enables developers to develop and debug their code on Databricks compute using any IDE's native running and debugging functionality. The [Databricks Visual Studio Code extension](https://docs.databricks.com/aws/en/dev-tools/vscode-ext/) uses Databricks Connect to provide built-in debugging of user code on Databricks.
    
*   **Build interactive data apps**. Just like a JDBC driver, the [Databricks Connect library](https://pypi.org/project/databricks-connect/) can be embedded in any application to interact with Databricks. Databricks Connect provides the full expressiveness of Python through PySpark, eliminating SQL programming language impedance mismatch and enabling you to run all data transformations with Spark on Databricks serverless scalable compute.
    

## How does it work?[​](#how-does-it-work "Direct link to How does it work?")

Databricks Connect is built on open-source [Spark Connect](https://spark.apache.org/spark-connect/), which has a [decoupled client-server architecture](https://www.databricks.com/blog/2022/07/07/introducing-spark-connect-the-power-of-apache-spark-everywhere.html) for Apache Spark that allows remote connectivity to Spark clusters using the DataFrame API. The underlying protocol uses Spark unresolved logical plans and Apache Arrow on top of gRPC. The client API is designed to be thin, so that it can be embedded everywhere: in application servers, IDEs, notebooks, and programming languages.

![Where Databricks Connect code runs](https://docs.databricks.com/aws/en/assets/images/run-debug-code-cacb5aad2cf81e02e77f6e61fc3857ec.png)

*   **General code runs locally**: Python and Scala code runs on the client side, enabling interactive debugging. All code is executed locally, while all Spark code continues to run on the remote cluster.
*   **DataFrame APIs are executed on Databricks compute**. All the data transformations are converted to Spark plans and run on the Databricks compute through the remote Spark session. They are materialized on your local client when you use commands such as `collect()`, `show()`, `toPandas()`.
*   **UDF code runs on Databricks compute**: UDFs defined locally are serialized and transmitted to the cluster where it runs. APIs that run user code on Databricks include: [UDFs](https://docs.databricks.com/aws/en/udf/), `foreach`, `foreachBatch`, and `transformWithState`.
*   For dependencies management:
    *   **Install application dependencies on your local machine**. These run locally and need to be installed as part of your project, such as part of your Python virtual environment.
    *   **Install UDF dependencies on Databricks**. See [Manage UDF dependencies](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/udf#dependencies).

[Spark Connect](https://spark.apache.org/spark-connect/) is an open-source gRPC-based protocol within Apache Spark that allows remote execution of Spark workloads using the DataFrame API.

For Databricks Runtime 13.3 LTS and above, Databricks Connect is an extension of Spark Connect with additions and modifications to support working with Databricks compute modes and Unity Catalog.

## Next steps[​](#next-steps "Direct link to Next steps")

See the following tutorials to quickly begin developing Databricks Connect solutions:

*   [Databricks Connect for Python classic compute tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-cluster)
*   [Databricks Connect for Python serverless compute tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-serverless)
*   [Databricks Connect for Scala classic compute tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/tutorial)
*   [Databricks Connect for Scala serverless compute tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/jar-compile)
*   [Databricks Connect for R tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/r/#tutorial)

To see example applications that use Databricks Connect, see the [GitHub examples repository](https://github.com/databricks-demos/dbconnect-examples), which includes the following examples:

*   [A simple ETL application](https://github.com/databricks-demos/dbconnect-examples/tree/main/python/ETL)
*   [An interactive data application based on Plotly](https://github.com/databricks-demos/dbconnect-examples/tree/main/python/Plotly)
*   [An interactive data application based on Plotly and PySpark AI](https://github.com/databricks-demos/dbconnect-examples/tree/main/python/Plotly-AI)
