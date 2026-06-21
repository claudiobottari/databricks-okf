---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4295425762e8e76a005e331a8ba58b8b0fb6263078854367c728ca3c38174644
  pageDirectory: concepts
  sources:
    - search-traces-programmatically-databricks-on-aws.md
    - tutorial-search-traces-programmatically-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflowsearch_traces-api
    - MlflowClient.search_traces()
    - Search Traces API
    - Search Traces Programmatically
    - Search traces programmatically
    - search traces programmatically
    - search_traces API
  citations:
    - file: search-traces-programmatically-databricks-on-aws.md
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
    - file: tutorial-search-traces-programmatically-databricks-on-aws.md
title: mlflow.search_traces() API
description: Primary Python API for programmatically querying and filtering MLflow traces stored in tracking servers, inference tables, or Unity Catalog tables.
tags:
  - mlflow
  - tracing
  - api
timestamp: "2026-06-19T20:20:01.874Z"
---

# mlflow.search_traces() API

The `mlflow.search_traces()` function provides a programmatic interface for querying and retrieving traces stored in the MLflow tracking server, inference tables, or Unity Catalog tables. It is a core tool for analyzing GenAI application behavior, building evaluation datasets, and collecting human feedback.^[search-traces-programmatically-databricks-on-aws.md]

## Overview

`mlflow.search_traces()` enables developers to filter, select, and retrieve traces along multiple dimensions, including status, execution time, metadata, tags, and timestamps. The function returns either a pandas DataFrame or a list of [[MLflow Trace|MLflow Traces|Trace]] objects, which can be further analyzed or reshaped into evaluation datasets.^[search-traces-programmatically-databricks-on-aws.md]

The function is commonly used in workflows involving [MLflow Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md), where labeled traces from expert review sessions are retrieved for evaluation against ground truth responses.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## API Signature

```python
def mlflow.search_traces(
    experiment_ids: list[str] | None = None,
    filter_string: str | None = None,
    max_results: int | None = None,
    order_by: list[str] | None = None,
    extract_fields: list[str] | None = None,
    run_id: str | None = None,
    return_type: Literal['pandas', 'list'] | None = None,
    model_id: str | None = None,
    sql_warehouse_id: str | None = None,
    include_spans: bool = True,
    locations: list[str] | None = None,
) -> pandas.DataFrame | list[Trace]
```

^[search-traces-programmatically-databricks-on-aws.md]

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `experiment_ids` | `list[str] \| None` | Filter traces by experiment IDs. |
| `filter_string` | `str \| None` | SQL-like query string for filtering traces. |
| `max_results` | `int \| None` | Maximum number of traces to return. |
| `order_by` | `list[str] \| None` | Sort order for results. |
| `extract_fields` | `list[str] \| None` | Specific fields to extract from traces. |
| `run_id` | `str \| None` | Filter traces by a specific [MLflow Run](/concepts/mlflow-run.md) ID. |
| `return_type` | `Literal['pandas', 'list'] \| None` | Format of returned data. |
| `model_id` | `str \| None` | Filter traces by model ID. |
| `sql_warehouse_id` | `str \| None` | SQL warehouse ID for improved performance on large datasets. |
| `include_spans` | `bool` | Whether to include span data in results. |
| `locations` | `list[str] \| None` | Filter by locations such as experiment, run, model, or Unity Catalog schema. |

^[search-traces-programmatically-databricks-on-aws.md]

## Search Query Syntax

The `filter_string` argument uses a SQL-like query language to filter traces. String values must be wrapped in single quotes (for example, `trace.status = 'OK'`), and numeric values must not be quoted (for example, `trace.execution_time_ms > 1000`). Combine conditions with `AND`; the `OR` operator is not supported.^[search-traces-programmatically-databricks-on-aws.md]

### Supported Fields and Comparators

| Field | Type | Supported Comparators |
|-------|------|----------------------|
| `trace.status` | String | `=`, `!=` |
| `trace.timestamp_ms` | Numeric | `>`, `>=`, `<`, `<=`, `=` |
| `trace.execution_time_ms` | Numeric | `>`, `>=`, `<`, `<=`, `=` |
| `trace.latency` | Numeric (alias for `execution_time_ms`) | `>`, `>=`, `<`, `<=`, `=` |
| `trace.timestamp` | Numeric (alias for `timestamp_ms`) | `>`, `>=`, `<`, `<=`, `=` |
| `metadata.<key>` | String | `=`, `!=` |
| `tag.<key>` | String | `=`, `!=` |

^[search-traces-programmatically-databricks-on-aws.md, tutorial-search-traces-programmatically-databricks-on-aws.md]

### Query Syntax Rules

- Use prefixes: `trace.`, `tag.`, or `metadata.`
- Use backticks if tag or attribute names contain dots: `` tag.`mlflow.traceName` ``
- Use single quotes only: `'value'` not `"value"`
- Use Unix timestamps in milliseconds for time comparisons
- Use `AND` only; `OR` is not supported

^[search-traces-programmatically-databricks-on-aws.md]

## Return Format

`mlflow.search_traces()` returns either a pandas DataFrame or a list of `Trace` objects. The DataFrame contains the following columns:

```
['trace_id', 'trace', 'client_request_id', 'state', 'request_time', 
 'execution_duration', 'request', 'response', 'trace_metadata', 
 'tags', 'spans', 'assessments']
```

^[tutorial-search-traces-programmatically-databricks-on-aws.md]

## Usage Examples

### Basic Search by Status

```python
# Find all successful traces
mlflow.search_traces(filter_string="trace.status = 'OK'")

# Find all failed traces
mlflow.search_traces(filter_string="trace.status = 'ERROR'")
```

^[tutorial-search-traces-programmatically-databricks-on-aws.md]

### Search by Time Range

```python
import time
from datetime import datetime

# Traces from the last 5 minutes
current_time_ms = int(time.time() * 1000)
five_minutes_ago = current_time_ms - (5 * 60 * 1000)
mlflow.search_traces(
    filter_string=f"trace.timestamp_ms > {five_minutes_ago}"
)

# Traces within a date range
start_date = int(datetime(2026, 1, 1).timestamp() * 1000)
end_date = int(datetime(2026, 1, 31).timestamp() * 1000)
mlflow.search_traces(
    filter_string=f"trace.timestamp_ms > {start_date} AND trace.timestamp_ms < {end_date}"
)
```

^[tutorial-search-traces-programmatically-databricks-on-aws.md]

### Search by Execution Time

```python
# Find slow traces
mlflow.search_traces(filter_string="trace.execution_time_ms > 2500")

# Using the latency alias
mlflow.search_traces(filter_string="trace.latency > 1000")
```

^[tutorial-search-traces-programmatically-databricks-on-aws.md]

### Search by Metadata and Tags

```python
# Search by custom metadata
mlflow.search_traces(
    filter_string="metadata.`mlflow.trace.user` = 'name@my_company.com'"
)

# Search by tags
mlflow.search_traces(filter_string="tag.environment = 'production'")
mlflow.search_traces(
    filter_string="tag.`mlflow.traceName` = 'my_app'"
)
```

^[tutorial-search-traces-programmatically-databricks-on-aws.md]

### Complex Filters with AND

```python
# Recent successful production traces
current_time_ms = int(time.time() * 1000)
one_hour_ago = current_time_ms - (60 * 60 * 1000)
mlflow.search_traces(
    filter_string=f"trace.status = 'OK' AND "
                  f"trace.timestamp_ms > {one_hour_ago} AND "
                  f"tag.environment = 'production'"
)

# Fast traces from a specific user
mlflow.search_traces(
    filter_string="trace.execution_time_ms < 2500 AND "
                  "metadata.`mlflow.trace.user` = 'name@my_company.com'"
)
```

^[tutorial-search-traces-programmatically-databricks-on-aws.md]

### Retrieving Traces from a Labeling Session

```python
# Get traces from an expert review session
labeled_traces = mlflow.search_traces(
    run_id=labeling_session.mlflow_run_id,
)
```

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Limiting Results

```python
# Get the most recent trace
traces = mlflow.search_traces(max_results=1)
```

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Best Practices

### Use Keyword Arguments

Always use keyword (named) arguments with `mlflow.search_traces()`. The function allows positional arguments, but the argument list is evolving.^[search-traces-programmatically-databricks-on-aws.md]

**Good practice:** `mlflow.search_traces(filter_string="trace.status = 'OK'")`

**Bad practice:** `mlflow.search_traces([], "trace.status = 'OK'")`

### SQL Warehouse Integration for Large Datasets

For improved performance on large trace datasets in inference tables or Unity Catalog tables, specify a SQL warehouse ID using the `MLFLOW_TRACING_SQL_WAREHOUSE_ID` environment variable:^[search-traces-programmatically-databricks-on-aws.md]

```python
import os
os.environ['MLFLOW_TRACING_SQL_WAREHOUSE_ID'] = 'fa92bea7022e81fb'

traces = mlflow.search_traces(
    filter_string="trace.status = 'OK'",
    locations=['my_catalog.my_schema'],
)
```

For very large result sets, use `MlflowClient.search_traces()` instead, as it supports pagination.^[search-traces-programmatically-databricks-on-aws.md]

### Handling Returned Data

The returned DataFrame or list of `Trace` objects can be used for further analysis, converted into [evaluation datasets](/concepts/mlflow-evaluation-dataset.md), or passed directly to `mlflow.genai.evaluate()` for quality assessment.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Differences from OSS MLflow

Databricks-managed MLflow and open source MLflow share most search query syntax but have a few field-level differences. See the official documentation for details on platform-specific behavior.^[search-traces-programmatically-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] – The trace objects returned by `search_traces()`
- [MLflow Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) – Workflow that uses `search_traces()` to retrieve labeled traces
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) – Versioned datasets built from queried traces
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Framework that consumes traces for quality assessment
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The foundation for generating and storing traces

## Sources

- [search-traces-programmatically-databricks-on-aws.md]
- [tutorial-search-traces-programmatically-databricks-on-aws.md]
- [10-minute-demo-collect-human-feedback-databricks-on-aws.md]

# Citations

1. [search-traces-programmatically-databricks-on-aws.md](/references/search-traces-programmatically-databricks-on-aws-0153c5e0.md)
2. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
3. [tutorial-search-traces-programmatically-databricks-on-aws.md](/references/tutorial-search-traces-programmatically-databricks-on-aws-4b1ea59e.md)
