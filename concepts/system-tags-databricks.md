---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b3f3d374de29ff76cbb999a69e40dbbbc3203642e657d52dfb1e4fb960645335
  pageDirectory: concepts
  sources:
    - supported-classification-tags-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - system-tags-databricks
    - ST(
    - System Tables (Databricks)
    - System Tables in Databricks
  citations:
    - file: supported-classification-tags-databricks-on-aws.md
title: System Tags (Databricks)
description: Tags automatically assigned by the Databricks system to columns when sensitive data is detected, such as those indicating PII or compliance-related data.
tags:
  - data-governance
  - unity-catalog
  - tags
  - databricks
timestamp: "2026-06-19T23:05:47.302Z"
---

## [System Tags](/concepts/system-tags.md) (Databricks)

**System Tags** are metadata tags assigned by [Data Classification](/concepts/data-classification.md) after it detects sensitive data in [Unity Catalog](/concepts/unity-catalog.md) columns. These tags are system-governed — meaning they are managed by Databricks and cannot be manually created or deleted by users. [Data Classification](/concepts/data-classification.md) automatically applies the appropriate system tag to every column that matches a known sensitive-data pattern, enabling compliance monitoring and policy enforcement. ^[supported-classification-tags-databricks-on-aws.md]

### Process

[Data Classification Scans](/concepts/data-classification-scans.md) table schemas for patterns that match predefined sensitive-data types. When a match is found, the system writes a system tag (also referred to as a *system-governed tag*) on the corresponding column. The tags are then visible in the [Unity Catalog](/concepts/unity-catalog.md) schema browser and can be used for auditing, attribute-based access control, or integration with external compliance tools. ^[supported-classification-tags-databricks-on-aws.md]

### Compliance framework mapping

Each system tag can be relevant to one or more regulatory compliance frameworks. The following frameworks are explicitly listed in the Databricks documentation:

- Personally Identifiable Information (PII)
- PCI DSS (Payment Card Industry Data Security Standard)
- GDPR (General Data Protection Regulation)
- HIPAA (Health Insurance Portability and Accountability Act)
- GLBA (Gramm‑Leach‑Bliley Act)
- DPDPA (Digital Personal Data Protection Act)
- PIPEDA (Personal Information Protection and Electronic Documents Act)

A single tag may appear in multiple framework mappings. For example, a tag that detects a person’s full name is relevant to both PII and GDPR. ^[supported-classification-tags-databricks-on-aws.md]

### Global vs. [Regional Tags](/concepts/regional-tags.md)

[System Tags](/concepts/system-tags.md) are organized into two categories:

| Category | Description |
|---|---|
| **Global tags** | Detect sensitive data **regardless of geographic origin**. Available in all Databricks workspaces across all cloud regions. |
| **Regional tags** | Detect sensitive data **specific to a particular country or region**. With the exception of United States tags, [Regional Tags](/concepts/regional-tags.md) are only available in workspaces deployed in the corresponding region. |

[Global Tags](/concepts/global-tags.md) are applied to patterns that are universal (e.g., email addresses, credit‑card numbers). [Regional Tags](/concepts/regional-tags.md) are tailored to national identifiers, such as tax IDs, national ID numbers, or passport formats of a specific country. ^[supported-classification-tags-databricks-on-aws.md]

### Regional tag availability

The following regions have dedicated [Regional Tags](/concepts/regional-tags.md). United States tags are an exception — they are available **in all Databricks workspaces**, regardless of deployment region. Tags for other regions are only available in workspaces that are physically deployed in that region.

- United States (available in all regions)
- United Kingdom
- Germany
- Australia
- Brazil
- India
- Canada

^[supported-classification-tags-databricks-on-aws.md]

### Related concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) where [System Tags](/concepts/system-tags.md) are stored and managed.
- [Data Classification](/concepts/data-classification.md) – The feature that automatically detects sensitive data and assigns [System Tags](/concepts/system-tags.md).
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – A policy mechanism that can use [System Tags](/concepts/system-tags.md) to restrict data access.
- [Sensitive Data Discovery](/concepts/admin-side-data-discovery.md) – The underlying process that identifies patterns matching system-tag definitions.

### Sources

- supported-classification-tags-databricks-on-aws.md

# Citations

1. [supported-classification-tags-databricks-on-aws.md](/references/supported-classification-tags-databricks-on-aws-27a61e84.md)
