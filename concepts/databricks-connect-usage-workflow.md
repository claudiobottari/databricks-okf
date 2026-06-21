---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2aaa8a14e7c02ce28f4eddc6ef1e87b1af4c1af602a01432efa171a285c8d322
  pageDirectory: concepts
  sources:
    - databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-usage-workflow
    - DCUW
  citations:
    - file: databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect usage workflow
description: "The typical three-step workflow for getting started with Databricks Connect: confirming requirements, installing the package, and walking through a tutorial."
tags:
  - databricks
  - workflow
  - getting-started
timestamp: "2026-06-19T18:10:28.511Z"
---

# Databricks Connect Usage Workflow

**Databricks Connect** enables you to connect popular IDEs (such as IntelliJ IDEA), notebook servers, and other custom applications to Databricks compute. The workflow for using Databricks Connect follows a consistent sequence of steps, from verifying your environment to running your first remote job. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites and Version Selection

Before starting, confirm that your Databricks workspace and local development environment meet the [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements). You must also choose a Databricks Connect package version that is compatible with your Databricks Runtime version. The workflow supports Databricks Runtime 13.3 LTS and above (for Scala) and equivalent versions for Python and R. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Installation

Install the Databricks Connect library for your language:

- **Scala:** See [Install [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install).
- **Python:** See [Databricks Connect for Python](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/).
- **R:** See [Databricks Connect for R](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/r/).

^[databricks-connect-for-scala-databricks-on-aws.md]

## Cluster Configuration

Configure your Databricks cluster to accept remote connections. The cluster must be running and meet the connectivity requirements specified in [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config). For Scala, the default workflow uses a "classic compute" cluster. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Running Code from Your IDE

After installation and cluster setup, you can run your first code from a local IDE. For Scala with IntelliJ IDEA, walk through the [Tutorial: Run code from IntelliJ IDEA on classic compute](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/tutorial). This tutorial demonstrates how to write a simple Spark application locally and have it execute on the remote Databricks cluster. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Exploring Examples and Advanced Workflows

Once the basic workflow is working, consult additional resources to expand your usage:

- **Simple code examples:** See [Code examples for [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/examples).
- **Complex applications:** Explore the [dbconnect-examples](https://github.com/databricks-demos/dbconnect-examples) GitHub repository, which includes a simple ETL application and charts visualizations with JFreeChart.
- **Migration:** If upgrading from Databricks Runtime 12.2 LTS and below, see [Migrate to [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/migrate).
- **Troubleshooting and limitations:** Refer to [troubleshooting](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/troubleshooting) and [limitations](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/limitations) documentation.

^[databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Overview of the connectivity tool.
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — Python-specific usage workflow.
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) — R-specific usage workflow.
- [Cluster Configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) — Detailed setup for remote compute.
- [IntelliJ IDEA Integration](/concepts/intellij-idea-databricks-integration.md) — IDE-specific instructions for Scala.
- [Databricks Runtime Compatibility](/concepts/databricks-runtime-compatibility.md) — Version requirements for Databricks Connect.

## Sources

- databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-connect-for-scala-databricks-on-aws-9156fcdc.md)
