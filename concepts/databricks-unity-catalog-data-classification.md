---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 96280ec9477318fab7bf0654ddbf37c94935858a40a00375bb64f2637a9d8db5
  pageDirectory: concepts
  sources:
    - supported-classification-tags-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-unity-catalog-data-classification
    - DUCDC
  citations:
    - file: supported-classification-tags-databricks-on-aws.md
title: Databricks Unity Catalog Data Classification
description: The data classification subsystem within Unity Catalog that uses system tags to identify and label sensitive data across tables.
tags:
  - unity-catalog
  - data-governance
  - classification
  - databricks
timestamp: "2026-06-19T23:06:02.355Z"
---

## Databricks [Unity Catalog](/concepts/unity-catalog.md) [Data Classification](/concepts/data-classification.md)

**Databricks [Unity Catalog](/concepts/unity-catalog.md) Data Classification** is a feature that automatically detects sensitive data within tables and assigns [System Tags](/concepts/system-tags.md) to matching columns. The classification process scans column names, data types, and optionally sample data to identify patterns that correspond to sensitive information types (such as personally identifiable information, financial data, or health records). The [System Tags](/concepts/system-tags.md) that are applied can then be used for fine-grained access control, audit logging, and compliance reporting. ^[supported-classification-tags-databricks-on-aws.md]

### Compliance Framework Reference

The classification tags are mapped to common regulatory frameworks, so a single tag may be relevant to more than one framework. The supported compliance frameworks include: ^[supported-classification-tags-databricks-on-aws.md]

- **PII** – Personally Identifiable Information
- **PCI DSS** – Payment Card Industry Data Security Standard
- **GDPR** – General Data Protection Regulation
- **HIPAA** – Health Insurance Portability and Accountability Act
- **GLBA** – Gramm-Leach-Bliley Act
- **DPDPA** – Digital Personal Data Protection Act (India)
- **PIPEDA** – Personal Information Protection and Electronic Documents Act (Canada)

Each tag type is designed to help organizations meet the requirements of one or more of these frameworks. ^[supported-classification-tags-databricks-on-aws.md]

### [Global Tags](/concepts/global-tags.md)

[Global Tags](/concepts/global-tags.md) detect sensitive data regardless of geographic origin. They are available in all Databricks workspaces across every cloud region. These tags apply to data types that are universally recognized as sensitive, such as credit card numbers, email addresses, or social security numbers (U.S. format). ^[supported-classification-tags-databricks-on-aws.md]

### [Regional Tags](/concepts/regional-tags.md)

[Regional Tags](/concepts/regional-tags.md) detect sensitive data that is specific to particular countries or regions. The following country-specific tags are available: ^[supported-classification-tags-databricks-on-aws.md]

- **United States** – Available in all regions (not restricted to U.S. workspaces)
- **United Kingdom**
- **Germany**
- **Australia**
- **Brazil**
- **India**
- **Canada**

Except for United States tags, [Regional Tags](/concepts/regional-tags.md) are only available in Databricks workspaces deployed in the corresponding region. For example, Brazil-specific tags are only available in workspaces hosted in Brazil. ^[supported-classification-tags-databricks-on-aws.md]

### Tagging Mechanism

The tags applied by [Data Classification](/concepts/data-classification.md) are [System Tags](/concepts/system-tags.md)—tags that are managed by the Databricks system rather than by users. They appear in [Unity Catalog](/concepts/unity-catalog.md) as attributes on columns that contain detected sensitive data. The classification engine matches column metadata and sample data against the built-in tag definitions to determine which tags to assign. ^[supported-classification-tags-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The underlying catalog that stores the classification tags as column attributes.
- [System Tags](/concepts/system-tags.md) – Managed tags that can be used for governance and access control.
- Data Governance – Broader discipline of managing data availability, usability, and security.
- [Compliance Frameworks](/concepts/compliance-framework-reference-databricks.md) – Regulatory standards that classification tags help satisfy.
- [Sensitive Data Discovery](/concepts/admin-side-data-discovery.md) – The process of automatically identifying sensitive data in datasets.

### Sources

- supported-classification-tags-databricks-on-aws.md

# Citations

1. [supported-classification-tags-databricks-on-aws.md](/references/supported-classification-tags-databricks-on-aws-27a61e84.md)
