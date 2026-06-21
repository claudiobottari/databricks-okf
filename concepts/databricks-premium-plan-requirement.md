---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9d845838e3d53c8bf58c355708372e97a4fccf45573d0c154040eae2d74487f
  pageDirectory: concepts
  sources:
    - hive-metastore-table-access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-premium-plan-requirement
    - DPPR
    - Databricks Premium Plan
  citations:
    - file: hive-metastore-table-access-control-legacy-databricks-on-aws.md
title: Databricks Premium Plan Requirement
description: The pricing tier prerequisite stating that Hive metastore table access control requires the Premium plan or above on Databricks.
tags:
  - databricks
  - pricing
  - prerequisites
timestamp: "2026-06-19T19:05:14.849Z"
---

# Databricks Premium Plan Requirement

The **Databricks Premium Plan Requirement** is a licensing prerequisite that restricts certain features and capabilities to workspaces on a Premium plan or above. This requirement is documented for legacy data governance features, specifically the Hive [Metastore](/concepts/metastore.md) table access control system.

## Scope

Several advanced security and governance features on Databricks require the Premium plan or a higher tier (such as the Enterprise plan). The Premium plan is the minimum tier needed to enable table-level access controls in the legacy Hive [Metastore](/concepts/metastore.md). ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Affected Features

### Hive [Metastore](/concepts/metastore.md) Table Access Control (Legacy)

The [Hive Metastore Table Access Control (Legacy)](/concepts/hive-metastore-table-access-control-legacy.md) system requires the Premium plan or above. This feature allows administrators to programmatically grant and revoke access to objects in the workspace's built-in Hive [Metastore](/concepts/metastore.md) from Python and SQL. When table access control is enabled on a cluster, users can set permissions for data objects accessed through that cluster. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

Requirements for using Hive [Metastore](/concepts/metastore.md) table access control:
- A Databricks workspace on the Premium plan or above
- A Data Science & Engineering cluster with [table access control](/concepts/table-access-control-tacl.md) properly configured, or a SQL warehouse

## Migration Recommendation

Databricks recommends upgrading from the legacy Hive [Metastore](/concepts/metastore.md) table access control to [Unity Catalog](/concepts/unity-catalog.md), which simplifies security and governance by providing a central place to administer and audit data access across multiple workspaces. Unity Catalog may have its own licensing requirements that users should verify separately. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore Table Access Control (Legacy)](/concepts/hive-metastore-table-access-control-legacy.md) – The affected data governance feature requiring Premium plan
- [Unity Catalog](/concepts/unity-catalog.md) – The recommended replacement for legacy Hive [Metastore](/concepts/metastore.md) governance
- Databricks Pricing Tiers – Overview of available plan levels (Standard, Premium, Enterprise)
- [Table Access Control](/concepts/table-access-control-tacl.md) – The mechanism for granting and revoking permissions on Hive [Metastore](/concepts/metastore.md) objects

## Sources

- hive-metastore-table-access-control-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-table-access-control-legacy-databricks-on-aws.md](/references/hive-metastore-table-access-control-legacy-databricks-on-aws-d8a45857.md)
