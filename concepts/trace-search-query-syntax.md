---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e5cf1ce92adc0d85ecb7c6b4e07312f4169c19a5379a6381615a9b15bd0f196
  pageDirectory: concepts
  sources:
    - search-traces-programmatically-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-search-query-syntax
    - TSQS
    - Search query syntax
    - Trace.search_spans()
  citations:
    - file: search-traces-programmatically-databricks-on-aws.md
title: Trace Search Query Syntax
description: SQL-like filter language used with mlflow.search_traces() to filter traces by fields like status, execution time, tags, and metadata.
tags:
  - mlflow
  - query-language
  - filtering
timestamp: "2026-06-19T20:19:49.215Z"
---

# Trace Search Query Syntax

**Trace Search Query Syntax** refers to the SQL-like query language used with [`mlflow.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces) to filter and retrieve traces stored in the MLflow tracking server, inference tables, or Unity Catalog tables. The syntax enables selecting subsets of traces for analysis or for creating evaluation datasets. ^[search-traces-programmatically-databricks-on-aws.md]

## Overview

The `filter_string` argument in `mlflow.search_traces()` accepts a SQL-like query language to filter traces. String values must be wrapped in single quotes (for example, `trace.status = 'OK'`), while numeric values must not be quoted (for example, `trace.execution_time_ms > 1000`). Multiple conditions can be combined using `AND`; the `OR` operator is not supported. ^[search-traces-programmatically-databricks-on-aws.md]

## Supported Filters and Comparators

The following fields and comparators are supported on Databricks-managed MLflow:

| Field Prefix | Description |
|---|---|
| `trace.` | Trace-level attributes such as `status`, `execution_time_ms`, `timestamp_ms` |
| `tag.` | Tags attached to traces |
| `metadata.` | Metadata fields on traces |
| `span.attributes.*` | Third-party OpenTelemetry span attributes (for traces ingested from tools like Langfuse) |

^[search-traces-programmatically-databricks-on-aws.md]

Standard comparators include `=`, `!=`, `>`, `<`, `>=`, `<=`, and `LIKE` for pattern matching on string fields.

## Key Syntax Rules

When constructing a `filter_string`, follow these rules: ^[search-traces-programmatically-databricks-on-aws.md]

- **Use prefixes**: Always prefix field names with `trace.`, `tag.`, or `metadata.`
- **Backtick escaping**: If tag or attribute names contain dots, wrap them in backticks: `` tag.`mlflow.traceName` ``
- **Single quotes only**: Use `'value'`, not `"value"`
- **Unix timestamps**: Use Unix timestamps in milliseconds for time fields (for example, `1749006880539`), not date strings
- **AND only**: Combine conditions with `AND`; `OR` is not supported

## Differences from OSS MLflow

Databricks-managed MLflow and open source software (OSS) MLflow share most search query syntax but have a few field-level differences. Users should consult the documentation for specific field availability on their platform. ^[search-traces-programmatically-databricks-on-aws.md]

## Searching Third-Party OpenTelemetry Spans

To search traces ingested from third-party OpenTelemetry tools such as Langfuse, use the `span.attributes.*` prefix instead of the standard `trace.` prefix. ^[search-traces-programmatically-databricks-on-aws.md]

## Best Practices

### Keyword Arguments

Always use keyword (named) arguments with `mlflow.search_traces()`. While it accepts positional arguments, the function arguments are evolving. ^[search-traces-programmatically-databricks-on-aws.md]

**Good practice:** `mlflow.search_traces(filter_string="trace.status = 'OK'")`

**Bad practice:** `mlflow.search_traces([], "trace.status = 'OK'")`

### SQL Warehouse Integration

`mlflow.search_traces()` can optionally use a Databricks SQL warehouse to improve performance on large trace datasets in inference tables or Unity Catalog tables. Specify the SQL warehouse ID using the `MLFLOW_TRACING_SQL_WAREHOUSE_ID` environment variable. ^[search-traces-programmatically-databricks-on-aws.md]

```python
import os
os.environ['MLFLOW_TRACING_SQL_WAREHOUSE_ID'] = 'fa92bea7022e81fb'

traces = mlflow.search_traces(
    filter_string="trace.status = 'OK'",
    locations=['my_catalog.my_schema'],
)
```

### Handling Large Result Sets

`mlflow.search_traces()` returns results in memory, which works well for smaller result sets. For large result sets, use [`MlflowClient.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_traces) since it supports pagination. ^[search-traces-programmatically-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of trace collection and storage
- mlflow.search_traces() — The API function that uses this query syntax
- Trace Analysis — Analyzing queried traces for insights
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Building test datasets from queried traces
- OpenTelemetry Integration — Ingesting traces from third-party tools

## Sources

- search-traces-programmatically-databricks-on-aws.md

# Citations

1. [search-traces-programmatically-databricks-on-aws.md](/references/search-traces-programmatically-databricks-on-aws-0153c5e0.md)
