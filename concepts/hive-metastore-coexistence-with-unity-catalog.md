---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94fa21ce593c57f5813d6690a5a9ccc87ddc2ceeac47f544c377bee47f4091a2
  pageDirectory: concepts
  sources:
    - work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-coexistence-with-unity-catalog
    - HMCWUC
  citations:
    - file: work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
    - file: work-with-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
title: Hive Metastore Coexistence with Unity Catalog
description: The per-workspace legacy Hive metastore can continue to be used alongside Unity Catalog in Databricks, appearing as a top-level catalog named `hive_metastore` in the three-level namespace.
tags:
  - databricks
  - unity-catalog
  - hive-metastore
  - migration
timestamp: "2026-06-19T23:26:44.801Z"
---

# Hive [Metastore](/concepts/metastore.md) Coexistence with [Unity Catalog](/concepts/unity-catalog.md)

**Hive [Metastore](/concepts/metastore.md) Coexistence with Unity Catalog** describes the ability to continue using a legacy per-workspace Hive [Metastore](/concepts/metastore.md) within a Databricks workspace that has been enabled for [Unity Catalog](/concepts/unity-catalog.md). This setup allows organizations that have existing data in their Hive [Metastore](/concepts/metastore.md) to access that data alongside Unity Catalog–managed data during a migration period.

## Overview

When a workspace was in service before it was enabled for [Unity Catalog](/concepts/unity-catalog.md), it likely has a Hive [Metastore](/concepts/metastore.md) containing tables that you may want to continue using. The [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) is additive—it can coexist with the per-workspace Hive [Metastore](/concepts/metastore.md). The Hive [Metastore](/concepts/metastore.md) appears as a top-level catalog called `hive_metastore` in [Unity Catalog](/concepts/unity-catalog.md)'s [Three-Level Namespace](/concepts/three-level-namespace.md). ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Accessing Legacy Hive [Metastore](/concepts/metastore.md) Tables

You can reference tables in the legacy Hive [Metastore](/concepts/metastore.md) using the [Three-Level Namespace](/concepts/three-level-namespace.md) notation. For example, a table called `sales_raw` in the `sales` schema is accessible as:

```sql
SELECT * from hive_metastore.sales.sales_raw;
```

You can also use a `USE` statement to set the [Catalog and Schema](/concepts/catalog-and-schema.md):

```sql
USE hive_metastore.sales;
SELECT * from sales_raw;
```

^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Access Control Differences

If you configured [legacy table access control](/concepts/table-access-control-tacl.md) on the Hive [Metastore](/concepts/metastore.md), Databricks continues to enforce those access controls for data in the `hive_metastore` catalog for clusters running in [Standard Access Mode](/concepts/standard-access-mode.md). Several key differences exist between the two access models: ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

- **Metastore scope**: [Unity Catalog](/concepts/unity-catalog.md) is an account-level object; the Hive [Metastore](/concepts/metastore.md) is a workspace-level object. Permissions within `hive_metastore` refer to local users and groups in the workspace.
- **Account groups**: [Unity Catalog](/concepts/unity-catalog.md) applies access control to account groups, while Hive [Metastore](/concepts/metastore.md) policies apply to workspace-local groups.
- **`USE CATALOG` and `USE SCHEMA` permissions**: In [Unity Catalog](/concepts/unity-catalog.md), principals must have these privileges on the [Catalog and Schema](/concepts/catalog-and-schema.md) in addition to table-level privileges. With workspace-level table access controls, granting `USAGE` on the root catalog automatically grants it on all databases, but `USAGE` on the root catalog is not required.
- **Views**: In [Unity Catalog](/concepts/unity-catalog.md), a view owner does not need to be an owner of referenced tables and views—having `SELECT` privilege is sufficient. With workspace-level controls, a view's owner must be an owner of all referenced tables and views.
- **No `ANY FILE` or `ANONYMOUS FUNCTION`**: [Unity Catalog](/concepts/unity-catalog.md) lacks these concepts.
- **No `DENY` support**: [Unity Catalog](/concepts/unity-catalog.md)'s privilege model operates on least privilege; ungrants are implicit denials.
- **No `READ_METADATA` privilege**: [Unity Catalog](/concepts/unity-catalog.md) manages metadata access differently.

## Joining Data Across Metastores

You can join data in a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) with data in the legacy Hive [Metastore](/concepts/metastore.md) using [Three-Level Namespace](/concepts/three-level-namespace.md) notation:

```sql
SELECT *
FROM hive_metastore.sales.sales_current
JOIN main.shared_sales.sales_historical
ON hive_metastore.sales.sales_current.order_id
   = main.shared_sales.sales_historical.order_id;
```

This join only works on the workspace where the legacy data resides. Attempting such a join in another workspace results in an error. Databricks recommends upgrading legacy tables to Unity Catalog. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Default Catalog Behavior

Each workspace enabled for [Unity Catalog](/concepts/unity-catalog.md) has a configured default catalog. If you omit the top-level catalog name in data operations, the default catalog is assumed. The initial default depends on how the workspace was enabled: ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

- **Automatic enablement**: The workspace catalog was set as the default.
- **Manual enablement**: The `hive_metastore` catalog was set as the default.

During transition from Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md), using `hive_metastore` as the default catalog avoids impacting existing code that references the Hive [Metastore](/concepts/metastore.md) until full migration is complete.

## [Cluster-Scoped Data Access Permissions](/concepts/cluster-scoped-data-access-permissions.md)

When using the Hive [Metastore](/concepts/metastore.md) alongside [Unity Catalog](/concepts/unity-catalog.md), data access credentials associated with the cluster are used to access Hive [Metastore](/concepts/metastore.md) data but not data registered in [Unity Catalog](/concepts/unity-catalog.md). Paths outside [Unity Catalog](/concepts/unity-catalog.md) (such as paths not registered as tables or external locations) use cluster-assigned access credentials. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Resource Limits and Migration Recommendations

The Databricks-hosted legacy Hive [Metastore](/concepts/metastore.md) has resource limits on concurrent connections and connections per hour. Exceeding these limits can cause cluster and job connection errors or startup failures. Two strategies help avoid these limits: ^[work-with-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

- **Migrate to Unity Catalog**: The most effective approach—upgrade tables and [disable direct access to the Hive metastore](/concepts/disabling-direct-access-to-the-legacy-hive-metastore.md). [Unity Catalog](/concepts/unity-catalog.md) does not use the legacy Hive [Metastore](/concepts/metastore.md), so its connection limits no longer apply.
- **Optimize workload orchestration**: Smooth peak concurrency by avoiding synchronized job and cluster launches, limiting burst fan-out, and minimizing transient activity spikes.

Tables in the Hive [Metastore](/concepts/metastore.md) do not benefit from [Unity Catalog](/concepts/unity-catalog.md)'s full security and governance features, including built-in auditing, lineage, and access control. Databricks recommends migrating those tables and their workloads to [Unity Catalog](/concepts/unity-catalog.md). Two migration paths exist: upgrading all tables to [Unity Catalog](/concepts/unity-catalog.md), or federating the Hive metastore to [Unity Catalog](/concepts/unity-catalog.md) for a more gradual approach. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Hive metastore](/concepts/built-in-hive-metastore.md)
- [Legacy table access control](/concepts/table-access-control-tacl.md)
- [Upgrade a Databricks workspace to Unity Catalog](/concepts/migrating-existing-workspaces-to-unity-catalog.md)
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md)
- Default catalog
- Disable access to the Hive metastore

## Sources

- work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md

# Citations

1. [work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md](/references/work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws-c5d018d3.md)
2. work-with-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
