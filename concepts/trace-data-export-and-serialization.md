---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a1e537eaef3f43ff0b1682e6ade42e592bc95c8645ce4ea30d1c42903d7aba18
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-data-export-and-serialization
    - Serialization and Trace Data Export
    - TDEAS
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Trace Data Export and Serialization
description: Methods for converting MLflow Trace objects to dictionaries, JSON strings, and Pandas DataFrame rows for data portability and analysis.
tags:
  - mlflow
  - tracing
  - serialization
  - export
timestamp: "2026-06-19T21:57:02.099Z"
---

# Trace Data Export and Serialization

**Trace Data Export and Serialization** refers to the set of methods in the [MLflow Tracing](/concepts/mlflow-tracing.md) API that enable converting [Trace](/concepts/traces.md) and Span objects into portable formats—dictionaries, JSON strings, and Pandas DataFrame rows—as well as reconstructing trace objects from those formats. These capabilities allow users to store, transfer, and further process trace data outside the MLflow runtime. ^[access-trace-data-databricks-on-aws.md]

## Dictionary Conversion

The [`Trace.to_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_dict) method converts an entire `Trace` object to a dictionary. The returned dictionary contains top‑level keys `'info'` and `'data'`, each of which is itself a dictionary. Individual components can also be converted: `trace.info.to_dict()` and `trace.data.to_dict()` produce dictionaries for [TraceInfo](/concepts/traceinfo.md) and [TraceData](/concepts/tracedata.md) respectively. A trace can be reconstructed from a dictionary using `Trace.from_dict()`. ^[access-trace-data-databricks-on-aws.md]

```python
trace_dict = trace.to_dict()
print(f"Info keys: {trace_dict['info'].keys()}")
print(f"Data keys: {trace_dict['data'].keys()}")

info_dict = trace.info.to_dict()
data_dict = trace.data.to_dict()

from mlflow.entities import Trace
reconstructed_trace = Trace.from_dict(trace_dict)
print(f"Reconstructed trace ID: {reconstructed_trace.info.trace_id}")
```

## JSON Serialization

The [`Trace.to_json`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_json) method serializes a trace to a JSON string. It supports pretty‑printing via the `pretty=True` parameter. A trace can be loaded from a JSON string using `Trace.from_json()`. ^[access-trace-data-databricks-on-aws.md]

```python
trace_json = trace.to_json()
trace_json_pretty = trace.to_json(pretty=True)

from mlflow.entities import Trace
loaded_trace = Trace.from_json(trace_json)
print(f"Loaded trace ID: {loaded_trace.info.trace_id}")
```

## Pandas DataFrame Conversion

The [`Trace.to_pandas_dataframe_row`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_pandas_dataframe_row) method converts a single trace to a dictionary suitable for use as a row in a Pandas DataFrame. The returned dictionary contains keys such as `'trace_id'`, `'state'`, and `'execution_duration'`. Multiple traces can be aggregated into a DataFrame by calling this method for each trace and constructing a DataFrame from the list of rows. ^[access-trace-data-databricks-on-aws.md]

```python
row_data = trace.to_pandas_dataframe_row()
print(f"DataFrame row keys: {list(row_data.keys())}")

import pandas as pd
trace_rows = [t.to_pandas_dataframe_row() for t in traces]  # traces is a list of Trace objects
df = pd.DataFrame(trace_rows)
print(f"Trace IDs: {df['trace_id'].tolist()}")
print(f"States: {df['state'].tolist()}")
print(f"Durations: {df['execution_duration'].tolist()}")
```

## Span Conversion

Individual Span objects can be converted to and from dictionaries. The `Span.to_dict()` method returns a dictionary representation, and `Span.from_dict()` reconstructs a span from that dictionary. ^[access-trace-data-databricks-on-aws.md]

```python
span_dict = span.to_dict()
print(f"Span dict keys: {span_dict.keys()}")

from mlflow.entities import Span
reconstructed_span = Span.from_dict(span_dict)
print(f"Reconstructed span: {reconstructed_span.name}")
```

These methods allow traces and their components to be exported for downstream analysis, storage, and integration with other tools.

## Related Concepts

- [Trace](/concepts/traces.md) – The main object representing an entire traced execution.
- [TraceInfo](/concepts/traceinfo.md) – Metadata component of a trace (ID, status, timing, tags, token usage, assessments).
- [TraceData](/concepts/tracedata.md) – Execution data component (spans, request/response payloads).
- Span – An individual unit of work within a trace, also serializable.
- Pandas DataFrame – The data structure produced by `to_pandas_dataframe_row`.

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
