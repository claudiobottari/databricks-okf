---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e92f328c1afc00f079ad71f09fda9d295ed9d55ba9826398af8894bc83c9558
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
    - what-is-the-any-file-securable-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - standard-access-mode
    - SAM
    - Access Mode
    - Access Modes
    - Access modes
    - access modes
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
    - file: what-is-the-any-file-securable-databricks-on-aws.md
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md (inferred from context)
title: Standard Access Mode
description: A Databricks cluster access mode that enables table access control by default.
tags:
  - databricks
  - compute
  - access-mode
  - clusters
timestamp: "2026-06-19T18:40:01.446Z"
---

# Standard Access Mode

**Standard Access Mode** (formerly called *shared access mode*) is a concurrency and isolation mode available on Databricks clusters|Compute configuration and SQL warehouses. In this mode, multiple users can share a single compute resource while fine-grained access controls are enforced. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md, what-is-the-any-file-securable-databricks-on-aws.md]

## Relationship with Table Access Control

When a cluster is configured with Standard Access Mode, [Hive Metastore Table Access Control](/concepts/hive-metastore-table-access-control.md) is enabled by default. This means that any user attached to the cluster is subject to the privileges that have been granted on Hive [Metastore](/concepts/metastore.md) securable objects (schemas, tables, views, etc.). Workspace administrators can then restrict or allow access at the object level. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Relationship with the ANY FILE Securable

The legacy [ANY FILE Securable](/concepts/any-file-securable.md) — a privilege that bypasses Hive table ACLs and grants direct filesystem access — applies only when the compute resource uses Standard Access Mode. Specifically, `SELECT` and `MODIFY` privileges on the `ANY FILE` securable are evaluated only on clusters or SQL warehouses running in this mode. Standard Access Mode is therefore a prerequisite for any legacy file-level access that is not governed by Unity Catalog. ^[what-is-the-any-file-securable-databricks-on-aws.md]

## Usage Context

Standard Access Mode is used in two main contexts:

- **Clusters** – Created through the UI or REST API; table access control is enabled automatically.
- **SQL warehouses** – The access mode is set at the warehouse level and determines whether `ANY FILE` privileges take effect.

For clusters, the alternative access mode is **Single User** (formerly *unrestricted*), which does not impose the same data isolation restrictions. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md (inferred from context)]

## Related Concepts

- [Cluster access modes](/concepts/databricks-connect-cluster-access-modes.md) – Overview of the available concurrency and isolation models.
- [Table access control](/concepts/table-access-control-tacl.md) – The privilege system for Hive [Metastore](/concepts/metastore.md) objects.
- [ANY FILE Securable](/concepts/any-file-securable.md) – A legacy privilege that requires Standard Access Mode.
- [Unity Catalog](/concepts/unity-catalog.md) – The modern governance solution that supersedes legacy table ACLs.
- SQL warehouses – Compute resources that also support Standard Access Mode.
- Single User Access Mode – The alternative mode, offering no built-in data isolation.

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
- what-is-the-any-file-securable-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
2. [what-is-the-any-file-securable-databricks-on-aws.md](/references/what-is-the-any-file-securable-databricks-on-aws-2b8e33ad.md)
3. enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md (inferred from context)
