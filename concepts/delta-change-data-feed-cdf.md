---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60dca9aa3a0b7ffd9cc5f1fe0a43a3b0f648a0e759ade3754b7e0d36dbe45182
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-change-data-feed-cdf
    - DCDF(
    - Change Data Feed (CDF)
    - Delta Change Data Feed
    - change data feed (CDF)
    - Change Data Feed
    - Change data feed
    - change data feed
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Delta Change Data Feed (CDF)
description: A Delta table feature that records row-level changes and is required for Triggered and Continuous online table sync modes.
tags:
  - databricks
  - delta-lake
  - change-data-capture
timestamp: "2026-06-19T09:53:33.443Z"
---

# Delta Change Data Feed (CDF)

**Delta Change Data Feed (CDF)** is a feature of [Delta Lake](/concepts/delta-lake.md) that tracks row-level changes made to a Delta table. When enabled, CDF creates a record of inserted, updated, and deleted rows, allowing downstream systems to process only the changed data rather than performing full table scans. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Overview

CDF captures the change history of a Delta table by recording each data modification event as an output row with metadata columns indicating the type of change. This enables incremental processing patterns such as streaming, change data capture (CDC), and [Online Tables](/concepts/online-tables.md) synchronization. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Use with Online Tables

CDF is a requirement for certain sync modes when creating online tables in Databricks. Online tables that use **Triggered** or **Continuous** sync mode must have CDF enabled on the source Delta table. Without CDF, only the **Snapshot** sync mode is available, which performs a full copy of the source data on each refresh. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Sync Modes and CDF Requirements

| Sync Mode | CDF Required | Behavior |
|-----------|-------------|----------|
| Snapshot | No | Performs full copy of source data on each refresh |
| Triggered | Yes | Syncs only changed rows since last update |
| Continuous | Yes | Continuously syncs changes as they occur |

^[databricks-online-tables-legacy-databricks-on-aws.md]

## Enabling CDF

CDF can be enabled on a Delta table using the `delta.enableChangeDataFeed` table property:

```sql
ALTER TABLE <table-name> SET TBLPROPERTIES (
   delta.enableChangeDataFeed = true
);
```

^[databricks-online-tables-legacy-databricks-on-aws.md]

Once enabled, CDF records all subsequent INSERT, UPDATE, and DELETE operations on the table. Existing data prior to enabling CDF is not captured. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Limitations

- CDF must be enabled before data modifications occur to capture changes. Enabling it retroactively does not capture past changes. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- Views and materialized views do not support CDF and therefore cannot use Triggered or Continuous sync modes for online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Troubleshooting CDF Issues

If an online table fails to select Triggered or Continuous sync mode, the likely cause is that the source table does not have CDF enabled. To resolve this:

1. Verify CDF is enabled on the source table by checking table properties.
2. Enable CDF using the `ALTER TABLE` command shown above.
3. If the source table is a View or materialized view, CDF is not supported and only Snapshot sync mode is available. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format that provides CDF capabilities
- [Online Tables](/concepts/online-tables.md) — Serverless read-only copies of Delta Tables that use CDF for incremental syncing
- Change Data Capture (CDC) — The broader pattern of capturing and propagating data changes
- Delta Table Properties — Configuration options for Delta tables including CDF settings

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
