---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e95f6129f4c0dc3bfbd6982337b64b9930efc0f8071d428d7498f6cc3309a28c
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-relationship-patterns
    - LRP
    - external-lineage-relationship-patterns
    - ELRP
    - External lineage relationship
  citations:
    - file: external-lineage-databricks-on-aws.md
title: Lineage Relationship Patterns
description: Design patterns for modeling external lineage, including chaining multiple external metadata objects, connecting two Unity Catalog tables through an intermediary, and adding column-level lineage.
tags:
  - lineage
  - modeling
  - data-governance
timestamp: "2026-06-19T10:29:17.370Z"
---

# Lineage Relationship Patterns

**Lineage Relationship Patterns** describe the standard ways to model data lineage connections between external metadata objects and Unity Catalog entities. These patterns help you represent complex data flows that span multiple systems, enabling end-to-end visibility into data provenance across your organization.

## Overview

Unity Catalog automatically captures runtime data lineage for queries that run on Databricks. For workloads that execute outside of Databricks—such as first-mile ETL or last-mile BI—you can add [External Lineage](/concepts/external-lineage.md) metadata manually using defined relationship patterns. This gives you an end-to-end lineage view that connects external sources (e.g., Salesforce, MySQL) and external consumers (e.g., Tableau, Power BI) to Unity Catalog objects. ^[external-lineage-databricks-on-aws.md]

## Core Patterns

### Connecting Two Unity Catalog Tables

To specify a lineage relationship between two tables that are both registered in Unity Catalog, create an external metadata object that sits between them. Specify one table as upstream to the external metadata object and the other as downstream so that they appear connected in the lineage graph. ^[external-lineage-databricks-on-aws.md]

This pattern is useful when the transformation between the two tables is performed outside of Databricks and you want to represent that transformation explicitly in the lineage graph.

### Adding Multiple Levels of Lineage

To annotate data that passes through multiple systems before it enters Databricks, create multiple external metadata objects and configure external lineage relationships between each of them. ^[external-lineage-databricks-on-aws.md]

For example, data might flow from a source system → an ETL tool → a staging area → a Unity Catalog table. Each intermediate system can be represented as a separate external metadata object with lineage relationships connecting them in sequence.

### Adding Column-Level Lineage

To capture column-level mappings between external objects and Unity Catalog objects, specify column names when you create the external metadata object, then map the source and target columns when you configure the lineage relationship. ^[external-lineage-databricks-on-aws.md]

Column-level lineage is useful for understanding how individual columns are transformed as data moves through the pipeline.

## Implementing Lineage Relationships

### Creating External Metadata Objects

An external metadata object represents an entity in an external system, such as a dashboard in Tableau or a table in MySQL. When creating one, you specify:

- **Name**: A human-readable name (spaces not allowed)
- **System type**: Select from common external data and BI systems, or choose **Custom**
- **Entity type**: The type of object, such as "table" or "dashboard"
- **URL**: Optional click-through URL to the external asset
- **Columns**: Optional column names for column-level mapping
- **Properties**: Optional JSON key-value pairs for tracking additional metadata ^[external-lineage-databricks-on-aws.md]

### Creating Lineage Relationships

When configuring relationships between external metadata objects and other Unity Catalog objects, you specify:

1. **Direction**: Whether the relationship is upstream (data flows from the object into Unity Catalog) or downstream (data flows from Unity Catalog to the object)
2. **Object type**: Can be a Table, Model (with a specific version), Path (for volumes or external locations), or another External Metadata object
3. **Column mappings**: Optional column-level mappings between source and target
4. **Properties**: Optional JSON metadata, such as the query text that created the table or annotations explaining the workflow ^[external-lineage-databricks-on-aws.md]

## Example: End-to-End Lineage

The following pattern represents data that flows from external databases through Databricks and out to an external report: ^[external-lineage-databricks-on-aws.md]

1. Create external metadata objects for each external system (MySQL table, PostgreSQL table)
2. Configure upstream relationships from each external object to the Unity Catalog managed table
3. Create an external metadata object for the downstream report (Tableau dashboard)
4. Configure a downstream relationship from the Unity Catalog table to the report object

The lineage graph then shows the complete data flow: MySQL and PostgreSQL → Unity Catalog table → Tableau dashboard, with column transformations represented in the relationship mappings.

## Limitations

- External lineage is not recorded in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`) ^[external-lineage-databricks-on-aws.md]
- You can create up to 10,000 external metadata objects and 100,000 external lineage relationships per [Metastore](/concepts/metastore.md) ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [External Lineage](/concepts/external-lineage.md) — The overall framework for adding lineage metadata from systems outside Databricks
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Automatically captured lineage for Databricks queries
- [Lakeflow Connect Source Lineage](/concepts/lakeflow-connect-source-lineage.md) — Automatic source lineage for managed ingestion pipelines
- [External Metadata API](/concepts/external-metadata-api.md) — Programmatic interface for creating external metadata objects
- [External Lineage API](/concepts/external-lineage-api.md) — Programmatic interface for creating lineage relationships
- Databricks SDK for Python — SDK for managing lineage relationships programmatically

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
