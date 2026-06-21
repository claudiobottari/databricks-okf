---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aff8a448be3da9b67055199bb3a4d5b88f89de3ec4fd9ae811c6198a740c1b10
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakehouse-federation-with-online-tables
    - LFWOT
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Lakehouse Federation with Online Tables
description: The ability to query online tables using Lakehouse Federation and a Serverless SQL warehouse, supporting only SELECT operations for interactive or debugging purposes, not for production workloads.
tags:
  - databricks
  - lakehouse-federation
  - querying
  - serverless-sql
timestamp: "2026-06-19T14:52:45.093Z"
---

# Lakehouse Federation with Online Tables

**Lakehouse Federation with Online Tables** is a feature that allows users to query [Online Tables](/concepts/online-tables.md) directly using [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) from a Serverless SQL Warehouse. Online tables are read-only, row-oriented copies of [Delta Table](/concepts/delta-lake-table.md)s designed for low-latency online access. When combined with Lakehouse Federation, these tables can be queried using standard SQL for interactive or debugging purposes. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Requirements

To use Lakehouse Federation with online tables, you must connect through a Serverless SQL Warehouse. Only `SELECT` (read) operations are supported; write operations such as `INSERT`, `UPDATE`, or `DELETE` are not allowed. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Limitations and Intended Use

This capability is **intended for interactive or debugging purposes only** and should **not be used for production or mission-critical workloads**. The performance and reliability characteristics of querying online tables via Lakehouse Federation are not designed for high-throughput production traffic. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Use Cases

Lakehouse Federation with online tables can be used to:

- Inspect the current state of an online table during development or troubleshooting.
- Perform ad‑hoc queries to verify data synchronization between the source Delta table and the online table.
- Quickly validate feature values before integrating with [Model Serving](/concepts/model-serving.md) or Feature Serving endpoints.

## Related Concepts

- [Online Tables](/concepts/online-tables.md) – The row‑oriented, serverless tables optimized for real‑time lookups.
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) – A feature that enables querying data across multiple external systems from Databricks.
- Serverless SQL Warehouse – The compute resource required to query online tables via Lakehouse Federation.
- [Delta Table](/concepts/delta-lake-table.md) – The source table from which an online table is created.
- [Model Serving](/concepts/model-serving.md) – A service that can automatically look up features from online tables during inference.
- Feature Serving – A REST API endpoint that serves features from online tables to external applications.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – A common application pattern that uses online tables for structured data lookups.

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
