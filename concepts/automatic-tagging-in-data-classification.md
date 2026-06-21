---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b867439e122c4ae37c43b30b88e5968ec459ef3f155105a5e2eea5c39e347fb5
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-tagging-in-data-classification
    - ATIDC
    - Automatic Data Classification
  citations:
    - file: data-classification-databricks-on-aws.md
      start: 18
      end: 20
    - file: data-classification-databricks-on-aws.md
      start: 63
      end: 66
    - file: data-classification-databricks-on-aws.md
      start: 58
      end: 62
    - file: data-classification-databricks-on-aws.md
      start: 56
      end: 57
    - file: data-classification-databricks-on-aws.md
      start: 62
      end: 62
    - file: data-classification-databricks-on-aws.md
      start: 9
      end: 10
    - file: data-classification-databricks-on-aws.md
      start: 58
      end: 60
    - file: data-classification-databricks-on-aws.md
      start: 12
      end: 14
    - file: data-classification-databricks-on-aws.md
      start: 77
      end: 79
title: Automatic Tagging in Data Classification
description: The ability to automatically apply governed tags to all existing and future column detections of a given classification type, configurable at catalog and metastore levels.
tags:
  - tagging
  - data-governance
  - unity-catalog
timestamp: "2026-06-19T18:04:05.674Z"
---

```markdown
---
title: Automatic Tagging in Data Classification
summary: A feature that automatically applies classification tags to all existing and future detections of a given classification type, configurable at both [[metastore|Metastore]] and catalog levels.
sources:
  - data-classification-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:27:13.126Z"
updatedAt: "2026-06-18T11:27:13.126Z"
tags:
  - tagging
  - automation
  - governance
aliases:
  - automatic-tagging-in-data-classification
  - ATIDC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Automatic Tagging in Data Classification

**Automatic Tagging** is a capability within [[Data Classification]] that applies classification tags to columns in Unity Catalog where the classification engine has detected sensitive data with high confidence. Once enabled, the system tags both existing and newly detected columns automatically, allowing organizations to then enforce governance controls — such as [[ABAC GRANT Policy]] or [[Row Filter Policies]] — based on those tags. ^[data-classification-databricks-on-aws.md:18-20]

## Workflow Overview

1. Classify a catalog or schema using the Data Classification engine.
2. Review the detected columns in the classification results panel.
3. If the detections are correct, enable automatic tagging for that classification tag.

When automatic tagging is activated, the classification tag is applied to all matching columns. Tags are not backfilled immediately; they will appear during the next scan (typically within 24 hours). After the first scan, subsequent classifications of new columns are tagged immediately. ^[data-classification-databricks-on-aws.md:63-66]

## Configuration Levels

Automatic tagging can be configured at two levels:

- **Metastore level**: Enable or disable across all catalogs at once. Requires [[metastore|Metastore]] admin privileges and the `ASSIGN` permission on the tag being applied.
- **Catalog level**: Enable or disable for a specific catalog. Catalog-level settings override the metastore-level setting. Requires `USE CATALOG` and `APPLY TAG` on the catalog, plus `ASSIGN` on the tag being applied. ^[data-classification-databricks-on-aws.md:58-62]

### Catalog-Level States

Each classification tag at the catalog level can be in one of three states:

| State | Description |
|-------|-------------|
| **Default (inherited)** | The catalog follows the metastore-level setting. |
| **Active** | Tagging is explicitly enabled for this catalog, regardless of the [[metastore|Metastore]] setting. |
| **Inactive** | Tagging is explicitly disabled for this catalog. Existing tags are not removed. |

^[data-classification-databricks-on-aws.md:58-62]

## Enabling Automatic Tagging

When reviewing classification results, you can enable automatic tagging for a specific classification tag from the results panel. The action requires the appropriate permissions (see #Requirements). Once enabled, future scans will apply the tag to all columns that match the classification, including columns in schemas added later to the catalog. ^[data-classification-databricks-on-aws.md:56-57]

If you disable automatic tagging, no new tags are applied, but any tags that were already assigned remain on the columns. ^[data-classification-databricks-on-aws.md:62]

## Requirements

To enable automatic tagging for a catalog, you must have: ^[data-classification-databricks-on-aws.md:9-10]

- `USE CATALOG` on the catalog.
- `APPLY TAG` on the catalog.
- `ASSIGN` on the tag being applied (typically a [[Governed Tags|governed tag]] from the Data Classification system).

To configure automatic tagging at the [[metastore|Metastore]] level, you must be a [[metastore|Metastore]] admin and have the `ASSIGN` permission on the tag. ^[data-classification-databricks-on-aws.md:58-60]

By default, only account admins have `MANAGE` and `ASSIGN` permissions on data classification system governed tags. Account admins can grant these permissions to other users, service principals, or groups. ^[data-classification-databricks-on-aws.md:12-14]

## Managing Detections

If a classification is incorrect, you can exclude individual column detections from the review panel. Excluding a detection: ^[data-classification-databricks-on-aws.md:77-79]

- Removes any existing classification tag from that column.
- Prevents future scans from reapplying the tag to that column.
- Provides feedback that improves the accuracy of future classification results.

## Related Concepts

- [[Data Classification]] — The AI-driven system that discovers sensitive data
- [[Governed Tags]] — Tags applied by automatic tagging that drive ABAC policies
- [[ABAC GRANT Policy]] — Attribute-based access control that can reference classification tags
- [[Row Filter Policies]] — ABAC policies that restrict rows based on tags
- [[Column Mask Policies]] — ABAC policies that mask sensitive columns
- [[Unity Catalog]] — The governance layer where classification is performed
- [[Data Classification System Table]] — The `system.data_classification.results` table that stores classification metadata

## Sources

- data-classification-databricks-on-aws.md
```

# Citations

1. [data-classification-databricks-on-aws.md:18-20](/references/data-classification-databricks-on-aws-066fe683.md)
2. [data-classification-databricks-on-aws.md:63-66](/references/data-classification-databricks-on-aws-066fe683.md)
3. [data-classification-databricks-on-aws.md:58-62](/references/data-classification-databricks-on-aws-066fe683.md)
4. [data-classification-databricks-on-aws.md:56-57](/references/data-classification-databricks-on-aws-066fe683.md)
5. [data-classification-databricks-on-aws.md:62-62](/references/data-classification-databricks-on-aws-066fe683.md)
6. [data-classification-databricks-on-aws.md:9-10](/references/data-classification-databricks-on-aws-066fe683.md)
7. [data-classification-databricks-on-aws.md:58-60](/references/data-classification-databricks-on-aws-066fe683.md)
8. [data-classification-databricks-on-aws.md:12-14](/references/data-classification-databricks-on-aws-066fe683.md)
9. [data-classification-databricks-on-aws.md:77-79](/references/data-classification-databricks-on-aws-066fe683.md)
