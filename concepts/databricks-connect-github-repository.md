---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: acd271cc042106a1d450a5a1c0a540f9126744495db968e754abb79a980f7345
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-github-repository
    - DCGR
    - MLflow GitHub repository
    - git repository
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect GitHub repository
description: A GitHub repository (dbconnect-examples) containing example applications for Databricks Connect including ETL and Plotly-based interactive apps
tags:
  - databricks
  - examples
  - github
timestamp: "2026-06-18T14:37:36.327Z"
---

# Databricks Connect GitHub Repository

The **Databricks Connect GitHub repository** is a public collection of example applications hosted at `github.com/databricks-demos/dbconnect-examples` that demonstrate how to use Databricks Connect in various real-world scenarios. The repository contains sample code for both Python and Scala, covering use cases from simple ETL pipelines to interactive data visualization applications. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Overview

Databricks Connect enables developers to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. The GitHub repository provides ready-to-run examples that illustrate common integration patterns, helping developers understand how to structure their own Databricks Connect projects. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Example Applications

The repository includes several example applications for Python:

### Simple ETL Application

A basic extract, transform, load (ETL) pipeline that demonstrates core Databricks Connect workflows, including reading from tables, creating DataFrames, and writing results back to the cluster. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Interactive Data Application with Plotly

An application showcasing how to build interactive data visualizations using the Plotly library, connected to Databricks clusters through Databricks Connect. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Interactive Data Application with Plotly and PySpark AI

An extended version of the Plotly example that incorporates PySpark AI capabilities, demonstrating how to combine interactive visualization with AI-driven data analysis. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Code Examples in the Repository

The repository supplements the documentation-based examples found in the official Databricks Connect guides. Documentation examples cover foundational operations such as:

- **Reading a table**: Querying existing tables and displaying their contents using `spark.read.table()`. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]
- **Creating a DataFrame**: Building in-memory DataFrames, saving them as tables on the cluster, and running SQL queries against those tables. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]
- **Using [DatabricksSession](/concepts/databrickssession.md) or SparkSession**: Writing portable code that works in environments with or without the `DatabricksSession` class available. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The underlying technology that enables remote connections to Databricks clusters
- [DatabricksSession](/concepts/databrickssession.md) — The primary entry point for creating Spark sessions in Databricks Connect
- PySpark AI — AI-enhanced PySpark capabilities demonstrated in the repository's examples
- Plotly Integration with Databricks — Interactive visualization library used in the example applications
- ETL Pipelines on Databricks — Broader context for the ETL example in the repository

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)
