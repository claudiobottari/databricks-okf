---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8281ea6f1c9faf640a71961e093b83cab81a576d2104fdc88a24abb1499e58eb
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - uniform-ingress-table
    - UIT
    - Uniform Ingress
    - uniform ingress
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Uniform Ingress Table
description: A Delta table configured to act as an ingress point for Apache Iceberg data, supporting only CREATE and REFRESH operations
tags:
  - delta-lake
  - apache-iceberg
  - databricks
timestamp: "2026-06-18T11:56:51.769Z"
---

# Uniform Ingress Table

A **Uniform Ingress Table** is a [Delta Lake](/concepts/delta-lake.md) table that is configured to expose its metadata in the Apache Iceberg format, enabling Iceberg-compatible readers to read the table directly without converting the underlying data files. It is a core component of the **Delta Uniform** feature, which provides interoperability between Delta Lake and [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) by allowing Iceberg readers to consume Delta tables through a virtual Iceberg metadata layer. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Purpose and Behavior

Delta Uniform ingress tables are created to support use cases where external tools or workloads use the Iceberg read API to access data that is stored in Delta format. The table registers a synthetic Iceberg metadata location that points to the Delta table’s transaction log, translating Delta operations into Iceberg snapshots on the fly. Only `CREATE` and `REFRESH` operations are supported on Uniform Ingress Tables; other operations (such as direct metadata manipulation) are not permitted. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Prerequisites

A Unity Catalog [Metastore](/concepts/metastore.md) must be enabled on the workspace to use Delta Uniform ingress tables. The error [UNITY_CATALOG_NOT_ENABLED](/concepts/unity-catalog-enablement.md) is raised if Unity Catalog is absent. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Conditions

The DELTA_UNIFORM_INGRESS_VIOLATION error class groups several sub‑errors that can occur when a table is not properly set up for uniform ingress. The most relevant to this concept is:

- **NOT_UNIFORM_INGRESS_TABLE** – Returned when a read operation attempts to read a table as a Uniform Ingress Table but the table is not configured for uniform ingress. The error message states: `Table <tableName> is not a uniform ingress table.` ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

Other related sub‑errors include:
- DELTA_LOG_LOCATION_NOT_FOUND
- UNEXPECTED_DELTA_LOG_LOCATION
- OPERATION_NOT_SUPPORTED (when an unsupported operation is attempted on a Uniform Ingress Table)

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The open-source storage layer underlying this feature.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format made readable through the ingress mechanism.
- [Delta Uniform](/concepts/delta-uniform.md) – The broader interoperability feature that enables Iceberg reading of Delta tables.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer required for using Uniform Ingress Tables.
- DELTA_UNIFORM_INGRESS_VIOLATION – The error class covering ingress‑related failures.

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)
