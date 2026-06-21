---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ff1f9b09477acdd0e6217b701f97018133bf6488f36ba72700ed27fe3628f24
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-connect-cluster-configuration-requirements
    - DCCCR
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect cluster configuration requirements
description: The target Databricks workspace and cluster must meet specific compute configuration requirements for Databricks Connect to work, including appropriate runtime versions and cluster settings.
tags:
  - databricks
  - cluster
  - configuration
timestamp: "2026-06-19T09:48:51.000Z"
---

# Databricks Connect Cluster Configuration Requirements

**Databricks Connect** enables you to connect IDEs (such as RStudio Desktop), notebook servers, and custom applications to Databricks clusters. For any Databricks Connect client — Python, Scala, or R — the target cluster must meet specific configuration requirements. ^[databricks-connect-for-r-databricks-on-aws.md]

## General Requirements

Your target Databricks workspace and cluster must satisfy the requirements described in the official [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config) documentation. This page covers cluster connectivity, networking, and access control settings needed for Databricks Connect to work. ^[databricks-connect-for-r-databricks-on-aws.md]

## Databricks Runtime Version

Databricks Connect for R (using `sparklyr`) requires a cluster running **Databricks Runtime 13.0 or above**. The tutorial in the source material specifically uses **Databricks Runtime 13.3 LTS and above**, but the integration is noted for Runtime 13.0 and above. ^[databricks-connect-for-r-databricks-on-aws.md]

For other language bindings (Python, Scala), consult the corresponding documentation for supported runtime versions.

## Cluster ID

To connect, you must provide the cluster's **cluster ID**. You can find this ID in the Databricks workspace: navigate to **Compute** → click your cluster's name → the string between `clusters` and `configuration` in the browser address bar is the cluster ID. ^[databricks-connect-for-r-databricks-on-aws.md]

## Authentication

Databricks Connect for R currently supports only **Databricks personal access tokens** for authentication. The token must have appropriate permissions to access the cluster. ^[databricks-connect-for-r-databricks-on-aws.md]

## Limitations

Databricks Connect has limited compatibility with [Apache Spark MLlib](/concepts/apache-spark-mllib.md) because Spark MLlib uses Resilient Distributed Datasets (RDDs), whereas Databricks Connect supports only the **DataFrame API**. If you need to use all of sparklyr's Spark MLlib functions, use Databricks notebooks or the `db_repl` function of the `brickster` package instead. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Overview of the client-server architecture.
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — Python‑specific setup and requirements.
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — Scala‑specific setup and requirements.
- [Personal Access Token Authentication](/concepts/databricks-personal-access-token-pat-authentication.md) — How to create and use PATs.
- Databricks Runtime — Version compatibility and features.
- Spark DataFrame API — The only API supported by Databricks Connect.

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
