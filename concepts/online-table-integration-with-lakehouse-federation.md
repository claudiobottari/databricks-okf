---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f48a2828775fc16c5c75053c6ac18fdf0fca54760543bf9730abdf40f0acc6a
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-table-integration-with-lakehouse-federation
    - OTIWLF
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Table Integration with Lakehouse Federation
description: Online tables can be queried via Lakehouse Federation using Serverless SQL warehouses, but only for SELECT operations and intended for interactive/debugging use, not production.
tags:
  - databricks
  - lakehouse-federation
  - querying
timestamp: "2026-06-18T15:09:24.931Z"
---

# Online Table Integration with Lakehouse Federation

**Online Table Integration with Lakehouse Federation** allows users to query online tables—row‑oriented, serverless replicas of Delta tables—using Databricks’ Lakehouse Federation feature. This capability is intended for interactive debugging or ad‑hoc exploratory queries rather than production workloads. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Overview

An [Online Table (legacy)](/concepts/databricks-online-tables-legacy.md) is a read‑only copy of a Delta Table stored in a row‑oriented format optimised for low‑latency, high‑throughput lookups (e.g., for Model Serving, Feature Serving, or RAG applications). By integrating these tables with [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md), users can run standard `SELECT` queries against online tables from Serverless SQL warehouses, enabling quick validation of the data that is being served. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Requirements

- The workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md) and the Serverless SQL warehouse must be used. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- Only read operations (`SELECT`) are supported; write operations are not allowed. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Usage

To query an online table through Lakehouse Federation, connect a Serverless SQL warehouse and run a standard `SELECT` statement against the online table’s fully qualified name in Unity Catalog (e.g., `main.default.my_online_table`). The query engine automatically resolves the online table through the federation layer. ^[databricks-online-tables-legacy-databricks-on-aws.md]

> **Important**: This integration is intended for **interactive or debugging purposes only**. It must not be used for production or mission‑critical workloads. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Limitations

- Queries must be executed from a Serverless SQL warehouse; other warehouse types are not supported. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- Only `SELECT` statements are permitted (no `INSERT`, `UPDATE`, `DELETE`, or DDL operations on the online table via federation). ^[databricks-online-tables-legacy-databricks-on-aws.md]
- The integration does not provide the same throughput or latency guarantees as the direct endpoint access used by Model Serving or Feature Serving. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## When to Use Lakehouse Federation vs. Direct Endpoint Access

Use Lakehouse Federation when you need to quickly inspect the contents of an online table during development or troubleshooting. For production data lookups (e.g., serving features to a real‑time model), always use the dedicated feature serving or model serving endpoint that automatically reads from the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Online Table (legacy)](/concepts/databricks-online-tables-legacy.md) – The row‑oriented serverless copy of a Delta table.
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) – The Databricks feature for querying external data sources.
- Serverless SQL Warehouse – The compute required to query online tables via federation.
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – The recommended way to serve online table data for production.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages online tables.

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
