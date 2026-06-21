---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c39b598f28bc88856e64c984a52a73853013bdb95e212f22a2efd9f66588bfe
  pageDirectory: concepts
  sources:
    - hive-metastore-table-access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-built-in-hive-metastore
    - WBHM
  citations:
    - file: hive-metastore-table-access-control-legacy-databricks-on-aws.md
title: Workspace Built-in Hive Metastore
description: A managed Hive metastore service that deploys per-Databricks-workspace and serves as a central metadata repository for all clusters in that workspace.
tags:
  - databricks
  - hive-metastore
  - metadata
timestamp: "2026-06-19T10:47:26.288Z"
---

# Workspace Built-in Hive [Metastore](/concepts/metastore.md)

**Workspace Built-in Hive Metastore** refers to the managed Hive [Metastore](/concepts/metastore.md) that is automatically deployed with each Databricks workspace. It serves as the default metadata repository for tables and data objects when a workspace is not using [Unity Catalog](/concepts/unity-catalog.md). ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Overview

Each Databricks workspace deploys a built-in Hive [Metastore](/concepts/metastore.md) as a managed service. An instance of the [Metastore](/concepts/metastore.md) is deployed to each cluster and securely accesses metadata from a central per-workspace repository. By default, a cluster allows all users to access all data managed by the workspace's built-in Hive [Metastore](/concepts/metastore.md). ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Table Access Control (Legacy)

If table access control is enabled for a cluster, users can programmatically grant and revoke access to objects in the workspace's Hive [Metastore](/concepts/metastore.md) using Python and SQL commands. When table access control is enabled, users can set permissions for data objects that are accessed using that cluster. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Legacy Status and Recommendation

Hive [Metastore](/concepts/metastore.md) table access control is a legacy data governance model. Databricks recommends that customers upgrade the tables managed by the Hive [Metastore](/concepts/metastore.md) to the Unity Catalog [Metastore](/concepts/metastore.md). Unity Catalog simplifies security and governance by providing a central place to administer and audit data access across multiple workspaces in an account. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Requirements

Enabling table access control on the workspace built-in Hive [Metastore](/concepts/metastore.md) requires:
- The Databricks workspace must be on the **Premium plan or above**.
- The cluster must be a Data Science & Engineering cluster with appropriate configuration, or the user must use a SQL warehouse.

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Related Topics

The Hive [Metastore](/concepts/metastore.md) table access control documentation covers:
- [Enable Hive Metastore Table Access Control on a Cluster](/concepts/cluster-level-hive-metastore-access-control.md) (legacy) — How to enable the feature for a cluster.
- [Hive Metastore Privileges and Securable Objects](/concepts/hive-metastore-privileges-and-securable-objects.md) (legacy) — The available privileges and objects.
- [What is the ANY FILE Securable?](/concepts/any-file-securable.md) — Details on the `ANY FILE` securable object.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The recommended modern data governance solution.
- Data Governance – Overall data management policies and controls.
- [Hive Metastore](/concepts/built-in-hive-metastore.md) – General Hive metadata storage concept.
- [Table Access Control](/concepts/table-access-control-tacl.md) – Mechanism to manage permissions on data objects.

## Sources

- hive-metastore-table-access-control-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-table-access-control-legacy-databricks-on-aws.md](/references/hive-metastore-table-access-control-legacy-databricks-on-aws-d8a45857.md)
