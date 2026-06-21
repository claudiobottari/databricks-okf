---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b73f915c4926ad05a269943e7ce5dbdf407c7e4df8ef9b024aabddd20c81b3ba
  pageDirectory: concepts
  sources:
    - hive-metastore-table-access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-table-access-control-legacy
    - HMTAC(
    - HMAC
    - Enable Hive metastore table access control on a cluster (legacy)
  citations:
    - file: hive-metastore-table-access-control-legacy-databricks-on-aws.md
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Hive Metastore Table Access Control (Legacy)
description: A legacy Databricks data governance model that enables programmatic grant and revoke of permissions on Hive metastore objects via Python and SQL, per cluster.
tags:
  - databricks
  - data-governance
  - access-control
  - legacy
timestamp: "2026-06-19T19:04:42.325Z"
---

# Hive [Metastore](/concepts/metastore.md) Table Access Control (Legacy)

**Hive [Metastore](/concepts/metastore.md) table access control** is a legacy data governance model in Databricks that allows administrators to programmatically grant and revoke access to objects in a workspace's built-in Hive [Metastore](/concepts/metastore.md). When enabled on a cluster, users can set permissions for data objects accessed through that cluster, restricting access to authorized users only. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Overview

Each Databricks workspace deploys with a built-in Hive [Metastore](/concepts/metastore.md) as a managed service. An instance of the [Metastore](/concepts/metastore.md) deploys to each cluster and securely accesses metadata from a central per-workspace repository. By default, a cluster allows all users to access all data managed by the workspace's built-in Hive [Metastore](/concepts/metastore.md) unless table access control is enabled for that cluster. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

Databricks recommends upgrading to [Unity Catalog](/concepts/unity-catalog.md) as the modern alternative. Unity Catalog simplifies security and governance by providing a central place to administer and audit data access across multiple workspaces in your account. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Requirements

- This feature requires the [Databricks Premium Plan](/concepts/databricks-premium-plan-requirement.md) or above. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]
- This feature requires a Data Science & Engineering cluster with an appropriate configuration, or a SQL warehouse. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Enabling Table Access Control

To enable table access control on a cluster, you must configure the cluster appropriately. The specific configuration steps depend on the version of table access control you wish to use. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### SQL-Only Table Access Control

This version restricts users to SQL commands only. To enable SQL-only table access control on a cluster, set the following flag in the cluster's Spark configuration: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

```
spark.databricks.acl.sqlOnly true
```

Access to SQL-only table access control is not affected by the "Enable Table Access Control" workspace admin setting, which controls only the workspace-wide enablement of Python and SQL table access control. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Python and SQL Table Access Control

This version lets users run Python commands using the DataFrame API as well as SQL. When enabled on a cluster, users on that cluster: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- Can access Spark only using the Spark SQL API or DataFrame API. Access to tables and views is restricted by administrators according to Hive metastore privileges and securable objects (legacy).
- Must run commands on cluster nodes as a low-privilege user forbidden from accessing sensitive parts of the filesystem or creating network connections to ports other than 80 and 443.
- Only built-in Spark functions can create network connections on ports other than 80 and 443.
- Only workspace admin users or users with the `ANY FILE` privilege can read data from external databases through the PySpark JDBC connector.
- To allow Python processes to access additional outbound ports, set the Spark config `spark.databricks.pyspark.iptable.outbound.whitelisted.ports` to the desired ports. The supported format is `[port[:port][,port[:port]]...]`, for example: `21,22,9000:9999`. Ports must be within the valid range of `0-65535`.

Attempts to circumvent these restrictions will fail with an exception. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

**Important:** Even if table access control is enabled for a cluster, Databricks workspace administrators still have access to file-level data. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Workspace-Level Enablement

Before users can configure Python and SQL table access control, a workspace admin must enable table access control for the workspace: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

1. Go to the admin settings page.
2. Click the **Security** tab.
3. Turn on the **Table Access Control** option.

### Enforcing Table Access Control

To ensure users access only authorized data, restrict users to clusters with table access control enabled: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- Ensure users do not have permission to create clusters. Clusters created without table access control allow access to any data.
- Ensure users do not have `CAN ATTACH TO` permission for any cluster that is not enabled for table access control.

See Compute permissions for more information.

## Creating a Cluster with Table Access Control

Table access control is enabled by default in clusters with [Standard Access Mode](/concepts/standard-access-mode.md). To create a cluster using the REST API, see Create new cluster. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Setting Privileges on Data Objects

Once table access control is enabled on a cluster, see Hive metastore privileges and securable objects (legacy) for instructions on setting privileges on Hive [Metastore](/concepts/metastore.md) securable objects. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Limitations

- Table access control is not supported with Machine Learning Runtime. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Migration to Unity Catalog

Databricks recommends that you [upgrade tables managed by the Hive metastore to Unity Catalog](/concepts/hive-metastore-to-unity-catalog-migration.md). Unity Catalog provides centralized administration and auditing of data access across multiple workspaces in your account. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The modern data governance solution
- Hive metastore privileges and securable objects (legacy) — Detailed privilege types and object hierarchy
- [ANY FILE Securable](/concepts/any-file-securable.md) — A special securable object for unrestricted file access
- [Standard Access Mode](/concepts/standard-access-mode.md) — Cluster access mode that enables table access control by default
- Compute permissions — Managing cluster-level permissions
- PySpark JDBC connector — External database connectivity with table access control restrictions

## Sources

- hive-metastore-table-access-control-legacy-databricks-on-aws.md
- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-table-access-control-legacy-databricks-on-aws.md](/references/hive-metastore-table-access-control-legacy-databricks-on-aws-d8a45857.md)
2. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
