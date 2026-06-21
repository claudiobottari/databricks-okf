---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 671fbcd95b7a34deedf70e0adaa52054a5646b9c0136a1a264623447ffc12830
  pageDirectory: concepts
  sources:
    - work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-catalog-joins-between-hive-metastore-and-unity-catalog
    - Unity Catalog and Cross-Catalog Joins Between Hive Metastore
    - CJBHMAUC
  citations:
    - file: work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
title: Cross-Catalog Joins Between Hive Metastore and Unity Catalog
description: Using three-level namespace notation, users can join tables across the legacy Hive metastore and Unity Catalog, though such joins only work on the workspace where the Hive metastore data resides.
tags:
  - databricks
  - unity-catalog
  - hive-metastore
  - query
timestamp: "2026-06-19T23:26:31.442Z"
---

# Cross-Catalog Joins Between Hive [Metastore](/concepts/metastore.md) and [Unity Catalog](/concepts/unity-catalog.md)

**Cross-Catalog Joins Between Hive [Metastore](/concepts/metastore.md) and Unity Catalog** allow you to combine data from the legacy per-workspace Hive [Metastore](/concepts/metastore.md) with data registered in a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) within the same workspace. This capability is provided by the [Three-Level Namespace](/concepts/three-level-namespace.md) (`catalog.schema.table`) support in Databricks, where the legacy Hive [Metastore](/concepts/metastore.md) is exposed as a top-level catalog named `hive_metastore`. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Using [Three-Level Namespace](/concepts/three-level-namespace.md) Notation

When a workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md), the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) is additive: the existing Hive [Metastore](/concepts/metastore.md) continues to be accessible. You can refer to tables in the Hive [Metastore](/concepts/metastore.md) by prefixing the schema and table name with `hive_metastore`. For example, a table `sales_raw` in schema `sales` in the Hive [Metastore](/concepts/metastore.md) can be referenced as `hive_metastore.sales.sales_raw`. You can also set the current [Catalog and Schema](/concepts/catalog-and-schema.md) using `USE hive_metastore.sales`. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Performing a Cross-Catalog Join

By using [Three-Level Namespace](/concepts/three-level-namespace.md) notation, you can join data from the `hive_metastore` catalog with tables in any [Unity Catalog](/concepts/unity-catalog.md) catalog. The following SQL example joins `sales_current` from the Hive [Metastore](/concepts/metastore.md) with `sales_historical` from a [Unity Catalog](/concepts/unity-catalog.md) catalog named `main`:

```sql
SELECT *
FROM hive_metastore.sales.sales_current
JOIN main.shared_sales.sales_historical
  ON hive_metastore.sales.sales_current.order_id = main.shared_sales.sales_historical.order_id;
```

^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Limitations and Considerations

- **Workspace-scoped**: A cross-catalog join between the Hive [Metastore](/concepts/metastore.md) and [Unity Catalog](/concepts/unity-catalog.md) will only work on the workspace where the Hive [Metastore](/concepts/metastore.md) data resides. Attempting to run the same join in another workspace results in an error. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]
- **Legacy feature**: The per-workspace Hive [Metastore](/concepts/metastore.md) is a legacy feature. Tables in the Hive [Metastore](/concepts/metastore.md) do not benefit from [Unity Catalog](/concepts/unity-catalog.md)'s built-in auditing, lineage, and access control. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]
- **Default catalog**: The default catalog setting for a workspace may be `hive_metastore` (if enabled manually) or the workspace catalog (if enabled automatically). If the default is `hive_metastore`, queries that omit the catalog name will reference the Hive [Metastore](/concepts/metastore.md) first. Changing the default catalog is possible but should be done after full migration. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]
- **Access control differences**: [Unity Catalog](/concepts/unity-catalog.md) and legacy Hive [Metastore](/concepts/metastore.md) access controls differ (e.g., account vs. workspace groups, `USE CATALOG` requirements, view ownership rules). Be aware that the Hive [Metastore](/concepts/metastore.md) access model remains in effect for the `hive_metastore` catalog. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Recommendation

Databricks recommends migrating tables and workloads from the Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md) and then disabling direct access to the Hive [Metastore](/concepts/metastore.md). Two migration paths are available: upgrading all Hive [Metastore](/concepts/metastore.md) tables to [Unity Catalog](/concepts/unity-catalog.md), or using [Hive Metastore Federation](/concepts/hive-metastore-federation.md) to create a foreign catalog that mirrors the Hive [Metastore](/concepts/metastore.md) for a more gradual transition. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore](/concepts/built-in-hive-metastore.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Three-Level Namespace](/concepts/three-level-namespace.md)
- Default Catalog
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md)
- Data Migration to Unity Catalog
- [Disable Hive Metastore Access](/concepts/disable-legacy-hive-metastore-access.md)

## Sources

- work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md

# Citations

1. [work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md](/references/work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws-c5d018d3.md)
