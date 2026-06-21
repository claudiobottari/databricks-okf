---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 28084ae2ef1e65fc9ebb57b244523bf82b7f6973355e4a8b49dba1bec0d3efb9
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - privileges-for-external-lineage-management
    - PFELM
  citations:
    - file: external-lineage-databricks-on-aws.md
title: Privileges for External Lineage Management
description: The specific Unity Catalog privileges required to create external metadata objects (CREATE EXTERNAL METADATA), specify lineage relationships (MODIFY on the external object), and define upstream/downstream relationships to UC objects (write/read privileges).
tags:
  - permissions
  - access-control
  - unity-catalog
  - lineage
timestamp: "2026-06-18T12:17:36.484Z"
---

# Privileges for External Lineage Management

**Privileges for External Lineage Management** refers to the set of Unity Catalog permissions required to create and manage external lineage metadata objects and their relationships with other Unity Catalog objects. These privileges control who can add, modify, and link external metadata representing entities from systems outside Databricks, such as source databases, ETL tools, or BI dashboards. ^[external-lineage-databricks-on-aws.md]

## Required Privileges

To add external lineage metadata in Unity Catalog, you must have specific privileges depending on the task being performed: ^[external-lineage-databricks-on-aws.md]

| Task | Required Privilege | Scope |
|------|--------------------|-------|
| Create an external metadata object | `CREATE EXTERNAL METADATA` | [Metastore](/concepts/metastore.md) |
| Specify lineage relationships from an external metadata object to other objects | `MODIFY` | External metadata object |
| Specify a downstream lineage relationship to a Unity Catalog object | Read privileges (e.g., `SELECT`) | The downstream Unity Catalog object |
| Specify an upstream lineage relationship to a Unity Catalog object | Write privileges (e.g., `MODIFY`) | The upstream Unity Catalog object |

## Privilege Details

### CREATE EXTERNAL METADATA

The `CREATE EXTERNAL METADATA` privilege is granted at the [Metastore](/concepts/metastore.md) level. This privilege allows a user or service principal to create external metadata securable objects in Unity Catalog. External metadata objects represent entities in external systems — such as a table in MySQL, a dashboard in Tableau, or a report in Power BI — that are not natively registered in Unity Catalog. ^[external-lineage-databricks-on-aws.md]

### MODIFY on External Metadata Objects

After an external metadata object is created, the `MODIFY` privilege on that object is required to configure lineage relationships between it and other Unity Catalog objects. This privilege controls who can link the external entity to tables, models, paths, or other external metadata objects in the lineage graph. ^[external-lineage-databricks-on-aws.md]

### Read and Write Privileges on Unity Catalog Objects

When establishing lineage relationships that involve native Unity Catalog objects: ^[external-lineage-databricks-on-aws.md]

- **Read privileges** (such as `SELECT` on a table) are required to specify a **downstream** relationship — meaning the Unity Catalog object is consumed by the external system. For example, if a Unity Catalog table feeds into a Tableau dashboard, you need `SELECT` on the table to create the lineage relationship.
- **Write privileges** (such as `MODIFY` on a table) are required to specify an **upstream** relationship — meaning the Unity Catalog object was created or populated from the external system. For example, if a MySQL table is ingested into a Unity Catalog managed table, you need `MODIFY` on the managed table to create the lineage link.

## Workflow Example

The typical workflow for adding external lineage involves two steps, each requiring different privileges: ^[external-lineage-databricks-on-aws.md]

1. **Create the external metadata object**: Requires `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md). This step creates a placeholder in Unity Catalog that represents an entity in an external system, such as a "Salesforce accounts" table or a "Power BI Sales Dashboard."
2. **Configure lineage relationships**: Requires `MODIFY` on the external metadata object plus the appropriate read or write privilege on the target Unity Catalog object. This step connects the external entity to its upstream data sources or downstream consumers in the lineage graph.

## Viewing Lineage Results

Once external metadata objects and their lineage relationships are configured, the external entities appear in the lineage graph view of related Unity Catalog objects. Users can see the full end-to-end data flow, including sources outside Databricks and destinations in external BI tools. ^[external-lineage-databricks-on-aws.md]

## Limitations

External lineage is not recorded in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`). Additionally, there are resource limits of up to 10,000 external metadata objects and 100,000 external lineage relationships per [Metastore](/concepts/metastore.md). ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that provides external lineage capabilities
- [External Lineage API](/concepts/external-lineage-api.md) — The REST API for programmatic lineage management
- [External Metadata API](/concepts/external-metadata-api.md) — The REST API for creating external metadata objects
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — General information about data lineage in Databricks
- Lakeflow Connect — Automatic lineage recording for managed ingestion pipelines
- Metastore-Level Privileges — The broader set of metastore-wide permissions

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
