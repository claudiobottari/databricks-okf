---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1a4deb46d5e5f16d8ee21c5f73d9f0223cddc0da0e2c6b6dd640b5596381452
  pageDirectory: concepts
  sources:
    - databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-with-serverless-compute
    - DCWSC
    - Connect to serverless compute
  citations:
    - file: databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect with Serverless Compute
description: Support for running Python code on Databricks serverless compute via Databricks Connect
tags:
  - databricks
  - serverless
  - python
timestamp: "2026-06-18T11:34:16.058Z"
---

# Databricks Connect with Serverless Compute

Databricks Connect lets you run PySpark code from your local IDE (such as PyCharm), notebook server, or custom application, while the execution happens on a Databricks cluster. When configured with serverless compute, your local Python processes connect to a serverless endpoint that executes Spark operations without requiring a classic, always-on cluster. This approach simplifies infrastructure management and reduces startup latency. ^[databricks-connect-for-python-databricks-on-aws.md]

## Overview

Serverless compute for Databricks Connect is supported for **Databricks Runtime 13.3 LTS and above**. The integration allows you to develop and test Spark applications locally while leveraging the fully managed, auto-scaling serverless compute environment. Databricks provides a dedicated tutorial for running Python code on serverless compute. ^[databricks-connect-for-python-databricks-on-aws.md]

## Requirements

Before using Databricks Connect with serverless compute, confirm that both your workspace and local development environment meet the prerequisites:

- **Workspace**: Must have serverless compute enabled. See [Serverless Compute in Databricks](/concepts/serverless-gpu-compute-on-databricks.md) for enabling instructions.
- **Databricks Connect version**: Choose a package version compatible with your Databricks Runtime and serverless compute configuration. Refer to the [usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements).
- **Local environment**: Python 3.8 or later, with the `databricks-connect` package installed. ^[databricks-connect-for-python-databricks-on-aws.md]

## Getting Started

1. Install Databricks Connect for Python. See [Install Databricks Connect for Python](/concepts/databricks-connect-for-python.md).
2. Configure your IDE or notebook to point to your Databricks workspace and use serverless compute as the target.
3. Walk through the tutorial: [Tutorial: Run Python code on serverless compute](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-serverless).

The tutorial covers creating a Spark session, running DataFrames, and debugging locally while the workload executes on the serverless endpoint. ^[databricks-connect-for-python-databricks-on-aws.md]

## Additional Resources

- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) — Settings for classic clusters and serverless endpoints.
- Code Examples for Databricks Connect for Python — Simple snippets to verify connectivity.
- Example Applications — Full projects on GitHub, including ETL and Plotly-based interactive apps.
- Troubleshooting Databricks Connect — Common issues and solutions.
- [Limitations of Databricks Connect](/concepts/limitations-of-dbutils-in-databricks-connect.md) — Known restrictions when using serverless compute. ^[databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The general client library for remote Spark execution.
- Serverless Compute — Databricks’ on-demand, auto-scaling compute model.
- PySpark — The Python API for Apache Spark that runs on the connected compute.
- Databricks Runtime — The execution environment versioned alongside Databricks Connect.

## Sources

- databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-connect-for-python-databricks-on-aws.md](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
