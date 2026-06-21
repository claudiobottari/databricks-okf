---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6966b408fb37abbfbb02a60d5db848a053a7c7760440a313c89e9ed4e214e79
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clone-restrictions-with-streaming-tables-and-materialized-views
    - Materialized Views and CLONE Restrictions with Streaming Tables
    - CRWSTAMV
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: CLONE Restrictions with Streaming Tables and Materialized Views
description: Streaming tables and materialized views are not supported as source or target tables for CLONE operations.
tags:
  - limitations
  - streaming
  - materialized-views
timestamp: "2026-06-19T18:02:40.775Z"
---

# CLONE Restrictions with Streaming Tables and Materialized Views

**CLONE Restrictions with Streaming Tables and Materialized Views** refers to the limitation that Streaming Tables and [Materialized Views](/concepts/materialized-views-in-databricks.md) cannot be used as source or target tables for the `CLONE` operation in Databricks SQL and Databricks Runtime. This restriction applies to both deep and shallow cloning operations. ^[create-table-clone-databricks-on-aws.md]

## Overview

The `CREATE TABLE CLONE` statement supports cloning Delta, managed Apache Iceberg, and Apache Parquet tables. However, streaming tables and materialized views are explicitly excluded from this support. Neither type can serve as the source table being cloned, nor as the target table being created or replaced by the clone operation. ^[create-table-clone-databricks-on-aws.md]

## Affected Operations

The restriction applies to all forms of the `CLONE` statement:

- `CREATE TABLE ... CLONE`
- `CREATE OR REPLACE TABLE ... CLONE`
- `REPLACE TABLE ... CLONE`

Both `SHALLOW CLONE` and `DEEP CLONE` variants are affected. ^[create-table-clone-databricks-on-aws.md]

## Reason for Restriction

Streaming tables and materialized views have continuous data processing semantics that differ from standard tables. Streaming tables ingest data incrementally from streaming sources, while materialized views maintain pre-computed results that are refreshed on a schedule. The `CLONE` operation is designed for static or batch-updated tables and does not support the incremental processing or refresh mechanisms associated with these table types. ^[create-table-clone-databricks-on-aws.md]

## Workarounds

To create a copy of a streaming table or materialized view, consider the following approaches:

- Use `CREATE TABLE ... AS SELECT` to copy the current data into a new table.
- For streaming tables, create a new streaming table with the same source configuration.
- For materialized views, create a new materialized view with the same query definition.

These alternatives do not preserve the full metadata or history of the original table in the same way that `CLONE` does, but they allow you to replicate the data or logic.

## Related Concepts

- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) — The full syntax and parameters for the clone operation.
- Streaming Tables — Tables that ingest data incrementally from streaming sources.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Pre-computed views that are refreshed on a schedule.
- Deep Clone vs Shallow Clone — Differences between copying data and referencing source files.
- [Delta Lake Cloning](/concepts/delta-table-cloning.md) — General guidance on cloning Delta tables on Databricks.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
