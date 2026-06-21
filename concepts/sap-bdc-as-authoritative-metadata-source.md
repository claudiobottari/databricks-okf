---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c0beef95b0007aec512c39f128898b54753e08ef7e3e3d3439b3cc625c40815
  pageDirectory: concepts
  sources:
    - sap-bdc-semantic-metadata-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-as-authoritative-metadata-source
    - SBAAMS
  citations:
    - file: sap-bdc-semantic-metadata-databricks-on-aws.md
title: SAP BDC as Authoritative Metadata Source
description: SAP Business Data Cloud is the source of truth for semantic metadata; metadata synced into Databricks is read-only and cannot be directly modified by users or OpenSharing recipients.
tags:
  - data-lineage
  - sap
  - metadata-management
  - data-governance
timestamp: "2026-06-19T20:18:20.881Z"
---

# SAP BDC as Authoritative Metadata Source

**SAP BDC as Authoritative Metadata Source** refers to the role of SAP Business Data Cloud (BDC) as the single source of truth for semantic metadata that is automatically synchronized into [Unity Catalog](/concepts/unity-catalog.md) for mounted SAP BDC shares. This metadata is read-only in Databricks and cannot be directly queried by OpenSharing recipients. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Overview

SAP table and column names can be difficult to read. For all mounted SAP BDC shares, semantic metadata is automatically ingested into Unity Catalog at the table level when a table is accessed, making the data more understandable and discoverable. Any changes made in SAP BDC are reflected in Unity Catalog. SAP BDC is the authoritative source of truth for this metadata; metadata synced from SAP BDC is read-only in Databricks. OpenSharing recipients of SAP BDC shares cannot directly access or query the semantic metadata. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

To see the latest metadata in Catalog Explorer, users can click **Refresh Table** to trigger ingestion. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## SAP Semantic Types Ingested

The following semantics from SAP BDC are ingested into Unity Catalog:

- Table and column comments
- Key constraints
- Data lineage
- Personal data tags
- Sensitive information tags

^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Tag Namespace and Governance

SAP BDC syncs governance tags in the `sap.PersonalData` namespace as system governed tags on tables in Unity Catalog. These tags classify whether SAP BDC data contains personal or sensitive information. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

> **Important:** Do not manually assign, modify, or delete tags in the `sap.*` namespace. These are system-reserved values automatically assigned by the Databricks system when SAP BDC shares are mounted. If manually assigned, Databricks might clear or remove them later. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

To govern access based on these tags, create [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies that reference them. The following tags are synced (see the SAP CSN Interop specification for more information on SAP personal data annotations):
- `sap.PersonalData.Personal`
- `sap.PersonalData.Sensitive`

^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Using Synced Metadata

After mounting an SAP BDC share to a catalog, synced metadata is available across multiple Databricks surfaces:

### Catalog Explorer
View comments, key constraints, and tags in the table and column details. Users can filter columns by searching for the contents of their comments, making it easier to find relevant columns. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### SQL
Use `DESCRIBE TABLE EXTENDED` to view table and column comments and key constraints. Query `INFORMATION_SCHEMA.TABLE_TAGS` to view SAP governance tags. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Genie Spaces
In a Genie Space that includes SAP BDC tables, users can ask questions in natural language without needing to understand SAP naming conventions. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Governance
Use synced SAP governance tags in [Unity Catalog ABAC policies](/concepts/unity-catalog-abac-row-filter-policies.md) to control access to sensitive data. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Audit Logs
Metadata sync events, including tag assignments, comment updates, and constraint changes, are recorded in audit logs. Use audit logs to track when SAP BDC metadata was ingested or updated in your catalog. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Sources

- sap-bdc-semantic-metadata-databricks-on-aws.md

# Citations

1. [sap-bdc-semantic-metadata-databricks-on-aws.md](/references/sap-bdc-semantic-metadata-databricks-on-aws-325246e0.md)
