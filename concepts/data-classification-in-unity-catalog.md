---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f13c67e130d56af3cafff01d56d341646534e9cb6ff8d92d9e7b11d7096e22d8
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
    - get-started-with-unity-catalog-databricks-on-aws.md
    - what-is-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - data-classification-in-unity-catalog
    - DCIUC
  citations:
    - file: custom-classifiers-databricks-on-aws.md
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: Data Classification in Unity Catalog
description: The broader Databricks data classification system that automatically scans tables across catalogs to detect sensitive data using built-in and custom classifiers.
tags:
  - data-governance
  - unity-catalog
  - security
timestamp: "2026-06-19T09:39:45.928Z"
---

# Data Classification in Unity Catalog

**Data Classification in Unity Catalog** is an automated governance capability that uses an AI agent to scan tables in your [Unity Catalog](/concepts/unity-catalog.md) and tag columns containing sensitive data, such as personally identifiable information (PII), financial data, and credentials. The resulting tags can then be consumed by [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies to dynamically enforce masking or filtering based on what the data actually contains. ^[custom-classifiers-databricks-on-aws.md, get-started-with-unity-catalog-databricks-on-aws.md]

## How It Works

Data Classification runs as a background scan across catalogs that have the feature enabled. During each scan, the AI agent inspects column values and metadata, then automatically applies [Governed Tags](/concepts/governed-tags.md) to columns that match built-in classification rules. Scans are periodic; newly classified data appears on the Data Classification results page within a few hours after the scan completes. ^[custom-classifiers-databricks-on-aws.md]

The classification results are visible in [Catalog Explorer](/concepts/catalog-explorer.md) and through the Data Classification UI. You can view which columns have been tagged with which sensitivity markers at a glance. ^[custom-classifiers-databricks-on-aws.md]

## Custom Classifiers

The built-in classifier covers common sensitive data types, but you can extend it with **custom classifiers** to detect organization-specific classes (e.g., internal employee IDs, proprietary product codes, vendor identifiers). A custom classifier is created by selecting a governed tag and providing between 1 and 10 example columns that contain representative values. Databricks then learns detection rules from those examples and applies them in future scans. ^[custom-classifiers-databricks-on-aws.md]

Custom classifiers are managed by [Metastore](/concepts/metastore.md) admins and apply to all Data Classification–enabled catalogs in the [Metastore](/concepts/metastore.md). Per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]

For detailed instructions, see [Custom Classifiers](/concepts/custom-classifiers.md).

### Management

From the Data Classification results page, you can open the **Manage custom classifiers** side panel to create, edit, or delete custom classifiers. Editing changes the example columns; the governed tag and tag value cannot be changed after creation. A suspended classifier (caused by invalid examples or inaccessible tables) stops producing detections until resolved. ^[custom-classifiers-databricks-on-aws.md]

## Integration with ABAC

One of the primary benefits of Data Classification is its integration with [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md). Once columns are tagged, you can write ABAC column mask policies that automatically mask or redact sensitive values based on the tags applied by classification. This allows governance to follow the data rather than requiring manual per-table configuration. ^[get-started-with-unity-catalog-databricks-on-aws.md]

For example, a policy can state that any column tagged with `pii : email` must be masked for non‑privileged users. When Data Classification later discovers a new PII column, the policy takes effect automatically. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Encryption and Security

Custom classifier configuration and the detection metadata generated from your example columns are encrypted at rest. You can optionally manage the encryption key by configuring a Customer-Managed Key (CMK) on the System Catalog. This encrypts all data in the system catalog, including custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- You can create a maximum of 50 custom classifiers per [Metastore](/concepts/metastore.md). ^[custom-classifiers-databricks-on-aws.md]
- Each custom classifier must reference between 1 and 10 example columns. ^[custom-classifiers-databricks-on-aws.md]
- The governed tag used by a custom classifier cannot be changed after creation. ^[custom-classifiers-databricks-on-aws.md]
- New and updated custom classifiers apply only to subsequent scans; existing results are not reclassified until the next scan completes. ^[custom-classifiers-databricks-on-aws.md]
- Custom classifiers apply to all Data Classification–enabled catalogs; per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]
- All general Data Classification limitations (such as supported table types) also apply to custom classifiers. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer in which Data Classification operates.
- [Governed Tags](/concepts/governed-tags.md) — The tags that classification applies and ABAC policies consume.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Dynamic access policies that leverage classified tags.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) — A policy type that can mask classified columns.
- [Custom Classifiers](/concepts/custom-classifiers.md) — Extend classification to organization-specific data.
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for browsing classified assets.
- System Catalog — Contains metadata tables, including classification results.
- Customer-Managed Key (CMK) — Used to encrypt classification metadata.

## Sources

- custom-classifiers-databricks-on-aws.md
- get-started-with-unity-catalog-databricks-on-aws.md
- what-is-unity-catalog-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
2. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)
