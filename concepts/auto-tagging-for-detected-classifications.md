---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5dc800785602f127cff9c8ee00cc14460cafff0dbee33a5a9e0e6d0bc91846d0
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-tagging-for-detected-classifications
    - AFDC
  citations:
    - file: data-classification-databricks-on-aws.md
title: Auto-tagging for Detected Classifications
description: Automatic tagging feature that applies classification tags to all existing and future detections of a classification type. Configurable at both metastore level and catalog level, with catalog-level settings taking precedence.
tags:
  - data-governance
  - tagging
  - automation
timestamp: "2026-06-19T09:40:57.976Z"
---

# Auto-tagging for Detected Classifications

**Auto-tagging for Detected Classifications** is a feature of [Databricks Data Classification](/concepts/databricks-data-classification.md) that automatically applies classification tags to columns when the classification engine detects sensitive data types. When enabled, all existing and future detections of a given classification type are automatically tagged, providing a foundation for [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies and governance controls. ^[data-classification-databricks-on-aws.md]

## Overview

After the classification engine detects sensitive data in columns (such as PII, financial information, or credentials), auto-tagging ensures that the corresponding classification tag is applied to those columns without manual intervention. This enables downstream governance policies — such as [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) — to dynamically mask or restrict access based on the tags. ^[data-classification-databricks-on-aws.md]

The tagging status for each classification type is displayed on the Data Classification results page as **Active** or **Inactive**. At the [Metastore](/concepts/metastore.md) level, a status of **Partially Active** indicates that tagging is enabled in some but not all catalogs. ^[data-classification-databricks-on-aws.md]

## Enabling Auto-tagging

You can configure auto-tagging at two levels: the [Metastore](/concepts/metastore.md) (across all catalogs) or an individual catalog. Catalog-level settings take precedence over the metastore-level setting. ^[data-classification-databricks-on-aws.md]

### At the [Metastore](/concepts/metastore.md) Level

To enable or disable auto-tagging across all catalogs at once, you must be a [Metastore](/concepts/metastore.md) admin and have `ASSIGN` permission on the tag being applied. ^[data-classification-databricks-on-aws.md]

### At the Catalog Level

To enable or disable for the current catalog only, you must have `USE CATALOG` and `APPLY TAG` on the catalog, and `ASSIGN` on the tag being applied. Catalog-level auto-tagging has three states: ^[data-classification-databricks-on-aws.md]

- **Default (inherited)**: The catalog inherits the tagging setting from the [Metastore](/concepts/metastore.md) level.
- **Active**: Tagging is explicitly enabled for this catalog, regardless of the metastore-level setting.
- **Inactive**: Tagging is explicitly disabled for this catalog, regardless of the metastore-level setting.

When you disable tagging, no future tags are applied, but existing tags are not removed. ^[data-classification-databricks-on-aws.md]

## Timing

When you enable automatic tagging, tags are not backfilled immediately. They are populated during the next scan, which typically takes effect within 24 hours. After the initial backfill, subsequent classifications are tagged immediately. ^[data-classification-databricks-on-aws.md]

## Requirements

To enable auto-tagging for a catalog, the user must have: ^[data-classification-databricks-on-aws.md]

- `USE CATALOG` on the catalog
- `APPLY TAG` on the catalog
- `ASSIGN` on the tag being applied

By default, only account admins have `MANAGE` and `ASSIGN` permissions on data classification system governed tags. Account admins can grant these permissions to other users, service principals, or groups. ^[data-classification-databricks-on-aws.md]

## Interaction with Exclusions

If a detection is incorrect, you can exclude individual column detections from the review panel. Excluding a detection: ^[data-classification-databricks-on-aws.md]

- Removes any existing classification tag from that column.
- Prevents future scans from reapplying the tag to that column.
- Provides feedback that improves the accuracy of future classification results.

To re-include the detection, click the exclusion icon again. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Databricks Data Classification](/concepts/databricks-data-classification.md) — The AI agent that detects sensitive data
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Governance framework that uses tags for access policies
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) — Dynamic column masking based on classification tags
- [Governed Tags](/concepts/governed-tags.md) — The tag system used for classification and access control
- [Supported classification tags](/concepts/classification-tags-and-governed-tags-system.md) — The complete list of tags the classification engine can detect
- [Data Classification Results](/concepts/data-classification-results-page.md) — The system table and UI for reviewing detections

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
