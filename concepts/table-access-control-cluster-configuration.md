---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 709a1125e011840530e19704ff560eaf3d425b8b754eb79868acdf132c86177a
  pageDirectory: concepts
  sources:
    - hive-metastore-table-access-control-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-access-control-cluster-configuration
    - TACCC
  citations:
    - file: hive-metastore-table-access-control-legacy-databricks-on-aws.md
title: Table Access Control Cluster Configuration
description: The per-cluster toggle that controls whether Hive metastore table access control is enforced, with default being open access to all data.
tags:
  - databricks
  - configuration
  - clusters
  - security
timestamp: "2026-06-19T19:04:43.860Z"
---

# Table Access Control Cluster Configuration

**Table Access Control Cluster Configuration** refers to the process of enabling table access control on a Databricks cluster so that data governed by the workspace's built-in [Hive Metastore](/concepts/built-in-hive-metastore.md) can be accessed only according to user-defined permissions. This is a legacy feature that provides fine-grained access control for tables, views, databases, and functions defined in the Hive [Metastore](/concepts/metastore.md). ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Overview

Each Databricks workspace deploys with a built-in Hive [Metastore](/concepts/metastore.md) that securely stores metadata for the workspace. By default, when a cluster is created, **all users** can access all data managed by that [Metastore](/concepts/metastore.md). Enabling table access control on the cluster changes this behavior: it allows data owners to programmatically grant and revoke access to Hive [Metastore](/concepts/metastore.md) objects using Python or SQL. Once enabled, the cluster respects the permissions set on securable objects (tables, views, databases, functions). ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Requirements

- A workspace on the **Premium Plan** or above.
- A **Data Science & Engineering clusters|Data Science & Engineering cluster** configured with table access control enabled, or a **SQL Warehouse** (which automatically enforces table access control).

Without these requirements, the cluster remains open to all users. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Legacy Status

Hive [Metastore](/concepts/metastore.md) table access control is a legacy data governance model. Databricks recommends upgrading the tables managed by the Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md). Unity Catalog provides a single, centralized place to administer and audit data access across multiple workspaces in an account, simplifying security and governance. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Related Pages

The original documentation covers three subtopics that are directly relevant to this configuration:

- [Enable Hive metastore table access control on a cluster (legacy)](/concepts/hive-metastore-table-access-control-legacy.md)
- Hive metastore privileges and securable objects (legacy)
- [What is the `ANY FILE` securable?](/concepts/any-file-securable.md)

These pages provide step-by-step instructions, the full list of privileges, and details on the special `ANY FILE` securable.

## Related Concepts

- [Hive Metastore](/concepts/built-in-hive-metastore.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Table Access Control](/concepts/table-access-control-tacl.md)
- Data Science & Engineering Clusters
- SQL Warehouse
- Premium Plan
- Data Governance

## Sources

- hive-metastore-table-access-control-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-table-access-control-legacy-databricks-on-aws.md](/references/hive-metastore-table-access-control-legacy-databricks-on-aws-d8a45857.md)
