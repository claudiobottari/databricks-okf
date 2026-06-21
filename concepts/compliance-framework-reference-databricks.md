---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04403547e90d72b4c37439afa2fb012fba1c9904ccb2f2fffbb6c7f936cc41eb
  pageDirectory: concepts
  sources:
    - supported-classification-tags-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compliance-framework-reference-databricks
    - CFR(
    - Compliance Framework Reference
    - Compliance framework reference
    - Compliance Frameworks
    - Compliance frameworks
  citations:
    - file: supported-classification-tags-databricks-on-aws.md
title: Compliance Framework Reference (Databricks)
description: A mapping of classification tags to common regulatory compliance frameworks including PII, PCI DSS, GDPR, HIPAA, GLBA, DPDPA, and PIPEDA.
tags:
  - compliance
  - data-governance
  - regulation
  - databricks
timestamp: "2026-06-19T23:05:51.674Z"
---

# Compliance Framework Reference (Databricks)

The **Compliance Framework Reference** for Databricks [Data Classification](/concepts/data-classification.md) maps [System Tags](/concepts/system-tags.md) to common regulatory frameworks. [Data Classification](/concepts/data-classification.md) detects sensitive data and assigns [System Tags](/concepts/system-tags.md) to matching columns, and the compliance framework reference shows which tags are relevant to each regulatory standard. ^[supported-classification-tags-databricks-on-aws.md]

## Supported Regulatory Frameworks

The following compliance frameworks are supported by Databricks [Data Classification](/concepts/data-classification.md) tags:

- **PII** — Personally Identifiable Information
- **PCI DSS** — Payment Card Industry Data Security Standard
- **GDPR** — General Data Protection Regulation
- **HIPAA** — Health Insurance Portability and Accountability Act
- **GLBA** — Gramm-Leach-Bliley Act
- **DPDPA** — Digital Personal Data Protection Act
- **PIPEDA** — Personal Information Protection and Electronic Documents Act

A single tag may appear in more than one framework. ^[supported-classification-tags-databricks-on-aws.md]

## Tag Categories

### [Global Tags](/concepts/global-tags.md)

[Global Tags](/concepts/global-tags.md) detect sensitive data regardless of geographic origin. These tags are available in Databricks workspaces deployed in **all regions**. ^[supported-classification-tags-databricks-on-aws.md]

### [Regional Tags](/concepts/regional-tags.md)

[Regional Tags](/concepts/regional-tags.md) detect sensitive data specific to certain countries or regions. With the exception of United States tags (which are available in all regions), [Regional Tags](/concepts/regional-tags.md) are only available in Databricks workspaces deployed in the corresponding region. ^[supported-classification-tags-databricks-on-aws.md]

The following regional tag sets are available:

- **United States** — Available in all regions
- **United Kingdom** — Available in UK-deployed workspaces
- **Germany** — Available in Germany-deployed workspaces
- **Australia** — Available in Australia-deployed workspaces
- **Brazil** — Available in Brazil-deployed workspaces
- **India** — Available in India-deployed workspaces
- **Canada** — Available in Canada-deployed workspaces

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The system that detects sensitive data and assigns tags
- [System Tags](/concepts/system-tags.md) — [Governed Tags](/concepts/governed-tags.md) automatically assigned by Databricks
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that manages classification tags
- Data Governance — Overall framework for managing data access and compliance

## Sources

- supported-classification-tags-databricks-on-aws.md

# Citations

1. [supported-classification-tags-databricks-on-aws.md](/references/supported-classification-tags-databricks-on-aws-27a61e84.md)
