---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: de4b8abbff634b1f67ffdd1217ed3d0c08eb77a6f9b3e9c9a92a5a7a0088cf43
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - detection-exclusion-and-feedback-loop
    - Feedback Loop and Detection Exclusion
    - DEAFL
  citations:
    - file: data-classification-databricks-on-aws.md
title: Detection Exclusion and Feedback Loop
description: A Beta feature allowing users to exclude individual column detections, which removes existing tags, prevents reapplication, and provides feedback to improve future classification accuracy.
tags:
  - feedback
  - accuracy
  - classification
timestamp: "2026-06-18T14:58:14.156Z"
---

# Detection Exclusion and Feedback Loop

**Detection Exclusion and Feedback Loop** refers to the mechanism in [Databricks Data Classification](/concepts/databricks-data-classification.md) that allows users to mark individual column detections as incorrect. Excluding a detection removes the associated classification tag from that column, prevents it from being reapplied in future scans, and feeds the user’s correction back into the classification engine to improve the accuracy of future results. ^[data-classification-databricks-on-aws.md]

This feature is in **Beta**. ^[data-classification-databricks-on-aws.md]

## How It Works

When data classification scans a table, it identifies columns that contain sensitive data (e.g., PII, financial information) and applies the appropriate [Governed Tags](/concepts/governed-tags.md). A user reviewing the results may see a detection that is incorrect – for example, a column that was flagged as containing email addresses when it does not. Using the **Exclude** icon in the review panel, the user can exclude that individual detection. ^[data-classification-databricks-on-aws.md]

Excluding a detection performs three actions:

1. **Removes the tag** – Any existing classification tag is removed from that column. ^[data-classification-databricks-on-aws.md]
2. **Prevents re‑application** – Future scans will not reapply the same tag to that column. ^[data-classification-databricks-on-aws.md]
3. **Improves accuracy** – The system uses the exclusion as feedback to refine its classification model, leading to more accurate detections over time. ^[data-classification-databricks-on-aws.md]

If the exclusion was made in error, the user can click the icon again to re‑include the detection, restoring the tag and allowing future scans to reconsider it. ^[data-classification-databricks-on-aws.md]

## Steps to Exclude a Detection

1. Navigate to the Data Classification results page for the relevant catalog. See [View classification results](/concepts/classification-results-ui.md).
2. For a specific classification type (e.g., `email_address`), click **Review** to open the review panel.
3. In the **Detected Columns** tab, locate the column you wish to exclude.
4. Click the **Exclude** icon (a small cross or toggle) next to the column entry.
5. To re‑include, click the icon again.

The exclusion is immediate and persists across scans. ^[data-classification-databricks-on-aws.md]

## The Feedback Loop

The detection exclusion and feedback loop is a core component of Databricks Data Classification’s adaptive intelligence. Each manual exclusion acts as a labelled correction that the system ingests to adjust its detection logic. As more exclusions are provided, the classification engine becomes more precise, reducing false positives in subsequent scans of the same or similar columns. This continuous human‑in‑the‑loop improvement is what makes the feedback loop effective for governing sensitive data at scale. ^[data-classification-databricks-on-aws.md]

## Benefits

- **Accuracy improvement** – User corrections directly enhance the classification model. ^[data-classification-databricks-on-aws.md]
- **Reduced noise** – Incorrect tags are removed and stay removed, giving a cleaner picture of sensitive data. ^[data-classification-databricks-on-aws.md]
- **Persistent exclusions** – Once excluded, the column is not re‑tagged for the same classification type, avoiding repeated manual work. ^[data-classification-databricks-on-aws.md]
- **Low‑effort governance** – Combined with [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) and automatic tagging, exclusions help ensure that only the correct columns are governed. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) – The automated scanning and tagging process that produces the detections.
- [Governed Tags](/concepts/governed-tags.md) – The tag system used to label detected sensitive data.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – Dynamic masking policies that can be applied based on classification tags.
- Review detections – The workflow for inspecting classification results.
- [Automatic Tagging](/concepts/automatic-tagging.md) – Enabling bulk tagging for a classification type across the [Metastore](/concepts/metastore.md) or catalog.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
