---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a99a1d820789e56d29c52f55039268f540666eb16f7e701565e8eaef0f22bcdd
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - example-columns-pattern
    - ECP
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Example Columns Pattern
description: The technique of providing 1–10 representative example columns from existing tables to teach a custom classifier what values to detect; broader and more varied examples produce more accurate detection rules.
tags:
  - data-governance
  - machine-learning
  - classification
timestamp: "2026-06-18T11:25:21.258Z"
---

# Example Columns Pattern

The **Example Columns Pattern** is the practice of selecting representative columns from existing tables in Unity Catalog to train a [custom classifier](/concepts/custom-classifiers.md) that detects organization-specific sensitive data during Data Classification scans. This pattern enables organizations to extend the built-in classification system to recognize data types unique to their context, such as internal employee IDs, proprietary product codes, vendor identifiers, or partner account numbers, without writing complex rules or regular expressions. ^[custom-classifiers-databricks-on-aws.md]

## How It Works

When you create a custom classifier, you choose a [governed tag](/concepts/governed-tags.md) (and optionally a specific tag value) and provide between 1 and 10 example columns that contain representative values for the class. Databricks analyzes the values in those columns to learn a classification rule. The learned rule is then applied during subsequent Data Classification scans across all catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled. ^[custom-classifiers-databricks-on-aws.md]

Detections from the custom classifier typically appear on the Data Classification results page within a few hours after creation. Updated classifiers take effect on the next scan; existing detections from the previous configuration remain in place. ^[custom-classifiers-databricks-on-aws.md]

## Requirements

To use the Example Columns Pattern, your workspace must meet these prerequisites: ^[custom-classifiers-databricks-on-aws.md]

- Data Classification must be enabled on at least one catalog in the [Metastore](/concepts/metastore.md).
- Serverless compute must be available in the workspace (enabled by default in workspaces with Unity Catalog).
- To create, edit, or delete a custom classifier, you must be a **metastore admin**.
- To create or edit a custom classifier, you must have `ASSIGN` privileges on the governed tag the classifier uses.
- To select a column for the classifier, you must have `SELECT` on the table that contains it.

## Best Practices for Selecting Example Columns

- **Choose varied and representative columns.** Broader and more varied examples produce more accurate detection rules. ^[custom-classifiers-databricks-on-aws.md]
- **Ensure columns contain typical values** of the class you want to detect. If the examples are too narrow or skewed, the classifier may fail to detect actual sensitive data or produce false positives.
- **Avoid columns with null or empty values** — the system needs actual data to learn the pattern.
- **Update examples if a classifier is suspended.** If rule generation or validation fails, edit the custom classifier with a different set of example columns to resolve the suspension. ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- A maximum of **50 custom classifiers** can be created per [Metastore](/concepts/metastore.md). ^[custom-classifiers-databricks-on-aws.md]
- Each custom classifier must reference **between 1 and 10 example columns**.
- The governed tag and tag value **cannot be changed after creation**. To switch to a different tag, delete the classifier and create a new one.
- Custom classifiers apply to **all Data Classification-enabled catalogs** in the [Metastore](/concepts/metastore.md); per-catalog or per-schema scoping is not supported.
- New and updated classifiers apply only to **subsequent scans**; previously scanned data is not automatically reclassified.
- All general Data Classification limitations (e.g., supported table types) also apply to custom classifiers.

## Suspended Classifiers

If rule generation or validation fails, Databricks suspends the custom classifier and shows a warning on the Data Classification results page. A suspended classifier produces no new detections. Common causes include: ^[custom-classifiers-databricks-on-aws.md]

- One or more example columns reference tables that have been deleted or renamed.
- The example columns are not representative enough for stable detection.
- The governed tag is no longer valid, or the tag value is no longer valid.

To resolve a suspension, edit the custom classifier with different example columns. If the suspension is caused by an invalid governed tag or tag value, delete the classifier and create a new one with a valid tag.

## Related Concepts

- [Custom Classifiers](/concepts/custom-classifiers.md) — The broader feature that uses the Example Columns Pattern
- [Governed Tags](/concepts/governed-tags.md) — Tags that define the classification categories used by custom classifiers
- [Data Classification](/concepts/data-classification.md) — The scanning system that detects sensitive data in Unity Catalog
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) — Governance controls applied based on classification results

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
