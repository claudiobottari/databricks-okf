---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9169046e73f17786d06efd686c7759ad67bfd66f8e14ea8539673fef13770c8f
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-lineage-privileges-unity-catalog
    - ELP(C
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Lineage Privileges (Unity Catalog)
description: The specific Unity Catalog privileges required to create external metadata objects and define lineage relationships, including CREATE EXTERNAL METADATA and MODIFY privileges.
tags:
  - access-control
  - unity-catalog
  - permissions
timestamp: "2026-06-19T10:28:38.524Z"
---

# External Lineage Privileges (Unity Catalog)

**External Lineage Privileges** are the set of Unity Catalog permissions required to create and manage external lineage metadata — that is, lineage relationships that connect assets outside Databricks (such as MySQL tables, Salesforce records, or Tableau dashboards) to objects registered in Unity Catalog. These privileges control who can add external metadata objects and who can define lineage relationships between those objects and Unity Catalog securables. ^[external-lineage-databricks-on-aws.md]

## Required Privileges

Different tasks in the external lineage workflow require different privileges:

| Task | Required Privilege |
|------|-------------------|
| Create an external metadata securable object | `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md) |
| Specify lineage relationships between an external metadata object and any other Unity Catalog object | `MODIFY` on the external metadata object |
| Specify a downstream lineage relationship to a Unity Catalog object | Read privileges on the object (e.g., `SELECT` on a table) |
| Specify an upstream lineage relationship to a Unity Catalog object | Write privileges on the object (e.g., `MODIFY` on a table) |

^[external-lineage-databricks-on-aws.md]

## How Priviledges Apply

The privilege model is designed around the direction of the lineage relationship:

- **Downstream relationships**: When an external asset consumes data from a Unity Catalog object (for example, a Power BI dashboard reading from a managed table), you need at least read permission on the Unity Catalog object to define that relationship. The rationale is that you must be able to see the data to confirm it flows to the downstream system. ^[external-lineage-databricks-on-aws.md]

- **Upstream relationships**: When an external asset provides data that flows into a Unity Catalog object (for example, a Salesforce table feeding a managed table), you need write permission on the Unity Catalog object. This ensures that the person creating the lineage has authority over how data enters the object. ^[external-lineage-databricks-on-aws.md]

## Creating External Metadata Objects

To create an external metadata securable — the object that represents an external entity in the lineage graph — a user or service principal must have the `CREATE EXTERNAL METADATA` privilege on the [Metastore](/concepts/metastore.md). This is a metastore-level privilege that controls the ability to register any external metadata object. ^[external-lineage-databricks-on-aws.md]

External metadata objects can be created via:
- **Catalog Explorer UI**: Navigate to **External data > External Metadata** tab and click **Create external metadata**.
- **External Metadata API**: Use the programmatic API for automated workflows. ^[external-lineage-databricks-on-aws.md]

## Defining Lineage Relationships

Once an external metadata object exists, defining lineage relationships requires:

1. `MODIFY` privilege on the external metadata object itself (for any relationship involving it).
2. Appropriate privileges on the Unity Catalog object being connected:
   - `SELECT` (or similar read privilege) for downstream targets.
   - `MODIFY` (or similar write privilege) for upstream sources.

Relationships can be defined via:
- **Catalog Explorer UI**: Select the external metadata object and click **Create lineage relationship**.
- **External Lineage API**: Use the programmatic API.
- **Databricks SDK for Python**: Use the Python SDK for code-driven workflows. ^[external-lineage-databricks-on-aws.md]

## Relationship to Other Permissions

External lineage privileges complement, but do not replace, the standard Unity Catalog permissions on the objects themselves. Users who view lineage graphs do not need special external lineage privileges — they simply need the appropriate read privileges on the objects in the graph. ^[external-lineage-databricks-on-aws.md]

## Limitations

External lineage relationships are not recorded in Unity Catalog's system tables (`system.access.table_lineage` and `system.access.column_lineage`). This means external lineage is visible in the lineage graph UI but cannot be queried programmatically through system tables. ^[external-lineage-databricks-on-aws.md]

## Rescource Limits

A single [Metastore](/concepts/metastore.md) can contain up to 10,000 external metadata objects and 100,000 external lineage relationships. Privilege management should account for these limits when planning large-scale external lineage integration. ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [External Lineage (Unity Catalog)](/concepts/external-lineage-unity-catalog.md) — The broader concept of adding non-Databricks lineage
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The general privilege model in Unity Catalog
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Runtime lineage automatically captured by Databricks
- [External Metadata API](/concepts/external-metadata-api.md) — Programmatic interface for creating external metadata objects
- [External Lineage API](/concepts/external-lineage-api.md) — Programmatic interface for defining lineage relationships
- Lakeflow Connect — Managed ingestion that automatically records source lineage

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
