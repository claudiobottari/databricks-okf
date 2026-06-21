---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8a1e7926d8aebb3e56fbeb829ab31f59cee64f12355099c86fa9e4078f96f9b
  pageDirectory: concepts
  sources:
    - sap-bdc-semantic-metadata-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-semantic-metadata-ingestion
    - SBSMI
  citations:
    - file: sap-bdc-semantic-metadata-databricks-on-aws.md
title: SAP BDC Semantic Metadata Ingestion
description: Automatic syncing of SAP Business Data Cloud table and column semantic metadata (comments, constraints, tags) into Databricks Unity Catalog for mounted SAP BDC shares.
tags:
  - data-integration
  - unity-catalog
  - sap
  - metadata-management
timestamp: "2026-06-19T20:18:00.598Z"
---

## SAP BDC Semantic Metadata Ingestion

**SAP BDC Semantic Metadata Ingestion** refers to the automatic synchronization of business metadata from SAP Business Data Cloud (SAP BDC) into [Unity Catalog](/concepts/unity-catalog.md) when an SAP BDC share is mounted. This ingestion process makes SAP data more understandable and discoverable within the Databricks environment by translating cryptic SAP table and column names into readable business descriptions. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Overview

SAP table and column names are often difficult to interpret. For all mounted SAP BDC shares, semantic metadata is automatically ingested at the table level when a table is accessed. Any changes made in SAP BDC are reflected in Unity Catalog. SAP BDC remains the source of truth for semantic metadata; metadata synced from SAP BDC is read-only in Databricks. OpenSharing recipients of SAP BDC shares cannot directly access or query the semantic metadata. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Semantic Metadata Types

The following semantics from SAP BDC are ingested into Unity Catalog:

- **Comments**: Business-friendly descriptions for tables and columns are synced as comments, enabling users to understand the meaning of data without relying on raw SAP naming conventions. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

- **Key Constraints**: Primary key and foreign key relationships defined in SAP BDC are ingested as key constraints in Unity Catalog, preserving the data model’s referential integrity. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

- **Governance Tags (Personal Data)**: SAP BDC syncs governance tags in the `sap.PersonalData` namespace as [system governed tags](/concepts/governed-tags.md) on tables in Unity Catalog. These tags classify whether SAP BDC data contains personal or sensitive information. Tags in the `sap.*` namespace are system-reserved and should not be manually assigned, modified, or deleted — the Databricks system automatically assigns them when SAP BDC shares are mounted, and manual changes may be cleared by the system. To govern access based on these tags, create [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies that reference them. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Where Metadata Is Used

After mounting an SAP BDC share to a catalog, the synced metadata becomes available across Databricks:

- **[Catalog Explorer](/concepts/catalog-explorer.md)**: View comments, key constraints, and tags in table and column details. Columns can be filtered by searching comment contents to find relevant columns. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

- **SQL**: Use `DESCRIBE TABLE EXTENDED` to view table and column comments and key constraints. Query `INFORMATION_SCHEMA.TABLE_TAGS` to view SAP governance tags. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

- **Genie Spaces**: In a Genie Space that includes SAP BDC tables, users can ask questions in natural language without needing to understand SAP naming conventions. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

- **Governance**: Use synced SAP governance tags in ABAC policies to control access to sensitive data. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

- **Audit logs**: Metadata sync events — including tag assignments, comment updates, and constraint changes — are recorded in audit logs. Use these logs to track when SAP BDC metadata was ingested or updated in the catalog. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Refresh Mechanism

If the latest metadata is not visible in Catalog Explorer, click **Refresh Table** to trigger a manual ingestion of the current SAP BDC metadata. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Related Concepts

- [SAP BDC Connector](/concepts/sap-bdc-connector.md) – how to create and manage the SAP BDC connection
- Unity Catalog tags – system tags and user-defined tags
- [Delta Sharing](/concepts/delta-sharing.md) – the underlying protocol for sharing SAP data
- Data governance – how ABAC policies use governance tags
- [OpenSharing](/concepts/opensharing.md) – recipient model for SAP BDC shares

### Sources

- sap-bdc-semantic-metadata-databricks-on-aws.md

# Citations

1. [sap-bdc-semantic-metadata-databricks-on-aws.md](/references/sap-bdc-semantic-metadata-databricks-on-aws-325246e0.md)
