---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb50c86c322009474078caed6a8a7c632f618eba8abbad463840a2190bd55ed9
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - custom-classifier-lifecycle-management
    - CCLM
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifier Lifecycle Management
description: The process of creating, editing, deleting, and troubleshooting custom classifiers, including handling suspended classifiers and understanding detection timing.
tags:
  - lifecycle
  - management
  - operations
timestamp: "2026-06-19T09:39:05.624Z"
---

# Custom Classifier Lifecycle Management

**Custom Classifier Lifecycle Management** covers the full lifecycle of custom classifiers in Databricks [Data Classification](/concepts/data-classification.md): creation, editing, deletion, suspension, troubleshooting, and retirement. Custom classifiers extend the built-in classification system so that organizations can detect sensitive data types unique to their business, such as internal employee IDs, proprietary product codes, or partner account numbers. ^[custom-classifiers-databricks-on-aws.md]

## Prerequisites

Before creating or managing custom classifiers, the following requirements must be met:

- [Data Classification](/concepts/data-classification.md) must be enabled on at least one catalog in the [Metastore](/concepts/metastore.md).
- The workspace must have [serverless compute](/concepts/serverless-gpu-compute.md) available (enabled by default in workspaces with [Unity Catalog](/concepts/unity-catalog.md)).
- To create, edit, or delete a custom classifier, you must be a **metastore admin**.
- To create or edit a custom classifier, you must have `ASSIGN` privileges on the [governed tag](/concepts/governed-tags.md) the classifier uses.
- To select a column as an example for the classifier, you must have `SELECT` on the table that contains that column.

^[custom-classifiers-databricks-on-aws.md]

## Create a Custom Classifier

1. Navigate to the Data Classification results page and click **Manage custom classifiers**.
2. In the side panel, click **Create custom classifier**.
3. **Select a tag**: Choose an existing governed tag, or click **Create new tag** to define one inline. If the tag has allowed values, pick the specific value to detect.
4. **Select example columns**: Browse the catalog tree and choose columns that contain representative values for the class. Broader, more varied examples produce more accurate detection rules. You must select between 1 and 10 columns.
5. Click **Create**.

Detections from the new custom classifier typically appear on the results page within a few hours. The classifier applies to **all** catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled; per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]

## Manage Custom Classifiers

The **Manage custom classifiers** side panel lists all custom classifiers configured for the [Metastore](/concepts/metastore.md). From this panel you can search by tag name, edit example columns, or delete a classifier. ^[custom-classifiers-databricks-on-aws.md]

### Edit a Custom Classifier

To update the example columns:

1. Select the custom classifier in the side panel.
2. Click **Edit** next to the example columns list.
3. Add or remove columns (the limit of 1–10 still applies).
4. Click **Save**.

Updates take effect within a few hours. Existing detections from the previous configuration remain in place. The governed tag and tag value **cannot** be changed after creation. To switch to a different tag, delete the classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]

### Delete a Custom Classifier

1. Select the custom classifier in the side panel.
2. Click **Delete** and confirm.

After deletion:
- No new detections are produced for that classifier.
- Existing detections are removed from the Data Classification results page.
- Tags that were already auto-applied to columns are **not** automatically removed. ^[custom-classifiers-databricks-on-aws.md]

## Suspended Custom Classifiers

If rule generation or validation fails, Databricks suspends the custom classifier and shows a warning on the Data Classification results page. A suspended classifier produces no new detections. Common causes include:

- One or more example columns reference tables that have been deleted or renamed.
- The example columns are not representative enough for the system to learn a stable pattern.
- The governed tag is no longer valid, or the tag value is no longer valid.

To resolve a suspension, edit the custom classifier and replace example columns that are inaccessible or not representative. If the tag or value is invalid, delete the classifier and create a new one with a valid tag. ^[custom-classifiers-databricks-on-aws.md]

## View Custom Classifier Detections

To view detections produced by custom classifiers, follow the same steps as for built-in classifications. See [View classification results](/concepts/classification-results-ui.md) in the Data Classification documentation. ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- Maximum of **50 custom classifiers per metastore**.
- Each classifier must reference **between 1 and 10 example columns**.
- Governed tag naming is subject to Tag Policy rules.
- Custom classifiers apply to all Data Classification-enabled catalogs in the [Metastore](/concepts/metastore.md); per-catalog or per-schema scoping is not supported.
- The governed tag used by a custom classifier **cannot be changed after creation**. To use a different tag, delete and recreate the classifier.
- New and updated classifiers apply only to **subsequent** Data Classification scans. Existing scan results are not automatically reclassified; detections appear after the next scan completes.
- All Data Classification [limitations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification#limitations) (including supported table types) also apply to custom classifiers. ^[custom-classifiers-databricks-on-aws.md]

## Troubleshooting

### A custom classifier is suspended

Follow the guidance in [#Suspended Custom Classifiers](/concepts/suspended-custom-classifier.md). Ensure example columns still exist and are accessible, and that the governed tag and value are valid.

### Permission denied when creating or listing custom classifiers

Verify you are a [Metastore](/concepts/metastore.md) admin. Creating or editing additionally requires `ASSIGN` on the governed tag. See [#Prerequisites](/concepts/prerequisite-permission-validation.md).

### Cannot select an example column

You must have `SELECT` on the table containing the column. If you lack `SELECT`, ask the table owner to grant it, or choose a different example column. ^[custom-classifiers-databricks-on-aws.md]

## Encryption and Security

Custom classifier configuration and detection metadata generated from example columns are encrypted at rest. You can use a customer-managed key (CMK) on your system catalog to manage the encryption key. Configuring a CMK on the system catalog encrypts all data in the system catalog, not just custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
