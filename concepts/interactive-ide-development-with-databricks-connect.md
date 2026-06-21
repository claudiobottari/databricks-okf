---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: be7dd153d51477ccaed749d3461c3bb9cd23b2dc54ea3ec15d0b9f3ed2c24ec2
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - interactive-ide-development-with-databricks-connect
    - IIDWDC
    - IDE Development with Databricks
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Interactive IDE Development with Databricks Connect
description: A workflow enabling developers to write Spark code in IDEs like VS Code, PyCharm, and IntelliJ IDEA while running and debugging that code on remote Databricks compute clusters.
tags:
  - ide
  - development-workflow
  - debugging
timestamp: "2026-06-18T11:33:23.171Z"
---

# Interactive IDE Development with Databricks Connect

**Interactive IDE Development with Databricks Connect** refers to the practice of using the Databricks Connect client library to write and debug Apache Spark code from local integrated development environments (IDEs) such as Visual Studio Code, PyCharm, and IntelliJ IDEA, while executing the Spark workloads remotely on Databricks compute. This approach combines the rich editing and debugging capabilities of a local IDE with the scalable processing power of the Databricks Lakehouse. ^[databricks-connect-databricks-on-aws.md]

## Overview

Databricks Connect is a client library for the Databricks Runtime (Databricks Runtime 13.3 LTS and above) that enables remote connectivity to Databricks compute from any application, notebook, or IDE. It is built on the open-source [Spark Connect](https://spark.apache.org/spark-connect/) protocol, which provides a decoupled client-server architecture for Apache Spark using gRPC and Apache Arrow. ^[databricks-connect-databricks-on-aws.md]

Databricks Connect is available for Python, R, and Scala. ^[databricks-connect-databricks-on-aws.md]

## What Can I Do with Databricks Connect?

Using Databricks Connect, developers can write code with Spark APIs and run those operations remotely on Databricks compute instead of a local Spark session. Key capabilities include: ^[databricks-connect-databricks-on-aws.md]

- **Interactively develop and debug from any IDE**. Developers can use their IDE's native running and debugging functionality while the Spark code executes on Databricks. The [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md) leverages Databricks Connect to provide built-in debugging of user code on Databricks. ^[databricks-connect-databricks-on-aws.md]
- **Build interactive data apps**. The Databricks Connect library (available on [PyPI](https://pypi.org/project/databricks-connect/)) can be embedded in any application, similar to a JDBC driver, to interact with Databricks. It provides the full expressiveness of Python through PySpark, eliminating SQL programming-language impedance mismatch and enabling all data transformations with Spark on Databricks serverless scalable compute. ^[databricks-connect-databricks-on-aws.md]

## How It Works

Databricks Connect is built on Spark Connect, which uses a client-server architecture. The underlying protocol transmits Spark unresolved logical plans over gRPC, with Apache Arrow for data serialization. The client API is designed to be thin, allowing it to be embedded in application servers, IDEs, notebooks, and programming languages. ^[databricks-connect-databricks-on-aws.md]

The execution model splits code between local and remote environments: ^[databricks-connect-databricks-on-aws.md]

- **General code runs locally**: Python and Scala code runs on the client side, enabling interactive debugging. All non-Spark code executes locally.
- **DataFrame APIs execute on Databricks compute**: Data transformations are converted to Spark plans and run on the remote Spark session on Databricks. Results are materialized locally when commands such as `collect()`, `show()`, or `toPandas()` are called.
- **UDF code runs on Databricks compute**: User-defined functions (UDFs) defined locally are serialized and transmitted to the cluster for execution. APIs that run user code on Databricks include: UDFs, `foreach`, `foreachBatch`, and `transformWithState`.

![Where Databricks Connect code runs](https://docs.databricks.com/aws/en/assets/images/run-debug-code-cacb5aad2cf81e02e77f6e61fc3857ec.png) ^[databricks-connect-databricks-on-aws.md]

For Databricks Runtime 13.3 LTS and above, Databricks Connect is an extension of Spark Connect with additions and modifications to support working with Databricks compute modes and [Unity Catalog](/concepts/unity-catalog.md). ^[databricks-connect-databricks-on-aws.md]

## Dependencies Management

Managing dependencies for Databricks Connect projects requires a split approach: ^[databricks-connect-databricks-on-aws.md]

- **Install application dependencies on your local machine** – these run locally and should be installed as part of your project (e.g., in a Python virtual environment).
- **Install UDF dependencies on Databricks** – dependencies needed by user-defined functions that run on the cluster must be installed on the Databricks compute. See the documentation on Manage UDF dependencies.

## Next Steps

The following tutorials are available for quickly getting started with Databricks Connect:

- Databricks Connect for Python classic compute tutorial
- Databricks Connect for Python serverless compute tutorial
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) classic compute tutorial
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) serverless compute tutorial
- Databricks Connect for R tutorial

Example applications using Databricks Connect can be found in the [GitHub examples repository](https://github.com/databricks-demos/dbconnect-examples), including a simple ETL application, an interactive data application based on Plotly, and a version using PySpark AI. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md)
- [Spark Connect](/concepts/spark-connect.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Apache Arrow
- gRPC
- User-Defined Functions (UDFs)
- Databricks serverless compute
- PySpark

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
