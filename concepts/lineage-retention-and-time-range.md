---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48c6bba637e8910abccd05e9084b4d20e617f0efb2778428c5c8e8ad88594a30
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-retention-and-time-range
    - Time Range and Lineage Retention
    - LRATR
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Lineage Retention and Time Range
description: Lineage data in Catalog Explorer is retained indefinitely for events after September 1, 2024, with an 'All time' option for newer metastores; lineage system tables retain a rolling one-year window.
tags:
  - retention
  - system-tables
  - data-governance
timestamp: "2026-06-18T14:58:52.599Z"
---

# Lineage Retention and Time Range

**Lineage Retention and Time Range** describes how long [Unity Catalog](/concepts/unity-catalog.md) retains [Data Lineage](/concepts/data-lineage.md) information and the time-range options available for viewing it in [Catalog Explorer](/concepts/catalog-explorer.md) and system tables.

## Retention in Catalog Explorer

Lineage data displayed in Catalog Explorer is retained indefinitely. All lineage data captured after **September 1, 2024** is available. For metastores created after that date, Catalog Explorer includes an **All time** option in the lineage time-range dropdown. For older metastores (created before September 1, 2024), the dropdown includes an **All available** option that starts from September 1, 2024. The default selection is **1 year**. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Retention in System Tables

Lineage system tables — `system.access.table_lineage` and `system.access.column_lineage` — retain a rolling **1-year window** of data. This is a different retention policy than the indefinite retention in Catalog Explorer. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Limitations

Lineage data captured before September 1, 2024 is not available, regardless of the viewer. This affects both Catalog Explorer and system table queries. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI for browsing lineage with time-range controls.
- [Lineage System Tables](/concepts/lineage-system-tables.md) – Programmatic access to lineage with a 1-year rolling window.
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) – Overall concept and usage.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that stores lineage.

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)
