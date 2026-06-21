---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dafe9dad1e146e57ada3b0c934f3afc3a8008ebcd0751a2d9eca2c014279bdbb
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-limitations-in-unity-catalog
    - LLIUC
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Lineage Limitations in Unity Catalog
description: Known constraints including no lineage before September 2024, no preservation on renamed objects, no capture for RDDs, global temp views, spark-submit jobs, and incomplete column coverage for UDFs and path-based references.
tags:
  - limitations
  - data-governance
timestamp: "2026-06-19T14:41:07.755Z"
---

# Lineage Limitations in Unity Catalog

**Lineage Limitations in Unity Catalog** describes the known restrictions and gaps in the data lineage feature of [Unity Catalog](/concepts/unity-catalog.md). Understanding these limitations helps users avoid misinterpretation of lineage graphs and plan for alternative tracking when necessary. Lineage is automatically captured for queries run on Databricks, but several scenarios reduce its completeness or accuracy. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Data Coverage Limitations

- **Date cutoff**: Lineage data captured **before September 1, 2024** is not available. Catalog Explorer provides an **All available** option for older metastores, starting from that date. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Jobs API `runs submit` and `spark submit` tasks**: Table and column-level lineage is still captured for these workflows, but the link to the specific job run is **not** recorded. The job run does not appear in lineage views as an upstream or downstream dependency. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Renamed objects**: Lineage is **not preserved** when catalogs, schemas, tables, views, or columns are renamed. The historical lineage graph breaks for renamed identifiers. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Spark SQL dataset checkpointing**: Lineage is **not captured** for queries that use Spark SQL dataset checkpointing. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Lakeflow Spark Declarative Pipelines**: Coverage is incomplete for pipelines that use **PRIVATE tables**. Most other pipeline types are fully covered. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **RDDs and global temp views**: Resilient Distributed Datasets (RDDs) and global temp views are **not captured** in lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **`system.information_schema` tables**: Tables under `system.information_schema` are **excluded** from lineage tracking. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Column-Level Lineage Limitations

Column-level lineage is captured “as much as possible,” but the following cases prevent column-level mapping:

- **Path-based references**: If the source or target table is referenced by file path (e.g., `select * from delta."s3://bucket/path"`), column lineage is **not captured**. Column lineage is supported only when both source and target are referenced by fully qualified table name (e.g., `catalog.schema.table`). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **User-defined functions (UDFs)**: Use of UDFs can obscure the mapping between source and target columns, preventing column-level lineage from being recorded. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Compute and Runtime Requirements That Limit Lineage Capture

If the following compute requirements are not met, certain types of lineage are not captured:

- **Streaming lineage**: Lineage tracking of streaming between Delta tables requires **Databricks Runtime 11.3 LTS or above**. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Lakeflow Spark Declarative Pipelines column lineage**: Requires **Databricks Runtime 13.3 LTS or above**. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Networking**: If your workspace is deployed in a customer-managed VPC or uses AWS PrivateLink, you might need to update outbound firewall rules to allow connectivity to the Amazon Kinesis endpoint in the Databricks control plane. Failure to do so can prevent lineage data from being emitted. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Visibility and Permissions Limitations

- **`BROWSE` privilege required**: Users must have at least `BROWSE` on the parent catalog to view lineage. Without adequate object permissions, tables appear as **masked nodes** in the lineage graph, and the graph cannot be expanded beyond them. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Cross-workspace masking**: Lineage is aggregated across all workspaces attached to the same [Metastore](/concepts/metastore.md), but detailed information about workspace-level objects (notebooks, jobs, dashboards) from **other workspaces is masked**. Only the workspace where the object was created can reveal its details. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Retention Considerations

- **Catalog Explorer**: Lineage data displayed in Catalog Explorer is retained **indefinitely** for events captured after September 1, 2024. There is no rolling window for Catalog Explorer itself. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **System tables**: The `system.access.table_lineage` and `system.access.column_lineage` system tables retain a **rolling 1-year window** of data. Queries against these tables will not return events older than one year. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Notes on Transaction Behavior

[Transactions](/concepts/delta-acid-transactions.md) emit lineage events as each read and write occurs, and lineage events persist even if the transaction is subsequently rolled back. This means lineage graphs may show data flows that never materialized in a committed state. This behavior is by design, but users should be aware that rolled-back operations still appear in lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — The main feature overview
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer providing lineage
- [External Lineage](/concepts/external-lineage.md) — Registering lineage for non-Databricks assets
- System Tables for Lineage — Programmatic access to lineage data
- Manage Privileges in Unity Catalog — Permission model affecting lineage visibility
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — Pipelines with partial lineage coverage

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)
