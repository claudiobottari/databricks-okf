---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf06f5777d53c1e2e0b7053ba85fb6ba2b29e01b6ecf5caac72506aae7bdacf9
  pageDirectory: concepts
  sources:
    - upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deprecation-comments-and-genie-code-integration
    - Genie Code Integration and Deprecation Comments
    - DCAGCI
  citations:
    - file: upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
title: Deprecation Comments and Genie Code Integration
description: Mechanism to annotate deprecated Hive tables with structured comments, triggering strikethrough display and Quick Fix links in notebooks, plus Genie Code auto-replacement of table references.
tags:
  - unity-catalog
  - migration
  - developer-tools
timestamp: "2026-06-19T23:19:43.963Z"
---

#Deprecation Comments and [Genie Code](/concepts/genie-code.md) Integration

**Deprecation Comments and [Genie Code](/concepts/genie-code.md) Integration** is a feature that streamlines the migration of Hive tables and views to [Unity Catalog](/concepts/unity-catalog.md) by using structured table comments as triggers for automated code updates. When a Hive table is migrated to [Unity Catalog](/concepts/unity-catalog.md), administrators can add a specially formatted comment to the deprecated Hive table. Notebooks and the SQL query editor then display the deprecated table name with strikethrough text and a warning, and provide a **Quick Fix** link to [Genie Code](/concepts/genie-code.md) that can automatically update queries to reference the new [Unity Catalog](/concepts/unity-catalog.md) table. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Format of Deprecation Comments

To activate the warning and Quick Fix behavior, the comment on the deprecated Hive table must follow this exact format:

```
This table is deprecated. Please use catalog.default.table instead of hive_metastore.schema.table.
```

The comment includes the full three-level name of the replacement [Unity Catalog](/concepts/unity-catalog.md) table (catalog.schema.table) and the full three-level name of the original Hive table (hive_metastore.schema.table). Comments can be added using [Catalog Explorer](/concepts/catalog-explorer.md) or the SQL `COMMENT ON` command. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Behavior in Notebooks and the SQL Query Editor

Once a deprecation comment is set, any cell or query that references the deprecated Hive table will automatically:

- Display the deprecated table name with **strikethrough** formatting.
- Show the comment text as a **warning**.
- Offer a **Quick Fix** link that launches [Genie Code](/concepts/genie-code.md), which can update the code to use the new [Unity Catalog](/concepts/unity-catalog.md) table. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

This visual feedback helps users identify and fix deprecated table references proactively during development.

## Using [Genie Code](/concepts/genie-code.md) to Update Deprecated Table References

[Genie Code](/concepts/genie-code.md) provides advanced table search capabilities that can find the equivalent [Unity Catalog](/concepts/unity-catalog.md) table even if the user does not know its exact location. When a user asks [Genie Code](/concepts/genie-code.md) to replace a `hive_metastore` table with an equivalent table in [Unity Catalog](/concepts/unity-catalog.md), Genie:

1. Searches the [Unity Catalog](/concepts/unity-catalog.md) for tables with similar schema.
2. Identifies the best match based on **schema similarity**.
3. Updates the code to reference the discovered [Unity Catalog](/concepts/unity-catalog.md) table.

This allows users to complete table migrations without manually locating each replacement. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Best Practices

- Add deprecation comments to all Hive tables that have been migrated to [Unity Catalog](/concepts/unity-catalog.md), regardless of the migration method used (SYNC, [CLONE](/concepts/deep-clone.md), CREATE TABLE AS SELECT, or the upgrade wizard and view migration).
- Keep the deprecated Hive table in place as long as the deprecation comment and [Genie Code](/concepts/genie-code.md) integration are actively being used to update workloads. Dropping the old table removes the mechanism that triggers the Quick Fix.
- After all references have been updated, revoke access to the deprecated table and test for dependencies before dropping it. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore](/concepts/built-in-hive-metastore.md) – The legacy table registry that is being replaced.
- [Unity Catalog](/concepts/unity-catalog.md) – The target catalog for table and view migrations.
- [Genie Code](/concepts/genie-code.md) – AI-powered assistant that helps update code references.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI tool for managing table comments and metadata.
- SQL Query Editor – Interface where deprecation warnings appear.
- SYNC – Command to copy external Hive tables to [Unity Catalog](/concepts/unity-catalog.md).
- [CLONE](/concepts/deep-clone.md) – Command to copy managed Delta tables to [Unity Catalog](/concepts/unity-catalog.md).
- CREATE TABLE AS SELECT – Alternative method for migrating tables.
- [Manage Privileges](/concepts/manage-privilege.md) – Granting access to new [Unity Catalog](/concepts/unity-catalog.md) tables.

## Sources

- upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md](/references/upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws-c9a7f3f8.md)
