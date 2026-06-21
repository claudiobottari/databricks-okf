---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 98c2b5e896d952873ef3ac38dd6b0f9c7e8ae5ec7f25010ae7ce44197b6e08b1
  pageDirectory: concepts
  sources:
    - read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.91
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policies-on-shared-data
    - APOSD
  citations:
    - file: read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
title: ABAC Policies on Shared Data
description: Attribute-based access control (ABAC) policies such as row filters and column masks can be applied to shared tables, schemas, and catalogs but not to shared streaming tables or materialized views.
tags:
  - access-control
  - security
  - data-governance
timestamp: "2026-06-19T20:07:32.178Z"
---

# ABAC Policies on Shared Data

**Attribute-based access control (ABAC)** is a data governance model that provides flexible, scalable, and centralized access control across Databricks. Recipients of shared data can create ABAC policies on the tables, schemas, and catalogs that are created from a share. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Supported Objects

ABAC policies can be created for the following shared objects:

- Shared tables
- Shared schemas
- Shared catalogs (created from a share)

Materialized views are supported **with limitations**. These limitations are documented in the ABAC requirements. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Limitations

ABAC policies **cannot** be created on:

- Shared streaming tables
- Shared materialized views

This restriction applies regardless of the type of share. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Configuration

To configure ABAC policies, recipients use the same tools as for row filters and column masks. For detailed instructions, see [Create and manage row filter and column mask policies](/concepts/row-filter-and-column-mask-policies.md). ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The underlying access control model.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance platform that enforces ABAC policies.
- [Row Filters](/concepts/row-filter-policies.md) – A type of ABAC policy that restricts which rows are visible.
- Column Masks – A type of ABAC policy that obfuscates column values.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) – Shareable objects with ABAC limitations.
- Streaming Tables – Shareable objects on which ABAC policies cannot be created.
- [OpenSharing](/concepts/opensharing.md) – The data sharing protocol used to share the data.

## Sources

- read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md](/references/read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws-21150d4f.md)
