---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38733178d4b6e4ffa33f97185eb23d3f8c98aa36aef57c64e0eab0086128a271
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - detection-exclusion-feedback-loop
    - DEFL
  citations:
    - file: data-classification-databricks-on-aws.md
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: Detection Exclusion Feedback Loop
description: A Beta feature allowing users to exclude individual column detections, which removes existing classification tags, prevents future reapplication, and provides feedback that improves the accuracy of future classification results.
tags:
  - data-governance
  - feedback
  - accuracy
timestamp: "2026-06-19T09:40:57.423Z"
---

# Detection Exclusion Feedback Loop

**Detection Exclusion Feedback Loop** refers to the mechanism in [Databricks Data Classification](/concepts/databricks-data-classification.md) where excluding a column detection both removes the classification tag from that column and provides feedback that improves the accuracy of future classification scans. This creates a continuous improvement cycle for automated data classification in [Unity Catalog](/concepts/unity-catalog.md).

## Overview

The detection exclusion feedback loop is a Beta feature of Databricks Data Classification that allows users to correct misclassifications and improve the system over time. When a column is incorrectly classified, users can exclude that detection, which triggers multiple actions that collectively refine the classification engine's accuracy.^[data-classification-databricks-on-aws.md]

## How the Feedback Loop Works

### Exclusion Actions

When a user excludes a column detection, three actions occur simultaneously:

1. **Tag removal**: Any existing classification tag is removed from the excluded column.
2. **Future prevention**: The system prevents future scans from reapplying the same classification tag to that column.
3. **Accuracy feedback**: The exclusion provides feedback that improves the accuracy of future classification results across the catalog.

^[data-classification-databricks-on-aws.md]

### Reversing Exclusions

Users can re-include a previously excluded detection by clicking the exclusion icon again. This restores the ability for future scans to re-evaluate and potentially reapply the classification tag to that column.^[data-classification-databricks-on-aws.md]

### User Interface

Exclusions are managed from the Data Classification review panel. For each detected column, an exclusion icon is available. The review panel displays detected columns ordered by most recent detection first, along with sample values (when the user has appropriate permissions).^[data-classification-databricks-on-aws.md]

## Relationship to Automatic Tagging

The feedback loop interacts with the [Automatic Tagging](/concepts/automatic-tagging.md) feature. When automatic tagging is enabled for a classification, excluded columns will not receive tags during future scans. However, when you disable tagging entirely, no future tags are applied, but existing tags (including those from before the exclusion) are not removed.^[data-classification-databricks-on-aws.md]

## Tag Inheritance and Exclusion

Columns do **not** inherit tags from their parent table or ancestors. The exclusion only applies to the specific column on which it was set. Tags on parent objects (catalogs, schemas, tables) are inherited by child objects except columns, but exclusion operates directly on column-level tags.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Best Practices

- **Review detections regularly**: Periodically check classification results to identify and exclude incorrect classifications.
- **Use exclusions for false positives**: When a column is consistently misclassified (e.g., a name field tagged as a phone number), excluding it prevents the error from recurring.
- **Combine with ABAC policies**: After excluding incorrect detections, create [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) or [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) for the remaining accurate classifications to govern sensitive data access.

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The AI-powered system that uses this feedback loop.
- [Automatic Tagging](/concepts/automatic-tagging.md) — The feature that applies tags based on classifications.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) — Dynamic masking policies that can be applied to classified columns.
- [Governed Tags](/concepts/governed-tags.md) — The tags used by classification and access control policies.
- Supported Classification Tags — The full list of tags the classification engine can detect.

## Sources

- data-classification-databricks-on-aws.md
- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
2. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
