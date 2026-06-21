---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b431771c234df82f8a4a5567cd65d56a25569580ea25417a077870881eb49c9b
  pageDirectory: concepts
  sources:
    - databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-code-examples-and-tutorials
    - tutorials and Databricks Connect code examples
    - DCCEAT
  citations:
    - file: databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect code examples and tutorials
description: Tutorials and example applications demonstrating Databricks Connect for Python, including ETL, Plotly, and PySpark AI examples.
tags:
  - databricks
  - tutorials
  - examples
timestamp: "2026-06-19T18:10:14.956Z"
---

# Databricks Connect Code Examples and Tutorials

**Databricks Connect** enables you to connect popular IDEs (such as PyCharm), notebook servers, and other custom applications to Databricks compute resources. This page catalogs the available code examples and tutorials for getting started with Databricks Connect for Python, Scala, and R.

## Overview

Databricks Connect allows you to develop and run code remotely against Databricks clusters, including both classic compute and serverless compute. The Python API is the primary interface, with additional support for Scala and R. ^[databricks-connect-for-python-databricks-on-aws.md]

## Getting Started Tutorials

The following tutorials walk through the complete setup and first-run experience:

- **Tutorial: Run code from PyCharm on classic compute** – Demonstrates how to connect a local PyCharm IDE to a classic Databricks cluster and execute code. ^[databricks-connect-for-python-databricks-on-aws.md]
- **Tutorial: Run Python code on serverless compute** – Shows how to connect to serverless compute resources for a fully managed execution environment. ^[databricks-connect-for-python-databricks-on-aws.md]

Both tutorials require that you first confirm [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) and install the appropriate package version. ^[databricks-connect-for-python-databricks-on-aws.md]

## Simple Code Examples

For straightforward examples that demonstrate the core API patterns, see the **Code examples for Databricks Connect for Python** documentation. These are designed for quick reference and cover basic DataFrame creation, transformations, and cluster interaction. ^[databricks-connect-for-python-databricks-on-aws.md]

## Example Applications (GitHub Repository)

More complex, end-to-end examples are available in the [dbconnect-examples](https://github.com/databricks-demos/dbconnect-examples) GitHub repository. The Python subdirectory includes:

- **A simple ETL application** (`python/ETL`) – Demonstrates a complete extract, transform, load pipeline using Databricks Connect. ^[databricks-connect-for-python-databricks-on-aws.md]
- **An interactive data application based on Plotly** (`python/Plotly`) – Shows how to build an interactive visualization dashboard using Plotly and Databricks Connect. ^[databricks-connect-for-python-databricks-on-aws.md]
- **An interactive data application based on Plotly and PySpark AI** (`python/Plotly-AI`) – Demonstrates combining Plotly visualizations with PySpark AI capabilities. ^[databricks-connect-for-python-databricks-on-aws.md]

## Additional Examples

- **Spark shell** – Databricks Connect can be used with the Spark shell for interactive exploration. ^[databricks-connect-for-python-databricks-on-aws.md]
- **Databricks Utilities** – See [Databricks Utilities with Databricks Connect for Python](/concepts/databricks-utilities-with-databricks-connect.md) for examples of using `dbutils` within a Databricks Connect session. ^[databricks-connect-for-python-databricks-on-aws.md]

## Related Documentation

- [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) – Prerequisites and version compatibility.
- [Install Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – Installation instructions.
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – Cluster setup for connected sessions.
- [Migrate to Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – Guidance for upgrading from Databricks Runtime 12.2 LTS and below.
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – Scala-specific documentation.
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) – R-specific documentation.
- Troubleshooting Databricks Connect – Common issues and solutions.
- [Limitations of Databricks Connect](/concepts/restricted-dbutils-in-databricks-connect.md) – Known constraints.

## Sources

- databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-connect-for-python-databricks-on-aws.md](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
