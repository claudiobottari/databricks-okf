---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1813b33cc80fdf45358541e47b1393a889228471bfc3bbd595bbdf3a0429017f
  pageDirectory: concepts
  sources:
    - supported-classification-tags-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - global-tags
  citations:
    - file: supported-classification-tags-databricks-on-aws.md
title: Global Tags
description: Classification tags that detect sensitive data regardless of geographic origin and are available in all Databricks workspace regions.
tags:
  - data-governance
  - classification
  - global
  - databricks
timestamp: "2026-06-19T23:05:51.823Z"
---

---

title: Global Tags
summary: [System Tags](/concepts/system-tags.md) that detect sensitive data regardless of geographic origin and are available in all Databricks workspace regions.
sources:
  - supported-classification-tags-databricks-on-aws.md
kind: concept
---

# Global Tags

**Global Tags** are a category of [System Tags](/concepts/system-tags.md) used in Databricks [Data Classification](/concepts/data-classification.md) that detect sensitive data irrespective of geographic origin. Unlike [Regional Tags](/concepts/regional-tags.md), which only apply in specific cloud regions, global tags are available in all Databricks workspace deployments. ^[supported-classification-tags-databricks-on-aws.md]

## Overview

[Data Classification](/concepts/data-classification.md) automatically analyzes column values and assigns [System Tags](/concepts/system-tags.md) to columns that match sensitive data patterns. The full set of supported classification tags is organized into two groups: **global tags** and **regional tags**. Global tags are designed to recognize data types that are universally considered sensitive, such as personally identifiable information (PII), without requiring region-specific patterns. ^[supported-classification-tags-databricks-on-aws.md]

## Characteristics

- **Region‑independent**: Global tags detect sensitive data regardless of the geographic origin of the data or the cloud region in which the workspace is deployed. ^[supported-classification-tags-databricks-on-aws.md]
- **Universally available**: They are available in all Databricks workspaces across all regions, in contrast to [Regional Tags](/concepts/regional-tags.md) that are restricted to specific regions. ^[supported-classification-tags-databricks-on-aws.md]

## Compliance Framework Mapping

Global tags are mapped to common regulatory compliance frameworks. The same tag may appear in multiple frameworks. Frameworks include:

- PII
- PCI DSS
- GDPR
- HIPAA
- GLBA
- DPDPA
- PIPEDA

For a full mapping of each tag to its corresponding compliance frameworks, see the [Compliance framework reference](/concepts/compliance-framework-reference-databricks.md). ^[supported-classification-tags-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) – The process that detects sensitive data and assigns [System Tags](/concepts/system-tags.md).
- [System Tags](/concepts/system-tags.md) – Managed governance tags that cannot be deleted or renamed.
- [Regional Tags](/concepts/regional-tags.md) – Tags that detect sensitive data specific to certain countries or regions.
- [Supported classification tags](/concepts/classification-tags-and-governed-tags-system.md) – The complete list of all classification tags.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer in which [Data Classification](/concepts/data-classification.md) operates.
- Personal data detection – The underlying pattern‑matching logic for tags.

## Sources

- supported-classification-tags-databricks-on-aws.md

# Citations

1. [supported-classification-tags-databricks-on-aws.md](/references/supported-classification-tags-databricks-on-aws-27a61e84.md)
