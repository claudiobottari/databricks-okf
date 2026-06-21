---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 239e46427fd49c85d44e38548a88c088c74a054c46d61e2b3f303724827144af
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-metadata-api
    - EMA
    - External Metadata
    - external metadata
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Metadata API
description: A REST API for programmatically creating and managing external metadata objects in Unity Catalog, including specifying names, system types, entity types, URLs, column definitions, and custom properties.
tags:
  - api
  - metadata
  - lineage
  - unity-catalog
timestamp: "2026-06-18T12:17:50.883Z"
---

```markdown
---
title: External Metadata API
summary: The External Metadata API allows users to create and manage external metadata securable objects in Unity Catalog, representing entities in external data or BI systems, and to establish lineage relationships between those objects and Unity Catalog assets.
sources:
  - external-lineage-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:04:29.448Z"
updatedAt: "2026-06-18T08:04:29.448Z"
tags:
  - unity-catalog
  - lineage
  - api
  - external-metadata
aliases:
  - external-metadata-api
  - EMA
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# External Metadata API

The **External Metadata API** is a REST API provided by Databricks that lets you programmatically add external lineage metadata to [[Unity Catalog]]. It enables you to create external metadata securable objects representing entities in external systems—such as databases, dashboards, or reports—and to define lineage relationships between those objects and Unity Catalog tables, models, paths, or other external metadata objects. ^[external-lineage-databricks-on-aws.md]

## Purpose

Unity Catalog automatically captures runtime data lineage for queries executed inside Databricks. The External Metadata API fills the gap for workloads that run outside Databricks—for example, first-mile ETL (before ingestion) or last-mile BI (after export). By adding external metadata objects and lineage relationships, you get an end-to-end lineage view that includes sources like Salesforce or MySQL and destinations like Tableau or Power BI. ^[external-lineage-databricks-on-aws.md]

## Using the API

The External Metadata API is one of the manual methods for adding external lineage. You can also use [[Catalog Explorer]] UI or the Databricks SDK for Python. The API corresponds to the following endpoint (as referenced in the Databricks API documentation):

- **External Metadata API**: `https://docs.databricks.com/api/workspace/externalmetadata`
- **External Lineage API**: `https://docs.databricks.com/api/workspace/externallineage`

Use the External Metadata API to create external metadata objects, and the External Lineage API to create lineage relationships between them and Unity Catalog objects. ^[external-lineage-databricks-on-aws.md]

### Creating an External Metadata Object

An external metadata object represents an entity in an external system, such as a table in MySQL or a dashboard in Tableau. Required fields include:

- **Name**: A human-readable identifier (no spaces).
- **System type**: Select from common external systems or use "Custom".
- **Entity type**: Describe the type of object (e.g., "table", "dashboard").

Optional fields include:

- **URL**: A click-through URL to the external asset.
- **Description**: Free-text.
- **Columns**: For column-level mapping, enter column names (UI or comma-delimited text).
- **Properties**: Arbitrary JSON key-value pairs for additional metadata. ^[external-lineage-databricks-on-aws.md]

### Creating Lineage Relationships

Lineage relationships can be created using Catalog Explorer, the [[External Lineage API]], or the Databricks SDK for Python. For each relationship, you specify:

- Direction: **Upstream** (data source) or **Downstream** (data consumer).
- Target object type: **Table**, **Model** (with version), **Path** (for volumes or external locations), or **External metadata**.
- Optional advanced settings: Column mappings and additional metadata (e.g., query text, annotations). ^[external-lineage-databricks-on-aws.md]

## Requirements

To use the External Metadata API, you need the following privileges:

- `CREATE EXTERNAL METADATA` on the [[metastore|Metastore]] to create external metadata objects.
- `MODIFY` on the external metadata object to define lineage relationships from it.
- For downstream relationships to a Unity Catalog object: read privilege (e.g., `SELECT` on a table).
- For upstream relationships from a Unity Catalog object: write privilege (e.g., `MODIFY` on a table). ^[external-lineage-databricks-on-aws.md]

## Limitations

- External lineage is **not** recorded in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`).
- Limits apply:
  - Up to 10,000 external metadata objects per [[metastore|Metastore]].
  - Up to 100,000 external lineage relationships per [[metastore|Metastore]]. ^[external-lineage-databricks-on-aws.md]

## Modeling Complex Lineage

The API supports patterns beyond simple one-hop relationships:

- **Connect two Unity Catalog tables**: Create an external metadata object that sits between them, specifying one table as upstream and the other as downstream.
- **Multiple levels**: Create multiple external metadata objects and chain them via lineage relationships to represent a multi-stage pipeline.
- **Column-level lineage**: Specify column names when creating the external metadata object, then map source and target columns when configuring the lineage relationship. ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [[External Lineage]] — The broader feature that provides end-to-end lineage for external systems
- [[External Lineage API]] — The accompanying API for defining lineage relationships
- [[Data Lineage in Unity Catalog]] — The automatic lineage capture within Databricks
- [[Unity Catalog]] — The governance layer where external metadata objects are registered
- [[Catalog Explorer]] — The UI for manual external lineage management
- Lakeflow Connect — Managed ingestion that automatically records source lineage

## Sources

- external-lineage-databricks-on-aws.md
```

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
