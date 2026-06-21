---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d041eba81f132a47875098dd267e69ae88c92499a1ec1d679b8ecda0d3591a4
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - example-column-custom-classifier
    - EC(C
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Example Column (Custom Classifier)
description: A column selected from a Unity Catalog table that provides representative values for training a custom classifier's detection rules in Databricks Data Classification.
tags:
  - data-governance
  - classification
  - configuration
timestamp: "2026-06-19T18:03:22.859Z"
---

# Example Column (Custom Classifier)

**Example Column (Custom Classifier)** refers to a column in a Unity Catalog table that is selected as a sample of representative values when creating or editing a [Custom Classifier (_Custom_)_](). Example columns provide the data from which Databricks Data Classification learns to detect an organization‑specific sensitive data class, such as employee IDs, proprietary product codes, or partner account numbers. ^[custom-classifiers-databricks-on-aws.md]

## Purpose

Example columns serve as the training material for a custom classifier. The system analyzes the values in these columns to build detection rules for the governed tag assigned to the classifier. Broader and more varied example columns produce more accurate detection. ^[custom-classifiers-databricks-on-aws.md]

## Requirements

When selecting an example column, the following constraints apply:

- Each custom classifier must reference **between 1 and 10 example columns**. No more, no fewer. ^[custom-classifiers-databricks-on-aws.md]
- The user creating or editing the classifier must have the `SELECT` privilege on the table that contains the column. If `SELECT` is missing, the column cannot be chosen. ^[custom-classifiers-databricks-on-aws.md]
- The table must be in a Unity Catalog [Metastore](/concepts/metastore.md) where [Data Classification]() is enabled and [Serverless Compute]() is available. ^[custom-classifiers-databricks-on-aws.md]

## Selection Process

When creating a custom classifier via the **Manage custom classifiers** side panel, the second step is **Select example columns**:

1. Browse the catalog tree and select columns that contain representative values for the class.
2. Prefer columns whose values are typical of what should be detected. Broader variety improves detection accuracy.
3. Click **Create** to finalize the classifier. ^[custom-classifiers-databricks-on-aws.md]

After creation, detections from the example columns typically appear on the Data Classification results page within a few hours. ^[custom-classifiers-databricks-on-aws.md]

## Editing Example Columns

Example columns can be updated after the custom classifier is created:

1. In the **Manage custom classifiers** side panel, choose the classifier.
2. Click **Edit** next to the example columns list.
3. Add or remove columns (respecting the 1–10 limit).
4. Click **Save**.

Updates take effect within a few hours. Existing detections from the previous configuration remain in place. Changes to the governed tag or tag value are not allowed after creation — to switch tags, delete the classifier and recreate it. ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- A custom classifier must use at least 1 and at most 10 example columns. ^[custom-classifiers-databricks-on-aws.md]
- Example columns must come from tables that exist and are accessible. If a referenced table is deleted or renamed, the classifier may become suspended. ^[custom-classifiers-databricks-on-aws.md]
- Example columns that are not representative enough can cause rule generation or validation failure, leading to classifier suspension. ^[custom-classifiers-databricks-on-aws.md]
- All [Data Classification limitations]() apply to custom classifiers, including supported table types. ^[custom-classifiers-databricks-on-aws.md]

## Troubleshooting

- **Suspended classifier**: If example columns reference deleted/renamed tables or are insufficiently representative, edit the classifier with a better set of columns. If the issue is an invalid governed tag, delete and recreate the classifier. ^[custom-classifiers-databricks-on-aws.md]
- **Cannot select a column**: The user lacks `SELECT` on the table. Grant the privilege or choose a different column. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Custom Classifier](/concepts/custom-classifiers.md) – The classifier object that uses example columns.
- [Governed Tag](/concepts/governed-tags.md) – The tag assigned to the classifier, with allowed values.
- [Data Classification](/concepts/data-classification.md) – The scanning system that detects sensitive data.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) where classifiers and tables reside.
- [Metastore Admin](/concepts/metastore-admin-role.md) – Required to create, edit, or delete a custom classifier.
- Serverless Compute – Required for classification scans.
- [Column-Level Masking](/concepts/abac-column-level-mask-unity-catalog.md) – ABAC mask that can be applied after detection.

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
