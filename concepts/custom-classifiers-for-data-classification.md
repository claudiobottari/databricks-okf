---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 871247b2aefc5a1dd61b7a1a2808c818f8a24217e2d9c44f0185a244ec19edda
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifiers-for-data-classification
    - CCFDC
    - Custom Classifier|Custom Classifier
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifiers for Data Classification
description: User-defined classifiers that extend Databricks' built-in data classification system to detect organization-specific sensitive data types such as internal employee IDs, proprietary product codes, or partner account numbers.
tags:
  - data-governance
  - unity-catalog
  - classification
timestamp: "2026-06-18T11:25:19.259Z"
---

# Custom Classifiers for Data Classification

**Custom classifiers** extend the [Data Classification](/concepts/data-classification.md) system in [Unity Catalog](/concepts/unity-catalog.md) so you can detect sensitive data that is specific to your organization — for example, internal employee IDs, proprietary product codes, vendor identifiers, or partner account numbers. ^[custom-classifiers-databricks-on-aws.md]

To create a custom classifier, you select a [governed tag](/concepts/governed-tags.md) and provide example columns that contain representative values for the class. Data Classification then detects this class during its regular scans. ^[custom-classifiers-databricks-on-aws.md]

Using custom classifiers, you can:

- **Tag organization-specific data** — detect and configure auto-tagging for data types unique to your organization.
- **Extend governance controls** — apply [ABAC column-level masks](/concepts/abac-column-level-mask-unity-catalog.md) to sensitive data that the classifier discovers. ^[custom-classifiers-databricks-on-aws.md]

## Encryption at Rest

Custom classifier configuration and the detection metadata that Databricks generates from your example columns are encrypted at rest. You can use a customer-managed key (CMK) on your system catalog to manage the encryption key. Configuring a CMK on the system catalog encrypts all data in the system catalog, not just custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

## Requirements

| Requirement | Detail |
|-------------|--------|
| Data Classification enabled | Must be enabled on at least one catalog in the [Metastore](/concepts/metastore.md). |
| Compute | Workspace must have [serverless compute](/concepts/serverless-gpu-compute.md) available (enabled by default in workspaces with Unity Catalog). |
| [Metastore](/concepts/metastore.md) admin | To create, edit, or delete a custom classifier. |
| Tag assignment permission | `ASSIGN` privileges on the governed tag the classifier uses. |
| Column selection permission | `SELECT` on the table that contains the example column. |

^[custom-classifiers-databricks-on-aws.md]

## Create a Custom Classifier

1. From the Data Classification results page, click **Manage custom classifiers**.
2. In the side panel, click **Create custom classifier**.
3. **Select a tag**. Choose an existing governed tag, or click **Create new tag** to define one inline. If the tag has allowed values, choose the specific value you want to detect.
4. **Select example columns**. Browse the catalog tree and select columns that contain representative values for the class. Choose columns whose values are typical — broader and more varied examples produce more accurate detection rules.
5. Click **Create**.

Detections from the custom classifier typically appear on the results page within a few hours. ^[custom-classifiers-databricks-on-aws.md]

A custom classifier applies to **all** catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled. Per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]

## Manage Custom Classifiers

The **Manage custom classifiers** side panel lists all custom classifiers configured for the [Metastore](/concepts/metastore.md). From this panel you can search by tag name, edit the example columns of an existing classifier, or delete a classifier. ^[custom-classifiers-databricks-on-aws.md]

### Edit a Custom Classifier

1. In the **Manage custom classifiers** side panel, select the custom classifier.
2. Click **Edit** next to the example columns list.
3. Add or remove columns (the example column limit still applies).
4. Click **Save**.

Updates take effect within a few hours. Existing detections from the previous configuration remain in place. The governed tag and tag value cannot be changed after creation. To switch to a different tag, delete the classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]

### Delete a Custom Classifier

1. Select the custom classifier in the side panel.
2. Click **Delete**.
3. Confirm the deletion.

When you delete a custom classifier:

- No new detections are produced.
- Existing detections are removed from the Data Classification results page.
- Tags that were already auto-applied to columns are **not** removed automatically. ^[custom-classifiers-databricks-on-aws.md]

### Suspended Custom Classifiers

If rule generation or validation fails, Databricks suspends the custom classifier and shows a warning on the Data Classification results page. A suspended classifier produces no new detections.

Common causes include:

- Example columns reference tables that have been deleted or renamed.
- The example columns are not representative enough.
- The governed tag (or its value) is no longer valid.

To resolve, edit the custom classifier with a different set of example columns. If the suspension is caused by an invalid tag, delete the classifier and create a new one with a valid tag. ^[custom-classifiers-databricks-on-aws.md]

## View Custom Classifier Detections

To view custom classifier detections, follow the same steps as for built-in classifications. See [View classification results](/concepts/classification-results-ui.md). ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- Maximum **50 custom classifiers per metastore**.
- Each classifier must reference **between 1 and 10 example columns**.
- Governed tag naming is subject to Tag Policy rules.
- Custom classifiers apply to **all** Data Classification-enabled catalogs in the [Metastore](/concepts/metastore.md). Per-catalog or per-schema scoping is not supported.
- The governed tag cannot be changed after creation. To use a different tag, delete and recreate.
- New and updated classifiers apply only to **subsequent** Data Classification scans. Existing scan results are not automatically reclassified.
- All [Data Classification limitations](/concepts/data-classification.md) apply to custom classifiers as well, including supported table types. ^[custom-classifiers-databricks-on-aws.md]

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|--------------|------------|
| Classifier is suspended | Example columns reference deleted/renamed tables; insufficiently representative examples; invalid governed tag. | Edit classifier with better columns; or delete and recreate with a valid tag. |
| Permission denied when creating or listing | Not a [Metastore](/concepts/metastore.md) admin, or missing `ASSIGN` on the governed tag. | Verify [Metastore](/concepts/metastore.md) admin role and tag permissions. |
| Cannot select an example column | Missing `SELECT` on the table. | Ask the table owner to grant `SELECT`, or choose a different column. |

^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The built-in system that custom classifiers extend.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where classification runs.
- [Governed Tags](/concepts/governed-tags.md) — The tags used to label sensitive data.
- [ABAC column-level masks](/concepts/abac-column-level-mask-unity-catalog.md) — Access control policies that can be driven by classifier-detected tags.
- [Serverless compute](/concepts/serverless-gpu-compute.md) — Required compute for classifier operations.
- [Customer-managed key (CMK)](/concepts/customer-managed-keys-cmk-for-online-feature-stores.md) — Encryption key management for system catalog data.
- System table reference: data classification — Reference for querying classification metadata.

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
