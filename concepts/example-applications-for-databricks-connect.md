---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a66c84f8753467917a40a968b3e080a7f9b5546aad14d2c9c8c1598d6747416a
  pageDirectory: concepts
  sources:
    - databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - example-applications-for-databricks-connect
    - EAFDC
  citations:
    - file: databricks-connect-for-scala-databricks-on-aws.md
title: Example applications for Databricks Connect
description: Reference code examples, including a simple ETL application and charts visualizations with JFreeChart, demonstrating Databricks Connect usage.
tags:
  - databricks
  - examples
  - etl
  - visualization
timestamp: "2026-06-19T14:47:27.609Z"
---

# Example applications for Databricks Connect

**Example applications for Databricks Connect** are sample projects that demonstrate how to use the Databricks Connect client library to build and run custom applications that connect to a remote Databricks Spark cluster. These examples help developers understand how to set up, configure, and use Databricks Connect in their own workflows.

## Overview

Databricks Connect enables you to connect popular IDEs such as IntelliJ IDEA, notebook servers, and other custom applications to Databricks compute. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Available examples

For more complex code examples beyond the basic tutorial, see the [example applications for Databricks Connect](https://github.com/databricks-demos/dbconnect-examples) repository in GitHub. The following specific examples are available:

- **A simple ETL application** — demonstrates a basic extract, transform, load (ETL) workflow using Databricks Connect with Scala. ^[databricks-connect-for-scala-databricks-on-aws.md]
- **Charts visualizations with JFreeChart** — shows how to create chart visualizations using the JFreeChart library while connected to a Databricks cluster. ^[databricks-connect-for-scala-databricks-on-aws.md]

Both examples are located in the [dbconnect-examples](https://github.com/databricks-demos/dbconnect-examples) repository, specifically under the `scala` directory structure. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Getting started

To begin using Databricks Connect with these examples:

1. Confirm that your workspace and local development environment meet the Databricks Connect requirements. See [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md). ^[databricks-connect-for-scala-databricks-on-aws.md]
2. Choose a Databricks Connect package version that is compatible with your configuration. ^[databricks-connect-for-scala-databricks-on-aws.md]
3. Install Databricks Connect. See [Install Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). ^[databricks-connect-for-scala-databricks-on-aws.md]
4. Walk through the tutorial for running code from IntelliJ IDEA on classic compute. See Tutorial: Run code from IntelliJ IDEA on classic compute. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) — the main client library for connecting remote applications to Databricks.
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — the Scala-specific version of Databricks Connect.
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) — how to configure compute for use with Databricks Connect.
- [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) — system and environment requirements.
- [Install Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — installation instructions.

## Sources

- databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-connect-for-scala-databricks-on-aws-9156fcdc.md)
