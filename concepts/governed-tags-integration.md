---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d769791354d58b786ed8b586d1387f46bcd92cea7aea6580422352c1ccc9860b
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - governed-tags-integration
    - GTI
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Governed Tags Integration
description: Custom classifiers assign governed tags to detected columns, enabling ABAC column-level masks and auto-tagging for organization-specific data types.
tags:
  - data-governance
  - tagging
  - access-control
timestamp: "2026-06-19T09:39:03.371Z"
---

# Governed Tags Integration

**Governed Tags Integration** refers to the use of [Governed Tags](/concepts/governed-tags.md) as the foundation for automated sensitive-data discovery and downstream access controls in Unity Catalog. By coupling governed tags with custom classifiers and attribute-based access control (ABAC), organizations can detect proprietary data types, auto-tag them, and then enforce dynamic masking—all without manual per-column configuration. ^[custom-classifiers-databricks-on-aws.md]

## Overview

Governed tags are the attribute system that enables tag-based governance policies in Unity Catalog. When combined with [Data Classification](/concepts/data-classification.md), governed tags can be automatically applied to columns that match a predefined pattern. Custom classifiers extend this mechanism by allowing you to detect data types that are unique to your organization—such as internal employee IDs or proprietary product codes—and assign a governed tag accordingly. ^[custom-classifiers-databricks-on-aws.md]

## Integration with Custom Classifiers

A custom classifier is defined by selecting a governed tag (and optionally a specific tag value) and providing one to ten example columns that contain representative values. The system learns a detection rule from those examples and, during subsequent data classification scans, automatically tags matching columns with the chosen governed tag. ^[custom-classifiers-databricks-on-aws.md]

This integration enables two key workflows:

- **Tagging organization-specific data**: Detect and auto-tag data types that are unique to your organization. ^[custom-classifiers-databricks-on-aws.md]
- **Enabling ABAC governance controls**: Once a column is tagged, you can apply [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md) that reference the tag, enforcing dynamic masking at query time. ^[custom-classifiers-databricks-on-aws.md]

## Requirements for Integration

To create or edit a custom classifier that uses a governed tag, you must:

- Be a [Metastore](/concepts/metastore.md) admin.
- Have `ASSIGN` privileges on the governed tag the classifier uses. See [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md). ^[custom-classifiers-databricks-on-aws.md]
- Have `SELECT` on the table containing the example column. ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- Governed tag naming is subject to Tag Policy rules. ^[custom-classifiers-databricks-on-aws.md]
- The governed tag (and tag value) used by a custom classifier cannot be changed after creation. To switch to a different tag, you must delete the classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]
- Custom classifiers apply to all catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled; per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]
- New and updated custom classifiers apply only to subsequent scans; existing scan results are not automatically reclassified. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) — The attribute system used in tag-based governance.
- [Data Classification](/concepts/data-classification.md) — The scanning engine that detects sensitive data.
- [Custom Classifiers](/concepts/custom-classifiers.md) — Extensions to built-in classification for organization-specific data.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md) — Dynamic masking policies that reference governed tags.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The framework that evaluates tag-based policies at query time.

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
