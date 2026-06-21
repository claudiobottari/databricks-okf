---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 800d65a24ba87cd3040b13587c3df74946b8632bf3ce37f1bbd422f8009c6f58
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-interactive-development
    - DCID
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Databricks Connect Interactive Development
description: The capability to interactively develop and debug Spark code from IDEs (VS Code, PyCharm, IntelliJ) and build interactive data applications using Databricks compute instead of local Spark sessions.
tags:
  - databricks
  - ide
  - interactive-development
  - debugging
timestamp: "2026-06-19T09:47:08.109Z"
---

# Databricks Connect Interactive Development

**Databricks Connect Interactive Development** refers to the workflow of using the [Databricks Connect](/concepts/databricks-connect.md) client library to interactively develop and debug Spark applications from local IDEs, notebooks, or custom applications while executing Spark operations remotely on Databricks compute infrastructure.

## Overview

Databricks Connect is a client library for the Databricks Runtime that allows you to connect to Databricks compute from development environments such as Visual Studio Code, PyCharm, IntelliJ IDEA, notebooks, and custom applications. This enables new interactive user experiences based on your Databricks Lakehouse. ^[databricks-connect-databricks-on-aws.md]

Databricks Connect is available for [Python](/concepts/python-wheel-task.md), R, and Scala programming languages. ^[databricks-connect-databricks-on-aws.md]

## Capabilities

### Interactive Development and Debugging from IDEs

Databricks Connect allows developers to write code using Spark APIs and run it remotely on Databricks compute instead of in a local Spark session. Developers can develop and debug their code on Databricks compute using any IDE's native running and debugging functionality. The [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md) uses Databricks Connect to provide built-in debugging of user code on Databricks. ^[databricks-connect-databricks-on-aws.md]

### Building Interactive Data Applications

Like a JDBC driver, the Databricks Connect library can be embedded in any application to interact with Databricks. It provides the full expressiveness of Python through PySpark, eliminating SQL programming language impedance mismatch and enabling all data transformations to run with Spark on Databricks serverless scalable compute. ^[databricks-connect-databricks-on-aws.md]

## Architecture and Execution Model

Databricks Connect is built on open-source [Spark Connect](/concepts/spark-connect.md), which has a decoupled client-server architecture for Apache Spark that allows remote connectivity to Spark clusters using the DataFrame API. The underlying protocol uses Spark unresolved logical plans and Apache Arrow on top of gRPC. The client API is designed to be thin so that it can be embedded everywhere: in application servers, IDEs, notebooks, and programming languages. ^[databricks-connect-databricks-on-aws.md]

The execution model distributes code execution as follows: ^[databricks-connect-databricks-on-aws.md]

- **General code runs locally**: Python and Scala code runs on the client side, enabling interactive debugging. All non-Spark code is executed locally.
- **DataFrame APIs are executed on Databricks compute**: All data transformations are converted to Spark plans and run on the Databricks compute through the remote Spark session. Results are materialized on the local client when using commands such as `collect()`, `show()`, or `toPandas()`.
- **UDF code runs on Databricks compute**: User-Defined Functions (UDFs) defined locally are serialized and transmitted to the cluster where they execute. Other APIs that run user code on Databricks include `foreach`, `foreachBatch`, and `transformWithState`.

## Dependencies Management

- **Application dependencies**: Install application dependencies on your local machine as part of your project, such as in your Python virtual environment. These run locally. ^[databricks-connect-databricks-on-aws.md]
- **UDF dependencies**: Install UDF dependencies on Databricks. See Manage UDF Dependencies for details. ^[databricks-connect-databricks-on-aws.md]

## Requirements

Databricks Connect for Databricks Runtime 13.3 LTS and above is built on Spark Connect with additions and modifications to support working with Databricks compute modes and [Unity Catalog](/concepts/unity-catalog.md). ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md) — The open-source gRPC-based protocol underpinning Databricks Connect
- Databricks Runtime — The compute environment that runs on Databricks clusters
- PySpark — The Python API for Apache Spark used with Databricks Connect
- [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md) — IDE integration using Databricks Connect
- Remote Spark Session — The mechanism for executing Spark operations remotely

## Example Applications

Example applications are available in the [GitHub examples repository](https://github.com/databricks-demos/dbconnect-examples), including: ^[databricks-connect-databricks-on-aws.md]

- A simple ETL application
- An interactive data application based on Plotly
- An interactive data application based on Plotly and PySpark AI

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
