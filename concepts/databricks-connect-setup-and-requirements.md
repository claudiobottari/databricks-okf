---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3016ce339c85eade8d82b6882ffa6a233f421f7c54e8ac9c3ccc682d9c499549
  pageDirectory: concepts
  sources:
    - databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-setup-and-requirements
    - requirements and Databricks Connect setup
    - DCSAR
    - Installation Requirements for Databricks Connect
  citations:
    - file: databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect setup and requirements
description: Prerequisites, installation steps, and compatibility requirements for using Databricks Connect in a local development environment.
tags:
  - databricks
  - installation
  - setup
timestamp: "2026-06-19T14:46:28.290Z"
---

## Databricks Connect Setup and Requirements

**Databricks Connect** enables you to connect popular IDEs (such as PyCharm), notebook servers, and other custom applications to Databricks compute resources. This allows you to develop and run code locally while executing it remotely on a Databricks cluster or serverless compute. ^[databricks-connect-for-python-databricks-on-aws.md]

This page covers setup and requirements for Databricks Connect for Python, which is supported for Databricks Runtime 13.3 LTS and above. For Scala or R versions, see the respective documentation. ^[databricks-connect-for-python-databricks-on-aws.md]

### Requirements

Before installing Databricks Connect, you must confirm that both your Databricks workspace and local development environment meet the necessary requirements. These include compatibility between the Databricks Connect package version, the Databricks Runtime version, and your local Python environment. The full list of requirements is documented in the [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) guide. ^[databricks-connect-for-python-databricks-on-aws.md]

### Installation

Installation is done via pip. For detailed instructions, see the [Install Databricks Connect for Python](/concepts/databricks-connect-for-python.md) guide. ^[databricks-connect-for-python-databricks-on-aws.md]

### Getting Started

After satisfying the requirements and installing the package, you can proceed with a tutorial that matches your intended compute type:

- Tutorial: Run code from PyCharm on classic compute
- Tutorial: Run Python code on serverless compute

^[databricks-connect-for-python-databricks-on-aws.md]

### Additional Resources

The following resources provide further guidance for setting up and using Databricks Connect:

- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – How to configure your Databricks cluster for use with Databricks Connect.
- Databricks Connect for Python code examples – Simple code snippets to get started.
- Databricks Connect example applications (GitHub) – More complex examples including ETL, interactive data apps, and Plotly with PySpark AI.
- [Databricks Utilities with Databricks Connect for Python](/concepts/databricks-utilities-with-databricks-connect.md) – Using `dbutils` in a connected environment.
- [Migrate to Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – Guidance for upgrading from Databricks Runtime 12.2 LTS and below.
- Databricks Connect for Python troubleshooting and [Databricks Connect for Python limitations](/concepts/databricks-connect-limitations.md).

^[databricks-connect-for-python-databricks-on-aws.md]

### Sources

- databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-connect-for-python-databricks-on-aws.md](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
