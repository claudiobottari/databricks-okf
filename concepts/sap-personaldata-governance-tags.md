---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15d71df03c1c9485500c78b07e7c7512014b44b65f0a7c0b376b63649d575922
  pageDirectory: concepts
  sources:
    - sap-bdc-semantic-metadata-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-personaldata-governance-tags
    - SPGT
  citations:
    - file: sap-bdc-semantic-metadata-databricks-on-aws.md
title: SAP PersonalData Governance Tags
description: System-reserved governance tags in the sap.PersonalData namespace that automatically sync from SAP BDC into Unity Catalog to classify tables containing personal or sensitive information.
tags:
  - data-governance
  - sap
  - privacy
  - tagging
timestamp: "2026-06-19T20:18:08.772Z"
---

# SAP PersonalData Governance Tags

**SAP PersonalData Governance Tags** are system-governed tags in the `sap.PersonalData` namespace that automatically sync from SAP Business Data Cloud (BDC) into [Unity Catalog](/concepts/unity-catalog.md) for mounted SAP BDC shares. These tags classify whether SAP BDC data contains personal or sensitive information, enabling attribute-based access control (ABAC) policies to govern data access. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Overview

When SAP BDC shares are mounted to Unity Catalog, SAP BDC syncs governance tags in the `sap.PersonalData` namespace as system governed tags on tables in Unity Catalog. These tags make the data more understandable and discoverable by indicating which tables and columns contain personal or sensitive information, even when SAP table and column names are difficult to interpret. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Important Usage Notes

SAP BDC is the source of truth for semantic metadata. Metadata synced from SAP BDC is read-only in Databricks. OpenSharing recipients of SAP BDC shares cannot directly access or query the semantic metadata. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

**Do not manually assign, modify, or delete tags in the `sap.*` namespace.** These are system-reserved values automatically assigned by the Databricks system when SAP BDC shares are mounted. If you assign them manually, Databricks might clear or remove them later. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## How Tags Are Synced

Semantic metadata is automatically ingested into Unity Catalog at the table level when a table is accessed. Any changes made in SAP BDC are reflected in Unity Catalog. If you don't see the latest metadata in [Catalog Explorer](/concepts/catalog-explorer.md), click **Refresh Table** to trigger ingestion. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Governing Access with ABAC Policies

To govern access based on SAP PersonalData tags, create [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies that reference these tags in Unity Catalog. ABAC policies allow you to control access to sensitive data by evaluating the tags assigned to tables and columns. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Viewing Tags

SAP PersonalData governance tags are visible in several places within Databricks:

- **Catalog Explorer**: View tags in the table and column details. You can filter columns by searching for the contents of their comments.
- **SQL**: Query `INFORMATION_SCHEMA.TABLE_TAGS` to view SAP governance tags assigned to tables and columns.
- **Audit Logs**: Metadata sync events, including tag assignments, comment updates, and constraint changes, are recorded in audit logs. Use audit logs to track when SAP BDC metadata was ingested or updated in your catalog.

^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Specifications

For more information about SAP personal data annotations and the specific tag values that may be synced, see the SAP CSN Interop specification and its extensions for personal data schema definitions. The specification defines the schema for personal data classification annotations used by SAP BDC. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Related Concepts

- SAP Business Data Cloud (BDC) — The source system for semantic metadata
- Unity Catalog Tags — System governed tags and their management
- System Governed Tags — Tags automatically assigned by the Databricks system
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Policy framework that can reference these tags
- Delta Sharing with SAP BDC — The sharing mechanism for mounting SAP data
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for viewing tags and metadata
- SAP CSN Interop Specification — Specification defining personal data annotations

## Sources

- sap-bdc-semantic-metadata-databricks-on-aws.md

# Citations

1. [sap-bdc-semantic-metadata-databricks-on-aws.md](/references/sap-bdc-semantic-metadata-databricks-on-aws-325246e0.md)
