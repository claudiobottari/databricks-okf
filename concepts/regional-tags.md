---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c99bdc25d9c3e206a48642739fe956557fbeb220ec5a28eae990b7b60fcff53
  pageDirectory: concepts
  sources:
    - supported-classification-tags-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - regional-tags
  citations:
    - file: supported-classification-tags-databricks-on-aws.md
title: Regional Tags
description: Classification tags that detect sensitive data specific to certain countries or regions, available only in Databricks workspaces deployed in the corresponding region.
tags:
  - data-governance
  - classification
  - regional
  - databricks
timestamp: "2026-06-19T23:05:51.442Z"
---

# Regional Tags

**Regional tags** are a category of [Data Classification](/concepts/data-classification.md) [System Tags](/concepts/system-tags.md) that detect sensitive data specific to certain countries or regions. Unlike [Global Tags](/concepts/global-tags.md), which apply across all cloud regions, regional tags are generally available only in Databricks workspaces deployed in the corresponding geographic region. The sole exception is **United States** tags, which are available in all regions. ^[supported-classification-tags-databricks-on-aws.md]

## Availability by Region

Regional tags are provided for the following countries or regions:

- United States (available in all Databricks workspaces)
- United Kingdom
- Germany
- Australia
- Brazil
- India
- Canada

With the exception of United States tags, each set of regional tags is only available when the Databricks workspace is deployed in that specific region. ^[supported-classification-tags-databricks-on-aws.md]

## Relationship to [Data Classification](/concepts/data-classification.md)

When [Data Classification](/concepts/data-classification.md) scans a table, it automatically detects sensitive data and assigns regional tags to matching columns, along with [Global Tags](/concepts/global-tags.md). Regional tags help organizations comply with jurisdiction-specific regulations (e.g., GDPR, DPDPA, PIPEDA) by identifying data that is subject to local data protection laws. ^[supported-classification-tags-databricks-on-aws.md]

## Related Concepts

- [Global Tags](/concepts/global-tags.md) – Tags that detect sensitive data regardless of geographic origin.
- [System Tags](/concepts/system-tags.md) – Tags automatically managed by Databricks.
- [Data Classification](/concepts/data-classification.md) – The process that detects sensitive data and assigns tags.
- [Compliance Framework Reference](/concepts/compliance-framework-reference-databricks.md) – Mapping of tags to regulatory frameworks such as GDPR, HIPAA, and PCI DSS.

## Sources

- supported-classification-tags-databricks-on-aws.md

# Citations

1. [supported-classification-tags-databricks-on-aws.md](/references/supported-classification-tags-databricks-on-aws-27a61e84.md)
