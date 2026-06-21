---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0c035d1a9924a7fc466aaeeb519c60498486900b29071004d076b73a2e9c9e15
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-lineage-limitations-and-quotas
    - Quotas and External Lineage Limitations
    - ELLAQ
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Lineage Limitations and Quotas
description: "Resource limits and constraints for external lineage: a maximum of 10,000 external metadata objects and 100,000 external lineage relationships per metastore, and external lineage is not recorded in lineage system tables."
tags:
  - limits
  - governance
timestamp: "2026-06-19T18:47:15.763Z"
---

# External Lineage Limitations and Quotas

External lineage in [Unity Catalog](/concepts/unity-catalog.md) allows you to manually or automatically add lineage metadata for workloads running outside Databricks. However, there are specific limitations and quotas that govern how much external lineage can be created and where it is visible.

## Limitations

- **Not recorded in lineage system tables**: External lineage is **not** captured in the system tables `system.access.table_lineage` or `system.access.column_lineage`. These tables contain only lineage generated automatically by Databricks runtime queries. ^[external-lineage-databricks-on-aws.md]

## Resource Quotas

The following per-[Metastore](/concepts/metastore.md) quotas apply to external lineage metadata:

| Resource | Maximum per [Metastore](/concepts/metastore.md) |
|---|---|
| External metadata objects | 10,000 |
| External lineage relationships | 100,000 |

^[external-lineage-databricks-on-aws.md]

These limits are enforced across all workspaces attached to the same [Metastore](/concepts/metastore.md). For additional details, see the main Resource limits documentation on Databricks.

## Related Concepts

- [External Metadata Object](/concepts/external-metadata-object.md) – An entity representing an external system (e.g., a Tableau dashboard or a MySQL table) that can be linked into Unity Catalog lineage graphs.
- External lineage relationship – A directional connection between an external metadata object and another Unity Catalog object (table, model, path, or another external metadata object).
- [Lineage System Tables](/concepts/lineage-system-tables.md) – The `system.access.table_lineage` and `system.access.column_lineage` tables that store automatically captured runtime lineage.
- [Metastore](/concepts/metastore.md) – The top-level container for Unity Catalog metadata, including external lineage metadata.
- Resource limits – General Databricks resource quotas applicable to various objects.
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) – The broader overview of how lineage is captured and displayed.
- Lakeflow Connect – An automated ingestion pipeline that can record source lineage without manually creating external metadata objects.

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
