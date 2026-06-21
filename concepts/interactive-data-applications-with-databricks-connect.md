---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a58fb7ae92730c87b0bebd9dc127331e0fd93359dc671245e68e36f0e908f75
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - interactive-data-applications-with-databricks-connect
    - IDAWDC
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Interactive Data Applications with Databricks Connect
description: The ability to embed Databricks Connect in applications (like JDBC but with full PySpark expressiveness) to build interactive data apps that leverage Databricks serverless compute.
tags:
  - applications
  - interactive
  - databricks
timestamp: "2026-06-19T18:09:36.952Z"
---

# Interactive Data Applications with Databricks Connect

**Interactive Data Applications with Databricks Connect** refers to embedding the [Databricks Connect](/concepts/databricks-connect.md) client library into custom applications — such as dashboards, analytics tools, or web services — to interact with Databricks Lakehouse using the full PySpark DataFrame API over a remote connection. This approach eliminates the need for SQL-only interfaces and allows developers to build rich, programmatic data experiences on top of Databricks serverless or classic compute.

## Overview

Databricks Connect is built on [Spark Connect](/concepts/spark-connect.md), an open-source gRPC-based protocol that decouples the Spark client from the server. By embedding the thin `databricks-connect` library, any application can submit [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) operations directly to a remote Databricks cluster without running a local Spark session. This enables interactive data applications that combine local Python logic with remote, scalable data processing. ^[databricks-connect-databricks-on-aws.md]

Just like a JDBC driver, the Databricks Connect library can be embedded in any application to interact with Databricks. It provides the full expressiveness of Python through PySpark, eliminating the SQL programming language impedance mismatch and enabling you to run all data transformations with Spark on Databricks serverless scalable compute. ^[databricks-connect-databricks-on-aws.md]

## Architecture

Databricks Connect uses a client-server architecture where the client is a small, embeddable library and the server runs on Databricks compute. ^[databricks-connect-databricks-on-aws.md]

- **General code (Python, Scala) runs locally** on the client machine, enabling interactive debugging and seamless integration with existing application logic. ^[databricks-connect-databricks-on-aws.md]
- **DataFrame APIs are executed remotely** on Databricks compute. All data transformations are converted to Spark plans and sent over gRPC to the remote Spark session. Results are materialized locally only when using actions like `collect()`, `show()`, or `toPandas()`. ^[databricks-connect-databricks-on-aws.md]
- **UDFs and user code** that runs on the cluster (e.g., `udf`, `foreach`, `foreachBatch`, `transformWithState`) are serialized and transmitted to Databricks compute. ^[databricks-connect-databricks-on-aws.md]

The underlying protocol uses unresolved logical plans and Apache Arrow for efficient data transfer. ^[databricks-connect-databricks-on-aws.md]

## Building an Interactive Data Application

To embed Databricks Connect in an application:

1. Install the `databricks-connect` Python package in your project environment.
2. Configure the connection to a Databricks workspace and cluster (classic or serverless).
3. Write application code using standard PySpark DataFrame APIs.
4. Run the application locally; all Spark operations execute on the remote Databricks compute.

Because the client is thin, it can be included in:
   - Web application backends (e.g., Flask, FastAPI)
   - Desktop or CLI tools
   - Jupyter or IDEs like Visual Studio Code, PyCharm, IntelliJ IDEA
   - Scheduled or event-driven data services

## Benefits

- **Full Python/PySpark expressiveness** – Use Python loops, conditionals, libraries, and pandas-like syntax alongside Spark transformations, avoiding the limitations of SQL-only query builders. ^[databricks-connect-databricks-on-aws.md]
- **Scalable serverless compute** – Applications can leverage Databricks serverless compute, paying only for the resources used during data processing. ^[databricks-connect-databricks-on-aws.md]
- **Interactive debugging** – Because general application code runs locally, developers can use standard IDE debugging tools (breakpoints, step-through) while Spark logic executes remotely. ^[databricks-connect-databricks-on-aws.md]
- **Reduced infrastructure** – No need to maintain local Spark clusters; all processing is offloaded to Databricks.

## Example Applications

Databricks provides example applications in the [GitHub examples repository](https://github.com/databricks-demos/dbconnect-examples), including:

- A simple ETL pipeline using Databricks Connect
- An interactive data application based on Plotly
- An interactive data application based on Plotly and PySpark AI

These demonstrate how to combine Databricks Connect with popular visualization libraries and AI capabilities. ^[databricks-connect-databricks-on-aws.md]

## Next Steps

To get started building interactive data applications:

- Follow the [Databricks Connect for Python classic compute tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-cluster)
- Follow the [Databricks Connect for Python serverless compute tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-serverless)
- Review the [example applications repository](https://github.com/databricks-demos/dbconnect-examples)

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables remote Spark execution
- [Spark Connect](/concepts/spark-connect.md) — The underlying open-source protocol for decoupled Spark clients
- PySpark DataFrame API — The primary API used in interactive applications
- Databricks Serverless Compute — The compute mode often paired with Databricks Connect
- [Visual Studio Code Extension for Databricks](/concepts/databricks-visual-studio-code-extension.md) — Uses Databricks Connect for built-in debugging

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
