---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 54d4f49238cd124e16c93e260684b53fd82eb8051cfedc8272339e67d857ee9c
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-lineage-relationship-patterns
    - ELRP
    - External lineage relationship
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Lineage Relationship Patterns
description: "Patterns for modeling complex external lineage: connecting two Unity Catalog tables via an intermediary external metadata object, adding multiple levels of lineage across systems, and specifying column-level lineage."
tags:
  - data-lineage
  - modeling
  - patterns
timestamp: "2026-06-19T18:47:08.565Z"
---

# External Lineage Relationship Patterns

**External Lineage Relationship Patterns** describe the recommended ways to model data flow between external systems and Unity Catalog objects when adding external lineage manually. These patterns help you represent complex data pipelines that span multiple systems outside Databricks, ensuring that the lineage graph in Unity Catalog provides an end-to-end view of data movement.

## Overview

Unity Catalog automatically captures lineage for queries run on Databricks, but workloads that run outside of Databricks (such as first‑mile ETL or last‑mile BI) are not captured automatically. You can add external lineage metadata manually to bridge these gaps. The following patterns guide you in structuring those relationships for common scenarios. ^[external-lineage-databricks-on-aws.md]

## Requirements

Before adding external lineage, you must have the necessary privileges:
- `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md) to create an external metadata securable object.
- `MODIFY` on the external metadata object to specify lineage relationships.
- Read privileges (e.g., `SELECT`) on a downstream Unity Catalog object.
- Write privileges (e.g., `MODIFY`) on an upstream Unity Catalog object.

^[external-lineage-databricks-on-aws.md]

## Modeling Patterns

### Connect Two Unity Catalog Tables

To specify a lineage relationship between two tables that are both registered in Unity Catalog, create an external metadata object that sits between them. You specify one table as upstream to the external metadata object and the other as downstream so that they appear connected in the lineage graph. This pattern is used when you want to annotate that data flows from one Unity Catalog table to another through an external process or system. ^[external-lineage-databricks-on-aws.md]

### Add Multiple Levels of Lineage

If data passes through multiple external systems before entering Databricks, you can model the full chain by creating multiple external metadata objects and configuring external lineage relationships between each of them. For example, you might create objects for a source database, an intermediate transformation tool, and a downstream dashboard, then link them sequentially. This provides a multi‑hop view of the data’s journey. ^[external-lineage-databricks-on-aws.md]

### Add Column‑Level Lineage

To capture how individual columns are transformed, include column names when you create the external metadata object. Then, when you configure the lineage relationship, map the source and target columns. This enables column‑level granularity in the lineage graph, showing exactly which columns in the external object correspond to which columns in the Unity Catalog object. ^[external-lineage-databricks-on-aws.md]

## Limitations

- External lineage is not recorded in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`).
- You can create up to 10,000 external metadata objects and 100,000 external lineage relationships per [Metastore](/concepts/metastore.md). See [Resource limits](https://docs.databricks.com/aws/en/resources/limits).

^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Overview of automatic and external lineage.
- [External Metadata Object](/concepts/external-metadata-object.md) — The securable object that represents an entity in an external system.
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for manually creating external metadata and lineage relationships.
- [Lakeflow Connect Source Lineage](/concepts/lakeflow-connect-source-lineage.md) — Automatic source lineage for managed ingestion pipelines.
- [External Metadata API](/concepts/external-metadata-api.md) — REST API for creating external metadata objects.
- [External Lineage API](/concepts/external-lineage-api.md) — REST API for creating lineage relationships.

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
