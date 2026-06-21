---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d9ad9fb426000138e87ced64101b13858d1b79c5f55420df353fd1108a8e3d5
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-table-sync-modes
    - OTSM
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Table Sync Modes
description: "Three synchronization modes for updating online tables from source Delta tables: Snapshot (full copy), Triggered (manual/periodic incremental updates), and Continuous (real-time streaming sync)."
tags:
  - databricks
  - sync-modes
  - data-pipelines
  - online-tables
timestamp: "2026-06-19T18:14:20.342Z"
---

# Online Table Sync Modes

**Online Table Sync Modes** control how a [Databricks online table (legacy)](/concepts/databricks-online-tables.md) synchronizes data from its source [Delta Table](/concepts/delta-lake-table.md). The three available modes—Snapshot, Triggered, and Continuous—determine the frequency of updates, the method of data transfer, and the requirements on the source table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Snapshot

Snapshot mode performs a full copy of the source Delta table each time the sync runs. It does **not** require [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDF) to be enabled on the source table. This is the only mode supported for source tables that are [OpenSharing tables](/concepts/delta-sharing.md), views, or materialized views, and for tables that lack CDF. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Triggered

Triggered mode uses the source table’s change data feed to apply only the rows that changed since the last update. This is more efficient than Snapshot for large tables with frequent small changes. Triggered **requires** CDF to be enabled on the source table. Updates occur only when manually triggered (via the **Sync now** button in Catalog Explorer or through the pipeline API) or on a scheduled basis. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Continuous

Continuous mode continuously watches the change data feed of the source table and applies changes in near-real time. Like Triggered, it **requires** CDF enabled on the source table. This mode is appropriate for applications that demand the online table reflect source changes with minimal latency. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Requirements

- **Snapshot**: No special requirements; CDF is not needed. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Triggered and Continuous**: The source table **must** have Change Data Feed enabled. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- OpenSharing tables, views, and materialized views support **only** Snapshot mode. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Scheduling Periodic Updates

For online tables using Snapshot or Triggered sync mode, you can schedule automatic periodic updates. The schedule is managed at the pipeline level: ^[databricks-online-tables-legacy-databricks-on-aws.md]

1. In Catalog Explorer, navigate to the online table.
2. In the **Data Ingest** section, click the link to the pipeline.
3. Click **Schedule** (upper-right corner) and add or modify a schedule.

This allows cron-like triggers to refresh the online table without manual intervention.

## Selecting a Sync Mode

When creating an online table in Catalog Explorer, the **Sync mode** dropdown offers the three choices. The system may gray out **Triggered** or **Continuous** if the source table does not meet the Change Data Feed requirement or is a view or materialized view. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Databricks online table (legacy)](/concepts/databricks-online-tables.md) – The feature that provides low-latency row-oriented copies of Delta tables.
- [Delta Table](/concepts/delta-lake-table.md) – The source format for online tables.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Required for incremental sync modes (Triggered, Continuous).
- [Delta Sharing](/concepts/delta-sharing.md) – OpenSharing tables that only support Snapshot mode.
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – Serves online table data via REST API.
- [Model Serving](/concepts/model-serving.md) – Integrates with online tables for automatic feature lookup.

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
