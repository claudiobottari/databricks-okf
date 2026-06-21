---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f593afffdcd24aaca4965ea1d1b41d8c63ce05a4b88c6546c04873e87ebb262c
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-tagging-with-governed-tags
    - ATWGT
  citations:
    - file: data-classification-databricks-on-aws.md
title: Automatic Tagging with Governed Tags
description: A mechanism to automatically apply governed classification tags to detected columns; configurable at metastore and catalog levels with inherited, active, or inactive states.
tags:
  - tagging
  - governance
  - unity-catalog
timestamp: "2026-06-18T14:58:08.143Z"
---

##Automatic Tagging with Governed Tags

**Automatic Tagging with Governed Tags** is a feature of [Databricks Data Classification](/concepts/databricks-data-classification.md) that applies [Governed Tags](/concepts/governed-tags.md) to columns automatically when the classification engine detects sensitive data. When enabled for a specific classification type (e.g., `class.email_address`), all existing and future detections of that classification receive the corresponding governed tag without manual intervention.^[data-classification-databricks-on-aws.md]

### How It Works

After classification results are reviewed and confirmed, a user can enable automatic tagging for a given classification. The tagging engine applies the governed tag to every column where that classification was detected (with high confidence). Enabling automatic tagging does **not** backfill tags immediately; tags are populated during the next scheduled scan, which typically completes within 24 hours. Subsequent classifications on new or changed tables are tagged as soon as they are detected.^[data-classification-databricks-on-aws.md]

Automatic tagging can be configured at two levels: metastore-wide and per-catalog. The catalog-level setting takes precedence over the metastore-level setting.^[data-classification-databricks-on-aws.md]

### Permissions Required

To enable automatic tagging, a user must have the following privileges on the target catalog and tag:

- `USE CATALOG` on the catalog
- `APPLY TAG` on the catalog
- `ASSIGN` on the governed tag being applied

At the [Metastore](/concepts/metastore.md) level, the user must also be a [Metastore](/concepts/metastore.md) admin and have `ASSIGN` on the tag.^[data-classification-databricks-on-aws.md]

### Configuration States (Catalog Level)

When configuring automatic tagging for a single catalog, the setting has three states:^[data-classification-databricks-on-aws.md]

| State | Description |
|-------|-------------|
| **Default (inherited)** | The catalog inherits the tagging setting from the [Metastore](/concepts/metastore.md) level. |
| **Active** | Tagging is explicitly enabled for this catalog, regardless of the metastore-level setting. |
| **Inactive** | Tagging is explicitly disabled for this catalog, regardless of the metastore-level setting. |

When tagging is set to **Inactive**, no future tags are applied, but existing tags are **not** removed.^[data-classification-databricks-on-aws.md]

### Relationship to Governance Controls

Automatic tagging is a prerequisite for using [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies that match on governed tags. Once tags are applied, ABAC column mask policies or row filter policies can automatically protect or restrict access to the tagged columns without requiring per-table configuration. This enables a workflow where data is first classified, then automatically tagged, and finally governed by policy.^[data-classification-databricks-on-aws.md]

### Best Practices

- Review detections before enabling automatic tagging to avoid tagging false positives. Use the exclusion mechanism to remove incorrect detections.^[data-classification-databricks-on-aws.md]
- Consider enabling at the [Metastore](/concepts/metastore.md) level for organization-wide compliance coverage, then override at the catalog level when a specific classification should not be automatically tagged in a particular catalog.^[data-classification-databricks-on-aws.md]

### Related Concepts

- [Data Classification](/concepts/data-classification.md) – The AI-driven process that detects sensitive data and suggests tags.
- [Governed Tags](/concepts/governed-tags.md) – The tag system that powers ABAC policies in Unity Catalog.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – Use governed tags to dynamically mask sensitive columns.
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) – Use governed tags to restrict access to rows.
- System Table for Data Classification – Stores classification results and sample values.

### Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
