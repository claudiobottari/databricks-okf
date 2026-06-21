---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d51d645f8e3611b21e153020b7fa73a8f744b4675511971a0bad36d13b905cb
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - modeling-external-lineage-relationships
    - MELR
  citations:
    - file: external-lineage-databricks-on-aws.md
title: Modeling External Lineage Relationships
description: Patterns for representing complex data flows through external metadata objects, including connecting two Unity Catalog tables via an intermediary object, modeling multi-hop pipelines, and adding column-level lineage with source-to-target mappings.
tags:
  - lineage
  - modeling
  - data-governance
  - best-practices
timestamp: "2026-06-18T12:18:00.282Z"
---

# Modeling External Lineage Relationships

**Modeling External Lineage Relationships** refers to the design patterns you can use when adding external lineage metadata to [Unity Catalog](/concepts/unity-catalog.md) to represent data flows that originate or terminate outside of Databricks. While Unity Catalog automatically captures runtime lineage for queries executed on Databricks, external lineage enables you to connect that view to upstream sources (e.g., Salesforce, MySQL) or downstream consumers (e.g., Tableau, Power BI). The modeling patterns described below help you represent these real-world workflows accurately in the lineage graph. ^[external-lineage-databricks-on-aws.md]

## Prerequisites

Before you can model external lineage relationships, you must have the appropriate privileges:

- `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md) to create an external metadata securable.
- `MODIFY` on the external metadata object to specify lineage relationships.
- Read privileges (e.g., `SELECT`) on a Unity Catalog object if it is downstream of the external metadata.
- Write privileges (e.g., `MODIFY`) on a Unity Catalog object if it is upstream of the external metadata. ^[external-lineage-databricks-on-aws.md]

An external metadata object must first be created (via Catalog Explorer, the [External Metadata API](https://docs.databricks.com/api/workspace/externalmetadata), or the [Databricks SDK for Python](https://docs.databricks.com/aws/en/dev-tools/sdk-python)). Each object represents an entity in an external system, such as a table, dashboard, or report. You then add lineage relationships between that object and other Unity Catalog objects (tables, models, paths, or other external metadata objects). ^[external-lineage-databricks-on-aws.md]

## Common Modeling Patterns

### Connect Two Unity Catalog Tables

When you need to show a lineage relationship between two tables that are both already registered in Unity Catalog—but the transformation happens outside Databricks (for example, a SQL query run in an external ETL tool)—create an intermediate external metadata object that sits between them.

1. Create an external metadata object representing the external operation (e.g., an ETL job).
2. Point the upstream Unity Catalog table as input to the external metadata object.
3. Point the external metadata object as input to the downstream Unity Catalog table.

The lineage graph will show the two tables connected through the external metadata object, accurately reflecting the external workflow. ^[external-lineage-databricks-on-aws.md]

### Add Multiple Levels of Lineage

Data often passes through several external systems before reaching Databricks. To model this, create multiple external metadata objects—one for each system—and chain them with upstream/downstream relationships.

For example:

- External metadata object `MySQL` (source table) → External metadata object `Airflow` (ETL pipeline) → External metadata object `S3 staging` (intermediate storage) → Unity Catalog table.

Each node in the chain represents a distinct system or stage, and you configure lineage relationships between each adjacent pair. ^[external-lineage-databricks-on-aws.md]

### Add Column-Level Lineage

When you create the external metadata object, you can list its columns (e.g., `id`, `name`, `release_date`). Then, when you configure a lineage relationship, you can map source columns to target columns.

This is useful for documenting how columns from an upstream system are transformed or renamed before reaching a Unity Catalog table. Column-level mappings appear in the lineage graph when viewers inspect the relationship. ^[external-lineage-databricks-on-aws.md]

### External Lineage for Models and Paths

External lineage is not limited to tables. You can also connect external metadata objects to:

- **Models** – select the model and the model version.
- **Paths** – for volumes or external locations.
- **Other external metadata objects** – enabling the multi-level patterns above. ^[external-lineage-databricks-on-aws.md]

## Example Workflow

The following diagram (conceptual) shows two external upstream sources (MySQL, PostgreSQL) being ingested into a Unity Catalog table, with columns mapped, and then consumed by an external dashboard:

```
[MySQL table] ──→ [External metadata: ingestion job] ──→ [Unity Catalog managed table]
[PostgreSQL table] ──→ [External metadata: ingestion job] ──→ [Unity Catalog managed table]
                                                                    │
                                                                    ↓
                                                          [External metadata: Tableau dashboard]
```

In this scenario, you would create external metadata objects for the MySQL table, the PostgreSQL table, the ingestion job, and the Tableau dashboard, then wire the upstream/downstream relationships and add column-level mappings as needed. ^[external-lineage-databricks-on-aws.md]

## Automatic Modeling via Lakeflow Connect

For managed ingestion pipelines created by Lakeflow Connect, external lineage is recorded automatically. Lakeflow Connect captures source-to-destination lineage from the source tables to the Unity Catalog destination tables, without requiring manual object creation. See Track source data lineage for managed ingestion pipelines. ^[external-lineage-databricks-on-aws.md]

## Limitations

- External lineage is **not** recorded in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`). ^[external-lineage-databricks-on-aws.md]
- You can create up to **10,000 external metadata objects** and **100,000 external lineage relationships** per [Metastore](/concepts/metastore.md). See Resource limits. ^[external-lineage-databricks-on-aws.md]

## Best Practices

- **Use descriptive names** for external metadata objects so that Databricks users can easily understand what a node represents in the lineage graph.
- **Include URLs** where possible so viewers can click through to the external asset (e.g., a Tableau dashboard URL).
- **Add annotations** via JSON key-value properties to record the query text or workflow description for the relationship.
- **Keep column-level mappings accurate** to enable downstream impact analysis and provenance tracking.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where external lineage is stored
- [Data Lineage](/concepts/data-lineage.md) – Automatic lineage captured by Databricks
- Lakeflow Connect – Automated source lineage for managed ingestion pipelines
- [External Metadata API](/concepts/external-metadata-api.md) – REST API for creating external metadata objects
- [External Lineage API](/concepts/external-lineage-api.md) – REST API for creating lineage relationships
- Resource limits – [Metastore](/concepts/metastore.md) quotas for external objects and relationships

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
