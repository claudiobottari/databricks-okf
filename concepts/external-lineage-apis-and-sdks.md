---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa0bc08d65d13a8ddcd74ed357fac19f439c0b29d3c0f14e7f2a8ab3b23194e7
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-lineage-apis-and-sdks
    - SDKs and External Lineage APIs
    - ELAAS
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Lineage APIs and SDKs
description: Programmatic interfaces for adding external lineage, including the External Metadata API, External Lineage API, and Databricks SDK for Python, in addition to the manual Catalog Explorer UI.
tags:
  - api
  - sdk
  - automation
timestamp: "2026-06-19T18:47:18.164Z"
---

# External Lineage APIs and SDKs

**External Lineage APIs and SDKs** allow you to manually add lineage metadata to [Unity Catalog](/concepts/unity-catalog.md) for workloads that run outside of Databricks. Unity Catalog automatically captures runtime data lineage from queries executed on Databricks, but you may need to represent data flows from external sources (e.g., Salesforce, MySQL) or to external consumers (e.g., Tableau, Power BI). The external lineage APIs and SDKs let you create and connect external metadata objects so that these relationships appear in the lineage graph within Unity Catalog, providing an end‑to‑end view. ^[external-lineage-databricks-on-aws.md]

You can add external lineage manually using:
- The [Catalog Explorer](/concepts/catalog-explorer.md) UI,
- The [External Metadata API](/concepts/external-metadata-api.md) and [External Lineage API](/concepts/external-lineage-api.md), or
- The Databricks SDK for Python.

Automatic source lineage recording is also available through Lakeflow Connect managed ingestion pipelines. ^[external-lineage-databricks-on-aws.md]

## External Metadata API

The External Metadata API is used to create an external metadata securable object in Unity Catalog that represents an entity in an external system, such as a dashboard in Tableau or a table in MySQL. After creating this object, you can then configure lineage relationships between it and other Unity Catalog objects using the External Lineage API. ^[external-lineage-databricks-on-aws.md]

The API is documented at the [External Metadata API reference](https://docs.databricks.com/api/workspace/externalmetadata). It is one of the programmatic options alongside the Catalog Explorer UI. ^[external-lineage-databricks-on-aws.md]

## External Lineage API

The External Lineage API is used to specify upstream or downstream lineage relationships between an external metadata object and any other Unity Catalog object (table, model, path, or another external metadata object). It supports both table‑level and column‑level mappings. ^[external-lineage-databricks-on-aws.md]

The API is documented at the [External Lineage API reference](https://docs.databricks.com/api/workspace/externallineage). You can use it to add relationships that make the external metadata object visible in the lineage graph. ^[external-lineage-databricks-on-aws.md]

## Databricks SDK for Python

The Databricks SDK for Python provides a higher‑level interface to create external metadata objects and configure lineage relationships without making raw HTTP calls. The SDK simplifies programmatic integration with Databricks APIs. ^[external-lineage-databricks-on-aws.md]

## Requirements

To use the APIs or SDK to add external lineage metadata, you must have the following privileges:

- `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md) to create an external metadata securable object.
- `MODIFY` on the external metadata object to specify lineage relationships.
- Read privileges (e.g., `SELECT`) on a Unity Catalog object to specify it as a downstream target.
- Write privileges (e.g., `MODIFY`) on a Unity Catalog object to specify it as an upstream source.

^[external-lineage-databricks-on-aws.md]

## Modeling Relationships

When using the APIs or SDK, you can model more complex scenarios:

- **Connect two Unity Catalog tables**: Create an external metadata object that sits between them, then specify one table as upstream and the other as downstream.
- **Multiple levels of lineage**: Create several external metadata objects and chain them together to represent data passing through multiple external systems.
- **Column‑level lineage**: Provide column names when creating the external metadata object and map source/target columns when adding the lineage relationship.

^[external-lineage-databricks-on-aws.md]

## Limitations

- External lineage is **not recorded** in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`).
- There are metastore‑level resource limits: up to 10,000 external metadata objects and 100,000 external lineage relationships per [Metastore](/concepts/metastore.md). ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Data Lineage](/concepts/data-lineage.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [External Metadata API](/concepts/external-metadata-api.md)
- [External Lineage API](/concepts/external-lineage-api.md)
- Databricks SDK for Python
- Lakeflow Connect

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
