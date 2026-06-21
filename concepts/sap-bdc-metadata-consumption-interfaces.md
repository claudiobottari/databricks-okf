---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38b23c9b62cdf3af1ea694a68f55aa0a3d37470796fe6101b31ec1c84e9c5d54
  pageDirectory: concepts
  sources:
    - sap-bdc-semantic-metadata-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-metadata-consumption-interfaces
    - SBMCI
  citations:
    - file: sap-bdc-semantic-metadata-databricks-on-aws.md
title: SAP BDC Metadata Consumption Interfaces
description: "Multiple Databricks interfaces for consuming synced SAP BDC metadata: Catalog Explorer, SQL (DESCRIBE TABLE, INFORMATION_SCHEMA), Genie Spaces natural language queries, ABAC governance policies, and audit logs."
tags:
  - data-discovery
  - unity-catalog
  - sap
  - user-interfaces
timestamp: "2026-06-19T20:18:07.776Z"
---

# SAP BDC Metadata Consumption Interfaces

**SAP BDC Metadata Consumption Interfaces** refers to the various ways that semantic metadata automatically synced from SAP Business Data Cloud (BDC) into Unity Catalog can be accessed, queried, and used within the Databricks platform. When SAP BDC shares are mounted to a catalog, semantic metadata — including comments, key constraints, and governance tags — becomes available across multiple Databricks interfaces. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Available Interfaces

### Catalog Explorer

In **Catalog Explorer**, users can view comments, key constraints, and tags in the table and column details. Columns can be filtered by searching the contents of their comments, making it easier to locate relevant columns within SAP tables. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### SQL Queries

Users can run `DESCRIBE TABLE EXTENDED` to view table-level and column-level comments as well as key constraints. To view SAP governance tags, query the `INFORMATION_SCHEMA.TABLE_TAGS` system table. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Genie Spaces

In a Genie Space that includes SAP BDC tables, users can ask questions in natural language without needing to understand SAP naming conventions. The synced semantic metadata allows Genie to interpret and respond to queries about the underlying SAP data. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Governance Interfaces

Synced SAP [governance tags](/concepts/governed-tags.md) can be referenced in [Attribute-Based Access Control (ABAC) policies](/concepts/attribute-based-access-control-abac.md) to control access to sensitive data. Tags in the `sap.PersonalData` namespace classify whether SAP BDC data contains personal or sensitive information. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

**Important**: Tags in the `sap.*` namespace are system-reserved values automatically assigned by Databricks when SAP BDC shares are mounted. They should not be manually assigned, modified, or deleted, as Databricks might clear or remove them later. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Audit Logs

Metadata sync events — including tag assignments, comment updates, and constraint changes — are recorded in audit logs. These logs can be used to track when SAP BDC metadata was ingested or updated in a catalog. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Metadata Refresh

If the latest metadata does not appear in Catalog Explorer, clicking **Refresh Table** triggers metadata ingestion. SAP BDC is the source of truth for semantic metadata, and metadata synced from SAP BDC is read-only in Databricks. OpenSharing recipients of SAP BDC shares cannot directly access or query the semantic metadata. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Related Concepts

- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md)
- Unity Catalog Tags
- [System Tags](/concepts/system-tags.md)
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md)
- [Delta Sharing](/concepts/delta-sharing.md)

## Sources

- sap-bdc-semantic-metadata-databricks-on-aws.md

# Citations

1. [sap-bdc-semantic-metadata-databricks-on-aws.md](/references/sap-bdc-semantic-metadata-databricks-on-aws-325246e0.md)
