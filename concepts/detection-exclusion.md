---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6ba1f34ab73a9a421581d524fdf8e6e7b3d72af234e1ed533ff49f9283e61dc
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - detection-exclusion
    - detection-exclusion-and-feedback-loop
    - Feedback Loop and Detection Exclusion
    - DEAFL
    - detection-exclusion-feedback-loop
    - DEFL
    - detection-exclusions-in-data-classification
    - DEIDC
    - detection-exclusions
  citations:
    - file: data-classification-databricks-on-aws.md
title: Detection Exclusion
description: A beta feature allowing users to exclude individual column detections, which removes existing tags, prevents reapplication, and provides feedback to improve future classification accuracy.
tags:
  - data-governance
  - classification
  - beta
timestamp: "2026-06-19T14:40:28.235Z"
---

# Detection Exclusion

**Detection Exclusion** allows users to remove individual column detections from [Data Classification (Databricks)](/concepts/data-classification-databricks.md) results, preventing future scans from reapplying the associated classification tag to that column. The exclusion also provides feedback that improves the accuracy of future classification runs. ^[data-classification-databricks-on-aws.md]

The feature is in Beta|Beta release. ^[data-classification-databricks-on-aws.md]

## Overview

When Data Classification identifies a column as containing sensitive data (e.g., a Supported classification tags|classification tag such as `class.email_address`), it automatically tags the column. If the classification is incorrect — for example, if the column does not actually contain sensitive data — users can exclude that detection from the review panel. ^[data-classification-databricks-on-aws.md]

Exclusions are available per column within the **Review** panel for any classification type. ^[data-classification-databricks-on-aws.md]

## Effects of Excluding a Detection

Excluding a detection performs three actions: ^[data-classification-databricks-on-aws.md]

1. **Removes the existing tag** from the column (if a tag was already applied).
2. **Prevents future scans** from reapplying the same classification tag to that column.
3. **Provides feedback** that improves the accuracy of subsequent classification results across the catalog.

If [Automatic Tagging](/concepts/automatic-tagging.md) was enabled for the classification type, the exclusion overrides the automatic tagging for that specific column. ^[data-classification-databricks-on-aws.md]

## Process

To exclude a detection: ^[data-classification-databricks-on-aws.md]

1. Open the Data Classification results page for a catalog.
2. Click **Review** for the relevant classification type (e.g., `class.phone_number`).
3. In the **Detected Columns** tab, locate the column you want to exclude.
4. Click the **Exclude** icon (typically a crossed‑eye or similar symbol) next to the column entry.

To re‑include a previously excluded detection, click the same icon again. Re‑including will allow the tag to be reapplied in the next scan. ^[data-classification-databricks-on-aws.md]

## Use in GDPR Compliance

Data Classification assists with GDPR discovery and deletion workflows. If an incorrect classification is flagged during such a review, excluding the detection removes the tag and prevents its reapplication, ensuring compliance rules are not misapplied. ^[data-classification-databricks-on-aws.md]

## Relationship to Automatic Tagging

Automatic tagging applies classification tags when enabled at the [Metastore](/concepts/metastore.md) or catalog level. Exclusion takes precedence over automatic tagging: even if automatic tagging is active, an excluded column will not have the tag reapplied. To fully disable tagging for a classification type across all columns, use the **Automatic Tagging** toggle in the results page rather than excluding individual columns. ^[data-classification-databricks-on-aws.md]

## Requirements

To exclude a detection, users must have the same permissions required to view classification results: `USE CATALOG` and either `MANAGE` or (`SELECT` + `USE SCHEMA`) on the catalog. Users also need `SELECT` on the system.data_classification.results System Table|system.data_classification.results|results system table to see sample values associated with detections. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification (Databricks)](/concepts/data-classification-databricks.md) — The overarching feature that detects and tags sensitive data.
- [Automatic Tagging](/concepts/automatic-tagging.md) — Enables or disables tagging for a classification type across all columns.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Governance policies built on classification tags.
- System tables — The `system.data_classification.results` table stores classification results, including exclusion metadata.
- GDPR discovery and deletion — A use case where exclusion helps avoid misapplied deletion rules.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
