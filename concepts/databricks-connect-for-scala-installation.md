---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 77effe08e8a4b703ebd9302061db7f16bb5b3daf84001678a6cf773051c2e4ba
  pageDirectory: concepts
  sources:
    - databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-for-scala-installation
    - DCFSI
    - Databricks Connect Installation
    - Databricks Connect for Scala installation guide
  citations:
    - file: databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect for Scala installation
description: Installation process for setting up Databricks Connect for Scala on a local development machine.
tags:
  - databricks
  - scala
  - installation
timestamp: "2026-06-19T09:48:56.848Z"
---

# [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) installation

**Databricks Connect for Scala installation** refers to the process of setting up the Databricks Connect client library in a local Scala development environment so that it can connect to Databricks compute resources. Databricks Connect allows you to use popular IDEs such as IntelliJ IDEA, notebook servers, and other custom applications to run Spark code against a Databricks cluster. ^[databricks-connect-for-scala-databricks-on-aws.md]

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above. For earlier versions, see the migration guide. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites

Before installing [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), confirm that your workspace and local development environment meet the Databricks Connect usage requirements. You must also choose a Databricks Connect package version that is compatible with your cluster configuration and Databricks Runtime version. ^[databricks-connect-for-scala-databricks-on-aws.md]

For detailed requirements, see [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md). ^[databricks-connect-for-scala-databricks-on-aws.md]

## Installation steps

The full installation instructions for [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) are provided in a dedicated guide. Follow the steps in that guide to add the Databricks Connect library as a dependency to your Scala project and configure the connection to your Databricks workspace. ^[databricks-connect-for-scala-databricks-on-aws.md]

Refer to [Install [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install) for the complete procedure. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Verify the installation

After installation, you can validate the setup by running the tutorial provided by Databricks. See Tutorial: Run code from IntelliJ IDEA on classic compute for a step-by-step walkthrough. ^[databricks-connect-for-scala-databricks-on-aws.md]

## Related resources

- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – Configure the cluster used by Databricks Connect.
- Code examples for Databricks Connect for Scala – Simple examples to get started.
- [Example applications for Databricks Connect](/concepts/example-applications-for-databricks-connect.md)(https://github.com/databricks-demos/dbconnect-examples) – More complex ETL and visualization examples on GitHub.
- Migrate to Databricks Connect for Scala – Guidance for upgrading from Databricks Runtime 12.2 LTS and below.
- [Troubleshooting Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – Common issues and solutions.
- [Databricks Connect Limitations](/concepts/databricks-connect-limitations.md) – Known constraints.

## Sources

- databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-connect-for-scala-databricks-on-aws-9156fcdc.md)
