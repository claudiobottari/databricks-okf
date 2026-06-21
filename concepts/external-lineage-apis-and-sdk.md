---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5c3891ce5902735cb47fd58e26ab8aefa1738fe29f276c4ed11345570a140c6
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-lineage-apis-and-sdk
    - SDK and External Lineage APIs
    - ELAAS
    - external-lineage-apis-and-sdks
    - SDKs and External Lineage APIs
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Lineage APIs and SDK
description: Programmatic interfaces including the External Metadata API, External Lineage API, and Databricks SDK for Python for managing external lineage without the UI.
tags:
  - api
  - sdk
  - automation
  - lineage
timestamp: "2026-06-19T10:30:01.616Z"
---

# External Lineage APIs and SDK

**External Lineage APIs and SDK** enable you to programmatically add external lineage metadata to [Unity Catalog](/concepts/unity-catalog.md), supplementing the runtime lineage that Databricks automatically captures from queries executed within the platform. This allows you to build an end-to-end lineage view that encompasses data sources and consumers outside of Databricks, such as first-mile ETL systems (e.g., Salesforce, MySQL) and last-mile BI tools (e.g., Tableau, Power BI). ^[external-lineage-databricks-on-aws.md]

## Overview

While Unity Catalog automatically captures data lineage for queries run on Databricks, you may have workloads that operate outside the platform. External lineage APIs and SDKs allow you to augment the automatically captured lineage with metadata from these external systems. ^[external-lineage-databricks-on-aws.md]

You can add external lineage in two ways:

- **Manually**, using the [Catalog Explorer](/concepts/catalog-explorer.md) UI, the External Metadata API, the External Lineage API, or the Databricks SDK for Python.
- **Automatically**, using Lakeflow Connect managed ingestion pipelines, which record source lineage from source tables to destination tables in Unity Catalog. ^[external-lineage-databricks-on-aws.md]

## APIs

### External Metadata API

The **External Metadata API** is used to create external metadata securable objects in Unity Catalog. These objects represent entities in external systems, such as dashboards in Tableau, tables in MySQL, or custom data sources. ^[external-lineage-databricks-on-aws.md]

Key capabilities:

- Define external metadata objects with properties including name, system type (e.g., Tableau, Power BI, MySQL), entity type (e.g., table, dashboard), URL, description, and columns for column-level lineage.
- Specify additional properties as JSON key-value pairs. ^[external-lineage-databricks-on-aws.md]

### External Lineage API

The **External Lineage API** is used to configure lineage relationships between external metadata objects and other Unity Catalog objects (tables, models, paths, or other external metadata objects). ^[external-lineage-databricks-on-aws.md]

Key capabilities:

- Create upstream relationships (e.g., an external source feeding into a Unity Catalog table).
- Create downstream relationships (e.g., a Unity Catalog table being consumed by an external dashboard).
- Add column-level mappings between source and target objects.
- Attach additional metadata as JSON key-value pairs (e.g., query text or workflow annotations). ^[external-lineage-databricks-on-aws.md]

## Python SDK

The Databricks SDK for Python provides programmatic access to both the External Metadata and External Lineage APIs, enabling you to automate the creation and management of external lineage within your data pipelines and CI/CD workflows. ^[external-lineage-databricks-on-aws.md]

## Prerequisites and Permissions

To add external lineage metadata, you must have the following privileges: ^[external-lineage-databricks-on-aws.md]

| Task | Required Privilege |
|------|-------------------|
| Create an external metadata securable object | `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md) |
| Specify lineage relationships from an external metadata object to another Unity Catalog object | `MODIFY` on the external metadata object |
| Specify a downstream lineage relationship to a Unity Catalog object | Read privileges on the object (e.g., `SELECT` on a table) |
| Specify an upstream lineage relationship to a Unity Catalog object | Write privileges on the object (e.g., `MODIFY` on a table) |

## Modeling Complex Relationships

When adding external lineage manually, you can model more complex relationships: ^[external-lineage-databricks-on-aws.md]

- **Connect two Unity Catalog tables**: Create an external metadata object that sits between two tables already registered in Unity Catalog. Specify one table as upstream and the other as downstream so they appear connected in the lineage graph.
- **Add multiple levels of lineage**: Create multiple external metadata objects and configure lineage relationships between each of them to annotate data that passes through multiple systems before entering Databricks.
- **Add column-level lineage**: Specify column names when creating the external metadata object, then map source and target columns when configuring the lineage relationship.

## Limitations

- External lineage is not recorded in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`). ^[external-lineage-databricks-on-aws.md]
- You can create up to 10,000 external metadata objects and 100,000 external lineage relationships per [Metastore](/concepts/metastore.md). ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Automatic lineage capture for Databricks workloads
- [External Metadata](/concepts/external-metadata-api.md) — The securable objects representing external systems
- [Lakeflow Connect Source Lineage](/concepts/lakeflow-connect-source-lineage.md) — Automatic external lineage for ingestion pipelines
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for managing external lineage
- Databricks SDK for Python — Programmatic access to Databricks APIs
- Resource Limits — [Metastore](/concepts/metastore.md) capacity constraints

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
