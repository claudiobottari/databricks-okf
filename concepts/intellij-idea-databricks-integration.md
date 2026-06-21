---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea7a99a175485bac31772a87cdb7fc4620a934a9633cc978c64ea21c43d33a74
  pageDirectory: concepts
  sources:
    - databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - intellij-idea-databricks-integration
    - IIDI
    - IntelliJ IDEA Integration
  citations:
    - file: databricks-connect-for-scala-databricks-on-aws.md
title: IntelliJ IDEA Databricks Integration
description: Using Databricks Connect for Scala from the IntelliJ IDEA IDE to run Spark code on Databricks compute.
tags:
  - databricks
  - scala
  - ide
  - intellij
timestamp: "2026-06-18T15:04:48.857Z"
---

# IntelliJ IDEA Databricks Integration

**IntelliJ IDEA Databricks Integration** refers to the ability to connect the IntelliJ IDEA IDE to Databricks compute resources using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). This integration allows developers to write, test, and debug Scala code locally in IntelliJ IDEA while executing Spark jobs on a remote Databricks cluster, combining the power of a local IDE with the scalability of the Databricks platform. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Overview

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) enables IntelliJ IDEA (along with other IDEs, notebook servers, and custom applications) to connect directly to a Databricks cluster. The local development environment sends Spark commands to the remote cluster for execution, while the code authoring and debugging experience remains in the local IDE. ^[databricks-connect-for-scala-databricks-on-aws.md]

## How It Works

The integration is built on the Databricks Connect client library for Scala. Instead of running Spark jobs locally, IntelliJ IDEA communicates with a Databricks cluster via the Databricks Connect API. The cluster processes the Spark jobs and returns results to the local environment. This approach lets developers use IntelliJ’s full feature set — code completion, debugging, and refactoring — without needing a local Spark installation. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites

- The workspace and local development environment must meet [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md).
- The Databricks Connect package version must be compatible with the cluster’s Databricks Runtime version.
- The integration is supported for Databricks Runtime 13.3 LTS and above. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Getting Started

To set up the integration:

1. Confirm compatibility and install [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). See [Install Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md).
2. Walk through the official tutorial: Tutorial: Run code from IntelliJ IDEA on classic compute.
3. Configure the compute resource for Databricks Connect. See [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md). ^[databricks-connect-for-scala-databricks-on-aws.md]

## Additional Resources

- Code examples for Databricks Connect for Scala — simple code snippets.
- [Databricks Connect examples repository](https://github.com/databricks-demos/dbconnect-examples) — more complex applications including an ETL example and chart visualizations with JFreeChart.
- Migrate to Databricks Connect for Scala — for upgrading from Databricks Runtime 12.2 LTS and below.
- [Troubleshooting Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) and Limitations — known issues and constraints. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — the overarching framework for connecting external applications to Databricks compute.
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md)
- IntelliJ IDEA — the popular Java/Scala IDE.
- Scala on Databricks — developing Scala applications in the Databricks environment.
- Classic compute — the compute type used in the IntelliJ IDEA tutorial.

## Sources

- databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-connect-for-scala-databricks-on-aws-9156fcdc.md)
