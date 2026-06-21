---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8d153dab9f06f30b40be8901d4a3b719be6324ba53e16783a393638a37c0936
  pageDirectory: concepts
  sources:
    - sap-bdc-semantic-metadata-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-system-governed-tags
    - UCSGT
    - Unity Catalog governed tags
    - Unity Catalog system tags
  citations:
    - file: sap-bdc-semantic-metadata-databricks-on-aws.md
title: Unity Catalog System Governed Tags
description: System-reserved tags (in the sap.* namespace) that are automatically assigned by the Databricks system and must not be manually created, modified, or deleted by users.
tags:
  - unity-catalog
  - tagging
  - governance
timestamp: "2026-06-19T20:18:09.875Z"
---

# Unity Catalog System Governed Tags

**Unity Catalog System Governed Tags** are metadata tags automatically assigned and maintained by Databricks system processes on Unity Catalog securable objects. Unlike user-managed tags, system governed tags are read-only and cannot be manually created, modified, or deleted by users.

## Overview

System governed tags are applied automatically by Databricks to provide metadata about data assets without requiring manual user intervention. These tags serve as a foundation for governance workflows, particularly [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies, which can reference system governed tags to dynamically control access to data. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Characteristics

System governed tags have the following key properties:

- **Read-only**: Users cannot manually assign, modify, or delete system governed tags. Attempting to do so may result in the tags being cleared or removed by the Databricks system later. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]
- **Automatic synchronization**: Tags are automatically ingested and updated when data from integrated sources (such as SAP BDC) is mounted or accessed. Changes made in the source system are reflected in Unity Catalog. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]
- **System-reserved namespaces**: Tags in certain namespaces (such as `sap.*`) are reserved for system use. Users should not manually assign tags in these namespaces. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## SAP `sap.PersonalData` Namespace

A prominent example of system governed tags comes from SAP Business Data Cloud (BDC) integration. SAP BDC syncs governance tags in the `sap.PersonalData` namespace as system governed tags on tables in Unity Catalog. These tags classify whether SAP BDC data contains personal or sensitive information. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

The following tags are synced from SAP BDC:

- Tags in the `sap.PersonalData` namespace, as defined by the SAP CSN Interop specification for personal data annotations.

^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Governance Use Cases

### Attribute-Based Access Control (ABAC)

System governed tags can be referenced in ABAC policies to control access to sensitive data. For example, you can create ABAC policies that check for specific `sap.PersonalData` tags to restrict which users or groups can access tables containing personal information. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Audit Logging

Metadata sync events, including tag assignments and updates, are recorded in Audit Logs. This allows administrators to track when SAP BDC metadata was ingested or updated in a catalog. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

### Querying Tags in SQL

You can query system governed tags using SQL. For example, query `INFORMATION_SCHEMA.TABLE_TAGS` to view SAP governance tags assigned to tables. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Best Practices

- **Do not manually assign system-reserved tags**: Tags in namespaces like `sap.*` are automatically managed by Databricks. Manual assignment may lead to inconsistency or removal by the system. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]
- **Use ABAC policies for governance**: Rather than modifying system governed tags, create ABAC policies that reference them to control access based on automatically-synced metadata. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]
- **Refresh metadata as needed**: If you don't see the latest tags in Catalog Explorer, use the **Refresh Table** option to trigger metadata ingestion. ^[sap-bdc-semantic-metadata-databricks-on-aws.md]

## Comparison: System Governed Tags vs. User-Managed Tags

| Feature | System Governed Tags | User-Managed Tags |
|---------|---------------------|-------------------|
| Assignment | Automatic by Databricks | Manual by users |
| Modification | Read-only | Editable by authorized users |
| Lifecycle | Managed by system processes | Managed by users |
| Namespaces | System-reserved (e.g., `sap.*`) | User-defined namespaces |

## Related Concepts

- Unity Catalog Tags — General tagging framework for Unity Catalog securable objects
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Access control policies that can reference system governed tags
- [SAP Business Data Cloud (BDC) integration](/concepts/sap-business-data-cloud-bdc-connector.md) — Source of SAP system governed tags
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for viewing tags on tables and columns
- Audit Logs — Record of metadata sync events including tag assignments

## Sources

- sap-bdc-semantic-metadata-databricks-on-aws.md

# Citations

1. [sap-bdc-semantic-metadata-databricks-on-aws.md](/references/sap-bdc-semantic-metadata-databricks-on-aws-325246e0.md)
