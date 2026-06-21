---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ebdcbe8b9a426d591791782ca1d404f6c88bab9246a213c64e8334b327389f3
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-governed-tags-for-data-classification
    - UCGTFDC
  citations:
    - file: data-classification-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Unity Catalog Governed Tags for Data Classification
description: The system of governed tags (PII, GDPR, HIPAA, DPDPA, etc.) that are automatically applied by the classification engine to detected sensitive columns.
tags:
  - tags
  - governance
  - classification
  - unity-catalog
timestamp: "2026-06-18T11:27:34.253Z"
---

# Unity Catalog Governed Tags for Data Classification

**Unity Catalog Governed Tags for Data Classification** are a set of predefined, system-managed tags in [Unity Catalog](/concepts/unity-catalog.md) that mark specific data types (e.g., email addresses, phone numbers, personal names) for automated detection, governance, and access control. These tags are created and maintained by Databricks and serve as the foundation for [Data Classification](/concepts/data-classification.md) in Unity Catalog, enabling the automatic identification and labeling of sensitive data across your [Metastore](/concepts/metastore.md). ^[data-classification-databricks-on-aws.md]

## Overview

Governed tags for data classification are a specialized subset of [Governed Tags](/concepts/governed-tags.md) that Databricks provides to classify sensitive data without requiring manual tag creation or maintenance. Unlike user-defined governed tags, which you create and manage yourself, data classification tags are predefined by Databricks and are automatically applied when you enable [Data Classification](/concepts/data-classification.md). They cover common sensitive data types such as names, email addresses, phone numbers, and credit card numbers. ^[data-classification-databricks-on-aws.md]

## How Governed Tags Enable Data Classification

When you enable [Data Classification](/concepts/data-classification.md) for a catalog, the classification engine uses an AI agent to automatically scan tables in that catalog and apply the appropriate classification tags. The engine detects data that matches the criteria for each classification tag, such as columns containing email addresses or phone numbers. When the engine identifies a match, it applies the corresponding governed tag to the column. ^[data-classification-databricks-on-aws.md]

The classification engine relies on intelligent scanning to determine when to scan a table. New tables and columns in a catalog are typically scanned within 24 hours of being created. Subsequent scans are incremental and optimized to minimize cost. ^[data-classification-databricks-on-aws.md]

## Supported Classification Tags

For a full list of supported tags, see [Supported classification tags](/concepts/classification-tags-and-governed-tags-system.md). The tags are organized into the following categories: ^[data-classification-databricks-on-aws.md]

### [Global Tags](/concepts/global-tags.md)

Tags available across all Databricks regions:

| Tag Name | Description |
|----------|-------------|
| `class.email_address` | Email addresses |
| `class.phone_number` | Phone numbers |
| `class.person_name` | Personal names |
| `class.credit_card` | Credit card numbers |
| `class.ip_address` | IP addresses |
| `class.street_address` | Street addresses |
| `class.ssn` | Social Security Numbers |
| `class.drivers_license` | Driver's license numbers |
| `class.date_of_birth` | Dates of birth |
| `class.gender` | Gender information |
| `class.age` | Age information |
| `class.account_number` | Account numbers |
| `class.password` | Passwords |
| `class.tax_id` | Tax identification numbers |
| `class.passport_number` | Passport numbers |
| `class.bank_routing_number` | Bank routing numbers |
| `class.medical_record_number` | Medical record numbers |
| `class.health_insurance_id` | Health insurance IDs |
| `class.health_condition` | Health conditions |

### [Regional Tags](/concepts/regional-tags.md)

Tags specific to certain geographic or regulatory regions:

| Tag Name | Description |
|----------|-------------|
| `class.uk_nino` | UK National Insurance Number |
| `class.uk_driving_licence` | UK Driving Licence Number |
| `class.uk_passport` | UK Passport Number |
| `class.eu_national_id` | EU National ID |
| `class.in_aadhaar` | Indian Aadhaar number |
| `class.in_pan` | Indian Permanent Account Number |
| `class.jp_my_number` | Japanese My Number |
| `class.kr_resident_id` | Korean Resident Registration Number |
| `class.br_cpf` | Brazilian CPF |
| `class.br_cnpj` | Brazilian CNPJ |
| `class.mx_curp` | Mexican CURP |
| `class.mx_rfc` | Mexican RFC |

### Compliance Framework Tags

Tags organized by regulatory frameworks:

| Framework | Tag |
|-----------|-----|
| PII | `class.pii` |
| PII | `class.pii_sensitive` |
| GDPR | `class.gdpr_personal_data` |
| GDPR | `class.gdpr_special_category` |
| HIPAA | `class.hipaa_protected` |
| HIPAA | `class.hipaa_electronic` |
| DPDPA | `class.dpdp_personal_data` |
| DPDPA | `class.dpdp_sensitive_personal_data` |
| CCPA | `class.ccpa_personal_information` |
| PCI DSS | `class.pci_dss` |

## How Tags Are Applied

When you enable automatic tagging for a classification tag, all existing and future detections of that classification are automatically tagged with the corresponding governed tag. Automatic tagging can be configured at two levels: ^[data-classification-databricks-on-aws.md]

### [Metastore](/concepts/metastore.md) Level

- **Requires**: [Metastore](/concepts/metastore.md) admin privileges and `ASSIGN` on the tag being applied.
- **Scope**: Applies to all catalogs in the [Metastore](/concepts/metastore.md).
- **Effect**: Enables or disables tagging across all catalogs at once.

### Catalog Level

- **Requires**: `USE CATALOG`, `APPLY TAG` on the catalog, and `ASSIGN` on the tag being applied.
- **Scope**: Applies to the current catalog only.
- **States**:
  - **Default (inherited)**: The catalog inherits the tagging setting from the [Metastore](/concepts/metastore.md) level.
  - **Active**: Tagging is explicitly enabled for this catalog, regardless of the [Metastore](/concepts/metastore.md) level.
  - **Inactive**: Tagging is explicitly disabled for this catalog, regardless of the [Metastore](/concepts/metastore.md) level.

Catalog-level settings take precedence over the metastore-level setting. When tagging is disabled, no future tags are applied, but existing tags are not removed. ^[data-classification-databricks-on-aws.md]

> **Note**: When you enable automatic tagging, tags are not backfilled immediately. They will be populated in the next scan, which should take effect within 24 hours. Subsequent classifications will be tagged immediately. ^[data-classification-databricks-on-aws.md]

## Managing Permissions on Classification Tags

By default, only account admins have `MANAGE` and `ASSIGN` permissions on data classification system governed tags. Account admins can grant `MANAGE` and `ASSIGN` for individual governed tags to other users, service principals, or groups. See [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md). ^[data-classification-databricks-on-aws.md]

## Viewing Classification Results and Tag Status

When you view classification results, the UI shows for each classification type: ^[data-classification-databricks-on-aws.md]

- **Detected columns**: The number of columns where the classification was detected.
- **Auto-tagging**: The tagging status for that classification — **Active** or **Inactive**. In the [Metastore](/concepts/metastore.md) view, **Partially Active** indicates tagging is enabled in some but not all catalogs.
- **User Access (last 7d)**: The number of distinct users who accessed unmasked vs. masked data of that classification over the last 7 days.

## Using Tags for Governance

Governed tags for data classification are the foundation for [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) in Unity Catalog. You can use them to create ABAC policies that automatically mask or restrict access to classified columns. Databricks recommends using ABAC policies to create governance controls based on data classification results. ^[data-classification-databricks-on-aws.md]

### Creating Row Filter and Column Mask Policies

You can use classification tags in [row filter](/concepts/row-filter-policies.md) and column mask policies to restrict access to sensitive data based on the classification tag applied to the column. For example, you can create a policy that masks any column with the `class.email_address` or `class.phone_number` tag. ^[data-classification-databricks-on-aws.md]

### Creating ABAC GRANT Policies

Classification tags can also be used in [ABAC GRANT Policies](/concepts/abac-grant-policies.md) to grant `EXECUTE` on models based on the tags applied to the model's catalog, schema, or the model itself. For example, a GRANT policy can grant access to models that have a specific classification tag. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Requirements

To use governed tags for data classification: ^[data-classification-databricks-on-aws.md]

- Your workspace must have [serverless compute](/concepts/serverless-gpu-compute.md) available (enabled by default in workspaces with Unity Catalog).
- To enable data classification, you must own the catalog or have `USE CATALOG` and `MANAGE` privileges on it.
- To enable automatic tagging for a catalog, you must have `USE CATALOG` on the catalog, `APPLY TAG` on the catalog, and `ASSIGN` on the tag being applied.

## Benefits of Using Governed Tags for Data Classification

Using governed tags for data classification provides several key benefits: ^[data-classification-databricks-on-aws.md]

- **Automated discovery**: The AI agent automatically detects and tags sensitive data across your catalog without manual effort.
- **Incremental scanning**: The system intelligently determines when to scan, optimizing for new and changed data.
- **Cost optimization**: Initial scans are more costly, but subsequent scans are incremental with lower costs.
- **Governance integration**: Tags integrate directly with ABAC policies for immediate access control.
- **Compliance support**: Predefined tags for major compliance frameworks (PII, GDPR, HIPAA, DPDPA, PCI DSS) simplify regulatory compliance.

## Audit Logging

Databricks logs all governed tag operations (assignments and deletions) in the `system.access.audit` system table. This enables monitoring and investigation of when governed tags are created, modified, or removed. Key logged actions include: ^[data-classification-databricks-on-aws.md]

- `createEntityTagAssignment`
- `deleteEntityTagAssignment`

## Exclusions and Corrections

If a classification is incorrect, you can exclude the detection from the review panel. Excluding a detection: ^[data-classification-databricks-on-aws.md]

- Removes any existing classification tag from that column.
- Prevents future scans from reapplying the tag to that column.
- Provides feedback that improves the accuracy of future classification results.

## Limitations

- Views and metric views are not supported. If the view is based on existing tables, Databricks recommends classifying the underlying tables to see if they contain sensitive data. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The automated system for identifying and tagging sensitive data
- [Governed Tags](/concepts/governed-tags.md) — The broader tag system for data governance in Unity Catalog
- [Supported classification tags](/concepts/classification-tags-and-governed-tags-system.md) — Full list of all classification tags
- ABAC policies — Attribute-based access control policies using governed tags
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that use tags to filter data rows
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that use tags to mask sensitive columns
- [GRANT policies](/concepts/grant-policies-beta.md) — ABAC policies that use tags to grant access dynamically
- [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md) — How to grant tag management permissions
- [Audit logging](/concepts/abac-policy-audit-logging.md) — Tracking tag and policy operations

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
