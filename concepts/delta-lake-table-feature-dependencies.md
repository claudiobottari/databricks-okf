---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e06b3c5331a6e865ee257dfaf46510f7c5c4a45a6e1da4d07a7b6d64fcf05b28
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-lake-table-feature-dependencies
    - DLTFD
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: Delta Lake Table Feature Dependencies
description: The concept that Delta Lake table features have dependency relationships where enabling a compatibility mode like IcebergCompatV1 requires certain features to be enabled and prohibits others.
tags:
  - delta-lake
  - table-features
  - databricks
timestamp: "2026-06-19T10:05:58.737Z"
---

# [Delta Lake Table](/concepts/delta-lake-table.md) Feature Dependencies

**Delta Lake Table Feature Dependencies** refer to the relationships between table features that determine which features can be enabled, disabled, or used together in a Delta table. Understanding these dependencies is essential when working with compatibility modes such as [IcebergCompatV1](/concepts/icebergcompatv.md) or when managing the feature set of a Delta table.

## Overview

Delta Lake tables support a variety of features (such as column mapping, deletion vectors, change data feed, and Iceberg compatibility) that can be enabled or disabled over time. Some features have dependencies on other features: a feature may require another feature to be enabled, or two features may be mutually incompatible and cannot both be enabled simultaneously. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

When operations violate these dependency rules, Delta Lake raises errors from the [`DELTA_ICEBERG_COMPAT_V1_VIOLATION`](./delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md) error class.

## Types of Feature Dependencies

### Required Features

Some features cannot function without other features being enabled. If a required feature is missing, Delta Lake will raise an error. For example, IcebergCompatV1 requires certain table features to be supported and enabled. Attempting to drop a feature that another enabled feature requires will result in a `DISABLING_REQUIRED_TABLE_FEATURE` error. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### Invalid Operations on Dependent Features

When a user attempts to perform an operation that violates a feature dependency, Delta Lake returns an error. For instance:

- **Disabling a required feature**: If you try to drop a feature that is required by another enabled feature (such as IcebergCompatV1), the operation fails. You must first disable the dependent feature before dropping its requirements. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]
- **Missing a required feature**: When enabling a feature that depends on other features, those dependencies must already be enabled on the table. A `MISSING_REQUIRED_TABLE_FEATURE` error is raised if a prerequisite feature is absent. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### Incompatible Features

Certain features are designed to be incompatible with each other. For example, IcebergCompatV1 may be incompatible with specific other table features. Attempting to enable both will produce an `INCOMPATIBLE_TABLE_FEATURE` error. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### Table Property Constraints

Some compatibility modes impose constraints on table properties. IcebergCompatV1 requires certain table properties to be set to specific values. If the property is missing or has a different value, a `WRONG_REQUIRED_TABLE_PROPERTY` error is returned, detailing which property must be changed and what value is required. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Resolving Feature Dependency Violations

When a feature dependency violation occurs, the recommended approach is:

1. Identify the conflicting feature or missing dependency from the error message.
2. If a feature is incompatible, disable the incompatible feature before enabling the new one, or choose an alternative feature combination.
3. If a required feature is missing, enable the prerequisite feature first.
4. If a required feature cannot be disabled because another feature depends on it, disable the dependent feature first before removing the requirement.

For [IcebergCompatV1](/concepts/icebergcompatv.md)-related violations, disabling IcebergCompatV1 is often the first step before making changes to its dependent features. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Concepts

- Delta Lake Table Features — The complete set of features available for Delta tables
- [IcebergCompatV1](/concepts/icebergcompatv.md) — A compatibility mode with specific feature dependencies
- Delta Table Properties — Configuration properties that may be constrained by features
- [Column Mapping](/concepts/delta-table-column-mapping.md) — A feature that may have dependencies with other features
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — A feature that may interact with compatibility modes

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
