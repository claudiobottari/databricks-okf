---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 09d32ae7399768ff3408347be06c178655ff33d26ecedf441d9c7d54aa7d9295
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-data-export-and-conversion
    - Conversion and Trace Data Export
    - TDEAC
    - Accessing Trace Data
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Trace Data Export and Conversion
description: MLflow traces support export and conversion to multiple formats including Python dictionaries (to_dict), JSON strings (to_json), and pandas DataFrame rows (to_pandas_dataframe_row), with corresponding from_dict/from_json reconstruction methods.
tags:
  - mlflow
  - data-export
  - serialization
timestamp: "2026-06-19T13:52:57.797Z"
---

# Trace Data Export and Conversion

**Trace data export and conversion** refers to the set of operations that transform MLflow [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) objects from their in-memory representation into serialized formats suitable for storage, transfer, or analysis. [MLflow Tracing](/concepts/mlflow-tracing.md) provides built-in methods for converting traces to dictionaries, JSON strings, and Pandas DataFrame rows. ^[access-trace-data-databricks-on-aws.md]

## Converting to Dictionary

The [`Trace.to_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_dict) method converts an entire trace object to a Python dictionary, preserving both the `info` ([Trace Metadata](/concepts/trace-metadata.md)) and `data` ([trace data](/concepts/tracedata.md)) components. You can also convert individual components using [`TraceInfo.to_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo.to_dict) and [`TraceData.to_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceData.to_dict). ^[access-trace-data-databricks-on-aws.md]

```python
# Convert entire trace to dictionary
trace_dict = trace.to_dict()
print(f"Trace dict keys: {trace_dict.keys()}")
print(f"Info keys: {trace_dict['info'].keys()}")
print(f"Data keys: {trace_dict['data'].keys()}")

# Convert individual components
info_dict = trace.info.to_dict()
data_dict = trace.data.to_dict()
```

A trace dictionary can be reconstructed back into a `Trace` object using [`Trace.from_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.from_dict). ^[access-trace-data-databricks-on-aws.md]

```python
from mlflow.entities import Trace

reconstructed_trace = Trace.from_dict(trace_dict)
print(f"Reconstructed trace ID: {reconstructed_trace.info.trace_id}")
```

## JSON Serialization

The [`Trace.to_json`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_json) method serializes the trace to a JSON string. You can optionally pass `pretty=True` to produce human-readable, indented JSON output. A JSON string can be deserialized back to a `Trace` object using [`Trace.from_json`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.from_json). ^[access-trace-data-databricks-on-aws.md]

```python
# Convert to JSON string
trace_json = trace.to_json()
print(f"JSON length: {len(trace_json)} characters")

# Pretty print JSON
trace_json_pretty = trace.to_json(pretty=True)
print("Pretty JSON (first 500 chars):")
print(trace_json_pretty[:500])

# Load trace from JSON
from mlflow.entities import Trace

loaded_trace = Trace.from_json(trace_json)
print(f"Loaded trace ID: {loaded_trace.info.trace_id}")
```

## Pandas DataFrame Conversion

The [`Trace.to_pandas_dataframe_row`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_pandas_dataframe_row) method converts a trace to a dictionary suitable for inclusion as a row in a Pandas DataFrame. This is useful when you need to aggregate or analyze multiple traces together using DataFrame operations. ^[access-trace-data-databricks-on-aws.md]

```python
import pandas as pd

# Convert trace to DataFrame row
row_data = trace.to_pandas_dataframe_row()
print(f"DataFrame row keys: {list(row_data.keys())}")

# Create DataFrame from multiple traces
traces = mlflow.search_traces(max_results=5)

# If you have individual trace objects
trace_rows = [t.to_pandas_dataframe_row() for t in [trace]]
df = pd.DataFrame(trace_rows)
print(f"DataFrame shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# Access specific data from DataFrame
print(f"Trace IDs: {df['trace_id'].tolist()}")
print(f"States: {df['state'].tolist()}")
print(f"Durations: {df['execution_duration'].tolist()}")
```

The resulting DataFrame columns include trace metadata fields such as `trace_id`, `state`, and `execution_duration`, enabling straightforward quantitative analysis. ^[access-trace-data-databricks-on-aws.md]

## Span Conversion

Individual spans within a trace can also be converted to dictionaries and reconstructed using [`Span.to_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span.to_dict) and [`Span.from_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span.from_dict). This allows you to export and reimport specific spans independently of the full trace. ^[access-trace-data-databricks-on-aws.md]

```python
# Convert span to dictionary
span_dict = span.to_dict()
print(f"Span dict keys: {span_dict.keys()}")

# Recreate span from dictionary
from mlflow.entities import Span
reconstructed_span = Span.from_dict(span_dict)
print(f"Reconstructed span: {reconstructed_span.name}")
```

## Use Cases

- **Data portability**: Export traces as JSON or dictionaries to transfer between systems or store in external databases. ^[access-trace-data-databricks-on-aws.md]
- **Custom analysis**: Convert traces to Pandas DataFrames for statistical analysis, visualization, or machine learning workflows. ^[access-trace-data-databricks-on-aws.md]
- **Serialization for storage**: Store trace data in serialized formats for long-term retention or audit logging. ^[access-trace-data-databricks-on-aws.md]
- **Reconstruction**: Export a trace, transmit it to another process, and reconstruct the `Trace` object on the receiving end using `from_dict` or `from_json`. ^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework providing these export capabilities
- [Accessing Trace Data](/concepts/trace-data-export-and-conversion.md) — How to retrieve and inspect individual trace components
- Analyzing Traces — Examples of trace analysis workflows
- [Assessments](/concepts/assessments.md) — Evaluating and scoring trace outputs
- Trace Search — Finding traces by criteria using MLflow search APIs

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
