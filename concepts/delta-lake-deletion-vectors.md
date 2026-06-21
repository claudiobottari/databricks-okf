---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48ce38d856dfe56ecaf087b5ee89a103f8663e9c3ae78557ad4b6785da0d442b
  pageDirectory: concepts
  sources:
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-deletion-vectors
    - DLDV
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
title: Delta Lake Deletion Vectors
description: A Delta Lake feature that marks rows as logically deleted rather than physically removing them, enabling efficient operations like MERGE and UPDATE without rewriting entire Parquet files.
tags:
  - delta-lake
  - data-management
  - optimization
timestamp: "2026-06-19T18:29:25.049Z"
---

# Delta Lake Deletion Vectors

**Delta Lake Deletion Vectors** are a storage optimization mechanism in [Delta Lake](/concepts/delta-lake.md) that enable efficient deletion of records from Parquet-based tables without rewriting entire data files. Deletion vectors provide a soft-delete capability by marking which rows in existing Parquet files should be considered deleted, allowing subsequent read operations to skip these records without physically modifying the underlying storage files. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Supported Table Types

Deletion vectors are only supported on Parquet-based Delta tables. The system enforces this restriction through the `PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE` validation check, which prevents the creation of persistent deletion vectors on tables using non-Parquet storage formats. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Compatibility Constraints

### Incremental Symlink Manifest Generation

[Symlink Manifest Generation](/concepts/symlink-manifest-generation.md) (incremental) is unsupported while deletion vectors are present in a table. The `EXISTING_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION` validation error occurs when attempting to generate symlink manifests on a table that already contains deletion vectors. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

Furthermore, persistent deletion vectors and incremental [Symlink Manifest Generation](/concepts/symlink-manifest-generation.md) are mutually exclusive (`PERSISTENT_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION`). This means you cannot simultaneously maintain both persistent deletion vectors and incremental symlink manifests on the same table. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Removing Deletion Vectors

To produce a version of a Delta table without deletion vectors, run the following command:

```sql
REORG TABLE <table> APPLY (PURGE)
```

This command physically rewrites the data files to eliminate deletion vectors from the table, enabling compatibility with features like symlink manifest generation that are incompatible with deletion vectors. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Deletion Vectors](/concepts/delta-lake-deletion-vectors.md) – The soft-delete mechanism for Parquet tables
- [Symlink Manifest Generation](/concepts/symlink-manifest-generation.md) – A manifest generation approach for Delta tables
- Table Properties Validation – Validation checks that enforce consistency rules on Delta tables
- [REORG TABLE](/concepts/reorg-table.md) – The command used to reorganize table data and purge deletion vectors
- Delta Lake Storage Optimization – Broader optimization techniques for Delta Lake storage

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
