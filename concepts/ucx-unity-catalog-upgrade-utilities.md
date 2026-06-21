---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9fbbae6d043d5056af40caa6cd02176585a26ab13646e73b9c4a4445adcc439
  pageDirectory: concepts
  sources:
    - upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ucx-unity-catalog-upgrade-utilities
    - U(CUU
    - UCX utilities
  citations:
    - file: upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
title: UCX (Unity Catalog Upgrade Utilities)
description: A Databricks Labs open-source project providing automation tools to help upgrade non-Unity-Catalog workspaces to Unity Catalog at scale.
tags:
  - databricks
  - unity-catalog
  - migration
  - tooling
timestamp: "2026-06-19T23:17:21.463Z"
---

## UCX ([Unity Catalog](/concepts/unity-catalog.md) Upgrade Utilities)

**UCX ([Unity Catalog](/concepts/unity-catalog.md) Upgrade Utilities)** is a Databricks Labs project that provides tools to help upgrade a non–Unity Catalog workspace to [Unity Catalog](/concepts/unity-catalog.md). It is particularly well-suited for larger-scale migrations. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Overview

The primary purpose of UCX is to automate and simplify the process of migrating workspace-local identities, Hive [Metastore](/concepts/metastore.md) tables, DBFS assets, compute configurations, and jobs to [Unity Catalog](/concepts/unity-catalog.md). The project is maintained under the Databricks Labs umbrella and is not directly supported by Databricks. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Usage

UCX is referenced in the official Databricks upgrade guide as a recommended option for performing the overall upgrade workflow. A guided demonstration is available showing how to use UCX to upgrade to [Unity Catalog](/concepts/unity-catalog.md). For full documentation and installation instructions, refer to the UCX project page: [Use the UCX utilities to upgrade your workspace to [Unity Catalog](/concepts/unity-catalog.md)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/ucx). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The target data governance platform.
- [Hive metastore](/concepts/built-in-hive-metastore.md) — Legacy [Metastore](/concepts/metastore.md) that tables are upgraded from.
- DBFS — Legacy file system that data and assets are migrated away from.
- Account-level identities — Identity model required by [Unity Catalog](/concepts/unity-catalog.md).
- Databricks Labs — Community-driven projects that are not officially supported.

### Sources

- upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws-30141815.md)
