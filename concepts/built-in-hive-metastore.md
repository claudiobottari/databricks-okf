---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9d11c35ec29f9d8f8d70c2171534480b873405f0f1d15ca4a7e996085423444
  pageDirectory: concepts
  sources:
    - hive-metastore-table-access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - built-in-hive-metastore
    - BHM
    - Hive Metastore
    - Hive metastore
    - workspace-built-in-hive-metastore
    - WBHM
  citations:
    - file: hive-metastore-table-access-control-legacy-databricks-on-aws.md
title: Built-in Hive Metastore
description: A per-workspace managed service in Databricks that deploys an instance to each cluster and provides centralized metadata storage for the workspace's Hive tables.
tags:
  - databricks
  - architecture
  - metadata
timestamp: "2026-06-19T19:04:32.890Z"
---

# Built-in Hive [Metastore](/concepts/metastore.md)

The **built-in Hive metastore** is a managed metadata service that is deployed with every Databricks workspace. It provides a central, per-workspace repository for table and view metadata, and each cluster runs an instance of the [Metastore](/concepts/metastore.md) to securely access that metadata. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Architecture

An instance of the built-in Hive [Metastore](/concepts/metastore.md) deploys to each cluster and retrieves metadata from a central repository that is scoped to the workspace. By default, when a cluster is created, all users can access all data objects managed by the built-in Hive [Metastore](/concepts/metastore.md) — unless **table access control** is explicitly enabled for that cluster. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Access Control (Legacy)

Table access control is a feature of the built-in Hive [Metastore](/concepts/metastore.md) that allows administrators to programmatically grant and revoke permissions on data objects using Python or SQL commands. When table access control is enabled on a cluster, users can set privileges on tables, views, databases, and other securable objects that are accessed through that cluster. This provides a finer-grained security model than the default "all-access" behavior. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

### Requirements for Table Access Control

- The workspace must be on the [Premium plan or above](https://databricks.com/product/pricing/platform-addons).
- The cluster must be a Data Science & Engineering cluster with the [appropriate configuration](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/table-acl), or a SQL warehouse.
^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Legacy Status and Migration

Databricks considers Hive [Metastore](/concepts/metastore.md) table access control a **legacy** data governance model. The recommended approach is to **upgrade** tables managed by the built-in Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md). Unity Catalog simplifies security and governance by providing a central place to administer and audit data access across multiple workspaces within an account. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The modern data governance solution that replaces the built-in Hive [Metastore](/concepts/metastore.md).
- [Hive metastore](/concepts/built-in-hive-metastore.md) – The underlying metadata store technology.
- [Table access control](/concepts/table-access-control-tacl.md) – Legacy permission system for the built-in Hive [Metastore](/concepts/metastore.md).
- Databricks cluster – The compute environment that hosts an instance of the [Metastore](/concepts/metastore.md).
- SQL warehouse – Compute environment that also supports table access control.

## Sources

- hive-metastore-table-access-control-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-table-access-control-legacy-databricks-on-aws.md](/references/hive-metastore-table-access-control-legacy-databricks-on-aws-d8a45857.md)
