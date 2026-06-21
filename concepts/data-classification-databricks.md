---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6cd5f1207ade5f1caf8acb92b272324bce0532e3670caf2c294ffab48655fbc6
  pageDirectory: concepts
  sources:
    - supported-classification-tags-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-classification-databricks
    - DC(
    - Data Classification#Limitations|Data Classification limitations
  citations:
    - file: supported-classification-tags-databricks-on-aws.md
title: Data Classification (Databricks)
description: A Databricks feature that detects sensitive data in tables and automatically assigns system tags to matching columns.
tags:
  - data-governance
  - unity-catalog
  - security
  - databricks
timestamp: "2026-06-19T23:05:41.427Z"
---

# [Data Classification](/concepts/data-classification.md) (Databricks)

**Data Classification** is a feature in Databricks that detects sensitive data and assigns [System Tags](/concepts/system-tags.md) to matching columns in tables managed by [Unity Catalog](/concepts/unity-catalog.md). The tags are organized into two categories: **global tags**, which apply across all cloud regions, and **regional tags**, which detect data specific to certain countries or regions. For a complete list of supported tags, see the official documentation. ^[supported-classification-tags-databricks-on-aws.md]

## Compliance Framework Reference[​](#compliance-framework-reference)

The classification tags are mapped to common regulatory frameworks. A single tag may appear in more than one framework. The supported frameworks include:

- PII (Personally Identifiable Information)
- PCI DSS
- GDPR
- HIPAA
- GLBA
- DPDPA
- PIPEDA

The mapping tables in the source documentation show which tags are relevant to each framework. ^[supported-classification-tags-databricks-on-aws.md]

## [Global Tags](/concepts/global-tags.md)[​](#global-tags)

[Global Tags](/concepts/global-tags.md) detect sensitive data regardless of geographic origin. They are available in all Databricks workspaces across every region. These tags cover categories such as personal identifiers, financial information, and health data that are recognized globally. ^[supported-classification-tags-databricks-on-aws.md]

## [Regional Tags](/concepts/regional-tags.md)[​](#regional-tags)

[Regional Tags](/concepts/regional-tags.md) detect sensitive data that is specific to particular countries or regions. With the exception of United States tags—which are available in all regions—regional tags are only available in Databricks workspaces deployed in the corresponding region. The supported regional tag sets are:

- United States
- United Kingdom
- Germany
- Australia
- Brazil
- India
- Canada

These tags help organizations comply with local data protection regulations by identifying data elements that are defined as sensitive under the laws of that jurisdiction. ^[supported-classification-tags-databricks-on-aws.md]

## Related Concepts

- [System Tags](/concepts/system-tags.md) – Tags managed by the system that cannot be manually created or deleted.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance catalog that hosts classification tags.
- Data Governance – Broader topic covering classification, lineage, and access control.
- [Compliance frameworks](/concepts/compliance-framework-reference-databricks.md) – Regulatory standards such as GDPR, HIPAA, and PCI DSS.

## Sources

- supported-classification-tags-databricks-on-aws.md

# Citations

1. [supported-classification-tags-databricks-on-aws.md](/references/supported-classification-tags-databricks-on-aws-27a61e84.md)
