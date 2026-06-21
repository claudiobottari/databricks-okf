---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5caa3cb074d78f85ed034be1027f05ab0de475f33b6894e23b47d42b112ce805
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-table-types-for-external-metadata-in-databricks
    - STTFEMID
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Supported Table Types for External Metadata in Databricks
description: Only streaming tables and materialized views are supported for external metadata operations; other table types trigger the TABLE_TYPE error.
tags:
  - databricks
  - delta-lake
  - table-types
timestamp: "2026-06-18T15:19:36.559Z"
---

Here is a clear and well-structured wiki page based solely on the provided source material.

---

## Supported Table Types for External Metadata in Databricks

**Supported Table Types for External Metadata in Databricks** refers to the specific table formats and configurations that can be used with the External Metadata feature in [Delta Lake](/concepts/delta-lake.md) on Databricks. The feature supports a limited set of table types, and unsupported types generate the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error.

## Overview

The External Metadata feature in Databricks supports only **streaming tables** and **materialized views**. When the feature encounters a table type that is not supported, it raises a `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error with the message: "`<tableType>` table, only streaming table and materialized view are supported." ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Unsupported Table Types

The following table types and configurations are **not** supported with External Metadata and will trigger the error:

- **Tables with Column Mask (CM) policies**: External Metadata does not support tables that have column masking policies applied. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **Tables with Row-level Security (RLS) policies**: External Metadata does not support tables that have row-level security policies applied. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Additional Unsupported Configurations

Beyond table types, the following related operations are also unsupported:

- **Column rename without column mapping**: If column mapping is not enabled when using an alias in a reconciliation query, the operation is not supported. The error message is: "Column mapping must be enabled to use an alias in the reconciliation query." ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **Unsupported projection**: The projection used in a reconciliation query is not supported if it takes a form not recognized by the system. The error message is: "The projection '`<projectionSql>`' of reconciliation query is not supported." ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [External Metadata](/concepts/external-metadata-api.md)
- Streaming Tables
- [Materialized Views](/concepts/materialized-views-in-databricks.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [Row-level Security](/concepts/row-level-security-rls-policies.md)
- [Column Mapping](/concepts/delta-table-column-mapping.md)

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
