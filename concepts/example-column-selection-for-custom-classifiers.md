---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6aba10ae4f65bf6a610cdde6ec5aef5a94a7d273b66d1f9c19995b86ce92086f
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - example-column-selection-for-custom-classifiers
    - ECSFCC
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Example column selection for custom classifiers
description: Process of choosing 1-10 representative table columns per classifier to train detection rules, where broader and more varied examples improve accuracy.
tags:
  - data-governance
  - configuration
  - classification
timestamp: "2026-06-18T14:57:05.531Z"
---

# Example Column Selection for Custom Classifiers

**Example column selection for custom classifiers** refers to the process of choosing representative columns from Unity Catalog tables to serve as training data for a [custom classifier](/concepts/custom-classifiers.md). The quality and variety of the selected columns directly determines how accurately the classifier detects the sensitive data class across the [Metastore](/concepts/metastore.md).

## Overview

When creating a [custom classifier](/concepts/custom-classifiers.md) in Databricks Data Classification, the system learns detection rules from example columns that contain representative values for the data class you want to detect. The example column selection step is critical: broader and more varied examples produce more accurate detection rules. ^[custom-classifiers-databricks-on-aws.md]

Databricks generates detection metadata from the provided example columns, which is encrypted at rest. ^[custom-classifiers-databricks-on-aws.md]

## Column Requirements

### Number of Columns

Each custom classifier must reference between **1 and 10** example columns to provide sufficient data for classification. You can add or remove columns when editing an existing classifier, subject to this limit. ^[custom-classifiers-databricks-on-aws.md]

### Permission Requirements

To select a column as an example, you must have `SELECT` permission on the table that contains it. If you lack `SELECT` on the table, ask the table owner to grant it, or choose a different example column. ^[custom-classifiers-databricks-on-aws.md]

### Content Guidelines

Choose columns whose values are typical of what you want detected. For example, if you are creating a classifier for internal employee IDs, select columns from tables that contain actual employee ID values. Columns with broader value variety and more representative samples produce more stable and accurate detection rules. ^[custom-classifiers-databricks-on-aws.md]

## Selection Process

When creating a custom classifier through the Data Classification results page:

1. Navigate to the **Manage custom classifiers** side panel.
2. Click **Create custom classifier** and select a governed tag with a specific value.
3. Browse the catalog tree and select columns that contain representative values for the class.
4. Click **Create** to finalize.

Detections from the custom classifier typically appear on the results page within a few hours. ^[custom-classifiers-databricks-on-aws.md]

## Editing Example Columns

You can update the example columns for an existing custom classifier:

1. In the **Manage custom classifiers** side panel, select the classifier to edit.
2. Click **Edit** next to the example columns list.
3. Add or remove columns as needed, staying within the 10-column limit.
4. Click **Save**.

Updates take effect within a few hours. Existing detections from the previous configuration remain in place. ^[custom-classifiers-databricks-on-aws.md]

## Impact on Detection Accuracy

The quality of example columns directly affects the classifier's ability to produce reliable detections. If the example columns are not representative enough for the system to learn a stable detection pattern, the classifier may be suspended. Common causes for suspension include:

- One or more example columns reference tables that have been deleted or renamed.
- The example columns are not representative enough for the system to learn a stable detection.
- The governed tag or tag value is no longer valid.

To resolve a suspension, edit the custom classifier with a different set of example columns and wait for the next scan. ^[custom-classifiers-databricks-on-aws.md]

## Best Practices

- **Select multiple columns** from different tables to capture variety in formatting and content.
- **Choose active tables** that are unlikely to be deleted or renamed.
- **Ensure columns contain authentic values** that reflect the real-world format of the data class.
- **Avoid columns with sparse data** or values that are too similar, as they may not provide enough variation for the system to generalize.
- **Verify accessibility** by confirming you have `SELECT` permission before selecting a column.

## Related Concepts

- [Custom Classifiers](/concepts/custom-classifiers.md)
- [Data Classification](/concepts/data-classification.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Data Classification System Table](/concepts/data-classification-system-table.md)
- Supported Classification Tags

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
