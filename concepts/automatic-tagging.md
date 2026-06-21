---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 644fbe0fef0c7e5004f0bfb7d3b9a5ea7b1f12899175084c5d52c92d871ba2d3
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-tagging
    - automatic-tagging-in-data-classification
    - ATIDC
    - Automatic Data Classification
    - automatic-tagging-with-governed-tags
    - ATWGT
  citations:
    - file: data-classification-databricks-on-aws.md
title: Automatic Tagging
description: A mechanism in Databricks Data Classification that automatically applies governed tags to detected columns, configurable at both metastore and catalog levels with inheritance semantics.
tags:
  - data-governance
  - tagging
  - unity-catalog
timestamp: "2026-06-19T14:40:21.782Z"
---

# Automatic Tagging

**Automatic Tagging** is a feature of [Data Classification](/concepts/data-classification.md) in [Unity Catalog](/concepts/unity-catalog.md) that automatically applies governed tags to columns identified as containing sensitive data. When enabled, every existing and future detection of a specified classification type is tagged, enabling downstream governance controls such as [Attribute-based access control](/concepts/attribute-based-access-control-abac.md) policies.^[data-classification-databricks-on-aws.md]

## Overview

After the classification engine detects sensitive data in a column (e.g., personal information, financial data), automatic tagging ensures that a corresponding governed tag is applied without manual intervention. This allows data teams to enforce access policies based on tags, such as masking columns tagged with `class.email_address` for unauthorized users. The feature is part of the broader Databricks Data Classification system, which uses an AI agent to scan tables in Unity Catalog.^[data-classification-databricks-on-aws.md]

## Configuration Levels

Automatic tagging can be configured at two levels: the **metastore level** and the **catalog level**. Catalog-level settings take precedence over the metastore-level setting.^[data-classification-databricks-on-aws.md]

| Level | Description | Required Permissions |
|-------|-------------|----------------------|
| [Metastore](/concepts/metastore.md) | Enable or disable automatic tagging across all catalogs at once. | [Metastore](/concepts/metastore.md) admin + `ASSIGN` on the tag being applied. |
| Catalog | Enable or disable for a specific catalog only; overrides the [Metastore](/concepts/metastore.md) setting. | `USE CATALOG`, `APPLY TAG` on the catalog, and `ASSIGN` on the tag. |

At the catalog level, automatic tagging has three states:

- **Default (inherited)**: The catalog inherits the tagging setting from the [Metastore](/concepts/metastore.md) level.
- **Active**: Tagging is explicitly enabled for this catalog, regardless of the [Metastore](/concepts/metastore.md) setting.
- **Inactive**: Tagging is explicitly disabled for this catalog, regardless of the [Metastore](/concepts/metastore.md) setting.

When tagging is disabled, no future tags are applied, but existing tags are not removed.^[data-classification-databricks-on-aws.md]

## Timing and Backfill

When automatic tagging is first enabled, tags are **not backfilled immediately**. The initial tagging occurs during the next scheduled scan, typically within 24 hours. After that, subsequent classifications are tagged immediately as they are detected.^[data-classification-databricks-on-aws.md]

## Viewing Auto-Tagging Status

On the Data Classification results page, each classification type shows an **Auto-tagging** column with one of three statuses: **Active**, **Inactive**, or **Partially Active** (when tagging is enabled in some but not all catalogs). This allows administrators to monitor which sensitive data categories are being automatically tagged across the [Metastore](/concepts/metastore.md).^[data-classification-databricks-on-aws.md]

## Excluding Detections

If a classification detection is incorrect, users can exclude the individual column from detection via the review panel. Excluding a detection removes any existing classification tag from that column and prevents future scans from reapplying the tag. This provides feedback that improves the accuracy of future classifications.^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) – The AI-driven system that detects sensitive data and powers automatic tagging.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance catalog where automatic tagging is configured and applied.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – Policies that use tags to control data access.
- System tables – The `system.data_classification.results` table stores classification and tagging data.
- [Governed Tags](/concepts/governed-tags.md) – The tag objects used by automatic tagging, managed through permissions.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
