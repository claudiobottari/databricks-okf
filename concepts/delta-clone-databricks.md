---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 278564b2651da81b52899848cf445b060d89ed6785a7b9e8d7fbb7276515d6f8
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-clone-databricks
    - DC(
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: Delta Clone (Databricks)
description: A Databricks operation that creates a deep or shallow clone of a Delta table; certain source table features like indexes or partition evolution can cause incompatibility errors.
tags:
  - databricks
  - delta-lake
  - data-operations
timestamp: "2026-06-18T11:50:31.936Z"
---

# Delta Clone (Databricks)

**Delta Clone** is a Databricks operation that creates a copy (clone) of a table from a source format (such as Apache Iceberg, Apache Hive, or other external formats) into a [Delta Lake Table](/concepts/delta-lake-table.md). The cloning process transfers both the schema and data from the source to Delta format, enabling compatibility with Delta Lake features and optimizations.

## Error Condition: DELTA_CLONE_INCOMPATIBLE_SOURCE

The `DELTA_CLONE_INCOMPATIBLE_SOURCE` error (SQLSTATE: 0AKDC) occurs when a clone operation fails because the source table has a valid format but contains unsupported features that Delta cannot accommodate during the cloning process. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### Common Causes

The error is triggered by one of the following unsupported conditions in the source table:

#### HAS_INDEXES

The source table contains indexes that Delta cannot clone. The error message includes a list of the specific indexes present in the table. Resolution requires dropping the indexes from the source table before attempting the clone operation. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

#### ICEBERG_MISSING_PARTITION_SPECS

When cloning from an Apache Iceberg source, the source table may lack partition specifications. Delta requires partition spec information to properly organize data, so this condition prevents the clone from proceeding. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

#### ICEBERG_UNDERGONE_PARTITION_EVOLUTION

The source Apache Iceberg table has undergone partition evolution—a process where the partitioning scheme changed over the table's lifetime. Delta does not support cloning tables that have experienced partition evolution because the historical partition metadata is incompatible with Delta's format. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The native storage format for Databricks that supports ACID transactions and schema enforcement
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – An open table format for large analytic datasets that may require conversion to Delta
- [Table Cloning](/concepts/delta-table-cloning.md) – The process of creating a copy of a table's structure and data
- Database Migration – The broader context of moving data between storage formats
- Partition Evolution – The process where a table's partitioning scheme changes over time, causing compatibility issues with Delta cloning
- SQLSTATE – The SQL standard error classification system used for Databricks errors

## Best Practices

To avoid the `DELTA_CLONE_INCOMPATIBLE_SOURCE` error during cloning operations:

1. **Verify source compatibility** – Check that the source table does not have indexes, missing partition specs, or a history of partition evolution before starting the clone.
2. **Remove indexes** – If the error identifies `HAS_INDEXES`, drop the indexes from the source table before attempting the clone.
3. **Use compatible Iceberg tables** – Ensure the source Iceberg table has a consistent partition specification and has not undergone partition evolution.
4. **Consider alternative migration** – Use [COPY INTO](/concepts/copy-into-command.md) or MERGE patterns if the source format is not directly compatible with Delta cloning. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
