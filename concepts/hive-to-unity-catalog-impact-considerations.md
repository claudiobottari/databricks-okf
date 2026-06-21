---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a2f866f3f4f7b531ae25579e9d6d9b9b44bbd3fa0091e8665534d964b64af01
  pageDirectory: concepts
  sources:
    - upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-to-unity-catalog-impact-considerations
    - HIC
  citations:
    - file: upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
title: Hive-to-Unity-Catalog Impact Considerations
description: "Key behavioral changes when migrating: Unity Catalog manages partitions differently (no direct partition manipulation commands), and table history is not migrated with CLONE operations."
tags:
  - unity-catalog
  - migration
  - best-practices
timestamp: "2026-06-19T23:19:12.786Z"
---

# Hive-to-Unity-Catalog Impact Considerations

**Hive-to-Unity-Catalog Impact Considerations** describes the behavioral, operational, and technical changes that organizations must account for when migrating tables and views from a workspace-local Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md). Understanding these impacts before migration helps avoid unexpected disruptions to existing workloads and queries.

## Behavioral Changes

### Partition Management Differences

[Unity Catalog](/concepts/unity-catalog.md) manages partitions differently than Hive. Hive commands that directly manipulate partitions are **not supported** on tables managed by [Unity Catalog](/concepts/unity-catalog.md). Workloads that rely on direct partition operations must be modified before migration. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

### Table History and Time Travel

When you migrate a Hive table to [Unity Catalog](/concepts/unity-catalog.md) using `CREATE TABLE CLONE`, the table history is **not** preserved. The new table in [Unity Catalog](/concepts/unity-catalog.md) is treated as a fresh table, meaning you cannot perform [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) or other operations that depend on pre-migration history. This applies to all clones regardless of the migration method chosen. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Table Type Considerations

### Managed Tables

[Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md) have [Unity Catalog](/concepts/unity-catalog.md) fully manage their lifecycle, file layout, and storage. They always use the Delta table format and reside in a reserved [Managed storage location](/concepts/managed-storage-location.md). To create managed tables from Hive tables, you must use **CLONE** or **CREATE TABLE AS SELECT (CTAS)**, as these copy the data into the [Unity Catalog](/concepts/unity-catalog.md) managed storage. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

### External Tables

External tables allow [Unity Catalog](/concepts/unity-catalog.md) to register the table's metadata without managing the underlying data lifecycle. They support multiple data formats and enable direct access by non-Databricks compute. Migration to external tables can be performed quickly because no data copying is required — the data stays in its existing cloud storage location. External tables are useful for migration scenarios and when direct external access is needed. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Workload Modification Requirements

After migration, all existing queries and workloads must be updated to reference the new [Unity Catalog](/concepts/unity-catalog.md) tables instead of the old Hive [Metastore](/concepts/metastore.md) tables. Databricks provides tooling to assist with this transition:

- **Deprecation comments**: Adding a specially formatted comment to the old Hive table causes notebooks and the SQL query editor to display the deprecated table name in strikethrough text with a warning, and provides a **Quick Fix** link to [Genie Code](/concepts/genie-code.md) that can automatically update references. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- **Genie Code**: [Genie Code](/concepts/genie-code.md) can search the workspace catalog for tables with matching schemas and automatically replace Hive [Metastore](/concepts/metastore.md) references with [Unity Catalog](/concepts/unity-catalog.md) equivalents. This is useful even when the exact [Unity Catalog](/concepts/unity-catalog.md) location is unknown. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Permission Model Migration

When migrating to [Unity Catalog](/concepts/unity-catalog.md), the permission model changes from [legacy table access control](/concepts/table-access-control-tacl.md) to [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md). Users may need to be re-granted access on the new tables, as [Unity Catalog](/concepts/unity-catalog.md) permissions are managed at the account level rather than the workspace level. [Unity Catalog](/concepts/unity-catalog.md) recommends granting table ownership to groups rather than individual users for easier management. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Pre-Migration Testing

Before dropping old Hive tables, Databricks recommends:

- Revoking access to the old tables and re-running related queries to identify dependencies.
- Testing all workloads against the new [Unity Catalog](/concepts/unity-catalog.md) tables.
- Not dropping old tables prematurely if they are still needed for dependency discovery or if they serve as the source for ongoing `SYNC` operations. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## View Migration

Views in the Hive [Metastore](/concepts/metastore.md) cannot be directly migrated. After all tables referenced by a view have been migrated to the same [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md), you must create a new view that references the new [Unity Catalog](/concepts/unity-catalog.md) tables. The view's query logic must be re-created in [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Hive Metastore](/concepts/built-in-hive-metastore.md)
- [Managed Tables vs External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md)
- [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md)
- SYNC Command
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md)
- CREATE TABLE AS SELECT
- [Genie Code](/concepts/genie-code.md)
- [Legacy Table Access Control](/concepts/table-access-control-tacl.md)
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md)
- [Catalog Explorer Upgrade Wizard](/concepts/catalog-explorer-upgrade-wizard.md)
- [UCX Migration Tool](/concepts/ucx-unity-catalog-migration-toolkit.md)

## Sources

- upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md](/references/upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws-c9a7f3f8.md)
