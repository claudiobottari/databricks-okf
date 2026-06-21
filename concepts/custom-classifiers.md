---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b74767b6fb9386962882ed2708e6315a918db96d18f55b9c252c93e4a549216
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifiers
    - Custom Classifier
    - custom classifier
    - custom-classifiers-for-data-classification
    - CCFDC
    - Custom Classifier|Custom Classifier
    - custom-classifiers-for-databricks-data-classification
    - CCFDDC
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifiers
description: User-defined classifiers that extend Databricks' built-in data classification to detect organization-specific sensitive data types like internal employee IDs, proprietary product codes, and partner account numbers.
tags:
  - data-governance
  - unity-catalog
  - classification
timestamp: "2026-06-19T09:38:52.493Z"
---

# Custom Classifiers

**Custom classifiers** extend Databricks' built-in [Data Classification] system in [Unity Catalog] to detect sensitive data that is specific to an organization, such as internal employee IDs, proprietary product codes, vendor identifiers, or partner account numbers. ^[custom-classifiers-databricks-on-aws.md]

## Overview

To create a custom classifier, a [Metastore](/concepts/metastore.md) admin selects a [governed tag] and provides example columns that contain representative values for the class. Data Classification then detects this class during its regular scans. ^[custom-classifiers-databricks-on-aws.md]

Custom classifiers serve two main purposes:

- **Tag organization-specific data**: Detect and configure auto-tagging for data types unique to an organization, such as employee IDs, partner codes, or internal account numbers.
- **Extend governance controls**: Apply [ABAC column-level masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts#policy-types) to sensitive data detected by custom classifiers. ^[custom-classifiers-databricks-on-aws.md]

### Encryption

Custom classifier configuration and the detection metadata that Databricks generates from example columns are encrypted at rest. A customer-managed key (CMK) on the system catalog can be used to manage the encryption key. Configuring a CMK on the system catalog encrypts all data in the system catalog, not just custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

## Requirements

To create, edit, or delete custom classifiers, the following prerequisites must be met: ^[custom-classifiers-databricks-on-aws.md]

- Data Classification must be enabled on at least one catalog in the [Metastore](/concepts/metastore.md).
- The workspace must have serverless compute available (enabled by default in workspaces with Unity Catalog).
- To create, edit, or delete a custom classifier, you must be a **metastore admin**.
- To create or edit a custom classifier, you must have `ASSIGN` privileges on the governed tag the classifier uses.
- To select a column for the classifier, you must have `SELECT` on the table that contains it.

## Create a Custom Classifier

Custom classifiers are created through the Data Classification results page in Catalog Explorer: ^[custom-classifiers-databricks-on-aws.md]

1. From the **Data Classification results page**, click **Manage custom classifiers**.
2. In the **Manage custom classifiers** side panel, click **Create custom classifier**.
3. **Select a tag**: Choose an existing governed tag, or click **Create new tag** to define one inline. If the tag has allowed values, choose the specific value to detect.
4. **Select example columns**: Browse the catalog tree and select between 1 and 10 columns that contain representative values for the class. Broader and more varied examples produce more accurate detection rules.
5. Click **Create**.

Detections from the custom classifier typically appear on the results page within a few hours. ^[custom-classifiers-databricks-on-aws.md]

A custom classifier applies to **all** catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled. Per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]

## Manage Custom Classifiers

The **Manage custom classifiers** side panel lists all custom classifiers configured for the [Metastore](/concepts/metastore.md). From this panel, you can search by tag name, edit example columns, or delete a classifier. ^[custom-classifiers-databricks-on-aws.md]

### Edit a Custom Classifier

To update the example columns: ^[custom-classifiers-databricks-on-aws.md]

1. In the **Manage custom classifiers** side panel, select the classifier to edit.
2. Click **Edit** next to the example columns list.
3. Add or remove columns (the limit of 1–10 columns still applies).
4. Click **Save**.

Updates take effect within a few hours. Existing detections from the previous configuration remain in place. The governed tag and tag value **cannot be changed** after creation. To switch to a different tag, delete the custom classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]

### Delete a Custom Classifier

1. In the **Manage custom classifiers** side panel, select the classifier to delete.
2. Click **Delete** and confirm.

When a custom classifier is deleted: ^[custom-classifiers-databricks-on-aws.md]

- No new detections are produced.
- Existing detections are removed from the Data Classification results page.
- Tags that were already auto-applied to columns **are not** removed automatically.

### Suspended Custom Classifiers

If rule generation or validation fails, Databricks suspends the custom classifier and shows a warning on the Data Classification results page. A suspended classifier produces no new detections. ^[custom-classifiers-databricks-on-aws.md]

Common causes of suspension include: ^[custom-classifiers-databricks-on-aws.md]

- Example columns reference tables that have been deleted or renamed since creation.
- Example columns are not representative enough for stable detection.
- The governed tag is no longer a governed tag, or the tag value is no longer valid.

To resolve a suspension, edit the custom classifier with a different set of example columns and wait for the next scan. If the suspension is caused by an invalid tag, delete and recreate the classifier. ^[custom-classifiers-databricks-on-aws.md]

## View Custom Classifier Detections

Custom classifier detections are viewed the same way as built-in classifications. See the Data Classification documentation for viewing classification results. ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- Maximum of **50 custom classifiers** per [Metastore](/concepts/metastore.md). ^[custom-classifiers-databricks-on-aws.md]
- Each classifier must reference **between 1 and 10 example columns**. ^[custom-classifiers-databricks-on-aws.md]
- Governed tag naming is subject to Tag Policy rules. ^[custom-classifiers-databricks-on-aws.md]
- Custom classifiers apply to all Data Classification-enabled catalogs in the [Metastore](/concepts/metastore.md); per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]
- The governed tag used by a custom classifier cannot be changed after creation. To use a different tag, delete and recreate. ^[custom-classifiers-databricks-on-aws.md]
- New and updated custom classifiers apply only to subsequent Data Classification scans. Existing scan results are not automatically reclassified. ^[custom-classifiers-databricks-on-aws.md]
- All Data Classification limitations apply to custom classifiers, including supported table types. ^[custom-classifiers-databricks-on-aws.md]

## Troubleshooting

### Permission Denied When Creating or Listing Custom Classifiers

You must be a [Metastore](/concepts/metastore.md) admin. Creating or editing additionally requires `ASSIGN` privileges on the governed tag. ^[custom-classifiers-databricks-on-aws.md]

### Cannot Select an Example Column

You must have `SELECT` on the table that contains the column. If you lack this permission, ask the table owner to grant it or choose a different example column. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md)
- System Tables

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
