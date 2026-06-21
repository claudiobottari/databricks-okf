---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 165a80c446cec32cdacda9df21b395914e530407ac8f6f91ac8f51413f8d4888
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-semantic-metadata-sync
    - SBSMS
    - SAP BDC Semantic Metadata
    - SAP BDC semantic metadata
    - SAP semantic metadata
    - sap-bdc-semantic-metadata-synchronization
    - sap-semantic-metadata-synchronization
    - SSMS
  citations:
    - file: share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md
    - file: sap-bdc-semantic-metadata-databricks-on-aws.md
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Semantic Metadata Sync
description: Automatic synchronization of SAP semantic metadata (table and column comments, primary keys, foreign keys, governance tags) into Unity Catalog when a share from SAP BDC is mounted to a catalog.
tags:
  - metadata
  - unity-catalog
  - sap-bdc
timestamp: "2026-06-19T18:00:09.465Z"
---

```markdown
# SAP BDC Semantic Metadata Sync

**SAP BDC Semantic Metadata Sync** refers to the automatic process by which business-oriented metadata from SAP Business Data Cloud (SAP BDC) is ingested into Unity Catalog when an OpenSharing share from SAP BDC is mounted as a catalog. This synchronization makes ambiguous SAP table and column names human-readable and surfaces key constraints and governance tags, thereby improving data discoverability and governance. ^[share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md, sap-bdc-semantic-metadata-databricks-on-aws.md]

## Overview

SAP table and column names are often cryptic and difficult to interpret directly. When a share received from SAP BDC is mounted to a Unity Catalog catalog, semantic metadata automatically syncs into Unity Catalog. This metadata syncs at the table level, typically upon table access. Any updates made to the metadata in SAP BDC are subsequently reflected in Unity Catalog during the next sync. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Types of Semantic Metadata Synced

The following SAP semantics are ingested into Unity Catalog: ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md, sap-bdc-semantic-metadata-databricks-on-aws.md]

- **Table and column comments** – Descriptive text that conveys the business meaning of tables and columns.
- **Primary keys and foreign keys** – Key constraints that define relationships and uniqueness between tables.
- **Governance tags** – System-governed tags in the `sap.PersonalData` namespace, which classify data as containing personal or sensitive information. These tags are automatically assigned by Databricks when SAP BDC shares are mounted.

> **Important:** Tags in the `sap.*` namespace are system-reserved. Do not manually assign, modify, or delete them. Databricks may clear or remove manually-assigned tags of this namespace later. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Read-Only Nature

SAP BDC is the authoritative source for semantic metadata. Metadata synced from SAP BDC is **read-only** in Databricks. OpenSharing recipients of SAP BDC shares cannot directly access or query the semantic metadata. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Where Metadata Is Available

After mounting a share, synced metadata is accessible across Databricks: ^[share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md, sap-bdc-semantic-metadata-databricks-on-aws.md]

- **Catalog Explorer** – View comments, key constraints, and tags in table and column details. Columns can be filtered by searching the contents of their comments.
- **SQL** – Use `DESCRIBE TABLE EXTENDED` to view table and column comments and key constraints. Query `INFORMATION_SCHEMA.TABLE_TAGS` to view SAP governance tags.
- **Genie Spaces** – In a Genie Space that includes SAP BDC tables, users can ask questions in natural language without needing to understand SAP naming conventions.
- **Governance** – Use the synced SAP governance tags in ABAC policies to control access to sensitive data.
- **Audit logs** – Metadata sync events (tag assignments, comment updates, constraint changes) are recorded in audit logs, enabling tracking of when SAP BDC metadata was ingested or updated.

## Refreshing Metadata

If the latest metadata is not visible in Catalog Explorer, clicking **Refresh Table** on the table triggers immediate ingestion of the latest sync from SAP BDC. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Related Concepts

- SAP Business Data Cloud – The source system for the synced data.
- Delta Sharing with SAP BDC – The OpenSharing mechanism used to share data.
- [[Unity Catalog]] – The catalog where metadata is stored and governed.
- [[Governed Tags and System Tags|System governed tags]] – Tags automatically assigned by Databricks.
- ABAC policies – Attribute-based access control that can reference SAP tags.
- [[Catalog Explorer]] – The UI for browsing synced metadata.
- [[Genie Space Snapshot|Genie Spaces]] – Natural-language query interface that benefits from semantic metadata.
- Audit logs – Records of metadata sync events for compliance.

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
- sap-bdc-semantic-metadata-databricks-on-aws.md
- share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md
```

# Citations

1. [share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md](/references/share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws-2f32cce2.md)
2. [sap-bdc-semantic-metadata-databricks-on-aws.md](/references/sap-bdc-semantic-metadata-databricks-on-aws-325246e0.md)
3. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
