---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85d84cf67fd0ebfa23200b87c846230f41f58d378dc611977a88324553ae1d42
  pageDirectory: concepts
  sources:
    - search-traces-programmatically-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sql-warehouse-integration-for-trace-search
    - SWIFTS
    - SQL warehouse for tracing
  citations:
    - file: search-traces-programmatically-databricks-on-aws.md
title: SQL Warehouse Integration for Trace Search
description: Performance optimization using a Databricks SQL warehouse to accelerate queries on large trace datasets in inference or Unity Catalog tables.
tags:
  - mlflow
  - performance
  - sql-warehouse
timestamp: "2026-06-19T20:19:57.240Z"
---

# SQL Warehouse Integration for Trace Search

**SQL Warehouse Integration for Trace Search** refers to the ability to use a Databricks SQL warehouse as the query engine for the `mlflow.search_traces()` API, improving performance when searching large trace datasets stored in [Inference Tables](/concepts/inference-tables.md) or [Unity Catalog](/concepts/unity-catalog.md) tables.

## Overview

By default, `mlflow.search_traces()` queries traces from the MLflow tracking server or from inference tables and Unity Catalog tables using a standard query path. For large trace datasets, this can result in slower performance. The SQL warehouse integration provides an alternative, more performant execution path by routing queries through a Databricks SQL warehouse. ^[search-traces-programmatically-databricks-on-aws.md]

## Enabling SQL Warehouse Integration

To use a SQL warehouse for trace search, set the `MLFLOW_TRACING_SQL_WAREHOUSE_ID` environment variable to the ID of a target SQL warehouse. Once set, all subsequent calls to `mlflow.search_traces()` will use the specified warehouse to execute queries. ^[search-traces-programmatically-databricks-on-aws.md]

```python
import os
os.environ['MLFLOW_TRACING_SQL_WAREHOUSE_ID'] = 'fa92bea7022e81fb'

# Use SQL warehouse for better performance
traces = mlflow.search_traces(
    filter_string="trace.status = 'OK'",
    locations=['my_catalog.my_schema'],
)
```

^[search-traces-programmatically-databricks-on-aws.md]

## Performance Benefits

The SQL warehouse integration is specifically intended to **improve performance on large trace datasets** in inference tables or Unity Catalog tables. When working with smaller trace volumes, the performance difference may be negligible, but for production-scale trace collections spanning thousands or millions of traces, routing queries through a SQL warehouse can significantly reduce query time. ^[search-traces-programmatically-databricks-on-aws.md]

## Considerations

While `mlflow.search_traces()` supports the SQL warehouse integration for performance, the API returns all results in memory as a pandas DataFrame or list of `Trace` objects. This approach works well for smaller result sets. For **large result sets** that exceed available memory, use `MlflowClient.search_traces()` instead, which supports pagination and can handle very large result volumes without loading everything into memory at once. ^[search-traces-programmatically-databricks-on-aws.md]

## Related Concepts

- mlflow.search_traces() — The primary API for programmatic trace search
- SQL warehouse — The compute resource used for the query execution
- [Inference Tables](/concepts/inference-tables.md) — A data source for trace storage that benefits from this integration
- [Unity Catalog](/concepts/unity-catalog.md) — A catalog schema that can serve as a trace location
- mlflow.search_traces() API|MlflowClient.search_traces() — Paginated alternative for large result sets
- [Trace Search Query Syntax](/concepts/trace-search-query-syntax.md) — SQL-like filtering language used with `mlflow.search_traces()`

## Sources

- search-traces-programmatically-databricks-on-aws.md

# Citations

1. [search-traces-programmatically-databricks-on-aws.md](/references/search-traces-programmatically-databricks-on-aws-0153c5e0.md)
