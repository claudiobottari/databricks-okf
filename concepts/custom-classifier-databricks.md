---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 384950753203528b771fd7e0e0b9162c43dd08eb07f1ee7e33c875378ae9802a
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifier-databricks
    - CC(
    - custom-classifiers-databricks-on-aws.md
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifier (Databricks)
description: User-defined classifier that extends Databricks Data Classification to detect organization-specific sensitive data using governed tags and example columns.
tags:
  - data-governance
  - unity-catalog
  - classification
timestamp: "2026-06-19T18:02:54.245Z"
---

# Custom Classifier (Databricks)

A **custom classifier** in Databricks Data Classification allows you to detect sensitive data that is specific to your organization, such as internal employee IDs, proprietary product codes, vendor identifiers, or partner account numbers. Custom classifiers extend the [built-in classification system](/concepts/data-classification.md) in [Unity Catalog](/concepts/unity-catalog.md) by letting you define detection rules based on your own examples. ^[custom-classifiers-databricks-on-aws.md]

To create a custom classifier, you select a [governed tag](/concepts/governed-tags.md) and provide example columns that contain representative values for the class. Data Classification then detects this class during its regular scans. ^[custom-classifiers-databricks-on-aws.md]

Using custom classifiers, you can tag organization-specific data – such as employee IDs, partner codes, or internal account numbers – and configure auto-tagging for those data types. You can also extend governance controls by applying [ABAC column-level masks](/concepts/abac-column-level-mask-unity-catalog.md) to the sensitive data. ^[custom-classifiers-databricks-on-aws.md]

Custom classifier configuration and the detection metadata generated from your example columns are encrypted at rest. You can use a Customer-Managed Key (CMK) on your system catalog to manage the encryption key; configuring a CMK on the system catalog encrypts all data in the system catalog, not just custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

## Requirements

To use custom classifiers, the following prerequisites must be met:

- Data Classification must be enabled on at least one catalog in the [Metastore](/concepts/metastore.md).
- Your workspace must have Serverless Compute available (enabled by default in workspaces with Unity Catalog).
- To create, edit, or delete a custom classifier, you must be a [Metastore](/concepts/metastore.md) admin.
- To create or edit a custom classifier, you must have `ASSIGN` privileges on the governed tag the classifier uses.
- To select a column for the classifier, you must have `SELECT` on the table that contains it.

^[custom-classifiers-databricks-on-aws.md]

## Create a Custom Classifier

1. From the Data Classification results page, click **Manage custom classifiers**.
2. In the **Manage custom classifiers** side panel, click **Create custom classifier**.
3. **Select a tag**. Choose an existing governed tag, or click **Create new tag** to define one inline. If the tag has allowed values, choose the specific value you want to detect.
4. **Select example columns**. Browse the catalog tree and select columns that contain representative values for the class. Choose columns whose values are typical of what you want detected – broader and more varied examples produce more accurate detection rules.
5. Click **Create**.

^[custom-classifiers-databricks-on-aws.md]

Detections from the custom classifier typically appear on the results page within a few hours. ^[custom-classifiers-databricks-on-aws.md]

A custom classifier applies to **all** catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled. Per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]

## Manage Custom Classifiers

The **Manage custom classifiers** side panel lists all custom classifiers configured for the [Metastore](/concepts/metastore.md). From this panel, you can search by tag name, edit the example columns of an existing classifier, or delete a classifier. ^[custom-classifiers-databricks-on-aws.md]

### Edit a Custom Classifier

To update the example columns for an existing custom classifier:

1. In the **Manage custom classifiers** side panel, select the custom classifier you want to edit.
2. Click **Edit** next to the example columns list.
3. Add or remove columns. The example column limit still applies.
4. Click **Save**.

Updates take effect within a few hours. Existing detections from the previous configuration remain in place. ^[custom-classifiers-databricks-on-aws.md]

The governed tag and tag value cannot be changed after a custom classifier is created. To switch to a different tag, delete the custom classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]

### Delete a Custom Classifier

1. In the **Manage custom classifiers** side panel, select the custom classifier you want to delete.
2. Click **Delete**.
3. Confirm the deletion.
4. Confirm that the classifier is removed from the **Manage custom classifiers** side panel.

When you delete a custom classifier: no new detections are produced for that classifier; existing detections are removed from the Data Classification results page; tags that were already auto-applied to columns are **not** removed automatically. ^[custom-classifiers-databricks-on-aws.md]

### Suspended Custom Classifiers

If rule generation or validation fails, Databricks suspends the custom classifier and shows a warning on the Data Classification results page. A suspended custom classifier produces no new detections. ^[custom-classifiers-databricks-on-aws.md]

To resolve a suspension, edit the custom classifier and replace example columns that are inaccessible or not representative enough. If the governed tag or tag value is no longer valid, delete the custom classifier and create a new one with a valid tag. ^[custom-classifiers-databricks-on-aws.md]

## View Custom Classifier Detections

To view custom classifier detections, follow the same steps as for built-in classifications. See [Data Classification#View Classification Results|View classification results](/concepts/data-classification-results-page.md). ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- You can create a maximum of **50 custom classifiers per metastore**.
- Each custom classifier must reference between **1 and 10 example columns** to provide sufficient data for classification.
- Governed tag naming is subject to Tag Policy rules.
- Custom classifiers apply to all Data Classification-enabled catalogs in the [Metastore](/concepts/metastore.md). Per-catalog or per-schema scoping is not supported.
- The governed tag used by a custom classifier cannot be changed after creation. To use a different tag, delete and recreate the custom classifier.
- New and updated custom classifiers apply only to subsequent Data Classification scans. Existing scan results are not automatically reclassified, so detections for previously scanned data appear after the next scan completes.
- All [Data Classification#Limitations|Data Classification limitations](/concepts/data-classification-databricks.md) apply to custom classifiers as well, including supported table types.

^[custom-classifiers-databricks-on-aws.md]

## Troubleshooting

**A custom classifier is suspended.** Common causes include: one or more example columns reference tables that have been deleted or renamed; the example columns are not representative enough; or the governed tag is no longer valid. To resolve, edit the classifier with a different set of example columns, or delete and recreate with a valid tag. ^[custom-classifiers-databricks-on-aws.md]

**Permission denied when creating or listing custom classifiers.** You must be a [Metastore](/concepts/metastore.md) admin. Creating or editing additionally requires `ASSIGN` privileges on the governed tag. ^[custom-classifiers-databricks-on-aws.md]

**Cannot select an example column.** You must have `SELECT` on the table that contains the column. Ask the table owner to grant it, or choose a different column. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) – The built‑in classification system that custom classifiers extend.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance platform under which custom classifiers operate.
- [Governed Tags](/concepts/governed-tags.md) – The tag mechanism used to label detected sensitive data.
- [ABAC](/concepts/abac-attribute-based-access-control.md) – Attribute‑based access control that can use custom classifier tags for column‑level masks.
- Customer-Managed Key (CMK) – Encryption key management for the system catalog containing classifier metadata.
- Supported Classification Tags – The list of built‑in tags that can be augmented with custom classifiers.

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
