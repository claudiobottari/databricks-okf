---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7170a0a5cfb1c0b7e617e4b611dc20d18ca568c42adc2a2532d5c3b10bcaca8
  pageDirectory: concepts
  sources:
    - hive-metastore-table-access-control-legacy-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - legacy-data-governance-models-in-databricks
    - LDGMID
  citations:
    - file: hive-metastore-table-access-control-legacy-databricks-on-aws.md
title: Legacy Data Governance Models in Databricks
description: Older data governance approaches on Databricks that are superseded by Unity Catalog, including Hive metastore table access control.
tags:
  - databricks
  - governance
  - legacy
  - unity-catalog
timestamp: "2026-06-19T10:47:37.199Z"
---

# Legacy Data Governance Models in Databricks

**Legacy Data Governance Models in Databricks** refer to the earlier approaches for managing data access and permissions within the Databricks platform, primarily centered around the built-in Hive [Metastore](/concepts/metastore.md). These models have been superseded by [Unity Catalog](/concepts/unity-catalog.md), which provides a more centralized and scalable governance solution.

## Overview

Each Databricks workspace deploys with a built-in Hive [Metastore](/concepts/metastore.md) as a managed service. An instance of the [Metastore](/concepts/metastore.md) deploys to each cluster and securely accesses metadata from a central per-workspace repository. This Hive [Metastore](/concepts/metastore.md) served as the primary data catalog for legacy governance. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Hive [Metastore](/concepts/metastore.md) Table Access Control

By default, a cluster allows all users to access all data managed by the workspace's built-in Hive [Metastore](/concepts/metastore.md) unless table access control is enabled for that cluster. Table access control lets administrators programmatically grant and revoke access to objects in the workspace's Hive [Metastore](/concepts/metastore.md) from Python and SQL. When table access control is enabled, users can set permissions for data objects accessed using that cluster. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

### Requirements

Hive [Metastore](/concepts/metastore.md) table access control requires the Databricks Premium plan or above. It also requires a Data Science & Engineering cluster with an appropriate configuration or a SQL Warehouse. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Limitations of the Legacy Model

The legacy Hive [Metastore](/concepts/metastore.md) approach had several limitations that motivated the shift to Unity Catalog:

- **Per-workspace isolation:** Each workspace maintained its own Hive [Metastore](/concepts/metastore.md), making cross-workspace data sharing difficult.
- **No centralized auditing:** There was no single pane for administering and auditing data access across multiple workspaces.
- **Cluster-dependent permissions:** Table access control was tied to specific cluster configurations, not to a workspace or account level. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Deprecation and Migration

Hive [Metastore](/concepts/metastore.md) table access control is a legacy data governance model. Databricks recommends that customers upgrade the tables managed by the Hive [Metastore](/concepts/metastore.md) to the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). Unity Catalog simplifies security and governance by providing a central place to administer and audit data access across multiple workspaces in a single account. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Key Legacy Concepts

- **Securable objects:** The legacy model defined various securable objects including tables, databases, and the `ANY FILE` securable.
- **Privileges:** Administrators could grant and revoke specific privileges (such as SELECT, MODIFY, and ownership) on these objects.
- **`ANY FILE` securable:** A special securable type in the legacy Hive [Metastore](/concepts/metastore.md) access control model. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The modern, recommended data governance solution
- [Hive Metastore](/concepts/built-in-hive-metastore.md) — The underlying metadata repository for legacy governance
- [Table Access Control](/concepts/table-access-control-tacl.md) — The mechanism for setting permissions on Hive [Metastore](/concepts/metastore.md) objects
- [Unity Catalog Migration](/concepts/unity-catalog-migration-path.md) — The process of upgrading from legacy to modern governance
- Data Governance — Broader framework for managing data access and quality

## Sources

- hive-metastore-table-access-control-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-table-access-control-legacy-databricks-on-aws.md](/references/hive-metastore-table-access-control-legacy-databricks-on-aws-d8a45857.md)
