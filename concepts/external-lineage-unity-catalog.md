---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a91f6c3e12469e917f205fc7087cb180628499d842aef03a922ac3248626ab4f
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-lineage-unity-catalog
    - EL(C
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Lineage (Unity Catalog)
description: The ability to manually or automatically add lineage metadata for data sources and consumers outside of Databricks, enabling end-to-end data lineage views in Unity Catalog.
tags:
  - data-governance
  - lineage
  - unity-catalog
timestamp: "2026-06-19T10:28:27.777Z"
---

# External Lineage (Unity Catalog)

**External Lineage** in Unity Catalog allows you to augment the automatically captured runtime data lineage from Databricks with metadata about workloads that run outside Databricks. This provides an end-to-end view of data flow from sources (e.g., Salesforce, MySQL) before ingestion into Unity Catalog, through Databricks transformations, and to downstream consumers (e.g., Tableau, Power BI).^[external-lineage-databricks-on-aws.md]

## Overview

Unity Catalog automatically captures data lineage for queries executed on Databricks. However, data often originates from or is consumed by external systems. External lineage enables you to manually or automatically record these relationships, enriching the lineage graph with entries for external tables, dashboards, reports, and other assets.^[external-lineage-databricks-on-aws.md]

You can add external lineage in two ways:
- **Manually** – using the [Catalog Explorer](/concepts/catalog-explorer.md) UI, the [External Metadata API](/concepts/external-metadata-api.md), the [External Lineage API](/concepts/external-lineage-api.md), or the Databricks SDK for Python.^[external-lineage-databricks-on-aws.md]
- **Automatically** – using Lakeflow Connect managed ingestion pipelines, which record source lineage from source tables to destination tables in Unity Catalog.^[external-lineage-databricks-on-aws.md]

## Use Cases

- **First-mile ETL**: Capture the origin of data before it enters Databricks (e.g., a MySQL table or a Salesforce object).^[external-lineage-databricks-on-aws.md]
- **Last-mile BI**: Track where data is consumed outside Databricks (e.g., a Tableau dashboard or Power BI report).^[external-lineage-databricks-on-aws.md]
- **Multi-hop pipelines**: Annotate data passing through multiple external systems before reaching Databricks.^[external-lineage-databricks-on-aws.md]

## Requirements

To add external lineage metadata, you need the following privileges:^[external-lineage-databricks-on-aws.md]

| Action | Required Privilege |
|--------|--------------------|
| Create an external metadata securable object | `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md) |
| Specify lineage relationships from an external metadata object to any other Unity Catalog object | `MODIFY` on the external metadata object |
| Specify a downstream lineage relationship to a Unity Catalog object | Read privileges on the object (e.g., `SELECT` on a table) |
| Specify an upstream lineage relationship to a Unity Catalog object | Write privileges on the object (e.g., `MODIFY` on a table) |

## Adding External Lineage Manually

Adding external lineage manually involves two steps: creating an **external metadata object** that represents the external entity, and then creating **lineage relationships** between that object and other Unity Catalog objects.

### Create an External Metadata Object

You can create an external metadata object using the Catalog Explorer UI or the External Metadata API.^[external-lineage-databricks-on-aws.md]

To use Catalog Explorer:

1. In your Databricks workspace, click the **Catalog** icon, then click **External data**.
2. Go to the **External Metadata** tab and click **Create external metadata**.
3. Specify the details:
   - **Name** – A human-readable name (no spaces) that helps users identify the external asset in lineage.
   - **System type** – Select from a list of common external data and BI systems, or choose **Custom**.
   - **Entity type** – Enter the type of object, such as "table" or "dashboard".
   - **URL** (optional) – A clickable link to the external asset (e.g., a Tableau dashboard URL).
   - **Description** (optional).
   - **Columns** (optional) – For column-level lineage, enter column names one at a time or as a comma-delimited list.
   - **Properties** (optional) – JSON key-value pairs for additional metadata, such as the query text that created the table.
4. Click **Create**. A dialog offers the option to immediately create lineage relationships.

### Create Lineage Relationships

After the external metadata object exists, you can create lineage relationships between it and other Unity Catalog objects (tables, models, paths, or other external metadata objects) using Catalog Explorer, the External Lineage API, or the Databricks SDK for Python.^[external-lineage-databricks-on-aws.md]

To add relationships via Catalog Explorer:

1. Navigate to the external metadata object in Catalog Explorer (under **External data** > **External Metadata**).
2. Click **Create lineage relationship**.
3. Choose whether the relationship is **upstream** or **downstream**.
4. Enter the **Object type** of the target:
   - **Table** – Search for the table.
   - **Model** – Select the model and choose the model version.
   - **Path** – For volumes or external locations, enter the path.
   - **External metadata** – Select another external metadata object.
5. (Optional) Under **Advanced**, add:
   - Column mappings between the external object and the source/target.
   - Additional metadata as JSON key-value pairs (e.g., query text, annotations).
6. Click **Create**.

The external lineage relationship now appears in the **Lineage** tab of the related objects.

## Automatic Lineage with Lakeflow Connect

For managed ingestion pipelines, Lakeflow Connect automatically records source lineage from the source tables (e.g., a MySQL database) to the destination tables in Unity Catalog. See Track source data lineage for managed ingestion pipelines.^[external-lineage-databricks-on-aws.md]

## Modeling Complex Lineage Relationships

When adding external lineage manually, use these patterns to represent more complex data flows:^[external-lineage-databricks-on-aws.md]

- **Connect two Unity Catalog tables** – Create an external metadata object that sits between the two tables. Specify one table as upstream to the external object and the other as downstream. This connects them in the lineage graph.
- **Add multiple levels of lineage** – To annotate data that passes through several systems before reaching Databricks, create multiple external metadata objects and configure lineage relationships between each of them.
- **Add column-level lineage** – When creating the external metadata object, specify column names. Then, when configuring a lineage relationship, map source columns to target columns.

## Limitations

- External lineage is **not recorded** in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`).^[external-lineage-databricks-on-aws.md]
- Per [Metastore](/concepts/metastore.md) resource limits apply: up to **10,000 external metadata objects** and **100,000 external lineage relationships**. See Resource limits.^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) – Overview of automatically captured lineage.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that stores and displays lineage.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI for managing external lineage.
- [External Metadata API](/concepts/external-metadata-api.md) – REST API for creating external metadata objects.
- [External Lineage API](/concepts/external-lineage-api.md) – REST API for creating lineage relationships.
- Databricks SDK for Python – Programmatic access to external lineage.
- Lakeflow Connect – Managed ingestion with automatic source lineage.
- System Tables – Where external lineage is not recorded.
- Resource Limits – Quotas for external metadata and lineage.

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
