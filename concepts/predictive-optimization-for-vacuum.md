---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e395434d92d56e0eeaa491a61b7f5fb9af5344fdc8cb43ad48019e41448f5c69
  pageDirectory: concepts
  sources:
    - vacuum-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - predictive-optimization-for-vacuum
    - POFV
  citations:
    - file: vacuum-databricks-on-aws.md
title: Predictive Optimization for VACUUM
description: When predictive optimization is enabled, Databricks automatically triggers VACUUM operations, making manual VACUUM commands unnecessary in most cases.
tags:
  - databricks
  - automation
  - optimization
timestamp: "2026-06-19T23:24:19.127Z"
---

# Predictive Optimization for VACUUM

**Predictive Optimization for VACUUM** is a feature on Databricks that automatically triggers the `VACUUM` operation on Delta tables and Apache Iceberg tables as part of the platform's optimization process. When enabled, it eliminates the need for manual `VACUUM` execution in most cases. ^[vacuum-databricks-on-aws.md]

## Overview

The `VACUUM` command removes unused files from a table directory, including data files that are no longer in the latest state of the transaction log and are older than a retention threshold. With predictive optimization, Databricks handles this cleanup automatically, ensuring tables remain optimized without requiring user intervention. ^[vacuum-databricks-on-aws.md]

## Supported Table Types

Predictive optimization for `VACUUM` applies to both Delta tables and Apache Iceberg tables. For both table types, the automatic triggering of `VACUUM` means users do not need to run the command manually in most scenarios. ^[vacuum-databricks-on-aws.md]

## Relationship to Manual VACUUM

If predictive optimization is enabled, Databricks automatically triggers the `VACUUM` operation as part of its optimization process. You don't need to run `VACUUM` manually in most cases. ^[vacuum-databricks-on-aws.md]

## Retention Considerations

The retention window for `VACUUM` is determined by the `delta.deletedFileRetentionDuration` table property, which defaults to 7 days. This means `VACUUM` removes data files that are no longer referenced by a Delta table version in the last 7 days. To retain data for a longer period — such as to support [time travel](/concepts/delta-lake-time-travel.md) for longer durations — set this table property to a higher value. ^[vacuum-databricks-on-aws.md]

Databricks strongly recommends setting a retention interval of at least 7 days. If the retention period is too short, `VACUUM` could delete uncommitted files from long-running jobs before those jobs complete. ^[vacuum-databricks-on-aws.md]

## Related Concepts

- VACUUM — The SQL command for removing unused files from table directories
- Predictive Optimization — The broader optimization framework that automates table maintenance
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that manages table transactions and file versions
- [Time Travel](/concepts/delta-lake-time-travel.md) — The ability to query previous versions of a Delta table, which is affected by `VACUUM` operations
- Table Properties — Configuration settings like `delta.deletedFileRetentionDuration` that control retention behavior

## Sources

- vacuum-databricks-on-aws.md

# Citations

1. [vacuum-databricks-on-aws.md](/references/vacuum-databricks-on-aws-9d87fed3.md)
