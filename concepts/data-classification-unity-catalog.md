---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30775b27c0bffa43aee0d3b8f82ea45f6f1bb4a991d923a89c2543b6f1ca7697
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-classification-unity-catalog
    - DC(C
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Data Classification (Unity Catalog)
description: Built-in system in Databricks Unity Catalog that scans tables and automatically detects sensitive data using built-in and custom classifiers.
tags:
  - data-governance
  - unity-catalog
  - classification
timestamp: "2026-06-19T18:03:00.449Z"
---

# Data Classification (Unity Catalog)

**Data Classification** in Unity Catalog is a feature that automatically detects sensitive data in tables and columns. It uses a built-in classification system that can be extended with [Custom Classifiers](/concepts/custom-classifiers.md) to detect data types specific to an organization, such as internal employee IDs, proprietary product codes, or partner account numbers. Detected classifications can auto-apply [Governed Tags](/concepts/governed-tags.md) to columns, which can then be used for [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) column-level masks. ^[custom-classifiers-databricks-on-aws.md]

## Encryption

Configuration data and detection metadata generated from example columns for custom classifiers are encrypted at rest. You can use a Customer-Managed Key (CMK) on the System Catalog to manage the encryption key. Configuring a CMK on the system catalog encrypts all data in the system catalog, not just custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

## Requirements

- Data Classification must be enabled on at least one catalog in the [Metastore](/concepts/metastore.md). ^[custom-classifiers-databricks-on-aws.md]
- The workspace must have Serverless Compute available (enabled by default in workspaces with Unity Catalog). ^[custom-classifiers-databricks-on-aws.md]
- To create, edit, or delete a custom classifier, you must be a [Metastore](/concepts/metastore.md) admin. ^[custom-classifiers-databricks-on-aws.md]
- To create or edit a custom classifier, you must have `ASSIGN` privileges on the governed tag the classifier uses. ^[custom-classifiers-databricks-on-aws.md]
- To select a column for the classifier, you must have `SELECT` on the table that contains it. ^[custom-classifiers-databricks-on-aws.md]

## Custom Classifiers

Custom classifiers extend the built-in classification system so you can detect sensitive data that is unique to your organization. For full details, see the [Custom Classifiers](/concepts/custom-classifiers.md) page. ^[custom-classifiers-databricks-on-aws.md]

### Creating a Custom Classifier

1. From the Data Classification results page, click **Manage custom classifiers**.
2. In the side panel, click **Create custom classifier**.
3. **Select a tag**: Choose an existing governed tag, or click **Create new tag** to define one inline. If the tag has allowed values, choose the specific value you want to detect.
4. **Select example columns**: Browse the catalog tree and select columns that contain representative values for the class. Broader and more varied examples produce more accurate detection rules. Each classifier must reference between 1 and 10 example columns.
5. Click **Create**.

Detections from the custom classifier typically appear on the results page within a few hours. Custom classifiers apply to **all** catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled; per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]

### Managing Custom Classifiers

The **Manage custom classifiers** side panel lists all custom classifiers configured for the [Metastore](/concepts/metastore.md). From this panel, you can search by tag name, edit the example columns of an existing classifier, or delete a classifier. ^[custom-classifiers-databricks-on-aws.md]

When you edit a custom classifier, the governed tag and tag value cannot be changed after creation; to switch to a different tag, delete the classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]

When you delete a custom classifier:
- No new detections are produced for that classifier.
- Existing detections are removed from the Data Classification results page.
- Tags that were already auto-applied to columns are not removed automatically. ^[custom-classifiers-databricks-on-aws.md]

### Suspended Custom Classifiers

If rule generation or validation fails, Databricks suspends the custom classifier and shows a warning on the Data Classification results page. A suspended custom classifier produces no new detections. Common causes include:
- One or more example columns reference tables that have been deleted or renamed.
- The example columns are not representative enough for stable detection.
- The governed tag is no longer valid.

To resolve, edit the custom classifier with a different set of example columns and wait for the next scan. If the suspension is caused by an invalid governed tag or tag value, delete the classifier and create a new one with a valid tag. ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- Maximum of 50 custom classifiers per [Metastore](/concepts/metastore.md). ^[custom-classifiers-databricks-on-aws.md]
- Each custom classifier must reference between 1 and 10 example columns. ^[custom-classifiers-databricks-on-aws.md]
- Governed tag naming is subject to Tag Policy rules. ^[custom-classifiers-databricks-on-aws.md]
- Custom classifiers apply to all Data Classification-enabled catalogs in the [Metastore](/concepts/metastore.md); per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]
- The governed tag used by a custom classifier cannot be changed after creation. ^[custom-classifiers-databricks-on-aws.md]
- New and updated custom classifiers apply only to subsequent Data Classification scans; existing scan results are not automatically reclassified. ^[custom-classifiers-databricks-on-aws.md]
- All Data Classification limitations apply, including supported table types. ^[custom-classifiers-databricks-on-aws.md]

## Troubleshooting

- **Permission denied when creating or listing custom classifiers**: You must be a [Metastore](/concepts/metastore.md) admin. Creating or editing additionally requires `ASSIGN` privileges on the governed tag. ^[custom-classifiers-databricks-on-aws.md]
- **Cannot select an example column**: You must have `SELECT` on the table that contains the column. Ask the table owner to grant it, or choose a different column. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Custom Classifiers](/concepts/custom-classifiers.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- System Catalog
- Serverless Compute
- Customer-Managed Key (CMK)

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
