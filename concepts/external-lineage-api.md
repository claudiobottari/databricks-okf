---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40c5d23ea2323855dd4f184c24189e7864b4386b1e5034336094959d2d949bbb
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-lineage-api
    - ELA
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Lineage API
description: A REST API for programmatically creating lineage relationships between external metadata objects and Unity Catalog objects (tables, models, paths, or other external metadata), with optional column-level mappings and custom metadata.
tags:
  - api
  - lineage
  - unity-catalog
  - databricks
timestamp: "2026-06-18T12:18:13.925Z"
---

# External Lineage API

The **External Lineage API** allows you to programmatically add lineage relationships between external metadata objects and Unity Catalog entities, enriching the automatically captured runtime lineage with metadata from workloads that run outside of Databricks. ^[external-lineage-databricks-on-aws.md]

## Overview

Unity Catalog automatically captures data lineage from queries executed on Databricks. However, many data pipelines include systems outside of Databricks—such as first-mile ETL sources (e.g., Salesforce, MySQL) or last-mile BI tools (e.g., Tableau, Power BI). The External Lineage API lets you model these external relationships, giving you an end-to-end view of data flow in [Unity Catalog](/concepts/unity-catalog.md). ^[external-lineage-databricks-on-aws.md]

## Prerequisites

Before using the External Lineage API, you must have the following privileges: ^[external-lineage-databricks-on-aws.md]

- `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md) to create an external metadata securable object.
- `MODIFY` on the external metadata object to specify lineage relationships between it and other objects.
- Read privileges (e.g., `SELECT`) on a Unity Catalog object to specify it as a downstream target.
- Write privileges (e.g., `MODIFY`) on a Unity Catalog object to specify it as an upstream source.

## Workflow

Using the External Lineage API involves two steps: ^[external-lineage-databricks-on-aws.md]

1. **Create an external metadata object** using the [External Metadata API](/concepts/external-metadata-api.md) or Catalog Explorer. This object represents an entity in an external system, such as a Tableau dashboard or a MySQL table.

2. **Configure lineage relationships** using the External Lineage API to connect the external metadata object to other Unity Catalog objects (tables, models, paths, or other external metadata objects).

## Supported Relationship Types

The API supports both upstream and downstream relationships between: ^[external-lineage-databricks-on-aws.md]

| Target Object Type | Description |
|-------------------|-------------|
| Table | A Unity Catalog table |
| Model | A MLflow Model version |
| Path | A volume or external location |
| External metadata | Another external metadata object |

## Column-Level Lineage

When you create an external metadata object, you can specify column names. When configuring a lineage relationship, you can then map source and target columns between the external object and the Unity Catalog object, enabling [Column-Level Lineage](/concepts/column-level-lineage.md) tracking. ^[external-lineage-databricks-on-aws.md]

## Modeling Complex Lineage

The API supports several patterns for modeling complex real-world data flows: ^[external-lineage-databricks-on-aws.md]

- **Connecting two Unity Catalog tables**: Create an external metadata object that sits between two registered tables. Specify one table as upstream and the other as downstream to show them as connected in the lineage graph.
- **Multiple levels of lineage**: Create multiple external metadata objects to annotate data passing through several systems before entering Databricks.
- **Additional metadata**: Attach JSON key-value pairs to lineage relationships, such as the text of the query that created a table or annotations explaining the external workflow.

## Limitations

- External lineage is not recorded in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`). ^[external-lineage-databricks-on-aws.md]
- You can create up to 10,000 external metadata objects and 100,000 external lineage relationships per [Metastore](/concepts/metastore.md). ^[external-lineage-databricks-on-aws.md]

## Alternative Methods

In addition to the API, you can add external lineage: ^[external-lineage-databricks-on-aws.md]

- **Manually** using [Catalog Explorer](/concepts/catalog-explorer.md) or the Databricks SDK for Python.
- **Automatically** using Lakeflow Connect managed ingestion pipelines, which record source lineage from source tables to destination tables in Unity Catalog.

## Related Concepts

- [External Metadata API](/concepts/external-metadata-api.md) — Used to create external metadata objects
- [Unity Catalog Data Lineage](/concepts/unity-catalog-data-lineage.md) — The broader lineage system in Databricks
- [Lakeflow Connect Source Lineage](/concepts/lakeflow-connect-source-lineage.md) — Automated lineage for ingestion pipelines
- [Column-Level Lineage](/concepts/column-level-lineage.md) — Granular field-level tracking
- Resource Limits in Databricks — Limits on external metadata and lineage objects

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
