---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43052cf3295ea287c7dde61c9eb1120877337dcbd868698db52119125437f2d1
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-github-examples-repository
    - DCGER
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect GitHub Examples Repository
description: A curated collection of example applications demonstrating Databricks Connect usage, including ETL, Plotly visualizations, and PySpark AI integrations
tags:
  - databricks
  - examples
  - github
timestamp: "2026-06-18T10:58:54.818Z"
---

# Databricks Connect GitHub Examples Repository

The **Databricks Connect GitHub Examples Repository** is a public code repository hosted at `github.com/databricks-demos/dbconnect-examples` that provides sample applications demonstrating how to use [Databricks Connect](/concepts/databricks-connect.md) in various real-world scenarios. The repository covers both [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) and [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) use cases.^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Contents

The repository includes several example applications that go beyond basic connectivity, showcasing how to integrate Databricks Connect with popular data science and visualization tools. Notable examples include:^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

- **Simple ETL application** (`python/ETL`) — Demonstrates a basic extract, transform, and load workflow using Databricks Connect.
- **Interactive data application based on Plotly** (`python/Plotly`) — Shows how to combine Databricks Connect with the Plotly visualization library for interactive data exploration.
- **Interactive data application based on Plotly and PySpark AI** (`python/Plotly-AI`) — Extends the Plotly example by incorporating PySpark AI capabilities.

## Purpose

The examples in this repository are intended to complement the official Databricks Connect documentation by providing complete, runnable applications that illustrate best practices for connecting local development environments to Databricks clusters. Developers can use these as templates or reference implementations when building their own Databricks Connect applications.^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Getting Started

To use the examples, you must first set up the Databricks Connect client. The repository assumes that you are using default authentication for Databricks Connect client setup. After cloning the repository, you can run the example scripts directly from your local environment, provided that Databricks Connect is properly configured to connect to a running Databricks cluster.^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The SDK that enables connecting local applications to Databricks clusters
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — Python-specific implementation of Databricks Connect
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — Scala-specific implementation of Databricks Connect
- [DatabricksSession](/concepts/databrickssession.md) — The entry point for creating a Spark session with Databricks Connect
- PySpark AI — AI-enhanced PySpark capabilities featured in one of the examples
- Plotly — The visualization library used in interactive data application examples

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)
