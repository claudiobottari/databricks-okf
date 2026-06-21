---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a0652cec333bc0c93fb0045c56a89ba7c7003d89b611190291ed60033e1b541
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-requirement-for-delta-uniform
    - UCRFDU
    - unity-catalog-requirement-for-delta-uniform-iceberg-reads
    - UCRFDUIR
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Unity Catalog Requirement for Delta Uniform
description: Unity Catalog must be enabled to read Apache Iceberg tables via Delta Uniform; otherwise a UNITY_CATALOG_NOT_ENABLED error is raised.
tags:
  - databricks
  - unity-catalog
  - delta-lake
timestamp: "2026-06-19T15:08:39.667Z"
---

# Unity Catalog Requirement for Delta Uniform

**Unity Catalog Requirement for Delta Uniform** refers to the mandatory dependency that [Delta Uniform](/concepts/delta-uniform.md)—a feature enabling interoperability between Delta Lake and Apache Iceberg formats—must be used within a [Unity Catalog](/concepts/unity-catalog.md)-enabled environment. When attempting to use Delta Uniform capabilities outside of Unity Catalog, operations fail with specific error conditions. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Condition

When Delta Uniform operations are attempted in a workspace or [Metastore](/concepts/metastore.md) that does not have Unity Catalog enabled, the system returns the following error:

**SQLSTATE: KD00E** — Read Delta Uniform fails with the message: `Metadata conversion from <format> to Delta failed, <errorMessage>`. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### Specific Error: UNITY_CATALOG_NOT_ENABLED

The error condition `UNITY_CATALOG_NOT_ENABLED` provides the explicit message:

> Unity Catalog is required for Read Apache Iceberg with Delta Uniform.

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This error occurs when Delta Uniform attempts to read [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables, but Unity Catalog is not enabled for the [Metastore](/concepts/metastore.md) or workspace where the operation is being performed. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Affected Operations

The Unity Catalog requirement applies to the core Delta Uniform functionality for:

- **Reading Apache Iceberg tables** through Delta Uniform's metadata conversion layer
- **Creating Delta Uniform ingress tables** that bridge [Delta Lake](/concepts/delta-lake.md) and Iceberg formats

The `UNITY_CATALOG_NOT_ENABLED` error is one of several error types under the `DELTA_UNIFORM_INGRESS_VIOLATION` error class, which also includes errors related to missing delta log locations, non-uniform ingress tables, unsupported operations, and unexpected delta log locations. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Why Unity Catalog Is Required

Delta Uniform relies on Unity Catalog to:

1. **Manage metadata conversion** between Delta Lake and Iceberg formats
2. **Track table uniformity status** across the catalog
3. **Coordinate the ingress process** for creating and refreshing uniform tables

Without Unity Catalog, Delta Uniform lacks the necessary metadata infrastructure to maintain format compatibility and manage the conversion processes that enable cross-format reads. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Resolution

To resolve the `UNITY_CATALOG_NOT_ENABLED` error, enable Unity Catalog on your Databricks workspace and [Metastore](/concepts/metastore.md). Once Unity Catalog is properly configured, Delta Uniform operations can proceed normally. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The feature enabling Delta Lake and Apache Iceberg interoperability
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that Delta Uniform bridges with Delta Lake
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution required for Delta Uniform operations
- [Delta Lake](/concepts/delta-lake.md) — The storage layer foundation for Delta Uniform
- DELTA_UNIFORM_INGRESS_VIOLATION — The error class containing Unity Catalog requirement errors

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)
