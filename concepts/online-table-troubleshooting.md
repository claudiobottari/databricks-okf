---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 69729909a2b2298e30a879e143305999f04db27489c76697de7e2242cc9ebdc0
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-table-troubleshooting
    - OTT
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
      start: 193
      end: 208
    - file: databricks-online-tables-legacy-databricks-on-aws.md
      start: 152
      end: 167
    - file: databricks-online-tables-legacy-databricks-on-aws.md
      start: 170
      end: 174
    - file: databricks-online-tables-legacy-databricks-on-aws.md
      start: 212
      end: 215
    - file: databricks-online-tables-legacy-databricks-on-aws.md
      start: 217
      end: 220
    - file: databricks-online-tables-legacy-databricks-on-aws.md
      start: 222
      end: 232
    - file: databricks-online-tables-legacy-databricks-on-aws.md
      start: 138
      end: 150
    - file: databricks-online-tables-legacy-databricks-on-aws.md
      start: 93
      end: 108
    - file: databricks-online-tables-legacy-databricks-on-aws.md
      start: 111
      end: 113
title: Online Table Troubleshooting
description: Common issues with online tables including missing Create option, unavailable sync modes, pipeline failures due to deleted source tables, firewall blocks, and exceeded metastore size limits.
tags:
  - databricks
  - troubleshooting
  - debugging
timestamp: "2026-06-19T09:54:43.613Z"
---

# Online Table Troubleshooting

This page describes common problems that occur when working with [Online Tables](/concepts/online-tables.md) and how to diagnose and resolve them. Online tables are read-only, row‑oriented copies of Delta tables used for low‑latency lookups from [Model Serving](/concepts/model-serving.md), Feature Serving, and RAG applications.

## General Troubleshooting Approach

When an online table displays an error or offline status, the first step is to examine the underlying synchronization pipeline. In Catalog Explorer, open the online table’s **Overview** tab and click the pipeline ID shown in the **Data Ingest** section. On the pipeline UI, locate the entry that says “Failed to resolve flow ‘\_\_online\_table’”. Click it to view a popup with detailed error information. This approach surfaces the root cause for most update failures. ^[databricks-online-tables-legacy-databricks-on-aws.md#L193-L208]

## Common Issues and Solutions

### “Create online table” option is not visible in Catalog Explorer

The most common cause is that the source table’s securable kind is not supported. Supported types include `TABLE_EXTERNAL`, `TABLE_DELTA`, `TABLE_DELTA_EXTERNAL`, `TABLE_DELTASHARING`, `TABLE_DELTASHARING_MUTABLE`, `TABLE_STREAMING_LIVE_TABLE`, `TABLE_STANDARD`, `TABLE_FEATURE_STORE`, `TABLE_FEATURE_STORE_EXTERNAL`, `TABLE_VIEW`, `TABLE_VIEW_DELTASHARING`, and `TABLE_MATERIALIZED_VIEW`. Check the **Details** tab of the source table in Catalog Explorer to confirm its securable kind. ^[databricks-online-tables-legacy-databricks-on-aws.md#L152-L167]

### Cannot select Triggered or Continuous sync mode

The **Triggered** and **Continuous** sync modes require [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDF) to be enabled on the source Delta table. If CDF is disabled, or if the source is a View or materialized view, only the **Snapshot** mode is available. Enable CDF on the source table to unlock incremental sync modes. ^[databricks-online-tables-legacy-databricks-on-aws.md#L170-L174]

### Online table update fails or status shows offline

Several underlying issues can cause a failed update. Common causes include:

- **Source table deleted or recreated** while the online table was synchronizing. This occurs frequently with continuous online tables because they are always running. If the source table is dropped and re‑created with the same name, the pipeline may become confused. To recover, you can trigger a full refresh using the pipeline API (`w.pipelines.start_update(pipeline_id='...', full_refresh=True)`) after confirming the source is correctly re‑established. ^[databricks-online-tables-legacy-databricks-on-aws.md#L212-L215]
- **Source table inaccessible from Serverless Compute** due to firewall or network restrictions. In the error details, you may see a message like “Failed to start the Lakeflow Spark Declarative Pipelines service on cluster xxx…”. Verify that the source table’s location is reachable by Databricks Serverless Compute and that no egress firewall rules block it. ^[databricks-online-tables-legacy-databricks-on-aws.md#L217-L220]
- **Metastore‑wide storage limit exceeded** – The total uncompressed size of all online tables in a Unity Catalog [Metastore](/concepts/metastore.md) cannot exceed 2 TB during Public Preview. Because online tables store data in row‑oriented format, the size can be up to 100× larger than the compressed Delta table size shown in Catalog Explorer. To estimate the row‑expanded size of a source table, run the following query from a Serverless SQL Warehouse: ^[databricks-online-tables-legacy-databricks-on-aws.md#L222-L232]

```sql
SELECT sum(length(to_csv(struct(*)))) FROM `source_table`;
```

The result is the estimated expanded size in bytes. If you are approaching the 2 TB limit, consider removing unneeded online tables or reducing the amount of data in the source table.

## Additional Limitations That May Cause Problems

- Only one online table can be created per source Delta table.
- Primary key columns cannot be of type ARRAY, MAP, or STRUCT; rows with null in a primary key column are silently skipped.
- Columns of String type are limited to 64 KB; column names are limited to 64 characters; total row size is limited to 2 MB.
- Catalog, schema, and table names may only contain alphanumeric characters and underscores; dashes are not allowed. ^[databricks-online-tables-legacy-databricks-on-aws.md#L138-L150]

## Checking Pipeline Health and Triggering a Manual Refresh

Use the pipeline ID returned in the online table’s spec to inspect or restart the sync. The following Python SDK example retrieves the pipeline ID and starts a full refresh: ^[databricks-online-tables-legacy-databricks-on-aws.md#L93-L108]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
table = w.online_tables.get('main.default.my_online_table')
pipeline_id = table.spec.pipeline_id

# Start a full refresh to discard existing data and re‑sync
w.pipelines.start_update(pipeline_id=pipeline_id, full_refresh=True)
```

Deleting the online table via `w.online_tables.delete(...)` stops all synchronization and releases resources. ^[databricks-online-tables-legacy-databricks-on-aws.md#L111-L113]

## Related Concepts

- [Delta Tables](/concepts/delta-lake-table.md) – The source data that online tables replicate.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Required for incremental sync modes.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where online tables are registered.
- [Model Serving with Automatic Feature Lookup](/concepts/model-serving-with-automatic-feature-lookup.md) – Using online tables for inference.
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – REST API for serving features from online tables.
- Serverless Compute – The compute platform that runs online table pipelines.

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md:193-208](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
2. [databricks-online-tables-legacy-databricks-on-aws.md:152-167](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
3. [databricks-online-tables-legacy-databricks-on-aws.md:170-174](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
4. [databricks-online-tables-legacy-databricks-on-aws.md:212-215](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
5. [databricks-online-tables-legacy-databricks-on-aws.md:217-220](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
6. [databricks-online-tables-legacy-databricks-on-aws.md:222-232](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
7. [databricks-online-tables-legacy-databricks-on-aws.md:138-150](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
8. [databricks-online-tables-legacy-databricks-on-aws.md:93-108](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
9. [databricks-online-tables-legacy-databricks-on-aws.md:111-113](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
