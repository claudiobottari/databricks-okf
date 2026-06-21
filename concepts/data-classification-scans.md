---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bca739aa2a8f08f16f756efa31df53ad87ad740d0754f9449563fab573196184
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - data-classification-scans
    - DCS
    - Data Classification Expenses
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Data Classification Scans
description: The recurring scan process in Unity Catalog that detects built-in and custom classifications; new or updated classifiers only apply to subsequent scans, and results typically appear within a few hours.
tags:
  - data-governance
  - unity-catalog
  - classification
timestamp: "2026-06-18T11:25:50.342Z"
---

# Data Classification Scans

**Data Classification Scans** are the periodic, automated processes by which Databricks Data Classification inspects the schemas and sample data of tables in Unity Catalog to identify and tag columns containing sensitive data types such as personally identifiable information (PII), financial data, or credentials.

## Overview

Data Classification in Unity Catalog scans tables to detect sensitive data using both built-in classifiers and custom classifiers. The system analyzes column names, schema metadata, and sample data from each table, then suggests or automatically applies [Governed Tags](/concepts/governed-tags.md) to columns that match known data patterns. ^[custom-classifiers-databricks-on-aws.md]

## How Scans Work

### Scan Scope

When Data Classification is enabled on a catalog, all tables within that catalog become subject to periodic scans. The scanning system evaluates columns against a set of detection rules derived from built-in classification tags and any [Custom Classifiers](/concepts/custom-classifiers.md) configured for the [Metastore](/concepts/metastore.md). ^[custom-classifiers-databricks-on-aws.md]

### Detection Methods

The scan process uses multiple detection techniques:

- **Schema analysis**: Column names and data types are evaluated for patterns matching known sensitive data categories.
- **Data sampling**: Representative samples of column values are examined against classification patterns.
- **Pattern matching**: Values are tested against regular expressions and pattern libraries for common sensitive data formats.

### Scan Frequency

Scans run periodically on a schedule managed by Databricks. New and updated classifiers produce results after the next scheduled scan completes. ^[custom-classifiers-databricks-on-aws.md]

## Built-in Classifiers

Databricks provides a library of built-in classifiers that detect common sensitive data types. These classifiers are automatically available when Data Classification is enabled. Built-in classifiers cover categories such as:

- Personally identifiable information (names, addresses, phone numbers)
- Financial data (credit card numbers, bank account numbers)
- Credentials (passwords, API keys, tokens)
- Healthcare data (medical record numbers, diagnosis codes)

## Custom Classifiers

Custom classifiers extend the built-in detection capabilities to identify organization-specific sensitive data. Each custom classifier references a [governed tag](/concepts/governed-tags.md) and uses between 1 and 10 example columns that contain representative values for the class. The system learns from these examples to generate detection rules for subsequent scans. ^[custom-classifiers-databricks-on-aws.md]

Custom classifiers apply to **all** catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled. Per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]

## Viewing Classification Results

Scan results are displayed in the Data Classification results page in Catalog Explorer. Results include:

- Catalog, schema, and table names
- Column names with detected classifications
- Applied [Governed Tags](/concepts/governed-tags.md)
- Confidence levels for each detection

## Automatic Tagging

Based on scan results, governed tags can be automatically applied to matching columns. When auto-tagging is configured, the system applies the appropriate governed tag value to each column that matches a classification rule. These tags then drive [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies such as [Row Filter Policies](/concepts/row-filter-policies.md), [Column Mask Policies](/concepts/column-mask-policies.md), or [ABAC GRANT Policy](/concepts/abac-grant-policy.md). ^[custom-classifiers-databricks-on-aws.md]

## Requirements

To use Data Classification scans, the following requirements must be met:

- Data Classification must be enabled on at least one catalog in the [Metastore](/concepts/metastore.md).
- The workspace must have serverless compute available (enabled by default in workspaces with Unity Catalog).
- To create or manage custom classifiers, the user must be a [Metastore](/concepts/metastore.md) admin.
- To create or edit a custom classifier, the user must have `ASSIGN` privileges on the governed tag the classifier uses.

## Limitations

- A maximum of 50 custom classifiers can be created per [Metastore](/concepts/metastore.md).
- Each custom classifier must reference between 1 and 10 example columns.
- Custom classifiers apply to all Data Classification-enabled catalogs — per-catalog or per-schema scoping is not supported.
- New and updated custom classifiers apply only to subsequent scans. Existing scan results are not automatically reclassified.
- Supported table types are limited to those that Unity Catalog can access.

## Suspended Classifiers

If rule generation or validation fails for a custom classifier, Databricks suspends it. A suspended classifier produces no new detections until the issue is resolved. Common causes of suspension include deleted example tables, unrepresentative example columns, or invalid governed tags. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- Data Classification Tags — The governed tags used for classifying sensitive data
- [Custom Classifiers](/concepts/custom-classifiers.md) — User-defined classifiers for organization-specific data types
- [Governed Tags](/concepts/governed-tags.md) — Tags that drive ABAC policies based on classification results
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Access control model that uses classification tags
- [ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md) — Logging of tag assignments and policy operations
- [Data Classification System Table](/concepts/data-classification-system-table.md) — The system table containing classification metadata

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
