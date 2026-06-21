---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9cf7473e8b42900fceae12eaecccb90872328588a656647ad5784398a090a27a
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - detection-exclusions-in-data-classification
    - DEIDC
  citations:
    - file: data-classification-databricks-on-aws.md
title: Detection Exclusions in Data Classification
description: A Beta feature allowing users to exclude individual column detections, removing existing tags, preventing reapplication, and providing feedback to improve future classification accuracy.
tags:
  - exclusions
  - feedback
  - accuracy
  - beta
timestamp: "2026-06-18T11:27:34.740Z"
---

# Detection Exclusions in Data Classification

**Detection Exclusions** allow users to mark individual column-level classification results as incorrect in [Data Classification](/concepts/data-classification.md). Excluding a detection removes any existing classification [tag](/concepts/governed-tags.md) from that column and prevents the classification engine from reapplying the same tag to that column in future scans. This feedback mechanism also improves the accuracy of the classification model over time. ^[data-classification-databricks-on-aws.md]

Detection exclusions are currently in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). ^[data-classification-databricks-on-aws.md]

## How Exclusions Work

When a classification scan identifies a column with a high-confidence tag — such as `class.email_address` or `class.phone_number` — the result appears on the Data Classification review panel. If the detection is incorrect (e.g., a column contains a user ID that happens to match an email pattern but is not actually an email), users can exclude that specific detection. The exclusion:

- Removes the classification tag from the column immediately.
- Tells the classification engine to skip that column in subsequent scans, preventing the tag from being reapplied.
- Provides a signal that helps improve the model’s accuracy for future classifications across all tables in the [Metastore](/concepts/metastore.md). ^[data-classification-databricks-on-aws.md]

## Excluding a Detection

To exclude a detection:

1. Navigate to the Data Classification results page for a catalog or the [Metastore](/concepts/metastore.md).
2. Click **Review** next to the classification type (e.g., "Email Address").
3. In the **Detected Columns** tab, find the column you want to exclude.
4. Click the **Exclude** icon (a circle with a line through it) to the right of the entry.

![Excluding an individual column from detection.](https://docs.databricks.com/aws/en/assets/images/data-classification-exclude-column-f48e33a1e2a5a2c32d71029d58bf862b.png)

The exclusion takes effect immediately. ^[data-classification-databricks-on-aws.md]

## Re-including a Detection

If a detection was excluded in error, you can reverse the action by clicking the **Exclude** icon again. After re-inclusion, the column will be reconsidered during the next scheduled scan and may receive the tag again if the classification engine still identifies it with high confidence. ^[data-classification-databricks-on-aws.md]

## Impact on Future Scans

Excluded detections are respected in all future incremental scans. The classification engine does not re-evaluate excluded columns unless the exclusion is manually reversed. This prevents repeated false positives and reduces unnecessary scanning cost. ^[data-classification-databricks-on-aws.md]

Exclusions are stored at the [Metastore](/concepts/metastore.md) level and apply across all workspaces sharing that [Metastore](/concepts/metastore.md). There is no mechanism to exclude an entire column from all classification tags at once; exclusions are specific to a single classification type on a single column.

## Best Practices

- **Review detections promptly.** After a new scan completes, examine the results in the Data Classification UI to catch false positives early.
- **Exclude rather than ignore.** Excluding a detection improves the system’s accuracy for all users. Simply ignoring an incorrect tag does not train the model.
- **Document exclusions.** Keep a record of why a detection was excluded to aid audits and future reviews.
- **Validate after tag changes.** If a column’s data format changes (e.g., from a numeric ID to an email field), re-include any previous exclusion so the column can be reclassified correctly.

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The AI-driven system that discovers and tags sensitive data in Unity Catalog.
- [Governed Tags](/concepts/governed-tags.md) — The tag framework used to mark sensitive data and enforce ABAC policies.
- Supported Classification Tags — The full list of tags the classification engine can apply.
- ABAC Policy — Attribute-based access control policies that can be triggered by classification tags.
- [Data Classification Results System Table](/concepts/data-classification-results-system-table.md) — The `system.data_classification.results` table storing all classification outcomes.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
