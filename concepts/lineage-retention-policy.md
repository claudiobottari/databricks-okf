---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f813af012c28be7c62a2de47ab2d6c191281053f516a3be1eef053e33453386c
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-retention-policy
    - LRP
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Lineage Retention Policy
description: Lineage data displayed in Catalog Explorer is retained indefinitely from September 1, 2024 onward, while system tables retain a rolling one-year window.
tags:
  - retention
  - data-governance
  - lineage
timestamp: "2026-06-19T18:04:41.978Z"
---

# Lineage Retention Policy

**Lineage Retention Policy** defines how long [Data Lineage](/concepts/data-lineage.md) information is retained in [Unity Catalog](/concepts/unity-catalog.md) and made available through different access mechanisms. The retention duration differs depending on whether lineage is accessed through the [Catalog Explorer](/concepts/catalog-explorer.md) UI or via [Lineage System Tables](/concepts/lineage-system-tables.md).

## Lineage in Catalog Explorer

Lineage data displayed in Catalog Explorer is retained indefinitely. All lineage data captured after September 1, 2024 is available for viewing. For metastores created after that date, Catalog Explorer includes an **All time** option in the lineage time‑range dropdown. For older metastores, the dropdown includes an **All available** option that starts from September 1, 2024. The default selection is **1 year**. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Lineage in System Tables

Lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`) retain a rolling 1‑year window of data. This means lineage records older than one year are automatically removed from the system tables. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Key Distinctions

| Access Mechanism | Retention Duration |
|-----------------|-------------------|
| Catalog Explorer UI | Indefinite (from September 1, 2024 onward) |
| System tables (`table_lineage`, `column_lineage`) | Rolling 1‑year window |

## Implications

- **Historical analysis**: Catalog Explorer provides access to the complete history of lineage events since September 2024, enabling long‑term impact analysis and compliance audits.
- **Programmatic queries**: System tables provide a rolling one‑year window suitable for operational queries and automated workflows.
- **Data cutoff**: Lineage data captured before September 1, 2024 is not available through any mechanism. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) – Overview of lineage tracking, requirements, and viewing methods.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI tool for browsing and exploring Unity Catalog objects.
- [Lineage System Tables](/concepts/lineage-system-tables.md) – Programmatic access to lineage data via system tables.
- [Column‑Level Lineage](/concepts/column-level-lineage.md) – Granular lineage tracking at the column level.

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)
