---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 960a17ecf5a262c43a1a4545a2a17ad66cf98616667c22a46c29390b9bc319b5
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clone-limitations-for-streaming-tables-and-materialized-views
    - Materialized Views and CLONE Limitations for Streaming Tables
    - CLFSTAMV
    - clone-restrictions-with-streaming-tables-and-materialized-views
    - Materialized Views and CLONE Restrictions with Streaming Tables
    - CRWSTAMV
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: CLONE Limitations for Streaming Tables and Materialized Views
description: Streaming tables and materialized views cannot be used as source or target tables for the CLONE operation.
tags:
  - databricks
  - limitations
  - cloning
timestamp: "2026-06-18T11:25:05.166Z"
---

## CLONE Limitations for Streaming Tables and Materialized Views

**CLONE Limitations for Streaming Tables and Materialized Views** refers to the restriction that the `CLONE` operation in Databricks SQL and Databricks Runtime cannot use a Streaming Table or a [Materialized View](/concepts/materialized-views-in-databricks.md) as either the source or the target table. This limitation applies to both `SHALLOW CLONE` and `DEEP CLONE` operations. ^[create-table-clone-databricks-on-aws.md]

### Overview

The `CREATE TABLE CLONE` statement creates a copy of a source Delta, managed Iceberg, or Parquet table at a specific version. However, when the source or target is a streaming table or a materialized view — both of which are managed by Databricks’ incremental processing engine — the clone operation is disallowed. Databricks documentation explicitly states: “Streaming tables and materialized views are not supported as source or target tables for `CLONE`.” ^[create-table-clone-databricks-on-aws.md]

### Limitation Details

- **No source support:** You cannot clone a streaming table or materialized view to create another table.
- **No target support:** You cannot use a `CLONE` statement to copy data into an existing streaming table or materialized view.
- The restriction applies regardless of whether you use `SHALLOW CLONE` (metadata only, referencing source data files) or `DEEP CLONE` (full independent copy of data and metadata).
- The limitation is referenced in the separate limitations pages for CREATE STREAMING TABLE and [CREATE MATERIALIZED VIEW](/concepts/delta-streaming-tables-and-materialized-views.md) and in the main [CLONE](/concepts/deep-clone.md) documentation. ^[create-table-clone-databricks-on-aws.md]

### Impact

Users who need to create copies of streaming tables or materialized views for purposes such as testing, snapshots, or migration must use alternative methods. For example, to create a static snapshot of a streaming table you could:
- Query the streaming table with `SELECT *` and write the results to a new Delta table.
- Use `INSERT INTO` to copy data into a regular table.
- Leverage Delta Live Tables pipelines or other ETL workflows to materialize the data differently.

The same guidance applies when you want to populate a streaming table from an existing regular table — cloning is not available, so an incremental ingestion pattern must be used instead.

### Related Concepts

- [CLONE](/concepts/deep-clone.md) — The general clone operation and its supported source/target types.
- Streaming Tables — Tables that are incrementally updated by streaming queries.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Pre-computed views that are refreshed on a schedule or continuously.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for most Databricks tables.
- Delta Live Tables — A framework for building reliable data pipelines that can produce streaming tables and materialized views.

### Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
