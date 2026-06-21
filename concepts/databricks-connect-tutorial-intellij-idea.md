---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d6a5bdf8e4e89ecabb492e54aa869698507c27f0f69b57ad44f093f7c06bd82
  pageDirectory: concepts
  sources:
    - databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-tutorial-intellij-idea
    - DCT(I
  citations:
    - file: databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect tutorial (IntelliJ IDEA)
description: A walkthrough guide for running Scala code from IntelliJ IDEA on classic Databricks compute using Databricks Connect.
tags:
  - databricks
  - scala
  - tutorial
  - intellij
timestamp: "2026-06-19T09:49:03.252Z"
---

# Databricks Connect tutorial (IntelliJ IDEA)

**Databricks Connect tutorial (IntelliJ IDEA)** is a guided walkthrough that shows how to use [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) to run Scala code from the IntelliJ IDEA IDE directly against a Databricks cluster (classic compute). The tutorial is designed for users who have already confirmed that their workspace and local environment meet the requirements and have installed the appropriate Databricks Connect package.^[databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites

Before starting the tutorial, you must:

- Verify that your workspace and local development environment satisfy the [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md).
- Choose a Databricks Connect package version that is compatible with your Databricks Runtime version (13.3 LTS and above).^[databricks-connect-for-scala-databricks-on-aws.md]
- Install [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). See [Install [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install).^[databricks-connect-for-scala-databricks-on-aws.md]

The tutorial assumes you have an active Databricks workspace with a running cluster (classic compute) and that IntelliJ IDEA is configured with the necessary Scala plugin.

## What the tutorial covers

The tutorial, titled **“Run code from IntelliJ IDEA on classic compute,”** walks you through the following steps:

1. Setting up your IntelliJ IDEA project to use Databricks Connect.
2. Configuring the connection to your Databricks cluster.
3. Running sample Spark code from IntelliJ IDEA and observing the results on the remote compute.^[databricks-connect-for-scala-databricks-on-aws.md]

The tutorial is the primary hands-on resource for getting started with [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). It is referenced from the Databricks Connect documentation and can be accessed directly from the following link: [Tutorial: Run code from IntelliJ IDEA on classic compute](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/tutorial).^[databricks-connect-for-scala-databricks-on-aws.md]

## Additional resources

After completing the tutorial, you can explore more complex examples and best practices:

- Databricks Connect for Scala code examples – Simple code snippets.
- Databricks Connect example applications – Full applications such as a simple ETL pipeline and JFreeChart visualizations (available on GitHub).
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – Tuning cluster settings for Databricks Connect.
- Migrate to Databricks Connect for Scala – Guidance for upgrading from Databricks Runtime 12.2 LTS and below.^[databricks-connect-for-scala-databricks-on-aws.md]

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The overall framework connecting local IDEs to Databricks.
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – Python counterpart.
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) – R counterpart.
- Classic compute – The type of compute used in the tutorial.
- IntelliJ IDEA – The IDE used in the tutorial.

## Sources

- databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-connect-for-scala-databricks-on-aws-9156fcdc.md)
