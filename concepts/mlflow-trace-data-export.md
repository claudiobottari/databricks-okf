---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8fd4badb05e1e8270d726ace7910846727aadeeb454fdc44ec1df5b4d8ca52e
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-data-export
    - MTDE
    - Trace Export
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: MLflow Trace Data Export
description: Methods for converting MLflow Trace objects to dictionaries, JSON strings, and Pandas DataFrame rows for serialization and analysis.
tags:
  - mlflow
  - tracing
  - serialization
timestamp: "2026-06-19T17:25:41.038Z"
---

# MLflow Trace Data Export

**MLflow Trace Data Export** refers to the set of methods and data structures used to serialize, convert, and reconstruct [trace](/concepts/mlflow-tracing.md) objects for analysis, storage, or integration with other tools. The `mlflow.entities.Trace` class provides built-in export to dictionaries, JSON strings, and Pandas DataFrame rows, as well as corresponding factory methods that rehydrate traces from those formats. ^[access-trace-data-databricks-on-aws.md]

## Overview

A [Trace](/concepts/traces.md) object comprises two main components: `TraceInfo` (metadata) and `TraceData` (actual execution data, including Span|spans and full request/response payloads). Export methods operate on the entire trace or on its individual components. The library also allows conversion of individual Span objects to and from dictionaries. ^[access-trace-data-databricks-on-aws.md]

## Data Export Methods

### Convert to Dictionary

The [`Trace.to_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_dict) method serialises the entire trace into a Python dictionary. The dictionary contains keys `"info"` and `"data"`, each holding the corresponding sub‑dictionaries. Individual components can also be converted using `TraceInfo.to_dict()` and `TraceData.to_dict()`. ^[access-trace-data-databricks-on-aws.md]

```python
trace_dict = trace.to_dict()
print(f"Info keys: {trace_dict['info'].keys()}")
print(f"Data keys: {trace_dict['data'].keys()}")

info_dict = trace.info.to_dict()
data_dict = trace.data.to_dict()
```

### JSON Serialization

The [`Trace.to_json`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_json) method returns a JSON string representation of the trace. An optional `pretty=True` parameter produces indented output for readability. ^[access-trace-data-databricks-on-aws.md]

```python
trace_json = trace.to_json()
print(f"JSON length: {len(trace_json)} characters")

trace_json_pretty = trace.to_json(pretty=True)
```

### Pandas DataFrame Conversion

The [`Trace.to_pandas_dataframe_row`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_pandas_dataframe_row) method returns a dictionary keyed by column names, suitable for appending as a row in a `pandas.DataFrame`. Multiple traces can be collected into a DataFrame for batch analysis. ^[access-trace-data-databricks-on-aws.md]

```python
row_data = trace.to_pandas_dataframe_row()
print(f"DataFrame row keys: {list(row_data.keys())}")

# Build a DataFrame from several traces
trace_rows = [t.to_pandas_dataframe_row() for t in traces]
df = pd.DataFrame(trace_rows)
print(f"DataFrame shape: {df.shape}")
```

### Span Conversion

Individual Span objects can be exported using `Span.to_dict()` and reconstructed from the resulting dictionary with `Span.from_dict(span_dict)`. ^[access-trace-data-databricks-on-aws.md]

```python
span_dict = span.to_dict()
reconstructed_span = Span.from_dict(span_dict)
```

## Reconstructing Traces

Traces exported as dictionaries or JSON strings can be rebuilt using the following class methods:

- `Trace.from_dict(trace_dict)` – reconstruct from a dictionary. ^[access-trace-data-databricks-on-aws.md]
- `Trace.from_json(trace_json)` – reconstruct from a JSON string. ^[access-trace-data-databricks-on-aws.md]

```python
from mlflow.entities import Trace

reconstructed_trace = Trace.from_dict(trace_dict)
reconstructed_trace = Trace.from_json(trace_json)
```

Both methods produce a fully functional `Trace` object whose metadata and span data match the original.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The overarching framework for capturing and inspecting execution traces.
- [Trace](/concepts/traces.md) – The central entity containing `TraceInfo` and `TraceData`.
- [TraceInfo](/concepts/traceinfo.md) – Metadata about a trace (ID, status, timestamps, tags, token usage, assessments).
- [TraceData](/concepts/tracedata.md) – Execution data including spans and full request/response payloads.
- Span – An individual unit of work within a trace, with start/end times, attributes, and status.
- Access Trace Data – How to read trace metadata, spans, assessments, and token usage.
- [Analyze Traces](/concepts/traces.md) – Practical examples of working with exported trace data.

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
