---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71eaa48f9b9ee034a88d0ea022f3fd1841f7f150f23164a713a7265e81fac7af
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-visual-studio-code-extension
    - DVSCE
    - Databricks VS Code Extension
    - VS Code
    - Visual Studio Code Extension for Databricks
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Databricks Visual Studio Code Extension
description: A VS Code extension that uses Databricks Connect to provide built-in debugging of user code on Databricks compute.
tags:
  - databricks
  - vscode
  - extension
  - debugging
timestamp: "2026-06-19T09:47:01.657Z"
---

# Databricks Visual Studio Code Extension

The **Databricks Visual Studio Code Extension** is an official extension for Visual Studio Code that provides integrated development capabilities for Databricks, allowing developers to write, run, and debug code against Databricks compute directly from their local IDE. ^[databricks-connect-databricks-on-aws.md]

## Overview

The extension connects to Databricks compute using [Databricks Connect](/concepts/databricks-connect.md), which is a client library for the Databricks Runtime built on [Spark Connect](/concepts/spark-connect.md). This connection enables developers to run code remotely on Databricks compute while editing locally in Visual Studio Code, providing the responsiveness of a local IDE with the power of distributed Databricks compute. ^[databricks-connect-databricks-on-aws.md]

## Key Capabilities

### Interactive Development and Debugging

The extension uses Databricks Connect to provide built-in debugging of user code on Databricks. Developers can use Visual Studio Code's native running and debugging functionality while their code executes on Databricks compute. This allows for interactive development and debugging workflows directly from the IDE. ^[databricks-connect-databricks-on-aws.md]

### Remote Code Execution

Using the extension, you can write code using Spark APIs and run them remotely on Databricks compute instead of in a local Spark session. The execution model separates concerns: ^[databricks-connect-databricks-on-aws.md]

- **General code runs locally**: Python and Scala code executes on the client side, enabling interactive debugging with full Visual Studio Code debugging features.
- **DataFrame APIs execute on Databricks compute**: All data transformations are converted to Spark plans and run on the Databricks compute through the remote Spark session. Results are materialized on the local client when using commands such as `collect()`, `show()`, or `toPandas()`.
- **UDF code runs on Databricks compute**: User-defined functions defined locally are serialized and transmitted to the cluster where they execute.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that powers the extension's remote execution capabilities
- [Spark Connect](/concepts/spark-connect.md) — The open-source gRPC-based protocol enabling remote Spark execution
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-built runtime that includes GPU support and common libraries
- Visual Studio Code — The IDE platform for this extension

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
