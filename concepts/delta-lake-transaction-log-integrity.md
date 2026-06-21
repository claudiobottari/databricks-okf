---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 279c61cb65de30f6e89a4e2aaec3feaf80195875b2a7201a1b0ecb74a62a7d06
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-transaction-log-integrity
    - DLTLI
    - Transaction log integrity
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Delta Lake Transaction Log Integrity
description: Delta Lake uses a transaction log to commit changes atomically; users must never manually modify, add, or delete Parquet data files directly as it can cause data loss or corruption.
tags:
  - delta-lake
  - transaction-log
  - data-integrity
timestamp: "2026-06-18T14:32:02.267Z"
---

Here is the wiki page for "Delta Lake Transaction Log Integrity".

---

## Delta Lake Transaction Log Integrity

**Delta Lake Transaction Log Integrity** refers to the guarantees and mechanisms that ensure all changes committed to a [Delta Lake Table](/concepts/delta-lake-table.md) are recorded atomically, consistently, and accurately in the table’s transaction log. This integrity is foundational to Delta Lake’s ability to provide ACID transactions on data lakes.

## Core Principle

Delta Lake uses a transaction log to commit changes to a table atomically. You should never manually modify, add, or delete Parquet data files in a [Delta Lake Table](/concepts/delta-lake-table.md), as this can lead to data loss or table corruption. The transaction log is the single source of truth for the state of a [Delta Lake Table](/concepts/delta-lake-table.md), and bypassing it breaks the integrity of the table.^[best-practices-delta-lake-databricks-on-aws.md]

## Best Practices for Maintaining Integrity

### Avoid Manual Operations on Data Files

Delta Lake handles all data management operations automatically through its transaction log. The following operations should never be performed manually:

- **Direct file modification**: Do not directly modify, add, or delete Parquet data files in a [Delta Lake Table](/concepts/delta-lake-table.md).^[best-practices-delta-lake-databricks-on-aws.md]
- **Manual partition management**: Delta Lake automatically tracks the set of partitions present in a table and updates the list as data is added or removed. As a result, there is no need to run `ALTER TABLE [ADD|DROP] PARTITION` or `MSCK`.^[best-practices-delta-lake-databricks-on-aws.md]
- **Direct partition reading**: Avoid reading partitions directly (e.g., `spark.read.format("parquet").load("/data/date=2017-01-01")`). Instead, use a `WHERE` clause for data skipping, such as `spark.read.table("<table-name>").where("date = '2017-01-01'")`.^[best-practices-delta-lake-databricks-on-aws.md]

### Use `CREATE OR REPLACE TABLE` for Table Recreation

When deleting and recreating a table in the same location, you should always use a `CREATE OR REPLACE TABLE` statement. This ensures the transaction log properly tracks the table lifecycle.^[best-practices-delta-lake-databricks-on-aws.md]

### Do Not Manually Refresh

Delta Lake tables always return the most up-to-date information, so there is no need to call `REFRESH TABLE` manually after changes.^[best-practices-delta-lake-databricks-on-aws.md]

## File Compaction and Transaction Integrity

Running `OPTIMIZE` to compact small files does not remove the old files. To remove old files after compaction, you must run the `VACUUM` command. Both operations are managed through the transaction log, preserving integrity.^[best-practices-delta-lake-databricks-on-aws.md]

## Avoiding Conflicts During Merge Operations

Maintaining transaction log integrity requires careful management of concurrent writes, especially with Delta Lake MERGE operations. To reduce the chance of conflicts:

- Reduce the search space for matches by adding known constraints in the match condition (e.g., specifying partition columns like `date` and `country`).^[best-practices-delta-lake-databricks-on-aws.md]
- Compact small files into larger files to improve search throughput and reduce conflict windows.^[best-practices-delta-lake-databricks-on-aws.md]

## Remove Legacy Configurations

Legacy Delta configurations can prevent new optimizations and default values from being applied. Databricks recommends removing most explicit legacy Delta configurations from Spark configurations and table properties when upgrading to a new Databricks Runtime version to maintain compatibility and integrity.^[best-practices-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that provides ACID transactions
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The core component that ensures transactional integrity
- Delta Lake MERGE — Operation that benefits from proper performance tuning
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) — Recommended table type for Delta Lake workloads
- Predictive Optimization — Service that automatically manages file compaction

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
