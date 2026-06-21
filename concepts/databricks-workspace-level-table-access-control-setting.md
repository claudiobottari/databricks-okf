---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6288976f027f382d62208fd24f902f46ae8a2ff39e77e41a06fd43ad09723f7
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-workspace-level-table-access-control-setting
    - DWTACS
    - Workspace-Level HMS Access Control
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Databricks Workspace-level Table Access Control Setting
description: An admin setting on the Security tab of the Databricks workspace settings page that must be enabled before users can configure Python and SQL table access control on clusters.
tags:
  - databricks
  - admin
  - workspace-configuration
timestamp: "2026-06-18T12:10:24.576Z"
---

# Databricks Workspace-level Table Access Control Setting

The **Workspace-level Table Access Control Setting** is a legacy toggle in the Databricks admin console that enables the **Python and SQL table access control** mode for the built-in Hive [Metastore](/concepts/metastore.md). When turned on, it permits administrators and cluster creators to configure clusters that restrict user access to data objects using Hive [Metastore](/concepts/metastore.md) privileges. This setting does not affect the SQL-only mode of table access control, which is controlled independently via a Spark configuration flag. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Databricks recommends using [Unity Catalog](/concepts/unity-catalog.md) for modern data governance. The workspace-level table access control setting is part of the legacy Hive [Metastore](/concepts/metastore.md) access control system.

## Enabling the Setting

A Databricks workspace admin can enable the setting as follows:

1. Go to the admin **Settings** page.
2. Click the **Security** tab.
3. Toggle the **Table Access Control** option to on.

Once enabled, users who have the necessary permissions can create or use clusters that enforce Python and SQL table access control. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Effect on Users and Clusters

When the workspace setting is on and a cluster is configured for Python and SQL table access control, users on that cluster:

- Are restricted to using only the Spark SQL API or DataFrame API for data access.
- Run on cluster nodes as a low-privilege user, forbidden from accessing sensitive filesystem areas or creating network connections to ports other than 80 and 443 (with exceptions for built-in Spark functions and, for workspace admins or users with `ANY FILE` privilege, PySpark JDBC connectors).
- Attempts to bypass these restrictions result in exceptions. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

The **SQL-only** table access control mode is configured by setting `spark.databricks.acl.sqlOnly true` in the cluster's Spark configuration and is **not** controlled by the workspace-level toggle. Workspace admins can enable the workspace setting to allow both Python and SQL access control, but this does not block users from creating clusters with SQL-only mode if they have cluster creation permissions. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enforcement Requirements

Merely turning on the setting does not itself restrict data access. Administrators must also ensure that:

- Users do not have permission to create clusters without table access control.
- Users do not have `CAN ATTACH TO` permission for any cluster that does not have table access control enabled.

Without these enforcement steps, users could bypass the intended restrictions by using unsecured clusters. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Related Concepts

- Hive metastore privileges and securable objects (legacy) — How to grant privileges once table access control is enabled.
- [Unity Catalog](/concepts/unity-catalog.md) — The modern, recommended governance solution that replaces Hive [Metastore](/concepts/metastore.md) access control.
- [Cluster access modes](/concepts/databricks-connect-cluster-access-modes.md) — How to configure clusters for standard, single user, or shared access modes, which affect table access control behavior.
- [Legacy table access control](/concepts/table-access-control-tacl.md) — Overview of the legacy system and its limitations.

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
