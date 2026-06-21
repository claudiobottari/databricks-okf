---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94799350dd0a8023904db71523167c75f02c5ac91b5e818f22e07fa3c4b5670f
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - standard-access-mode-for-clusters
    - SAMFC
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Standard Access Mode for Clusters
description: A Databricks cluster access mode that enables table access control by default, as opposed to legacy modes that require explicit configuration.
tags:
  - databricks
  - clusters
  - access-mode
timestamp: "2026-06-18T12:10:35.922Z"
---

# Standard Access Mode for Clusters

**Standard Access Mode** is one of the available access modes for Databricks clusters. When a cluster is configured in Standard Access Mode, [Table Access Control](/concepts/table-access-control-tacl.md) (also known as Hive [Metastore](/concepts/metastore.md) table access control) is enabled by default on that cluster. This means that data access on the cluster is governed by the privileges set on Hive [Metastore](/concepts/metastore.md) securable objects, such as tables, views, and databases. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Table Access Control in Standard Access Mode comes in two versions, which determine the type of commands users can run: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- **SQL-only table access control** – restricts users to SQL commands only.
- **Python and SQL table access control** – allows users to run SQL commands and Python code that uses the DataFrame API, subject to the same access restrictions.

Because table access control is enabled by default in Standard Access Mode, users on these clusters cannot access data for which they have not been granted the necessary privileges, unless they are a workspace administrator (who retains file-level access). ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

When creating a new cluster in the UI or via the API, Standard Access Mode is one of the available access mode options. Workspace administrators can enforce table access control by restricting users to clusters that use this mode. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore Privileges and Securable Objects (Legacy)](/concepts/hive-metastore-privileges-and-securable-objects.md) — How to set privileges on objects protected by table access control.
- Cluster Access Modes — Overview of other access modes (e.g., Single User, Shared, No Isolation).
- [Table Access Control](/concepts/table-access-control-tacl.md) — The full documentation for enabling and managing table access control in the Hive [Metastore](/concepts/metastore.md).

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
