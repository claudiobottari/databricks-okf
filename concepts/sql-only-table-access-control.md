---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 31498c269a04881c5575b1b36f495a03842495fdcde4e883194a7827a5b68844
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sql-only-table-access-control
    - STAC
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: SQL-only Table Access Control
description: A restrictive version of table access control that limits users to SQL commands only, configured via Spark conf spark.databricks.acl.sqlOnly true.
tags:
  - databricks
  - security
  - sql
  - access-control
timestamp: "2026-06-19T18:40:06.464Z"
---

```yaml
---
title: SQL-only Table Access Control
summary: A restrictive mode of Hive [[metastore|Metastore]] table access control that limits users to SQL commands only on a cluster.
sources:
  - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:10:22.488Z"
updatedAt: "2026-06-19T10:21:46.500Z"
tags:
  - databricks
  - access-control
  - sql
aliases:
  - sql-only-table-access-control
  - STAC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# SQL-only Table Access Control

**SQL-only Table Access Control** is a restrictive version of the built-in Hive [[metastore|Metastore]] [[Table Access Control (TACL)|table access control (legacy)]] on Databricks that limits users on a cluster to SQL commands only. It is one of two versions of table access control available for the Hive [[metastore|Metastore]], the other being [[Python and SQL Table Access Control|Python and SQL Table Access Control (legacy)]].^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

This version enforces access privileges defined on [[Hive Metastore Securable Objects|Hive metastore securable objects (legacy)]]. When enabled, users can interact with data only through SQL commands, and access to tables and views is governed by privileges set by administrators.^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enabling SQL-only Table Access Control

To enable SQL-only table access control on a cluster, set the following Spark configuration property in the cluster's Spark configuration:^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

```ini
spark.databricks.acl.sqlOnly true
```

This flag can be set when creating or editing a cluster through the cluster configuration UI.^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## How It Differs from Python and SQL Table Access Control

Unlike the Python and SQL version, enabling SQL-only table access control does **not** depend on the workspace-wide **Enable Table Access Control** setting in the admin security page. That setting controls only the Python and SQL variant.^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Important Notes

- Table access control (any version) is not supported on Machine Learning Runtime clusters.^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]
- Even with table access control enabled, Databricks workspace administrators retain access to file-level data on the cluster.^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]
- SQL-only table access control is available only for the legacy Hive [[metastore|Metastore]]. It does not apply to [[Unity Catalog]].^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]
- For information on setting privileges on Hive [[metastore|Metastore]] objects after enabling table access control, see Hive metastore privileges and securable objects (legacy).^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Related Concepts

- [[Python and SQL Table Access Control|Python and SQL Table Access Control (legacy)]] — The other version that allows Python and DataFrame API alongside SQL
- Hive metastore privileges and securable objects (legacy) — The privilege model used with table access control
- [[Standard access mode]] — Cluster access mode that enables table access control by default
- [[Unity Catalog]] — The modern governance solution that replaces the legacy Hive [[metastore|Metastore]]
- Machine Learning Runtime — A runtime that does not support table access control
- [[Cluster-Scoped Data Access Permissions|Cluster-level permissions]] — Used to enforce table access control by restricting cluster access

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
```

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
