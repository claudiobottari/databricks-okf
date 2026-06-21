---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 63005fffd5e510b1bfb03be8ee00a6bdefd83c5a66e9ed3e246421923f36fdc7
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifier-limitations-databricks
    - CCL(
    - NCCL
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifier Limitations (Databricks)
description: Constraints on custom classifiers including a 50-classifier-per-metastore cap, 1-10 example column requirement, immutable tag assignment, and metastore-wide application scope.
tags:
  - data-governance
  - unity-catalog
  - limitations
timestamp: "2026-06-19T18:03:03.176Z"
---

# Custom Classifier Limitations (Databricks)

**Custom Classifier Limitations (Databricks)** describes the constraints and boundaries that apply when using custom classifiers for data classification in [Unity Catalog](/concepts/unity-catalog.md). Custom classifiers extend the built-in classification system to detect organization-specific sensitive data, such as internal employee IDs, proprietary product codes, or vendor identifiers. ^[custom-classifiers-databricks-on-aws.md]

## Scope and Capacity Limits

The following limits govern custom classifier creation and application:

- **Maximum classifiers per metastore**: You can create a maximum of **50 custom classifiers** per [Metastore](/concepts/metastore.md). ^[custom-classifiers-databricks-on-aws.md]
- **Example column requirements**: Each custom classifier must reference between **1 and 10 example columns** to provide sufficient data for classification. ^[custom-classifiers-databricks-on-aws.md]
- **Global [Metastore](/concepts/metastore.md) scope**: Custom classifiers apply to **all** catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled. Per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]

## Immutability of Tag Assignment

The governed tag and tag value used by a custom classifier **cannot be changed after creation**. To switch to a different tag, you must delete the custom classifier and create a new one with the desired tag. ^[custom-classifiers-databricks-on-aws.md]

## Scan Timing and Reclassification

New and updated custom classifiers apply **only to subsequent Data Classification scans**. Existing scan results are not automatically reclassified, so detections for previously scanned data appear only after the next scan completes. ^[custom-classifiers-databricks-on-aws.md]

## Tag Naming Constraints

Governed tag naming is subject to Tag Policy rules. Custom classifiers must use governed tags that comply with these policies. ^[custom-classifiers-databricks-on-aws.md]

## Inherited Limitations

All standard [Data Classification](/concepts/data-classification.md) limitations apply to custom classifiers as well, including restrictions on supported table types. ^[custom-classifiers-databricks-on-aws.md]

## Impact of Deletion

When you delete a custom classifier:
- No new detections are produced for that classifier.
- Existing detections are removed from the Data Classification results page.
- Tags that were already auto-applied to columns are **not removed automatically**. ^[custom-classifiers-databricks-on-aws.md]

## Suspension Conditions

Rule generation or validation failures cause Databricks to suspend the custom classifier. A suspended classifier produces no new detections until the issue is resolved. Common causes include:
- Example columns referencing tables that have been deleted or renamed.
- Example columns not representative enough for stable detection.
- The governed tag is no longer valid, or the tag value has become invalid. ^[custom-classifiers-databricks-on-aws.md]

## Permission Requirements

- To create, edit, or delete a custom classifier, you must be a **metastore admin**.
- To create or edit a custom classifier, you must have **`ASSIGN` privileges** on the governed tag the classifier uses.
- To select a column for the classifier, you must have **`SELECT` on the table** that contains it. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The built-in classification system for Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform for Databricks
- [Governed Tags](/concepts/governed-tags.md) — Tags used by custom classifiers for auto-tagging
- Tag Policy — Rules governing tag naming conventions
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Column-level masking enabled by classifiers
- Serverless Compute — Required for custom classifier functionality

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
