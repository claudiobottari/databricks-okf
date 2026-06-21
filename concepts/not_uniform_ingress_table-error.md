---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74c0d54d5314616973f5edbebfcf1e21abc81f2d81a6b01507df0ac667bb8f3e
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - not_uniform_ingress_table-error
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: NOT_UNIFORM_INGRESS_TABLE Error
description: An error raised when a table referenced in a Delta Uniform ingress operation is not actually configured as a uniform ingress table.
tags:
  - databricks
  - error-messages
  - delta-lake
timestamp: "2026-06-19T15:08:37.398Z"
---

# NOT_UNIFORM_INGRESS_TABLE Error

The **NOT_UNIFORM_INGRESS_TABLE** error is a sub‑error of the `DELTA_UNIFORM_INGRESS_VIOLATION` error class (SQLSTATE `KD00E`) that occurs when a read operation on a Delta Uniform table fails because the target table is not configured as a uniform ingress table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Details

The full error message is:

```
Table <tableName> is not a uniform ingress table.
```

This error is raised when a user attempts to read a Delta table using the [Delta Uniform](/concepts/delta-uniform.md) (Apache Iceberg ingress) protocol, but the table does not have uniform ingress enabled. The broader `DELTA_UNIFORM_INGRESS_VIOLATION` error class covers multiple conditions related to metadata conversion failures, including missing Delta log locations, unsupported operations, and missing Unity Catalog. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that enables reading Delta tables via Apache Iceberg format.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format used for the ingress protocol.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage layer for Delta Uniform tables.
- [Unity Catalog](/concepts/unity-catalog.md) – Required for reading Delta Uniform tables (as indicated by the related `UNITY_CATALOG_NOT_ENABLED` error). ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Troubleshooting

To resolve the error, ensure that the table is created or altered to support [Uniform Apache Iceberg Ingress](/concepts/uniform-apache-iceberg-ingress-table.md). Tables must be defined as uniform ingress tables to be readable via the Delta Uniform protocol. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)
