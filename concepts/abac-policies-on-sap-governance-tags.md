---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44061fd78423d6c4f00ef64857720836a6bb9ddf79762c3cc6560c2a3ce42780
  pageDirectory: concepts
  sources:
    - sap-bdc-semantic-metadata-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - abac-policies-on-sap-governance-tags
    - APOSGT
  citations:
    - file: sap-bdc-semantic-metadata-databricks-on-aws.md
title: ABAC Policies on SAP Governance Tags
description: Using attribute-based access control (ABAC) policies in Unity Catalog that reference SAP system-governed tags to control access to sensitive SAP BDC data.
tags:
  - access-control
  - data-governance
  - unity-catalog
  - sap
  - security
timestamp: "2026-06-19T20:18:11.692Z"
---

# ABAC Policies on SAP Governance Tags

**ABAC Policies on SAP Governance Tags** refers to the use of attribute-based access control (ABAC) policies in Unity Catalog that reference governance tags synced from SAP Business Data Cloud (BDC). These policies enable fine-grained access control to sensitive SAP data based on automatically assigned personal data classifications. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Overview

When SAP BDC shares are mounted to Unity Catalog, SAP BDC syncs governance tags in the `sap.PersonalData` namespace as [system governed tags](/concepts/governed-tags.md) on tables in Unity Catalog. These tags classify whether SAP BDC data contains personal or sensitive information. Users can then create ABAC policies that reference these tags to control access to sensitive data. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Important Restrictions

Tags in the `sap.*` namespace are system-reserved values that are automatically assigned by the Databricks system when SAP BDC shares are mounted. Do not manually assign, modify, or delete these tags, as Databricks might clear or remove them later if they are assigned manually. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Creating ABAC Policies

To govern access based on SAP governance tags, create ABAC policies that reference the synced tags from the `sap.PersonalData` namespace. For example, you can restrict access to tables or columns that contain personal data by writing a policy rule that checks for the presence of a specific SAP governance tag. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

For more details on how to write ABAC policies in Unity Catalog, see the documentation on [attribute-based access control in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md). ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Querying SAP Governance Tags

You can query `INFORMATION_SCHEMA.TABLE_TAGS` to view SAP governance tags that have been synced to your catalog. This is useful for understanding which tags are available for use in ABAC policies. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Additional Resources

- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md) for creating and managing connections
- [System governed tags](/concepts/governed-tags-and-system-tags.md) for understanding tag management in Unity Catalog
- [Attribute-based access control in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md) for detailed policy authoring
- Audit and monitor data sharing for tracking metadata sync events

## Sources

- sap-bdc-semantic-metadata-databricks-on-aws.md

# Citations

1. [sap-bdc-semantic-metadata-databricks-on-aws.md](/references/sap-bdc-semantic-metadata-databricks-on-aws-325246e0.md)
