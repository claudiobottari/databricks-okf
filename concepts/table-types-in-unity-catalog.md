---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21dd3940eacb5068b9094ad10a716e07c03bcdb2daa5975950a932ef7a11a9ee
  pageDirectory: concepts
  sources:
    - unity-catalog-securable-objects-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-types-in-unity-catalog
    - TTIUC
    - Table Formats in Unity Catalog
  citations:
    - file: unity-catalog-securable-objects-reference-databricks-on-aws.md
title: Table Types in Unity Catalog
description: Unity Catalog supports managed tables (storage managed by Unity Catalog), external tables (user-specified storage path), and foreign tables (from foreign catalogs), each with different lifecycle and governance characteristics.
tags:
  - unity-catalog
  - tables
  - data-storage
timestamp: "2026-06-19T23:15:57.270Z"
---

# Table Types in [Unity Catalog](/concepts/unity-catalog.md)

**Table Types in Unity Catalog** categorize how structured data is stored and managed within Databricks. Within a schema, a table is the primary securable object for structured data. [Unity Catalog](/concepts/unity-catalog.md) supports three primary table types: **managed tables**, **external tables**, and **foreign tables**. Each type differs in how storage location, lifecycle management, and metadata governance are handled. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Managed Tables

**Managed tables** are tables where the storage location path is determined by [Unity Catalog](/concepts/unity-catalog.md). Although [Unity Catalog](/concepts/unity-catalog.md) manages the metadata and lifecycle, the actual data files reside in the customer's cloud account. Databricks recommends using managed tables to take advantage of the latest table features, including automatic optimization, lifecycle management, and full [Unity Catalog governance](/concepts/unity-catalog-governance.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

Managed tables provide the tightest integration with [Unity Catalog](/concepts/unity-catalog.md). [Unity Catalog](/concepts/unity-catalog.md) controls the storage location, data layout, and optimization processes, making them the preferred choice for most use cases. See [Unity Catalog managed tables in Databricks for Delta Lake and Apache Iceberg](/concepts/unity-catalog-managed-tables.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## External Tables

**External tables** are tables where you specify the storage location path. [Unity Catalog](/concepts/unity-catalog.md) continues to manage the table's metadata, but does **not** manage the data's lifecycle, optimization, storage location, or layout. This means that external systems can access the data files directly, potentially bypassing [Unity Catalog governance](/concepts/unity-catalog-governance.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

External tables are useful when you need to keep data in a specific cloud storage location that is shared with other systems or when you need to maintain control over the physical data layout. However, because [Unity Catalog](/concepts/unity-catalog.md) does not manage the data lifecycle, users must handle optimization and lifecycle tasks themselves. See Work with external tables. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Foreign Tables

**Foreign tables** are tables that originate from a foreign catalog and are registered in [Unity Catalog](/concepts/unity-catalog.md) through catalog federation. These tables allow you to query data that resides in external database systems without moving the data. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

Foreign tables enable query federation scenarios where [Unity Catalog](/concepts/unity-catalog.md) acts as a unified metadata layer across multiple data sources. See Work with foreign tables. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Comparison of Table Types

| Feature | Managed Table | External Table | Foreign Table |
|---|---|---|---|
| Storage location | Determined by [Unity Catalog](/concepts/unity-catalog.md) | User-specified | External system |
| Lifecycle management | Managed by [Unity Catalog](/concepts/unity-catalog.md) | Not managed by [Unity Catalog](/concepts/unity-catalog.md) | Managed by external system |
| Optimization | Managed by [Unity Catalog](/concepts/unity-catalog.md) | User-managed | Managed by external system |
| Data location | Cloud account | Cloud account | External system |
| Governance | Full [Unity Catalog governance](/concepts/unity-catalog-governance.md) | [Unity Catalog](/concepts/unity-catalog.md) metadata only | [Unity Catalog](/concepts/unity-catalog.md) metadata only |

## Related Concepts

- Table — The primary securable object for structured data in [Unity Catalog](/concepts/unity-catalog.md)
- Schema — The second-level container that holds tables
- [Catalog](/concepts/unity-catalog.md) — The top-level container for data assets
- [Three-Level Namespace](/concepts/three-level-namespace.md) — The `catalog.schema.table` naming convention
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) — Deep dive into managed table capabilities
- External Tables — Detailed guidance on creating and managing external tables
- Catalog Federation — How foreign tables are created and used
- [Delta Lake](/concepts/delta-lake.md) — The storage format commonly used with managed tables
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — An alternative open table format supported by [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- unity-catalog-securable-objects-reference-databricks-on-aws.md

# Citations

1. [unity-catalog-securable-objects-reference-databricks-on-aws.md](/references/unity-catalog-securable-objects-reference-databricks-on-aws-c3527d93.md)
