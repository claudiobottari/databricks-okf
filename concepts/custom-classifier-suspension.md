---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a6358e9751bfaa1b4cfadd65d8adcfcc959c5930abd4df45887b14bd0ce49204
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifier-suspension
    - CCS
    - CCCS
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifier Suspension
description: Automatic suspension mechanism that halts detection for a custom classifier when rule generation or validation fails due to inaccessible columns, unrepresentative data, or invalid governed tags.
tags:
  - troubleshooting
  - data-governance
  - classification
timestamp: "2026-06-19T18:02:59.649Z"
---

# Custom Classifier Suspension

**Custom Classifier Suspension** occurs when Databricks Data Classification detects that rule generation or validation has failed for a [Custom Classifier|Custom Classifier](/concepts/custom-classifiers.md). When a classifier is suspended, it stops producing new detections and displays a warning on the Data Classification results page. ^[custom-classifiers-databricks-on-aws.md]

## Causes

A custom classifier can become suspended for several reasons:

- One or more of the example columns reference tables that have been deleted or renamed since the classifier was created.
- The example columns are not sufficiently representative for the system to learn a stable detection rule.
- The [Governed Tag|governed tag](/concepts/governed-tags.md) used by the classifier is no longer a governed tag, or the specific tag value is no longer valid.

These causes are identified in the troubleshooting guidance for custom classifiers. ^[custom-classifiers-databricks-on-aws.md]

## Symptoms

A suspended custom classifier produces no new detections. The Data Classification results page shows a warning banner indicating that one or more custom classifiers are suspended. ^[custom-classifiers-databricks-on-aws.md]

## Resolution

To resolve a suspension, edit the custom classifier and replace example columns that are inaccessible or not representative enough. If the governed tag or tag value is no longer valid, delete the custom classifier and create a new one with a valid tag. ^[custom-classifiers-databricks-on-aws.md]

### Steps to resolve

1. Open the **Manage custom classifiers** side panel from the Data Classification results page.
2. Select the suspended custom classifier.
3. Click **Edit** next to the example columns list.
4. Add or remove columns to ensure they are accessible and provide representative values.
5. Click **Save**. Updates take effect within a few hours.

If the governed tag itself is invalid, delete the custom classifier and create a new one with a valid tag. ^[custom-classifiers-databricks-on-aws.md]

## Prevention

To minimize the risk of suspension, ensure that:

- Example columns remain accessible (the table is not deleted or renamed).
- The columns contain a broad and varied set of values representative of the class to be detected.
- The governed tag and tag value continue to exist and are valid.

Regularly review custom classifiers after schema changes or tag policy updates. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Custom Classifier](/concepts/custom-classifiers.md) – User-defined classifiers that detect organization-specific sensitive data.
- [Data Classification](/concepts/data-classification.md) – The system that scans Unity Catalog for sensitive data.
- [Governed Tags](/concepts/governed-tags.md) – Tag-based governance controls used by custom classifiers.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer in Databricks.
- [ABAC Column-Level Masks](/concepts/abac-column-level-mask-unity-catalog.md) – Attribute-based access control masks that can be applied to classified columns.

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
