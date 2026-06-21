---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 429dd85e355c8b22a0af059de88d0b1c9aebdc3a41ab09f1eee6290dd81cc62c
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifier-databricks-unity-catalog
    - CC(UC
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifier (Databricks Unity Catalog)
description: A custom classifier extends Databricks' built-in data classification system to detect organization-specific sensitive data (e.g., employee IDs, product codes) by associating a governed tag with example columns.
tags:
  - data-governance
  - unity-catalog
  - classification
timestamp: "2026-06-19T14:39:52.489Z"
---

# Custom Classifier (Databricks Unity Catalog)

**Custom Classifier (Databricks Unity Catalog)** extends the built-in Data Classification system in Unity Catalog. Custom classifiers enable you to detect sensitive data that is specific to your organization — such as internal employee IDs, proprietary product codes, vendor identifiers, or partner account numbers — by providing example columns that contain representative values for the class. ^[custom-classifiers-databricks-on-aws.md]

## How Custom Classifiers Work

To create a custom classifier, you select a [governed tag](/concepts/governed-tags.md) and provide example columns from your tables that contain representative values for the class you want to detect. Data Classification uses these examples to learn the pattern and detect the class during its regular scans. ^[custom-classifiers-databricks-on-aws.md]

Using custom classifiers, you can:
- **Tag organization-specific data**: Detect and configure auto-tagging for data types unique to your organization, such as employee IDs, partner codes, or internal account numbers.
- **Extend governance controls**: Apply [ABAC column-level masks](/concepts/abac-column-level-mask-unity-catalog.md) to sensitive data.

**Note**: Custom classifier configuration and the detection metadata that Databricks generates from your example columns are encrypted at rest. You can use a customer-managed key (CMK) on your system catalog to manage the encryption key. Configuring a CMK on the system catalog encrypts all data in the system catalog, not just custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

## Requirements

- Data Classification must be enabled on at least one catalog in the [Metastore](/concepts/metastore.md). See [Use data classification](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification#use-data-classification).
- Your workspace must have [serverless compute](/concepts/serverless-gpu-compute.md) available (enabled by default in workspaces with Unity Catalog).
- To create, edit, or delete a custom classifier, you must be a **metastore admin**.
- To create or edit a custom classifier, you must have `ASSIGN` privileges on the governed tag the classifier uses. See [Manage permissions on governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/manage-permissions).
- To select a column for the classifier, you must have `SELECT` on the table that contains it.

## Creating a Custom Classifier

### Step-by-Step Creation

1. From the **Data Classification results** page, click **Manage custom classifiers**.
2. In the **Manage custom classifiers** side panel, click **Create custom classifier**.
3. **Select a tag**: Choose an existing governed tag, or click **Create new tag** to define one inline. If the tag has allowed values, choose the specific value you want to detect.
4. **Select example columns**: Browse the catalog tree and select columns that contain representative values for the class. Broader and more varied examples produce more accurate detection rules.
5. Click **Create**.

Detections from the custom classifier typically appear on the results page within a few hours. ^[custom-classifiers-databricks-on-aws.md]

### Important Notes on Scope

A custom classifier applies to **all** catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled. Per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]

## Managing Custom Classifiers

The **Manage custom classifiers** side panel lists all custom classifiers configured for the [Metastore](/concepts/metastore.md). From this panel, you can search by tag name, edit the example columns of an existing classifier, or delete a classifier. ^[custom-classifiers-databricks-on-aws.md]

### Editing a Custom Classifier

1. In the **Manage custom classifiers** side panel, select the custom classifier you want to edit.
2. Click **Edit** next to the example columns list.
3. Add or remove columns (the example column limit still applies — between 1 and 10).
4. Click **Save**.

Updates take effect within a few hours. Existing detections from the previous configuration remain in place. ^[custom-classifiers-databricks-on-aws.md]

**Important**: The governed tag and tag value cannot be changed after a custom classifier is created. To switch to a different tag, delete the custom classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]

### Deleting a Custom Classifier

1. In the **Manage custom classifiers** side panel, select the custom classifier you want to delete.
2. Click **Delete**.
3. Confirm the deletion.

When you delete a custom classifier:
- No new detections are produced for that classifier.
- Existing detections are removed from the Data Classification results page.
- Tags that were already auto-applied to columns are **not** removed automatically.

### Suspended Custom Classifiers

If rule generation or validation fails, Databricks suspends the custom classifier and shows a warning on the Data Classification results page. A suspended custom classifier produces no new detections. ^[custom-classifiers-databricks-on-aws.md]

Common causes for suspension include:
- One or more example columns reference tables that have been deleted or renamed since the classifier was created.
- The example columns are not representative enough for the system to learn a stable detection.
- The governed tag is no longer a governed tag, or the tag value is no longer valid.

To resolve a suspension:
- Edit the custom classifier and replace example columns that are inaccessible or not representative enough.
- If the governed tag or tag value is no longer valid, delete the custom classifier and create a new one with a valid tag.

## Viewing Custom Classifier Detections

To view custom classifier detections, follow the same steps as for built-in classifications. See [View classification results](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification#view-classification-results). ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- **Maximum**: You can create a maximum of **50** custom classifiers per [Metastore](/concepts/metastore.md).
- **Example columns**: Each custom classifier must reference between **1 and 10** example columns to provide sufficient data for classification.
- **Scope**: Custom classifiers apply to all Data Classification-enabled catalogs in the [Metastore](/concepts/metastore.md). Per-catalog or per-schema scoping is not supported.
- **Tag immutability**: The governed tag used by a custom classifier cannot be changed after creation. To use a different tag, delete and recreate the custom classifier.
- **Scan timing**: New and updated custom classifiers apply only to subsequent Data Classification scans. Existing scan results are not automatically reclassified, so detections for previously scanned data appear after the next scan completes.
- **All Data Classification limitations** apply to custom classifiers as well, including supported table types. See [Limitations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification#limitations).

## Troubleshooting

### Permission Denied When Creating or Listing Custom Classifiers

You must be a [Metastore](/concepts/metastore.md) admin. Creating or editing a custom classifier additionally requires `ASSIGN` privileges on the governed tag. ^[custom-classifiers-databricks-on-aws.md]

### Cannot Select an Example Column

You must have `SELECT` on the table that contains the column. If you do not have `SELECT` on the table, ask the table owner to grant it, or choose a different example column. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The built-in system for detecting sensitive data
- [Governed Tags](/concepts/governed-tags.md) — The tag system that custom classifiers use
- [ABAC](/concepts/abac-attribute-based-access-control.md) — Attribute-based access control for column-level masking
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform for Databricks
- System Catalog — The catalog that stores system metadata

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
