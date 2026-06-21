---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc0cbc1df50df87d900a4404fb7c05de0a8e12cf159504dd9f2ad34934b921e5
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - interactive-development-with-databricks-connect
    - IDWDC
    - Remote Development with Databricks
    - interactive-ide-development-with-databricks-connect
    - IIDWDC
    - IDE Development with Databricks
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Interactive Development with Databricks Connect
description: The ability to develop and debug Spark code from any IDE (VS Code, PyCharm, IntelliJ) with code running remotely on Databricks compute while supporting local debugging.
tags:
  - ide
  - debugging
  - developer-tools
  - databricks
timestamp: "2026-06-19T14:45:12.041Z"
---

# Interactive Development with Databricks Connect

**Interactive Development with Databricks Connect** refers to the practice of using the Databricks Connect client library to write Spark code in local IDEs, notebooks, or custom applications and execute it remotely on Databricks compute. This enables a new set of interactive user experiences that bridge local development workflows with the power of the Databricks Lakehouse. ^[databricks-connect-databricks-on-aws.md]

## Overview

Databricks Connect is a client library for the Databricks Runtime (version 13.3 LTS and above) that allows you to connect to Databricks compute from environments such as Visual Studio Code, PyCharm, and IntelliJ IDEA, notebooks, and any custom application. It is available for [Python](/concepts/python-wheel-task.md), R, and Scala. ^[databricks-connect-databricks-on-aws.md]

## Features

Using Databricks Connect, you can write code using Apache Spark APIs and run those transformations remotely on Databricks compute instead of in a local Spark session. Two primary use cases are highlighted: ^[databricks-connect-databricks-on-aws.md]

- **Interactively develop and debug from any IDE** – Developers can use their favorite IDE's native running and debugging functionality to step through code that executes on Databricks. The [Visual Studio Code Extension for Databricks](/concepts/databricks-visual-studio-code-extension.md) leverages Databricks Connect for built-in debugging on Databricks. ^[databricks-connect-databricks-on-aws.md]
- **Build interactive data apps** – Like a JDBC driver, the Databricks Connect library can be embedded in any application to interact with Databricks. It provides the full expressiveness of Python through PySpark, eliminating the SQL programming language impedance mismatch and enabling all data transformations to run on Databricks serverless scalable compute. ^[databricks-connect-databricks-on-aws.md]

## How It Works

Databricks Connect is built on the open-source [Spark Connect](/concepts/spark-connect.md) framework, which introduces a decoupled client-server architecture for Apache Spark. The underlying protocol uses Spark unresolved logical plans and Apache Arrow on top of gRPC. The client API is designed to be thin so it can be embedded everywhere: in application servers, IDEs, notebooks, and programming languages. ^[databricks-connect-databricks-on-aws.md]

The execution model splits work between the local client and remote Databricks compute: ^[databricks-connect-databricks-on-aws.md]

- **General code runs locally** – Python and Scala code that does not require Spark runs on the client side, enabling interactive debugging. All such code is executed locally while all Spark code continues to run on the remote cluster. ^[databricks-connect-databricks-on-aws.md]
- **DataFrame APIs are executed on Databricks compute** – Every data transformation is converted into a Spark plan and sent to the remote Spark session on Databricks. Results are materialized on the local client only when commands such as `collect()`, `show()`, or `toPandas()` are called. ^[databricks-connect-databricks-on-aws.md]
- **UDF code runs on Databricks compute** – User-defined functions (UDFs) defined locally are serialized and transmitted to the cluster where they execute. This also applies to APIs such as `foreach`, `foreachBatch`, and `transformWithState`. ^[databricks-connect-databricks-on-aws.md]

### Dependencies Management

- **Application dependencies** that run locally must be installed on the local machine as part of the project (e.g., in a Python virtual environment). ^[databricks-connect-databricks-on-aws.md]
- **UDF dependencies** that run on Databricks must be installed on the cluster separately. ^[databricks-connect-databricks-on-aws.md]

## Relationship to Spark Connect

[Spark Connect](/concepts/spark-connect.md) is an open-source, gRPC-based protocol within Apache Spark that enables remote execution of Spark workloads using the DataFrame API. For Databricks Runtime 13.3 LTS and above, Databricks Connect is an extension of Spark Connect with additions and modifications to support working with Databricks compute modes and [Unity Catalog](/concepts/unity-catalog.md). ^[databricks-connect-databricks-on-aws.md]

## Next Steps

To get started quickly, see the following tutorials: ^[databricks-connect-databricks-on-aws.md]

- [Databricks Connect for Python classic compute tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-cluster)
- [Databricks Connect for Python serverless compute tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-serverless)
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) classic compute tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/tutorial)
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) serverless compute tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/jar-compile)
- [Databricks Connect for R tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/r/#tutorial)

Example applications are available in the [GitHub examples repository](https://github.com/databricks-demos/dbconnect-examples), including a simple ETL application, an interactive data application based on Plotly, and an interactive data application based on Plotly and PySpark AI. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md)
- Databricks Runtime 13.3 LTS and above
- [Unity Catalog](/concepts/unity-catalog.md)
- DataFrame API
- [Visual Studio Code Extension for Databricks](/concepts/databricks-visual-studio-code-extension.md)
- PySpark
- gRPC
- Apache Spark
- User-Defined Functions (UDFs)

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
