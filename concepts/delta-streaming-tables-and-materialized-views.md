---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e8a1cd7444bf1d9722ed64323e813704749e7bd36adc47419e73c0c590e203c
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-streaming-tables-and-materialized-views
    - Materialized Views and Delta Streaming Tables
    - DSTAMV
    - Streaming tables and materialized views
    - CREATE MATERIALIZED VIEW
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Delta Streaming Tables and Materialized Views
description: The only table types supported by Delta external metadata; other table types trigger the DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE error.
tags:
  - delta-lake
  - streaming
  - views
timestamp: "2026-06-18T11:53:28.722Z"
---

# Delta Streaming Tables and Materialized Views

**Delta Streaming Tables** and **Materialized Views** are two types of Delta tables in Databricks that enable incremental data processing and automated refresh of query results. They are the only table types supported by the External Metadata feature for reconciliation queries. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Overview

Delta Streaming Tables and Materialized Views represent a paradigm shift from traditional batch ETL pipelines. Rather than recomputing entire datasets on each schedule, these table types process only new data incrementally, reducing cost and latency. They are managed as first-class objects in Unity Catalog, meaning schemas, access controls, lineage, and metadata are tracked automatically.

Both table types support incremental processing, where only new or changed data is processed since the last refresh. This makes them suitable for near-real-time data pipelines, Lakehouse applications, and operational analytics.

## Delta Streaming Tables

A **Delta Streaming Table** (often called a streaming live table or streaming table) is a [Delta Lake](/concepts/delta-lake.md) table that is incrementally maintained by a streaming query. The table automatically processes new data as it arrives from a streaming source, executing transformations defined in the table's query.

Key characteristics:

- **Incremental processing**: Only processes new records since the last update, rather than reprocessing the entire source. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **Continuous or triggered refresh**: Can run continuously (processing records as they arrive) or on a schedule. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **Exactly-once semantics**: Automatic tracking of what has been processed ensures no duplicates or missed records.
- **Source support**: Works with Auto Loader, Kafka, Kinesis, Event Hubs, and other streaming sources.

Use cases:
- Ingesting and transforming event streams (clickstream, IoT, logs)
- Building real-time dashboards and monitoring
- Processing CDC (change data capture) streams
- Incremental feature engineering for machine learning

## Materialized Views

A **Materialized View** is a precomputed, incrementally maintained view of a query. Unlike a traditional view, which re-executes the underlying query each time it is accessed, a Materialized View stores the results physically and updates them incrementally as the source data changes. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

Key characteristics:

- **Query-based definition**: Defined by a SQL SELECT statement that specifies which data to materialize.
- **Incremental refresh**: Only recomputes rows affected by changes in the source tables, rather than re-executing the entire query.
- **Automatic freshness**: Configured to refresh on a schedule or manually triggered.
- **Source support**: Can materialize results from batch tables, streaming tables, or other materialized views.

Use cases:
- Pre-aggregating expensive computations for dashboards
- Denormalizing data from multiple fact and dimension tables
- Accelerating common query patterns
- Building curated datasets from raw ingestion layers

## Shared Characteristics

Both Delta Streaming Tables and Materialized Views share the following properties: ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

- **Declarative definition**: Tables are defined by a query (SQL or DataFrame API), and the system manages the incremental maintenance.
- **Managed storage**: Data is stored as Delta Lake tables in Unity Catalog, providing ACID transactions, time travel, and schema evolution.
- **Incremental computation**: Only new or changed data is processed since the last refresh, avoiding full recomputation.
- **External Metadata support**: Only streaming tables and materialized views are supported as source types for reconciliation queries in the External Metadata feature.

## Important Distinction

While both table types process data incrementally, their refresh semantics differ:

- **Streaming Tables** consume from streaming sources (or batch sources treated as streams) and append or upsert new records as they arrive. The refresh is defined by the stream's progress.
- **Materialized Views** are generally batch-refreshed on a schedule, recomputing only the rows affected by changes in referenced tables.

In practice, both can be used together in a pipeline: Streaming Tables ingest raw data incrementally, and Materialized Views aggregate or join that data for consumption.

## External Metadata Support

The External Metadata feature supports reconciliation queries only against streaming tables and materialized views. Attempting to use other table types — such as tables with Column Mask policies, Row-Level Security policies, or tables where column mapping is not enabled — results in the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

The supported table types are explicitly listed as "streaming table and materialized view" in the error conditions for this feature. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Limitations

- Column Mask policies and Row-Level Security policies are not supported on table types other than streaming tables and materialized views for External Metadata reconciliation. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- Column mapping must be enabled to use an alias in reconciliation queries. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- Certain projections are not supported in reconciliation queries. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer underlying streaming tables and materialized views
- Auto Loader — A common source for streaming tables
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages these table types
- Incremental Processing — The compute paradigm used by both table types
- Delta Live Tables — The Databricks product that provides automation for building and maintaining streaming tables and materialized views
- [External Metadata](/concepts/external-metadata-api.md) — The feature that supports reconciliation queries on these table types

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
